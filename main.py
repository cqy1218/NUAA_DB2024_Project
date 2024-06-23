import pymysql
import sys
from tkinter import *
from tkinter import ttk


# 连接数据库函数
def con():
    con_con = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password="1218",
            database="dbtest",
            charset='utf8')
    db = con_con.cursor()
    return con_con, db

# 断连数据库函数
def db_close(con_con, db):
    con_con.close()
    db.close()


# 增加功能函数
def add(con_con, db):
    # 存入数据
    def add_ok():
        data = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()]
        # print("已读入数据：", data)
        db_add(con_con, db, data)
        root.destroy()

    root = Tk()
    root.title("添加数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")    # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1, sticky='we', **padding)
    Label(root, text="成绩：").grid(row=2, column=0, sticky='e', **padding)
    entry3 = Entry(root)
    entry3.grid(row=2, column=1, sticky='we', **padding)
    Label(root, text="学期：").grid(row=3, column=0, sticky='e', **padding)
    entry4 = Entry(root)
    entry4.grid(row=3, column=1, sticky='we', **padding)
    Label(root, text="教学班：").grid(row=4, column=0, sticky='e', **padding)
    entry5 = Entry(root)
    entry5.grid(row=4, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="确定添加", command=add_ok).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    root.mainloop()


# 数据库添加函数
def db_add(con_con, db, data):
    try:
        db.execute("INSERT INTO SC(SNO, CNO, GRADE, SEMESTER, TEACHINGCLASS) VALUES('%s', '%s', '%s', '%s', '%s')"
                   % (data[0], data[1], data[2], data[3], data[4]))
        con_con.commit()
        add_right()
    except:
        add_wrong()


# 添加成功弹窗函数
def add_right():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("添加数据")
    Label(root1, text='添加成功！', fg='blue', width=20, height=6, anchor='c').pack()


# 添加失败弹窗函数
def add_wrong():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("添加数据")
    Label(root1, text='添加失败！', fg='red', width=20, height=6, anchor='c').pack()


'''
# 增加功能函数
def add():
    flag = True
    while (flag):
        print()
        # 数据输入
        print("请输入插入数据：")
        sno = input("学号Sno：")
        cno = input("课程号Cno：")
        grade = input("成绩Grade：")
        semester = input("学期Semester：")
        teachingclass = input("教学班Teachingclass：")
'''


# 删除功能函数
def delete(con_con, db):
    def del1(con_con, db):
        root.destroy()
        delete_sc(con_con, db)

    def del2(con_con, db):
        root.destroy()
        delete_s(con_con, db)


    def del3(con_con, db):
        root.destroy()
        delete_c(con_con, db)


    # 设置窗口大小以屏幕居中
    root = Tk()
    root.title("删除数据")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    Label(root, text="请选择删除模式").grid(row=0, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="精确单删", command=lambda: del1(con_con, db))
    button.grid(row=1, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="学号统删", command=lambda: del2(con_con, db))
    button.grid(row=2, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="课程统删", command=lambda: del3(con_con, db))
    button.grid(row=3, column=0, columnspan=2, sticky="nsew")
    root.grid_columnconfigure(0, weight=1)  # 设置网格权重以垂直居中
    root.mainloop()


# 删除成功弹窗函数
def del_right():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("删除数据")
    Label(root1, text='删除成功！', fg='blue', width=20, height=6, anchor='c').pack()

# 删除失败弹窗函数
def del_wrong():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("删除数据")
    Label(root1, text='删除失败！', fg='red', width=20, height=6, anchor='c').pack()


