# 한 글자로 처리할 크로아티아 알파벳 모음
exception = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sentence = input()

# 원문의 크로아티아 알파벳을 X로 변경
for i in exception:
    sentence = sentence.replace(i, 'X')

print(len(sentence))


# # 처음에 시도한 방법 .. 이건 왜 안 됐지? 예제랑 답은 똑같은데
# sentence = input()
# exception = 0
# flag_1 = False
# flag_2 = False

# print(sentence[::-1])

# # lj, nj 모두 마지막 글자가 j이기 때문에 flag를 하나만 사용하기 위해 문자열 reverse
# for i in sentence[::-1]:
#     # Exception 2) dz인 경우 한 글자로 카운트 되기 때문에 제외될 글자 수 increase, flag_1 off
#     if flag_1 == True:
#         if i == 'd':
#             exception += 1
#         flag_1 = False
    
#     # Exception 3) lj, nj인 경우 한 글자로 카운트 되기 때문에 제외될 글자 수 increase, flag_2 off
#     elif flag_2 == True:
#         if i == 'l' or i == 'n':
#             exception += 1
#         flag_2 = False

#     # Exception 1) 특수 문자
#     elif i == '=' or i == '-':
#         exception += 1
    
#     # Exception 2) dz 판단 위한 z 입력되면 flag_1 on
#     elif i == 'z':
#         flag_1 = True
    
#     # Exception 3) lj, nj 판단 위한 j 입력되면 flag_2 on
#     elif i == 'j':
#         flag_2 = True

# print(len(sentence) - exception)