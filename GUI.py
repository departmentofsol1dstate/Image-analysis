# -*- coding: utf-8 -*-
"""
Interface with Tkinter.
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import PIL.ImageTk, PIL.Image
import ctypes

import image_analysis

def draw_img_con(width_img, height_img, f_name, label_, image_):

    image_ = open_and_resize_image(f_name, width_img, height_img)
    label_.config(image=image_, bg='#CCCCCC', bd=2, relief='ridge')
    return image_, label_

def clicked():
    global image, image_1, image_2, label, label_1, label_2, contours, file_name

    scale_1.set(140)
    
    scale_2.set(50)

    file_name = askopenfilename()
    if(not file_name.endswith('.png')):
        return

    subframe.config(bd=2, relief='ridge')

    width_img = (subframe.winfo_width()-8) // 2
    height_img = subframe.winfo_height() - 8
    image, label = draw_img_con(width_img, height_img, file_name, label, image)
    
    image_analysis.Algorithm(file_name, scale_1.get(), scale_2.get())
    
    contours = [len(image_analysis.cnt), len(image_analysis.cnt_1)]

    LB.config(text=f'Количество всех контуров: {contours[0]}, количество контуров после обработки: {contours[1]}.')

    image_1, label_1  = draw_img_con(width_img, height_img, 'fixed_image.png', label_1, image_1)
    
    width_img = frame.winfo_width() - subframe_3.winfo_width() - 8
    height_img = frame.winfo_height() - 8
	
    nb.tab(frame_1, state=tk.NORMAL)
    
    image_2, label_2  = draw_img_con(width_img, height_img, 'fixed_image.png', label_2, image_2)
    
def clicked_2():

    global image, image_1, image_2, label, label_1, label_2, contours

    image_analysis.Algorithm(file_name, scale_1.get(), scale_2.get())
    
    width_img = (subframe.winfo_width()-8) // 2
    height_img = subframe.winfo_height() - 8
    
    image, label = draw_img_con(width_img, height_img, file_name, label, image)
    image_1, label_1  = draw_img_con(width_img, height_img, 'just_image.png', label_1, image_1)
    
    width_img = frame_1.winfo_width() - subframe_3.winfo_width() - 8
    height_img = frame_1.winfo_height() - 8
    
    image_2, label_2  = draw_img_con(width_img, height_img, 'fixed_image.png', label_2, image_2)

    contours = [len(image_analysis.cnt), len(image_analysis.cnt_1)]

    LB.config(text=f'Количество всех контуров: {contours[0]}, количество контуров после обработки: {contours[1]}.')
    
def resize_image(w, h, w_box, h_box, image):
    '''
    Функция масштабирует изображение на размеры: w_box, h_box.

    Parameters
    ----------
    w : int
        ширина изображения.
    h : int
        высота изображения.
    w_box : int
        ширина виджета.
    h_box : int
        высота виджета.
    image : Image
        изображение.

    Returns:
    -------
    new_image: PhotoImage
        масштабированное изображение.
    '''
    
    coefficient_1 = h_box/h
    coefficient_2 = w_box/w
    coefficient = min(coefficient_1, coefficient_2)
    new_w = int(coefficient*w)
    new_h = int(coefficient*h)
    new_image = image.resize((new_w, new_h))
    #print(new_w, new_h)
    return new_image

def open_and_resize_image(filename, width_img, height_img):
    '''
    Функция готовит изображения для вывода на экран
    
    Parameters
    ----------
    filename : str
        путь к файлу.
    width_img : int
        ширина виджета.
    height_img : int
        высота виджета.

    Returns
    -------
    resized_image_TK : imageTk.PhotoImage
        масштабированное изображение для Tkinter.
    '''
    
    with PIL.Image.open(filename) as image:
        w, h = image.size
        resized_image = resize_image(w, h, width_img, height_img, image)
    
        resized_image_TK = PIL.ImageTk.PhotoImage(resized_image)
        return resized_image_TK


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
w_scr = screensize[0]
h_scr = screensize[1]
file_name = None
image = None
image_1 = None
image_2 = None
contours = [0, 0]

window = tk.Tk()
window.title('Программа для поиска деффектов на изображении')
window.geometry(f'{w_scr}x{h_scr}+0+0')
window.state('zoomed')

nb = ttk.Notebook(master=window)
nb.pack(fill=tk.BOTH, expand=1)

frame = tk.Frame(master=nb, bg='#9999FF')
frame.place(x=0, y=0)
nb.add(frame, text='вкладка 1')

frame_1 = tk.Frame(master=nb, bd=2, relief='ridge', bg='#9999FF')
frame_1.place(x=0, y=0)
nb.add(frame_1, text='вкладка 2', state=tk.DISABLED)

LB = tk.Label(master=window, text=f'Количество всех контуров: {contours[0]}, количество контуров после обработки: {contours[1]}.',
              bd=2, bg='gray', relief='ridge')
LB.pack(side=tk.LEFT)

window.update()

button = tk.Button(master=frame, text='Выберите фотографию', bg='gray', bd=2,
                   relief='raised', height=3, command=clicked)
button.place(x=0, y=0, relheight=0.1, relwidth=0.15)

subframe = tk.Frame(master=frame, bg='#9999FF')
subframe.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

label = tk.Label(master=subframe, bg='#9999FF')
label.place(relx=0, rely=0)

label_1 = tk.Label(master=subframe, bg='#9999FF')
label_1.place(anchor=tk.NE, relx=1, rely=0)

label_2 = tk.Label(master=frame_1)
label_2.place(x=0, y=0)

subframe_3 = tk.Frame(master=frame_1, bd=2, relief='raised')
subframe_3.place(anchor=tk.NE, relheight=0.9, relwidth=0.15, relx=1, rely=0)

label_3 = tk.Label(subframe_3, text='Порог для бин.\nизображения',
                   bd=1, relief='ridge')
label_3.place(x=0, y=0, relwidth=0.5, relheight=0.1)

label_4 = tk.Label(subframe_3, text='Мин. длина\nконтура', bd=1, relief='ridge')
label_4.place(relx=0.5, y=0, relwidth=0.5, relheight=0.1)

scale_1 = tk.Scale(subframe_3, from_=0, to=255, orient=tk.VERTICAL,
                   bd=1, relief='raised')
scale_1.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)

scale_2 = tk.Scale(subframe_3, from_=0, to=210, orient=tk.VERTICAL, 
                   bd=1, relief='raised')
scale_2.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)

button_2 = tk.Button(master=frame_1, text='Анализ', bg='gray',
                     bd=2, relief='raised', command=clicked_2)
button_2.place(anchor=tk.SE, relx=1, rely=1, relheight=0.1, relwidth=0.15)

window.mainloop()