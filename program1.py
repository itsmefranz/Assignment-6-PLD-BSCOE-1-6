#Assignment 6: Program 1
#Create a program that ask 4 numbers. 
def inputFour():
    while True:
        try:
            num1= float(input("Enter first number here: "))
            num2= float(input("Enter second number here: "))
            num3= float(input("Enter third number here: "))
            num4= float(input("Enter fourth number here: "))
            break
        except ValueError as error:
            print(f"Invalid input. This is unacceptabl. {error}. Please try again.")
    return num1, num2, num3, num4

#Print the 4 numbers from highest to lowest using only if-else statement.
def hi_to_low(fig1, fig2, fig3, fig4):
##conditions assuming that the first number is the highest    
    if fig1 >= fig2 and fig1 >= fig3 and fig1 >= fig4:
        if fig2 >= fig3 and fig2 >= fig4:
            if fig3 >= fig4:
                num_order= [fig1, fig2, fig3, fig4]
                print(f"{num_order}")
            elif fig4 >= fig3:
                num_order= [fig1, fig2, fig4, fig3]
                print(f"{num_order}")
        elif fig3 >= fig2 and fig3 >= fig4:
            if fig2 >= fig4:
                num_order= [fig1, fig3, fig2, fig4]
                print(f"{num_order}")
            elif fig4 >= fig2:
                num_order= [fig1, fig3, fig4, fig2]
                print(f"{num_order}")
        elif fig4 >= fig2 and fig4 >= fig3:
            if fig3 >= fig2:
                num_order= [fig1, fig4, fig3, fig2]
                print(f"{num_order}")
            elif fig2 >= fig3:
                num_order= [fig1, fig4, fig2, fig3]
                print(f"{num_order}")

#conditions assuming that the second number is the highest
    elif fig2 >= fig1 and fig2 >= fig3 and fig2 >= fig4:
        if fig1 >= fig3 and fig1>= fig4:
            if fig3 >= fig4:
                num_order= [fig2, fig1, fig3, fig4]
                print(f"{num_order}")
            elif fig4 >= fig3:
                num_order= [fig2, fig1, fig4, fig3]
                print(f"{num_order}")
        elif fig3 >= fig1 and fig3 >= fig4:
            if fig1 >= fig4:
                num_order= [fig2, fig3, fig1, fig4]
                print(f"{num_order}")
            elif fig4 >= fig1:
                num_order= [fig2, fig3, fig4, fig1]
                print(f"{num_order}")
        elif fig4 >= fig3 and fig4 >= fig1:
            if fig3 >= fig1:
                num_order= [fig2, fig4, fig3, fig1]
                print(f"{num_order}")
            elif fig1 >= fig3:
                num_order= [fig2, fig4, fig1, fig3]
                print(f"{num_order}")

#conditions assuming that the third number is the highest
    elif fig3 >= fig1 and fig3 >= fig2 and fig3 >= fig4:
        if fig1 >= fig2 and fig1 >= fig4:
            if fig2 >= fig4:
                num_order= [fig3, fig1, fig2, fig4]
                print(f"{num_order}")
            elif fig4 >= fig2:
                num_order= [fig3, fig1, fig4, fig2]
                print(f"{num_order}")
        elif fig2 >= fig1 and fig2 >= fig4:
            if fig1 >= fig4:
                num_order= [fig3, fig2, fig1, fig4]
                print(f"{num_order}")
            elif fig4 >= fig1:
                num_order= [fig3, fig2, fig4, fig1]
                print(f"{num_order}")
        elif fig4 >= fig1 and fig4 >= fig2:
            if fig1 >= fig2:
                num_order= [fig3, fig4, fig1, fig2]
                print(f"{num_order}")
            elif fig2 >= fig1:
                num_order= [fig3, fig4, fig2, fig1]
                print(f"{num_order}")

#conditions assuming that the fourth number is the highest
    elif fig4 >= fig1 and fig4 >= fig2 and fig4 >= fig3:
        if fig1 >= fig2 and fig1 >= fig3:
            if fig3 >= fig2:
                num_order= [fig4, fig1, fig3, fig2]
                print(f"{num_order}")
            elif fig2 >= fig3:
                num_order= [fig4, fig1, fig2, fig3]
                print(f"{num_order}")
        elif fig2 >= fig1 and fig2 >= fig3:
            if fig1 >= fig3:
                num_order=[fig4, fig2, fig1, fig3]
                print(f"{num_order}")
            elif fig3 >= fig1:
                num_order= [fig4,fig2, fig3, fig1]
                print(f"{num_order}")
        elif fig3 >= fig1 and fig3 >= fig2:
            if fig2 >= fig1:
                num_order= [fig4, fig3, fig2, fig1]
                print(f"{num_order}")
            elif fig1 >= fig2:
                num_order= [fig4, fig3, fig1, fig2]
                print(f"{num_order}")

_num1, _num2, _num3, _num4= inputFour()
order_num= hi_to_low(_num1, _num2,_num3,_num4)

