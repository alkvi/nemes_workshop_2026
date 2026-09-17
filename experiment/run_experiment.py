import csv
import time
import tkinter as tk

from pylsl import StreamInfo, StreamOutlet

START_STOP_MARKER = 15

info = StreamInfo("Trigger", "Markers", 1, 0, "int32", "exp")
outlet = StreamOutlet(info)

DISPLAY_TEXT = {
    "left": "TAP LEFT",
    "right": "TAP RIGHT",
    "control": "CONTROL",
    "rest": "+",
}

root = tk.Tk()
# root.attributes("-fullscreen", True)
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
cx, cy = w // 2, h // 2

intro_text = canvas.create_text(
    cx,
    cy,
    fill="white",
    font=("Helvetica", 28),
    text="Tap your finger when instructed.\n\nFixate on the cross during rest.\n\nPress SPACE to start.",
)

root.update()

start_flag = {"go": False}


def start_experiment(event):
    if event.keysym == "space":
        start_flag["go"] = True


root.bind("<Key>", start_experiment)

while not start_flag["go"]:
    root.update()
    time.sleep(0.01)

canvas.delete(intro_text)

cond_text = canvas.create_text(cx, cy, fill="white", font=("Helvetica", 48), text="")
timer_text = canvas.create_text(
    cx, cy + 80, fill="white", font=("Helvetica", 24), text=""
)

root.update()

with open("experiment_design.csv") as f:
    trials = list(csv.DictReader(f))


def update_display(cond, t, duration):
    canvas.itemconfigure(cond_text, text=DISPLAY_TEXT[cond])
    canvas.itemconfigure(timer_text, text=f"{t:0.1f} / {duration:0.1f}s")
    root.update()


print("Starting experiment...")
outlet.push_sample([START_STOP_MARKER])

for trial in trials:
    cond = trial["condition"]
    duration = float(trial["duration"])
    marker = int(trial["marker"])

    outlet.push_sample([marker])

    block_start = time.time()
    while time.time() - block_start < duration:
        t = time.time() - block_start
        update_display(cond, t, duration)
        time.sleep(0.01)

outlet.push_sample([START_STOP_MARKER])

canvas.delete("all")
canvas.create_text(
    cx, cy, fill="white", font=("Helvetica", 28), text="Done.\n\nPress ESC to exit."
)
root.update()


def quit_exp(event):
    if event.keysym == "Escape":
        root.destroy()


root.bind("<Key>", quit_exp)

while True:
    root.update()
    time.sleep(0.01)
