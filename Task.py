#здесь в задаче не учтены системы счисления 11-15, я бы спросила у ребенка все ли ньюансы он учел
def any_to_ten(s, base):
    b = 1
    ans = 0
    for ch in s[::-1]:
        if ch in "ABCDEF":
            ans += b * (10 + ord(ch) - ord("A"))
        else:
            ans += b * int(ch)
        b *= base
    return ans

a, b = [int(x) for x in input().split()]

if b <= 10:
    print(str(b-1)*a + '_' + str(b))
    print(str(any_to_ten(str(b-1)*a, b)) + '_10')
elif b == 11:
    print("A" * a + '_' + str(b))
    print(str(any_to_ten('A' * a, b)) + '_10')
elif b == 12:
    print("B" * a + '_' + str(b))
    print(str(any_to_ten('B' * a, b)) + '_10')
elif b == 13:
    print("C" * a + '_' + str(b))
    print(str(any_to_ten('C' * a, b)) + '_10')
elif b == 14:
    print("D" * a + '_' + str(b))
    print(str(any_to_ten('D' * a, b)) + '_10')
elif b == 15:
    print("E" * a + '_' + str(b))
    print(str(any_to_ten('E' * a, b)) + '_10')
else:
    print("F" * a + '_' + str(b))
    print(str(any_to_ten('F' * a, b)) + '_10')
