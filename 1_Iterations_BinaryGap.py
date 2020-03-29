'''
0のときにだけカウントアップ
'''
def solution(N):
    binaryData = bin(N)[2:]
    print(str(binaryData))
    max = 0  
    cnt = 0
    for i in binaryData:
        if i == '1':
            max = max if max > cnt else cnt
            cnt = 0
        else:
            cnt += 1
    return max

print(solution(124100))

