import turtle
import matplotlib.pyplot as plt
def draw_bar(t, height):
    """ função para desenhar um histograma com o modulo turtle . """
    t.begin_fill()           
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))#cria um rotulo indica a frequencia o dado 
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

wn = turtle.Screen()         # atribui uma corde fundo
wn.bgcolor("pink")

tess = turtle.Turtle()       # inicia a tartatura 
tess.color("blue", "red")
tess.pensize(3)
tess.penup()
tess.setpos(-300,-200)
tess.pendown()
xs = [48,117,200,240,160,260,220]
xx = [1,2,3,4,5,6,7]

for a in xs:
    draw_bar(tess, a)

num_bins = 7
plt.xlabel('Dados')
plt.ylabel('Número de ocorrencias')
plt.bar(xx,xs, color="red")
plt.show()
