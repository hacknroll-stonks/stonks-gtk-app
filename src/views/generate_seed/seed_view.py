import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class SeedView(View):
    def __init__(self, window, data):
        super().__init__(window)
        self.data = data

        # Todo: Integrate with seed generation
        seed = "hello world"

        seed_label = Gtk.Label(
            label=seed
        )

        confirmation_button = Gtk.Button(
            label="OK"
        )
        confirmation_button.connect("clicked", self.click_handler)

        self.pack_start(child=seed_label, expand=False, fill=False, padding=0)
        self.pack_start(child=confirmation_button, expand=False, fill=False, padding=0)

    def click_handler(self, widget):
        self.window.navigate_to(
            path="home",
            data=None
        )
