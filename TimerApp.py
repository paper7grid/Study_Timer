import customtkinter as ctk
import time
import threading
class TimerApp(ctk.CTk):
    def__init__(self):
        super().__init__()
    
        self.title("Timer App")
        self.geometry("600x350")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.time_label = ctk.CTkLabel(self, text="🌸 Pomodoro Timer", font=("Helvetica", 24, bold))
        self.time_label.pack(pady=20)
        self.time_left = 25 * 60  # 25 minutes in seconds
        self.timer_running = False
        self.timer_display = ctk.CTkLabel(self, text="25:00", font=("Helvetica", 50))
        self.timer_display.pack(pady=10)
    
    