first_code = "PYTHON-2026"
second_code = "GOLANG-2025"

name_slice = slice(0, 6)
year_slice = slice(-4, None)

print(first_code[name_slice])
print(second_code[name_slice])

print(first_code[year_slice])
print(second_code[year_slice])