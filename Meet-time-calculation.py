##This program calculates the time two cars meet in multiple situations
##Input: road_maintain_info.txt, output: new_RW_info.txt

import sys
from tkinter import *

AB = 500 #distance between A and B - constant variable
Va = 100.5 #float variable
Vb = [80,-80] #list of integer variables
hour = ('hour','hours') #tuple of string variables
start_program = True #boolean varable

##inputs of dictionaries for command-line menu
menu_option = { 
    1: 'Same (road work expected)',
    2: 'Reverse',
    3: 'Exit',
    }

time_option = {
    1: '0 hour', #travel at the same time
    2: '1 hour', #A travels 1 hour before B
    3: '2 hours',#A travels 2 hours before B
    }

##transfer info from input file to output file
def process_file(i_file,o_file):
    for line in i_file:
        o_file.writelines(line)

##update the output file with the info that input file is missing
def update_o_file(o_file):
    global list3
    list1=[]
    string = ','.join([str(item) for item in list3])
    list1 = string
    o_file.writelines(list1)

##open input text file and create/update output text file        
def process_text_files():
    in_file_str = input('Enter road work information file: ')
    try:
        in_file = open(in_file_str,'r')
    except FileNotFoundError:
#'FileNotFoundError' used as unacceptable file name could be entered by the user
        print('The file', in_file_str,' does not exit')
        sys.exit()
    out_file = open('new_RW_info.txt','w')   
    process_file(in_file,out_file) #transfer info from input file to output file
    out_file = update_o_file(out_file) #add the lacking info to output file
    in_file.close()



def in_file():
    return open('road_maintain_info.txt','r')

##Create lists of road work info for calculation
info_list = []
for row in in_file():
    tokens = row.strip().split(',')
    info_list.append(tokens)
list3 = [2,60,150]
info_list.append(list3)
list1 = info_list[0]
list2 = info_list[1]




##define functions for displaying command-line menu
def print_menu():
    for key in menu_option.keys():
        print(key, '--', menu_option[key])

def print_menu1():
    for key in time_option.keys():
        print(key, '--', time_option[key])

def print_menu2():
    for key in time_option.keys():
        print(key, '--', time_option[key], end=', ')
        a = key - 1
        print('RW speed: {0}km/h, RW distance: {1}km'.\
                format(info_list[a][1],info_list[a][2]))
            
#define functions for calculating and displaying results
def t1(t,hour1):
    a = eval(list1[2])
    b = eval(list1[1])
    c = eval(list1[0])
    t = a/b + (AB - a + Vb[0]*((a/b))-c)/(Va-Vb[0])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1

def t2(t,hour1):
    a = eval(list2[2])
    b = eval(list2[1])
    c = eval(list2[0])
    t = a/b + (AB - a + Vb[0]*((a/b)-c))/(Va-Vb[0])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1

def t3(t,hour1):
    a = list3[2]
    b = list3[1]
    c = list3[0]
    t = a/b + (AB - a + Vb[0]*((a/b)-c))/(Va-Vb[0])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1   
            
def t4(t,hour1):
    t = (AB - Vb[1]*0)/(Va-Vb[1])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1           

def t5(t,hour1):
    t = (AB - Vb[1]*1)/(Va-Vb[1])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1

def t6(t,hour1):
    t = (AB - Vb[1]*2)/(Va-Vb[1])
    if t > 1:
        hour1 = hour[1]
    else:
        hour1 = hour[0]
    return t,hour1

