import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class GenerateSeedInputView(View):
    def __init__(self, window):
        super().__init__(window)

        entropy_label_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        entropy_label = Gtk.Label(label="Entropy")
        entropy_label_container.pack_start(child=entropy_label, expand=False, fill=False, padding=0)

        self.entropy_entry = Gtk.Entry(
            name="input-view__entropy-entry",
            placeholder_text="Input entropy values"
        )

        self.variance_check_button = Gtk.CheckButton(
            label="Variance?",
        )

        submit_button = Gtk.Button(
            label="Submit",
            name="input-view__submit-button"
        )
        submit_button.connect("clicked", self.submit_handler, "generate_seed_confirmation")

        self.pack_start(child=entropy_label_container, expand=False, fill=False, padding=0)
        self.pack_start(child=self.entropy_entry, expand=False, fill=False, padding=0)
        self.pack_start(child=self.variance_check_button, expand=False, fill=False, padding=0)
        self.pack_start(child=submit_button, expand=False, fill=False, padding=0)

    def submit_handler(self, widget, path):
        print(self.entropy_entry.get_text())
        print(self.variance_check_button.get_active())
        # Todo: Integrate with seed generation

        self.window.navigate_to(
            path="generate_seed_confirmation",
            data={
                "seed": "hello world"
            }
        )
