for value in range(1,5):
    print(value)
numbers=list(range(1,14,2))
print(numbers)
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares2=[value**2 for value in range(1,13)]
print(squares2)
