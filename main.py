import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
conn= sqlite3.connect('smartstudent.db')
c= conn.cursor()
#----------------------------------------------------------------CREATION OF THE TABLE------------------------------------------
'''c.execute("""CREATE TABLE MODEL2(
	    regno int primary key,
	    AI int,
	    CD int,
	    MC int,
	    DWDM int,
	    DS int,
	    IP int
)""")'''



	   



class smartstudent(tk.Tk):
	
	def __init__(self,*args,**kwargs):

		tk.Tk.__init__(self,*args,**kwargs)
		tk.Tk.wm_title(self,"Smart Student")
		tk.Tk.geometry(self,'800x750')
		tk.Tk.resizable(self,'0','0')
		container = tk.Frame(self)

		container.pack(side="top",fill="both",expand= True)

		container.grid_rowconfigure(0,weight= 1)
		container.grid_columnconfigure(0,weight=1)

		self.frames = {}

		for F in (StartPage,Pageone,second_page):

			frame = F(container,self)

			self.frames[F]= frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)
	

	def show_frame(self,cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		label = ttk.Label(self,text="Smart Student", font=("Montserrat",40))
		label.place(x='50',y='150')
		label = ttk.Label(self,text="This app lets you to view your performance and visually track your performance ", font=("Montserrat",10))
		label.place(x='50',y='230')
		label = ttk.Label(self,text="M.Prasanth ", font=("Montserrat",10))
		label.place(x='50',y='700')
		


		button1= ttk.Button(self,text="Next",command=lambda: controller.show_frame(Pageone))
		button1.place(x='680',y='700')
		'''button2 = ttk.Button(self,text="update marks",command=lambda: controller.show_frame(second_page))
		button2.pack()'''


class Pageone(tk.Frame):
	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		
		 #-----------------------------------------------------LABEL----------------------------------------------
		welcome=tk.Label(self,text='Welcome',font='Montserrat')
		welcome.config(font=("Montserrat",50))
		welcome.place(x='250',y='50')
		name = tk.Label(self,text='Name:',font='Montserrat')
		name.place(x='180',y='200')
		regno = tk.Label(self,text='Register number:',font='Montserrat')
		regno.place(x='180',y='250')
		phoneno = tk.Label(self,text='Phone number:',font='Montserrat')
		phoneno.place(x='180',y='300')
		department = tk.Label(self,text='Department:',font='Montserrat')
		department.place(x='180',y='350')
		emailid =tk.Label(self,text='Email ID:',font='Montserrat')
		emailid.place(x='180',y='400')
		note =tk.Label(self,text='"Tap the Next button if you are already an registered user"',font=('Montserrat',10),fg='red')
		note.place(x='190',y='500')
		#---------------------------------------------------Variable Declarations---------------------------------
		self.name= tk.StringVar()
		self.regno= tk.StringVar()
		self.phoneno=tk.StringVar()
		self.department= tk.StringVar()
		self.emailid= tk.StringVar()
		#---------------------------------------------------ENTRY--------------------------------------------------
		name=tk.Entry(self,width='40',textvariable='name')
		name.place(x='350',y='200',)
		regno=tk.Entry(self,width='40',textvariable='regno')
		regno.place(x='350',y='250')
		phoneno=tk.Entry(self,width='40',textvariable='phoneno')
		phoneno.place(x='350',y='300')
		department=tk.Entry(self,width='40',textvariable='department')
		department.place(x='350',y='350')
		emailid=tk.Entry(self,width='40',textvariable='emailid')
		emailid.place(x='350',y='400')
        #---------------------------------------------------Buttons------------------------------------------------
		button1 = ttk.Button(self,text="Next",command=lambda: controller.show_frame(second_page))
		button1.place(x='680',y='700')
		button2 = ttk.Button(self,text="Back",command=lambda: controller.show_frame(StartPage))
		button2.place(x='30',y='30')
		button3 = ttk.Button(self,text="Submit",command=lambda:submit())
		button3.place(x='580',y='700')
		def clear():
			name.delete(0,'end')
			regno.delete(0,'end')
			phoneno.delete(0,'end')
			department.delete(0,'end')
			emailid.delete(0,'end')

		def submit():
			lim= str(regno.get())
			
		
			if len(lim) > 15:
					messagebox.showinfo("Invalid","Enter register number again ")
					clear()
			elif len(lim) < 11:
				
				messagebox.showinfo("Invalid","Enter the  proper register number again or check the values")
				clear()
			else:
				try:

					conn= sqlite3.connect('smartstudent.db')
					c= conn.cursor()
					c.execute("INSERT INTO details VALUES('%s','%s','%s','%s','%s')"%(name.get(),int(regno.get()),phoneno.get(),department.get(),emailid.get()))
					c.close()
					conn.commit()
					conn.close()
					clear()
				
				except :
					messagebox.showinfo("Retry","The user already exists or fill all the details")
					clear()
				
			'''name.delete(0,END)
			regno.delete(0,END)
			phoneno.delete(0,END)
			department.delete(0,END)
			emailid.delete(0,END)'''
	   
		
		
		

class second_page(tk.Frame):
	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		#--------------------------------------------------search function-----------------------------------
		
			


		def search():
			try:
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				sql="SELECT * FROM details WHERE regno='%s'"%register_num.get()
				c.execute(sql)
				res=c.fetchone()
			
				
				lab1 = ttk.Label(self,text=res[0],font=('Montserrat',10))
				lab1.place(x='30',y='250')
				lab2 = ttk.Label(self,text=res[1],font=('Montserrat',10))
				lab2.place(x='150',y='250')
				lab3 = ttk.Label(self,text=res[2],font=('Montserrat',10))
				lab3.place(x='300',y='250')
				lab4 = ttk.Label(self,text=res[3],font=('Montserrat',10))
				lab4.place(x='450',y='250')
				lab5 = ttk.Label(self,text=res[4],font=('Montserrat',10))
				lab5.place(x='30',y='280')

				conn.close()

			except:
				messagebox.showinfo("Missing","Enter the register number")
				
		
			
			
			


	
			'''try:	
			except:
				messagebox.showinfo('no data','No such record')'''
		
		#--------------------------------------------examtype defenition---------------------------------------------------
		def clear():
			#register_num.delete(0,'end')
			AI.delete(0,'end')
			CD.delete(0,'end')
			MC.delete(0,'end')
			DWDM.delete(0,'end')
			DS.delete(0,'end')
			IP.delete(0,'end')
			examtype.delete(0,'end')
		def open():
			try:
				c.execute("SELECT * FROM CAT1 WHERE regno='%s'"%(register_num.get()))
				g=c.fetchone()
				h=list(g[1:])
				c.execute("SELECT * FROM CAT2 WHERE regno='%s'"%(register_num.get()))
				g1=c.fetchone()
				h1=list(g1[1:])
				c.execute("SELECT * FROM CAT3 WHERE regno='%s'"%(register_num.get()))
				g2=c.fetchone()
				h2=list(g2[1:])
				subs=list(('Ai','CD','MC','DWDM','DS','IP'))
				xpos= np.arange(len(subs))
				plt.bar(xpos,h,width=0.2, label="cat1")
				plt.bar(xpos+0.2,h1,width=0.2,label="cat2")
				plt.bar(xpos+0.4,h2,width=0.2,label="cat3")
				plt.xticks(xpos,subs)
				plt.ylabel("MARKS")
				plt.xlabel("SUBJECT")
				plt.title('CAT marks')
				plt.legend()
				plt.show()
				
			except TypeError :
				messagebox.showinfo("Data missing","please enter all the cat marks")
			
		def open1():
			try:
				c.execute("SELECT * FROM MODEL1 WHERE regno='%s'"%(register_num.get()))
				g=c.fetchone()
				h=list(g[1:])
				c.execute("SELECT * FROM MODEL2 WHERE regno='%s'"%(register_num.get()))
				g1=c.fetchone()
				h1=list(g1[1:])
				subs=list(('Ai','CD','MC','DWDM','DS','IP'))
				xpos= np.arange(len(subs))
				plt.bar(xpos,h,width=0.2, label="Model1")
				plt.bar(xpos+0.2,h1,width=0.2,label="Model2")
				plt.xticks(xpos,subs)
				plt.ylabel("MARKS")
				plt.xlabel("SUBJECT")
				plt.title('MODEL MARKS')
				plt.legend()
				plt.show()
			except TypeError:
				messagebox.showinfo("Data missing","please enter all the cat marks")








		def invoke():
			input= examtype.get()
			
		
			if input== "cat1":
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				c.execute("INSERT INTO CAT1 VALUES('%s','%s','%s','%s','%s','%s','%s')"%(register_num.get(),AI.get(),CD.get(),MC.get(),DWDM.get(),DS.get(),IP.get()))
				c.close
				conn.commit()
				conn.close()
			elif input== "cat2":
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				c.execute("INSERT INTO CAT2 VALUES('%s','%s','%s','%s','%s','%s','%s')"%(register_num.get(),AI.get(),CD.get(),MC.get(),DWDM.get(),DS.get(),IP.get()))
				c.close
				conn.commit()
				conn.close()
			elif input== "cat3":
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				c.execute("INSERT INTO CAT3 VALUES('%s','%s','%s','%s','%s','%s','%s')"%(register_num.get(),AI.get(),CD.get(),MC.get(),DWDM.get(),DS.get(),IP.get()))
				c.close
				conn.commit()
				conn.close()
			elif input== "model1":
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				c.execute("INSERT INTO MODEL1 VALUES('%s','%s','%s','%s','%s','%s','%s')"%(register_num.get(),AI.get(),CD.get(),MC.get(),DWDM.get(),DS.get(),IP.get()))
				c.close
				conn.commit()
				conn.close()
			elif input== "model2":
				conn= sqlite3.connect('smartstudent.db')
				c= conn.cursor()
				c.execute("INSERT INTO MODEL2 VALUES('%s','%s','%s','%s','%s','%s','%s')"%(register_num.get(),AI.get(),CD.get(),MC.get(),DWDM.get(),DS.get(),IP.get()))
				c.close
				conn.commit()
				conn.close()
			clear()
			



				


        #--------------------------------------------labels-----------------------------------------------------------------
		label = ttk.Label(self,text="Hey There!",font=('Montserrat',20))
		label.place(x='30',y='110') 
		label1 = ttk.Label(self,text="Please!..Enter your register number to update results",font=('Montserrat',10))
		label1.place(x='30',y='150')
		label2 = ttk.Label(self,text="Register Number:",font=('Montserrat',10))
		label2.place(x='30',y='190')
		label3 = ttk.Label(self,text="Exam Type:",font=('Montserrat',10))
		label3.place(x='500',y='190')
		sub1 = ttk.Label(self,text='Artificial Intelligence:',font='Montserrat')
		sub1.place(x='30',y='350')
		sub2 = ttk.Label(self,text='Compiler Design:',font='Montserrat')
		sub2.place(x='30',y='400')
		sub3 = ttk.Label(self,text='Moblile Computing:',font='Montserrat')
		sub3.place(x='30',y='450')
		sub4 = ttk.Label(self,text='Data Wharehouse and data mining:',font='Montserrat')
		sub4.place(x='30',y='500')
		sub5 = ttk.Label(self,text='Distributed systems:',font='Montserrat')
		sub5.place(x='30',y='550')
		sub6 = ttk.Label(self,text='Internet Programming:',font='Montserrat')
		sub6.place(x='30',y='600')
        #--------------------------------------------Entry-----------------------------------------------------------------
		
		register_num = ttk.Entry(self)
		register_num.place(x='170',y='190') 
		examtype= ttk.Entry(self)
		examtype.place(x='590',y='190') 
		AI=ttk.Entry(self,width='10',textvariable='AI')
		AI.place(x='370',y='350',)
		CD=ttk.Entry(self,width='10',textvariable='CD')
		CD.place(x='370',y='400')
		MC=ttk.Entry(self,width='10',textvariable='MC')
		MC.place(x='370',y='450')
		DWDM=ttk.Entry(self,width='10',textvariable='DWDM')
		DWDM.place(x='370',y='500')
		DS=ttk.Entry(self,width='10',textvariable='DS')
		DS.place(x='370',y='550')
		IP=ttk.Entry(self,width='10',textvariable='IP')
		IP.place(x='370',y='600')
        #---------------------------------------------option---------------------------------------------------------------- 
		
		#---------------------------------------------button----------------------------------------------------------------
		button= ttk.Button(self,text="Submit",command=lambda:invoke())
		button.place(x='680',y='700')
		button= ttk.Button(self,text="Visualize CAT",command=lambda:open())
		button.place(x='100',y='700')
		button= ttk.Button(self,text="Visualize Model",command=lambda:open1())
		button.place(x='200',y='700')
		button1= ttk.Button(self,text="back",command=lambda: controller.show_frame(Pageone))
		button1.place(x='30',y='30')
		button2= ttk.Button(self,text="go",width=10,command=lambda: search())
		button2.place(x='350',y='190')



		
	
	
app = smartstudent()
app.mainloop()


