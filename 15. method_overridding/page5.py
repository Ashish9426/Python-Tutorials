class Number:
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return f"Number [num = {self.__num}]"

    def __eq__(self, other):
        return self.__num == other.__num

    def __gt__(self, other):
        return self.__num > other.__num

    def __ge__(self, other):
        return self.__num >= other.__num

    def __add__(self, other):
        return Number(self.__num + other.__num)

    def __sub__(self, other):
        return Number(self.__num - other.__num)

    def __mul__(self, other):
        return Number(self.__num * other.__num)

    def __truediv__(self, other):
        return Number(self.__num / other.__num)

    def __floordiv__(self, other):
        return Number(self.__num // other.__num)


n1 = Number(100)
n2 = Number(200)
n3 = Number(300)
n4 = Number(400)


print(f"n1 = {n1}, type = {type(n1)}")
print(f"n2 = {n2}, type = {type(n2)}")

print(f"n1 == n2 = {n1 == n2}")
print(f"n1 != n2 = {n1 != n2}")

print(f"n1 > n2 = {n1 > n2}")
print(f"n1 < n2 = {n1 < n2}")

print(f"n1 >= n2 = {n1 >= n2}")
print(f"n1 <= n2 = {n1 <= n2}")

print("-" * 80)

# n1.__add__(n2)
print(f"n1 + n2 = {n1 + n2}")

# n1.__sub__(n2)
print(f"n1 - n2 = {n1 - n2}")

# n1.__mul__(n2)
print(f"n1 * n2 = {n1 * n2}")

# n1.__truediv__(n2)
print(f"n1 / n2 = {n1 / n2}")

# n1.__floordiv__(n2)
print(f"n1 // n2 = {n1 // n2}")


# answer = (n1 + n2) + n3 + n4
# answer = (ans12 + n3) + n4
# answer = (ans123 + n4)
answer = n1 + n2 + n3 + n4

# 10 + 20 + 30 + 40
# 30 + 30 + 40
# 60 + 40
# 100

# str1 = "test10"
# str2 = "test40"
# print(str1 + str2)
