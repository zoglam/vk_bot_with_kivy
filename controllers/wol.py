import socket
import struct


class Wol:

    def _make_magic_packet(self):
        splitMac = str.split(self.mac_address, ':')
        hexMac = struct.pack(
            'BBBBBB',
            int(splitMac[0], 16),
            int(splitMac[1], 16),
            int(splitMac[2], 16),
            int(splitMac[3], 16),
            int(splitMac[4], 16),
            int(splitMac[5], 16)
        )
        self.packet = b'\xff' * 6 + hexMac * 16

    def _send_packet(self, packet):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(packet, (self.dest_ip, int(self.port)))

    def wake(self, mac_ip_port_bind: tuple):
        self.mac_address, self.dest_ip, self.port = mac_ip_port_bind
        self._make_magic_packet()
        self._send_packet(self.packet)
