from online_bot import start
import account
import multiprocessing
import tkinter as tk

window = tk.Tk()
window.title('BestBuy Bot')
window.geometry('400x300')
back_image = tk.PhotoImage(file='3080.png')


def button_click():
    core2 = multiprocessing.Process(target=start)
    core2.start()
    window.destroy()


def gui_main():

    # Canvas settings
    my_canvas = tk.Canvas(window, width='400', height='300')
    my_canvas.pack(fill='both', expand=True)
    my_canvas.create_image(100, 100, image=back_image, anchor='nw')
    my_canvas.create_text(200, 80, text='Thanks for using this bot!', font=('Pursia', 25), fill='black')
    my_canvas.create_text(200, 120, text='First time using bot?', font=('Pursia', 12), fill='black')

    # Buttons
    check_files_btn = tk.Button(
        window,
        text='Create Files',
        bg='orange',
        command=lambda: account.check_files_2()
    )

    my_canvas.create_window(
        200, 150,
        window=check_files_btn
    )

    # Run Bot
    run_bot_btn = tk.Button(window, text='Run Bot', bg='green', command=lambda: button_click())
    my_canvas.create_window(200, 220, window=run_bot_btn)

    # Exit
    exit_btn = tk.Button(window, text='Exit', bg='red', command=lambda: window.destroy())
    my_canvas.create_window(200, 260, width=30, height=30, window=exit_btn)

    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    print('Running Main')
    core1 = multiprocessing.Process(target=gui_main)
    core1.start()
