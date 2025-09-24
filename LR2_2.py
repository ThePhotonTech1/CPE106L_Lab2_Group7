filename = input("Enter filename: ")
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    with open(filename, 'w') as f:
        pass
    lines = []
    print("File not found. Created new file.")
choice = input("Do you want to append to the file? (y/n): ").lower()
if choice == 'y':
    while True:
        text = input("Enter text to append: ")
        with open(filename, 'a') as f:
            f.write(text + '\n')
        with open(filename, 'r') as f:
            lines = f.readlines()
        more = input("Add more? (y/n): ").lower()
        if more != 'y':
            break
while True:
    print(f"Number of lines: {len(lines)}")
    inp = input("Enter line number (0 to quit): ")
    try:
        num = int(inp)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if num == 0:
        break
    if 1 <= num <= len(lines):
        print(lines[num - 1].rstrip())
    else:
        print("Invalid line number.")
