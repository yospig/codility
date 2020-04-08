# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if len(A) == 0:
        return A
    for _ in range(K):
        A.insert(0, A.pop(len(A)-1))
    return A