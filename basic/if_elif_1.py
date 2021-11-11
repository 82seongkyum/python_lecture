a = int(input("당신의 중간고사 성적을 입력하시오"))

if a>=90:
    print(f"({a}점수는 A학점에 해당합니다.")
elif(a>=80):
    print(f"({a}점수는 B학점에 해당합니다.")
elif(a>=70):
    print(f"({a}점수는 C학점에 해당합니다.")
elif(a>=60):
    print(f"({a}점수는 D학점에 해당합니다.")
else :
    print(f"계절학기를 들으세요.")