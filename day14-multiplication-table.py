# Multiplication Table Grid


def multiplication_table():
    # ask for size
    n = int(input("Enter table size: "))

    print("\n Multiplication Table\n")

    # print header row
    print("   ", end="")      # left padding
    for col in range(1, n + 1):
        print(f"{col:4}", end="")
    print("\n" + "-" * (4 * (n + 1)))

    # Nested loops for rows * cols
    for row in range(1, n + 1):
        # Row label
        print(f"{row:3}|", end="")

        for col in range(1, n +1):
            product = row * col

            # Highlight diagonal (squares)
            if row == col:
                # Add a star before square number
                print(f"*{product:<3}", end="")
            else:
                print(f"{product:4}", end="")

        print()    # new line after each row

if __name__ == "__main__":
    multiplication_table()