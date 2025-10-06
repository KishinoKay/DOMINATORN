import flet as ft
import pygame
import threading
from Script.system_script import coefficient
from Script.custom_color import custom_color_scheme

# 音声再生を非同期で管理するためにpygameを使う
pygame.mixer.init()
is_playing = False

# 音声を再生する関数
def play_sound1():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/under100.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True
def play_sound2():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/under100.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True
def play_sound3():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/over100.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True
def play_sound4():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/over300.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True

# 音声を停止する関数
def stop_sound(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    page.go("/main_page")


def Execution_view(page):
    page.theme_mode = ft.ThemeMode.DARK  # ダークモード
    page.theme = ft.Theme(color_scheme=custom_color_scheme)

    sum = float(coefficient.value)
    text = ft.Text("",
        size=42,  # 文字サイズを明示的に指定
        weight=ft.FontWeight.BOLD
        )
    
    if(sum<= 0):
        text.color ="#E0E0E0"
        coefficient.color = "#E0E0E0"
        # 音声を非同期で再生
        threading.Thread(target=play_sound1).start()
        text.value = "執行モード解除"
        coefficient.value = "同担係数: 0"
        logout_controls = ft.Container(
            content=ft.ElevatedButton("トリガーをロックします", on_click=lambda _: stop_sound(page))
        )
    elif(sum <100):
        text.color ="#E0E0E0"
        coefficient.color = "#E0E0E0"
        threading.Thread(target=play_sound2).start()
        text.value = "執行モード解除"
        coefficient.value = f"同担係数: {coefficient.value}"
        logout_controls = ft.Container(
            content=ft.ElevatedButton("トリガーをロックします", on_click=lambda _: stop_sound(page))
        )
    elif(sum<300):
        text.color ="#E0E0E0"
        coefficient.color = "#E0E0E0"
        threading.Thread(target=play_sound3).start()
        text.value = "執行モード パラライザー"
        coefficient.value = f"同担係数: {coefficient.value}"
        logout_controls = ft.Container(
            content=ft.ElevatedButton("速やかにトリガーを引いてください", on_click=lambda _: stop_sound(page))
        )
    else:
        text.color ="#FF0033"
        coefficient.color = "#FF0033"
        threading.Thread(target=play_sound4).start()
        text.value = "執行モード エリミネーター"
        coefficient.value = f"同担係数: {coefficient.value}"
        logout_controls = ft.Container(
            content=ft.ElevatedButton("速やかにトリガーを引いてください", on_click=lambda _: stop_sound(page))
        )

    input_content = ft.Column(
            controls=[text, coefficient, logout_controls],
            scroll=ft.ScrollMode.ALWAYS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    input_controls = ft.Container(
        content = input_content,
        alignment=ft.Alignment(0,0),  # 全体の中央揃え
        expand=True,  # ページ全体に広げる
        image_src="./assets/main_page.jpg",
        image_fit=ft.ImageFit.COVER
    )
    

    return ft.View(
        "/graph_page",
        controls=[
            input_controls
        ]
    )