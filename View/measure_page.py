import flet as ft
import pygame
import threading
from Script.measure_button import selections
from Script.system_script import main_script
from Script.custom_color import custom_color_scheme

# 音声再生を非同期で管理するためにpygameを使う
pygame.mixer.init()
is_playing = False

# 音声を再生する関数
def play_sound():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/kaisekityu.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True

# 音声を停止する関数
def stop_sound(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    page.go("/main_page")

def Error_on_click(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    if not is_playing:
        pygame.mixer.music.load('./Audio/error.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True
    # page.snack_bar.content.value = f"Hello, world: {d.counter}"
    page.snack_bar = ft.SnackBar(ft.Text("Error: 未回答の項目があります", color=ft.colors.RED))
    page.snack_bar.open = True
    page.update()


def measure_view(page):
    page.theme_mode = ft.ThemeMode.DARK  # ダークモード
    page.theme = ft.Theme(color_scheme=custom_color_scheme)

    # 音声を非同期で再生
    threading.Thread(target=play_sound).start()

    def page_go():
        if any(selection.value is None for selection in selections):
            Error_on_click(page)
        else:
            main_script()
            global is_playing
            if is_playing:
                pygame.mixer.music.stop()
                is_playing = False
            page.go("/Execution_page")

    #ページレイアウト調節
    def page_resized(e):
        input_content.height=page.window_height-100
        page.update()
    page.on_resized = page_resized

    logout_controls = ft.Container(
        content=ft.ElevatedButton("計測を確定する", on_click=lambda _: page_go())
    )

    date_append = ft.Container(
        content=ft.ElevatedButton("計測を中断する", on_click=lambda _: stop_sound(page)),
        alignment=ft.alignment.top_right,  # 右揃え
    )

    input_content = ft.Column(
            controls=[*selections,logout_controls],
            height=page.window_height-100,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    input_controls = ft.Container(
        content = input_content,
        image_src="./assets/main_page.jpg",
        image_fit=ft.ImageFit.COVER
    )
    

    return ft.View(
        "/graph_page",
        controls=[
            date_append,
            input_controls
        ]
    )