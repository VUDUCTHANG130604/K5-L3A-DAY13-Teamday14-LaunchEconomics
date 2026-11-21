# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Teamday14 · L3A · Bản nháp trước duyệt chéo**

Mẫu chạy thử giả lập gồm **1.200 yêu cầu**, **1.624 lượt chạy** ở **6 depot**. Số liệu A, B, D1 và E1 được kiểm tra bằng cách chạy [lab13.py](../../src/lab13.py).

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc** trên 978 việc thành công, gấp **16,3 lần** hóa đơn token và tool trên mỗi yêu cầu (`simulated`). [Bảng chi phí A2](bang_chi_phi.md) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% làm chi phí tăng **23,1%** (`simulated`). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Chi phí hệ thống **5.865 đ/yêu cầu** (`simulated`), gồm 222 ca nhân viên làm thay, so với mốc giả định **12.000 đ/yêu cầu**. `noi_dia` và `hang_nang` lần lượt **2.696** và **8.221 đ/việc thành công** (`simulated`). | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đóng trong 24 giờ và không mở lại trong 7 ngày **82,83%** (994/1.200). Bỏ qua gợi ý **27,12%** (48/177 đã xem lại). Mở lại trong 7 ngày **4,25%** (51/1.200). | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Đối chiếu với nhãn AI trùng **17/20 ca (85%)**, lệch ở ca **8, 13 và 17**. Có **5 phương án** khắc phục, gồm khóa chống hoàn trùng ở ca 20. Đồng thuận chính thức cần hai bộ nhãn độc lập. [Bảng lỗi](bang_loi.md#bảng-đối-chiếu-nhãn) | Chưa | Người gắn nhãn 1 |
| 6 · Kế hoạch pilot | Để phát hiện chênh **5 điểm %**, chia theo yêu cầu cần **1.251 yêu cầu/nhánh**. Chia theo 20 nhân viên/nhánh có trần cỡ mẫu hiệu dụng 1.000. Đơn vị chia chưa chốt và có **0/3 luật dừng hoàn chỉnh**. [Kế hoạch pilot](pilot_plan.yaml) | Chưa | Người phụ trách pilot |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi làm chi phí tăng **51,8%** (`simulated`). Xem lại 100% khi làm lại mất 15,3 phút/ca cho chi phí **12.415 đ/việc** và hòa vốn nếu thời gian xem lại ≤ **4,8 phút/ca** (`simulated`). | Giả lập | Người phụ trách chỉ số |

Phạm vi đề xuất khi trình lại gồm `noi_dia` và `hang_nang`. `quoc_te` có chi phí **22.515 đ/việc thành công** (`simulated`) và `doi_tac` chỉ đạt **54,4%** thành công. Trước khi trình, chốt cách chia và 3 luật dừng kèm người có quyền dừng, tính đồng thuận từ hai bộ nhãn độc lập, và xác nhận ít nhất 6 event có `trace_id` để đo chỉ số pilot.

**Đề xuất Gate 2a · No-go với hồ sơ hiện tại.** Chi phí toàn mẫu thấp hơn mốc nhân viên tự làm, nhưng kịch bản xem lại 100% có thể vượt mốc chi phí và kế hoạch vẫn thiếu 3 luật dừng. Đề xuất này chờ nhóm xác nhận trước duyệt chéo.
