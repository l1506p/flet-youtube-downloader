import flet as ft


class RadioComponent(ft.Container):
    def __init__(self, page, group_change):
        super(RadioComponent, self).__init__(padding=-8)
        self.page = page
        self.group_change = group_change
        self.radio_group = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="video", label="Video"),
                    ft.Radio(value="audio", label="Audio"),
                ]
            ),
            on_change=self.group_change,
        )
        self.content = self.radio_group
