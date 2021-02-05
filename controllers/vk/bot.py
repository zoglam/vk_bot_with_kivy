import http.client

from vk_api import VkApi
from vk_api.vk_api import VkApiMethod
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

from controllers.logger import Logger
from controllers.parser import Parser
from controllers.vk.view import View
from controllers.wol import Wol

message_handlers = []


class Bot:

    longpoll: VkLongPoll
    Lsvk: VkApiMethod

    def __init__(self, parser: Parser, logger: Logger):
        self.logger = logger
        self.parser = parser
        self.wol = Wol()
        self.init_session()

    def init_session(self):
        vk_session = VkApi(token=self.parser.get_token())
        self.longpoll = VkLongPoll(vk_session)
        self.Lsvk = vk_session.get_api()

    def message_handler(commands=None, **kwargs):
        def decorator(func):
            message_handlers.append({'func': func, 'commands': commands})
            return func
        return decorator

    @message_handler(commands=['Узнать IP'])
    def get_ip(self, msg):
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        output_message = conn.getresponse().read().decode('UTF-8')
        self.send_message(msg.user_id, output_message)

    @message_handler(commands=['Включить PC'])
    def turn_on_pc(self, msg):
        if self.parser.is_valid_params():
            self.wol.wake(self.parser.get_mac_ip_port_bind())
            self.logger.info('WOL packet successfully sent')
        else:
            raise Exception(
                f"Invalid format for: {self.parser.get_mac_ip_port_invalid_params()}")

    def send_message(self, user_id, message):
        self.Lsvk.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=View.get_keyboard(),
            message=message
        )

    def start_polling(self):
        try:
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    self.logger.info(
                        f'Message from id{event.user_id}: {event.text}')
                    for message_handler in message_handlers:
                        if event.text in message_handler['commands']:
                            message_handler['func'](self, event)
                            break
        except Exception as error:
            self.logger.alert(error)
            self.parser.app.run_bot()
            return
