import tkinter as tk
from datetime import timedelta

class Stopwatch:
    def init(self, root):
        self.root = root
        self.root.title("Секундомер")
        self.root.resizable(False, False)

        self.running = False
        self.seconds = 0

        self.time_label = tk.Label(
            root,
            text="00:00:00",
            font=("Helvetica", 48),
            bg="black",
            fg="green"
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
            self.root.after(1000, self.update_timer)  

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.seconds = 0
        self.time_label.config(text="00:00:00")


root = tk.Tk()
app = Stopwatch(root)
root.mainloop() 
