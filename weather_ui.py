from tkinter import *
import tkinter as tk
from weather_brain import Weather
from tkinter import ttk, messagebox


THEME_COLOR = '#A2678A'


class Weatherapp:

    def __init__(self, current: Weather):
        self.current = current
        self.window = Tk()
        self.window.title("Weather App")
        self.window.geometry("900x500")
        self.window.config(bg=THEME_COLOR)
        self.window.resizable(False, False)

        #background_image
        bg_image = PhotoImage(file="image/spaced.png")
        self.my_canvas = Canvas(self.window, width=900, height=500)
        self.my_canvas.pack(fill="both", expand=True)

        global canvas_bg
        global logo
        canvas_bg = self.my_canvas.create_image(0,0, image=bg_image, anchor="nw")

        #search
        self.textfield = tk.Entry(self.window, justify="center", width=40, font=("poppins", 10, "bold"))
        self.textfield.place(x=450, y=40)
        self.textfield.focus()

        #Search_button
        self.my_imageicon = Button(text="Search",borderwidth=0,width=10, cursor="hand2", command=self.getWeather)
        self.my_imageicon.place(x=740, y=39)

        #logo
        Logo_image = PhotoImage(file="image/logo.png")
        logo = self.my_canvas.create_image(50, 30, image=Logo_image, anchor="nw")

        self.my_canvas.create_text(430, 350, text="Wind", font=("Arial", 14), fill="white", anchor='sw')
        self.w_text = self.my_canvas.create_text(600, 350, text="...", font=("Arial", 14), fill="white", anchor='sw')

        self.my_canvas.create_text(430, 250, text="Humidity", font=("Arial", 14), fill="white", anchor='sw')
        self.h_text = self.my_canvas.create_text(600, 250, text="...", font=("Arial", 14), fill="white", anchor='sw')

        self.my_canvas.create_text(430, 200, text="Description", font=("Arial", 14), fill="white", anchor='sw')
        self.d_text = self.my_canvas.create_text(600, 200, text="...", font=("Arial", 14), fill="white", anchor='sw')

        self.my_canvas.create_text(430, 300, text="Pressure", font=("Arial", 14), fill="white", anchor='sw')
        self.p_text = self.my_canvas.create_text(600, 300, text="...", font=("Arial", 14), fill="white", anchor='sw')


        self.my_canvas.create_text(430, 300, text=" ", font=("Arial", 14), fill="white", anchor='sw')
        self.temp_text = self.my_canvas.create_text(100, 420, text="...", font=("Arial", 14), fill="white", anchor='sw')

        self.my_canvas.create_text(430, 420, text=" ", font=("Arial", 14), fill="white", anchor='sw')
        self.cond_text = self.my_canvas.create_text(430, 420, text=" ", font=("Arial", 14), fill="white", anchor='sw')


        self.window.mainloop()

    def getWeather(self):
        city = self.textfield.get()
        result = self.current.get_weather(city)
        #self.current.sample_func()

        if not result:
            messagebox.showerror("Weather App", "Invalid entry")
        else:

            self.my_canvas.itemconfig(self.temp_text, text=f"Temperature is {result[1]}°")

            self.my_canvas.itemconfig(self.cond_text, text=f"Feels like  {result[0]}")

            self.my_canvas.itemconfig(self.w_text, text=result[4])

            self.my_canvas.itemconfig(self.h_text, text=result[3])

            self.my_canvas.itemconfig(self.p_text, text=result[2])

            self.my_canvas.itemconfig(self.d_text, text=result[5])

            if result[6] == 721:
                bg_haze = tk.PhotoImage(file="image/bg_haze.png")
                self.my_canvas.itemconfig(canvas_bg, image=bg_haze)
                self.my_canvas.bg_haze = bg_haze
                himag = PhotoImage(file="image/haze.png")
                self.my_canvas.itemconfig(logo, image=himag)
                self.my_canvas.timag = himag

            elif result[6] <= 232:
                bg_tstorm = tk.PhotoImage(file="image/bg_tstorm.png")
                self.my_canvas.itemconfig(canvas_bg, image=bg_tstorm)
                self.my_canvas.bg_tstorm = bg_tstorm
                timag = PhotoImage(file="image/tstorm.png")
                self.my_canvas.itemconfig(logo, image=timag)
                self.my_canvas.timag = timag

            elif result[6] <= 321:

                bg_drizzle = tk.PhotoImage(file="image/bg_drizzle.png")
                self.my_canvas.itemconfig(canvas_bg, image=bg_drizzle)
                self.my_canvas.bg_drizzle = bg_drizzle

            elif result[6] <= 531:
                bg_rain = tk.PhotoImage(file="image/bg_rain.png")
                self.my_canvas.itemconfig(canvas_bg, image=bg_rain)
                self.my_canvas.bg_rain = bg_rain
                rimag = PhotoImage(file="image/rain.png")
                self.my_canvas.itemconfig(logo, image=rimag)
                self.my_canvas.rimag = rimag

            elif result[6] <= 804:
                bg_cloudy = tk.PhotoImage(file="image/bg_cloudy.png")
                self.my_canvas.itemconfig(canvas_bg, image=bg_cloudy)
                self.my_canvas.bg_cloudy = bg_cloudy
                cimag = PhotoImage(file="image/cloudy.png")
                self.my_canvas.itemconfig(logo, image=cimag)
                self.my_canvas.cimag = cimag

            else:
                print("clear sky")









