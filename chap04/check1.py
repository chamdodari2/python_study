# 0~100까지 짝수만 list_1에 저장하고 출력하시오
# 0~100까지 홀수만 list_2에 저장하고 출력하시오
list_1 =[]
list_2 =[]
for i in range(101):
    if i %2 ==0:

        list_1.append(i)
    else:
        list_2.append(i)
print(list_1)
print(list_2)