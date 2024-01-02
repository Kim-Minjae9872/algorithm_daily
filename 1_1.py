def solution(left, right):
    answer = 0
    for x in (range(left, right+1)):
        if int(x**0.5) == x**0.5:
            answer -= x
        else:
            answer += x

    return answer


print(solution(13, 17))
print(solution(24, 27))
