lessons_count = 20
lesson_price = 1500
discount = 0.1

print(f"Количество занятий: {lessons_count}")
print(f"Стоимость обучения: {lessons_count * lesson_price}")
print(f"Размер скидки: {discount * 100}%")
print(f"Итоговая стоимость: {lessons_count * lesson_price * (1 - discount)}")