#-*- coding:utf-8 -*-

# # 방법1) 결과는 제대로 나오지만 RuntimeError

# def draw_stars(num):
#     if num == 1:
#         return ['*']

#     else:
#         Stars = draw_stars(num/3)
#         List = []

#         for star in Stars:
#             List.append(star*3)
#         for star in Stars:
#             List.append(star + ' ' * (num/3) + star)
#         for star in Stars:
#             List.append(star*3)
        
#         return List

# num = int(input())
# print('\n'.join(draw_stars(num)))

# 방법2)

num = int(input())
cnt = 0

while num > 3:
    num /= 3
    cnt += 1
# num = 3^(cnt+1)

stars = ["***", "* *", "***"]

def make_stars():
    L = len(stars)
    new_stars = []

    for i in range(L*3):
        if i/L == 1:
            new_stars.append(stars[i%L] + ' '*L + stars[i%L])
        else:
            new_stars.append(stars[i%L]*3)
    
    return new_stars

for i in range(cnt):
    stars = make_stars()

for i in stars:
    print(i)