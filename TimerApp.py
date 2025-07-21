import customtkinter as ctk
import time
import threading
from PIL import Image
class TimerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Timer App")
        self.geometry("600x350")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        bg_image_path = "background_Tim.jpg" 
        image = Image.open(bg_image_path)
        self.bg_image = ctk.CTkImage(image, size=(600, 350))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relwidth=1, relheight=1)
        self.time_label = ctk.CTkLabel(self, text="🌸 Pomodoro Timer", font=("Helvetica", 24,))
        self.time_label.pack(pady=20)
        self.time_left = 25 * 60  # 25 minutes in seconds
        self.timer_running = False
        self.timer_display = ctk.CTkLabel(self, text="25:00", font=("Helvetica", 50))
        self.timer_display.pack(pady=10)
        self.start_button = ctk.CTkButton(self, text="start", command=self.start_timer)
        self.start_button.pack(pady=5)
        self.reset_button= ctk.CTkButton(self, text="reset", command=self.resent_button)
        self.reset_button.pack(pady=5)
        self.qoute_label = ctk.CTkLabel(
            self,
              text="Stay focused and keep going!", 
              font=("Helvetica", 14), 
              wraplength=500,
              justify="center"
        )
        self.qoute_label.pack(pady=20)
        self.break_button = ctk.CTkButton(self, text="Take a Break", command=self.start_break)
        self.break_button.pack(pady=5)
        self.sessions_completed = 0
        self.session_count_label = ctk.CTkLabel(self, text="Sessions Completed: 0", font=("Helvetica", 14))
        self.session_count_label.pack(pady=5)


       



    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            threading.Thread(target=self.countdown).start()
    def countdown(self):
        while self.time_left > 0 and self.timer_running:
            mins, secs = divmod(self.time_left, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            self.timer_display.configure(text=time_str)
            time.sleep(1)
            self.time_left -= 1
        if self.time_left == 0:
            if hasattr(self, 'is_break') and self.is_break:
                self.timer_display.configure(text="Break Over! Let's get back to work!")
                self.is_break = False
            else: 
                self.timer_display.configure(text="Done!")

    def resent_button(self):
        self.timer_running = False
        self.time_left = 25 * 60
        self.timer_display.configure(text="25:00")
    def start_break(self):
        if not self.timer_running:
            self.time_left = 10 * 60
            self.timer_running = True
            self.is_break = True
            self.timer_display.configure(text="10:00")
            threading.Thread(target=self.countdown).start()
    

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()
# This code creates a simple Pomodoro timer application using customtkinter.
# It includes a timer that counts down from 25 minutes, a reset button, and a break feature.
# The timer displays the remaining time in a "MM:SS" format and updates every second.