# Báo cáo cá nhân — Vũ Đức Thắng · 2A202603601

## 1. Thông tin thành viên

- Họ tên: Vũ Đức Thắng
- MSSV: `2A202603601`
- Email: Cần bổ sung
- Nhóm: Teamday14
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở CP3. Sau khi cả hai hoàn thành, đối chiếu với người gắn nhãn 1 và thống nhất nguyên nhân gốc cho các ca lệch.
- Cập nhật hồ sơ launch v0 từ các kết quả A–E, cùng nhóm chốt đề xuất Gate 2a và tổng hợp báo cáo nhóm.

## 3. Đóng góp cụ thể

- Tổng hợp chi phí, độ nhạy, cỡ mẫu và ba chỉ số chạy thử vào hồ sơ launch từ kết quả `lab13.py`. Ghi rõ phần đồng thuận và luật dừng còn chờ hoàn tất.
- Cập nhật báo cáo nhóm với kết quả chính và bằng chứng xử lý lỗi chạy lab trên PowerShell. Ghi đề xuất No-go cho vòng duyệt hiện tại để nhóm xác nhận.
- Ghi căn cứ gắn nhãn cho 20 ca trong bảng đối chiếu AI và tóm tắt biện pháp chống hoàn trùng ở mục 5 của hồ sơ. [Bảng đối chiếu](bang_loi.md#đối-chiếu-với-nhãn-đề-xuất-của-ai)

## 4. Bằng chứng

- Bản nháp lưu trong [hồ sơ launch v0](ho_so_launch_v0.md) và [báo cáo nhóm](group_report.md).
- Đối chiếu tham khảo với nhãn AI trùng **17/20 ca (85%)**. Ba ca lệch **8, 13 và 17** có quy tắc phân biệt và nhãn thống nhất dự thảo. [Bảng lỗi](bang_loi.md)

## 5. Công cụ AI đã dùng

- Dùng ChatGPT để soạn bản nháp và đối chiếu số trong hồ sơ với đầu ra của `lab13.py` chạy từ `src/`. Các số đầu vào được kiểm tra bằng cách đếm dòng trong hai CSV và đếm depot phân biệt. Kết quả sau cập nhật ghi nhận **3/3 phép thử A1 đạt**.
- Dùng ChatGPT để đề xuất nhãn dựa trên mô tả ca và nguyên nhân gốc. Khi lập bảng AI, bộ nhãn người gắn nhãn 1 đã có sẵn trong repo. Kết quả được kiểm tra bằng cách so từng ca theo số thứ tự.

## 6. Tự đánh giá

Phần tổng hợp nối được số liệu với nguồn và lý do đề xuất No-go. Bảng lỗi có căn cứ cho 20 nhãn dự thảo. Phần cần hoàn tất ở CP3 là đối chiếu bộ nhãn do thành viên thứ hai tự gắn và ghi nguyên nhân gốc cho các ca có ý kiến khác nhau.
