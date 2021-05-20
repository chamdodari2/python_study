for i in range(5):
    print(str(i) + "=반복 변수")
    print()
    
for i in range(5,10):
        print(str(i) + "=반복 변수")
print()

for i in range(0,10,3):
    print(str(i) + "=반복 변수")
    print()



array = [273,32,103,57,52]

for i in range(len(array)):
    print("{}번째 반복 : {}".format(i,array[i]))


for i in range(4,0 -1, -1):
    print("현재 반복 변수: {}".format(i))

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))

# for 반복문처럼 사용하기



# 확인문제 2. 빈칸을 채워 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리를 만들어보세요.
key_list = ("name", "hp", "mp", "level")
value_list = ("기사", 200, 30, 5)
character={}
# character={"name": "기사", "hp": "200","mp": "30", "level":  5}
for i in range(0,len(key_list)):
    character[key_list[i]] = value_list[i]
#최종출력
print(character)


# 1부터 숫자를 하나씩 증가시키면서 더하는 경우를 생각해 봅시다. 몇을 더할 때 1000을 넘는지 구해보세요. 그리고 그때의 값도 출력해보세요. 다음은 10000이 넘는 경우를 구한 예입니다.
limit =10000
i = 1
sum_value=0
while sum_value <limit:
    sum_value +=i
    i+=1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {} 입니다.".format(i-1,limit,sum_value))


# 1부터 100까지의 숫자가 있다고 할떄, 이를 다음과 같이 계산한다고 했을 때 최대가 되는 경우는 어떤 숫자를 곱헀을 때인지를 찾아 주세요.
max_value=0
a = 0
b = 0
for i in range(1,100//2+1):
    j=100-i

current=i*j
if max_value < current:
    a=i
    b=j
    max_value=current

print("최대가 되는 경우 : {}*{}={}".format(a,b,max_value))