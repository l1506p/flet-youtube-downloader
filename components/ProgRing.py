import flet as ft


class ProgressRingComponent(ft.Container):
    def __init__(self):
        super(ProgressRingComponent, self).__init__(
            expand=True,
            visible=False,
            bgcolor=ft.colors.with_opacity(
                0.3,
                ft.colors.BLACK,
            ),
        )
        self.content = ft.Stack(
            [
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.ProgressRing(
                                        bgcolor=ft.colors.BLUE_100,
                                        height=60,
                                        width=60,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ]
        )
