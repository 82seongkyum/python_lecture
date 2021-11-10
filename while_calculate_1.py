c = ""
while True :
    a = int(input("계산할 첫번째 수를 입력하세요 : "))
    b = int(input("계산할 두번째 수를 입력하세요 : "))
    c = input("계산할 연산자를 입력하세요 : ")
    if(c == "+"):
        print(f'{a}+{b} = {a+b}')
    elif(c == "-"):
        print(f'{a}-{b}= {a-b}')
    elif(c == "*"):
        print(f'{a}*{b}, {a*b}')
    elif(c == "/"):
        print(f'{a}/{b}, {a/b}')
    elif(c == "%"):
        print(f'{a}%{b}, {a%b}')
    elif(c == "//"):
        print(f'{a}//{b}, {a//b}')
    elif(c == "**"):
        print(f'{a}**{b}, {a**b}')
    else : 
        print("연산자를 잘못 입력했습니다.")
d = input("종료하시려면 'q'를 입력해주세요.")
    if(d == "q"):
        break