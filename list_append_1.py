aa = []
bb = []
value = 0

for i in range(0,100):
    aa.append(value)
    value +=2

for i in range(0, 100):
    bb.append(aa[99-i])

print(f"bb[0]에는 %d, bb[99]에는 %d 입력")