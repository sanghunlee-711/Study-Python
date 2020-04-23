days = ("Mon", "Tue", "Wed", "Thu","Fri")

for day in days:
  if day is "Wed":
    break
  else:
    print(day)
    
#day는 변수로 Mon이 들어갈 수도 Tue가 들어갈 수도 있음. 변수는 계속 값이 바뀔 수 있으며 현재 작업하는 item에 따라 값이 바뀔수도 있음
#days는 배열의 이름임.
"""for은 string, tuple,list 같이 배열의 요소를 순차적으로
가리킨다"""
"""
days = ("Mon", "Tue", "Wed", "Thu","Fri")

for letter in "nicolas":
  print(letter)
"""