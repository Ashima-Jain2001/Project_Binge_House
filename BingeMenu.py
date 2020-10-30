import os
from tkinter import *
import sqlite3
from tkinter import messagebox as mb
import BingeHouse

#connecting to database
connection = sqlite3.connect("myDatabase.db")
cursor = connection.cursor()
tableName = "loginTable"

fields = ('userName', 'password')
formFields = ('firstName', 'lastName', 'userName', 'password')

def createTable():
  CREATE_STATEMENT = "CREATE TABLE " + tableName + " ( firstName VARCHAR(30), lastName VARCHAR(30), userName VARCHAR(30), password VARCHAR(30));"
  cursor.execute(CREATE_STATEMENT); 

def saveUserDetails(fName, lName, userName, password):
  SAVE_STATEMENT = "INSERT INTO " + tableName + " values ( \"" + fName + "\" , \"" + lName + "\" , \"" + userName + "\" , \"" + password + "\" );"
  cursor.execute(SAVE_STATEMENT);
  print ('Successfully submitted!! \n')
  cursor.execute("SELECT * FROM " + tableName)
  result = cursor.fetchall()
  for i in result:
	  print(i)
    

def getPassword(userName):
  cursor.execute("SELECT password FROM " + tableName + " where userName = \"" +  userName + "\"");
  result = cursor.fetchall()
  if(result == None or len(result) == 0):
    return ""
  return ''.join(result[0])

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      #ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def submitFunc(entries):
   firstName = entries['firstName'].get()
   lastName = entries['lastName'].get()
   userName = entries['userName'].get()
   password = entries['password'].get()
   
   if firstName == "":
       mb.showerror('a', 'please enter firstName');
       return

   if lastName == "":
       mb.showerror('a', 'please enter lastName');
       return
   
   if userName == "":
       mb.showerror('a', 'please enter username');
       return

   if password == "":
       mb.showerror('a', 'please enter password');
       return

   saveUserDetails(firstName, lastName, userName, password)

def secondWindow():
   root = Tk()
   root.geometry('600x400') 
   root.configure(background='#123456')
   createTable()
   ents = makeform(root, formFields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Submit',
   command=(lambda e = ents: submitFunc(e)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   b2 = Button(root, text='Return',
   command=(lambda e = ents: returnFunc(e, root)))
   b2.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()

def returnFunc(entries, window):
    firstWindow()

def loginFunc(entries):
   userName = entries['userName'].get()
   password = entries['password'].get()
   
   if getPassword(userName) == password:
      print('You are successfully logged in')
      os.system('python BingeHouse.py')
   else:
      print('Wrong credentials') 

def registerFunc(entries):
   secondWindow()

def firstWindow():
   root = Tk()
   root.geometry('600x400') 
   root.configure(background='#456789')
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'Login',
      command=(lambda e = ents: loginFunc(e)))
   b1.pack(side = LEFT, padx = 5, pady = 5)
   b2 = Button(root, text='Register',
   command=(lambda e = ents: registerFunc(e)))
   b2.pack(side = LEFT, padx = 5, pady = 5)
   root.mainloop()

firstWindow()