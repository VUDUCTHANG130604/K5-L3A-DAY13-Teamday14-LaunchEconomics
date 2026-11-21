# Báo cáo cá nhân — Nguyễn Thị Hải Yến · 2A202603567

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Hải Yến
- MSSV: `2A202603567`
- Email: Cần bổ sung
- Vai trong nhóm: Người kiểm số (kiểm số, cỡ mẫu và chỉ số)

## 2. Phần việc phụ trách

- Chạy `src/lab13.py`, đối chiếu đầu ra với các bảng và điền `bang_chi_phi.md` (Nhiệm vụ A, B).
- Điền `chi_so.md`: đặc tả chỉ số E1, danh sách event có `trace_id`, kiểm tra chéo và rủi ro kinh tế E2.

## 3. Đóng góp cụ thể

- `bang_chi_phi.md` A3–B4: bảng 4 loại yêu cầu (`quoc_te` 22.515 đ = 1,88× baseline, chạy lại lần 2–3 chỉ ok 11,4% và 2,2%); chi phí cố định (0,38× ở đủ khối lượng, 0,48× ở một nửa); 9 kịch bản độ nhạy; giới hạn chạy lại (2 lần rẻ nhất cho cả hệ thống, 6.901.220 đ); xem lại 100% (0,98–1,03×) [simulated].
- Gộp bản A1–A2 của nhóm với bản của mình khi xung đột, giữ số đúng hơn sau khi tính lại.
- `chi_so.md`: ba chỉ số chạy thử (chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%), hai chỉ số tự đề xuất (phút xem lại trung vị, tỉ lệ hoàn tiền sai), 8 event và 4 rủi ro kinh tế lấy số từ B1.

## 4. Bằng chứng

- Commit `83e3065` (điền `bang_chi_phi.md`), `26cafa6` (gộp xung đột `bang_chi_phi.md`), `0d5b3a2` (điền `chi_so.md`).
- Số tự tính tay để đối chiếu:
  - Phần chi phí của lần chạy 2 và 3 tính lại từ `logix_runs.csv` là 93.804,488 đ, nên bảng ghi 93.804 (không phải 93.805).
  - Hoà vốn chi phí cố định ở A4: 40.000.000 ÷ (12.000 − 3.414) ≈ 4.660 việc thành công/tháng.
  - Chênh lệch ở B3 giữa giới hạn 1 lần và 2 lần: 7.449.781 − 6.901.220 = 548.561 đ.

## 5. Công cụ AI đã dùng

- Dùng Claude Code để chạy `lab13.py`, điền `bang_chi_phi.md` và `chi_so.md` từ đầu ra, và gộp xung đột git. Mỗi con số trong bảng được đối chiếu với dòng tương ứng trong `ket_qua.txt`. Ba số không có sẵn trong đầu ra (93.804, 4.660, 548.561) được tính lại riêng như ở mục 4.
- Các ngưỡng cảnh báo trong E2 (làm lại > 7%/tuần, phút xem lại trung vị > 4) là ngưỡng nhóm tự đặt, không tính từ dữ liệu.

## 6. Tự đánh giá

Các bảng A3–B4 và E1–E2 đã đủ số, có nhãn simulated và nối được với nguồn. Phần còn thiếu: chưa tự kiểm cỡ mẫu D1; người phụ trách trong E2 mới ghi theo vai, cần nhóm xác nhận tên.
