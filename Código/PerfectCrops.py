from sense_hat import SenseHat
import time
import datetime
from time import sleep
from guizero import App, Text, PushButton, Picture

sense = SenseHat()
sense.clear()
orientation=sense.get_orientation()
roll=orientation['roll']


e=(0,0,0)
w=(255,255,255)
r=(255,0,0)
a=(0,0,255)
y=(255,255,0)
o=(255,150,0)
c=(0,150,255)
g=(0,255,0)
dg=(0,125,0)
z=(200,170,120)
cb=(255,150,230)
pp=(170,0,255)
v=(150,100,50)

cold=[
e,e,e,e,e,w,e,e,
e,e,e,e,w,e,e,e,
e,e,e,w,e,e,e,w,
e,w,w,a,e,e,w,e,
w,a,a,a,a,w,e,e,
w,a,a,a,w,e,e,e,
w,a,a,a,w,e,e,e,
e,w,w,w,e,e,e,e,
]

hot=[
e,e,e,e,e,w,r,r,
e,e,e,e,w,r,r,r,
e,e,e,w,r,r,r,w,
e,w,w,r,r,r,w,e,
w,r,r,r,r,w,e,e,
w,r,r,r,w,e,e,e,
w,r,r,r,w,e,e,e,
e,w,w,w,e,e,e,e,
]

dry=[
y,o,o,y,o,o,o,y,
o,y,o,y,y,o,y,o,
o,o,y,y,y,y,o,o,
o,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,o,
o,o,y,y,y,y,o,o,
o,y,o,y,y,o,y,o,
y,o,o,o,y,o,o,y,
]

wet=[
e,e,e,e,e,c,e,e,
e,e,e,e,c,c,e,e,
e,e,e,c,w,a,e,e,
e,e,c,w,a,a,e,e,
e,c,c,a,a,a,a,e,
e,a,a,a,a,a,a,e,
e,e,a,a,a,a,e,e,
e,e,e,e,e,e,e,e,
]


def crop1():
    tomato=[
        e,g,e,e,e,e,e,e,
        e,e,g,g,e,g,g,e,
        e,e,e,g,g,e,e,g,
        e,e,r,g,g,r,e,e,
        e,r,r,r,r,r,r,e,
        e,r,r,r,r,r,r,e,
        e,r,r,r,r,r,r,e,
        e,e,r,r,r,r,e,e,
        ]
    return tomato

def crop2():
    lettuce=[
        e,e,e,e,e,e,e,e,
        e,e,e,dg,g,g,e,e,
        e,dg,g,dg,g,g,dg,e,
        g,g,dg,g,dg,g,g,g,
        g,g,dg,dg,g,g,g,dg,
        dg,dg,dg,g,dg,g,dg,e,
        e,dg,dg,dg,dg,dg,dg,e,
        e,e,dg,dg,dg,dg,e,e,
        ]
    return lettuce

def crop3():
    strawberry=[
        e,e,g,e,e,e,g,e,
        e,e,g,g,e,g,e,e,
        e,e,e,r,g,g,e,e,
        e,e,r,r,r,y,e,e,
        e,r,y,r,r,r,r,e,
        e,y,r,r,r,y,r,e,
        e,e,r,y,r,r,e,e,
        e,e,e,r,r,e,e,e,
        ]
    return strawberry

def crop4():
    onion=[
        e,e,g,g,e,g,e,e,
        e,e,g,g,g,g,e,e,
        e,e,e,g,g,e,e,e,
        e,e,cb,cb,cb,w,e,e,
        e,cb,cb,cb,w,cb,w,e,
        e,cb,w,cb,w,cb,w,e,
        e,cb,w,cb,w,cb,w,e,
        e,e,cb,w,cb,w,e,e,
        ]
    return onion

def crop5():
    eggplant=[
        e,e,e,e,e,e,e,e,
        e,e,e,e,g,g,g,e,
        e,e,e,e,pp,g,g,g,
        e,e,pp,pp,pp,pp,pp,g,
        e,pp,pp,pp,pp,pp,pp,e,
        e,pp,pp,pp,pp,pp,e,e,
        e,e,pp,pp,pp,pp,e,e,
        e,e,e,e,e,e,e,e,
        ]
    return eggplant

