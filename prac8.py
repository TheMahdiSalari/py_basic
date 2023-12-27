n = int(input("Enter the line number :"))
m = int(input("Enter the column number :"))
matrix = []
sum = 0
for i in range(n) :
    member = []
    for j in range(m) :
        print(i , j)
        x = float(input("Enter the member :"))
        member.append(x)
    matrix.append(member)
print(matrix)
print("-------------------")
for r in matrix :
    print(r)
print("-------------------")
for i in range(n) :
    for j in range(m) :
        if i == j :
            sum = sum + matrix[i][j]
print("Sum of diameters =", sum)