# 精确单删函数
def delete_sc(con_con, db):
    # 存入数据
    def del_ok():
        data = [entry1.get(), entry2.get()]
        db_del1(con_con, db, data)
        root.destroy()

    # 设置窗口大小以屏幕居中
    root = Tk()
    root.title("精确单删")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="确定删除", command=del_ok).grid(row=2, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    root.mainloop()

# 精确单删数据库函数
def db_del1(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE SNO='%s' AND CNO='%s'"
                   % (data[0], data[1]))
        if db.rowcount == 0:
            del_wrong()
        else:
            db.execute("DELETE FROM SC WHERE SNO='%s' AND CNO='%s'"
                       % (data[0], data[1]))
            con_con.commit()
            del_right()
    except:
        del_wrong()


# 学号统删函数
def delete_s(con_con, db):
    # 存入数据
    def del_ok():
        data = [entry1.get()]
        db_del2(con_con, db, data)
        root.destroy()

    # 设置窗口大小以屏幕居中
    root = Tk()
    root.title("学号统删")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="确定删除", command=del_ok).grid(row=1, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    root.mainloop()

# 学号统删数据库函数
def db_del2(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE SNO='%s'"
                   % (data[0]))
        if db.rowcount == 0:
            del_wrong()
        else:
            db.execute("DELETE FROM SC WHERE SNO='%s'"
                       % (data[0]))
            con_con.commit()
            del_right()
    except:
        del_wrong()


# 课程统删函数
def delete_c(con_con, db):
    # 存入数据
    def del_ok():
        data = [entry1.get()]
        db_del3(con_con, db, data)
        root.destroy()

    # 设置窗口大小以屏幕居中
    root = Tk()
    root.title("课程统删")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="课程号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="确定删除", command=del_ok).grid(row=1, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    root.mainloop()

# 课程统删数据库函数
def db_del3(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE CNO='%s'"
                   % (data[0]))
        if db.rowcount == 0:
            del_wrong()
        else:
            db.execute("DELETE FROM SC WHERE CNO='%s'"
                       % (data[0]))
            con_con.commit()
            del_right()
    except:
        del_wrong()


# 修改功能函数
def modify(con_con, db):
    # 存入数据
    def findddd():
        data = [entry1.get(), entry2.get()]
        root.destroy()
        find(con_con, db, data)

    root = Tk()
    root.title("修改数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="查询", command=findddd).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    root.mainloop()


# 真实修改函数
def mod(con_con, db, results):
    # 存入数据
    def mod_ok():
        data = [results[0][0], results[0][1], entry3.get(), entry4.get(), entry5.get()]
        db_mod(con_con, db, data)
        root.destroy()

    root = Tk()
    root.title("修改数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    Label(root, text=results[0][0]).grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    Label(root, text=results[0][1]).grid(row=1, column=1, sticky='we', **padding)
    Label(root, text="成绩：").grid(row=2, column=0, sticky='e', **padding)
    entry3 = Entry(root)
    entry3.grid(row=2, column=1, sticky='we', **padding)
    Label(root, text="学期：").grid(row=3, column=0, sticky='e', **padding)
    entry4 = Entry(root)
    entry4.grid(row=3, column=1, sticky='we', **padding)
    Label(root, text="教学班：").grid(row=4, column=0, sticky='e', **padding)
    entry5 = Entry(root)
    entry5.grid(row=4, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="确定修改", command=mod_ok).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    root.mainloop()

# 数据库修改函数
def db_mod(con_con, db, data):
    try:
        db.execute("DELETE FROM SC WHERE SNO='%s' AND CNO='%s'"
                   % (data[0], data[1]))
    except:
        mod_wrong()
    try:
        db.execute("INSERT INTO SC(SNO, CNO, GRADE, SEMESTER, TEACHINGCLASS) VALUES('%s', '%s', '%s', '%s', '%s')"
                   % (data[0], data[1], data[2], data[3], data[4]))
        con_con.commit()
        mod_right()
    except:
        mod_wrong()


# 修改成功弹窗函数
def mod_right():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("修改数据")
    Label(root1, text='修改成功！', fg='blue', width=20, height=6, anchor='c').pack()


# 修改失败弹窗函数
def mod_wrong():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("修改数据")
    Label(root1, text='修改失败！', fg='red', width=20, height=6, anchor='c').pack()


# 临时查找函数
def find(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE SNO='%s' AND CNO='%s'"
                   % (data[0], data[1]))
        if db.rowcount == 0:
            find_no()
        else:
            results = db.fetchall()
            mod(con_con, db, results)
    except:
        find_no()


# 查询为空函数
def find_no():
    root1 = Tk()
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root1.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root1.minsize(window_width, window_height)  # 设置最小窗口大小
    root1.title("查询数据")
    Label(root1, text='查询为空！', fg='red', width=20, height=6, anchor='c').pack()


# 查询功能函数
def query(con_con, db):
    def que1(con_con, db):
        root.destroy()
        query_sc(con_con, db)

    def que2(con_con, db):
        root.destroy()
        query_s(con_con, db)

    def que3(con_con, db):
        root.destroy()
        query_c(con_con, db)

    # 设置窗口大小以屏幕居中
    root = Tk()
    root.title("查询数据")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    Label(root, text="请选择查询模式").grid(row=0, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="精确查询", command=lambda: que1(con_con, db))
    button.grid(row=1, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="学号查询", command=lambda: que2(con_con, db))
    button.grid(row=2, column=0, columnspan=2, sticky="nsew")
    button = ttk.Button(root, text="课程查询", command=lambda: que3(con_con, db))
    button.grid(row=3, column=0, columnspan=2, sticky="nsew")
    root.grid_columnconfigure(0, weight=1)  # 设置网格权重以垂直居中
    root.mainloop()

# 精确查询
def query_sc(con_con, db):
    # 存入数据
    def findddd():
        data = [entry1.get(), entry2.get()]
        root.destroy()
        find1(con_con, db, data)

    root = Tk()
    root.title("查询数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    entry2 = Entry(root)
    entry2.grid(row=1, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="查询", command=findddd).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    root.mainloop()

# 精确查询数据库函数
def find1(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE SNO='%s' AND CNO='%s'"
                   % (data[0], data[1]))
        if db.rowcount == 0:
            find_no()
        else:
            results = db.fetchall()
            show1(con_con, db, results)
    except:
        find_no()

# 单个数据展示函数
def show1(con_con, db, results):
    # 返回
    def ok():
        root.destroy()

    root = Tk()
    root.title("查询结果")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    Label(root, text=results[0][0]).grid(row=0, column=1, sticky='we', **padding)
    Label(root, text="课程号：").grid(row=1, column=0, sticky='e', **padding)
    Label(root, text=results[0][1]).grid(row=1, column=1, sticky='we', **padding)
    Label(root, text="成绩：").grid(row=2, column=0, sticky='e', **padding)
    Label(root, text=results[0][2]).grid(row=2, column=1, sticky='we', **padding)
    Label(root, text="学期：").grid(row=3, column=0, sticky='e', **padding)
    Label(root, text=results[0][3]).grid(row=3, column=1, sticky='we', **padding)
    Label(root, text="教学班：").grid(row=4, column=0, sticky='e', **padding)
    Label(root, text=results[0][4]).grid(row=4, column=1, sticky='we', **padding)

    # 确认按钮
    Button(root, text="确定", command=ok).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 显示窗口
    root.mainloop()

# 学号查询函数
def query_s(con_con, db):
    # 存入数据
    def findddd():
        data = [entry1.get()]
        root.destroy()
        find2(con_con, db, data)

    root = Tk()
    root.title("查询数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="学号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="查询", command=findddd).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    root.mainloop()

# 学号查询数据库函数
def find2(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE SNO='%s'"
                   % (data[0]))
        if db.rowcount == 0:
            find_no()
        else:
            results = db.fetchall()
            showshow(con_con, db, results)
    except:
        find_no()

# 多数据展示函数
def showshow(con_con, db, results):
    # 返回
    def ok():
        root.destroy()

    root = Tk()
    root.title("查询结果")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    Label(root, text="学号").grid(row=0, column=0, sticky='')
    Label(root, text="课程号").grid(row=0, column=1, sticky='')
    Label(root, text="成绩").grid(row=0, column=2, sticky='')
    Label(root, text="学期").grid(row=0, column=3, sticky='')
    Label(root, text="教学班").grid(row=0, column=4, sticky='')
    i = 1
    for row in results:
        Label(root, text=row[0]).grid(row=i, column=0, sticky='')
        Label(root, text=row[1]).grid(row=i, column=1, sticky='')
        Label(root, text=row[2]).grid(row=i, column=2, sticky='')
        Label(root, text=row[3]).grid(row=i, column=3, sticky='')
        Label(root, text=row[4]).grid(row=i, column=4, sticky='')
        i = i + 1

    # 确认按钮
    Button(root, text="确定", command=ok).grid(row=i+1, column=2, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=0)

    # 显示窗口
    root.mainloop()


# 课程查询函数
def query_c(con_con, db):
    # 存入数据
    def findddd():
        data = [entry1.get()]
        root.destroy()
        find3(con_con, db, data)

    root = Tk()
    root.title("查询数据")

    # 设置窗口大小以屏幕居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 250
    window_height = 200
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
    root.minsize(window_width, window_height)  # 设置最小窗口大小

    # 调整布局和内边距使元件居中，读取数据
    padding = {'padx': 5, 'pady': 5}
    Label(root, text="课程号：").grid(row=0, column=0, sticky='e', **padding)
    entry1 = Entry(root)
    entry1.grid(row=0, column=1, sticky='we', **padding)

    # 确认提交按钮
    Button(root, text="查询", command=findddd).grid(row=5, column=0, columnspan=2)

    # 输入框在单元格内水平填充
    root.grid_columnconfigure(1, weight=1)

    # 清空输入
    entry1.delete(0, 'end')
    root.mainloop()

# 课程查询数据库函数
def find3(con_con, db, data):
    try:
        db.execute("SELECT * FROM SC WHERE CNO='%s'"
                   % (data[0]))
        if db.rowcount == 0:
            find_no()
        else:
            results = db.fetchall()
            showshow(con_con, db, results)
    except:
        find_no()


if __name__ == "__main__":
    # 连接数据库
    con_con, db = con()

    def menu1(con_con, db):
        root.destroy()
        add(con_con, db)

    def menu2(con_con, db):
        root.destroy()
        delete(con_con, db)

    def menu3(con_con, db):
        root.destroy()
        modify(con_con, db)

    def menu4(con_con, db):
        root.destroy()
        query(con_con, db)

    def menu5(con_con, db):
        root.destroy()
        db_close(con_con, db)
        exit()


    # 主函数接口
    flag = True
    while (flag == True):
        '''
        print()
        print("------学生选课管理系统------")
        print("        1.增加数据         ")
        print("        2.删除数据         ")
        print("        3.修改数据         ")
        print("        4.查询数据         ")
        print("        5.退出系统         ")
        print("--------------------------")
        print()
        print("请选择：", end='')
        choice = input()    
                
        # 5.退出系统
        if (choice == '5'):
            flag = False

        # 1.增加数据
        elif (choice == '1'):
            add(con_con, db)

        # 2.删除数据
        elif (choice == '2'):
            delete(con_con, db)

        # 3.修改数据
        elif (choice == '3'):
            modify()

        # 4.查询数据
        elif (choice == '4'):
            query()

        # 其他故障输入
        else:
            print()
            print("输入有误！请重新输入！")
            print()
        '''

        root = Tk()
        root.title("选课管理系统")

        # 设置窗口大小以屏幕居中
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 250
        window_height = 200
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # 设置窗口初始位置和大小
        root.minsize(window_width, window_height)  # 设置最小窗口大小

        Label(root, text="请选择功能").grid(row=0, column=0, columnspan=2, sticky="nsew")
        button = ttk.Button(root, text="添加数据", command=lambda: menu1(con_con, db))
        button.grid(row=1, column=0, columnspan=2, sticky="nsew")
        button = ttk.Button(root, text="删除数据", command=lambda: menu2(con_con, db))
        button.grid(row=2, column=0, columnspan=2, sticky="nsew")
        button = ttk.Button(root, text="修改数据", command=lambda: menu3(con_con, db))
        button.grid(row=3, column=0, columnspan=2, sticky="nsew")
        button = ttk.Button(root, text="查询数据", command=lambda: menu4(con_con, db))
        button.grid(row=4, column=0, columnspan=2, sticky="nsew")
        button = ttk.Button(root, text="退出系统", command=lambda: menu5(con_con, db))
        button.grid(row=5, column=0, columnspan=2, sticky="nsew")
        root.grid_columnconfigure(0, weight=1)  # 设置网格权重以垂直居中
        root.mainloop()











    # 断开连接
    db_close(con_con, db)
