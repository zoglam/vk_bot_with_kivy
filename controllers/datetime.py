from datetime import datetime


class DateTime:
    @staticmethod
    def now():
        return datetime.now().strftime("%d %b %H:%M")
