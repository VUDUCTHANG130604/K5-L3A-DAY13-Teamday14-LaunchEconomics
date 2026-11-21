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

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [sim] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [sim] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [sim] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [sim] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te`: 22.515 đ/việc = 1,88× baseline [sim]. Chạy lại gần như vô ích: tỉ lệ ok lần 1 là 30,0%, lần 2 là 11,4%, lần 3 là 2,2%. `doi_tac` (0,85×, lần 2–3 chỉ 18,2%/14,8%) cũng sát ngưỡng, nên để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [sim] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [sim] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi: kể cả ở một nửa khối lượng vẫn chỉ 0,48× baseline [sim]. Hoà vốn (12.000 đ) cần cố định ≤ 8.586 đ/việc, tức khoảng 4.660 việc thành công/tháng (~14% khối lượng đầy đủ).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | -5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | -8,1% |

(Tất cả chi phí mỗi việc thành công ở bảng trên đều là simulated, đơn vị đồng.)

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [sim], đúng bằng +5,6% + 40,7% vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1% khi tăng 25%). Giá token chỉ ±5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

(Chi phí cả hệ thống = tổng chi phí trợ lý + số yêu cầu không thành công × 12.000 đ; đều là simulated.)

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Rẻ nhất cho công ty là tối đa 2 lần (6.901.220 đ). Không trùng: chi phí mỗi việc thành công thấp nhất ở 1 lần (4.111 đ) nhưng đẩy thêm 97 ca cho nhân viên, nên cả hệ thống đắt hơn 548.561 đ [sim].

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 11.743 đ = 0,98× (làm lại 9 phút/ca) đến 12.415 đ = 1,03× (làm lại 15,3 phút/ca) [sim]. Hoà vốn chỉ khi xem lại ≤ 4,8–5,1 phút/yêu cầu.
- Kết quả này nói gì về thứ pilot cần học được? Lợi thế chi phí nằm hết ở chỗ không phải xem lại mọi việc. Pilot phải đo được số phút xem lại thật và tỉ lệ được phép bỏ xem lại (vẫn giữ mở lại 7 ngày ≤ 4,25%). Token không phải biến quyết định.
