def overlaps(rect1, rect2):
    ax1, ay1, ax2, ay2 = rect1
    bx1, by1, bx2, by2 = rect2

    if ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2:
        return False
    else:
        return True


print(overlaps((0,0,5,5), (3,3,7,7)))
print(overlaps((0,0,5,5), (5,0,10,5)))
print(overlaps((0,0,5,5), (6,6,10,10)))
print(overlaps((0,0,5,5), (1,1,2,2)))