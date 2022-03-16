def Calc(operation, input):
    if input == 3:
        if operation == '+':
            def calc(a1,a2,b1,b2,b3 = None, a3 = None):
                c1 = a1 + b1
                c2 = a2 + b2
                c3 =  a3 + b3
                return c1,c2,c3


        elif operation == '-':
            def calc(a1,a2,b1,b2,b3 = None, a3 = None):
                c1 = a1 + b1
                c2 = a2 + b2
                c3 = a3 + b3
                return c1,c2,c3


        elif operation == '*':
            def calc(a1,a2,b1,b2,b3 = None, a3 = None):
                c1 = a1 + b1
                c2 = a2 + b2
                c3 = a3 + b3
                return c1,c2,c3

        elif operation == '/':
            def calc(a1,a2,b1,b2,b3 = None, a3 = None):
                c1 = a1 + b1
                c2 = a2 + b2
                c3 = a3 + b3
                return c1,c2,c3
        else:
            raise Exception('Я могу только делить, умножать, вычитать и прибавлять')
    else:
        if operation == '+':
            def calc(a1, a2, b1, b2):
                c1 = a1 + b1
                c2 = a2 + b2
                return c1, c2


        elif operation == '-':
            def calc(a1, a2, b1, b2):
                c1 = a1 + b1
                c2 = a2 + b2

                return c1, c2


        elif operation == '*':
            def calc(a1, a2, b1, b2):
                c1 = a1 + b1
                c2 = a2 + b2
                return c1, c2

        elif operation == '/':
            def calc(a1, a2, b1, b2):
                c1 = a1 + b1
                c2 = a2 + b2
                return c1, c2
        else:
            raise Exception('Я могу только делить, умножать, вычитать и прибавлять')
    return calc


vid_vektora = 2
counter = Calc('+', vid_vektora)
print(counter(12,28,34,15))


