# -*- coding: UTF-8 -*-
import Tkinter
import tkFont

root=Tkinter.Tk()
root.minsize(600,400)

#声明控件
ft = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)

titleLabel=Tkinter.Label(root,font=ft,text='欢迎使用HM收作业系统')
comLabel=Tkinter.Label(root,text='端 口')
subLabel=Tkinter.Label(root,text='当前作业科目')
SerialButton=Tkinter.Button(root,text='打开串口')
CheckButton = Tkinter.Button(root,text='开始检查')
CommitButton = Tkinter.Button(root,text='提交数据')





#添加组件到pack
subLabel.grid(row=1,column=0)
titleLabel.grid(row=0,column=5)     #将LABEL组件添加到底框上
SerialButton.grid(row=2,column=0)
comLabel.grid(row=2,column=1)
CheckButton.grid(row=3,column=0)
CommitButton.grid(row=4,column=0)
root.mainloop()
