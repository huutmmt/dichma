from flask import Flask, render_template, request

app = Flask(__name__)

def substitution(input_text, key):
    # Thực hiện mã hóa thay thế ở đây và trả về kết quả
    result = ""
    for char in input_text:
        # Thực hiện logic mã hóa thay thế dựa trên key
        # Ví dụ đơn giản: thay thế mỗi ký tự 'a' thành 'b'
        if char == 'a':
            result += 'b'
        else:
            result += char
    return result

def encrypt_affine(input_text, key1, key2):
    # Thực hiện mã hóa affine ở đây và trả về kết quả
    result = ""
    for char in input_text:
        # Thực hiện logic mã hóa affine dựa trên key1 và key2
        # Ví dụ đơn giản: sử dụng công thức mã hóa affine
        # (Ax + B) mod 26 với x là vị trí ký tự trong bảng chữ cái
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            x = ord(char) - ord('a')
            encrypted_char = chr(((key1 * x + key2) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
        else:
            result += char
    return result

def decrypt_affine(encrypted_text, key1, key2):
    # Thực hiện giải mã affine ở đây và trả về kết quả
    result = ""
    for char in encrypted_text:
        # Thực hiện logic giải mã affine dựa trên key1 và key2
        # Ví dụ đơn giản: sử dụng công thức giải mã affine
        # x = (A^(-1) * (y - B)) mod 26 với y là vị trí ký tự trong bảng chữ cái
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            y = ord(char) - ord('a')
            # Tìm phần tử nghịch đảo của key1 (nếu tồn tại)
            mod_inverse = None
            for i in range(26):
                if (key1 * i) % 26 == 1:
                    mod_inverse = i
                    break
            if mod_inverse is not None:
                decrypted_char = chr(((mod_inverse * (y - key2)) % 26) + ord('a'))
                if is_upper:
                    decrypted_char = decrypted_char.upper()
                result += decrypted_char
            else:
                # Nếu không tồn tại phần tử nghịch đảo, không giải mã được
                result += char
        else:
            result += char
    return result


@app.route('/')
def home():
    # Trả về trang chủ
    return render_template('home.html')

@app.route('/substitution', methods=['GET', 'POST'])
def substitution_route():
    encrypted_text = None  # Khởi tạo giá trị mặc định
    if request.method == 'POST':
        # Nhận dữ liệu từ biểu mẫu
        input_text = request.form['input']
        key = request.form['key']

        # Thực hiện lập mã ở đây
        try:
            encrypted_text = substitution(input_text, key)
        except Exception as e:
            error_message = str(e)
            return render_template('substitution.html', error_message=error_message)

    return render_template('substitution.html', encrypted_text=encrypted_text)

@app.route('/affine', methods=['GET', 'POST'])
def affine():
    encrypted_text = decrypted_text = None  # Khởi tạo giá trị mặc định
    if request.method == 'POST':
        # Nhận dữ liệu từ biểu mẫu
        input_text = request.form['input']
        key1 = int(request.form['key1'])
        key2 = int(request.form['key2'])

        # Thực hiện lập mã và giải mã ở đây
        try:
            encrypted_text = encrypt_affine(input_text, key1, key2)
            decrypted_text = decrypt_affine(encrypted_text, key1, key2)
        except Exception as e:
            error_message = str(e)
            return render_template('affine.html', error_message=error_message)

    return render_template('affine.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
