from math import ceil

def paint(h, w, coverage):
    area = h*w
    can = area / 5
    return ceil(can)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(paint(test_h,test_w,coverage))