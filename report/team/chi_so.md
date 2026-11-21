# Chỉ số và rủi ro kinh tế của pilot hoàn phí

## E1 · Chỉ số

Đơn vị phân tích là yêu cầu hoàn phí. Ba kết quả đầu mô tả 1.200 yêu cầu của đợt chạy thử. Pilot ghi cùng định nghĩa ở hai nhánh và so sánh trên các đoàn hệ có đủ thời gian quan sát.

| Loại | Chỉ số | Tử số / mẫu số | Đợt chạy thử |
| --- | --- | --- | ---: |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Yêu cầu đóng lần đầu trong 24 giờ kể từ khi tạo, không mở lại trong 7 ngày sau đóng / tất cả yêu cầu đủ điều kiện | 994/1.200 = **82,83%** |
| Dùng | Bỏ qua gợi ý | Yêu cầu có quyết định cuối là sửa hoặc bỏ / yêu cầu được xem lại | 48/177 = **27,12%** |
| An toàn | Mở lại trong 7 ngày | Yêu cầu có ít nhất một lần mở lại trong 7 ngày sau đóng / tất cả yêu cầu đủ điều kiện | 51/1.200 = **4,25%** |
| Dùng bổ sung | Tỉ lệ tiếp cận gợi ý | Yêu cầu có ít nhất một gợi ý được hiển thị / tất cả yêu cầu đủ điều kiện của nhánh trợ lý | Đo từ pilot |
| An toàn bổ sung | Hoàn sai số tiền | Đơn có số tiền thực ghi khác số tiền đúng theo chính sách / đơn đã kiểm tra trong mẫu ngẫu nhiên hằng tuần | Đo từ pilot |

## Event và cách tính

Mỗi bản ghi có `event_id` để loại bản gửi lại, `request_id` để đếm yêu cầu, `trace_id` để truy vết và thời điểm phát sinh. Cấp mã theo dõi ngay khi tạo yêu cầu, kể cả ở nhánh thủ công. Lưu `staff_id`, `depot`, `arm`, `loai` và điều kiện tham gia tại thời điểm tiếp nhận.

| Event | Bên ghi | Thuộc tính dùng để tính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Hệ thống ticket | trace_id, created_at, eligible, arm, staff_id, depot, loai | Nhận yêu cầu |
| agent_run_completed | Trợ lý | trace_id, attempt, status, tokens_in, tokens_out, tool_calls | Sau từng lượt, kể cả lượt lỗi |
| suggestion_shown | Giao diện CSKH | trace_id, suggestion_id, staff_id | Hiển thị gợi ý |
| review_decision | Giao diện CSKH | trace_id, decision (giu/sua/bo), review_minutes, is_final | Hoàn tất xem lại |
| rework_completed | Giao diện CSKH | trace_id, rework_minutes, reason | Hoàn tất làm lại |
| refund_ledger_write | Sổ cái | trace_id, order_id, refund_id, amount_vnd, status | Mỗi lần ghi lệnh hoàn |
| ticket_closed | Hệ thống ticket | trace_id, closed_at, outcome, manual_minutes | Đóng yêu cầu |
| ticket_reopened | Hệ thống ticket | trace_id, reopened_at, reason | Mở lại yêu cầu |
| audit_checked | Kế toán | trace_id, order_id, paid_vnd, correct_vnd | Sau kiểm tra mẫu hằng tuần |

**Đối chiếu.** Chỉ số chính và mở lại dùng ba event tạo, đóng và mở lại, mỗi yêu cầu tính một lần. Bỏ qua gợi ý dùng quyết định cuối trong `review_decision`. Tiếp cận dùng `suggestion_shown` nối với `refund_request_created`. Sai tiền dùng `audit_checked` đối soát với `refund_ledger_write`. Mẫu số bằng 0 thì ghi “chưa có quan sát”.

**Chi phí và luật dừng.** Cộng token và tool từ mọi lượt chạy, phút xem lại và làm lại đo từ giao diện, cùng phút xử lý thủ công còn lại. Mỗi phút chỉ tính một lần. Cộng phần cố định phân bổ rồi chia số yêu cầu đủ điều kiện. Đối soát theo `order_id` mỗi giờ để phát hiện nhiều khoản hoàn thành công cho cùng một nghĩa vụ hoàn.

## E2 · Rủi ro kinh tế

Các mức tác động lấy từ A4, B1 và B4 của [bảng chi phí](bang_chi_phi.md). Ngưỡng theo dõi dưới đây là ngưỡng đề xuất cho pilot.

| Rủi ro | Tác động | Dấu hiệu | Hành động | Phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng | Làm lại gấp đôi đưa chi phí lên 6.787 đ/việc, tăng 51,8% (simulated) | Ca làm lại vượt 7% trong tuần, so với mức 4,9% trong phạm vi chạy thử | Rà 20 trace làm lại và sửa nguyên nhân lặp lại nhiều nhất | PM trợ lý hoàn phí |
| Xem lại toàn bộ kéo dài | 11.743–12.415 đ/việc thành công khi làm lại mất 9–15,3 phút/ca (simulated) | Cuối tuần 2 vẫn xem lại hơn 50% yêu cầu, hoặc vượt 4,8 phút/ca ở kịch bản làm lại 15,3 phút | Đo thời gian thật và tính lại chi phí trước khi tăng phạm vi | Trưởng CSKH |
| Ít yêu cầu hơn dự báo | Giảm một nửa khối lượng làm phần cố định tăng từ 1.185 lên 2.370 đ/việc (phép tính A4) | Số việc thành công tuần dưới 50% kế hoạch | Dự báo lại chi phí đơn vị trước khi cam kết công suất | Giám đốc vận hành |
