exam_score = 85
is_course_paid = True

if is_course_paid:
    if exam_score >= 60:
        print("Сертификат доступен")
    else:
        print("Необходимо сдать экзамен")
else:
    print("Необходимо оплатить обучение")