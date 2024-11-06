# 
x = int(input("   Enter the number: "))
y = int(input("   Enter your N: "))
# ...
for line in range(1, y + 1):
    square_root = x ** line
    print(f"Result: {x}^{line}={square_root}")