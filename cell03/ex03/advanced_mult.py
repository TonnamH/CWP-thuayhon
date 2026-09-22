row = 0
col = 0
while row < 11:
    print(f"Table de {row}:", end=" ")
    while col < 11:
        print(f"{row * col}", end=" ")
        col += 1
    print()
    row += 1
    col = 0
