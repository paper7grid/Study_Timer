import customtkinter as ctk
import time
import threading
class TimerApp(ctk.CTk):
    def __init__(self):
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
            self.timer_display.configure(text="Done!")
            self.timer_running = False
    def resent_button(self):
        self.timer_running = False
        self.time_left = 25 * 60
        self.timer_display.configure(text="25:00")

if __name__ == "__main__":
    app = TimerApp
    app.mainloop()

            