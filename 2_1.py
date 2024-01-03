def solution(food):
    answer = ''

    # def left_function(food):
    #     left = ''
    #     for i, lx in enumerate(food):
    #         if i == 0:
    #             pass
    #         else:
    #             left += int(lx/2)*str(i)
    #     return left

    def left_function(food):
        left = ''
        for i, lx in enumerate(food):
            left += int(lx/2)*str(i)
        return left

    answer = left_function(food)+'0'+left_function(food)[::-1]
    return answer


print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
