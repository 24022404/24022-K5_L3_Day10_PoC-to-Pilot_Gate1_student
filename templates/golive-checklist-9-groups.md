# Mẫu: Checklist go-live 9 nhóm việc

*Chín nhóm việc, bốn cột và ba trạng thái theo deck học viên trang 61. Cột "Bằng chứng lấy từ
đâu" trỏ tới phiếu bàn đã điền ở bước khác của lab; không điền thêm worksheet nào chỉ để lấp cột này.*

**Bàn:** ______ · **Thẻ đã bốc:** ___

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file, hoặc số trong report.
Điền lần 1 ở vòng 1 (phút 50–75). Cập nhật sau sự cố (phút 155–185).
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi `error-audit.md` | | | | |
| 2 | Dữ liệu | Bản đồ dữ liệu `pair-data-map.md` (câu 2.2): trường nào là nguồn sự thật, trường nào là bản sao | | | | |
| 3 | Bảo mật | Một vòng HAZOP với guideword PERTURBED (`hazop.md`): chữ nào đi vào model mà không do LogiX viết | | | | |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S8, S2 có thêm `pair-control-map.md` | | | | |
| 5 | Hiệu năng, hạ tầng | Đội tự ước tính; HAZOP guideword INCAPABLE: LLM không trả lời thì sao; số người duyệt và số ca mỗi giờ | | | | |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report: chi phí mỗi ticket so với làm tay, ROI, tiền LLM ticket đắt nhất; `config/operating_gates.json` mục `business` | | | | |
| 7 | Vận hành | `templates/runbook.md` + `config/operating_gates.json` mục `operations` (PIC, người duyệt, số người trực, điều kiện dừng, kênh báo tin) + metric trong `monitors.py` | | | | |
| 8 | Con người, pháp lý | Bên thứ ba (hãng, tài xế, shop, người nhận quà, người đứng tên duyệt); `config/operating_gates.json` mục `legal`; thẻ S6 có `pair-mental-models.md`, thẻ S7 và S8 có `pair-trust-calibration.md` | | | | |
| 9 | Quyết định | `pair-success-criteria.md` + hash Bản tiêu chí đã ký + `gate1-decision.md` | | | | |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register.
