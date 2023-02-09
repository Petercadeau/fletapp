from flet_mvc import FletController
from flet_mvc import alert

# Controller


class UserController(FletController):

    def login(self, username, password):
        for row in self.model.all():
            if row.username == username and row.password == password:
                # TODO: Change to chat page
                self.alert("Login successful", alert.SUCCESS)
                return True
        self.alert("Wrong username or password", alert.ERROR)
        return False

    def get_by_cedula(self, cedula):
        for row in self.model.all():
            if row.cedula == cedula:
                return row
