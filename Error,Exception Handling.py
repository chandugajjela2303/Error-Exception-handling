#Error handling
#syntax error
'''for i in range(10):
    print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''

#logical error
'''a=20
b=40
print(a-b)'''


'''a=3
b=9
if a<b:
    print("less")

a=3
b=9
if a>b:
    print("less")'''
    
#EXCEPTION HANDLING:
#TRY : Instructions from which we are expecting the exceptions.
#EXCEPT : Exception is raised in try block it will be handle by this block.
#ELSE : Optional(non-exceptions)
#FINALLY : Always it will display

while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends......")
        
    
