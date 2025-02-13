def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    filename = "numbers.txt"
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines:
            print(f"Error: '{filename}' is empty.")
            return
        
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total = sum(numbers)
            result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
            print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Make sure the file is in the same directory.")

if __name__ == "__main__":
    main()
