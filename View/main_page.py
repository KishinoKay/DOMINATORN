import flet as ft
import pygame
import threading
from Script.custom_color import custom_color_scheme

# 音声再生を非同期で管理するためにpygameを使う
pygame.mixer.init()
is_playing = False

# 音声を再生する関数
def play_sound():
    global is_playing
    if not is_playing:
        pygame.mixer.music.load('./Audio/mainpage.mp3')
        pygame.mixer.music.play(loops=0, start=0.0)
        is_playing = True

# 音声を停止する関数
def stop_sound1(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    page.go("/measure_page")

def stop_sound2(page):
    global is_playing
    if is_playing:
        pygame.mixer.music.stop()
        is_playing = False
    page.go("/access_SibylSystem")


def main_view(page):
    page.theme_mode = ft.ThemeMode.DARK  # ダークモード
    page.theme = ft.Theme(color_scheme=custom_color_scheme)

    # 音声を非同期で再生
    threading.Thread(target=play_sound).start()

    main_controls = ft.Column(
        controls=[
        ft.Text(
            "携帯型心理診断同担鎮圧執行システム",
            size=32,  # 文字サイズを明示的に指定
            weight=ft.FontWeight.BOLD
        ),
        ft.Text("ドミネー担",
                size=42,  # 文字サイズを明示的に指定
                weight=ft.FontWeight.BOLD
            ),
        ft.ElevatedButton("計測開始", on_click=lambda _: stop_sound1(page)),
        ft.ElevatedButton("データベースにアクセス", on_click=lambda _: stop_sound2(page))
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    alignment=ft.MainAxisAlignment.CENTER
    )

    return ft.View(
        "/graph_page",
        controls=[
            ft.Container(
                content=main_controls,
                alignment=ft.Alignment(0,0),  # 全体の中央揃え
                expand=True,  # ページ全体に広げる
                image_src="./assets/main_page.jpg",
                image_fit=ft.ImageFit.COVER
            )
        ]
    )