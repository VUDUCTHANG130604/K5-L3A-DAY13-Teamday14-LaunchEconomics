# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Bảng đối chiếu nhãn

Người gắn nhãn 1: Bùi Mạnh Linh · Người gắn nhãn 2: Vũ Đức Thắng (gắn riêng, không trao đổi trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Hệ thống | Không | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85% (đạt ngưỡng 80%, không cần viết lại định nghĩa). Ba ca không trùng: **8, 13, 17**.

Cách gắn nhãn: cả hai người đều dùng AI hỗ trợ (người 1 dùng Claude, người 2 dùng ChatGPT), đã ghi rõ ở báo cáo cá nhân. Đối chiếu nhãn thống nhất với bảng tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: khớp 20/20.

## Căn cứ gắn nhãn từng ca

Căn cứ theo mô tả trong phần “Hai mươi ca lỗi”. Ba ca lệch (8, 13, 17) do hai người diễn giải khác nhau về nguyên nhân gốc hoặc về việc lỗi đã lộ ra hay chưa. [Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx)

| Ca | Căn cứ gắn nhãn |
| --: | --- |
| 1 | Khách nhập số tài khoản thiếu hai chữ số, dẫn tới lệnh hoàn bị ngân hàng từ chối. |
| 2 | Trợ lý truyền tham số hàng thường cho kiện 28 kg nên tra sai bảng giá. |
| 3 | Hoàn về ví đúng thiết kế, trong khi khách chờ tiền vào tài khoản ngân hàng. |
| 4 | LogiX thiếu dữ liệu chặng giao do hãng nước ngoài thực hiện. |
| 5 | Kiểm tra mẫu mới phát hiện hoàn thừa theo giá trước giảm, dù khách và hệ thống đều không báo. |
| 6 | Khách chọn luồng giao trễ dù vấn đề thực tế là hàng bị vỡ. |
| 7 | Trợ lý báo hoàn thành dù API sổ cái thất bại và lệnh chưa được ghi. |
| 8 | Số tiền hoàn đúng, nên điều khoản bịa có thể lọt qua nếu chỉ kiểm số tiền. |
| 9 | Khách nhập mã đơn của sàn vào trường yêu cầu mã vận đơn. |
| 10 | Từ chối hoàn đúng điều khoản bất khả kháng, trong khi cam kết 24 giờ tạo kỳ vọng khác. |
| 11 | Trợ lý chưa hỗ trợ đầu vào bằng âm thanh. |
| 12 | Kết quả trả lời vẫn đúng nhưng các lần gọi tool thừa làm chi phí token tăng suốt ba tuần. |
| 13 | Trợ lý trả lời chung về phí vận chuyển và bỏ sót việc thông báo rằng yêu cầu hoàn phí bảo hiểm nằm ngoài phạm vi. |
| 14 | Khách bấm xác nhận đã nhận tiền trước khi tiền về. |
| 15 | Trợ lý tính hoàn 100% thay vì mức 50% theo chính sách. Nhân viên phát hiện trước khi gửi. |
| 16 | Thông báo gửi ngay đúng thiết kế nhưng đến lúc 2:14 sáng, gây phiền cho khách. |
| 17 | Bộ nhớ đệm dùng bản giá cũ sau ngày đổi giá, khiến số tiền hoàn trên 212 đơn sai. |
| 18 | Khoản hoàn đúng nhưng thiếu cách tính khiến khách hiểu số tiền được hoàn là thấp. |
| 19 | Đơn 14 tháng tuổi nằm ngoài phạm vi 12 tháng dữ liệu có thể truy cập. |
| 20 | Lệnh thứ hai thiếu khóa chống trùng, dẫn tới hai khoản hoàn cho cùng một đơn. |

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 → Hệ thống, không phải Ngầm:** trích dẫn "Điều 7.2" hiện ngay trong tin nhắn gửi khách nên lỗi đã lộ ra; Ngầm chỉ dùng khi cả khách lẫn hệ thống không ai thấy cho tới lúc kiểm tra mẫu.
- **Ca 13 → Giới hạn hệ thống, không phải Hệ thống:** nguyên nhân gốc là yêu cầu nằm ngoài phạm vi (phí bảo hiểm của đối tác); việc trợ lý không nói rõ mình không xử lý được là chỗ cần sửa, ghi ở cột khắc phục, không đổi nhãn.
- **Ca 17 → Ngầm, không phải Hệ thống:** dù gốc là bộ nhớ đệm giữ bảng giá cũ, 212 đơn lệch trong 9 ngày mà không khách nào mở lại và không cảnh báo nào kích, nên tiêu chí "có người thấy" quyết định nhãn là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_bank_rejected` với `reason = sai_so_tai_khoan`; cảnh báo khi vượt 1% số lệnh hoàn qua ngân hàng mỗi ngày | Kiểm tra độ dài số tài khoản theo từng ngân hàng trước khi tạo lệnh; hiện lại tên chủ tài khoản để khách xác nhận; ngân hàng từ chối thì nhắn khách nhập lại, không đóng yêu cầu | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: số `order_id` có từ 2 bản ghi hoàn tiền trong sổ cái; ngưỡng 0 ca | Khoá chống trùng (`order_id` + loại hoàn) ở bước ghi sổ cái; yêu cầu gửi lại thì trả trạng thái của lệnh đầu; nhắn "đang xử lý" ngay khi nhận yêu cầu để khách không gửi lại | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Tỉ lệ event `notification_sent` trong khung 22:00–07:00 và số phản ánh "làm phiền" theo tuần; ngưỡng 0,5% số thông báo bị phản ánh | Vẫn hoàn tiền ngay, nhưng thông báo trong khung 22:00–07:00 được xếp hàng gửi lúc 07:00 | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `input_unsupported` với `type = audio`, đếm theo tuần; vượt 3% số yêu cầu thì đưa chuyển giọng nói thành chữ vào lộ trình | Nói rõ chưa nghe được tin thoại, đưa nút chọn nhanh (mã vận đơn, lý do hoàn) hoặc chuyển nhân viên kèm file thoại | PM trợ lý hoàn phí |
| 12 | Ngầm | Token mỗi việc thành công và số lần gọi tool mỗi `trace_id`, theo depot, tính hằng ngày; cảnh báo khi một depot vượt 1,5 lần trung vị các depot 2 ngày liên tiếp | Kiểm tra lược đồ kết quả tool; thiếu trường thì ghi event `tool_response_incomplete` và dừng gọi lại thay vì thử mãi; sửa tool tra đơn của D05 | Kỹ sư trưởng agent |
