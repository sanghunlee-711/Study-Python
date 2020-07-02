# 인사로봇
number = 20
greeting = "안녕하세요"
place = "words and format"
welcome ="Welcome!"

#old version

print(number, "th guest", greeting, "." ,place, "come here", welcome)

base = '{}번 손님, {}. {}에 오신것을 {}!'
new_way = base.format(number, greeting, place, welcome)#format은 base와 같이 문자열에 사용할수 있는 기능임.
print(base)
print(new_way)


mine = "cysers"
yours="rocks"
results = "Lose"

print("I do {} you do {} ,So I {}".format(mine, yours, results))