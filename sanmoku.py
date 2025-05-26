import tkinter as tk
from tkinter import messagebox

class GomokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("3x3 五目並べ (○✕ゲーム)")
        self.current_player = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.master)
        frame.pack()

        for row in range(3):
            for col in range(3):
                btn = tk.Button(frame, text="", font=("Arial", 36), width=4, height=2,
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

        reset_btn = tk.Button(self.master, text="リセット", font=("Arial", 14), command=self.reset_board)
        reset_btn.pack(pady=10)

    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            if self.check_winner(self.current_player):
                messagebox.showinfo("勝利", f"{self.current_player} の勝ちです！")
                self.disable_all_buttons()
            elif self.is_full():
                messagebox.showinfo("引き分け", "引き分けです！")
                self.disable_all_buttons()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self, player):
        # 横・縦・斜めのチェック
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # 横
                return True
            if all(self.board[j][i] == player for j in range(3)):  # 縦
                return True
        if all(self.board[i][i] == player for i in range(3)):  # 斜め1
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # 斜め2
            return True
        return False

    def is_full(self):
        return all(self.board[r][c] != "" for r in range(3) for c in range(3))

    def disable_all_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "O"
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = GomokuGame(root)
    root.mainloop()