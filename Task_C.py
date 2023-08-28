k, n = [int(x) for x in input().split()]
inp = input().split()

for i in range(len(inp)):
    if int(inp[i]) % 2 != 0:
        inp[i] = "0"
inp.sort(reverse=True)
print(*inp)  #эта строчка не нужна, так как нам не надо видеть обратную сортировку, в которой мы будем видеть четные числа из списка
ab = 0
for i in range(k):
    ab += int(inp[i])
print(ab)