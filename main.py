lesson_number = 1
lesson_duration = 1.5
total_hours = 0

while lesson_number <= 5:
    total_hours += lesson_duration

    print(f"Занятие №{lesson_number}")
    print(f"Общая продолжительность: {total_hours} ч.")

    lesson_number += 1

print(f"Итого: {total_hours} ч.")