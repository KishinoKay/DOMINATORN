import flet as ft
from View.main_page import main_view
from View.measure_page import measure_view
from View.Execution_page import Execution_view
from View.access_SibylSystem import SibylSystem


def main(page: ft.Page):
    def route_change(e):
        app_route = ft.TemplateRoute(page.route)
        page.views.clear()
    
        if app_route.match("/main_page"):
            page.views.append(main_view(page)) #メイン画面
        elif app_route.match("/measure_page"):
            page.views.append(measure_view(page)) #計測画面
        elif app_route.match("/Execution_page"):
            page.views.append(Execution_view(page)) #執行画面
        elif app_route.match("/access_SibylSystem"):
            page.views.append(SibylSystem(page)) #データベース閲覧画面
        page.update()

    page.on_route_change = route_change

    page.go("/main_page") #グラフ描写画面のページへ移動



ft.app(main)
