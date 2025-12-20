import sympy as sp

def convert(func_str):   #将字符串转化为为系数数组
    x = sp.Symbol('x')
    expr = sp.sympify(func_str)
    poly = sp.Poly(expr, x)
    return poly.all_coeffs()  # 返回系数数组