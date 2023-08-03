import checkers


def game():
    size = int(input("Enter the size of the board (between 4 and 16): "))
    if size < 4 or size > 16:
        print("Invalid size. Please enter a size between 4 and 16.")
        return

    board = checkers.build_board(size)
    print("Generated board:")
    print(board)

    print("\nCounts:")
    print(f"Empty cells: {checkers.get_count(board, 'Empty')}")
    print(f"Red cells: {checkers.get_count(board, 'Red')}")
    print(f"Black cells: {checkers.get_count(board, 'Black')}")


if __name__ == "__main__":
    game()