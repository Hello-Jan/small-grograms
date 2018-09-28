# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox

import random

#GUI程序
class Application(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.pack(ipadx=40,ipady=10)
		self.number=StringVar()
		self.createWidgets()


	def createWidgets(self):
		self.label=Label(self,text='何以解忧，唯有暴富...')
		self.label.pack()
		self.alertButton=Button(self,text='选号',command=self.shownumber)
		self.alertButton.pack()
		self.label2=Label(self,textvariable=self.number)
		self.label2.pack()

	def shownumber(self):
		#红球序列
		L=[]
		choice_list=list(range(1,34))
		for i in range(6):
			Red=random.choice(choice_list)
			L.append(Red)
			choice_list.remove(Red)
		L.sort()
		L1=list(map(lambda x : "%02d" % x,L))

		result1="红球："+' '.join(L1)
		#蓝球
		Blue=random.randint(1,16)
		result2="篮球：%02d"%Blue
		self.number.set('\n'+result1+'\n'+result2)


app=Application()
app.master.title('自动选球')
app.mainloop()


