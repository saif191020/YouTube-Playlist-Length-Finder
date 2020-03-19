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
            playlist_name =soup.find(class_='pl-header-title').get_text().strip()
            timestamps =['00:'+video.find(class_='timestamp').get_text() for video in videos]
            timeinsec =[int(t.split(':')[-3])*3600+int(t.split(':')[-2])*60+int(t.split(':')[-1])   for t in timestamps]
            total_Time =str(datetime.timedelta(seconds=sum(timeinsec)))

            if total_Time == '0:00:00':
                tkinter.messagebox.showwarning('Not Found',"URL is not valid or URL dosent contain playlist")
            else:
                result['text']='Total Length  : '+total_Time
                plname['text']='Playlist Name :'+playlist_name
        except:
            tkinter.messagebox.showwarning('Not Found',"URL is not valid or URL dosent contain playlist")
        

root =Tk()
root.title('Playlist Length Finder')
root.iconbitmap(r'Images/ytlogo.ico')
contentFrame =Frame(root)

result =Label(root,text='Total Length  : --:--:--')
plname =Label(root,text='Playlist Name : ')
link   =Entry(contentFrame,width=50)
gbtn   =Button(contentFrame,text="Go!",command=findlen)

contentFrame.pack(pady=20,padx=30)
link.pack(side=LEFT)
gbtn.pack(side=LEFT)
result.pack()
plname.pack()

root.geometry('400x200+500+300')
root.mainloop()