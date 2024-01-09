def solution(n):
    def ternary_function(x):
        ternary = ''
        while x // 3 > 0:
            if x % 3 == 2:
                x = x//3
                ternary += str(2)
                continue
            elif x % 3 == 1:
                x = x//3
                ternary += str(1)
                continue
            elif x % 3 == 0:
                x = x//3
                ternary += str(0)
                continue
        ternary += str(x)
        return ternary

    answer = 0
    i = len(ternary_function(n)) - 1
    for a in ternary_function(n):
        answer += int(a) * (3 ** i)
        i -= 1
    return answer


print(solution(45))
print(solution(125))
print(solution(4839))
