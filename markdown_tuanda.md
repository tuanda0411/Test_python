## QA
# Q1 What is the difference between list and tuples in Python?
LIST  TUPLES
- thực hiện vòng lặp tốn thời gian hơn
- cho phép thay đổi
- dễ thực hiện các thao tác, chẳng hạn như chèn và xóa
-  tiêu tốn nhiều bộ nhớ hơn
- có phương thức tích hợp sẵn
- các thay đổi ko mong muốn có khả năng xảy ra hơn

TUPLES
- thực hiện vòng lặp nhanh hơn
- thích hợp để truy nhập các phần tử 
- không cho phép thay đổi
- Tiêu thụ ít bộ nhớ hơn so với danh sách
- ko có phương thức tích hợp sẵn
- ít có khả năng thay đổi hơn

# Q2 What are the key features of Python?
- dễ dàng code
- nhiều open source
- ngôn ngữ hướng đối tượng
- hỗ trợ chương trình giao diện.
- ngôn ngữ bậc cao
- tính năng mở rộng (viết được CT sang ngôn ngữ C or ngược lại).
- ngôn ngữ linh động (win, linux, unix, mac)
- Python là ngôn ngữ tích hợp(Python cũng là một ngôn ngữ Tích hợp vì chúng ta có thể dễ dàng tích hợp python với các ngôn ngữ khác như c, c ++)
- python thực thi từng dòng một.
- thư viện tiêu chuẩn lớn.
- ngôn ngữ nhập động. ko cần định dạng biến.

# Q3 What type of language is python?
- là loại ngôn ngữ bậc cao. hướng đối tượng.

# Q4 How is Python an interpreted language?
- Python được thực thi từng dòng một. Giống như các ngôn ngữ khác C, C ++, Java, v.v. không cần phải biên dịch python, điều này làm cho việc gỡ lỗi mã của chúng tôi trở nên dễ dàng hơn. 

# Q5 What is pep 8?
- là tài liệu cung cấp các hướng dẫn và phương pháp hay nhất về cách viết mã Python. Nó được viết vào năm 2001 bởi Guido van Rossum, Barry Warsaw và Nick Coghlan. Trọng tâm chính của PEP 8 là cải thiện khả năng đọc và tính nhất quán của mã Python.

# How is memory managed in Python?
- hầu như việc quản lý bộ nhớ sẽ do Python Memory Manager xử lý.
phần quan trọng nhất của quản lý bộ nhớ là memory allocation. Memory allocation có 2 loại:
Static Memory Allocation
Dynamic Memory Allocation

# Q7. What is name space in Python?
- một hệ thống đặt tên để tạo nên những cái tên độc nhất tránh sự mơ hồ.
- Namespace trong Python được thực hiện như cấu trúc dữ liệu dictionary, điều này có nghĩa là ánh xạ từ tên (keys) tới các đối tượng (values). Người sử dụng không phải biết điều này khi viết một chương trình Python khi sử dụng namespace
- Nhờ đó mà ta có thể nhận diện được các định danh (có thể cùng tên) dựa vào việc nó nằm trong namespace nào. Mỗi namespace có thời gian tồn tại và phạm vi sử dụng trong một chương trình là khác nhau tùy thuộc vào thời điểm chúng được tạo ra hoặc chúng là loại namespace nào

# Q8 What is PYTHON PATH?
- Các biến môi trường lưu trữ dữ liệu về một môi trường của hệ thống, để nó biết nơi cần tìm thông tin nhất định. Biến PATH là một trong những biến môi trường được biết đến nhiều nhất, vì nó tồn tại trên các máy Windows, Mac, Linux và thực hiện công việc trực tiếp với người dùng. Hình thức thực tế của PATH chỉ là một chuỗi văn bản chứa danh sách các đường dẫn thư mục mà hệ thống sẽ tìm kiếm mỗi khi bạn yêu cầu một chương trình
# Q9 
- là một đối tượng Python với các thuộc tính được đặt tên tùy ý mà bạn có thể liên kết và tham chiếu. ... Đơn giản, một mô-đun là một tệp bao gồm code Python. Một mô-đun có thể xác định các hàm, lớp và biến. Một mô-đun cũng có thể bao gồm mã chạy được

# Q10 
- một biến được khai báo bên ngoài hàm hoặc trong phạm vi toàn cục được gọi là biến toàn cục hay biến global. Biến toàn cục có thể được truy cập từ bên trong hoặc bên ngoài hàm.
- Biến được khai báo bên trong một hàm hoặc trong phạm vi cục bộ được gọi là biến cục bộ hay biến local
x = "Bien toàn cục"
def vidu():
 y = "Biến cục bộ"
vidu()
print(x)
print(y)

# Q11 What is __init__?
- Tất cả các lớp đều có một hàm gọi là __init __(), nó luôn luôn được thực hiện khi lớp đang được khởi tạo.
- Sử dụng hàm __init __() để gán giá trị cho các thuộc tính của đối tượng hoặc các hoạt động khác cần thiết khi đối tượng đang được khỏi tạo
- Các đối tượng cũng có thể chứa các phương thức. Phương thức trong đối tượng là các hàm thuộc về đối tượng

# Q12 What is self in Python?
- dùng để thể hiện lại chính class đang chứa nó, và dựa vào nó thì chúng ta có thể truy cập vào các phần tử đang có trong class hiện tại.