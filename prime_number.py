import math
n = 100
prime_num = [2]
for i in range(3, n+1, 2):
    flag = False
    max = math.ceil(math.sqrt(i))  # 先求开方
    for j in prime_num:
        if i % j == 0:  # 是合数
            flag = True
            break
        if j >= max:  # 大于开方还不可以整除就是质数
            flag = False
            break
    if not flag:
        prime_num.append(i)
print(prime_num)
