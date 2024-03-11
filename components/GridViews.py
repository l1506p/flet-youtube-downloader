import flet as ft

list_view_style: dict = {
    "padding": ft.padding.only(left=20, right=20),
}


class GridViewComponent(ft.Container):
    def __init__(self):
        super(GridViewComponent, self).__init__(**list_view_style)
        self.grid_cards = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=550,
            child_aspect_ratio=1.0,
            spacing=20,
            run_spacing=20,
            padding=ft.padding.only(bottom=50, top=10),
        )

        self.content = self.grid_cards

    def cards(self, video_id, img_url, length, title, author, on_click):
        card_view = ft.Container(
            content=ft.Column(
                controls=[
                    self.create_image(img_url=img_url, length=length),
                    self.create_title(title=title),
                    self.create_author_row(
                        author=author,
                        video_id=video_id,
                        title=title,
                        on_click=on_click,
                    ),
                ],
                tight=True,
                spacing=0,
            ),
            border_radius=10,
            bgcolor=ft.colors.WHITE38,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=3,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )
        return card_view

    def create_image(self, img_url, length):
        return ft.Stack(
            controls=[
                ft.Image(
                    src=img_url,
                    fit=ft.ImageFit.FIT_WIDTH,
                    border_radius=ft.border_radius.only(top_left=10, top_right=10),
                    height=225,
                    width=550,
                ),
                ft.Container(
                    content=ft.Text(
                        length,
                        weight="bold",
                        size=20,
                        bgcolor="black",
                        color="white",
                    ),
                    right=1,
                    bottom=1,
                    padding=6,
                ),
            ]
        )

    def create_title(self, title):
        return ft.Container(
            padding=6,
            height=80,
            content=ft.Tooltip(
                message=title,
                padding=2,
                text_style=ft.TextStyle(size=16, color="white"),
                show_duration=100,
                wait_duration=500,
                content=ft.Text(
                    title,
                    weight="bold",
                    size=20,
                    text_align="start",
                    max_lines=2,
                    overflow="ellipsis",
                ),
            ),
        )

    def create_author_row(self, author, video_id, title, on_click):
        return ft.Container(
            expand=True,
            alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(left=6, bottom=10),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            author,
                            weight="bold",
                            size=14,
                            color=ft.colors.BLUE_GREY_500,
                        ),
                        padding=6,
                    ),
                    ft.TextButton(
                        content=ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.FILE_DOWNLOAD_OUTLINED,
                                        color=ft.colors.BLUE_GREY_700,
                                    ),
                                    ft.Text(
                                        "download",
                                        size=18,
                                        color=ft.colors.BLUE_GREY_700,
                                    ),
                                ]
                            )
                        ),
                        data=[video_id, title],
                        on_click=on_click,
                        style=ft.ButtonStyle(
                            color={
                                "": ft.colors.BLUE_GREY_800,
                            },
                            bgcolor={
                                "": ft.colors.TRANSPARENT,
                                ft.MaterialState.HOVERED: ft.colors.BLUE_100,
                            },
                            shape={
                                "": ft.RoundedRectangleBorder(radius=8),
                            },
                        ),
                        width=150,
                        height=40,
                    ),
                ],
                alignment="spaceBetween",
            ),
        )
