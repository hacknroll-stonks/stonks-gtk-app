import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

from views.view import View
from gpio import buttons, keyboard

class WalletsView(View):
    
    bitcoinKey = ""
    ethereumKey = ""

    def __init__(self, window):
        super().__init__(window)
        keyboard.bind(self)

        # Read the public keys
        with open("Address.txt", "r") as file:
            bitcoinKey = file.readline().strip().split(" ")[1]
            ethereumKey = file.readline().strip().split(" ")[1]
        
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
        ethereum_button.connect("clicked", lambda widget: self.click_handler({"public_key": "ethereum"}))

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
        bitcoin_button.connect("clicked", lambda widget: self.click_handler({"public_key": "bitcoin"}))

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
            self.click_handler({"public_key": ethereumKey})
        else:
            self.click_handler({"public_key": bitcoinKey})

    def click_handler(self, data):
        # Todo: Generate public key, qr
        self.window.navigate_to(
            path="wallet_address",
            data=data
        )
