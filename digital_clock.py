import tkinter as tk
import time

def display_time():
    # current time in a specific format
    current_time = time.strftime('%I:%M:%S %p') 
    
    # clock updating with the current time
    clock_label.config(text=current_time)
    
    # updates after 1k milliseconds / 1 second
    clock_label.after(1000, display_time)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("700x200")

# using fonts and colors for the label
clock_label = tk.Label(window, font=("Verdana", 80), bg="black", fg="white")
clock_label.pack(pady=50)

# starts updating the time
display_time()

# main loop
window.mainloop()
