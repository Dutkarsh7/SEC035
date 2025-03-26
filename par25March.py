
rows = 5

for i in range(3, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
