# Báo cáo cá nhân — Trần Quốc Tuấn - 2A202603561

## 1. Thông tin thành viên

- Họ tên: Trần Quốc Tuấn    
- MSSV: 2A202603561
- Email: trtuan.475@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code (CP1, CP2, trước giờ giải lao)

## 2. Phần việc phụ trách

- Cài môi trường (`src/.venv`, `requirements.txt`) và chạy `src/lab13.py`.
- Viết code cho Nhiệm vụ A (CP1) và Nhiệm vụ B (CP2) trong `src/lab13.py`, in số cho người kiểm số điền vào `report/team/bang_chi_phi.md`.
- Không điền bảng hồ sơ (phần của người kiểm số và người giữ hồ sơ).

## 3. Đóng góp cụ thể

- **A1:** viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`. Ba phép thử in ĐẠT (1,20 · 1,25 · 1,25). Hệ số chi phí = E[số lần chạy] ÷ P(thành công) = 1/p, không phụ thuộc k.
- **A2:** viết `mo_hinh(runs, reqs, …)`. Tử số cộng token + tool của mọi lần chạy, kể cả lần lỗi, cộng phút xem lại và làm lại × 2.000 đ [simulated]. Mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Hàm tự lọc `runs` theo `request_id` để gọi lại được cho từng loại. Có tham số `max_lan_chay` cho B1 và B3.
- **A3, A4:** gọi lại `mo_hinh` theo từng `loai`, in bảng tỉ lệ ok theo lần thử, và cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang ở hai mức khối lượng.
- **B1–B4:** 9 kịch bản độ nhạy, một kịch bản đổi một cặp, giới hạn 1/2/3 lần chạy kèm chi phí cả hệ thống, và kịch bản xem lại 100% kèm mức phút hoà vốn.

## 4. Bằng chứng

File `src/lab13.py`. Chạy `cd src && python lab13.py` in ra các số sau (khớp số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`):

| Mục | Con số |
|---|---|
| A2 · Chi phí mỗi việc thành công | 4.472 đ [simulated] = 4.373.585 đ ÷ 978; gấp 16,3 lần hoá đơn token + tool mỗi yêu cầu (274,7 đ) |
| A2 · Tỉ trọng | làm lại 51,8% [simulated], xem lại 40,7% [simulated], token 5,6%, tool 1,9% |
| A3 · cps theo loại [simulated] | noi_dia 2.696 đ (0,22×) · hang_nang 8.221 đ (0,69×) · quoc_te 22.515 đ (1,88×) · doi_tac 10.215 đ (0,85×) |
| A3 · quoc_te, tỉ lệ ok theo lần thử | 30,0% → 11,4% → 2,2%: chạy lại không giúp |
| A4 · Phạm vi + cố định | 3.414 + 1.185 = 4.599 đ = 0,38× [simulated]; một nửa khối lượng: 5.784 đ = 0,48× |
| B1 · Xếp hạng | làm lại ×2: +51,8% · xem lại ×2: +40,7% · lương +25%: +23,1% · token ×2: chỉ +5,6% |
| B2 | token ×2 cùng xem lại ×2: 6.543 đ (+46,3% = 5,6 + 40,7) [simulated] |
| B3 | Giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) [simulated]; giới hạn 1 lần có cps thấp nhất (4.111 đ) nhưng đẩy thêm 85 ca sang nhân viên |
| B4 | Xem lại 100%: 11.743 đ = 0,98× [simulated]; với 15,3 phút làm lại: 1,03×; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (≤ 4,8 phút) |

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và hướng dẫn trong repo, viết code `src/lab13.py`, giải thích công thức (cấp số nhân cho số lần chạy kỳ vọng, vì sao hệ số chi phí = 1/p).
- Cách tự kiểm tra: chạy ba phép thử A1; đối chiếu từng con số A2, A3, A4, B1–B4 với bảng số trong hướng dẫn chi tiết (sai số cho phép 2%); kiểm tra B1 bằng quy tắc "giảm một nửa = nửa mức tăng của gấp đôi".

## 6. Tự đánh giá

- Hoàn thành CP1 và CP2; số in ra khớp đáp án đối chiếu.
- Hiểu được hai ý chính: (1) chi phí thật gấp 16,3 lần hoá đơn token vì giờ nhân viên chiếm 92,5% tổng chi phí; (2) tối ưu riêng chi phí mỗi việc thành công (giới hạn 1 lần chạy) không phải là rẻ nhất cho công ty.
