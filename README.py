class Calculator:
    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль!")
            return None
        except TypeError:
            print("Помилка: Неправильний тип даних!")
            return None
        else:
            return result

    def convert_to_int(self, value):
        try:
            return int(value)
        except ValueError:
            print(f"Помилка: Неможливо перетворити '{value}' на ціле число.")
            return None

    def get_element(self, my_list, index):
        try:
            return my_list[index]
        except IndexError:
            print("Помилка: Індекс за межами списку.")
            return None


# Створимо екземпляр класу
calc = Calculator()

# Демонстрація роботи
print("Ділення 10 на 2:", calc.divide(10, 2))         # 5.0
print("Ділення на 0:", calc.divide(5, 0))              # Помилка
print("Ділення з рядком:", calc.divide(5, "a"))        # Помилка

print("Конвертація '123':", calc.convert_to_int("123"))    # 123
print("Конвертація 'abc':", calc.convert_to_int("abc"))    # Помилка

print("Елемент списку [1, 2, 3], індекс 1:", calc.get_element([1, 2, 3], 1))  # 2
print("Невірний індекс:", calc.get_element([1, 2, 3], 10))                    # Помилка
