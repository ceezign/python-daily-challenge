# Pascal Triangle (Python)
from dataclasses import field


def generate_pascals_triangle(n):
    """Generate Pascal's triangle as a list of rows (each row is a list of ints).
    Uses nested loops and previous row values.
    """
    triangle = []
    for i in range(n):                   # outer loop: build row i (0-based)
        row = [1] * (i + 1)              # start with all 1s, length = i+1
        if i > 1:                        # only compute internal values when i >= 2
            for j in range(1, i):        # inner loop: fill position 1...i-1
                # each inner enry is sum of two numbers from previous rows
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def format_triangle(triangle, spacing=2):
    """
    Return a string that represents the triangle as a centered pyramid.
    Spacing: number of spaces between numbers horizontally.
    """
    if not triangle:
        return ""

    # Determine the width needed for the largest number so column align
    max_num_len = max(len(str(num))  for row in triangle for num in row)
    field = max_num_len                             # each number will be right-justifies to this width
    sep = " " * spacing                             # spacing between numbers

    rows_str = []
    for row in triangle:
        formatted = [str(num).rjust(field) for num in row]      # pad numbers
        row_str = sep.join(formatted)
        rows_str.append(row_str)

    max_width = len(rows_str[-1])        # width of the last (widest) row
    centered = [r.center(max_width) for r in rows_str]
    return "\n".join(centered)

def save_triangle_to_file(triangle, filename="pascal_triangle.text", spacing=2):
    contents = format_triangle(triangle, spacing=spacing)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(contents)
    print(f"Saved Pascal's Triangle to: {filename}")

def main():
    try:
        n = int(input("Enter number of rows (e.g. 5): ").strip())
        if n < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative integer.")
        return

    spacing_input = input("spacing between number (press Enter for default 2): ").strip()
    spacing = int(spacing_input) if spacing_input else 2

    triangle = generate_pascals_triangle(n)
    print("\nPascal's Triangle:\n")
    print(format_triangle(triangle, spacing=spacing))

    export = input("\nDo you want to save to a .txt file? (y/N): ").strip().lower()
    if export == "y":
        filename = input("Enter filename (default pascal_triangle.txt): ").strip() or "pascal_triangle.txt"
        save_triangle_to_file(triangle, filename, spacing)

if __name__ == "__main__":
    main()