def crop6():
    peas=[
        e,e,e,e,e,e,e,e,
        g,g,e,e,e,g,g,e,
        g,dg,e,e,e,g,dg,e,
        e,e,e,e,e,e,e,e,
        e,g,g,e,e,e,e,e,
        e,g,dg,e,e,g,g,e,
        e,e,e,e,e,g,dg,e,
        e,e,e,e,e,e,e,e,
        ]
    return peas

def crop7():
    bean=[
        e,e,e,e,e,e,e,e,
        e,e,z,z,z,z,z,e,
        e,z,z,z,z,z,z,e,
        e,z,z,z,v,v,z,e,
        e,z,z,v,v,e,e,e,
        e,z,z,v,e,e,e,e,
        e,z,z,z,e,e,e,e,
        e,e,e,e,e,e,e,e,
        ]
    return bean

def start():
    crops=[crop1,crop2,crop3,crop4,crop5,crop6,crop7]
    contador=0

    sense.set_pixels(crops[contador%len(crops)]())
    logic= True
    while logic: 
        orientation=sense.get_orientation()
        acceleration=sense.get_accelerometer_raw()
        z=acceleration['z']
        roll=orientation['roll']
        roll = round(roll,1)
        print(roll)
        if roll>90 and roll<180:
            print('next '+ str(roll))
            contador+=1
            sense.set_pixels(crops[contador%len(crops)]())
            sleep(2)
        if roll<= 350 and roll >270:
            print('prev ' + str(roll))
            contador-=1
            sense.set_pixels(crops[contador%len(crops)]())
            sleep(2)
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                print('press')
                CROP=crops[contador%len(crops)]()
                logic= False






    while True:
        t=sense.get_temperature()
        h=sense.get_humidity()

        date=datetime.datetime.now()
        H=date.hour
        M=date.minute
        
        p= str(H)
        k=':'
        m= str(M)

        t=round(t,1)
        h=round(h,1)

        if CROP==crop1():
            night=18
            morning=7
            hmin=50
            hmax=60
            if H<night and H>morning:
                tmin=21
                tmax=27
            else:
                tmin=16
                tmax=18

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''
        if CROP==crop2():
            night=18
            morning=7
            hmin=60
            hmax=80
            if H<night and H>morning:
                tmin=10
                tmax=24
            else:
                tmin=5
                tmax=15

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    """-------------------------------------------------------------------------------------------------------------------------------------------"""
                        
        if CROP==crop3():
            night=18
            morning=7
            hmin=70
            hmax=80
            if H<=night and H>=morning:
                tmin=26
                tmax=35
            else:
                tmin=10
                tmax=26

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''

        if CROP==crop4():
            night=16
            morning=8
            hmin=45
            hmax=65
            if H<=night and H>=morning:
                tmin=16
                tmax=25
            else:
                tmin=13
                tmax=20

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''

        if CROP==crop5():
            night=18
            morning=7
            hmin=50
            hmax=60
            if H<=night and H>=morning:
                tmin=25
                tmax=30
            else:
                tmin=20
                tmax=25

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''
        if CROP==crop6():
            night=16
            morning=8
            hmin=65
            hmax=75
            if H<=night and H>=morning:
                tmin=16
                tmax=18
            else:
                tmin=13
                tmax=15

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''
        if CROP==crop7():
            night=20
            morning=7
            hmin=60
            hmax=75
            if H<=night and H>=morning:
                tmin=18
                tmax=21
            else:
                tmin=19
                tmax=25

            """--------------------------------------------------------------------------------------------------------------------------------------"""    
            if H<=night and H>=morning:

                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0,255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
                    
            else:
                
                if t>tmin and t<tmax and h>hmin and h<hmax:
                    bg=[0, 255,0]
                else:
                    bg=[255,0,0]

                msg= "Temp={0},Hum={1} ".format(t,h)

                sense.show_message(msg+p+k+m,scroll_speed=0.09, text_colour=bg)

                sleep(1)

                if t>tmax:
                    sense.set_pixels(hot)
                    sleep(2)
                    
                if t<tmin:
                    sense.set_pixels(cold)
                    sleep(2)

                if h<hmin:
                    sense.set_pixels(dry)
                    sleep(2)

                if h>hmax:
                    sense.set_pixels(wet)
                    sleep(2)
        ''' ------------------------------------------------------------------------------------------------------------------------------------------- '''

    
app=App(title="Perfect CROPS")
update_text=PushButton(app,command=start, text="START")
perfect_crops=Picture(app,image="PC.gif")
welcome_message=Text(app,text= "Press START", size=40, font="Times New Roman", color="green")
app.display()

   
