# 딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
# 사용자로부터 입력받기
key = input(">접근하고자 하는 키 : ")
# 출력쓰
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# get()함수
# 존재하지 않는 키에 접근해보기
value = dictionary.get("존재하지 않는 키")
print("값:", value)

# None 확인 방법
if None == value:
    print("존재하지 않는 키에 접근했었습니다.")
# 반복문과 딕셔너리

for key in dictionary:
    print(key, ':', dictionary[key])


# 다음 빈칸을 채워서 numbers 내부에 들어있는 숫자가 몇번 등장하는지를 출력하는 코드를 작성해 보세요.
numbers = {1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3}
counter = {}
for number in numbers:
    if None != number:
        counter
        print()
counter = {}

# 최종출력
print(counter)


#
# list_2 =[]
# for i in range(101):
#     if i %2 ==0:
#
#         list_1.append(i)
#     else:
#         list_2.append(i)
# print(list_1)
# print(list_2)