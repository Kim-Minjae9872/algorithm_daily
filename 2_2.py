import numpy

seoul = ["Jane", "Kim"]
seoul = numpy.array(seoul)


def solution(seoul):
    kim = numpy.where(seoul == 'Kim')[0][0]
    answer = f'김서방은 {kim}에 있다'
    return answer


b = ['hi', 'hello', 'bye', 'hello', 'hi']
print(type(b))

b = numpy.array(b)
print(type(b))

print(numpy.where(b == 'hello')[0])
print(solution(seoul))
