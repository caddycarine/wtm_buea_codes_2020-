def leap_year(year):
    if (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)):
        return True
    return False
