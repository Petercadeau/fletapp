from flet_mvc import data
import flet as ft
from database.database import DataBase
from entities.User import User
from copy import copy

# Model


class UserModel():
    def __init__(self) -> None:
        """
        NOTE: __init__ method will be no longer needed
        in flet-mvc version 1.0.0. The ref objects can
        be created in a @data method like any datapoint.
        """
        self.ref_obj = ft.Ref[ft.Text]()
        self.table = "users"
        self.database = DataBase("mysql.connector")
        self.retun_type = User()
        self.__transform()

    @data
    def example(self):
        return ...

    @data
    def username(self):
        return "Peterca"

    @data
    def password(self):
        return "1234"

    @data
    def all(self):
        return self.all_data

    def __transform(self):
        self.all_data = []
        for row in self.database.get_all(self.table):
            element = copy(self.retun_type)
            for item in row:
                setattr(element, item, row[item])
            self.all_data.append(element)
