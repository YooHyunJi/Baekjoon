h, m = map(int, input().split())

# 기존 설정한 시간의 분이 45 이상일 때 -> 분만 계산
if m >= 45:
    m_mod = m - 45
    h_mod = h

# 기존 설정한 시간의 분이 45 미만일 때 -> 분과 시간 모두 계산
else:
    m_mod = m + 60 - 45
    # 기존 설정한 시간의 시가 0일 때는 예외적으로 처리
    if h == 0:
        h_mod = 23
    else:
        h_mod = h - 1

print(h_mod, m_mod)