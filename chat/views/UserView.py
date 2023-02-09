from flet_mvc import FletView
import flet as ft
from flet import (TextField, Container, Column, Row, Text, ElevatedButton)

# View


class UserView(FletView):
    def __init__(self, controller, model):
        self.username = TextField(
            value="Admin",
            height=35,
            text_size=12,
            content_padding=10,
        )
        self.password = TextField(
            value="admin",
            height=35,
            text_size=12,
            content_padding=10,
            password=True
        )
        view = [
            Container(
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                Text(
                                    "Login",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            alignment="center",
                        ),
                        Column(
                            controls=[
                                Text("Username"),
                                self.username,
                            ]
                        ),
                        Column(
                            controls=[
                                Text("Password"),
                                self.password,
                            ]
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="Login",
                                    on_click=self.login,
                                    width=100,
                                    height=35,
                                ),
                            ],
                            alignment="center",
                        ),
                    ]),
                bgcolor=ft.colors.BLACK12,
                border_radius=10,
                padding=10,
                width=300,
            )
        ]
        super().__init__(model, view, controller)

    def login(self, e):
        username = self.username.value
        password = self.password.value
        self.controller.login(username, password)
