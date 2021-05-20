# 딕셔너리 선언
dictionary={
    "name":"7D 건조 망고",
    "type" :"당절임",
    "ingredient" : ["망고","설탕","메중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

# 출력한다
print("name:",dictionary["name"])
print("type:",dictionary["type"])
for ingredient in dictionary["ingredient"]:
    print("ingredient:",ingredient)
# print("ingredient:",dictionary["ingredient"])
print("origin:",dictionary["origin"])
print()

# 값을 변경한다
dictionary["name"] = "8D 건조 망고"
print("name:",dictionary["name"])

#  list에서 인덱스를 지정하여 특정 값 출력

