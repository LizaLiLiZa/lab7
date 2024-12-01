import re
from datetime import datetime, date
# 1. Функция, принимающая на вход некий набор параметров (минимум 3 параметра).
# Внутри себя эта функция содержит заранее определённую строку, в которую можно подставлять значения переменных.
# Функция возвращает строку, в которую вставлены значения, такие что
# 1.1. Как минимум, одно значение - это просто строка
# 1.2. Как минимум, одно значение - это результат арифметической операции
# 1.3. Как минимум, одно значение - это результат вызова другой функции
def product_cost(product: str) -> int:
    if product == "Карамельки":
        return 100
    elif product == "Булочка с маком":
        return 3500
    else:
        return 10000000

def exercise_1(name: str, birthday: date, product: str) -> str:
    now = date(datetime.now().year, datetime.now().month, datetime.now().day)
    age = now.year - birthday.year - 1
    if birthday.month < now.month:
        age += 1
    elif birthday.month == now.month and birthday.day <= now.day:
        age += 1
    return f"""Добро пожаловать, {name}!!! Мы вас ждали.
На сегодняшний день ваша скидка составляет {(age := (now.year - birthday.year - 
            (1 if (birthday.month, birthday.day) > (now.month, now.day) else 0)))}%.
В вашем заказе {product}.
К оплате {product_cost(product) * (100 - age) / 100:.2f}.\n"""

# 2. Функция, которая формирует строку, состоящую из повторений комбинации других строк.
# Эта функция выводит получившуюся строку, где каждое повторение выводится на отдельной строке.
def exercise_2(str1, str2, str3, num) -> str:
    str_all = "".join(list(str1+str2+str3+"\n" for i in range(num)))
    return str_all

# 3. Функция, которая считает количество вхождений подстроки в строку без учёта регистра.
def exercise_3(str_: str, substr:str) -> int:
    str_ = str_.lower()
    substr = substr.lower()
    return str_.count(substr)

# 4. Функция, принимающая на вход строку и выводящая подстроку, содержащуюся между двумя индексами.
# Индексы ДОЛЖНЫ быть больше нуля и меньше длины строки минус 1.
# Тело функции ДОЛЖНО быть написано в одну строку.
def exercise_4(str_: str, i_start: int, i_end: int):
    return str_[i_start:i_end]

# 5. Функция, принимающая на вход произвольное количество разных строк, где содержатся любые кириллические буквы, а также могут содержаться латинские буквы, но только такие, которые визуально неотличимы от кириллических. Регистр букв произвольный.
# Эта функция ищет слова, в которых содержатся латинские буквы.
# На выход возвращаются строки, где были обнаружены латинские символы и количество слов, в которых была обнаружена хотя бы одна латинская буква.
#aсeopx
#ACEHKOPTX
def exercise_5(*str_: str):
    array_str = []
    pattern = r"[aceopxACEHKOPTX]"
    for i in str_:
        words = i.split()
        words_str = []
        count = 0
        for word in words:
            if re.search(pattern, word):
                words_str.append(word)
                count += 1
        if count != 0:
            words_str = [words_str, count]
            array_str.append(words_str)
    return array_str

# 6. Функция, определяющая, является ли строка палиндромом (одинаково читается с начала и с конца).
# Строка МОЖЕТ содержать как цифры, так и буквы.
def exercise_6(str_: str):
    if str_[::-1] == str_:
        return True
    return False

# 7. Функция, принимающая на вход строку, содержащую несколько слов, которые разделены одним или несколькими пробелами.
# У входной строки могут быть несколько пробелов в начале и в конце.
# Функция убирает лишние пробелы: то есть все пробелы в начале и в конце строки, а между словами оставляет только один пробел.
# Функция возвращает длину строки после удаления лишних пробелов.
def exercise_7(str_: str):
    str_ = ' '.join(str_.split())
    return len(str_)

# 8. Функция, принимающая на вход строку, содержащую текст из нескольких предложений.
# Функция заменяет символы окончания предложения на символ переноса строки.
# Функция возвращает получившуюся строку.
def exercise_8(str_:str):
    return re.sub(r"[\.!?]\s", "\n", str_+" ")

# 9. Минимум 3 функции, содержащие произвольные алгоритмы работы со строками.
# Функции ДОЛЖНЫ решать алгоритмы, отличные от реализованных в п. 1-8
def exersise_9_1(str_: str):
    if ". " in str_:
        str_ = re.sub(r"\.\s", ".\n", str_)
    if "! " in str_:
        str_ = re.sub(r"!\s", "!\n", str_)
    if "? " in str_:
        str_ = re.sub(r"?\s", "\n", str_)
    return str_

def exersise_9_2(value: str) -> bool:
    pattern_en = r"^[A-Z]{1}[a-z]{1,200}$"
    pattern_rus = r"^[А-Я]{1}[а-я]{1,200}$"
    if re.match(pattern_en, value) or re.match(pattern_rus, value):
        return True
    return False

def exersise_9_3(value: str) -> bool:
    pattern = r"^[0-9]{7,15}$"
    if re.match(pattern, value):
        return True
    return False
