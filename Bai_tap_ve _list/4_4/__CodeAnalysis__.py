class py_solution:                      # Khởi tạo 1 lớp.
    def int_to_Roman(self, num):        # Khởi tạo 1 hàm với thuộc tính là num.
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [                         # Tạo 2 list.
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''                      # Tạo 1 string rỗng.
        i = 0                               # Tạo biến i = 0.
        while num > 0:                      # Tạo 1 vòng lặp while với điều kiện num > 0.
            for _ in range(num // val[i]):  # Tạo 1 vòng lặp for với giá trị '_' trong khoảng phần nguyên của phép chia.
                roman_num += syb[i]         # String roman_num = '' + thêm syb[i].
                num -= val[i]               # Thuộc tính num = num - val[i].
            i += 1                          # Biến i tăng thêm 1.
        return roman_num                    # Trả về roman_num


print(py_solution().int_to_Roman(1))        # Truyền đối tượng vào thuộc tính và in ra kết quả.
print(py_solution().int_to_Roman(4000))
