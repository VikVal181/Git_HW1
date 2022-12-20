# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check(X,Y,Z):
    return (not(X or Y or Z) == (not(X) and not(Y) and not(Z)))

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            print(f'For X={X} Y={Y} Z={Z} is {check(X,Y,Z)}')
