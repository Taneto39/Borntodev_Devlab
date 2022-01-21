import tkinter as tk

main_window = tk.Tk()

main_window.option_add("*font", "20")
main_window.title("plotGraph")
tk.Label(main_window, text="plot", ).grid()
main_window.mainloop()