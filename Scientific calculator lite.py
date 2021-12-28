import math as m
print('1.To calculate sum of two numbers, type: "+"')
print('2.To claculate difference between two numbers, type: "-"')
print('3.To multiply some numbers, type: "*"')
print('4.To divde two numbers, type: "/"')
print('5.To find remainder of division of two numbers, type: "%"')
print('6.To divide two numbers and terminate their fractionl part, type: "//"')
print('7.To find factorial of a number, type: "!"')
print('8.To find HCF and LCM of any two numbers, type: "hcf"')
print('9.To find the sum of numbers from a given number to another number, type: "s"')
print('10.To find the table of any number, type: "table"')
print('11.To find the square root of a number, type: "sqrt"')
print('12.To find the power "n" of a number "x", type: "power"')
print('13.To find valuse of sin(x) where x is angle in degrees or radians, type: "sin"')
print('14.To find value of cos(x) where x is angle in degrees or radians, type: "cos"')
print('15.To find value of tan(x) where x is angle in degrees or radians, type: "tan"')
print('16.To find value of cosec(x) where x is angle in degrees or radians, type: "cosec"')
print('17.To find valuse of sec(x) where x is angle in degrees or radians, type: "sec"')
print('18.To find value of cot(x) where x is angle in degrees or radians, type: "cot"')
print('19.To switch angle between degrees and radians, type: "swap"')
print('20.To CANCEL THE OPPERATION , type: "break"')
while True:
    a = input('Enter an operator: ')
    if a == '+':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x+y
        print(x,'+',y,'=', s)
    elif a == '-':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x-y
        print(x,'-',y,'=', s)
    elif a == '*':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x*y
        print(x,'*',y,'=', s)
    elif a == '/':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x/y
        print(x,'/',y,'=', s)
    elif a == '%':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x%y
        print(x,'%',y,'=', s)
    elif a == '//':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        s = x//y
        print(x,'//',y,'=', s)
    elif a == '!':
        x = float(input('Enter the number: '))
        s = m.factorial(x)
        print('Factorial of ',x, '=',s)
    elif a == 'hcf':
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        if x<y:
            s = x
        else:
            s = y
        hcf = 1
        for i in range(2,s+1):
            if x%i == 0 and y%i == 0:
                hcf = i
        lcm = x*y/hcf
        print('LCM of ',x,' and ',y,' is ',lcm,' and HCF of ',x,' and ',y,' is ',hcf)
    elif a == 's':
        x = int(input('Enter the number from which you want to start: '))
        y = int(input('Enter the number upto which you want to add: '))
        b = 0
        for i in range(x,y+1):
              b+=i
              i+=1
        print(b)
    elif a == 'table':
        n = int(input('enter a nuber to ptint its table: '))
        for i in range(0,21):
            a = n*i
            print(n,' X ',i,' = ',a)
        o = input('if you want this table to go further type "y" else "n": ')
        if o=='y':
            num = int(input('enter the number upto which u want the table to go: '))
            for j in range(21,num+1):
                        b= n*j
                        print(n,' X ',j,' = ',b)
            else:
                print('THANK YOU')
    elif a == "sqrt":
        x = float(input('Enter the number: '))
        z = m.sqrt(x)
        print('Square root of ',x,' = ',z)
    elif a == "power":
        x = float(input('Enter the number: '))
        y = float(input('Enter the power: '))
        z = m.pow(x,y)
        print(x,' to the power ',y,' = ',z)
    elif a == 'sin':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            x = m.sin(b)
            print('sin(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            x = m.sin(m.radians(b))
            print('sin(',b,')',' = ',x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == 'cos':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            x = m.cos(b)
            print('cos(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            x = m.cos(m.radians(b))
            print('cos(',b,')',' = ',x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == 'tan':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            x = m.tan(b)
            print('tan(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            x = m.tan(m.radians(b))
            print('tan(',b,')',' = ',x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == 'cosec':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('cosec(0 rad) is undefined or infinity')
            else:
                x = 1/m.sin(b)
                print('cosec(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('cosec(0 deg) is undefined or infinity')
            else:
                x = 1/m.sin(m.radians(b))
                print('cosec(', b, ')', ' = ', x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == 'sec':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('sec(0 rad) = 1')
            else:
                x = 1/m.cos(b)
                print('sec(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('sec(0 deg) = 1')
            else:
                x = 1/m.cos(m.radians(b))
                print('sec(',b,')',' = ',x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == 'cot':
        y = input('The angle is in "rad" or "deg"?: ')
        if y == 'rad':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('cot(0 rad) is undefined or infinity')
            else:
                x = 1/m.tan(b)
                print('cot(',b,')',' = ',x)
        elif y == 'deg':
            b = float(input('Enter the angle: '))
            if b == 0:
                print('cot(0 deg) is undefined or infinity')
            else:
                x = 1/m.tan(m.radians(b))
                print('cot(',b,')',' = ',x)
        else:
            print('Please type "rad" or "deg" only')
    elif a == "swap":
        b = input(' If the angle is in "deg" or "rad"?: ')
        if b == "rad":
            c = float(input('Enter the angle: '))
            x = m.degrees(c)
            print(c,' in degrees = ',x)
        elif b == "deg":
            c = float(input('Enter the angle: '))
            x = m.radians(c)
            print(c,' in radians = ',x)
        else:
            print('Please type "rad" or "deg" only')       
    elif a == 'break':
        break
    else:
        print('PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY')
        
    
                 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
   
