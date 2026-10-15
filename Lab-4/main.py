from game import DIFFICULTIES, Mastermind


def choose_difficulty():
    options = ", ".join(
        f"{name} ({length} digits, 1-{top}, {turns} guesses)"
        for name, (length, top, turns) in DIFFICULTIES.items()
    )
    while True:
        choice = input(f"Choose difficulty — {options} [normal] > ").strip().lower() or "normal"
        if choice in DIFFICULTIES:
            return choice
        print("Unknown difficulty.")


if __name__ == "__main__":
    Mastermind(choose_difficulty()).run()
