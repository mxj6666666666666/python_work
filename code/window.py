#窗口显示   要留一个文本框来输入方程,里面应有输出输入的函数的函数

import tkinter as tk
from tkinter import messagebox

def close_window(event=None):
    # 关闭窗口
    root.destroy()

def calculate_equation():
    #获取方程式
    equation = equation_entry.get()

    if equation:
        try:
            result = eval(equation)
            result_label.config(text=f"输入的方程式: {equation}\n 计算结果: {result}")
        except Exception as e:
            result_label.config(text=f"错误: {e}")
    else:
        result_label.config(text="请输入方程式")

def clear_input():
    equation_entry.delete(0,tk.END)
    result_label.config(text="")

def show_window():
    global root,equation_entry,result_label,main_frame,calculate_button,clear_button

    root = tk.Tk()
    root.title("方程式计算机")
    root.geometry("1000x1000")
    #按下w或esc时关闭窗口
    root.bind('<w>',close_window)
    root.bind('<Escape>',close_window)
    #设置窗口居中
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    #创建主框架
    main_frame = tk.Frame(root,padx=20,pady=20)
    main_frame.pack(expand=True,fill=tk.BOTH)

    show_first_window()

    root.mainloop()


def show_first_window():

    #标题:
    title_label = tk.Label(main_frame,text="方程式计算机",font=("Arial",18,"bold"))
    title_label.pack(pady=(50,20))

    #输入标签
    input_label = tk.Label(main_frame,text="请输入方程式:")
    input_label.pack(pady=(0,5))

    #方程式输入框
    equation_entry = tk.Entry(main_frame)
    equation_entry.pack(pady=(0,20))
    equation_entry.focus()

    #按钮框架
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=(0,20))

    #计算按钮
    calculate_button = tk.Button(button_frame,text="计算",command=calculate_equation)
    calculate_button.pack(side=tk.LEFT,padx=(0,10))

    #清空按钮
    clear_button = tk.Button(button_frame,text="清空",command=clear_input)
    clear_button.pack(side=tk.LEFT)

    #文件按钮
    file_button = tk.Button(button_frame,text="文件",command=show_second_windows)
    file_button.pack(side=tk.LEFT)

    #结果显示区域
    result_frame = tk.LabelFrame(main_frame,text="结果",font=("Arial",12,"bold"),padx=10,pady=20)
    result_frame.pack(fill=tk.BOTH,expand=True)

    result_label = tk.Label(result_frame,text="",font=("Arial",12),justify=tk.LEFT,wraplength=500)
    result_label.pack(pady=20)

    #绑定回车键进行计算
    root.bind('<Return>', lambda event: calculate_equation())
    root.bind('<KP_Enter>', lambda event: calculate_equation())
    root.bind('<x>', lambda event: clear_input())

def clear_all_widgets():
    # 获取窗口中的所有组件
    for widget in root.winfo_children():
        widget.destroy()

def show_second_windows():
    clear_all_widgets()
    #创建主框架
    main_frame = tk.Frame(root,padx=20,pady=20)
    main_frame.pack(expand=True,fill=tk.BOTH)

    #标题:
    title_label = tk.Label(main_frame,text="方程式计算机-文件版",font=("Arial",18,"bold"))
    title_label.pack(pady=(50,20))

show_window()