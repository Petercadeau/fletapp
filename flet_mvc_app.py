import os

# get arguments
args = os.sys.argv
if len(args) < 2:
    print("Please provide a name for your app.")
    os.sys.exit(1)
appname = args[1]

print(f"Creating app {appname}...")


def check_folder(path):
    if os.path.exists(path):
        print("App already exists.")
        os.sys.exit(1)


check_folder(appname)

def create_folder(path):
    path = os.path.join(appname, path)
    if not os.path.exists(path):
        os.makedirs(path)


create_folder('models')
create_folder('views')
create_folder('entities')
create_folder('database')
create_folder('controllers')


def create_file(path, content):
    path = os.path.join(appname, path)
    with open(path, 'w') as f:
        f.write(content)


create_file('models/__init__.py', '')
create_file('views/__init__.py', '')
create_file('controllers/__init__.py', '')

models_init = '''from flet_mvc import data
import flet as ft

# Model


class Model():
    def __init__(self) -> None:
        """
        NOTE: __init__ method will be no longer needed
        in flet-mvc version 1.0.0. The ref objects can
        be created in a @data method like any datapoint.
        """
        self.ref_obj = ft.Ref[ft.Text]()

    @data
    def example(self):
        return ...'''

controllers_init = '''from flet_mvc import FletController

# Controller

class Controller(FletController):
    pass'''

views_init = '''from flet_mvc import FletView
import flet as ft

# View

class MainView(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text("Hello World!")
        ]
        super().__init__(model, view, controller)
'''

database_init = '''import config as Config
import mysql.connector as con


class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()
        return {description[0]: row[col] for col, description in enumerate(self._cursor.description)}


class DataBase():
    def __init__(self, connector) -> None:
        self.connector = connector
        self.config = Config.Config()
        self.con = self.get_conector()
        self.cursor = self.con.cursor()

    def get_conector(self):
        if self.connector == "mysql.connector":
            return con.connect(
                host=self.config.server,
                user=self.config.user,
                passwd=self.config.password,
                database=self.config.dbname,
                port=self.config.port
            )

    def get_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return CursorByName(self.cursor)

    def get_columns(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.column_names
'''

create_file('views/main.py', views_init)
create_file('models/main.py', models_init)
create_file('database/database.py', database_init)
create_file('controllers/main.py', controllers_init)

app_init = '''import flet as ft
from controllers.main import Controller
from views.main import MainView
from models.main import Model
from config import Config


def main(page: ft.Page):
    # MVC set-up
    model = Model()
    controller = Controller(page, model)
    view = MainView(controller, model)

    config = Config()

    # Settings
    page.title = config.appname

    # Run
    page.add(
        *view.content
    )


ft.app(target=main)
'''

appname_config = appname[0].upper() + appname[1:]

config_init = f'''class Config():
    def __init__(self) -> None:
        self.appname = "{appname_config}"
        self.dbname = "{appname}db"
        self.server = "localhost"
        self.user = "root"
        self.password = ""
        self.port = 3306
        self.connector = "mysql.connector"'''

create_file('config.py', config_init)
create_file(appname+'.py', app_init)
