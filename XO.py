def print_gameboard(board): # Функция печати игровой доски
  print("   0  1   2")
  for i, row in enumerate(board):
    print(i, "|", end="")
    for cell in row:
      print(cell, "|", end="")
    print()

def player_move(player): # Функция хода игрока
    while True:
        move = input(f"Игрок {player}, введите координаты хода (строка, столбец) через пробел: ")

        if len(move) == 3 and move[1] == " ": # Проверяем, является ли ввод двумя цифрами, разделенными пробелом
            if move[0].isdigit() and move[2].isdigit(): # Исключаем ввод букв
                row = int(move[0])
                col = int(move[2])
                # Проверяем, находятся ли координаты в пределах поля
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "-":
                    return row, col
                else:
                    print("Некорректный ход. Попробуйте снова.")
        else:
            print("Некорректный ввод. Введите два числа через пробел.")

def check_win(board): # Функция проеверки победы
  # Проверка строк
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != "-":
      return row[0]

  # Проверка столбцов
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
      return board[0][col]

  # Проверка диагоналей
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
    return board[0][2]

  # Ничья
  if all(cell != "-" for row in board for cell in row):
    return "Ничья"

  return None

board = [["-" for i in range(3)] for j in range(3)] # Инициализируем игровую доску

print("Добро пожаловать в игру 'Крестики-нолики'!") # Начало игры
print_gameboard(board)

current_player = "X" # Начало игрового цикла. Так как первыми ходят Х, начинаем с них
while True:
  row, col = player_move(current_player)
  board[row][col] = current_player

  print_gameboard(board)

  winner = check_win(board)
  if winner:
    if winner == "Ничья":
      print("Ничья!")
    else:
      print(f"Игрок {winner} победил!")
    break

  current_player = "O" if current_player == "X" else "X" # Переход хода