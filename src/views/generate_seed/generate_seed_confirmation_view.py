import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View
from gpio import keyboard


class GenerateSeedConfirmationView(View):
    def __init__(self, window, data):
        super().__init__(window)
        self.data = data
        keyboard.bind(self)

        # State for button navigation
        self.index = 0

        entropy_label_container = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=0
        )
        entropy_label = Gtk.Label(label=f"Entropy: {data['input']} {data['variance']}")
        entropy_label_container.pack_start(child=entropy_label, expand=False, fill=False, padding=0)

        self.buttons_container = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=0
        )

        redo_button = Gtk.Button(
            label="Redo",
            name="confirmation-view__button--selected"
        )
        redo_button.connect("clicked", lambda widget: self.click_handler("generate_seed_input"))

        confirm_button = Gtk.Button(
            label="Confirm",
            name="confirmation-view__button"
        )
        confirm_button.connect("clicked", lambda widget: self.click_handler("seed"))

        self.buttons_container.pack_start(child=redo_button, expand=True, fill=True, padding=0)
        self.buttons_container.pack_start(child=confirm_button, expand=True, fill=True, padding=0)

        self.pack_start(child=entropy_label_container, expand=False, fill=False, padding=0)
        self.pack_start(child=self.buttons_container, expand=False, fill=False, padding=0)

    def move_right(self):
        self.buttons_container.get_children()[self.index].set_name("confirmation-view__button")

        self.index = (self.index + 1) % 2

        self.buttons_container.get_children()[self.index].set_name("confirmation-view__button--selected")

    def move_left(self):
        # Same behaviour as move_right because only 2 buttons
        self.move_right()

    def select(self):
        if self.index == 0:
            self.click_handler("generate_seed_input")
        else:
            self.click_handler("seed")

    def click_handler(self, path):
        self.window.navigate_to(
            path=path,
            data=self.data
        )

