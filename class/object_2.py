class Car: # 클레스선언
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

# 메인코드
myCar1 = Car() 
myCar1.color = "빨강"
myCar1.speed = 0
# 예) myCar1 = Car("빨강", 0)
myCar2 = Car() 
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car() 
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 ")

myCar2.upSpeed(30)
print

myCar3.upSpeed(30)
print