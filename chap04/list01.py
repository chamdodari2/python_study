from builtins import print

list_1 = [1,2,3]
list_2 =  [4,5,6]
# 출력합니다
print('#리스트')
print('list_1= ' , list_1)
print('list_2 = ' , list_2)
# 기본 연산자
print("#리스트 기본 연산자")
print('list_1+list_2 = ',list_1+list_2)
print('list_1*3 = ',list_1*3)
print()
# 함수
print('#길이 구하기')
print('len(list_1) = ',len(list_1))

# 리스트 뒤에 요소 추가하기
print()
list_1.append(4)
list_1.append(5)
print(list_1)

# 리스트 중간에 요소 추가하기
print()
list_1.insert(0,10)
print(list_1)