lessons_count = 20
lesson_price = 1500

discount = 0.1 if lessons_count >= 10 else 0

total_price = lessons_count * lesson_price * (1 - discount)

print(total_price)