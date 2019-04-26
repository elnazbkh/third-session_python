i = 1
n = 1000000
answer = 0
while i < n:
    answer =  answer + 1 / i ** 2
    i = i + 1
# print(answer)
pi = (answer * 6)**0.5
print("3.14159265359")
print(pi)
