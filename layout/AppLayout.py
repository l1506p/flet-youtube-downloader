import flet as ft
from components.DirectoryRow import DirectoryRowComponent
from components.SearchField import SearchField
from components.Radio import RadioComponent
from components.ProgRing import ProgressRingComponent
from api.search_service import SearchSevice
from api.video_download_service import YtVideoDownload
from api.audio_download_service import YtAudioDownload


# Creating application layout
class AppLayout(ft.Container):
    def __init__(self, page):
        super().__init__(expand=True)
        self.page = page

        self.progress_ring = ProgressRingComponent()
        self.radio_component = RadioComponent(
            page=self.page, group_change=self.radio_group_change
        )
        self.directory_row = DirectoryRowComponent(
            page=self.page, radio_component=self.radio_component
        )
        self.search_field = SearchField()
        self.video_download = YtVideoDownload(
            page=self.page,
            progress_ring=self.progress_ring,
            dir=self.directory_row,
        )
        self.audio_download = YtAudioDownload(
            page=self.page,
            progress_ring=self.progress_ring,
            dir=self.directory_row,
        )

        self.search_service = SearchSevice(
            page=self.page,
            search_field=self.search_field,
            progress_ring=self.progress_ring,
            radio_component=self.radio_component,
        )

        self.search_field.search_btn.on_click = self.search_service.main_search_results

        self.search_service_container = ft.Column(
            controls=[
                self.search_service,
            ],
            expand=True,
            scroll="auto",
        )

        self.app_container = ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        self.directory_row,
                        self.search_field,
                        self.search_service_container,
                    ],
                ),
                self.progress_ring,
            ]
        )

        self.content = self.app_container

    def radio_group_change(self, e):
        self.page.client_storage.set(
            "radioGroupValue", value=e.control.value if e.control.value else "video"
        )
        group_value = self.page.client_storage.get("radioGroupValue")
        self.radio_component.radio_group.value = group_value
        self.radio_component.radio_group.update()
        self.page.update()

        def radio_group_change_inner():
            if self.radio_component.radio_group.value == "video":
                self.search_service.download = self.video_download.downloader
                self.search_field.search_btn.on_click = (
                    self.search_service.main_search_results
                )
                self.page.update()
            elif self.radio_component.radio_group.value == "audio":
                self.search_service.download = self.audio_download.downloader
                self.search_field.search_btn.on_click = (
                    self.search_service.main_search_results
                )
                self.page.update()

        radio_group_change_inner()
