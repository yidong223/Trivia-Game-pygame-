from .base import PygameController


class EndController(PygameController):
    """End Screen Controller: Runs event that displays End view, wait for ESC or window close to exit """

    def __init__(self, view):
        super().__init__(view)
        pass
    