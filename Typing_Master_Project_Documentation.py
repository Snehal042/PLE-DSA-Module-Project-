import random
import time
import json
WORD_LIST = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
TEST_DURATION = 60  # Test duration in seconds
def load_leaderboard(filename="leaderboard.json"):
    try:
        with open(filename, "r") as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = {}
    return leaderboard
def save_leaderboard(leaderboard, filename="leaderboard.json"):
    with open(filename, "w") as f:
        json.dump(leaderboard, f, indent=4)
def get_user_input(prompt):
    user_input = input(prompt)
    return user_input
def start_typing_test(username, word_list):
    print("Type the following words as fast as you can:")
    input("Press Enter to start the typing test...")

    start_time = time.time()
    word_count = 0

    while True:
        word = random.choice(word_list)
        print(word)
        user_input = get_user_input("Type the word: ")

        if user_input == word:
            word_count += 1

        if time.time() - start_time >= TEST_DURATION:
            break

    end_time = time.time()
    time_taken = end_time - start_time
    wpm = (word_count / time_taken) * 60

    print(f"Typing Metrics:")
    print(f"Words Typed: {word_count}")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")

    return wpm
def show_leaderboard(leaderboard):
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        print("Leaderboard:")
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for rank, (user, wpm) in enumerate(sorted_leaderboard, 1):
            print(f"{rank}. {user} - {wpm:.2f} WPM")
def main():
    leaderboard = load_leaderboard()

    print("Welcome to the Terminal Typing Master!")
    username = get_user_input("Enter your username for the leaderboard: ")

    while True:
        print("Main Menu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        option = get_user_input("Enter your choice: ")

        if option == '1':
            wpm = start_typing_test(username, WORD_LIST)
            leaderboard[username] = wpm
            save_leaderboard(leaderboard)
        elif option == '2':
            show_leaderboard(leaderboard)
        elif option == '3':
            save_leaderboard(leaderboard)
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
