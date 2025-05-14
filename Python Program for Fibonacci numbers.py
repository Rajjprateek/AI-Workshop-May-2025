# Python Program for Fibonacci numbers.

n = int(input("Enter the number of terms: "))

f = 0
s = 1

print("Fibonacci sequence:")
print(f, end=", ")
print(s, end=", ")

for _ in range(2, n):
    t = f + s
    print(t, end=", ")
    f = s
    s = t
