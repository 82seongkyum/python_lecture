# 함수 선언
def func1():
    global a # 이 함수 안에서 a는 전역변수
    a = 10
    print("func1()에서 a값 %d" %a)

def func2():
    print("func2()에서 a값 %d" %a)

# 함수 변수 선언
a = 20

# 메인코드
func1()
func2()
print(a)
# 메인코드 주석처리하면 결과값 20