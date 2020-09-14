###
# I made this basic GUI calculator as an exercise to learn about tkinter
###


# import
import tkinter as tk

### CONSTANT VARIABLES
NUM_BT_HEIGHT = 5
NUM_BT_WIDTH = NUM_BT_HEIGHT*2
WINDOW_HEIGHT = 502
WINDOW_WIDTH = 321

# http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
NUMBER_COLOR = "LightSteelBlue2"
OPERATOR_COLOR = "Light Gray"
CE_COLOR = "Gray"
EQ_COLOR = "Orange"

# maximum decimal places shown
DECIMAL_PLACES = 3

### Create window
window = tk.Tk()
window.title("Calculator")
window.geometry(str(WINDOW_WIDTH)+'x'+str(WINDOW_HEIGHT))
window.resizable(0,0)


### Top bar
topbar = tk.Label(window,text="",relief="ridge",borderwidth=6,font=("Arial Bold",12),bg="white",height=int(NUM_BT_HEIGHT/1.5),width=NUM_BT_WIDTH)
topbar.grid(column=0,row=0,columnspan=4,sticky='E'+'W')


### Function for button clicks
def clicked_bt(x,event=None):
    cur_top_bar = str(topbar.cget("text"))
    # print(cur_top_bar)
    if cur_top_bar == "ERROR":
        topbar.configure(text=str(x))
    else:
        newtext = cur_top_bar + str(x)
        topbar.configure(text=newtext)
    
    
### Number Buttons
bt_1 = tk.Button(window, text="1",command=lambda: clicked_bt(1),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_1.grid(column=0,row=4)
window.bind('<Key-1>',lambda a: clicked_bt(1,a))

bt_2 = tk.Button(window, text="2",command=lambda: clicked_bt(2),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_2.grid(column=1,row=4)
window.bind('<Key-2>',lambda a: clicked_bt(2,a))

bt_3 = tk.Button(window, text="3",command=lambda: clicked_bt(3),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_3.grid(column=2,row=4)
window.bind('<Key-3>',lambda a: clicked_bt(3,a))

bt_4 = tk.Button(window, text="4",command=lambda: clicked_bt(4),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_4.grid(column=0,row=3)
window.bind('<Key-4>',lambda a: clicked_bt(4,a))

bt_5 = tk.Button(window, text="5",command=lambda: clicked_bt(5),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_5.grid(column=1,row=3)
window.bind('<Key-5>',lambda a: clicked_bt(5,a))

bt_6 = tk.Button(window, text="6",command=lambda: clicked_bt(6),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_6.grid(column=2,row=3)
window.bind('<Key-6>',lambda a: clicked_bt(6,a))

bt_7 = tk.Button(window, text="7",command=lambda: clicked_bt(7),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_7.grid(column=0,row=2)
window.bind('<Key-7>',lambda a: clicked_bt(7,a))

bt_8 = tk.Button(window, text="8",command=lambda: clicked_bt(8),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_8.grid(column=1,row=2)
window.bind('<Key-8>',lambda a: clicked_bt(8,a))

bt_9 = tk.Button(window, text="9",command=lambda: clicked_bt(9),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_9.grid(column=2,row=2)
window.bind('<Key-9>',lambda a: clicked_bt(9,a))

bt_0 = tk.Button(window, text="0",command=lambda: clicked_bt(0),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=NUMBER_COLOR)    
bt_0.grid(column=1,row=5)
window.bind('<Key-0>',lambda a: clicked_bt(0,a))


### Operator Buttons
bt_div = tk.Button(window, text="/",command=lambda: clicked_bt('/'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=OPERATOR_COLOR)    
bt_div.grid(column=3,row=1)
window.bind('<Key-/>',lambda a: clicked_bt('/',a))

bt_mul = tk.Button(window, text="*",command=lambda: clicked_bt('*'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=OPERATOR_COLOR)    
bt_mul.grid(column=3,row=2)
window.bind('<Key-*>',lambda a: clicked_bt('*',a))

bt_sub = tk.Button(window, text="-",command=lambda: clicked_bt('-'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=OPERATOR_COLOR)    
bt_sub.grid(column=3,row=3)
window.bind('<Key-minus>',lambda a: clicked_bt('-',a))

bt_add = tk.Button(window, text="+",command=lambda: clicked_bt('+'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=OPERATOR_COLOR)    
bt_add.grid(column=3,row=4)
window.bind('<Key-plus>',lambda a: clicked_bt('+',a))


### Misc Buttons
bt_opbr = tk.Button(window, text="(",command=lambda: clicked_bt('('),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH)    
bt_opbr.grid(column=1,row=1)
window.bind('<Key-(>',lambda a: clicked_bt('(',a))

bt_clbr = tk.Button(window, text=")",command=lambda: clicked_bt(')'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH)    
bt_clbr.grid(column=2,row=1)
window.bind('<Key-)>',lambda a: clicked_bt(')',a))

bt_dec = tk.Button(window, text=".",command=lambda: clicked_bt('.'),height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH)    
bt_dec.grid(column=0,row=5)
window.bind('<Key-.>',lambda a: clicked_bt('.',a))


### Clear Button
def clicked_bt_AC(event=None):
    topbar.configure(text="")
bt_CE = tk.Button(window, text="AC",command=clicked_bt_AC,height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=CE_COLOR)    
bt_CE.grid(column=0,row=1)
window.bind('<Key-c>',lambda a: clicked_bt_AC(a))
window.bind('<Key-space>',lambda a: clicked_bt_AC(a))


### Equal Button
def clicked_bt_eq(event=None):
    if len(str(topbar.cget("text"))) > 30:
        topbar.configure(text="ERROR")
    try:
        expression = topbar.cget("text")
        #alternative to eval?
        answer = str(round(eval(expression),DECIMAL_PLACES))
        topbar.configure(text=answer)
    except:
        topbar.configure(text="ERROR")
bt_eq = tk.Button(window, text="=",command=clicked_bt_eq,height=NUM_BT_HEIGHT,width=NUM_BT_WIDTH,bg=EQ_COLOR)    
bt_eq.grid(column=2,row=5,columnspan=2,sticky='E'+'W')
window.bind('<Return>',lambda a: clicked_bt_eq(a))
window.bind('<Key-=>',lambda a: clicked_bt_eq(a))


### RUN CODE ###
window.mainloop()