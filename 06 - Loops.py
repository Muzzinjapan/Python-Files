## PART 1

start = 10
for row in range(9):
    for column in range(row+1):
        print(start, end=" ")
        start += 1
    print()


## PART 2

print()
print("Part II")
print()
size = input("How big should the box be?")
for side in range(int(size)-1):
    print("oo", end="")
print("oo")
for side in range(int(size)-2):
    print("o", end="")
    for spaces in range(int(size)-2):
        print("  ", end="")
    print("  o")
for side in range(int(size)-1):
    print("oo", end="")
print("oo")

## PART 3

