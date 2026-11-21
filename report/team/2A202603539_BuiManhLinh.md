# Báo cáo cá nhân — Bùi Mạnh Linh · 2A202603539

## 1. Thông tin thành viên

- Họ tên: Bùi Mạnh Linh
- MSSV: 2A202603539
- Email: 26ai.linhbm@vinuni.edu.vn
- Nhóm: Teamday14
- Vai trong nhóm (người viết code, người kiểm số, Người gắn nhãn 1 (thành viên số 3), người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (thành viên số 3)

## 2. Phần việc phụ trách

- Nhiệm vụ C (CP3): gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, đối chiếu với người gắn nhãn 2 (Vũ Đức Thắng), tính tỉ lệ đồng thuận, viết quy tắc cho ca không trùng và bảng khắc phục 5 ca.
- Mục 5 của hồ sơ launch v0 (bảng lỗi và cách khắc phục).
- Duyệt chéo Gate 2a: phụ trách `phieu_cham.md` khi nhóm làm hội đồng chấm nhóm n + 1.
- Theo dõi điều kiện "Xong khi" của các checkpoint.

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca: Do người dùng 1, 6, 9, 14 · Hệ thống 2, 7, 8, 15, 20 · Ngữ cảnh 3, 10, 16, 18 · Giới hạn hệ thống 4, 11, 13, 19 · Ngầm 5, 12, 17.
- So với nhãn người 2: trùng **17/20 = 85%**, lệch ca 8, 13, 17. Viết quy tắc phân biệt: ca 8 (lỗi đã lộ ra nên là Hệ thống), ca 13 (ngoài phạm vi nên là Giới hạn dù xử lý kém), ca 17 (không ai nhận ra nên là Ngầm).
- Bảng khắc phục 5 ca, mỗi loại một ca (1, 20, 16, 11, 12), chọn khác bài mẫu. Mỗi dòng có event hoặc phép đối soát kèm ngưỡng và tần suất, cùng một vai trò phụ trách.
- Cập nhật mục 5 hồ sơ launch v0 và dòng "Lỗi và khắc phục" trong báo cáo nhóm theo kết quả đồng thuận.

## 4. Bằng chứng

- Commit `34ee7b4` (gắn nhãn 1) và các thay đổi sau đó trong [bang_loi.md](bang_loi.md).
- Mục 5 trong [ho_so_launch_v0.md](ho_so_launch_v0.md).
- Con số: đồng thuận 17/20 = 85%; nhãn thống nhất khớp bảng tham khảo 20/20.

## 5. Công cụ AI đã dùng

- Dùng Claude Code để đọc 20 ca trong đề bài `.docx`, đề xuất nhãn kèm lý do theo nguyên nhân gốc và soạn bảng khắc phục.
- Lưu ý: khi đọc hướng dẫn chi tiết, Claude đã thấy bảng nhãn tham khảo trước khi gắn, nên bộ nhãn người 1 không hoàn toàn độc lập với đáp án. Người gắn nhãn 2 cũng dùng AI (ChatGPT) và đã thấy bộ nhãn người 1 trong repo khi lập bảng.
- Tự kiểm tra: đọc lại từng ca theo câu hỏi nhận diện của mỗi loại (đầu vào của khách có sai không, có vi phạm thiết kế và có người thấy không, …); kiểm tra mỗi dòng khắc phục có ngưỡng đo được và không ghi "cả đội".

## 6. Tự đánh giá

Bảng lỗi đạt điều kiện "Xong khi" của CP3: có hai bộ nhãn, đồng thuận 85%, quy tắc cho ba ca lệch, bảng khắc phục đủ năm loại. Điểm yếu là hai bộ nhãn đều có AI hỗ trợ và không thật sự độc lập, nên con số 85% đánh giá thấp mức khó thật của việc gắn nhãn. Lần sau cần tự gắn bằng tay trước rồi mới dùng AI để soát.
