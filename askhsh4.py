#askhsh4 python , ari8mos mhtrwou P15050
from PIL import Image, ImageDraw
import random
im = Image.new("RGB", (1024, 1024), "white")
draw = ImageDraw.Draw(im)
im.save('im.png')
#Dhmiourgia kenwn listwn me mege8os 20
x=[None] * 20
y=[None] * 20
r=[None] * 20

#topo8ethsh twn suntetagmenwn tou kentrou twn kuklwn kai twn aktinwn tou se listes x,y kai r antistoixa
for i in range(0,20):
    r[i] = random.randint(10,500)
    x[i] = random.randint(0,1024)
    y[i] =  random.randint(0,1024)
    
#elegxos gia temnomenous kuklous 
s=0
k=0
for i in range(0,20):
    c=0
    j=19
    while (j>i and c==0):
        m= ((x[i]-x[j])^2 + (y[i]-y[j])^2)^(1/2) 
        n= r[j]+r[i]
        k=k+1
    
        if m  <= n :
            c= c+1
        j=j-1  
    if c==1 :
        s=s+1
for i in range(0,20):
    draw.ellipse((x[i]-r[i], y[i]-r[i], x[i]+r[i], y[i]+r[i]), outline ='red')
#emfanizw s + 1 kuklous giati to s einai to a8roisma twn periptwsewn twn temnomenwn kuklwn , kai ka8e 1 periptwsh temnomenwn kuklwn apaitei 2 kuklous! 
print "oi kukloi pou temnontai einai :" , s +1
# apo8hkeuw tous kuklous se periptwsh mh emfanish tous apo ta programmata probolhs eikonwn tou upologisth 
im.save('im.png')
im.show()        
        

