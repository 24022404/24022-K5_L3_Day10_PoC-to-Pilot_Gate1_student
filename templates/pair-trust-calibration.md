# Mẫu: Hiệu chỉnh lòng tin (dùng ở thẻ S7 và S8)

*Phỏng theo Google PAIR Guidebook, worksheet **Explainability + Trust**, bài tập 1 "Trust calibration"
(https://pair.withgoogle.com/guidebook tr. 2–5). Viết lại cho LogiX-VN, không chép nguyên văn.*

**Cách làm của worksheet:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm.

Thẻ **S7**: điền cho **người đặt hàng** (gõ ghi chú vào ticket) và **người nhận hàng** (không dùng hệ thống, không ký gì với LogiX).
Thẻ **S8**: thay hai nhóm trong bảng bằng **nhân viên duyệt** (kiểm quyết định của trợ lý) và **trưởng ca đứng tên duyệt**;
mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
 điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.
- (Thẻ S8) Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
 tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
