import turtle as tu
def koch(t,x,n):
    ''' função para criar uma curva de koch simples com argumentos (t,x,n), onde o primeiro argumeto deve ser a tartaruga turtle.Turtle
        o segundo argumento o comprimento x do 
    '''
    
    angle = 60
    t.forward(x/3)
    t.left(angle)
    t.forward(x/3)
    t.right(2*angle)
    t.forward(x/3)
    t.left(angle)
    t.forward(x/3)
    if n > 0:
        t.left(angle)
        koch(t,x,n-2)
    if n > 0:
        t.right(2* angle)
        koch(t,x,n-2)
    if n > 0:
        t.left(angle)
        koch(t,x,n-2)


def snowflake(t,x,n):
    for v in range(0,3):
        koch(t,x,n)
        t.right(120)
    
    
t = tu.Turtle()

snowflake(t,50,2)
