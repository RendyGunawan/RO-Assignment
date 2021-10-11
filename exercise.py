operator = eval(input('select an operator by using the number(1.Addition, 2.Subtraction, 3.Multiplication, 4.Division'))
number_1=eval(input("enter a number: "))
number_2=eval(input("enter another number: "))
result=0
if(operator==1):
    result=number_1+number_2
    print(f'The result is: {result}')
elif(operator==2):
    result=number_1-number_2
    print(f'The result is: {result}')
elif(operator==3):
    result=number_1*number_2
    print(f'The result is: {result}')
else:
    result=number_1/number_2
    print(f'The result is: {result}')
