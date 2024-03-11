import flet as ft


def alertDialog(page, content_text, title, color):
    def close_dialog(e):
        alert_dialog.open = False
        page.update()

    alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title, color=color, weight="bold"),
        content=ft.Text(content_text, color=color, weight="bold"),
        actions=[
            ft.ElevatedButton("Ok", color=color, on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape=ft.RoundedRectangleBorder(radius=8),
    )

    return alert_dialog
