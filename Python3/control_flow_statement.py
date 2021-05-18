money=int(input("금액을 입력하세요:"))

if(money>=5000):
    print("아웃백")
elif(money>=3000):
    print("학식")
elif(money>=2000):
    print("컵라면")
else:
    print("공기밥")

activity = input("너 동아리 뭐해? : ")
if(activity=="멋쟁이사저처럼"):
    print("어, 너도 멋사야?")
else:
    print("..그래..")

for score in [96,98,100,87]:
    print(score)

sum = 0
for number in [1,2,3,4,5,6,7,8,9,10]:
    sum +=number
    print(sum)

# range(x,y) >> x이상 y미만의 수 리스트로 반환
# range(x) >> 0부터 x미만의 수 리스트로 반환

for number in range(1,11):
    sum +=number
    print(sum)

num=10
while(num>0):
    print("반복문 수행 중")
    num=num-1

# while(True): 무한루프문, break로 탈출
