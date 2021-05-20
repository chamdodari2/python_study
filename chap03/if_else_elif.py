# 입력을 받습니다
from main import print_hi

number = input("정수 입력 > ")
number = int(number)
# 짝수 조건
if number % 2 ==0:
    print('짝수입니다')
# 홀수 조건
if number % 2==1:
    print('홀수입니다.')



# else 조건문의 활용
# 입력을 받습니다
number = input('정수 입력하세요')
number = int(number)

#조건문을 사용합니다
if number %2 ==0:

# 조건이 참일 때, 즉 짝수 조건
    print('짝수입니다.')
# 조건이 거짓일 때, 즉 홀수 조건
else:
    print('홀수입니다')
    
    
    
    
# else 구문
# 날짜 시간과 관련된 기능을 가져옵니다
import datetime
# 현재 날짜/시간을 구하고 쉽게 사용할 수 있게 월을 변수에 저장합니다
now =datetime.datetime.now()
month = now.month

# 조건문으로 계절을 확인합니다.
if 3 <=month<=5:  #3이상 5 이하냐
    print('현재는 봄입니다')
elif 6 <= month <= 8:
    print('현재는 여름입니다.')
elif 9 <= month <=11:
    print('현재는  가을입니다.')
else:
    print('현재는 겨울입니다.')