# pythonla yapılmış basit xox(tic tac toe) oyunu


def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 9)


def check_win(board, player):
  for i in range(3):
    if all(board[i][j] == player
           for j in range(3)) or all(board[j][i] == player for j in range(3)):
      return True
  if all(board[i][i] == player
         for i in range(3)) or all(board[i][2 - i] == player
                                   for i in range(3)):
    return True
  return False


def is_board_full(board):
  return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def get_move(player):
  while True:
    move = input(f"Oyuncu '{player}' için hamle (örn: 1 1): ")
    try:
      row, col = map(int, move.split())
      if 1 <= row <= 3 and 1 <= col <= 3:
        return row - 1, col - 1
      else:
        print(
          "Geçersiz hamle. Satır ve sütun numaraları 1 ile 3 arasında olmalıdır."
        )
    except ValueError:
      print("Geçersiz hamle. Lütfen iki tam sayı girin.")


def main():
  board = [[' ' for _ in range(3)] for _ in range(3)]
  players = ['X', 'O']
  player_idx = 0

  while True:
    current_player = players[player_idx]
    print_board(board)
    row, col = get_move(current_player)

    if board[row][col] == ' ':
      board[row][col] = current_player
      if check_win(board, current_player):
        print_board(board)
        print(f"Oyuncu '{current_player}' kazandı!")
        break
      elif is_board_full(board):
        print_board(board)
        print("Oyun berabere!")
        break
      else:
        player_idx = 1 - player_idx
    else:
      print("Bu hücre dolu. Lütfen başka bir hamle yapın.")


if __name__ == "__main__":
  main()
