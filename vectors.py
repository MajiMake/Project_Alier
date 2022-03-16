def Calc(operation):
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
            return


    elif operation == '*':
        def calc(a1,a2,b1,b2,b3 = None, a3 = None):
            c1 = a1 + b1
            c2 = a2 + b2
            c3 = a3 + b3
            return

    elif operation == '/':
        def calc(a1,a2,b1,b2,b3 = None, a3 = None):
            c1 = a1 + b1
            c2 = a2 + b2
            c3 = a3 + b3
            return
    else:
        raise Exception('Я могу только делить, умножать, вычитать и прибавлять')
    return calc


def Fackinator(*args):
    if len(*args) == 4:
        a1 = args[0]
        a2 = args[1]
        b1 = args[2]
        b2 = args[3]
        return a1, a2, b1, b2
    elif len(*args) == 6:
        a1 = args[0]
        a2 = args[1]
        a3 = args[2]
        b1 = args[3]
        b2 = args[4]
        b3 = args[5]
        return a1, a2, a3, b1, b2, b3

def operate(op, numbers):
    oper = Calc(op)
    print(oper(Fackinator(numbers)))



operate('+', [22,75,88,11])


