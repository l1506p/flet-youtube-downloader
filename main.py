# import sys
import flet as ft
from layout.AppLayout import AppLayout
from utils.check_network_connection import check_connection

# output = open("output.txt", "wt")
# sys.stdout = output
# sys.stderr = output


def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.padding = 0
    page.bgcolor = ft.colors.AMBER_50
    page.window_min_width = 800

    page.appbar = ft.AppBar(
        title=ft.Text(
            "YOUTUBE DOWNLOADER",
            size=32,
            weight="bold",
            color=ft.colors.BLUE_GREY_800,
        ),
        center_title=True,
        bgcolor="blue300",
        toolbar_height=80,
    )

    def banner_close(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor="blue400",
        content=ft.Text(
            value="No internet connection",
            size=14,
            text_align="center",
        ),
        actions=[ft.IconButton(icon=ft.icons.CLOSE, on_click=banner_close)],
        content_padding=-10,
    )

    page.snack_bar = ft.SnackBar(
        bgcolor="#4bb346",
        content=ft.Text(
            "Downloaded successfully",
            size=18,
            color=ft.colors.BLUE_GREY_900,
            weight="bold",
            text_align="center",
        ),
    )

    check_connection(page=page)

    app_layout = AppLayout(page=page)

    page.add(app_layout)
    page.update()


ft.app(main, assets_dir="assets")
