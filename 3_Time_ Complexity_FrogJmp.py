# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    '''
    X <= Y
    X,Y,D 自然数のみ
    D is Jump Distance    
    Brute Force is... too Bad
    回しちゃだめ。パフォーマンス考えてOrder意識。
    '''
    # jump_cnt = 0
    # posX = X
    # while posX <= Y:
    #     posX += D
    #     jump_cnt += 1
    # return jump_cnt
    
    # 割って試すのが良さげ
    # ジャンプ不要
    if X == Y:
        return 0
    # 1ジャンプ
    if  D + X >= Y:
        return 1
    # nジャンプ
    remaining = Y - X
    return -(-remaining // D)

    
# solution(10,85,30)
print(solution(1,1,1)) # 0
print(solution(1,4,2)) # 2
print(solution(10,85,30)) # 3
print(solution(10,80,35)) # 2
print(solution(10,81,35)) # 3
print(solution(1,1000000000,2)) # 
print(solution(1,1000000000,1)) # 
print(-(-1 // 100))