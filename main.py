import logging
import sys

# Конфігурація логування
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Animal:
    def __init__(self, weight, width, length, age):
        try:
            if not all(isinstance(arg, (int, float)) for arg in [weight, width, length, age]):
                raise ValueError("Всі параметри повинні бути числами.")
            if weight <= 0 or width <= 0 or length <= 0 or age <= 0:
                raise ValueError("Всі параметри повинні бути додатними.")

            self.weight = weight
            self.width = width
            self.length = length
            self.age = age
            logging.debug(f"Створено об'єкт Animal: вага={self.weight}, ширина={self.width}, довжина={self.length}, вік={self.age}")
        except ValueError as e:
            logging.error(f"Помилка при створенні об'єкта Animal: {e}")
            raise # Перекидаємо виняток далі


    def display_info(self):
        try:
            log_message = f"Інформація про тварину: вага={self.weight}, ширина={self.width}, довжина={self.length}, вік={self.age}"
            print(log_message)
            logging.debug(log_message)
        except AttributeError as e:
            logging.error(f"Помилка при виводі інформації про тварину: {e}")
            print(f"Помилка: {e}")


# Приклад використання:

try:
    animal1 = Animal(weight=50, width=20, length=50, age=3)
    animal1.display_info()

    animal2 = Animal(weight=-10, width=5, length=10, age=1) #спровокуємо помилку
    animal2.display_info()
except ValueError as e:
    print(f"Помилка: {e}")
except Exception as e: # Зловимо інші помилки
    print(f"Непередбачена помилка: {e}")
    logging.exception(e) # Запишемо до логу з трасуванням стеку