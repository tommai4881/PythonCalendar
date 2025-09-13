"""
Tìm Chúa Nhật sau hay trùng đúng một ngày.
"""

from datetime import date, timedelta

def sunday(day: date):
    """
    Tìm Chúa Nhật sau hay trùng đúng một ngày.
    Args:
        date (datetime.date): Ngày bạn nhập.
    Returns:
        datetime.date: Ngày Chúa Nhật cần tìm.
    """
    return day + timedelta(6 - day.weekday())

if __name__ == "__main__":
    # Ví dụ tìm ngày Chúa Nhật sau hay trùng ngày hôm nay.
    print(sunday(date.today()))