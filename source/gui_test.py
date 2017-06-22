import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
import get_calendar
import naver_search
import pytz
import datetime
import get_api
import time

class Application(tk.Frame):
    def __init__(self, master=None) :
        tk.Frame.__init__(self, master)
        self.pack()
        pad = 50
        self.screen_width = self.master.winfo_screenheight() - pad
        self.screen_height = int(self.screen_width * 16 / 9)
        self.master.geometry("{0}x{1}+0+0".format(
            self.screen_width, self.screen_height))
        self.master.configure(background='black')
        self.calendar_list = tk.Text(self.master, background="black", bd=0, foreground="white")
        self.naver_lank = tk.Text(self.master, background="black", bd=0, foreground="white")
        self.time_now_show = tk.Text(self.master, background="black", bd=0, foreground="white")
        self.weather_show = tk.Text(self.master, background="black", bd=0, foreground="white")
        #self.news_show = tk.Text(self.master)
        self.create_calendar()
        self.create_naver_lank()
        #self.create_news()
        self.create_time()
        self.create_weather()


    def create_calendar(self) :
        # calendar
        calendar_data = get_calendar.get_calendar_list()
        print(calendar_data)

        self.calendar_list.config(height=len(calendar_data), width=30)
        self.calendar_list.place(x=self.screen_width - 250, y=100)

        for text_calendar_list in calendar_data:
            text_calendar = text_calendar_list[0] + ' ' + text_calendar_list[1] + ' ' + text_calendar_list[2] + '\n'
            self.calendar_list.insert('1.0', text_calendar)


    def create_naver_lank(self) :
        # naver top search data

        naver_data = naver_search.get_naver_top_lank()
        len_highest = 0
        for len_naver_data in naver_data :
            if len(len_naver_data) * 2 > len_highest :
                len_highest = len(len_naver_data) * 2
        self.naver_lank.config(height=len(naver_data), width=len_highest + 3)
        self.naver_lank.place(x=50, y=200)
        lank_num = 0
        for naver_lank_list in naver_data:
            lank_num += 1
            self.naver_lank.insert(tk.END, str(lank_num) + ' ' + naver_lank_list + '\n')

        self.naver_lank_change()

    def naver_lank_change(self) :
        # change naver lank

        naver_data = naver_search.get_naver_top_lank()
        len_highest = 0
        for len_naver_data in naver_data:
            if len(len_naver_data) * 2 > len_highest:
                len_highest = len(len_naver_data) * 2

        self.naver_lank.config(height=len(naver_data), width=len_highest + 3)
        self.naver_lank.delete('1.0', tk.END)

        lank_num = 0
        for naver_lank_list in naver_data:
            lank_num += 1
            self.naver_lank.insert(tk.END, str(lank_num) + ' ' + naver_lank_list + '\n')

        self.master.after(15000, self.naver_lank_change)  # it'll call itself continuously

    def create_weather(self) :
        weather_data = get_api.get_weather_data()
        print(weather_data)
        pty2string = {0: "맑음",
                      1: "비",
                      2: "진눈개비",
                      3: "눈",
                      }
        print(pty2string[weather_data['PTY']])
        if weather_data['PTY'] > 0 :
            print("강수확률 : " + str(weather_data['POP']) + "%")

        '''
        self.weather_show.config(height=len(calendar_data), width=30)
        self.weather_show.place(x=self.screen_width - 250, y=100)

        for text_calendar_list in calendar_data:
            text_calendar = text_calendar_list[0] + ' ' + text_calendar_list[1] + ' ' + text_calendar_list[2] + '\n'
            self.calendar_list.insert('1.0', text_calendar)
        '''




    def create_time(self) :
        # time data
        time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H:%M:%S')  # 'Z' indicates UTC time
        print(time_now)

        self.time_now_show.config(height=1, width=8, font=("Times",30))
        self.time_now_show.place(x=50, y=80)
        self.time_now_show.insert('1.0', time_now)
        self.time_change()


    def time_change(self) :
        time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H:%M:%S')  # Korea time
        #print(time_now)

        self.time_now_show.insert('1.0', time_now)
        self.master.after(100, self.time_change)  # it'll call itself continuously


    def create_news(self) :
        # naver news
        news_all = naver_search.get_naver_news()

        len_highest = 0
        for len_news_data in news_all:
            if len(len_news_data) * 2 > len_highest:
                len_highest = len(len_news_data) * 2
        print(len_highest)
        self.news_show = tk.Text(self.master, height=30, width=len_highest,
                                 background="black", bd=0, foreground="white")
        self.news_show.place(x=self.screen_width - len_highest * 7, y=300)

        print(naver_search.get_naver_news())
        for news_title in news_all:
            self.news_show.insert(tk.END, news_title + '\n')



root = tk.Tk()
app = Application(master=root)
app.mainloop()


#now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat() # 'Z' indicates UTC time