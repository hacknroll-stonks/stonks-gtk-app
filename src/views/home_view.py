import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class HomeView(Gtk.Box):
    def __init__(self, window):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0
        )

        self.window = window

        generate_seed_view_button = Gtk.Button(label="New seed phrase")
        generate_seed_view_button.connect("clicked", self.window.navigate_to, self, "generate_seed_input")

        wallets_view_button = Gtk.Button(label="Wallets")
        wallets_view_button.connect("clicked", self.window.navigate_to, self, "wallets")

        self.pack_start(child=generate_seed_view_button, expand=True, fill=True, padding=0)
        self.pack_start(child=wallets_view_button, expand=True, fill=True, padding=0)
