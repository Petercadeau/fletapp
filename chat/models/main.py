from flet_mvc import data
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
        return ...