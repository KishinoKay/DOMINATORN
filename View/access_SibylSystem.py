import flet as ft
import pygame
import threading
from Script.data_input import selections, date_in, date_list, list_append
from Script.custom_color import custom_color_scheme

# 音声再生を非同期で管理するためにpygameを使う
pygame.mixer.init()
is_playing = False

# 音声を再生する関数
def play_sound():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/sibyl_system.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True

# 音声を停止する関数
def stop_sound(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    page.go("/main_page")



def SibylSystem(page):
    page.theme_mode = ft.ThemeMode.DARK  # ダークモード
    page.theme = ft.Theme(color_scheme=custom_color_scheme)

    # 音声再生を非同期で開始
    threading.Thread(target=play_sound).start()

    #ページレイアウト調節
    def page_resized(e):
        date_list.height=page.window_height-100
        input_content.height=page.window_height-100
        page.update()
    page.on_resized = page_resized

    logout_controls = ft.Container(
        content=ft.ElevatedButton("データベースからログアウト", on_click=lambda _: stop_sound(page)),
        alignment=ft.alignment.top_right,  # 右揃え
    )

    date_append = ft.ElevatedButton("追加要素を確定",on_click=lambda _: date_in(page))

    input_content = ft.Column(
            controls=[*selections,date_append],
            width=300,
            height=page.window_height-100,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True
        )
    
    input_controls = ft.Container(
        content = input_content
    )
    

    list_append(page)
    
    date_list.height=page.window_height-100

    SibylList_controls = ft.Container(
        content = date_list,
        expand=True,
        image_src="./assets/main_page.jpg",
        image_fit=ft.ImageFit.COVER
    )

    return ft.View(
        "/graph_page",
        controls=[
            logout_controls,
            ft.Row(
                controls=[input_controls, SibylList_controls]
            )
        ]
    )