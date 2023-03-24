from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.menu_screen import MenuScreenModel
from Controller.menu_screen import MenuScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "menu screen": {
        "model": MenuScreenModel,
        "controller": MenuScreenController,
    },
}