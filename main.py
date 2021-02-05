from threading import Thread
import ctypes

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from controllers.logger import Logger
from controllers.vk.bot import Bot
from controllers.parser import Parser
from config import colors


class BotThread(Thread):

    def __init__(self, parser: Parser, logger: Logger):
        self.bot = Bot(parser, logger)
        Thread.__init__(self)

    def run(self):
        self.bot.start_polling()


class Main(MDApp):

    bot: BotThread = None
    parser: Parser
    logger: Logger

    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('templates/screen/screens.kv')

    def on_start(self):
        app = MDApp.get_running_app()
        self.parser = Parser(app)
        self.logger = Logger().init_terminal_instance(app)
        self.logger.info('App started')

    def go_to_server(self, screen_manager: ScreenManager):
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'server'

    def go_to_settings(self, screen_manager: ScreenManager):
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'settings'

    def run_bot(self):
        token = self.parser.get_token()
        bot_status = self.parser.get_bot_status()
        try:
            if self.bot is not None:
                self.bot = None
                self.logger.info('Polling stopped')
                bot_status.circle_color = colors.RED_COLOR
            elif token:
                self.bot = BotThread(self.parser, self.logger)
                self.bot.start()
                self.logger.info('Polling started')
                bot_status.circle_color = colors.GREEN_COLOR
            else:
                self.logger.alert('Empty token')
                bot_status.circle_color = colors.RED_COLOR
        except Exception as e:
            self.bot = None
            self.logger.alert(e)
            bot_status.circle_color = colors.RED_COLOR


if __name__ == '__main__':
    Main().run()
