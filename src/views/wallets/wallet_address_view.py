import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

from views.view import View


class WalletAddressView(View):
    def __init__(self, window, data):
        super().__init__(window)

        self.data = data

        # Todo: Insert QR code
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="assets/images/ethereum.png",
            width=256,
            height=256,
            preserve_aspect_ratio=True
        )
        qr_image = Gtk.Image.new_from_pixbuf(pixbuf)

        public_key_label = Gtk.Label(
            label=data["public_key"],
            name="wallet-address-view__label"
        )

        home_button = Gtk.Button(
            label="Home",
            name="submit-button--selected"
        )

        self.pack_start(child=qr_image, expand=False, fill=False, padding=0)
        self.pack_start(child=public_key_label, expand=False, fill=False, padding=0)
        self.pack_start(child=home_button, expand=False, fill=False, padding=0)

    def move_right(self):
        pass

    def move_left(self):
        pass

    def select(self):
        self.window.navigate_to(
            path="home",
            data=None
        )
