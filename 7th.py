n = int(input("Enter a number:"))
table = [n * i for i in range(1, 11)]

with open("table.txt", "w") as f:
    f.write(f"table of {n}: {str(table)}\n")