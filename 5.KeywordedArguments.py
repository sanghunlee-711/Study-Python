def plus(a, b):
  return a - b
result = plus(b=30, a=1)
print(result)

#keyword argument로 할당해줄 수 있음 ex) b=30, a =1

def say_hello(name, age):
  return "Hello name you are age years old"

hello = say_hello("nico", "12")
print(hello)

#return 의 모든 값이 그대로 나올것 (변수를 포함안해줘서임)


def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello("nico", "12")
print(hello)

#f for format

#->Hello nico you are 12 years old라고 출력됨[변수설정의 힘]


def say_hello(name, age):
  return "Hello" + name + "you are" + age + "years old"

hello = say_hello( name= "nico", age = "12")
print(hello)


