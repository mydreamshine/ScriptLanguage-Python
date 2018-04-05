import math

print(math.log(100))
print("Test.py file has been changed.")

"""주석구문 이부분은 주석입니다."""
'''이부분은 주석입니다.'''


colors = ['red', 'green', 'blue', 'white', 'gray']


# 끝글자를 기준으로 오름차순 정렬하기

def mysort(x):
    return x[-1]


colors.sort(key=mysort)

print(colors)