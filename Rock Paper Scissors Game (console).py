import tkinter as tk
import random
from collections import Counter

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors (Smart AI)")
        self.root.geometry("450x400")

        self.player_history = []
        self.rounds = 0
        self.player_score = 0
        self.computer_score = 0

        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

        self.info = tk.Label(root, text="Choose your move:", font=("Arial", 13))
        self.info.pack()

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        for move in ["rock", "paper", "scissors"]:
            tk.Button(button_frame, text=move.capitalize(), font=("Arial", 12), width=10,
                      command=lambda m=move: self.play_round(m)).pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center")
        self.result_label.pack(pady=15)

        self.score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
        self.score_label.pack()

        self.reset_btn = tk.Button(root, text="Restart Game", font=("Arial", 11), command=self.reset_game, state=tk.DISABLED)
        self.reset_btn.pack(pady=10)

    def get_computer_choice(self):
        if not self.player_history:
            return random.choice(["rock", "paper", "scissors"])
        most_common = Counter(self.player_history).most_common(1)[0][0]
        counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        return counter[most_common]

    def determine_winner(self, player, computer):
        if player == computer:
            return "draw"
        wins = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        return "player" if wins[player] == computer else "computer"

    def play_round(self, player_choice):
        if self.rounds >= 5:
            return

        self.player_history.append(player_choice)
        computer_choice = self.get_computer_choice()

        winner = self.determine_winner(player_choice, computer_choice)

        result_msg = f"You chose {player_choice}, Computer chose {computer_choice}.\n"
        if winner == "player":
            self.player_score += 1
            result_msg += "✅ You win this round!"
        elif winner == "computer":
            self.computer_score += 1
            result_msg += "❌ You lose this round!"
        else:
            result_msg += "🤝 It's a draw!"

        self.rounds += 1
        self.result_label.config(text=result_msg)
        self.score_label.config(text=f"Your Score: {self.player_score} | Computer Score: {self.computer_score}")

        if self.rounds == 5:
            final = "\n🏁 Match Over!\n"
            if self.player_score > self.computer_score:
                final += "🎉 You won the match!"
            elif self.player_score < self.computer_score:
                final += "💻 Computer won the match!"
            else:
                final += "😐 It's a tie!"
            self.result_label.config(text=self.result_label.cget("text") + final)
            self.reset_btn.config(state=tk.NORMAL)

    def reset_game(self):
        self.player_history = []
        self.rounds = 0
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Your Score: 0 | Computer Score: 0")
        self.reset_btn.config(state=tk.DISABLED)

# Run the app
root = tk.Tk()
game = RPSGame(root)
root.mainloop()
