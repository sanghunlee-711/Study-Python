import math 
"""
이러면 사용하지 않는 모든 기능을 
다 import해버림. 
쓸것만 Import하는 게 중요함."""

print(math.ceil(1.2))
print(math.fabs(-1.2))

from math import ceil, fsum
"""이렇게 뽑아오면 됨 ㅋ"""
print(ceil(1.2))
print(fsum([1, 2, 3, 4, 5, 6, 7]))


from math import ceil, fsum as sexy_sum


print(sexy_sum([1, 2, 3, 4, 5, 6, 7]))

"""
이런식으로 import하는 함수 이름을 바꿀 수 도 있음.
"""
"""
ex)
1. main.py
from calculator import plus, minus

print(plus(1,2), minus(1,2))

2.calculator.py

def plus(a, b):
  return a + b


def minus(a,b):
  return a - b
"""
# 위와 같이 다른 py에서 정의한 함수를 끌어올 수 있음!.
