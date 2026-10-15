import random
from logic import feedback

# name: (code length, highest symbol, allowed guesses)
DIFFICULTIES = {
    "easy": (3, 4, 12),
    "normal": (4, 6, 10),
    "hard": (5, 8, 8),
}


class Mastermind:
    def __init__(self, difficulty="normal"):
        self.length, self.max_symbol, self.max_turns = DIFFICULTIES[difficulty]
        self.symbols = "".join(str(n) for n in range(1, self.max_symbol + 1))
        self.code = [random.choice(self.symbols) for _ in range(self.length)]
        self.history = []
        self.over = False
        self.won = False

    @property
    def turns_left(self):
        return self.max_turns - len(self.history)

    def guess(self, guess):
        if self.over:
            raise RuntimeError("The game is over; no more guesses are accepted.")
        exact, partial = feedback(self.code, guess)
        self.history.append((guess, exact, partial))
        if exact == len(self.code):
            self.over = self.won = True
        elif self.turns_left == 0:
            self.over = True
        return exact, partial

    def validate(self, raw):
        """Return an error message for a malformed guess, or None if it is valid."""
        if len(raw) != self.length:
            return f"Guess must be exactly {self.length} digits (got {len(raw)})."
        bad = sorted(set(ch for ch in raw if ch not in self.symbols))
        if bad:
            return f"Invalid symbol(s) {', '.join(repr(ch) for ch in bad)}; use digits 1 to {self.max_symbol}."
        return None

    def show_history(self):
        print(f"{'#':>3}  {'Guess':<5}  {'Exact':>5}  {'Partial':>7}")
        for i, (guess, exact, partial) in enumerate(self.history, 1):
            print(f"{i:>3}  {guess:<5}  {exact:>5}  {partial:>7}")

    def run(self):
        print(f"Mastermind — enter {self.length} digits from 1 to {self.max_symbol}. Type q to quit.")
        while not self.over:
            try:
                raw = input(f"{self.turns_left} turns left > ").strip()
            except (EOFError, KeyboardInterrupt):
                raw = "q"
                print()
            if raw.lower() == "q":
                self.over = True
                print("You quit. The code was", "".join(self.code))
                return
            error = self.validate(raw)
            if error:
                print(error, "(no turn used)")
                continue
            exact, partial = self.guess(raw)
            print("Exact:", exact, " Partial:", partial)
            self.show_history()
        if self.won:
            print(f"You win! Cracked the code in {len(self.history)} guesses.")
        else:
            print("You lose! Out of guesses. The code was", "".join(self.code))
