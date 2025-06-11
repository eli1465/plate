import re


# تابع تولید پلاک
def plate_generator(p1, p2, p3, p4):
    return f"{p1}{p2}{p3} ایران {p4}"


# تابع بررسی صحت پلاک
def plate_validator(plate):
    pattern = r"^\d{2}[آ-ی]\d{3} ایران \d{2}$"
    return bool(re.match(pattern, plate))

