import flet as ft
from controllers.main import Controller
from views.main import MainView
from models.main import Model
from models.UserModel import UserModel
from views.UserView import UserView
from controllers.UserController import UserController
from config import Config


def main(page: ft.Page):
    # MVC set-up
    #model = Model()
    #controller = Controller(page, model)
    #view = MainView(controller, model)
    user_model = UserModel()
    user_controller = UserController(page, user_model)
    user_view = UserView(user_controller, user_model)
    config = Config()

    # Settings
    page.title = config.appname
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Run
    '''page.add(
        *view.content
    )'''
    page.add(
        *user_view.content
    )


ft.app(target=main)
