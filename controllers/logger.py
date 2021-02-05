from kivymd.app import MDApp
from kivymd.uix.label import Label

from controllers.datetime import DateTime
from config import colors

class Logger(Label):

    def init_terminal_instance(self, app: MDApp):
        self.terminal = app.root.ids.terminal
        return self

    def print_to_terminal(func):
        def wrapper(self, *args, **kwargs):
            new_log = Logger(**func(self, *args, **kwargs))
            self.terminal.add_widget(new_log)
        return wrapper

    @print_to_terminal
    def info(self, msg):
        return {
            'text': f'INFO | {DateTime.now()} | {msg}',
            'color': colors.WHITE_COLOR
        }

    @print_to_terminal
    def warning(self, msg):
        return {
            'text': f'WARN | {DateTime.now()} | {msg}',
            'color': colors.YELLOW_COLOR
        }

    @print_to_terminal
    def alert(self, msg):
        return {
            'text': f'ALERT | {DateTime.now()} | {msg}',
            'color': colors.RED_COLOR
        }
