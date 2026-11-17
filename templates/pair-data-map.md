# Mẫu: Bản đồ dữ liệu của trợ lý (dùng ở câu 2.2; mở lại khi thẻ sự cố liên quan dữ liệu)

*Phỏng theo Google PAIR Guidebook, worksheet **Data Collection + Evaluation**, bài tập 1 "Get to know your data"
(tiêu đề trong thân worksheet: "Map user needs to data requirements"; https://pair.withgoogle.com/guidebook tr. 2–3). Viết lại cho LogiX-VN, không chép nguyên văn.*

**Cách làm của worksheet:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Worksheet gốc viết cho việc huấn luyện model. Trợ lý LogiX không huấn luyện gì trong lab này, nên các dòng "dữ liệu huấn
luyện / đặc trưng / nhãn" được đổi thành "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật" (phần đổi là của LAB 10).

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | |
| Việc người dùng cần làm xong | |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | |
| Trường then chốt quyết định tiền và lỗi hãng | |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `__________`, `__________`, `__________` để giúp `__________` làm được `__________`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `__________`, `__________`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `__________`. Dấu hiệu nhìn thấy sớm nhất: `__________`.

→ Câu 2.2: lấy dòng "thế giới thật làm dữ liệu lệch" làm **ví dụ drift**: cái gì đổi, ngày nào, trường nào cho thấy, con số
nào của Bản tiêu chí bị ảnh hưởng.

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.
