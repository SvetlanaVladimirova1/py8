#  В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

MIN_DATE = 1
MAX_YEAR = 9999
MAX_MONTH = 12
MAX_DAY = 31
def real_date(date: str) -> bool:
    format_date = list(map(int, date.split(".")))
    day, month, year = format_date
    if not(MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY):
        print(False)
        return False
    if month in (4, 6, 9, 11) and day > 30:
        print(False)
        return False
    if month == 2 and leap_year(year) and day > 29:
        print(False)
        return False
    if month == 2 and not leap_year(year) and day > 28:
        print(False)
        return False
    print(True)
    return True
def leap_year(year:int)->bool:
    return not(year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
if __name__=='__main__':
    x = (str(i) for i in argv[1:])
    real_date(*x)
