from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Підготовка структури даних для зберігання ім'ян та днів народжень
    birthdays_per_week = defaultdict(list)
    
    # Отримання поточної дати
    today = datetime.today().date()

    # Перебір користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка дати на цей рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з поточною датою
        delta_days = (birthday_this_year - today).days

        # Визначення дня тижня
        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        # Визначення наступного понеділка, якщо день народження вихідний
        if delta_days >= 7:
            day_of_week = "Monday"

        # Зберігання результату
        birthdays_per_week[day_of_week].append(name)

    # Виведення результату
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)}
]

get_birthdays_per_week(users)
