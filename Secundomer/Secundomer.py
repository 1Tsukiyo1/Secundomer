import tkinter as tk
from tkinter import messagebox
from datetime import timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Секундомер с анимацией")
        self.root.resizable(False, False)

        self.running = False
        self.seconds = 0
        self.timer_interval = 1000  
        self.animation_speed = 2  
        self.max_animation_speed = 10  
        self.last_jump = 0 
        self.last_speed_change = 0  
        self.last_notification = 0 

        self.canvas = tk.Canvas(root, width=400, height=200, bg="lightblue")
        self.canvas.pack(pady=10)

        self.runner = self.canvas.create_oval(50, 150, 70, 170, fill="blue")  
        self.body = self.canvas.create_line(60, 170, 60, 200, width=3)  
        self.leg1 = self.canvas.create_line(60, 200, 50, 220, width=3, fill="red")  
        self.leg2 = self.canvas.create_line(60, 200, 70, 220, width=3, fill="green")  
        self.arm1 = self.canvas.create_line(60, 180, 50, 190, width=3, fill="orange")  
        self.arm2 = self.canvas.create_line(60, 180, 70, 190, width=3, fill="purple")  

        self.time_label = tk.Label(
            root,
            text="00:00:00",
            font=("Helvetica", 48),
            bg="white",
            fg="black"
        )
        self.time_label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(
            button_frame,
            text="Старт",
            font=("Helvetica", 14),
            command=self.start
        )
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(
            button_frame,
            text="Стоп",
            font=("Helvetica", 14),
            command=self.stop
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(
            button_frame,
            text="Сброс",
            font=("Helvetica", 14),
            command=self.reset
        )
        self.reset_button.grid(row=0, column=2, padx=10)

    def update_timer(self):
        if self.running:
            self.seconds += 1
            time_string = str(timedelta(seconds=self.seconds))
            self.time_label.config(text=time_string)

            if self.seconds % 10 == 0 and self.seconds != self.last_jump:
                self.jump()
                self.last_jump = self.seconds

            if self.seconds % 60 == 0 and self.seconds != self.last_speed_change:
                self.increase_animation_speed()
                self.last_speed_change = self.seconds

            if self.seconds % 300 == 0 and self.seconds != self.last_notification:
                self.root.after(0, self.send_notification, f"Прошло {self.seconds // 60} минут!")
                self.last_notification = self.seconds

            self.animate_runner()

            self.root.after(self.timer_interval, self.update_timer)

    def animate_runner(self):
        x1, y1, x2, y2 = self.canvas.coords(self.runner)
        new_x = x1 + self.animation_speed
        if new_x > 350:
            new_x = 50
        self.canvas.move(self.runner, new_x - x1, 0)
        self.canvas.move(self.body, new_x - x1, 0)
        self.canvas.move(self.leg1, new_x - x1, 0)
        self.canvas.move(self.leg2, new_x - x1, 0)
        self.canvas.move(self.arm1, new_x - x1, 0)
        self.canvas.move(self.arm2, new_x - x1, 0)

    def jump(self):
        self.canvas.move(self.runner, 0, -20)
        self.canvas.move(self.body, 0, -20)
        self.canvas.move(self.leg1, 0, -20)
        self.canvas.move(self.leg2, 0, -20)
        self.canvas.move(self.arm1, 0, -20)
        self.canvas.move(self.arm2, 0, -20)
        self.root.after(200, self.land)

    def land(self):
        self.canvas.move(self.runner, 0, 20)
        self.canvas.move(self.body, 0, 20)
        self.canvas.move(self.leg1, 0, 20)
        self.canvas.move(self.leg2, 0, 20)
        self.canvas.move(self.arm1, 0, 20)
        self.canvas.move(self.arm2, 0, 20)

    def increase_animation_speed(self):
        """Увеличивает скорость анимации (расстояние за шаг), но не затрагивает таймер"""
        if self.animation_speed < self.max_animation_speed:
            self.animation_speed += 1

    def send_notification(self, message):
        """Показывает уведомление через tkinter.messagebox без остановки таймера"""
        messagebox.showinfo("Секундомер", message)

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 0
        self.interval = 1000  
        self.time_label.config(text="00:00:00")
        self.canvas.coords(self.runner, 50, 150, 70, 170)
        self.canvas.coords(self.body, 60, 170, 60, 200)
        self.canvas.coords(self.leg1, 60, 200, 50, 220)
        self.canvas.coords(self.leg2, 60, 200, 70, 220)
        self.canvas.coords(self.arm1, 60, 180, 50, 190)
        self.canvas.coords(self.arm2, 60, 180, 70, 190)

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()

