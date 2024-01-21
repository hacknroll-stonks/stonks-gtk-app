import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View
from gpio import buttons


class HomeView(View):
    def __init__(self, window):
        super().__init__(window)

        # State for button navigation
        self.index = 0

        buttons.bind(self)

        generate_seed_view_button = Gtk.Button(
            label="New seed phrase",
            name="navigation-button--selected"
        )
        # Todo: Temp testing
        generate_seed_view_button.connect("clicked", lambda widget, path: self.click_handler(path), "generate_seed_input")

        wallets_view_button = Gtk.Button(
            label="Wallets",
            name="navigation-button"
        )
        wallets_view_button.connect("clicked", lambda widget, path: self.click_handler(path), "wallets")

        self.pack_start(child=generate_seed_view_button, expand=True, fill=True, padding=0)
        self.pack_start(child=wallets_view_button, expand=True, fill=True, padding=0)

    def move_right(self):
        self.get_children()[self.index].set_name("navigation-button")

        self.index = (self.index + 1) % 2

        self.get_children()[self.index].set_name("navigation-button--selected")

    def move_left(self):
        # Same behaviour as move_right because only 2 buttons
        self.move_right()

    def select(self):
        if self.index == 0:
            self.click_handler("generate_seed_input")
        else:
            self.click_handler("wallets")

    def click_handler(self, path):
        self.window.navigate_to(
            path=path,
            data=None
        )
