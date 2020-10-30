from tkinter import*

noodles_qty = 0
burger_qty = 0
pasta_qty = 0
fries_qty = 0
pizza_qty = 0
wraps_qty = 0
honeychilli_qty = 0
coke_qty = 0
icescream_qty = 0
tea_qty = 0
coffee_qty = 0
shake_qty = 0
water_qty = 0


    
def back():
        
    
    
    
    
    import sys
    import time
    from tkinter.messagebox import showinfo
    import datetime
    
    try:
        import Tkinter as tk
    except ImportError:
        import tkinter as tk
    
    try:
        import ttk
        py3 = False
    except ImportError:
        import tkinter.ttk as ttk
        py3 = True
    
    
    #noodles_qty = 0
    #burger_qty = 0
    #pasta_qty = 0
    #fries_qty = 0
    #pizza_qty = 0
    #wraps_qty = 0
    #honeychilli_qty = 0
    #coke_qty = 0
    #icescream_qty = 0
    #tea_qty = 0
    #coffee_qty = 0
    #shake_qty = 0
    #water_qty = 0
                
                
    
    def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root1
        root1 = tk.Tk()
        top = Toplevel1 (root1)
       
        root1.mainloop()
        
        
    
    w = None
    def create_Toplevel1(rt, *args, **kwargs):
        '''Starting point when module is imported by another module.
           Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
        global w, w_win, root
        
        root1 = rt
        w = tk.Toplevel (root1)
        top = Toplevel1 (w)
    
        return (w, top)
    
    def destroy_Toplevel1():
        global w
        w.destroy()
        w = None
    
    class Toplevel1:
        
        def __init__(self, top=None):
            def reset():
                       global noodles_qty
                       global burger_qty
                       global pasta_qty
                       global fries_qty
                       global pizza_qty
                       global wraps_qty
                       global honeychilli_qty
                       global coke_qty
                       global icescream_qty
                       global tea_qty
                       global shake_qty
                       global coffee_qty
                       global water_qty
                       honeychilli_qty = 0
                       wraps_qty = 0
                       noodles_qty = 0
                       burger_qty = 0
                       pasta_qty = 0
                       fries_qty = 0
                       pizza_qty = 0
                       coke_qty = 0
                       icescream_qty = 0
                       tea_qty = 0
                       coffee_qty = 0
                       shake_qty = 0
                       water_qty = 0
                       showinfo("Reset all Items", "All Items Reset!!")
                       self.Label5.config(text='0')
                       self.Label3.config(text="0")
                       self.Label5.config(text="0")
                       self.Label6.config(text="0")
                       self.Label8.config(text="0")
                       self.Label10.config(text='0')
                       self.Label11.config(text='0')
                       self.Label12.config(text='0')
                       self.Label13.config(text='0')
                       self.Label14.config(text='0')
                       self.Label15.config(text='0')
                       self.Label16.config(text='0')
                       self.Label17.config(text='0')
                       
                       
    
            
                        
                    
                  
                    
                    
                    
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
    
            top.geometry("1920x1080")
            #top.minsize(1920, 1080)
            #top.maxsize(2000,2000)
            #top.resizable(1, 1)
            top.title("BINGE HOUSE")
            top.configure(background="#d9d9d9")
            
    
            def noodlespos():
                global noodles_qty 
    
                noodles_qty = noodles_qty + 1
                
                #noodles_q=noodles_qty
                self.Label3 = tk.Label(top)
                self.Label3.place(relx=0.001, rely=0.253, height=50, width=87)
                self.Label3.configure(background="#FFC0CB")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(foreground="#000000")
                self.Label3.configure(text=f'{noodles_qty}')
                
            def noodlesneg():
                global noodles_qty 
    
                noodles_qty = noodles_qty - 1
                if noodles_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    noodles_qty=0
                
                #noodles_q=noodles_qty
                self.Label3 = tk.Label(top)
                self.Label3.place(relx=0.001, rely=0.253, height=50, width=87)
                self.Label3.configure(background="#FFC0CB")
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(foreground="#000000")
                self.Label3.configure(text=f'{noodles_qty}')
                
            def burgerpos():
                global burger_qty 
    
                burger_qty = burger_qty + 1
                
                #buger_q=burger_qty
                self.Label5 = tk.Label(top)
                self.Label5.place(relx=0.001, rely=0.363, height=50, width=87)
                self.Label5.configure(background="#FFC0CB")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(text=burger_qty) 
            def burgerneg():
                global burger_qty 
    
                burger_qty = burger_qty - 1
                if burger_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    burger_qty=0
                
                #burger_q=burger_qty
                self.Label5 = tk.Label(top)
                self.Label5.place(relx=0.001, rely=0.363, height=50, width=87)
                self.Label5.configure(background="#FFC0CB")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(text=burger_qty)
    
            def pastapos():
                global pasta_qty 
                
                pasta_qty = pasta_qty + 1
                
                #pasta_q=pasta_qty
                self.Label8 = tk.Label(top)
                self.Label8.place(relx=0.001, rely=0.473, height=50, width=87)
                self.Label8.configure(background="#FFC0CB")
                self.Label8.configure(disabledforeground="#a3a3a3")
                self.Label8.configure(foreground="#000000")
                self.Label8.configure(text=pasta_qty) 
                
            def pastaneg():
                global pasta_qty 
    
                pasta_qty = pasta_qty - 1
                if pasta_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    pasta_qty=0
                
                #pasta_q=pasta_qty
                self.Label8 = tk.Label(top)
                self.Label8.place(relx=0.001, rely=0.473, height=50, width=87)
                self.Label8.configure(background="#FFC0CB")
                self.Label8.configure(disabledforeground="#a3a3a3")
                self.Label8.configure(foreground="#000000")
                self.Label8.configure(text=pasta_qty)
            def friespos():
                global fries_qty 
    
                fries_qty = fries_qty + 1
                if fries_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    fries_qty=0
                
                #fries_q=fries_qty
                self.Label5 = tk.Label(top)
                self.Label5.place(relx=0.001, rely=0.583, height=50, width=87)
                self.Label5.configure(background="#FFC0CB")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(text=fries_qty)
            def friesneg():
                global fries_qty 
    
                fries_qty = fries_qty - 1
                if fries_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    fries_qty=0
                
                #fries_q=fries_qty
                self.Label5 = tk.Label(top)
                self.Label5.place(relx=0.001, rely=0.583, height=50, width=87)
                self.Label5.configure(background="#FFC0CB")
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(foreground="#000000")
                self.Label5.configure(text=fries_qty)
                
            def pizzapos():
                global pizza_qty 
    
                pizza_qty = pizza_qty + 1
                if pizza_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    pizza_qty=0
                
                #pizza_q=pizza_qty
                self.Label6 = tk.Label(top)
                self.Label6.place(relx=0.001, rely=0.693, height=50, width=87)
                self.Label6.configure(background="#FFC0CB")
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(foreground="#000000")
                self.Label6.configure(text=pizza_qty)
                
            def pizzaneg():
                global pizza_qty 
    
                pizza_qty = pizza_qty - 1
                if pizza_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    pizza_qty=0
                
                #pizza_q=pizza_qty
                self.Label6 = tk.Label(top)
                self.Label6.place(relx=0.001, rely=0.693, height=50, width=87)
                self.Label6.configure(background="#FFC0CB")
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(foreground="#000000")
                self.Label6.configure(text=pizza_qty)
                
            def wrapspos():
                global wraps_qty 
    
                wraps_qty = wraps_qty + 1
                if wraps_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    wraps_qty=0
                
                #wraps_q=wraps_qty
                self.Label10 = tk.Label(top)
                self.Label10.place(relx=0.2, rely=0.253, height=50, width=60)
                self.Label10.configure(background="#FFC0CB")
                self.Label10.configure(disabledforeground="#a3a3a3")
                self.Label10.configure(foreground="#000000")
                self.Label10.configure(text=wraps_qty)
                
            def wrapsneg():
                global wraps_qty 
    
                wraps_qty = wraps_qty - 1
                if wraps_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    wraps_qty=0
                
                #wraps_q=wraps_qty
                self.Label10 = tk.Label(top)
                self.Label10.place(relx=0.2, rely=0.253, height=50, width=60)
                self.Label10.configure(background="#FFC0CB")
                self.Label10.configure(disabledforeground="#a3a3a3")
                self.Label10.configure(foreground="#000000")
                self.Label10.configure(text=wraps_qty)
                
            def honeychillipos():
                global honeychilli_qty 
    
                honeychilli_qty = honeychilli_qty + 1
                if honeychilli_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    honeychilli_qty=0
                
                #honey_chilli_potato_q=honeychilli_qty
                self.Label11 = tk.Label(top)
                self.Label11.place(relx=0.2, rely=0.363, height=50, width=60)
                self.Label11.configure(background="#FFC0CB")
                self.Label11.configure(disabledforeground="#a3a3a3")
                self.Label11.configure(foreground="#000000")
                self.Label11.configure(text=honeychilli_qty)
                
            def honeychillineg():
                global honeychilli_qty 
    
                honeychilli_qty = honeychilli_qty - 1
                if honeychilli_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    honeychilli_qty=0
                
                #honey_chilli_potato_q=honeychilli_qty
                self.Label11 = tk.Label(top)
                self.Label11.place(relx=0.2, rely=0.363, height=50, width=60)
                self.Label11.configure(background="#FFC0CB")
                self.Label11.configure(disabledforeground="#a3a3a3")
                self.Label11.configure(foreground="#000000")
                self.Label11.configure(text=honeychilli_qty)
                
            def cokepos():
                global coke_qty 
    
                coke_qty = coke_qty + 1
                if coke_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    coke_qty=0
                
                #coke_q=coke_qty
                self.Label12 = tk.Label(top)
                self.Label12.place(relx=0.2, rely=0.473, height=50, width=60)
                self.Label12.configure(background="#FFC0CB")
                self.Label12.configure(disabledforeground="#a3a3a3")
                self.Label12.configure(foreground="#000000")
                self.Label12.configure(text=coke_qty)
            
            def cokeneg():
                global coke_qty 
    
                coke_qty = coke_qty - 1
                if coke_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    coke_qty=0
                
                #coke_q=coke_qty
                self.Label12 = tk.Label(top)
                self.Label12.place(relx=0.2, rely=0.473, height=50, width=60)
                self.Label12.configure(background="#FFC0CB")
                self.Label12.configure(disabledforeground="#a3a3a3")
                self.Label12.configure(foreground="#000000")
                self.Label12.configure(text=coke_qty)
            def icecreampos():
                global icescream_qty 
    
                icescream_qty = icescream_qty + 1
                if icescream_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    icescream_qty=0
                
                #ice_cream_float_q=icescream_qty
                self.Label13 = tk.Label(top)
                self.Label13.place(relx=0.2, rely=0.583, height=50, width=60)
                self.Label13.configure(background="#FFC0CB")
                self.Label13.configure(disabledforeground="#a3a3a3")
                self.Label13.configure(foreground="#000000")
                self.Label13.configure(text=icescream_qty)
                
            def icecreamneg():
                global icescream_qty 
    
                icescream_qty = icescream_qty - 1
                if icescream_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    icescream_qty=0
                
                #ice_cream_float_q=icescream_qty
                self.Label13 = tk.Label(top)
                self.Label13.place(relx=0.2, rely=0.583, height=50, width=60)
                self.Label13.configure(background="#FFC0CB")
                self.Label13.configure(disabledforeground="#a3a3a3")
                self.Label13.configure(foreground="#000000")
                self.Label13.configure(text=icescream_qty)
                
            def teapos():
                global tea_qty 
    
                tea_qty = tea_qty + 1
                if tea_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    tea_qty=0
                
                #tea_q=tea_qty
                self.Label14 = tk.Label(top)
                self.Label14.place(relx=0.2, rely=0.693, height=50, width=60)
                self.Label14.configure(background="#FFC0CB")
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(foreground="#000000")
                self.Label14.configure(text=tea_qty)
                
            def teaneg():
                global tea_qty 
    
                tea_qty = tea_qty - 1
                if tea_qty<0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    tea_qty=0
                
                #tea_q=tea_qty
                self.Label14 = tk.Label(top)
                self.Label14.place(relx=0.2, rely=0.693, height=50, width=60)
                self.Label14.configure(background="#FFC0CB")
                self.Label14.configure(disabledforeground="#a3a3a3")
                self.Label14.configure(foreground="#000000")
                self.Label14.configure(text=tea_qty)
                
            def coffeepos():
                global coffee_qty 
    
                coffee_qty  = coffee_qty  + 1
                if coffee_qty <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    coffee_qty =0
                
                #coffee_q=coffee_qty
                self.Label15 = tk.Label(top)
                self.Label15.place(relx=0.35, rely=0.253, height=50, width=60)
                self.Label15.configure(background="#FFC0CB")
                self.Label15.configure(disabledforeground="#a3a3a3")
                self.Label15.configure(foreground="#000000")
                self.Label15.configure(text=coffee_qty)
         
            def coffeeneg():
                global coffee_qty 
    
                coffee_qty  = coffee_qty  - 1
                if coffee_qty <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    coffee_qty =0
                
                #coffee_q=coffee_qty
                self.Label15 = tk.Label(top)
                self.Label15.place(relx=0.35, rely=0.253, height=50, width=60)
                self.Label15.configure(background="#FFC0CB")
                self.Label15.configure(disabledforeground="#a3a3a3")
                self.Label15.configure(foreground="#000000")
                self.Label15.configure(text=coffee_qty)
                
            def shakepos():
                global shake_qty 
    
                shake_qty  = shake_qty   + 1
                if shake_qty  <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    shake_qty  =0
              
                #shakes_q=shake_qty
                self.Label16 = tk.Label(top)
                self.Label16.place(relx=0.35, rely=0.363, height=50, width=60)
                self.Label16.configure(background="#FFC0CB")
                self.Label16.configure(disabledforeground="#a3a3a3")
                self.Label16.configure(foreground="#000000")
                self.Label16.configure(text=shake_qty)
                
            def shakeneg():
                global shake_qty 
    
                shake_qty = shake_qty   - 1
                if shake_qty  <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    shake_qty  =0
                
                #shakes_q=shake_qty
                self.Label16 = tk.Label(top)
                self.Label16.place(relx=0.35, rely=0.363, height=50, width=60)
                self.Label16.configure(background="#FFC0CB")
                self.Label16.configure(disabledforeground="#a3a3a3")
                self.Label16.configure(foreground="#000000")
                self.Label16.configure(text=shake_qty)
                
            def waterpos():
                global water_qty 
    
                water_qty  = water_qty   + 1
                if water_qty  <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    water_qty  =0
                
                #water_q=water_qty
                self.Label17 = tk.Label(top)
                self.Label17.place(relx=0.35, rely=0.473, height=50, width=60)
                self.Label17.configure(background="#FFC0CB")
                self.Label17.configure(disabledforeground="#a3a3a3")
                self.Label17.configure(foreground="#000000")
                self.Label17.configure(text=water_qty)
                
            def waterneg():
                global water_qty 
    
                water_qty  = water_qty   - 1
                if water_qty  <0:
                    showinfo("Error","Item cant be less than 0!!",icon='error')
                    water_qty  =0
                
                #water_q=water_qty
                self.Label17 = tk.Label(top)
                self.Label17.place(relx=0.35, rely=0.473, height=50, width=60)
                self.Label17.configure(background="#FFC0CB")
                self.Label17.configure(disabledforeground="#a3a3a3")
                self.Label17.configure(foreground="#000000")
                self.Label17.configure(text=water_qty)
                
                
                
                
                
                
                
            
            
            self.Button1 = tk.Button(top)
            self.Button1.place(relx=0.1, rely=0.253, height=30, width=80)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(text='''Noodle +''', command=noodlespos)
            
            self.Button11 = tk.Button(top)
            self.Button11.place(relx=0.1, rely=0.300, height=30, width=80)
            self.Button11.configure(activebackground="#ececec")
            self.Button11.configure(activeforeground="#000000")
            self.Button11.configure(background="#d9d9d9")
            self.Button11.configure(disabledforeground="#a3a3a3")
            self.Button11.configure(foreground="#000000")
            self.Button11.configure(highlightbackground="#d9d9d9")
            self.Button11.configure(highlightcolor="black")
            self.Button11.configure(pady="0")
            self.Button11.configure(text='''Noodle -''', command=noodlesneg)  
    
            self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
            top.configure(menu = self.menubar)
    
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.363, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Burger+''',command=burgerpos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.410, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Burger-''',command=burgerneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.473, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Pasta+''',command=pastapos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.520, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Pasta-''',command=pastaneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.583, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Fries+''',command=friespos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.630, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Fries-''',command=friesneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.693, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Pizza+''',command=pizzapos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.1, rely=0.740, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Pizza-''',command=pizzaneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.253, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Wraps+''',command=wrapspos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.300, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Wraps-''',command=wrapsneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.363, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''HoneyChilli+''',command=honeychillipos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.410, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''HoneyChilli-''',command=honeychillineg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.473, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Coke+''',command=cokepos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.520, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Coke-''',command=cokeneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.583, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''IceCream+''',command=icecreampos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.630, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''IceCream-''',command=icecreamneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.693, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Tea+''',command=teapos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.37, rely=0.740, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Tea-''',command=teaneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.253, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Coffee+''',command=coffeepos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.300, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Coffee-''',command=coffeeneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.363, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Shake+''',command=shakepos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.410, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Shake-''',command=shakeneg)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.473, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Water+''',command=waterpos)
            
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.520, height=30, width=80)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Water-''',command=waterneg)
            
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.20, rely=0.27, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹150",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.20, rely=0.385, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹130",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.20, rely=0.495, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹200",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.20, rely=0.605, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹140",font="bold")
            
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.20, rely=0.715, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹300",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.48, rely=0.275, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹120",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.48, rely=0.385, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹180",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.48, rely=0.495, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹80",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.48, rely=0.605, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹150",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.48, rely=0.715, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹50",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.765, rely=0.275, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹60",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.765, rely=0.385, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹100",font="bold")
            
            self.Label16 = tk.Label(top)
            self.Label16.place(relx=0.765, rely=0.495, height=30, width=100)
            self.Label16.configure(background="#696969")
            self.Label16.configure(disabledforeground="#a3a3a3")
            self.Label16.configure(foreground="#00FFFF")
            self.Label16.configure(text="₹40",font="bold")
            
            
            
            
           
           
           
           
           
           
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.25, rely=0.8, height=80, width=87)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Reset''', command=reset)
            
            
            
            
            
            
            
            def proceed():
                
                 




                import time
                import random
                from tkinter import messagebox 
                #root.destroy()
                root=Tk()
                root.geometry("1920x1080")
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
                
                
                
                #noodles_qty=2
                noodles_q=noodles_qty
                #burger_qty=2
                burger_q=burger_qty
                #pasta_qty=2
                pasta_q=pasta_qty
                #fries_qty=2
                fries_q=fries_qty
                #pizza_qty=2
                pizza_q=pizza_qty
                #wraps_qty=2
                wraps_q=wraps_qty
                #honey_chilli_potato_qty=2
                honey_chilli_potato_q=honeychilli_qty
                #coke_qty=2
                coke_q=coke_qty
                #shakes_qty=2
                shakes_q=shake_qty
                #ice_cream_float_qty=2
                ice_cream_float_q=icescream_qty
                #tea_qty=2
                tea_q=tea_qty
                #coffee_qty=2
                coffee_q=coffee_qty
                #water_qty=2
                water_q=water_qty
                
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
                
                
                
                def total():
                    x=random.randint(80000000, 100000000)
                    l3=Label(f2,font=('aerial', '15', 'bold'), bd="5",text=x,bg="pink", width=18, relief="sunken")
                    l3.grid(row=0, column=1)
                    amt=(noodles_q*noodles_price)+(burger_q*burger_price)+(pasta_q*pasta_price)+(fries_q*fries_price)+(pizza_q*pizza_price)+(wraps_q*wraps_price)+(honey_chilli_potato_q*honey_chilli_potato_price)+(coke_q*coke_price)+(shakes_q*shakes_price)+(ice_cream_float_q*ice_cream_float_price)+(tea_q*tea_price)+(coffee_q*coffee_price)+(water_q*water_price)
                    amt=float(amt)
                    
                    sgst=0.025*amt
                    
                    cgst=0.025*amt
                    
                    total_payable=amt+sgst+cgst
                    l17=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=amt, width=18, relief="sunken")
                    l17.grid(row=5, column=3)
                    l18=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=sgst, width=18, relief="sunken")
                    l18.grid(row=6, column=3) 
                    l19=Label(f2,font=('aerial', '15', 'bold'), bd="5" ,bg="pink", text=cgst, width=18, relief="sunken")
                    l19.grid(row=7, column=3)
                    l20=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=total_payable, width=18, relief="sunken")
                    l20.grid(row=8, column=3)  
                
                
                
                l3=Label(f2,font=('aerial', '15', 'bold'), text="Reference", bd="10")
                l3.grid(row=0, column=0)   
                l3=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", width=18, relief="sunken")
                l3.grid(row=0, column=1)   
                
                l4=Label(f2,font=('aerial', '15', 'bold'), text="Noodles", bd="10")
                l4.grid(row=1, column=0)   
                l4=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=noodles_q, width=18, relief="sunken")
                l4.grid(row=1, column=1) 
                
                l5=Label(f2,font=('aerial', '15', 'bold'), text="Burger", bd="10")
                l5.grid(row=2, column=0)   
                l5=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=burger_q, width=18, relief="sunken")
                l5.grid(row=2, column=1)
                
                l6=Label(f2,font=('aerial', '15', 'bold'), text="Pasta", bd="10")
                l6.grid(row=3, column=0)   
                l6=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=pasta_q, width=18, relief="sunken")
                l6.grid(row=3, column=1)
                
                 
                
                l7=Label(f2,font=('aerial', '15', 'bold'), text="Fries", bd="10")
                l7.grid(row=4, column=0)   
                l7=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=fries_q, width=18, relief="sunken")
                l7.grid(row=4, column=1)  
                
                l8=Label(f2,font=('aerial', '15', 'bold'), text="Pizza", bd="10")
                l8.grid(row=5, column=0)   
                l8=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=pizza_q, width=18, relief="sunken")
                l8.grid(row=5, column=1)  
                
                l9=Label(f2,font=('aerial', '15', 'bold'), text="Wraps", bd="10")
                l9.grid(row=6, column=0)   
                l9=Label(f2,font=('aerial', '15', 'bold'), bd="5", bg="pink", text=wraps_q, width=18, relief="sunken")
                l9.grid(row=6, column=1) 
                
                l10=Label(f2,font=('aerial', '15', 'bold'), text="Honey chilli potato", bd="10")
                l10.grid(row=7, column=0)   
                l10=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=honey_chilli_potato_q, width=18, relief="sunken")
                l10.grid(row=7, column=1) 
                
                l11=Label(f2,font=('aerial', '15', 'bold'), text="Coke", bd="10")
                l11.grid(row=8, column=0)   
                l11=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=coke_q, width=18, relief="sunken")
                l11.grid(row=8, column=1) 
                
                
                
                l12=Label(f2,font=('aerial', '15', 'bold'), text="Shakes", bd="10")
                l12.grid(row=0, column=2)   
                l12=Label(f2,font=('aerial', '15', 'bold'), bd="5", bg="pink", text=shakes_q, width=18, relief="sunken")
                l12.grid(row=0, column=3)  
                
                l13=Label(f2,font=('aerial', '15', 'bold'), text="Ice cream float", bd="10")
                l13.grid(row=1, column=2)   
                l13=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=ice_cream_float_q, width=18, relief="sunken")
                l13.grid(row=1, column=3)  
                
                l14=Label(f2,font=('aerial', '15', 'bold'), text="Tea", bd="10")
                l14.grid(row=2, column=2)   
                l14=Label(f2,font=('aerial', '15', 'bold'), bd="5", bg="pink", text=tea_q, width=18, relief="sunken")
                l14.grid(row=2, column=3)  
                
                l15=Label(f2,font=('aerial', '15', 'bold'), text="Coffee", bd="10")
                l15.grid(row=3, column=2)   
                l15=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=coffee_q, width=18, relief="sunken")
                l15.grid(row=3, column=3)  
                
                l16=Label(f2,font=('aerial', '15', 'bold'), text="Mineral water bottle", bd="10")
                l16.grid(row=4, column=2)   
                l16=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", text=water_q, width=18, relief="sunken")
                l16.grid(row=4, column=3)  
                
                l17=Label(f2,font=('aerial', '15', 'bold'), text="Amount", bd="10")
                l17.grid(row=5, column=2)   
                l17=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink",  width=18, relief="sunken")
                l17.grid(row=5, column=3)  
                
                l18=Label(f2,font=('aerial', '15', 'bold'), text="SGST 2.5%", bd="10")
                l18.grid(row=6, column=2)   
                l18=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink",  width=18, relief="sunken")
                l18.grid(row=6, column=3)  
                
                l19=Label(f2,font=('aerial', '15', 'bold'), text="CGST 2.5%", bd="10")
                l19.grid(row=7, column=2)   
                l19=Label(f2,font=('aerial', '15', 'bold'), bd="5" ,bg="pink",  width=18, relief="sunken")
                l19.grid(row=7, column=3)  
                
                
                l20=Label(f2,font=('aerial', '15', 'bold'), text="Total amount payable", bd="10")
                l20.grid(row=8, column=2)   
                l20=Label(f2,font=('aerial', '15', 'bold'), bd="5",bg="pink", width=18, relief="sunken")
                l20.grid(row=8, column=3)  
                
                def exit():
                    messagebox.showinfo("Exit", "You will exit")
                    root.destroy()
                    
                        
                b1=Button(f2, text="Total", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"), command=total)
                b1.grid(row =9, column = 1, pady = 10, padx=70)
                
                
                b2=Button(f2, text="Back", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"), command=back)
                b2.grid(row = 9, column = 2, pady = 10, padx=70)
                
                b2=Button(f2, text="Exit", width="11", bd="10", relief="raised", bg="pink", font=("arial", "16", "bold"), command=exit)
                b2.grid(row = 9, column = 3,pady = 10, padx= 70)
                
                root.mainloop()


            
            
           
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.65, rely=0.8, height=80, width=87)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Proceed''', command=proceed)
            
            
            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.25, rely=0.01, height=71, width=650)
            self.Label1.configure(background="#FFC0CB")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='''FOOD MENU''',font=("Times new roman", "50", "bold"), relief="groove")
            self.Label2 = tk.Label(top)
            self.Label2.place(relx=0.40, rely=0.12, height=65, width=293,)
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(foreground="#000000")
            localtime = time.asctime()
            self.Label2.configure(text=localtime,font=("arial", "15"))
           
            
            
           
            
       
            
    
    if __name__ == '__main__':
        vp_start_gui()
        
back()       
        
    
      
