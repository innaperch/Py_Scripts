import tkinter as tk
from tkinter import messagebox

# Створення головного вікна
root = tk.Tk()
root.title("Хрестики-Нолики")

# Глобальні змінні
turn = 'X'  # Початкова черга - 'X'
board = [' ' for _ in range(9)]  # Ігрове поле

# Функція для перевірки перемоги
def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Рядки
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Колонки
                      (0, 4, 8), (2, 4, 6)]  # Діагоналі
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

# Функція для оновлення клітинки
def click_cell(i):
    global turn
    if board[i] == ' ':
        board[i] = turn
        buttons[i].config(text=turn)
        winner = check_win()
        if winner:
            messagebox.showinfo("Перемога!", f"Гравець {winner} виграв!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Нічия!", "Нічия!")
            reset_game()
        else:
            turn = 'O' if turn == 'X' else 'X'  # Зміна черги

# Функція для скидання гри
def reset_game():
    global turn, board
    turn = 'X'
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ')

# Створення кнопок для кожної клітинки
buttons = []
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 24), width=5, height=2, command=lambda i=i: click_cell(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

# Кнопка для скидання гри
reset_button = tk.Button(root, text="Скинути гру", font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Запуск інтерфейсу
root.mainloop()
