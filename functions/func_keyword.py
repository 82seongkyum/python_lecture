# 함수를 여러번 순서 바꿔 호출 연습(예. v3 맨 앞으로 등)

def para_func(v1, v2, v3=0):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> {hap}")
hap1 = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> {hap1}")

# 교수님 블로그 참조