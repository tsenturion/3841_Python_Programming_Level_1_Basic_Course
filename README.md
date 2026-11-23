# Задачи LeetCode для базового курса Python

По три задачи на тему в порядке [программы курса](<Программа курса !3841.docx>). Задачи средней и высокой сложности отмечены отдельно.

## Модуль 1. Простые типы данных

### Арифметика и приоритет операций

- [2235. Сложение двух целых чисел](https://leetcode.com/problems/add-two-integers/)
- [2469. Перевод температуры из градусов Цельсия](https://leetcode.com/problems/convert-the-temperature/)
- [2651. Время прибытия с учётом задержки](https://leetcode.com/problems/calculate-delayed-arrival-time/)

### Форматирование строк

Для сборки результата попробуйте `f`-строки, а затем сравните их с `str.format()` и форматированием через `%`.

- [228. Запись последовательных чисел в виде диапазонов](https://leetcode.com/problems/summary-ranges/)
- [482. Форматирование лицензионного ключа](https://leetcode.com/problems/license-key-formatting/)
- [831. Маскировка адреса электронной почты и номера телефона](https://leetcode.com/problems/masking-personal-information/) — средняя

### Модуль `math`

- [1979. Наибольший общий делитель минимального и максимального элементов](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) — `math.gcd()`
- [1952. Проверка, есть ли у числа ровно три делителя](https://leetcode.com/problems/three-divisors/) — `math.isqrt()`
- [1175. Перестановки с простыми числами на простых позициях](https://leetcode.com/problems/prime-arrangements/) — `math.factorial()`

## Модуль 2. Условный оператор `if`

### Ветвление и условное выражение

- [3516. Кто из двух людей ближе к третьему](https://leetcode.com/problems/find-closest-person/)
- [2481. Минимальное число разрезов, чтобы разделить круг на равные части](https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/)
- [1822. Знак произведения элементов списка](https://leetcode.com/problems/sign-of-the-product-of-an-array/)

### Логические выражения и проверка вхождения

- [771. Сколько камней являются драгоценными](https://leetcode.com/problems/jewels-and-stones/)
- [1832. Проверка, содержит ли предложение все буквы алфавита](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)
- [3136. Проверка слова по нескольким условиям](https://leetcode.com/problems/valid-word/)

## Модуль 3. Последовательности и циклы

### Строки, индексы и срезы

- [2000. Разворот начала строки до заданного символа](https://leetcode.com/problems/reverse-prefix-of-word/)
- [2129. Преобразование регистра слов в заголовке](https://leetcode.com/problems/capitalize-the-title/)
- [541. Разворот первых `k` символов в каждом блоке длины `2k`](https://leetcode.com/problems/reverse-string-ii/)

### Циклы `while` и `for`, `range`

- [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
- [1342. Подсчёт шагов до уменьшения числа до нуля](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
- [1281. Разность произведения и суммы цифр](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

### Вложенные циклы

- [1512. Подсчёт пар равных элементов](https://leetcode.com/problems/number-of-good-pairs/)
- [2006. Подсчёт пар с заданной абсолютной разностью](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)
- [1588. Сумма элементов всех подмассивов нечётной длины](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

### `break`, `continue` и `else` в циклах

- [744. Поиск наименьшей буквы, большей заданной](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
- [796. Проверка циклического сдвига строки](https://leetcode.com/problems/rotate-string/)
- [28. Поиск первого вхождения подстроки](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Модуль 4. Списки

### Изменение списка на месте

- [27. Удаление заданного элемента](https://leetcode.com/problems/remove-element/)
- [26. Удаление дубликатов из отсортированного списка](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [88. Слияние двух отсортированных списков](https://leetcode.com/problems/merge-sorted-array/)

### Методы списков

- [1929. Соединение списка с его копией](https://leetcode.com/problems/concatenation-of-array/) — `copy()` и `extend()`
- [905. Перестановка элементов по чётности](https://leetcode.com/problems/sort-array-by-parity/) — `sort()` с параметром `key`
- [682. Подсчёт очков в бейсбольной игре](https://leetcode.com/problems/baseball-game/) — `append()` и `pop()`

### Вложенные списки

- [1672. Поиск самого богатого клиента](https://leetcode.com/problems/richest-customer-wealth/)
- [1572. Сумма элементов на диагоналях матрицы](https://leetcode.com/problems/matrix-diagonal-sum/)
- [867. Транспонирование матрицы](https://leetcode.com/problems/transpose-matrix/)

### Списковые включения

- [1431. Кто может получить больше всех конфет](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
- [2942. Индексы слов, содержащих заданный символ](https://leetcode.com/problems/find-words-containing-character/)
- [1313. Распаковка списка из пар «число повторений и значение»](https://leetcode.com/problems/decompress-run-length-encoded-list/)

## Модуль 5. Кортежи, словари и множества

### Кортежи

Храните координаты и пары значений в кортежах, чтобы использовать их как ключи словаря или элементы множества.

- [1496. Проверка, пересекает ли путь сам себя](https://leetcode.com/problems/path-crossing/)
- [1128. Подсчёт пар одинаковых костяшек домино](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)
- [874. Движение робота с учётом препятствий](https://leetcode.com/problems/walking-robot-simulation/) — средняя

### Словари

- [13. Перевод римского числа в целое](https://leetcode.com/problems/roman-to-integer/)
- [387. Поиск первого неповторяющегося символа](https://leetcode.com/problems/first-unique-character-in-a-string/)
- [1. Поиск двух чисел с заданной суммой](https://leetcode.com/problems/two-sum/)

### Множества

- [217. Проверка наличия дубликатов](https://leetcode.com/problems/contains-duplicate/)
- [349. Пересечение двух списков](https://leetcode.com/problems/intersection-of-two-arrays/)
- [2215. Поиск элементов, которые встречаются только в одном из двух списков](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

### Словарные включения

- [1331. Замена элементов их рангами](https://leetcode.com/problems/rank-transform-of-an-array/)
- [2325. Расшифровка сообщения по ключу](https://leetcode.com/problems/decode-the-message/)
- [506. Распределение мест по результатам участников](https://leetcode.com/problems/relative-ranks/)

### Включения множеств

- [804. Подсчёт уникальных записей слов азбукой Морзе](https://leetcode.com/problems/unique-morse-code-words/)
- [929. Подсчёт уникальных адресов электронной почты](https://leetcode.com/problems/unique-email-addresses/)
- [2441. Наибольшее положительное число, у которого в списке есть противоположное](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/)

## Модуль 6. Функции

Вынесите повторяющееся преобразование или подсчёт в отдельную функцию. Добавьте аннотации типов и краткую строку документации.

- [2446. Проверка пересечения двух событий по времени](https://leetcode.com/problems/determine-if-two-events-have-conflict/)
- [824. Преобразование слов по правилам Goat Latin](https://leetcode.com/problems/goat-latin/)
- [2287. Сколько раз из символов строки можно составить целевое слово](https://leetcode.com/problems/rearrange-characters-to-make-target-string/)

## Модуль 8. Пути и каталоги

Задачи моделируют переходы между каталогами и обрабатывают пути, представленные строками.

- [1598. Возврат в корневой каталог по журналу переходов](https://leetcode.com/problems/crawler-log-folder/)
- [71. Упрощение абсолютного пути в Unix](https://leetcode.com/problems/simplify-path/) — средняя
- [388. Поиск самого длинного абсолютного пути к файлу](https://leetcode.com/problems/longest-absolute-file-path/) — средняя

## Модуль 10. Регулярные выражения

- [125. Проверка палиндрома с удалением посторонних символов](https://leetcode.com/problems/valid-palindrome/) — `re.sub()`
- [819. Поиск самого частого разрешённого слова](https://leetcode.com/problems/most-common-word/) — `re.findall()`
- [65. Проверка записи числа](https://leetcode.com/problems/valid-number/) — `re.fullmatch()`, высокая сложность

## Модуль 11. Запросы SQL

Запросы из этих задач можно выполнить и в SQLite через `sqlite3`.

- [595. Отбор стран по площади или населению](https://leetcode.com/problems/big-countries/)
- [182. Поиск повторяющихся адресов электронной почты](https://leetcode.com/problems/duplicate-emails/)
- [175. Объединение таблиц с людьми и адресами](https://leetcode.com/problems/combine-two-tables/)

## Модуль 12. Работа с датами (опционально)

Используйте `datetime` для разбора дат и календарных вычислений.

- [1154. Определение порядкового номера дня в году](https://leetcode.com/problems/day-of-the-year/)
- [1360. Подсчёт дней между двумя датами](https://leetcode.com/problems/number-of-days-between-two-dates/)
- [1185. Определение дня недели по дате](https://leetcode.com/problems/day-of-the-week/)
