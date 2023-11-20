import random


class ChessBoard:
    def __init__(self):
        """
        Ініціалізація порожньої дошки 8x8
        """
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        # Список символів фігур, які можна використовувати
        self.pieces = ['♛', '♜', '♝', '♞', '♟', '♚', '♕', '♖', '♗', '♘', '♙']

    def place_pieces(self):
        """
        Очищення дошки і встановлення нового випадкового розташування фігур
        :return:
        """
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        # Гарантуємо, що чорний і білий королі завжди присутні на дошці
        self.board[random.randint(0, 7)][random.randint(0, 7)] = '♚'
        self.board[random.randint(0, 7)][random.randint(0, 7)] = '♔'

        # Додавання інших фігур на дошку у випадкових місцях
        # Випадкова кількість фігур
        for _ in range(random.randint(0, 10)):
            piece = random.choice(self.pieces)
            x, y = random.randint(0, 7), random.randint(0, 7)
            # Забезпечення того, щоб клітина була порожньою перед розміщенням
            # фігури
            while self.board[x][y] != " ":
                x, y = random.randint(0, 7), random.randint(0, 7)
            self.board[x][y] = piece

    def print_board(self):
        """
        Друк заголовків стовпців (букви a-h)
        :return:
        """
        print("  " + " ".join([chr(97 + i) for i in range(8)]))
        for i in range(8):
            # Друк рядків дошки з номерами рядків (1-8)
            print(str(8 - i) + " " + " ".join(self.board[i]) + " " + str(8 - i))
        # Повторення заголовків стовпців унизу дошки
        print("  " + " ".join([chr(97 + i) for i in range(8)]))


# Створення і відображення дошки
chess_board = ChessBoard()
for _ in range(3):
    chess_board.place_pieces()  # Розміщення фігур на дошці
    chess_board.print_board()  # Друк дошки
    print("\n")
