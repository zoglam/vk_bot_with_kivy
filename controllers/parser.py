import re

from kivymd.app import MDApp


class Parser:

    def __init__(self, app: MDApp):
        self.app = app

    def get_token(self) -> str:
        return self.app.root.ids.token.text

    def get_mac_ip_port_bind(self) -> tuple:
        return (
            self.app.root.ids.mac_address.text,
            self.app.root.ids.ip_address.text,
            self.app.root.ids.port.text
        )

    @property
    def mac_ip_port_valid_statuses(self) -> dict:
        mac_address, ip_address, port = self.get_mac_ip_port_bind()
        return {
            'mac_address': re.search(
                r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',
                mac_address
            ),
            'ip_address': re.search(
                r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$',
                ip_address
            ),
            'port': re.search(
                r'^(\d{1,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$',
                port
            )
        }

    def is_valid_params(self) -> bool:
        return all(self.mac_ip_port_valid_statuses.values())

    def get_mac_ip_port_invalid_params(self) -> str:
        return ', '.join(
            [
                p for p in self.mac_ip_port_valid_statuses
                if not self.mac_ip_port_valid_statuses[p]
            ])

    def get_bot_status(self) -> object:
        return self.app.root.ids.bot_status
