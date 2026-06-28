# 1 задача

# n = int(input())
# k = int(input())
# s1 = n + k
# while s1 >= 24 * 60 * 60:
#     s1 -= 24 * 60 * 60
# for x in range(24):
#     if s1 - 60 * 60 * x >= 0:
#         a = x
#         s2 = s1 - 60 * 60 * x
#     else:
#         break
# for y in range(60):
#     if s2 - 60 * y >= 0:
#         b = y
#         c = s2 - 60 * y
#     else:
#         break
# print(a, b, c)

# n = int(input())
# k = int(input())
# s = (n + k) % 24 * 60 * 60
# a = s // (60 * 60)
# b = s % (60 * 60) // 60
# c = s % 60
# print(a, b, c)
