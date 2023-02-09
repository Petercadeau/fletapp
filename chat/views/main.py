from flet_mvc import FletView
import flet as ft

# View

class MainView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text("Hello World!")
        ]
        super().__init__(model, view, controller)
