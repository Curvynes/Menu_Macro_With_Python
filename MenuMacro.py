import pydirectinput
import keyboard
import tkinter as tk

target_pos = None

def set_point(e=None):
    global target_pos
    target_pos = pydirectinput.position()
    status_label.config(text=f"Point set at {target_pos}")

def click_target(e=None):
    if target_pos is None:
        status_label.config(text="No point set! Press O first.")
    else:
        pydirectinput.moveTo(target_pos[0], target_pos[1], duration=0)
        pydirectinput.click(button='left')
        pydirectinput.click(button='left')
        status_label.config(text=f"Double-clicked at {target_pos}")

def start_macro():
    keyboard.on_press_key('o', set_point)
    keyboard.on_press_key('t', click_target)
    status_label.config(text="Macro running... Press O to set point, T to double-click, ESC to quit.")

window = tk.Tk()
window.title("Menu macro - made by curvynes")
window.geometry("500x300")
window.attributes("-topmost", True)

label = tk.Label(window, text="Curvynes's menu macro\n\nControls:\nO - Set point\nT - Move & double-click at point\nESC - Quit", font=("Arial", 12), justify="center")
label.pack(pady=20)

start_button = tk.Button(window, text="Start Macro", command=start_macro, font=("Arial", 12))
start_button.pack(pady=20)

status_label = tk.Label(window, text="Status: Waiting to start...", font=("Arial", 10))
status_label.pack(pady=10)

window.mainloop()
