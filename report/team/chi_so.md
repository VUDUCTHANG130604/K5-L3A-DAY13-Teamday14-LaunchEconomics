# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); phạm vi pilot 3,97% |
| Dùng | Nhóm tự đề xuất: Số phút xem lại trung vị mỗi yêu cầu được xem lại | Trung vị `phut_xem_lai` của event `review_decision` | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ hoàn tiền sai (hoàn trùng hoặc số tiền hoàn khác số được duyệt) | Số `refund_issued` trùng `request_id`, hoặc có `so_tien_vnd` khác `so_tien_duyet`, chia tổng số `refund_issued` | Không cần tính |

Chỉ số trong đợt chạy thử là: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%. Đợt chạy thử không có nhóm đối chứng nên không kết luận trợ lý đã nâng chỉ số nào.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống ticket | request_id, loai, depot, so_tien_vnd, created_at, trace_id | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý (agent) | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion` | Trợ lý (agent) | request_id, ket_qua (thanh_cong / chuyen_nhan_vien), so_lan_chay, so_tien_de_xuat, trace_id | Khi trợ lý chốt gợi ý hoặc chuyển nhân viên |
| `review_decision` | Nhân viên xem lại | request_id, staff_id, quyet_dinh_xem_lai (giu / sua / bo), phut_xem_lai, so_tien_duyet, trace_id | Khi nhân viên bấm duyệt, sửa hoặc bỏ gợi ý |
| `rework_done` | Nhân viên | request_id, staff_id, phut_lam_lai, ly_do, trace_id | Khi nhân viên làm lại xong một ca hỏng |
| `refund_issued` | Hệ thống thanh toán | request_id, so_tien_vnd, issued_at, trace_id | Khi tiền hoàn được chuyển cho khách |
| `request_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi yêu cầu được đóng |
| `request_reopened` | Hệ thống ticket | request_id, reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `request_created` và `request_closed` (closed_at − created_at ≤ 24 giờ), không có `request_reopened` trong 7 ngày sau closed_at → đo được.
- Dùng (bỏ qua gợi ý): `review_decision` có quyết định `sua` hoặc `bo`, chia tổng số `review_decision` → đo được.
- An toàn (lỗi lọt đến khách): số `request_reopened` trong 7 ngày, chia số `request_created` → đo được.
- Dùng (đề xuất, phút xem lại): `review_decision.phut_xem_lai` → đo được.
- An toàn (đề xuất, hoàn sai): `refund_issued` đối chiếu với `review_decision.so_tien_duyet` theo `request_id` → đo được.
- Chi phí mỗi việc thành công: `agent_run_completed` (token, tool) + `review_decision` + `rework_done` (phút) + `agent_suggestion` (thành công) → đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Làm lại gấp đôi: chi phí mỗi việc thành công lên 6.787 đ (+51,8%) [sim], vẫn 0,57× baseline | Tỉ lệ `rework_done` trong phạm vi vượt 7% mỗi tuần (hiện 4,9%) | Tách ca làm lại theo loại lỗi trong `bang_loi.md`; nếu do `hang_nang` thì thu hẹp phạm vi về `noi_dia` | Người kiểm số |
| Phải xem lại nhiều hơn / xem lại lâu hơn | Xem lại gấp đôi: 6.292 đ (+40,7%) [sim]; xem lại 100%: 0,98–1,03× baseline, hoà vốn khi ≤ 4,8–5,1 phút/yêu cầu | Trung vị `phut_xem_lai` > 4 phút, hoặc tỉ lệ bỏ qua gợi ý > 27% | Chuyển sang xem lại theo mẫu cho `noi_dia`; xem lại toàn bộ chỉ cho ca có số tiền lớn | Người gắn nhãn 2 kiêm giữ hồ sơ |
| Lương nhân viên tăng | Lương +25%: 5.506 đ (+23,1%) [sim], vẫn 0,46× baseline | Đơn giá phút nhân viên trong bảng lương quý | Cập nhật `LUONG_PHUT` và chạy lại `lab13.py`; chưa cần đổi phạm vi | Người viết code |
| Giá token tăng | Giá token gấp đôi: 4.723 đ (+5,6%) [sim] | Hoá đơn token + tool mỗi yêu cầu vượt 275 đ | Chỉ theo dõi; không phải biến quyết định | Người viết code |
