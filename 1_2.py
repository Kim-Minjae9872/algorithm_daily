def solution(s):
    answer = ''
    a = sorted(s, reverse=True)
    answer = answer.join(a)
    return answer


print(solution("Zbcdefg"))
print(solution("ZbcAebOFg"))
