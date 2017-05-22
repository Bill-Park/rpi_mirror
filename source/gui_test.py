import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
import get_calendar
import naver_search
import pytz
import datetime

class Application(tk.Frame):
    def __init__(self, master=None) :
        tk.Frame.__init__(self, master)
        self.pack()
        pad = 3
        self.master.geometry("{0}x{1}+0+0".format(
            self.master.winfo_screenwidth() - pad, self.master.winfo_screenheight() - pad))
        self.master.configure(background='black')
        self.createWidgets()

    def createWidgets(self) :
        calendar_data = get_calendar.get_calendar_list()
        print(calendar_data)
        self.calendar_list = tk.Text(self.master, height=len(calendar_data), width=30)
        self.calendar_list.place(x=5, y=50)

        for text_calendar_list in calendar_data :
            text_calendar = text_calendar_list[0] + ' ' + text_calendar_list[1] + ' ' + text_calendar_list[2] + '\n'
            self.calendar_list.insert(tk.END ,text_calendar)

        naver_data = naver_search.get_naver_top_lank()

        self.naver = tk.Text(self.master, height=len(naver_data), width=20)
        self.naver.place(x=5, y=200)
        lank_num = 0
        for naver_lank_list in naver_data :
            lank_num += 1
            self.naver.insert(tk.END, str(lank_num) + ' ' + naver_lank_list + '\n')

        # print(naver_data)

        time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat()  # 'Z' indicates UTC time
        time_short = str(time_now[:10]) + ' ' + str(time_now[11:16])
        #event_info = [start[:10], start[11:16], event_part['summary']]
        self.time_now_show = tk.Text(self.master, height=5, width=17)
        self.time_now_show.place(x=self.master.winfo_screenwidth() - 300, y=50)
        self.time_now_show.insert(tk.END, time_short)



        '''
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        #self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        #self.QUIT.pack(side="bottom")
        '''

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()


#now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat() # 'Z' indicates UTC time