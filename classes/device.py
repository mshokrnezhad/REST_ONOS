from .color import color


class device:

    def __init__(self, index, identification, name, hw_type, connections):
        self.index = index
        self.id = identification
        self.name = name
        self.type = hw_type
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