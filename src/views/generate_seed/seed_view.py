import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View

class SeedView(View):
    def __init__(self, window, data):
        super().__init__(window)
        self.data = data

        # Todo: Integrate with seed generation
        with open("Mnemonic.txt","r") as file:
            seed = file.readline().strip()


        seed_label = Gtk.Label(
            label=seed,
            wrap=True
        )

        confirmation_button = Gtk.Button(
            label="OK",
            name="submit-button--selected"
        )
        confirmation_button.connect("clicked", lambda widget: self.select())

        self.pack_start(child=seed_label, expand=False, fill=False, padding=0)
        self.pack_start(child=confirmation_button, expand=False, fill=False, padding=0)

    def move_right(self):
        pass

    def move_left(self):
        pass

    def select(self):
        self.window.navigate_to(
            path="home",
            data=None
        )
