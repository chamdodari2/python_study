
# 인덱스로 제거하기 : del, pop
# 리스트의 요소 하나 제거하기
list_1 =[0,1,2,3,4,5]
# 제거방법1 - del
del list_1 [1]
print('del list_1[1]:',list_1)

# 제거방법 2 - pop
list_1.pop(2)
print('pop(2):',list_1)

# 값으로 제거하기  - remove
list_1.remove(5)
print(list_1)

# 리스트의 모든 요소 제거  : clear
list_1.clear()
print(list_1)
