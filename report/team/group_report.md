# Báo cáo nhóm

**Bản nháp trước duyệt chéo Gate 2a**

## 1. Thông tin nhóm

- Tên nhóm **Teamday14**, lớp **L3A**.
- Repo `K5-L3A-DAY13-Teamday14-LaunchEconomics`. [Thông tin thành viên](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí trợ lý hoàn phí LogiX-VN, khả năng nhân viên sử dụng, các lỗi cần khắc phục và thiết kế pilot có đối chứng. Phân tích mẫu giả lập gồm 1.200 yêu cầu và 1.624 lượt chạy từ đợt chạy thử hai tuần ở 6 depot. [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)

## 3. Giải pháp

| Nhiệm vụ | Cách tiếp cận | Bằng chứng |
| --- | --- | --- |
| A · Chi phí | Tính chi phí của mọi lượt chạy và thời gian nhân viên, chia cho số việc thành công. Tách theo loại yêu cầu và xét chi phí cố định. | [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Thay từng yếu tố chi phí, so giới hạn 1–3 lượt chạy và kiểm tra kịch bản xem lại 100%. | [Bảng độ nhạy](bang_chi_phi.md) |
| C · Lỗi | Hai thành viên gắn nhãn độc lập 20 ca, tính đồng thuận rồi chọn 5 ca đại diện để đề xuất cách phát hiện và khắc phục. | [Bảng lỗi](bang_loi.md) |
| D · Pilot | Tính cỡ mẫu theo phương án chia, chọn nhóm đối chứng đồng thời và đặt trước luật dừng về an toàn, chi phí và mức sử dụng. | [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và rủi ro | Đặc tả chỉ số chính, chỉ số dùng và chỉ số an toàn, nối các event bằng `trace_id` và lấy tác động kinh tế từ bảng độ nhạy. | [Chỉ số và rủi ro](chi_so.md) |

## 4. Kết quả

- Dữ liệu đầu vào đã đối chiếu **1.200 dòng yêu cầu, 1.624 dòng lượt chạy và 6 depot phân biệt** trong hai file CSV. Mốc nhân viên tự làm là **12.000 đ/yêu cầu** theo giả định của lab (6 phút × 2.000 đ). [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- **Chi phí (`simulated`).** Mô hình cho **4.472 đ/việc thành công** và **5.865 đ/yêu cầu** khi cộng phần 222 ca nhân viên làm thay. Chi phí làm lại chiếm **51,8%** tổng chi phí. Ở phạm vi `noi_dia` và `hang_nang`, chi phí gồm cố định tăng từ **4.599** lên **5.784 đ/việc thành công** khi khối lượng giảm một nửa. [Bảng chi phí A2](bang_chi_phi.md), [kết quả từ mã A–B](../../src/lab13.py)
- **Chỉ số chạy thử.** Đóng trong 24 giờ và không mở lại trong 7 ngày **82,83%**, bỏ qua gợi ý **27,12%** trong số ca được xem lại, mở lại trong 7 ngày **4,25%**. [Kết quả E1](../../src/lab13.py)
- **Lỗi và khắc phục.** Hai bộ nhãn trùng **17/20 ca (85%)**, đạt ngưỡng 80%. Bảng lỗi có quy tắc phân biệt cho ba ca lệch **8, 13 và 17**; nhãn thống nhất khớp bảng tham khảo 20/20. Ca 20 cần khóa chống trùng ở bước ghi sổ cái để tránh hoàn hai lần. [Bảng lỗi](bang_loi.md)
- **Đề xuất dự thảo No-go ở vòng này.** Phạm vi để trình lại là `noi_dia` và `hang_nang`. Phương án chia theo yêu cầu cần **1.251 yêu cầu/nhánh** để phát hiện chênh 5 điểm %. Nhóm cần chốt phương án chia, điền đủ 3 luật dừng và xác nhận đặc tả ít nhất 6 event có `trace_id`. [Hồ sơ launch v0](ho_so_launch_v0.md)
- Phản hồi duyệt chéo của hội đồng đối với Teamday14 sẽ được bổ sung sau buổi duyệt.

## 5. Khó khăn và cách xử lý

- Lệnh `source .venv/bin/activate` trong PowerShell báo `CommandNotFoundException`. Chạy trực tiếp `.\.venv\Scripts\python.exe --version` từ `src/` đã xác nhận Python 3.11.9.
- Bản khởi đầu dừng ở A1 với `NotImplementedError`. Sau cập nhật, chạy `.\.venv\Scripts\python.exe -X utf8 lab13.py` từ `src/` đã qua **3/3 phép thử A1** và in các kết quả A–B, D1 và E1. [Code phân tích](../../src/lab13.py)

## 6. Tổng hợp đóng góp

- Vai người 4 gồm gắn nhãn độc lập ở CP3, giữ hồ sơ launch và tổng hợp báo cáo nhóm. Các đóng góp đã thực hiện và bằng chứng được cập nhật theo từng thành viên. [Thông tin nhóm](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử thiếu nhóm đối chứng, nên các chỉ số mô tả kết quả quan sát trong mẫu. Pilot cần đối chứng đồng thời để ước lượng tác động của trợ lý. Sau khi có dữ liệu pilot, thay phút xem lại và làm lại `simulated` bằng thời gian đo thực tế rồi tính lại chi phí. [Đặc tả chỉ số](chi_so.md)

## 8. Tài liệu tham khảo

- [Đề bài Lab 13](../../README.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [checkpoint](../../CHECKPOINTS.md) và [rubric Gate 2a](../../RUBRIC.md).
