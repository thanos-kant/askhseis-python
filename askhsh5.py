#askhsh5 python , ari8mos mhtrwou P15050
x=raw_input("Grapse thn hmeromhnia (dd/mm/yyyy) :")
x=x.split("/")


#ypologismos tou aiwna
y=int(x[2])
c=y/100
if (c==19):
	c=0
elif (c==23):
	c=0
	
elif (c==18):
	c=2
elif (c==22):
	c=2
	
elif (c==17):
	c=4
elif (c==21):
	c=4
	
elif (c==16 ):
	c=6
elif (c==20):
	c=6	


#ypologismos tou etous 

y=(c+(y%100)+(y%100)/4)%7

#ypologismos tou mhna
m=int(x[1])
if (m==4):
	m=0
elif (m==7):
        m=0
elif (m==1):
	m=1
elif (m==10):
        m=1
elif (m==5):
	m=2
	
elif (m==8):
	m=3
	
elif (m==2 ):
	m=4
elif (m==3 ):
	m=4
elif (m==11):
	m=4

elif (m==6):
	m=5


elif (m==9):
	m=6
elif (m==12):
	m=6
	

#ypologismos ths hmeras
d=int(x[0])
d=(y+m+d)%7	

#euresh tou disektou etous
disy=int(x[1])
etos=1
if (y%4==0):
	etos=2
	
if (etos==2 and (disy==1 or disy==2)):
	d=d-1



#euresh hmeras
if (d==-1):
	hmera= "Paraskevh"
elif (d==0):
	hmera= "Savvato"
elif (d==1):
	hmera= "Kuriakh"
elif (d==2):
	hmera= "Deutera"
elif (d==3):	
	hmera= "Trith"
elif (d==4):
	hmera= "Tetarth"
elif (d==5):
	hmera= "Pempth"
elif (d==6):
	hmera= "Paraskeuh"

	
print "H hmera ths sugkekrimenhs hmeromhnias htan : " + hmera
