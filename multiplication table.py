def multiplication_table(num):
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
n = int(input("Enter a number:"))
multiplication_table(n)

