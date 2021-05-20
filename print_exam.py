print("#하나만 출력")
print()
print("#하나만 출력2" ,"abce", sep="\n", end="\n\n")
print("결과",end="\n\n")

print(type('하나만'),type("하나만"),type(12),type(12.5),sep='\n',end='\n\n')

# print("안녕하세요" + '1' )

print("안녕하세요"[0])
print()
print("안녕하세요"[0:4],end='\n')
print("안녕하세요"[:3])#없으면 0 부터 시작
print("안녕하세요"[3:])#3부터 끝까지

hello ="안녕하세요"
print(type(hello), hello[:2],hello,sep='\n',end='\n\n')
res = input("답을 이야기하시오")
print("입력한 답은 " ,res)


a = "10 11 a b 14".split(" ")
print(type(a), a, sep='\n')



x,y,z = 10, 20 , 30
print(x,y,z, sep='\n',end='\n')

x,y = y,x

print(x,y, sep='\n',end='\n')
