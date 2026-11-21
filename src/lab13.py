"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng / tháng
YC_THANG = 45_000            # yêu cầu hoàn phí / tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot (chọn sau A3)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng.
    Lần thứ i chỉ xảy ra khi i-1 lần trước đều sai: P = (1-p)^(i-1).
    E = Σ_{i=1..k} (1-p)^(i-1) = (1 - (1-p)^k) / p  (cấp số nhân); k → ∞ thì E = 1/p."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy = 1 - P(cả k lần đều sai)."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy
    = số lần chạy kỳ vọng / xác suất thành công. Thay công thức vào: (1-(1-p)^k)/p ÷ (1-(1-p)^k) = 1/p,
    tức không phụ thuộc k: chạy lại không làm rẻ đi hay đắt lên MỖI việc thành công (khi p cố định)."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét → gọi lại cho từng loại (A3) không cần lọc tay.
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Giới hạn số lần chạy: bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn
        # coi như chuyển nhân viên, không còn phút xem lại / làm lại của trợ lý.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=token,
        tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('inf'),
        hoa_don_moi_yc=(token + tool) / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để phát hiện chênh p1 → p2 (so hai tỉ lệ, kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    return 1 + (m - 1) * icc


def tieu_de(s):
    print(f'\n===== {s} =====')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ---------------- A2 ----------------
    tieu_de('A2 · Chi phí mỗi việc thành công (toàn bộ mẫu)')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    goc = ket_qua['cps']
    print(f"Số lần gọi tool       : {runs['tool_calls'].sum():,}")
    print(f"Phút xem lại [sim]    : {reqs['phut_xem_lai_simulated'].sum():,}")
    print(f"Phút làm lại [sim]    : {reqs['phut_lam_lai_simulated'].sum():,}")
    print(f"cps / hoá đơn mỗi yc  : {goc / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'Tỉ trọng {k:8s}      : {ket_qua[k] / ket_qua["tong"] * 100:5.1f}%')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    ca_he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000): '
          f'{ca_he_thong:,.0f} đ = {ca_he_thong / BASELINE:.2f}× [sim]')

    # ---------------- A3 ----------------
    tieu_de('A3 · Theo loại yêu cầu')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps[sim]':>10s} {'so 12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        so_chay = runs['request_id'].isin(sub['request_id']).sum()
        print(f"{loai:10s} {len(sub):6d} {kq['thanh_cong'] / len(sub) * 100:8.1f}% "
              f"{so_chay / len(sub):8.2f} {kq['cps']:10,.0f} {kq['cps'] / BASELINE:6.2f}×")

    print('\nTỉ lệ lần chạy ok theo loại × lần thử (chạy lại có giúp không?):')
    rl = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    rl['ok'] = (rl['status'] == 'ok').astype(int)
    print((rl.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100).round(1))

    # ---------------- A4 ----------------
    tieu_de('A4 · Cộng chi phí cố định cho phạm vi noi_dia + hang_nang')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    kq_pv = mo_hinh(runs, pv)
    tc_thang = YC_THANG * kq_pv['thanh_cong'] / len(reqs)
    for nhan, kl in [('đủ khối lượng', tc_thang), ('một nửa khối lượng', tc_thang / 2)]:
        co_dinh = CO_DINH_THANG / kl
        tong_cps = kq_pv['cps'] + co_dinh
        print(f"{nhan:20s}: việc TC/tháng {kl:,.0f} → cố định {co_dinh:,.0f} đ/việc; "
              f"cps phạm vi {kq_pv['cps']:,.0f} + cố định = {tong_cps:,.0f} đ = {tong_cps / BASELINE:.2f}× [sim]")
    print(f"(Tổng phạm vi {kq_pv['tong']:,.0f} đ / {kq_pv['thanh_cong']} việc thành công)")

    # ---------------- B1 ----------------
    tieu_de('B1 · Độ nhạy: đổi từng yếu tố')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print(f"{'Gốc (A2)':25s} {goc:8,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------------- B2 ----------------
    tieu_de('B2 · Đổi một cặp: giá token ×2 và xem lại ×2')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'{cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%) — bằng tổng hai tác động riêng vì mô hình cộng tuyến tính')

    # ---------------- B3 ----------------
    tieu_de('B3 · Giới hạn chạy lại: chi phí cả hệ thống')
    print(f"{'gioi_han':>8s} {'tong_tro_ly':>12s} {'khong_tc':>8s} {'ca_he_thong':>12s} {'cps':>7s}")
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        ktc = len(reqs) - kq['thanh_cong']
        print(f"{k:8d} {kq['tong']:12,.0f} {ktc:8d} {kq['tong'] + ktc * BASELINE:12,.0f} {kq['cps']:7,.0f}")

    # ---------------- B4 ----------------
    tieu_de('B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang')
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'Yêu cầu có ≥1 lần chạy ok: {co_ok} × 5 phút; ca lam_lai: {so_lam_lai}; token+tool: {token_tool_pv:,.0f} đ')
    for phut_ll in [9, tb_lam_lai]:
        tong = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + token_tool_pv
        cps = tong / kq_pv['thanh_cong']
        # Hoà vốn: phút xem lại x sao cho cps = 12.000
        hoa_von = (BASELINE * kq_pv['thanh_cong'] - so_lam_lai * phut_ll * LUONG_PHUT - token_tool_pv) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {phut_ll:4.1f} phút/ca: tổng {tong:,.0f} đ → {cps:,.0f} đ = {cps / BASELINE:.2f}× [sim]; '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')

    # ---------------- D1 ----------------
    tieu_de('D1 · Cỡ mẫu (baseline 0,70, alpha 0,05, power 0,8, ICC 0,02)')
    ICC = 0.02
    n5 = co_mau(0.70, 0.75)
    print(f'a · Theo yêu cầu, +5 điểm: {n5:,} yêu cầu mỗi nhóm')
    de75 = he_so_thiet_ke(75, ICC)
    n_nv = math.ceil(n5 * de75)   # cỡ mẫu luôn làm tròn lên
    print(f'b · Theo nhân viên, m=75: DE={de75:.2f}; n={n_nv:,.0f} → {math.ceil(n_nv / 75)} người/nhóm, '
          f'tổng {2 * math.ceil(n_nv / 75)} > 40 → không đủ người')
    print(f'c · 20 nhân viên/nhóm: tối đa c/ICC = {20 / ICC:,.0f} < {n5:,} → không đạt')
    print(f'd · 6 depot/nhóm: tối đa {6 / ICC:,.0f}')
    n6 = co_mau(0.70, 0.76)
    # 20m / (1 + (m-1)ICC) ≥ n6  ⇔  m (20 - n6·ICC) ≥ n6 (1 - ICC)
    m_min = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e · +6 điểm: {n6} mỗi nhóm; 20 người/nhóm cần m ≥ {m_min} yêu cầu/người '
          f'(DE {he_so_thiet_ke(m_min, ICC):.2f})')
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    pw = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05)
    print(f'Nếu thiết kế cho 6 điểm (n={n6}) mà tác động thật chỉ 5 điểm: power ≈ {pw:.2f}')

    # ---------------- D3 / E1 (số phụ trợ cho người giữ hồ sơ) ----------------
    tieu_de('D3 · Tỉ lệ mở lại 7 ngày hiện tại')
    print(f"Toàn mẫu: {reqs['mo_lai_trong_7_ngay'].mean() * 100:.2f}% ({reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)}); "
          f"phạm vi pilot: {pv['mo_lai_trong_7_ngay'].mean() * 100:.2f}%")

    tieu_de('E1 · Ba chỉ số trong đợt chạy thử')
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    print(f'Chính  : {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng   : bỏ qua gợi ý {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f"An toàn: mở lại 7 ngày {reqs['mo_lai_trong_7_ngay'].mean() * 100:.2f}%")
    print(f"Tỉ lệ làm lại trong phạm vi: {(pv['ket_qua'] == 'lam_lai').mean() * 100:.1f}%")
