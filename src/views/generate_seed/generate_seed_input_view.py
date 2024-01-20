import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from views.view import View


class GenerateSeedInputView(View):
    def __init__(self, window):
        super().__init__(window)

        # State for button navigation
        self.section = 0  # 0: entropy_entry, 1: check_button + self.submit_button
        self.index = 0  # Index in current section

        entropy_label_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        entropy_label = Gtk.Label(label="Entropy")
        entropy_label_container.pack_start(child=entropy_label, expand=False, fill=False, padding=0)

        # Section 0: entropy_entry
        self.entropy_entry = Gtk.Entry(
            name="input-view__entropy-entry",
            placeholder_text="Input entropy values"
        )

        self.num_buttons_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

        # Initialize first num button as selected
        num_button = Gtk.Button(
            label=0,
            name="input-view__num-button--selected"
        )
        self.num_buttons_container.pack_start(child=num_button, expand=False, fill=False, padding=0)

        for i in range(1, 10):
            num_button = Gtk.Button(
                label=i,
                name="input-view__num-button"
            )
            self.num_buttons_container.pack_start(child=num_button, expand=False, fill=False, padding=0)

        # Add a finish input button
        finish_input_button = Gtk.Button(
            label="OK",
            name="input-view__num-button"
        )
        self.num_buttons_container.pack_start(child=finish_input_button, expand=False, fill=False, padding=0)

        # Section 1: check_button / submit_button
        self.variance_check_button = Gtk.CheckButton(
            label="Variance?",
        )

        self.submit_button = Gtk.Button(
            label="Submit",
            name="submit-button"
        )
        self.submit_button.connect("clicked", lambda widget: self.submit_handler())

        self.pack_start(child=entropy_label_container, expand=False, fill=False, padding=0)
        self.pack_start(child=self.entropy_entry, expand=False, fill=False, padding=0)
        self.pack_start(child=self.num_buttons_container, expand=False, fill=False, padding=0)
        self.pack_start(child=self.variance_check_button, expand=False, fill=False, padding=0)
        self.pack_start(child=self.submit_button, expand=False, fill=False, padding=0)

    def move_right(self):
        # entropy_entry
        if self.section == 0:
            prev_selected = self.num_buttons_container.get_children()[self.index]
            prev_selected.set_name("input-view__num-button")

            self.index = (self.index + 1) % 11

            new_selected = self.num_buttons_container.get_children()[self.index]
            new_selected.set_name("input-view__num-button--selected")

        # variance_check_button / self.submit_button
        else:
            if self.index == 0:
                self.index = 1
                self.variance_check_button.set_name("input-view__check-button")
                self.submit_button.set_name("submit-button--selected")

            else:
                self.index = 0
                self.variance_check_button.set_name("input-view__check-button--selected")
                self.submit_button.set_name("submit-button")

    def move_left(self):
        # entropy_entry
        if self.section == 0:
            prev_selected = self.num_buttons_container.get_children()[self.index]
            prev_selected.set_name("input-view__num-button")

            self.index = (self.index + 10) % 11

            new_selected = self.num_buttons_container.get_children()[self.index]
            new_selected.set_name("input-view__num-button--selected")

        # variance_check_button / self.submit_button
        else:
            if self.index == 0:
                self.index = 1
                self.variance_check_button.set_name("input-view__check-button")
                self.submit_button.set_name("submit-button--selected")

            else:
                self.index = 0
                self.variance_check_button.set_name("input-view__check-button--selected")
                self.submit_button.set_name("submit-button")

    def select(self):
        # entropy_entry
        if self.section == 0:
            # Finish input button selected
            if self.index == 10:
                self.num_buttons_container.get_children()[self.index].set_name("input-view__num-button")
                self.section = 1
                self.index = 0
                self.variance_check_button.set_name("input-view__check-button--selected")

            # Add selected digit to entropy_entry
            else:
                curr_value = self.entropy_entry.get_text()
                new_value = curr_value + str(self.index)
                self.entropy_entry.set_text(new_value)

        # variance_check_button / self.submit_button
        else:
            if self.index == 0:
                self.variance_check_button.set_active(not self.variance_check_button.get_active())
            else:
                self.submit_handler()

    def submit_handler(self):
        print(self.entropy_entry.get_text())
        print(self.variance_check_button.get_active())
        # Todo: Generate variance

        self.window.navigate_to(
            path="generate_seed_confirmation",
            data={
                "input": self.entropy_entry.get_text(),
                "variance": "1 2 3"
            }
        )
