from .color import color


class host:

    def __init__(self, index, identification, IP, connections):
        self.index = index
        self.id = identification
        self.IP = IP
        self.connections = connections

    def get_id(self):
        return self.id

    def get_index(self):
        return self.index

    def get_connections(self):
        return self.connections

    def add_connection(self, identification):
        self.connections.append(identification)

        return self.connections
