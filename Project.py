#KNAPSACK 0-1 AND FRACTIONAL
#GROUP 1 PROJECT
#MUHAMMAD ASHRAAF BIN OMAR 1614253
#AMIRUL HAKIM BIN RUSLAN 1616169
#MUHAMMAD NUR FAQIH BIN SHAMSUDIN 1616891
#MUHAMMAD HAIKAL BIN ABDUL RAHIM 1616973
#MUHAIMIN BIN MOHD HASHIM 1621249
#MUHAMMAD IZZUDDIN BIN ZAHARI 1526213

from tkinter import *
import tkinter as tk
import tkinter.messagebox
from prettytable import PrettyTable
import winsound

def clear_widget(widget):
    widget.destroy()

def cb():
    if var.get():
        stop_sound()
    else:
        start_sound()

def start_sound():
    global SOUND_IS_ON
    winsound.PlaySound('music.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    SOUND_IS_ON = True

def stop_sound():
    winsound.PlaySound(None, winsound.SND_PURGE)
    SOUND_IS_ON = False

def validation(n, value, weight, maxcapacity):
    condition = True

    if n != len(value) or n!= len(weight):
        condition = False
    elif n <=0:
        condition = False
    elif maxcapacity < 0:
        condition = False
    return condition
   
def greedymethod():

    n, value, weight, maxcapacity = getinput()
    condition = validation(n, value, weight, maxcapacity)
    if condition == False:
        print("Error! Please check your input.")
        tkinter.messagebox.showinfo('Warning!','Error! Please check your input.')
    else:
        fractional_knapsack(value, weight, maxcapacity)

def dynamicmethod():

    n, value, weight, maxcapacity = getinput()
    condition = validation(n, value, weight, maxcapacity)
    if condition == False:
        print("Error! Please check your input.")
        tkinter.messagebox.showinfo('Warning!','Error! Please check your input.')
    else:
        zeroone_knapSack(maxcapacity, weight, value, n,)

def fractional_knapsack(value, weight, capacity):

    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
     
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    max_value_cumulative = [0]*len(value)
    weight_cumulative = [0]*len(value)
    weight_before = 0
    fractions = [0]*len(value)
    
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            weight_cumulative[i] =+ fractions[i]*weight[i]+weight_before
            weight_before =+weight_cumulative[i]
            max_value += value[i]
            max_value_cumulative[i]+=(max_value)
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            weight_cumulative[i] =+ fractions[i]*weight[i]+weight_before
            weight_before =+weight_cumulative[i]
            max_value += value[i]*capacity/weight[i]
            max_value_cumulative[i]+=(max_value)
            break


    print("*Fractional Knapsack (Greedy Method) *")
    print("The weight of items are ", weight)
    print("The value of items are ", value)
    print('The number in which the items should be taken:', fractions)
    print('The maximum Benefit(value) of items that can be carried:', max_value)
    

    text1="The weight of items are: "
    text2="The value of items are: "
    text3='The number in which the items should be taken:'
    text4='The maximum Benefit(value) of items that can be carried:'
        
    x = PrettyTable()

    x.field_names = ["Weight","Value","Value Density","Total Weight","Total Benefit"]

    for i in range (len(value)):
        x.add_row([weight[i],value[i],ratio[i],weight_cumulative[i],max_value_cumulative[i]])

    x.sortby = "Value Density"
    x.reversesort = True
    print(x)

    display = Tk()
    display.title("*Fractional Knapsack (Greedy Method) OUTPUT")
    Label1 = Label(display, text=text1)
    Labela = Label(display, text=weight)
    Label2 = Label(display, text=text2)
    Labelb = Label(display, text=value)
    Label3 = Label(display, text=text3)
    Labelc = Label(display, text=fractions)
    Label4 = Label(display, text=text4)
    Labeld = Label(display, text=max_value)
    Label5 = Label(display, text=x)
    Label1.pack()
    Labela.pack()
    Label2.pack()
    Labelb.pack()
    Label3.pack()
    Labelc.pack()
    Label4.pack()
    Labeld.pack()
    Label5.pack()
        
def zeroone_knapSack(capacity, weight, value, n):

    K = [[0 for w in range(capacity + 1)] 
            for i in range(n + 1)] 
              
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weight[i - 1] <= w: 
                K[i][w] = max(value[i - 1]  
                  + K[i - 1][w - weight[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w]

    print("*0-1 Knapsack (Dynamic Programming Method) *")

    y = PrettyTable()

    ylist = ["Value","Weight","Item"]

    for i in range (capacity+1):
        ylist.append(i)

    y.field_names = ylist

    value2 = [0] + value
    weight2 = [0] + weight
    
    for i in range (n+1):
        ylist2 =[value2[i],weight2[i],i]
        for w in range (capacity+1):
            ylist2.append(K[i][w])
        y.add_row(ylist2)

    print("The Value Table is : ")    
    print(y)

    V = [[0 for w in range(capacity + 1)] 
            for i in range(n + 1)]

    for i in range(n + 1): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                V[i][w] = 0
            elif K[i - 1][w] != K[i][w]: 
                V[i][w]= 1 
            else: 
                V[i][w]=0

    z = PrettyTable()
    z.field_names = ylist

    for i in range (n+1):
        ylist2 =[value2[i],weight2[i],i]
        for w in range (capacity+1):
            ylist2.append(V[i][w])
        z.add_row(ylist2)

    print("The Keep Table is : ")    
    print(z)
    
    # stores the result of Knapsack 
    result = K[n][capacity]
    finalresult = result
      
    w = capacity
    no_item = [0]*len(value)
    cummulative_weight = [0]*len(value)
    total_benefit = [0]*len(value)
    benefit_before=0
    weight_before=0
    
    for i in range(n, 0, -1): 
        if result <= 0: 
            break
        # either the result comes from the  top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack  table. If it comes from the latter 
        # one/ it means the item is included. 
        if result == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            temp = weight[i - 1]
            
            for j in range (n):
                if weight[j] == temp:
                    no_item[j]=+1
                    total_benefit[j] =+value[j]+ benefit_before
                    benefit_before =+ total_benefit[j] 
                    cummulative_weight[j]=+ temp + weight_before
                    weight_before=+cummulative_weight[j]
                    
            # Since this weight is included 
            # its value is deducted 
            result = result - value[i - 1] 
            w = w - weight[i - 1]

    print("The value of items are:", value)
    print("The weight of items are:", weight)
    print('The number in which the items should be taken:', no_item)
    print('The maximum Benefit(value) of items that can be carried:', finalresult)

    text1 = "The Value Table is :"
    text3 = "The Keep Table is :"
    text5 = "The value of items are:"
    text6 = "The weight of items are:"
    text7 = "The number in which the items should be taken:"
    text8 = "The maximum Benefit(value) of items that can be carried:"

    display = Tk()
    display.title("*0-1 Knapsack (Dynamic Programming Method) *")
    Label1 = Label(display, text=text1)
    Label2 = Label(display, text=y)
    Label3 = Label(display, text=text3)
    Label4 = Label(display, text=z)
    Label5 = Label(display, text=text5)
    Labela = Label(display, text=value)
    Label6 = Label(display, text=text6)
    Labelb = Label(display, text=weight)
    Label7 = Label(display, text=text7)
    Labelc = Label(display, text=no_item)
    Label8 = Label(display, text=text8)
    Labeld = Label(display, text=finalresult)
    
    Label1.pack()
    Label2.pack()
    Label3.pack()
    Label4.pack()
    Label5.pack()
    Labela.pack()
    Label6.pack()
    Labelb.pack()
    Label7.pack()
    Labelc.pack()
    Label8.pack()
    Labeld.pack()

def getinput():

    print("***NEW INPUT***")
    n = entry_n.get()
    n = int(n)
    print("The number of item is ",n)
    value = entry_value.get().split(" ")
    value = list(map(int, value))
    print("The value of the items are ",value)
    weight = entry_weight.get().split(" ")
    weight = list(map(int, weight))
    print("The weight of the items are ",weight)
    maxcapacity = entry_max.get()
    maxcapacity = int(maxcapacity)
    print("The maximum capacity of knapsack is ",maxcapacity)
    
    return n, value, weight, maxcapacity
    
def main():
    global root
    global display
    global Label
    
    root = Tk()
    root.title("0-1 and Fractional and Fractional Knapsack Solver Ver1.0")
    root.iconbitmap(r'iium_icon.ico')


    start_sound()

    global var
    var= IntVar()

    global entry_n
    global entry_value
    global entry_weight
    global entry_max

    theLabel = Label(root, text="Welcome to 0-1 and Fractional Knapsack Solver",bg="black",fg="white")
    theLabel.pack(fill=X)

    photo = PhotoImage(file="iium.png")
    photolabel = Label(root, image=photo)
    photolabel.pack()

    c = Checkbutton(root, text="Check to stop the sound",variable=var,command=cb)
    c.pack()

    message1 = Label(root, text="Please fill in the required data",bg="black",fg="white")
    message1.pack(fill=X)

    message2 = Label(root, text="The value you entered must be postive number only",bg="red",fg="white")
    message2.pack(fill=X)

    topFrame = Frame(root)
    topFrame.pack()

    label_n = Label(topFrame, text="Number of items")
    label_value = Label(topFrame, text="Value of items [each item seperate by SPACE]")
    label_weight = Label(topFrame, text="Weight of items [each item seperate by SPACE]")
    label_max = Label(topFrame, text="Maximum Weight")
    entry_n = Entry(topFrame)
    entry_value = Entry(topFrame)
    entry_weight = Entry(topFrame)
    entry_max = Entry(topFrame)

    label_n.grid(row=0,column=0,sticky=E)
    label_value.grid(row=1,column=0,sticky=E)
    label_weight.grid(row=2,column=0,sticky=E)
    label_max.grid(row=3,column=0,sticky=E)

    entry_n.grid(row=0,column=1)
    entry_value.grid(row=1,column=1)
    entry_weight.grid(row=2,column=1)
    entry_max.grid(row=3,column=1)


    message2 = Label(root, text="Please click the way you want the problem to be solved",bg="black",fg="white")
    message2.pack(fill=X)

    botFrame = Frame(root)
    botFrame.pack()

    button1 = Button(botFrame, text="0-1 Problem (Dynamic Programming Method)",command = dynamicmethod, fg="red")
    button2 = Button(botFrame, text="Fractional Problem (Greedy Method)",command=greedymethod, fg="blue")

    button1.pack(side=LEFT)
    button2.pack(side=LEFT)

    root.mainloop()

main()