while start_program:
    process_text_files()
    print_menu()
    option = ''

    ##ensure input is correct
    try: 
        option = int(input('Enter choice of direction: '))
    except ValueError:
        print('Wrong input. Please enter a number!')
        sys.exit()
           
    if option == 1: #option 1 is same in the command-line menu
        print_menu2()
        option1 =''

        ##ensure input is correct
        try:
            option1 = int(input('Enter choice of time diff: '))
        except ValueError:
            print('Wrong input. Please enter a number!')
            sys.exit()
                
        if option1 == 1:    #option 1 is 0 hour in the command-line menu
            t,hour1= t1(t1,hour)
            print('If car A travels same time with car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        elif option1 == 2:#option 2 is 1 hour in the command-line menu
            t,hour1 = t2(t1,hour)
            print('If car A travels 1 hour before car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        elif option1 == 3:#option 3 is 2 hours in the command-line menu
            t,hour1 = t3(t1,hour)
            print('If car A travels 2 hours before car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
                  
    elif option == 2: #option 2 is reverse in the command-line menu
        print_menu1()
        option2 = ''

        ##ensure input is correct
        try:
            option2 = int(input('enter choice of time diff: '))
        except ValueError:
            print('Wrong input. Please enter a number!')
            sys.exit()

        if option2 == 1: #option 1 is 0 hour in the command-line menu
            t,hour1 = t4(t1,hour)
            print('If car A travels same time with car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        elif option2 == 2:#option 2 is 1 hour in the command-line menu
            t,hour1 = t5(t1,hour)
            print('If car A travels 1 hour before car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        elif option2 == 3:#option 3 is 2 hours in the command-line menu
            t,hour1 = t6(t1,hour)
            print('If car A travels 2 hours before car B, ', end = '\n')
            print('\t they will meet after car A has travelled: ', end ='')
            print('{0:.2f} {1:}'.format(t,hour1))
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
                       
    elif option == 3:
        exit()
            
    else: #when the input is > 3
        print('Invalid option. Please enter a number between 1 and 3.')
    break #stop the program from running infinite loops

##define the result display when calculation button is clicked
def findResult():
    entTimeDiff_int = eval(entTimeDiff.get())
    directionChoice = directionSelection()
    if directionChoice == menu_option[1]:
        if entTimeDiff_int == 0:
            t,hour1 = t1(t1,hour)
        elif entTimeDiff_int == 1:
            t,hour1 = t2(t1,hour)
        elif entTimeDiff_int == 2:
            t,hour1 = t3(t1,hour)
        else:
            t = 0
            hour1 = '- wrong input'
    if directionChoice == menu_option[2]:
        if entTimeDiff_int == 0:
            t,hour1 = t4(t1,hour)
        elif entTimeDiff_int == 1:
            t,hour1 = t5(t1,hour)
        elif entTimeDiff_int == 2:
            t,hour1 = t6(t1,hour)
        else:
            t = 0
            hour1 = '- wrong input'
    Result.set('{0:.2f} {1}'.format(t,hour1))

##determine the choice made by user in order to implement calculation            
def directionSelection():
    global lstDirection
    return lstDirection.get(lstDirection.curselection())


window = Tk()

##ensure the window is expanded smoothly by the user
for i in range (3):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    window.title("Meeting time calculation")

    ##display background info
    lblInfo = Label(window, text="Background Info:\n    Velocity of Car A:    100.5km/h\n\
Velocity of Car B:    80km/h \n Distance from A to B: 500km", fg="red")
    lblInfo.grid(row=0,column=0,padx=5,pady=5,sticky="w")

    ##display road work info
    lblRoadInfo = Label(window, text="Road Work Info:\n\
 0 hour: RW speed: 40km/h, RW distance: 50km\n\
 1 hour: RW speed: 50km/h, RW distance: 100km \n\
 2 hours: RW speed: 60km/h, RW distance: 150km",fg="red")
    lblRoadInfo.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky="e")
                                  
    ##label for the listbox
    lblChoice = Label(window, text="Choice of Direction", fg="black", bg="yellow")
    lblChoice.grid(row=1,column=0,padx=5,pady=5)

    ##label for user entry widget
    lblUserEntry = Label(window, text="Enter time diff (hour/hours)",fg="black", bg="yellow")
    lblUserEntry.grid(row=1,column=2, padx=5,pady=5)

    ##create listbox of direction choice    
    conOFdirectionList = StringVar()
    lstDirection = Listbox(window, width=25, height=2, fg="blue",bg="orange",\
                       listvariable=conOFdirectionList)
    lstDirection.grid(row=2,column=0,padx=5,pady=5)
    directionList = [menu_option[1],menu_option[2]]
    conOFdirectionList.set(tuple(directionList))

    ##create entry widget allowing user to input data 
    TimeDiff = StringVar()
    entTimeDiff = Entry(window,width=5,fg="blue",bg="orange",textvariable=TimeDiff)
    entTimeDiff.grid(row=2,column=2,padx=5,pady=5,sticky="ns")

    ##create calculation button to generate calculation for finding final result
    btnCalculate = Button(window,text="Calculate",fg="red", bg="white",command=findResult)
    btnCalculate.grid(row=3,column=1,padx=5,pady=5)

    ##label for displaying result
    lblResult = Label(window, text="Time until both cars meet after car A starts travelling:",\
                  fg="black", bg="yellow")
    lblResult.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

    ##create a readonly entry to display result
    Result = StringVar()
    entResult = Entry(window, state="readonly",width=20,fg="blue",textvariable=Result)
    entResult.grid(row=4,column=2,padx=5,pady=5,sticky="ns")

    ##create an exit button to close the program
    btnCalculate = Button(window,text="Exit",fg="red", bg="white",command= window.destroy)
    btnCalculate.grid(row=5,column=1,padx=5,pady=5)
    
window.mainloop()   

