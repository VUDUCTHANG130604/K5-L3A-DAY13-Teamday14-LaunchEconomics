# Team

## Thông tin nhóm

- Tên nhóm: Teamday14
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Teamday14-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/VUDUCTHANG130604/K5-L3A-DAY13-Teamday14-LaunchEconomics · `main` · (điền khi chốt)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |Trần Quốc Tuấn       |2A202603561      |trtuan.475@gmail.com       |trtuan475        |Nguời viết code        |
|   2 | Nguyễn Thị Hải Yến | 2A202603567 |       | Jennguyen106 | Kiểm số, cỡ mẫu và chỉ số |
|   3 | Bùi Mạnh Linh | 2A202603539 |       |        | Người gắn nhãn 1 |
|   4 | Vũ Đức Thắng | 2A202603601 |       |        | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## Trần Quốc Tuấn · 2A202603561

### Phần việc phụ trách

- Người viết code trước giờ giải lao (CP1, CP2): cài môi trường, viết và chạy `src/lab13.py` cho Nhiệm vụ A và B, in số để người kiểm số điền `bang_chi_phi.md`.

### Đóng góp cụ thể

- A1: ba hàm số lần chạy kỳ vọng, tỉ lệ thành công, hệ số chi phí (= 1/p); ba phép thử ĐẠT (1,20 · 1,25 · 1,25).
- A2–A4: hàm `mo_hinh` (tử số tính mọi lần chạy, mẫu số chỉ đếm `thanh_cong`): 4.472 đ/việc thành công [simulated], gấp 16,3 lần hoá đơn token; tách theo loại (quoc_te 1,88×); cộng chi phí cố định cho noi_dia + hang_nang: 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy (làm lại +51,8% > xem lại +40,7% > lương +23,1%), cặp token + xem lại +46,3%, giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ), xem lại 100%: 0,98× [simulated].

### Bằng chứng

- [`src/lab13.py`](src/lab13.py), commit `785090b`, [báo cáo cá nhân](report/team/2A202603561_TranQuocTuan.md).

## Nguyễn Thị Hải Yến · 2A202603567

### Phần việc phụ trách

- Người kiểm số: chạy `src/lab13.py`, đối chiếu đầu ra và điền `bang_chi_phi.md` (A, B) và `chi_so.md` (E1, E2).

### Đóng góp cụ thể

- `bang_chi_phi.md` A3–B4: `quoc_te` 1,88× baseline nên để ngoài phạm vi; chi phí cố định 0,38×–0,48×; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% lên 0,98–1,03× [simulated].
- `chi_so.md`: ba chỉ số chạy thử (82,83% · 27,12% · 4,25%), 2 chỉ số tự đề xuất, 8 event có `trace_id`, 4 rủi ro kinh tế.
- Tính lại phần chi phí lần chạy 2–3 từ `logix_runs.csv` (93.804,488 đ) để chốt số đúng khi gộp xung đột.

### Bằng chứng

- Commit `83e3065`, `26cafa6`, `0d5b3a2`, [báo cáo cá nhân](report/team/2A202603567_NguyenThiHaiYen.md).

## Vũ Đức Thắng · 2A202603601

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca ở CP3, giữ hồ sơ launch v0 và tổng hợp báo cáo nhóm.

### Đóng góp cụ thể

- Bản nháp cho vai người 4 đã tổng hợp chi phí, độ nhạy, cỡ mẫu và ba chỉ số chạy thử từ kết quả `lab13.py`. Báo cáo nhóm ghi lại lỗi PowerShell và kết quả chạy lại với 3/3 phép thử A1 đạt.
- Tổng hợp đối chiếu tham khảo 20 ca giữa nhãn AI và người 3, cùng biện pháp chống hoàn trùng. Cần bổ sung kết quả đồng thuận từ hai bộ nhãn độc lập và phản hồi duyệt chéo. [Bảng lỗi](report/team/bang_loi.md)

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202603601_VuDucThang.md), [hồ sơ launch v0](report/team/ho_so_launch_v0.md) và [báo cáo nhóm](report/team/group_report.md).

## Bùi Mạnh Linh · 2A202603539

### Phần việc phụ trách

- Người gắn nhãn 1: gắn nhãn 20 ca ở CP3, đối chiếu với người gắn nhãn 2, viết quy tắc cho ca lệch và bảng khắc phục 5 ca; phụ trách `phieu_cham.md` khi duyệt chéo.

### Đóng góp cụ thể

- Hai bộ nhãn trùng 17/20 (85%), quy tắc cho ca 8, 13, 17; bảng khắc phục 5 ca đủ năm loại; cập nhật mục 5 hồ sơ launch v0.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md), [báo cáo cá nhân](report/team/2A202603539_BuiManhLinh.md), commit `34ee7b4`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
