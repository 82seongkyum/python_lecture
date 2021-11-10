food = {"떡복이":"오뎅", 
        "짜장면":"단무지", 
        "라면":"김치", 
        "피자":"피클", 
        "맥주":"땅콩", 
        "치킨":"치킨무", 
        "삼겹살":"상추"
        };

while(True):
    myfood = input(str(list(food.keys()))+"중 좋아하는 음식은?")
    if myfood in foods :
        print()
    elfi myfood == "끝":
        break
    else :
        print("그런 음식이 없습니다. 확인해 보세요.")