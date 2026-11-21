# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 ÷ 274,7) [simulated]. Nhìn hoá đơn token sẽ đánh giá thấp chi phí thật rất nhiều.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7%; giờ nhân viên chiếm 92,5%, token + tool chỉ 7,5%.

Chi phí cả hệ thống trên mỗi yêu cầu trước chi phí cố định bằng (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu** (simulated).

## A3 · Tách theo loại yêu cầu

Trong A3–B4, các giá trị chi phí có tính thời gian nhân viên và các tỉ lệ so sánh tương ứng mang nhãn **simulated**. Đơn vị tiền là đồng.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Quốc tế tốn 22.515 đ/việc (simulated). Tỉ lệ chạy OK ở lần thứ ba chỉ 2,2%.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong mẫu có 900 việc thành công thuộc phạm vi trên 1.200 yêu cầu toàn hệ thống. Phân bổ 40 triệu đ/tháng trên số việc thành công dự kiến.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở cả hai mức khối lượng, chi phí đã cộng cố định trên mỗi việc thành công vẫn dưới mốc 12.000 đ (simulated).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi % (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ/việc, tăng 46,3% (= 5,6% + 40,7%, simulated).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại ×2 (+51,8%) · 2. tỉ lệ xem lại ×2 (+40,7%) · 3. lương tăng 25% (+23,1%), theo các kịch bản B1 (simulated)

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Tối đa 2 lần cho tổng chi phí hệ thống thấp nhất (6.901.220 đ). Giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ), nhưng phải xử lý thủ công 319 yêu cầu (simulated).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 948 ca xem lại × 5 phút và 48 ca làm lại × 9 phút, chi phí là 11.743 đ/việc thành công. Nếu làm lại mất trung bình 15,3 phút/ca, chi phí lên 12.415 đ/việc (simulated, chưa cộng cố định).
- Kết quả này nói gì về thứ pilot cần học được? Đo phút xem lại và làm lại thực tế. Với mức làm lại 15,3 phút/ca, ngưỡng xem lại hòa vốn là khoảng 4,8 phút/ca theo mô hình B4 (simulated).
