import flet as ft

search_field_style: dict = {
    "padding": ft.padding.only(top=8, left=20, right=20, bottom=8),
    "margin": ft.margin.only(left=8, right=8),
    "bgcolor": ft.colors.WHITE38,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=1,
        color=ft.colors.BLUE_GREY_300,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
}


class SearchField(ft.Container):
    def __init__(self):
        super(SearchField, self).__init__(**search_field_style)
        self.search_field = ft.TextField(
            hint_text="Search...",
            border_radius=ft.border_radius.only(top_left=8, bottom_left=8),
            border=ft.InputBorder.OUTLINE,
            expand=True,
            content_padding=ft.padding.only(left=10),
            text_style=ft.TextStyle(
                color=ft.colors.BLACK,
                weight="bold",
                size=20,
            ),
            on_change=self.refresh,
        )
        self.search_btn = ft.Container(
            content=ft.IconButton(
                icon=ft.icons.SEARCH,
                icon_size=32,
                icon_color=ft.colors.BLUE_GREY_800,
                style=ft.ButtonStyle(
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                            radius=ft.border_radius.only(top_right=8, bottom_right=8)
                        ),
                    },
                    padding={
                        "": ft.padding.only(top=8, bottom=8, left=22, right=22),
                    },
                    bgcolor=ft.colors.BLUE_200,
                    side={
                        "": ft.BorderSide(1, ft.colors.BLACK),
                    },
                ),
            )
        )

        self.content = ft.Row(
            controls=[
                self.search_field,
                self.search_btn,
            ],
            spacing=0,
        )

    def refresh(self, e):
        if self.search_field.value:
            self.search_field.error_text = ""
            self.search_btn.margin = ft.margin.only(top=0)
            self.search_field.update()
            self.search_btn.update()

    def textFieldError(self, e):
        self.search_field.error_text = "Please enter your request..."
        self.search_field.error_style = ft.TextStyle(size=16, weight="bold")
        self.search_btn.margin = ft.margin.only(bottom=31)
        self.search_field.update()
        self.search_btn.update()
