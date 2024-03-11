import flet as ft
from components.GridViews import GridViewComponent
from api.pytube_api import search_results
from utils.convert import convert
from utils.check_network_connection import check_connection
from utils.exceptions import video_or_audio_exception


class SearchSevice(ft.Container):
    def __init__(
        self,
        page,
        search_field,
        progress_ring,
        radio_component,
        download=None,
    ):
        super(SearchSevice, self).__init__()
        self.page = page
        self.progress_ring = progress_ring
        self.download = download
        self.grid_view = GridViewComponent()
        self.search_field = search_field
        self.radio_component = radio_component

        self.content = ft.Column(
            controls=[
                self.grid_view,
            ],
            expand=True,
            scroll="auto",
        )

    def main_search_results(self, e):
        if self.radio_component.radio_group.value == None:
            video_or_audio_exception(page=self.page)
        elif not self.search_field.search_field.value:
            self.search_field.textFieldError(e=e)
        else:
            self.progress_ring.visible = True
            self.progress_ring.update()
            res = search_results(input_value=self.search_field.search_field.value)
            self.progress_ring.visible = False
            self.progress_ring.update()
            self.grid_view.content.controls.clear()
            if res is not None:
                for i in res:
                    self.grid_view.content.controls.append(
                        self.grid_view.cards(
                            video_id=i.video_id,
                            img_url=i.thumbnail_url,
                            title=i.title,
                            author=i.author,
                            on_click=self.download,
                            length=convert(i.length),
                        )
                    )
                    self.grid_view.update()
                    self.page.update()
            else:
                check_connection(page=self.page)
                self.progress_ring.visible = False
                self.progress_ring.update()
