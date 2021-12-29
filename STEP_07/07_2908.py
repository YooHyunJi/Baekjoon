num_1, num_2 = input().split()

for i in range(3):
    # 자릿수가 같을 경우 다음 자릿수 비교
    if num_1[2-i] == num_2[2-i]:
        continue
    # num_1의 자릿수가 더 클 경우 num_1의 reverse 출력
    elif num_1[2-i] > num_2[2-i]:
        print("{}{}{}".format(num_1[2], num_1[1], num_1[0]))
        break
    # num_2의 자릿수가 더 클 경우 num_2의 reverse 출력
    else:
        print("{}{}{}".format(num_2[2], num_2[1], num_2[0]))
        break