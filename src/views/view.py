import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class View(Gtk.Box):
    def __init__(self, window):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=0,
            name="view-container"
        )

        self.window = window
