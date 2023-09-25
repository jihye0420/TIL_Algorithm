# * 최대공약수 & 최소공배수
from math import gcd

max_gong = gcd(2, 14)  # 최대공약수
min_gong = 2 * 14 // gcd(2, 14)  # 최소공배수
print(max_gong)
print(min_gong)
