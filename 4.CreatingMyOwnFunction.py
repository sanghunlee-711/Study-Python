#1

def say_hello(): #say_hello는 Function name ()안은 인자
  print("hello") #pirnt function은 ()안에 무언가를 넣는걸 허용
  print("bye")

""" python에서는 {}같은거 안씀 들여쓰기로 함수 안에 포함되어 있다는것을 의미함"""
say_hello() #()를 버튼이라 생각하자.

#2
def plus(a, b):
  print(a + b)

def minus(a, b=0):# b=0은 Default value 임 아무것도 입력안됬을때 임의로 값이 들어감
  print(a - b)

plus(2, 5)
minus(2)

#3
def p_plus(a, b):
  print(a + b)


def r_plus(a, b):
  return a + b # return kills the function


p_result = p_plus(2,3)
r_result = r_plus(2,3) ## Python이 r_plus(2,3)을 지켜보다 이것을 5로 바꿔버림

#4
print(p_result, r_result)


def r_plus(a, b):
  return a + b
  print("soasdkfjlalalalalalalal")
# function 에서 return 한번 사용&* 사용할 경우 그 밑의 것들은 실행 x, return 하는 순간 실행 끝!
r_result = r_plus(2,4)

#5
print(r_result)

def plus(a, b):
  return a + b


result = plus(2 , 4)
print(result)

#print는 화면에 그저 보여주는 용도일뿐 Program은 Print를 신경쓰지 않으며 print로 나타난 값을 쓸 수 X