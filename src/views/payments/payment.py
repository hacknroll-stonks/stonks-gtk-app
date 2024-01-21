import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class PaymentView(View):
    def __init__(self, window, data):
        super().__init__(window)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="assets/images/ethereum_QR_Code.png",
            width=256,
            height=256,
            preserve_aspect_ratio=True
        )
        qr_image = Gtk.Image.new_from_pixbuf(pixbuf)

        transaction_id_label = Gtk.Label(
            label=f"Transaction ID: {data['transaction_id']}"
        )

        address_from_label = Gtk.Label(
            label=f"Address from: {data['address_from']}"
        )

        address_to_label = Gtk.Label(
            label=f"Address to: {data['address_to']}"
        )

        value_label = Gtk.Label(
            label=f"Value: {data['value']}"
        )

        fees_label = Gtk.Label(
            label=f"Fee: {data['fee']}"
        )

        self.pack_start(child=qr_image, expand=False, fill=False, padding=0)
        self.pack_start(child=transaction_id_label, expand=False, fill=False, padding=0)
        self.pack_start(child=address_from_label, expand=False, fill=False, padding=0)
        self.pack_start(child=address_to_label, expand=False, fill=False, padding=0)
        self.pack_start(child=value_label, expand=False, fill=False, padding=0)
        self.pack_start(child=fees_label, expand=False, fill=False, padding=0)

        home_button = Gtk.Button(
            label="Home",
            name="submit-button--selected"
        )
        home_button.connect("clicked", lambda widget: self.select())

        self.pack_start(child=home_button, expand=False, fill=False, padding=0)

    def select(self):
        self.window.navigate_to(
            path="home",
            data=None
        )
