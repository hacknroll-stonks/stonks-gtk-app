import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class GenerateSeedConfirmationView(View):
    def __init__(self, window, data):
        super().__init__(window)
        self.data = data

        entropy_label_container = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=0
        )
        entropy_label = Gtk.Label(label=f"Entropy: {data['input']} {data['variance']}")
        entropy_label_container.pack_start(child=entropy_label, expand=False, fill=False, padding=0)

        buttons_container = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=0
        )

        redo_button = Gtk.Button(
            label="Redo"
        )
        redo_button.connect("clicked", self.click_handler, "generate_seed_input")

        confirm_button = Gtk.Button(
            label="Confirm"
        )
        confirm_button.connect("clicked", self.click_handler, "seed")

        buttons_container.pack_start(child=redo_button, expand=True, fill=True, padding=0)
        buttons_container.pack_start(child=confirm_button, expand=True, fill=True, padding=0)

        self.pack_start(child=entropy_label_container, expand=False, fill=False, padding=0)
        self.pack_start(child=buttons_container, expand=False, fill=False, padding=0)

    def click_handler(self, widget, path):
        self.window.navigate_to(
            path=path,
            data=self.data
        )

