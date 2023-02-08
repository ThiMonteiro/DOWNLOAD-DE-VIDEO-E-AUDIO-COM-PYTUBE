from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlretrieve
from pytube import YouTube
import webbrowser


# LINK DE EXEMPLO:
"https://www.youtube.com/watch?v=e0T0rI-GiR4&list=RDQMZRXVElXTYsg&start_radio=1"

# FUNÇÕES #################################################


def abrir_youtube():
    webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")


def download_audio_mp4():
    """FUNÇÃO QUE BAIXA AS MÚSICAS EM FORMATO MP4"""
    yt = YouTube(str(barra_de_pesquisa.get()).strip())
    audio_download = yt.streams.get_highest_resolution()
    audio_download.download(filename=yt.title+".mp4")


def download_audio_mp3():
    """FUNÇÃO QUE BAIXA AS MÚSICAS EM FORMATO MP3"""
    yt = YouTube(str(barra_de_pesquisa.get()).strip())
    audio_download = yt.streams.filter(only_audio=True).first()
    out_file = audio_download.download(filename=yt.title+".mp3")


def buscar():
    yt = YouTube(str(barra_de_pesquisa.get()).strip())
    urlretrieve(yt.thumbnail_url, "capa.jpg")
    # TITULO #########################################
    lb_titulo_musica = Label(
        window,
        text=yt.title,
        bg="#D93109",
        fg="#FFFFFF",
        font=("Times", "12", "bold"))

    lb_titulo_musica.place(relx=0.05, rely=0.34)
    ##################################################

    # BOTÕES DOWNLOAD ################################

    botao_mp4 = Button(
        window,
        text="Download MP4",
        bd=1, bg="#FFFFFF",
        fg="#000000",
        font=("Times", "11", "bold italic"),
        command=download_audio_mp4)

    botao_mp4.place(relx=0.45, rely=0.48)

    botao_mp3 = Button(
        window,
        text="Download MP3",
        bd=1, bg="#FFFFFF",
        fg="#000000",
        font=("Times", "11", "bold italic"),
        command=download_audio_mp3)

    botao_mp3.place(relx=0.45, rely=0.55)

    ##################################################

    # IMAGEM #########################################
    imagem = Image.open("capa.jpg")

    resize_imagem = imagem.resize((300, 200))
    tkinter_imagem = ImageTk.PhotoImage(resize_imagem)

    lb_imagem = Label(window, image=tkinter_imagem)

    # NÃO É CORRETO COMBINAR AS FUNÇÕES PACK(), PLACE() E GRID(). USEM APENAS UMA!!
    # MAS, A ÚNICA FORMA QUE ENCONTREI FOI ESSA. POR ENQUANTO NÃO ENCONTREI NENHUMA RESPOSTA SOBRE ISSO.
    lb_imagem.place(relx=0.05, rely=0.40).pack()

    ##################################################


##########################################################


# CONFIGURAÇÕES TKINTER ###################################
window = Tk()

window.title("Pytube Download")

window.geometry("800x700")

window.configure(background="#D93109")

window.resizable(width=False, height=False)

###########################################################

# BOTÃO DO YOUTUBE ########################################

frame_botao_youtube = Frame(
    window,
    background="#D93109",
    bd=1)

frame_botao_youtube.place(
    relx=0.34,
    rely=0.04,
    relwidth=0.30,
    relheight=0.08)


botao_youtube = Button(
    frame_botao_youtube,
    text="YouTube",
    bd=1,
    bg="#FFFFFF",
    fg="#000000",
    font=("Times", "11", "bold italic"),
    command=abrir_youtube)


botao_youtube.place(
    relx=0.07,
    rely=0.10,
    relwidth=0.85,
    relheight=0.80)

###########################################################

# BOTÃO BUSCAR ############################################

botao_buscar = Button(
    window,
    text="Buscar",
    bd=1, bg="#FFFFFF",
    fg="#000000",
    font=("Times", "11", "bold italic"),
    command=buscar)

botao_buscar.place(
    relx=0.05,
    rely=0.25,
    relwidth=0.20,
    relheight=0.05)

###########################################################

# BARRA DE PESQUISA ########################################


lb_msg = Label(
    window,
    text="Por favor, cole o link do YouTube aqui",
    bg="#D93109",
    fg="#FFFFFF",
    font=("Times", "13", "bold italic"))

lb_msg.place(
    relx=0.05,
    rely=0.15)


barra_de_pesquisa = Entry(
    window,
    background="#FFFFFF",
    bd=1,
    fg="#000000",
    font=("Times", "10", "bold italic"))

barra_de_pesquisa.place(
    relx=0.05,
    rely=0.19,
    relwidth=0.80,
    relheight=0.04)

###########################################################


window.mainloop()
