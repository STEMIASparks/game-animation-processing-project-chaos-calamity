def start():
    global x,y,w,l,sx,sy,h,s,score,t,done,objects
    #variables for dinosaur
    x = 80
    y = 230
    w = 20
    l = 50
    #varables for obsticles
    h = 250
    t = 280
    objects = [random(10,20), random(30,65)]
    #varables for movement
    sx = 0 
    sy = 1
    #varable for speed
    s = -350
    #Varable for score
    score = 0
    #variable turn on
    done = False
    
#makes keys work
def keyReleased():
    global done
    if done and (key == 'r' or key == 'R'):
        start()
        loop()

def setup():
    size (500,350)
    start()
    
def draw():
    global x, y, w, l, sx, sy, h, s, score, t, objects, done
    clear()
    background(255,255,255)
    line(1,280,500,280)

    i = 1
    xObject = t-s
#checking collition and game over screen 
    if xObject+objects[0] >= x and xObject <= (x+w):
        if (y*i)+l >= t-objects[1]:
            text ("GAME OVER", 200,150)
            done = True
            text("Restart? Press R", 180,170)
            noLoop()

# moving the player  
    while i < 2:
        fill(0,0,0)
        rect(x,y*i,w,l)
        i += 1
    x += sx
    if x > 500:
        x = 1  
        
#what makes the block come down after a jump
    y -= sy
    x += sx
    sy-=0.25
    if y+50 >= 280:
        sy=1
        
#key command to make the block jump at a certain height
    if keyPressed and y > 210:
        sy += 1 

 #makes objects move
    if objects[1] + h > t:
        h = t - objects[1]
    rect(t-s,h,objects[0], objects[1])  
    s += 5
    
# repositioning of objects
    if t-s <= 0:
        s = -350
        objects[0] = random(10,20)
        objects[1] = random(30,65)
    elif objects[1] < t:
        h = t

#score
    textSize(20)
    text("HI   " + str(score),380,30)
    fill(0,0,0)
    score += 1
