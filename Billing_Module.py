from tkinter import *
import time
import random
root=Tk()
root.geometry("2000x2000")
root.title("BINGE HOUSE")

f1=Frame(root)
f1.pack(side=TOP)

l1=Label(f1, bg="pink",  bd="3", relief="groove", text="BILLING SYSTEM", font=("Times new roman", "50", "bold"))
l1.grid(row=0, column=0)
localtime = time.asctime()
l2=Label(f1,relief="flat",text=localtime,font=("arial", "25"))
l2.grid(row=1, column=0)

f2=Frame(root)
f2.pack(side=LEFT)

rand=StringVar()
noodles_q=StringVar()
burger_q=StringVar()
pasta_q=StringVar()
fries_q=StringVar()
pizza_q=StringVar()
wraps_q=StringVar()
honey_chilli_potato_q=StringVar()
coke_q=StringVar()
shakes_q=StringVar()
ice_cream_float_q=StringVar()
tea_q=StringVar()
coffee_q=StringVar()
water_q=StringVar()
    


noodles_qty=2
noodles_q.set(noodles_qty)
burger_qty=2
burger_q.set(burger_qty)
pasta_qty=2
pasta_q.set(pasta_qty)
fries_qty=2
fries_q.set(fries_qty)
pizza_qty=2
pizza_q.set(pizza_qty)
wraps_qty=2
wraps_q.set(wraps_qty)
honey_chilli_potato_qty=2
honey_chilli_potato_q.set(honey_chilli_potato_qty)
coke_qty=2
coke_q.set(coke_qty)
shakes_qty=2
shakes_q.set(shakes_qty)
ice_cream_float_qty=2
ice_cream_float_q.set(ice_cream_float_qty)
tea_qty=2
tea_q.set(tea_qty)
coffee_qty=2
coffee_q.set(coffee_qty)
water_qty=2
water_q.set(water_qty)

noodles_price=150
burger_price=130
pasta_price=200
fries_price=140
pizza_price=300
wraps_price=120
honey_chilli_potato_price=180
coke_price=80
shakes_price=100
ice_cream_float_price=150
tea_price=50
coffee_price=60
water_price=40

amount=StringVar()
sgst=StringVar()
cgst=StringVar()
total_payable=StringVar()

def total():
    x=random.randint(80000000, 100000000)
    #x=str(x)
    rand.set(x)
    amt=(noodles_qty*noodles_price)+(burger_qty*burger_price)+(pasta_qty*pasta_price)+(fries_qty*fries_price)+(pizza_qty*pizza_price)+(wraps_qty*wraps_price)+(honey_chilli_potato_qty*honey_chilli_potato_price)+(coke_qty*coke_price)+(shakes_qty*shakes_price)+(ice_cream_float_qty*ice_cream_float_price)+(tea_qty*tea_price)+(coffee_qty*coffee_price)+(water_qty*water_price)
    amt=float(amt)
    amount.set(amt)
    tax1=0.025*amt
    sgst.set(tax1)
    tax2=0.025*amt
    cgst.set(tax2)
    tot_pay=amt+tax1+tax2
    total_payable.set(tot_pay)



l3=Label(f2,font=('aerial', '15', 'bold'), text="Reference", bd="10")
l3.grid(row=0, column=0)   
l3=Entry(f2,font=('aerial', '15', 'bold'), bd="5",textvariable=rand,insertwidth="3",bg="pink")
l3.grid(row=0, column=1)   

l4=Label(f2,font=('aerial', '15', 'bold'), text="Noodles", bd="10")
l4.grid(row=1, column=0)   
l4=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=noodles_q)
l4.grid(row=1, column=1) 

l5=Label(f2,font=('aerial', '15', 'bold'), text="Burger", bd="10")
l5.grid(row=2, column=0)   
l5=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=burger_q)
l5.grid(row=2, column=1)

l6=Label(f2,font=('aerial', '15', 'bold'), text="Pasta", bd="10")
l6.grid(row=3, column=0)   
l6=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=pasta_q)
l6.grid(row=3, column=1)

 

l7=Label(f2,font=('aerial', '15', 'bold'), text="Fries", bd="10")
l7.grid(row=4, column=0)   
l7=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=fries_q)
l7.grid(row=4, column=1)  

l8=Label(f2,font=('aerial', '15', 'bold'), text="Pizza", bd="10")
l8.grid(row=5, column=0)   
l8=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=pizza_q)
l8.grid(row=5, column=1)  

l9=Label(f2,font=('aerial', '15', 'bold'), text="Wraps", bd="10")
l9.grid(row=6, column=0)   
l9=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=wraps_q)
l9.grid(row=6, column=1) 

l10=Label(f2,font=('aerial', '15', 'bold'), text="Honey chilli potato", bd="10")
l10.grid(row=7, column=0)   
l10=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=honey_chilli_potato_q)
l10.grid(row=7, column=1) 

l11=Label(f2,font=('aerial', '15', 'bold'), text="Coke", bd="10")
l11.grid(row=8, column=0)   
l11=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=coke_q)
l11.grid(row=8, column=1) 



l12=Label(f2,font=('aerial', '15', 'bold'), text="Shakes", bd="10")
l12.grid(row=0, column=2)   
l12=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=shakes_q)
l12.grid(row=0, column=3)  

l13=Label(f2,font=('aerial', '15', 'bold'), text="Ice cream float", bd="10")
l13.grid(row=1, column=2)   
l13=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=ice_cream_float_q)
l13.grid(row=1, column=3)  

l14=Label(f2,font=('aerial', '15', 'bold'), text="Tea", bd="10")
l14.grid(row=2, column=2)   
l14=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=tea_q)
l14.grid(row=2, column=3)  

l15=Label(f2,font=('aerial', '15', 'bold'), text="Coffee", bd="10")
l15.grid(row=3, column=2)   
l15=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=coffee_q)
l15.grid(row=3, column=3)  

l16=Label(f2,font=('aerial', '15', 'bold'), text="Mineral water bottle", bd="10")
l16.grid(row=4, column=2)   
l16=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=water_q)
l16.grid(row=4, column=3)  

l17=Label(f2,font=('aerial', '15', 'bold'), text="Amount", bd="10")
l17.grid(row=5, column=2)   
l17=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=amount)
l17.grid(row=5, column=3)  

l18=Label(f2,font=('aerial', '15', 'bold'), text="SGST 2.5%", bd="10")
l18.grid(row=6, column=2)   
l18=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=sgst)
l18.grid(row=6, column=3)  

l19=Label(f2,font=('aerial', '15', 'bold'), text="CGST 2.5%", bd="10")
l19.grid(row=7, column=2)   
l19=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=cgst)
l19.grid(row=7, column=3)  


l20=Label(f2,font=('aerial', '15', 'bold'), text="Total amount payable", bd="10")
l20.grid(row=8, column=2)   
l20=Entry(f2,font=('aerial', '15', 'bold'), bd="5", insertwidth="3",bg="pink", textvariable=total_payable)
l20.grid(row=8, column=3)  

def exit():
    input=messagebox.askquestion("Exit", "Are you sure you want to exit")
    if(input=='yes'):
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will return to the main window')
        
b1=Button(f2, text="Total", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"), command=total)
b1.grid(row =9, column = 1, pady = 10, padx=70)


b2=Button(f2, text="Back", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"))
b2.grid(row = 9, column = 2, pady = 10, padx=70)

b2=Button(f2, text="Exit", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"), command=exit)
b2.grid(row = 9, column = 3,pady = 10, padx= 70)

root.mainloop()
