import turtle
turtle.tracer(0,0)
turtle.screensize(500,500)
turtle.pu()
turtle.goto(-0,-200)
turtle.pd()


def dessiner(courbe, longueur, angle):

    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere == 'F': turtle.forward(longueur)

def dessine_A(longueur, angle):
  Sequence_A = 'FF++FF++FF++F+F++F++F+'
  dessiner(Sequence_A,longueur,angle)

def dessine_B(longueur, angle):
  Sequence_B = 'F++FF'
  dessiner(Sequence_B,longueur,angle)

def Prebienski(counter,longueur, angle):
  dessine_A(longueur,angle)
  for i in range(3):
    if counter>1:
      Prebienski(counter-1,longueur*0.5,angle)
  dessine_B(longueur,angle)
  return counter-1

longueur = 10
angle = 120
niter = 5

counter = niter;

if counter >= 0:
  counter = Prebienski(counter, longueur, angle)

turtle.update()
turtle.exitonclick()