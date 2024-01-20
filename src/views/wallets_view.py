import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class WalletsView(View):
    def __init__(self, window):
        super().__init__(window)

        # State for button navigation
        self.index = 0

        ethereum_button = Gtk.Button(
            label="Ethereum",
            name="navigation-button--selected"
        )

        bitcoin_button = Gtk.Button(
            label="Bitcoin",
            name="navigation-button"
        )

        self.pack_start(child=ethereum_button, expand=True, fill=True, padding=0)
        self.pack_start(child=bitcoin_button, expand=True, fill=True, padding=0)

    def move_right(self):
        self.get_children()[self.index].set_name("navigation-button")

        self.index = (self.index + 1) % 2

        self.get_children()[self.index].set_name("navigation-button--selected")

    def move_left(self):
        # Same behaviour as move_right because only 2 buttons
        self.move_right()

    def select(self):
        if self.index == 0:
            self.click_handler({"wallet": "ethereum"})
        else:
            self.click_handler({"wallet": "bitcoin"})

    def click_handler(self, data):
        self.window.navigate_to(
            path="wallet_address",
            data=data
        )
