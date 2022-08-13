L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

maths = A/C
if (maths - A//C) !=0:
    maths = (A//C)+1
else:
    maths = A/C
korean = B/D
if (korean - B/D) !=0:
    korean = (B//D)+1
else:
    korean = B/D

print(int(L-max(maths, korean)))