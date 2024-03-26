def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0)
    ellipse(75, 75, 100, 150)
    triangle(100, 50, 100, 75, 150, 63)
    fill(255)
    ellipse(87, 50, 25, 25)  
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
