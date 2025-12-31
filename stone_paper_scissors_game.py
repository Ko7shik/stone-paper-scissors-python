import random

# -------------------- FUNCTIONS --------------------

def show_status(state):
    print("\n----------------------------")
    print(f"❤️ Lives: {state['lives']}")
    print(f"🔥 Win Streak: {state['win_streak']}")
    if state["water_unlocked"] and not state["water_used"]:
        print("💧 Water ability READY!")


def get_user_choice():
    return input("Choose stone, paper, scissors (or 'exit'): ").lower()


def should_use_fire(state):
    if state["fire_available"] and state["win_streak"] == 0:
        return random.choice([True, False])
    return False


def handle_fire(state, taunts):
    print("🔥🔥 ROBOT USED FIRE 🔥🔥")

    if state["water_unlocked"] and not state["water_used"]:
        print("💧 You used WATER to cancel FIRE!")
        state["water_used"] = True
        return False
    else:
        print(random.choice(taunts))
        print("🔥 Everything burned!")
        state["lives"] -= 1
        state["fire_available"] = False
        return True


def decide_winner(user, computer, state, taunts):
    if user == computer:
        print("😐 Draw!")
        return

    win = (
        (user == "stone" and computer == "scissors") or
        (user == "paper" and computer == "stone") or
        (user == "scissors" and computer == "paper")
    )

    if win:
        print("✅ You win!")
        state["user_score"] += 1
        state["win_streak"] += 1

        if state["win_streak"] == 3:  # your modified rule
            state["water_unlocked"] = True
            print("💧💧 WATER UNLOCKED! 💧💧")
    else:
        print("❌ You lose!")
        print(random.choice(taunts))
        state["computer_score"] += 1
        state["win_streak"] = 0
        state["lives"] -= 1
        state["fire_available"] = True


# -------------------- VARIABLES --------------------

choices = ["stone", "paper", "scissors"]

taunts = [
    "🤖 You cannot defeat me, human!",
    "🤖 Is that all you've got?",
    "🤖 Hahaha! Too easy!",
    "🤖 Your streak ends here!",
]

game_state = {
    "user_score": 0,
    "computer_score": 0,
    "win_streak": 0,
    "lives": 3,
    "fire_available": False,
    "water_unlocked": False,
    "water_used": False
}

# -------------------- MAIN GAME LOOP --------------------

while True:
    show_status(game_state)

    user_choice = get_user_choice()

    if user_choice == "exit":
        print("🏁 You quit the game.")
        break

    if user_choice not in choices:
        print("❌ Invalid choice.")
        continue

    if should_use_fire(game_state):
        round_over = handle_fire(game_state, taunts)
        if round_over:
            continue

    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice}")

    decide_winner(user_choice, computer_choice, game_state, taunts)

    if game_state["lives"] == 0:
        print("\n💀 GAME OVER 💀")
        print(
            f"Final Score → You: {game_state['user_score']} | "
            f"Robot: {game_state['computer_score']}"
        )
        break