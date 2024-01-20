import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class HomeView(View):
    def __init__(self, window):
        super().__init__(window)

        generate_seed_view_button = Gtk.Button(
            label="New seed phrase",
            name="home-view__navigation-button"
        )
        generate_seed_view_button.connect("clicked", self.click_handler, "generate_seed_input")

        wallets_view_button = Gtk.Button(
            label="Wallets",
            name="home-view__navigation-button"
        )
        wallets_view_button.connect("clicked", self.click_handler, "wallets")

        self.pack_start(child=generate_seed_view_button, expand=True, fill=True, padding=0)
        self.pack_start(child=wallets_view_button, expand=True, fill=True, padding=0)

    def click_handler(self, widget, path):
        self.window.navigate_to(
            path=path,
            data=None
        )
