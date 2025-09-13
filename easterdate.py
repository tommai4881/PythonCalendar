"""
Tính Lễ Phục Sinh.
"""

from datetime import date, timedelta

def easter(y, cal = True):
    """
    Hàm tìm Lễ Phục Sinh theo thuật toán của Carl Friedrich Gauss.    
    Args:
        y (int): Năm dương lịch cần tính.
        cal (bool, mặc định True): Loại lịch.
            - Nếu True: Julian đến 1582, Gregorian từ 1583 trở đi (ie trường hợp Công giáo)
            - Nếu False: Julian (ie trường hợp Chính Thống)
    Returns:
        datetime.date: Ngày lễ Phục Sinh cần tìm (theo lịch Gregorian tính trước vì module datetime chỉ hỗ trợ Gregorian)
    """
    a = y % 19
    b = y % 4
    c = y % 7
    k = y // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    if cal: # Việt Nam không dùng lịch Julian nên ta quy ước lấy 15/10/1582.
        m = (15 - p + k - q) % 30 if y > 1582 else 15
        n = (4 + k - q) % 7 if y > 1582 else 6
    else:
        m = 15
        n = 6
    d = (19 * a + m) % 30
    if d == 29 or (d == 28 and a > 10): 
        # Xử lý ngoại lệ đ/v epact 24 và 25 đen (25 chỉ đen khi a > 10)
        d -= 1
    e = (2 * b + 4 * c + 6 * d + n) % 7
    March = d + e + 22
    April = d + e - 9
    if March > 32: f = date(y, 4, April)
    else: f = date(y, 3, March)
    # Chỉnh Julian (đ/b đối với Gregorian tính trước)
    j = k - k // 4 - 2 if not cal or y <= 1582 else 0
    return f + timedelta(j)

if __name__ == "__main__": # Ví dụ
    print(easter(date.today().year, False)) # Lễ Phục Sinh năm nay
