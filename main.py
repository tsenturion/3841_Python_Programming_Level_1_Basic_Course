course_code = "PYTHON-2026"
digits_count = 0

for symbol in course_code:
    if symbol in "0123456789":
        digits_count += 1

print(f"Количество цифр: {digits_count}")