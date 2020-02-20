import requests
from bs4 import BeautifulSoup
import datetime
from tkinter import *
import tkinter.messagebox

def findlen():
    if link.get().strip() != "":
        ln=link.get().strip()
        try:
            page =requests.get(ln)

            soup =BeautifulSoup(page.content,'html.parser')

            videos =soup.find_all(class_='more-menu-wrapper')

            timestamps =['00:'+video.find(class_='timestamp').get_text() for video in videos]
            print(timestamps)
            timeinsec =[int(t.split(':')[-3])*3600+int(t.split(':')[-2])*60+int(t.split(':')[-1])   for t in timestamps]
            print(len(timeinsec))
            print(sum(timeinsec))
            total_Time =str(datetime.timedelta(seconds=sum(timeinsec)))

            if total_Time == '0:00:00':
                tkinter.messagebox.showwarning('Not Found',"URL is not valid or URL dosent contain playlist")
            else:
                result['text']='Total Length : '+total_Time
        except:
            tkinter.messagebox.showwarning('Not Found',"URL is not valid or URL dosent contain playlist")
        

root =Tk()
root.title('Playlist Length Finder')

contentFrame =Frame(root)

result =Label(root,text='Total Length : --:--:--')
link   =Entry(contentFrame)
gbtn   =Button(contentFrame,text="Go",command=findlen)

contentFrame.pack(pady=20,padx=30)
link.pack(side=LEFT)
gbtn.pack(side=LEFT)
result.pack()

root.geometry('290x200+500+300')
root.mainloop()