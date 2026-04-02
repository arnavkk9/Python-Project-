import random
import os
import sys

# Force UTF-8 output so emojis work on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

CHOICES = ["Rock", "Paper", "Scissors"]
EMOJIS  = {"Rock": "[R]", "Paper": "[P]", "Scissors": "[S]"}

try:
    # Test if the terminal can handle emojis
    "✊".encode(sys.stdout.encoding or "utf-8")
    EMOJIS = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
    WIN_ICON  = "🏆"
    CPU_ICON  = "🤖"
    TIE_ICON  = "🤝"
    DRAW_LINE = "== It's a draw! =="
    WIN_LINE  = "You win this round!"
    CPU_LINE  = "Computer wins this round."
except (UnicodeEncodeError, LookupError):
    WIN_ICON  = "***"
    CPU_ICON  = ">>>"
    TIE_ICON  = "==="
    DRAW_LINE = "== It's a draw! =="
    WIN_LINE  = "You win this round!"
    CPU_LINE  = "Computer wins this round."

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("=" * 40)
    print("    ROCK  PAPER  SCISSORS")
    print("=" * 40)

def show_scores(scores):
    print(f"\n  You: {scores['you']}   |   Draw: {scores['draw']}   |   Computer: {scores['cpu']}")
    print("-" * 40)

def get_user_choice():
    print("\n  Pick your move:\n")
    for i, c in enumerate(CHOICES, 1):
        print(f"    [{i}]  {EMOJIS[c]}  {c}")
    print("\n  [Q]  Quit\n")

    while True:
        raw = input("  Your choice: ").strip().lower()
        if raw in ("q", "quit"):
            return None
        if raw in ("1", "r", "rock"):
            return "Rock"
        if raw in ("2", "p", "paper"):
            return "Paper"
        if raw in ("3", "s", "scissors"):
            return "Scissors"
        print("  !  Enter 1, 2, 3  (or R / P / S)")

def decide(user, cpu):
    if user == cpu:
        return "draw"
    wins = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}
    return "you" if (user, cpu) in wins else "cpu"

def play_round(scores):
    user = get_user_choice()
    if user is None:
        return False                        # signal to quit

    cpu = random.choice(CHOICES)

    clear()
    banner()
    show_scores(scores)

    print(f"\n  You chose   →  {EMOJIS[user]}  {user}")
    print(f"  Computer    →  {EMOJIS[cpu]}  {cpu}\n")

    result = decide(user, cpu)

    if result == "draw":
        scores["draw"] += 1
        print(f"  {DRAW_LINE}")
    elif result == "you":
        scores["you"] += 1
        print(f"  {WIN_ICON}  {WIN_LINE}")
    else:
        scores["cpu"] += 1
        print(f"  {CPU_ICON}  {CPU_LINE}")

    show_scores(scores)
    return True

def ask_play_again():
    print("\n  Play again?  [Y] Yes   [N] No  (or just press Enter for Yes)\n")
    while True:
        raw = input("  → ").strip().lower()
        if raw in ("", "y", "yes"):
            return True
        if raw in ("n", "no", "q", "quit"):
            return False
        print("  Enter Y or N")

def final_verdict(scores):
    print("\n" + "=" * 40)
    print("          FINAL SCOREBOARD")
    print("=" * 40)
    print(f"  You      :  {scores['you']}")
    print(f"  Computer :  {scores['cpu']}")
    print(f"  Draws    :  {scores['draw']}")
    print("-" * 40)
    total = scores["you"] + scores["cpu"]
    if total == 0:
        print("  No rounds played. See you next time!")
    elif scores["you"] > scores["cpu"]:
        print(f"  {WIN_ICON}  Overall winner: YOU! Well played!")
    elif scores["cpu"] > scores["you"]:
        print(f"  {CPU_ICON}  Overall winner: Computer. Better luck next time!")
    else:
        print(f"  {TIE_ICON}  It's a tie overall!")
    print("=" * 40)

def main():
    scores = {"you": 0, "draw": 0, "cpu": 0}

    clear()
    banner()
    print("\n  Tip: Enter 1/2/3  or  R/P/S  to choose.")
    show_scores(scores)

    while True:
        still_playing = play_round(scores)
        if not still_playing:
            break
        if not ask_play_again():
            break
        clear()
        banner()
        show_scores(scores)

    final_verdict(scores)

if __name__ == "__main__":
    main()
