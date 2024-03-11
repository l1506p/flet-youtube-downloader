import flet as ft

dir_container_style: dict = {
    "padding": ft.padding.only(top=8, bottom=8),
    "margin": ft.margin.only(left=8, right=8, top=8),
    "bgcolor": ft.colors.WHITE38,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=1,
        color=ft.colors.BLUE_GREY_300,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
}


class DirectoryRowComponent(ft.Container):
    def __init__(self, page, radio_component):
        super(DirectoryRowComponent, self).__init__(**dir_container_style)
        self.page = page
        self.radio_component = radio_component
        self.get_directory_dialog = ft.FilePicker(on_result=self.set_directory_result)
        self.directory_path = ft.Text(
            weight="bold",
            size=15,
            color=ft.colors.BLUE_GREY_800,
        )
        self.directory_path.value = self.page.client_storage.get("download_path")
        self.page.overlay.extend([self.get_directory_dialog])

        self.brows_btn = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(
                            name=ft.icons.FOLDER_OUTLINED,
                            color=ft.colors.BLUE_GREY_800,
                        ),
                        ft.Text(
                            "Brows",
                            size=16,
                            weight="bold",
                            color=ft.colors.BLUE_GREY_800,
                        ),
                    ]
                )
            ),
            on_click=lambda _: self.get_directory_dialog.get_directory_path(),
            height=35,
            width=130,
            bgcolor="blue200",
            style=ft.ButtonStyle(
                shape={
                    "": ft.RoundedRectangleBorder(radius=8),
                },
            ),
        )

        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                self.brows_btn,
                                ft.Text(
                                    "Download Path: ",
                                    size=20,
                                    weight="bold",
                                    color=ft.colors.BLUE_GREY_800,
                                ),
                                self.directory_path,
                            ]
                        )
                    ),
                    self.radio_component,
                ],
                alignment="spaceEvenly",
            ),
        )

    def set_directory_result(self, e: ft.FilePickerResultEvent):
        dir_path = self.page.client_storage.get("download_path")
        self.page.client_storage.set(
            "download_path", value=e.path if e.path else dir_path
        )
        dir_path = self.page.client_storage.get("download_path")
        self.directory_path.value = dir_path
        self.directory_path.update()
