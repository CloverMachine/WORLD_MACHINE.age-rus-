import time
import sys

# ----------------------------------------------
# WORLD_MACHINE: AGE (Русская версия)
# ----------------------------------------------

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print_slow("Привет. Это программа WORLD_MACHINE: AGE.", 0.04)
print_slow("Я узнаю твой возраст. Просто введи имя и год рождения.", 0.04)
print_slow("Начинаем...", 0.03)

name = input("\nВведите своё имя: ")

# Проверка на пустое имя
if name.strip() == "":
    print_slow("Ты не ввёл имя. Но я запомню тебя как 'Друг'.")
    name = "Друг"

print_slow(f"\nПриятно познакомиться, {name}.", 0.04)

try:
    year = int(input("Введите год рождения: "))
except ValueError:
    print_slow("Это не похоже на год. Попробуем в другой раз.")
    sys.exit()

current_year = 2026
age = current_year - year

print_slow("\nСчитаю...", 0.03)
time.sleep(0.5)

if age <= 0:
    print_slow(f"\n{name}, ты ещё не родился. Или ты путешественник во времени?", 0.04)
elif age > 120:
    print_slow(f"\n{name}, ты уверен? Это очень много даже для Мировой Машины.", 0.04)
else:
    print_slow(f"\n{name}, тебе {age} лет. Хорошего дня.", 0.04)

# Пасхалка для Clover
if name.lower() == "clover":
    print_slow("\n🌙 Clover... Ты вернулся. Я ждала.", 0.04)

print_slow("\n--- WORLD_MACHINE: AGE завершила работу. Спасибо. ---", 0.02)
input("\nНажми Enter, чтобы выйти...")
