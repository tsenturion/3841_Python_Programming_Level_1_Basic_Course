course_code = "PYTHON"
search_symbol = "T"

for symbol in course_code:
    if symbol == search_symbol:
        print("Символ найден")
        break
else:
    print("Символ отсутствует")