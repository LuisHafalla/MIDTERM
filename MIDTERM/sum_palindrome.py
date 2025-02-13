def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_lines(lines):
    results = []
    for i, line in enumerate(lines, start=1):
        try:
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            results.append(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
        except ValueError:
            results.append(f"Error: Invalid number format in line {i}.")
    return results

def main():
    filename = "numbers.txt"
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        if not lines:
            print(f"Error: '{filename}' is empty.")
            return
        results = process_lines(lines)
        for res in results:
            print(res)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Make sure the file is in the same directory.")

if __name__ == "__main__":
    main()
