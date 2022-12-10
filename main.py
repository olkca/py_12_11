def plus():
    r = q1 + q2
    p = 'додавання'
    t = p
    print ('Результат ',t,' = ',r)
def subtraction():
    r = q1 - q2
    l = 'віднімання'
    t = l
    print ('Результат ',t,' = ',r)
def division():
    r = float(q1 / q2)
    m = 'ділення'
    t = m
    print ('Результат ',t,' = ',r)
def multiplication():
    r = q1 * q2
    n = 'множення'
    t = n
    print ('Результат ',t,' = ',r)

q1 = int (input('В 1: '))
q3 = (input('В: '))
q2 = int (input('В 2: '))
if q3 == "+":
    plus()
if q3 == "-":
    subtraction()
if q3 == "*":
    multiplication()
if q3 == "/":
    division()