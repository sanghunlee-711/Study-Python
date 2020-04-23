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