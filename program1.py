#Assignment 6: Program 1
def hi_to_low(fig1, fig2, fig3, fig4):
    if fig1 >= fig2 and fig1 >= fig3 and fig1 >= fig4:
        if fig2 >= fig3 and fig2 >= fig4:
            if fig3 >= fig4:
                num_order= {fig1, fig2, fig3, fig4}
                print(f"{num_order}")
            elif fig4 >= fig3:
                num_order= {fig1, fig2, fig4, fig3}
                print(f"{num_order}")
        elif fig3 >= fig2 and fig3 >= fig4:
            if fig2 >= fig4:
                num_order= {fig1, fig3, fig2, fig4}
                print(f"{num_order}")
            elif fig4 >= fig2:
                num_order= {fig1, fig3, fig4, fig2}
        elif fig4 >= fig2 and fig4 >= fig3:
            if fig3 >= fig2:
                num_order= {fig1, fig4, fig3, fig2}
                print(f"{num_order}")
            elif fig2 >= fig3:
                num_order= {fig1, fig4, fig2, fig3}
                print(f"{num_order}")
    elif fig2 >= fig1 and fig2 >= fig3 and fig2 >= fig4:
        if fig1 >= fig3 and fig1>= fig4:
            if fig3 >= fig4:
                num_order= {fig2, fig1, fig3, fig4}
                print(f"{num_order}")
            elif fig4 >= fig3:
                num_order= {fig2, fig1, fig4, fig3}
                print(f"{num_order}")

#Create a program that ask 4 numbers. 
num1= float(input("Enter first number here: "))
num2= float(input("Enter second number here: "))
num3= float(input("Enter third number here: "))
num4= float(input("Enter fourth number here: "))

#Print the 4 numbers from highest to lowest using only if-else statement.
hi_to_low(num1, num2, num3, num4)