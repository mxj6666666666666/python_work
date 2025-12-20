import window   # 窗口显示   要留一个文本框来输入方程,里面应有输出输入的函数
import convert_func  #将字符串转化为数组数组
import image    # 显示原函数图像
import zero     # 计算函数有没有零点,有则输出零点,无则输出零
import integral # 求函数积分 , 输出:函数的积分方程
import derivative # 求函数导数 , 输出:函数的导数方程
import tkinter as tk

def interface():
    root = tk.Tk()
    root.title("函数处理")
    root.geometry("1200x800")

    label1 = tk.Label(root, text="请输入函数：", font=("Arial", 30))
    label1.place(x=100, y=100)
    e1 = tk.Entry(root, font=("Arial", 30))  #输入函数
    e1.place(x=400, y=100)
    e2 = tk.Entry(root, font=("Arial", 30))  #输出零点
    e2.place(x=400, y=320)


    def draw_func():
        func_str = e1.get()
        coe=convert_func.convert(func_str)
        image.draw_function(coe)

    def find_zero():
        func_str = e1.get()
        coe = convert_func.convert(func_str)
        real_roots = zero.zero(coe)
        if real_roots == 0:
            e2.delete(0, "end")
            e2.insert("end","该函数没有零点")
        else:
            e2.delete(0, "end")
            e2.insert("end","零点为：")
            for i in real_roots:
                e2.insert("end",str(i)+"  ")

    b1=tk.Button(root, text="绘制函数图像", font=("Arial", 30),command=draw_func)
    b1.place(x=100, y=200)
    b2=tk.Button(root, text="求函数零点", font=("Arial", 30),command=find_zero)
    b2.place(x=100, y=300)

    root.mainloop()

