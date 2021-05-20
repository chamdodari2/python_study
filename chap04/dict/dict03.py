# 딕셔너리 선언
dictionary={}
# 요소 추가 전에 내용 출력
print("요소 추가 이전 dictionary>>> ",dictionary)

# 딕셔너리에 요소 추가
dictionary["name"] ="새로운 이름"
dictionary["head"] ="새로운 정신"
dictionary["body"] ="새로운 몸"

#출력
print("요소 추가 이후 dictionary >>>", dictionary)

# 딕셔너리 요소 제거
dictionary2 = {
    "name": "건조망고",
    "type": "당절임"}
print("요소 제거 이전:", dictionary2)
# 딕셔너리의 요소를 제거
del dictionary2["name"]
del dictionary2["type"]

# 요소 제거뒤 출력
print("요소 제거 이후 dictionary >>> ",dictionary2)


# KeyError 예외
dictionary3 = {}
# dictionary3["key"]
print("keyError예외 >> ",dictionary3["key"])


# 딕셔너리 내부에 키가 있는지 확인하기