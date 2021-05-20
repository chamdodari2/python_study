# 반복문 내부에 if조건문의 조건식을 채워서 100이상의 숫자만 출력하게 만들어 보세요.




list_1 = [273,32,103,'문자열',True,False]
list_2  = [i for i in list_1]
print(type(list_2),list_1)

# 1~100까지 짝수만
list_1 = [i for i in range(101) if i % 2 ==0]
print('짝수만',list_1)
# 1~100까지 홀수만
list_1 = [i for i in range(101) if i % 2 ==1]
print('홀수만',list_2)
# 확인문제
numbers=[273,103,5,32,65,9,72,800,99]
numberTo100 = [i for i in numbers if i >= 100]
print('numbers 에서 100 이상의 수', numberTo100)


# 4. 숫자를 하나하나 출력시키기
list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
for sub_list in list_of_list:
        for i in sub_list:
                print(i)


#
list_seq = [i for sub_list in list_of_list for i in sub_list]
print('list_seq',list_seq)