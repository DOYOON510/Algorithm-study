# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i%divisor==0:
#             answer.append(i)
#     answer.sort()
#     if answer==[]:
#         answer.append(-1)
#     return answer

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]