import tkinter as tk
from tkinter import simpledialog, messagebox
from itertools import combinations

class PlayerInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Biwenginator")
        self.players_info = {}
        self.current_player = 1
        self.team_deficit = 0  # Global variable for team deficit
        self.num_players_to_sell = 0  # Global variable for the number of players to sell
        self.combinations_list = []  # List to store valid combinations

        # Labels
        self.label_name = tk.Label(root, text="Player Name:")
        self.label_value = tk.Label(root, text="Player Value:")
        self.label_deficit = tk.Label(root, text="Team Deficit:")
        self.label_players_to_sell = tk.Label(root, text="Number of Players to Sell:")

        # Entry widgets
        self.entry_name = tk.Entry(root)
        self.entry_value = tk.Entry(root)
        self.entry_deficit = tk.Entry(root)
        self.entry_players_to_sell = tk.Entry(root)

        # Buttons
        self.next_button = tk.Button(root, text="Next Player", command=self.next_player)
        self.end_button = tk.Button(root, text="Calculate combinations", command=self.generate_combinations_and_display)

        # Result Text
        self.result_text = tk.Text(root, height=20, width=50)

        # Grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.label_value.grid(row=1, column=0, padx=10, pady=5)
        self.label_deficit.grid(row=2, column=0, padx=10, pady=5)
        self.label_players_to_sell.grid(row=3, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_value.grid(row=1, column=1, padx=10, pady=5)
        self.entry_deficit.grid(row=2, column=1, padx=10, pady=5)
        self.entry_players_to_sell.grid(row=3, column=1, padx=10, pady=5)
        self.next_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.end_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def next_player(self):
        player_name = self.entry_name.get()
        player_value = self.entry_value.get()

        if player_name and player_value:
            self.players_info[player_name] = float(player_value)
            self.result_text.insert(tk.END, f"{self.current_player}. {player_name}: {player_value}\n")
            self.current_player += 1
            self.entry_name.delete(0, tk.END)
            self.entry_value.delete(0, tk.END)
        else:
            tk.messagebox.showinfo("Error", "Please enter both player name and value.")

    def generate_combinations_and_display(self):
        team_deficit = self.entry_deficit.get()
        num_players_to_sell = self.entry_players_to_sell.get()

        if team_deficit and num_players_to_sell:
            try:
                self.team_deficit = float(team_deficit)
                self.num_players_to_sell = int(num_players_to_sell)
                self.generate_combinations()
                self.display_valid_combinations()
            except ValueError:
                tk.messagebox.showinfo("Error", "Please enter valid numeric values.")
        else:
            tk.messagebox.showinfo("Error", "Please enter both team deficit and the number of players to sell.")

    def generate_combinations(self):
        players = list(self.players_info.keys())
        self.combinations_list = list(combinations(players, self.num_players_to_sell))

    def display_valid_combinations(self):
        self.result_text.insert(tk.END, f"\nValid Combinations for {self.num_players_to_sell} Players (Sorted by Value):\n")

        # Sort combinations based on total value
        sorted_combinations = sorted(self.combinations_list, key=lambda comb: sum(self.players_info[player] for player in comb))

        for combination in sorted_combinations:
            combination_values = [self.players_info[player] for player in combination]
            if sum(combination_values) >= self.team_deficit:
                self.result_text.insert(tk.END, f"{', '.join(combination)}: {sum(combination_values)}\n")

    

def main():
    root = tk.Tk()
    app = PlayerInfoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
