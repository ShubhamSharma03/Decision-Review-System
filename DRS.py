import tkinter
import cv2
import PIL.Image , PIL.ImageTk
from functools import partial
import threading
import imutils
import time
stream=cv2.VideoCapture("clip1.mp4")
flag=True
def play(speed):
    global flag
    print(f"You Clicked on Play. Your Speed is {speed}")

    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="red", font="Times 26 bold", text="Decision Pending")
    flag = not flag



def pending(decision):

    # 1.Display Decision Pending Image
    frame=cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # 2. Wait 2 secs
    time.sleep(2)

    # 3. Display Sponsor
    frame = cv2.cvtColor(cv2.imread("sponsors.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 2 secs
    time.sleep(2)

    #  5. Display Out/NotOut Image
    if decision=='Out':
        decisionImg='out.jpg'
    else:
        decisionImg='notout.jpg'


    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thread=threading.Thread(target=pending,args=("Out",))
    thread.daemon=1
    thread.start()
    print("The Player is Out")
def notout():
    thread = threading.Thread(target=pending, args=("Not Out",))
    thread.daemon = 1
    thread.start()
    print("The Player is NotOut")


#Width And Height of Our Main Screen
SET_WIDTH=650
SET_HEIGHT=368

#Tkinter Starts Here
window=tkinter.Tk()
window.title("Third Umpire Decison Review Kit")
cv_img=cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

#Buttons to ControlBack

btn=tkinter.Button(window,text="<<Previous (Fast)",width=50,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<<Previous (Slow)",width=50,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next (Fast)>>",width=50,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="Next (Slow)>>",width=50,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()

btn=tkinter.Button(window,text="Give Not Out",width=50,command=notout)
btn.pack()

window.mainloop()
