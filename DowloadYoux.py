from tkinter import filedialog ,messagebox, Menu
import tkinter
from pytube import YouTube
import os


#ventana de tkinter
window = tkinter.Tk()
#Menu
barmenu = tkinter.Menu()
#color y el menu en la ventana
window.config(bg="antique white",menu=barmenu)
#titulo 
window.title("DownloadYoux")
#icono
window.iconbitmap("C:/Users/isra/Desktop/desarrollo/descargarVideosyoutube/1.ico")
#tamaño de la ventana
window.geometry("1000x550")

#etiqueta
etiqueta = tkinter.Label(window,text="ingresa la url de youtube").pack()
#caja de texto
box_text = tkinter.Entry(window,width=31)
box_text.pack()

file = tkinter.Menu(barmenu)
#barmenu.add_cascade(menu=file,label="Archivo")

#accion
barmenu.add_command(label="Salir",
    accelerator="Ctrl+s",
    command=window.quit)

#barra de progreso 
barprogress = bar1 = tkinter.P


#funciones
def ejecutavideo():
        archivo = filedialog.askdirectory(mustexist=True)
        text = box_text.get()
        pasar = ""
        pasar = text
        try:
                yt = YouTube(pasar)
        
        except:
                messagebox.showerror(title="!!Error¡¡",message="Error al descargar verifique la ruta")

        mp4_files = yt.streams.filter(file_extension="mp4")
        mp4_369p_files = mp4_files.get_highest_resolution()
        try:
                messagebox.showinfo(title="!Descargado¡",message="la descarga es exitosa :D")
                mp4_369p_files.download(output_path=archivo)
        except:
                messagebox.showerror(title="!!Error¡¡",message="Error al descargar verifique la ruta")
        

     
    
def ejecutaAudio():
        archivo2 = filedialog.askdirectory(mustexist=True)
        text2 = box_text.get()
        pasar2 = ""
        pasar2 = text2
        #verificar la url
        try:
                yt = YouTube(pasar2)
        except:
                messagebox.showerror(title="!!Error¡¡",message="Error al descargar verifique la ruta")

        #que se se haya descargado correctamente
        
        try:
                mp3_files = yt.streams.filter(only_audio=True).first().download(output_path=archivo2)
                new_file = os.path.splitext(mp3_files)
                os.rename(mp3_files,new_file[0]+'.mp3')
                
               
                messagebox.showinfo(title="!Descargando¡",message="la descarga es exitosa :D")
        
        except:
                messagebox.showerror(title="!!Error¡¡",message="Error al descargar verifique la ruta")

        

#boton
actionvideo = tkinter.Button(window,text="Descargar Video",fg="black",bg="red",command= ejecutavideo)
actionvideo.pack()

actionAudio = tkinter.Button(window,text="Descargar Audio",fg="black",bg="red" , command= ejecutaAudio)
actionAudio.pack()

window.mainloop()
