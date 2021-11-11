# # 전역변수 & 지역변수
# # a = 10
# # b = 20
# # def print_var():
# #     b = 30
# #     print(a+b)

# # print_var()

# a = 10
# b = 20
# def print_var():
#     b = 30
#     return a+b

# print_var()

def add_1(n):
    return n + 1

target = [1,2,3,4,5]

result = list(map(add_1, target))

print(result)