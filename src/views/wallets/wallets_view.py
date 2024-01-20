import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

from views.view import View


class WalletsView(View):
    def __init__(self, window):
        super().__init__(window)

        # State for button navigation
        self.index = 0

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="assets/images/ethereum.png",
            width=32,
            height=32,
            preserve_aspect_ratio=True
        )
        ethereum_image = Gtk.Image.new_from_pixbuf(pixbuf)

        ethereum_button = Gtk.Button(
            label="Ethereum",
            name="navigation-button--selected",
            image=ethereum_image,
            always_show_image=True
        )

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="assets/images/bitcoin.png",
            width=32,
            height=32,
            preserve_aspect_ratio=True
        )
        bitcoin_image = Gtk.Image.new_from_pixbuf(pixbuf)

        bitcoin_button = Gtk.Button(
            label="Bitcoin",
            name="navigation-button",
            image=bitcoin_image,
            always_show_image=True
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
        # Todo: Generate public key, qr
        self.window.navigate_to(
            path="wallet_address",
            data=data
        )
