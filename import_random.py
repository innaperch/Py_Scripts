import random
import tkinter as tk
from tkinter import messagebox

# Функція для генерації чисел та їх обробки
def generate_numbers():
    try:
        # Отримати кількість чисел від користувача
        count = int(entry_count.get())
        
        if count <= 0:
            messagebox.showerror("Помилка", "Введіть число більше 0.")
            return
        
        if count > 100:
            messagebox.showerror("Помилка", "Максимальна кількість унікальних чисел - 100.")
            return

        # Генерація унікальних чисел
        numbers = random.sample(range(0, 100), count)
        
        # Розбиття на парні та непарні
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        # Виведення результатів
        text_numbers.delete(1.0, tk.END)
        text_even.delete(1.0, tk.END)
        text_odd.delete(1.0, tk.END)

        text_numbers.insert(tk.END, ", ".join(map(str, numbers)))
        text_even.insert(tk.END, ", ".join(map(str, even_numbers)))
        text_odd.insert(tk.END, ", ".join(map(str, odd_numbers)))
    
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне ціле число.")

# Головне вікно
root = tk.Tk()
root.title("Генерація чисел")

# Мітка і поле для вводу кількості чисел
label_count = tk.Label(root, text="Введіть кількість чисел (макс 100):")
label_count.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_count = tk.Entry(root, width=10)
entry_count.grid(row=0, column=1, padx=10, pady=5)

# Кнопка для генерації чисел
button_generate = tk.Button(root, text="Згенерувати", command=generate_numbers)
button_generate.grid(row=0, column=2, padx=10, pady=5)

# Поля для відображення результатів
label_numbers = tk.Label(root, text="Згенеровані числа:")
label_numbers.grid(row=1, column=0, padx=10, pady=5, sticky="w")

text_numbers = tk.Text(root, height=5, width=50)
text_numbers.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

label_even = tk.Label(root, text="Парні числа:")
label_even.grid(row=3, column=0, padx=10, pady=5, sticky="w")

text_even = tk.Text(root, height=5, width=50)
text_even.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

label_odd = tk.Label(root, text="Непарні числа:")
label_odd.grid(row=5, column=0, padx=10, pady=5, sticky="w")

text_odd = tk.Text(root, height=5, width=50)
text_odd.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Запуск програми
root.mainloop()
