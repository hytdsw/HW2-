import random

class Encryptor:
    def __init__(self, *numbers):
        # Інкапсульовані числа
        self._numbers = numbers
        # Зберігає результат обчислень
        self._result = None
        # Викликаємо метод для виконання випадкової операції
        self._process()

    def _process(self):
        # Випадковий вибір математичної операції
        operation = random.choice(['+', '-', '*', '/'])
        # Обчислюємо результат на основі випадкової операції
        if operation == '+':
            self._result = sum(self._numbers)
        elif operation == '-':
            self._result = self._numbers[0]
            for num in self._numbers[1:]:
                self._result -= num
        elif operation == '*':
            self._result = 1
            for num in self._numbers:
                self._result *= num
        elif operation == '/':
            try:
                self._result = self._numbers[0]
                for num in self._numbers[1:]:
                    self._result /= num
            except ZeroDivisionError:
                self._result = "Error: Division by zero"

    # Перевизначення метода для виведення об'єкта
    def __str__(self):
        return f'Result: {self._result}'

# Використання
enc = Encryptor(10, 5, 2)
print(enc)
