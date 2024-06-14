import math

def trapezoidal_rule(f, a, b, n):
    dx = (b - a) / n
    x = [a + i * dx for i in range(n + 1)]
    y = [f(xi) for xi in x]
    area = (y[0] + y[-1]) / 2
    area += sum(y[1:-1])
    area *= dx
    return area

# 使用者輸入
a = float(input("請輸入區間的起點 a: "))

b = float(input("請輸入區間的終點 b: "))
n = int(input("請輸入區間切分的段數 n: "))

# 計算積分
area = trapezoidal_rule(math.sin, a, b, n)
print(f"函數 sin(x) 在區間 [{a}, {b}] 與 x 軸包圍的面積近似值為: {area:.2f}")
