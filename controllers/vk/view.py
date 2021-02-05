from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class View:
    @staticmethod
    def get_keyboard():
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('Узнать IP', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Включить PC', color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()
