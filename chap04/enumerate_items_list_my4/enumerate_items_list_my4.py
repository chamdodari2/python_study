list_a =[1,2,3,4,5]
list_reversed  = reversed(list_a)

print("# reversed()함수")

print(list_reversed)
print(list(list_reversed))
print()

for i in reversed(list_a):
    print("-",i)


numbers = [1,2,3,4,5,6]

for i in reversed(numbers):
    print("첫 번째 반복문 : {}".format(i))


for i in reversed(numbers):
    print("두 번쨰 반복문: {}".format(i))
    
    
example_list = ["요소A","요소B","요소C"]
i=0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i,item))
    i += 1



print("#반복문과 조합하기")
for i,value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))


example_dictionary={
    "키A":"값A",
    "키B":"값B",
    "키C":"값C",
}

for key,element in example_dictionary.items():
    print("dictionary[{}]= {}".format(key,element))


    array=[]

for i in range(0,20,2):
    array.append(i*i)
print(array)

array2 =[i*i for i in range(0,20,2)]

print(array2)

array3 = ["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array3 if fruit !="초콜릿"]

print(output)



# 2진수, 8진수, 16진수로 변환

