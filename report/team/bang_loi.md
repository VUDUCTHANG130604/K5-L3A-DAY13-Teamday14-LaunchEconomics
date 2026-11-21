# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_bank_rejected` với `reason = sai_so_tai_khoan`; cảnh báo khi vượt 1% số lệnh hoàn qua ngân hàng mỗi ngày | Kiểm tra độ dài số tài khoản theo từng ngân hàng trước khi tạo lệnh; hiện lại tên chủ tài khoản để khách xác nhận; ngân hàng từ chối thì nhắn khách nhập lại, không đóng yêu cầu | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: số `order_id` có từ 2 bản ghi hoàn tiền trong sổ cái; ngưỡng 0 ca | Khoá chống trùng (`order_id` + loại hoàn) ở bước ghi sổ cái; yêu cầu gửi lại thì trả trạng thái của lệnh đầu; nhắn "đang xử lý" ngay khi nhận yêu cầu để khách không gửi lại | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Tỉ lệ event `notification_sent` trong khung 22:00–07:00 và số phản ánh "làm phiền" theo tuần; ngưỡng 0,5% số thông báo bị phản ánh | Vẫn hoàn tiền ngay, nhưng thông báo trong khung 22:00–07:00 được xếp hàng gửi lúc 07:00 | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `input_unsupported` với `type = audio`, đếm theo tuần; vượt 3% số yêu cầu thì đưa chuyển giọng nói thành chữ vào lộ trình | Nói rõ chưa nghe được tin thoại, đưa nút chọn nhanh (mã vận đơn, lý do hoàn) hoặc chuyển nhân viên kèm file thoại | PM trợ lý hoàn phí |
| 12 | Ngầm | Token mỗi việc thành công và số lần gọi tool mỗi `trace_id`, theo depot, tính hằng ngày; cảnh báo khi một depot vượt 1,5 lần trung vị các depot 2 ngày liên tiếp | Kiểm tra lược đồ kết quả tool; thiếu trường thì ghi event `tool_response_incomplete` và dừng gọi lại thay vì thử mãi; sửa tool tra đơn của D05 | Kỹ sư trưởng agent |
