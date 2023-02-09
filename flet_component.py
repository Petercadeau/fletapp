import os
import sys


class FletCreateComponent():
    def __init__(self, type, appname, componentname) -> None:
        self.appname = appname
        self.type = type

        if self.type not in ['model', 'view', 'controller']:
            if self.type == 'm':
                self.type = 'model'
            elif self.type == 'v':
                self.type = 'view'
            elif self.type == 'c':
                self.type = 'controller'

        if self.type == 'component':
            self.create_all_components(componentname)
        else:
            self.run_creator(componentname)

    def create_all_components(self, componentname):
        types = ['model', 'view', 'controller']
        for type in types:
            self.type = type
            self.run_creator(componentname)

    def run_creator(self, componentname):
        if componentname == None:
            print(f"Please provide a name for your {self.type}")
            sys.exit(1)
        component = self.type[0].upper() + self.type[1:]
        self.componentname = componentname[0].upper(
        ) + componentname[1:] + component
        if self.check_folder() and self.check_file():
            print(f"Creating {self.type}...")
            self.create_component()

    def check_folder(self):
        if os.path.exists(self.appname):
            return True

    def check_file(self):
        if os.path.isfile(f"{self.appname}/{self.appname}.py"):
            return True

    def create_component(self):
        if self.type == 'model':
            code = self.create_model_file()
            self.create_entity()
        elif self.type == 'view':
            code = self.create_view_file()
        elif self.type == 'controller':
            code = self.create_controller_file()
        '''elif self.type == 'entity':
            code = self.create_entity_file()'''
        self.create_component_file(code)

    def create_entity(self):
        entityname = self.componentname.replace('Model', '')
        component = f'''class {entityname}:
    def __init__(self) -> None:
        # properties
        pass'''
        with open(f'{self.appname}/entities/{entityname}.py', 'w') as f:
            f.write(component)

    def create_controller_file(self):
        component = f'''from flet_mvc import FletController

# Controller

class {self.componentname}(FletController):
    pass'''
        return component

    def create_view_file(self):
        component = f'''from flet_mvc import FletView
import flet as ft

# View

class {self.componentname}(FletView):
    def __init__(self, controller, model):
        view = [
            ft.Text("Hello World!")
        ]
        super().__init__(model, view, controller)'''
        return component

    def create_model_file(self):
        table = self.componentname.replace('Model', '').lower()+"s"
        return_type = self.componentname.replace('Model', '')
        component = f'''from flet_mvc import data
import flet as ft
from database.database import DataBase
from entities.{return_type} import {return_type}

# Model


class {self.componentname}():
    def __init__(self) -> None:
        """
        NOTE: __init__ method will be no longer needed
        in flet-mvc version 1.0.0. The ref objects can
        be created in a @data method like any datapoint.
        """
        self.ref_obj = ft.Ref[ft.Text]()
        self.table = "{table}"
        self.database = DataBase("mysql.connector")
        self.retun_type = {return_type}()

    @data
    def example(self):
        return ...'''
        return component

    def create_component_file(self, component):
        with open(f'{self.appname}/{self.type}s/{self.componentname}.py', 'w') as f:
            f.write(component)
