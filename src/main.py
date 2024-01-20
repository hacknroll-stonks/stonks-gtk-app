import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from views import home_view


class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Stonks")
        # self.set_default_size(2360, 1460)
        self.set_default_size(400, 300)

        self.add_css("styles/style.css")

        # Render Home view on new window initialization
        self.add(home_view.HomeView(self))

    @staticmethod
    def add_css(css_file_path):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        provider.load_from_path(css_file_path)

    def navigate_to(self, widget, child, path):
        self.remove(child)

        match path:
            case "generate_seed_input":
                vbox = Gtk.Box(
                    orientation=Gtk.Orientation.VERTICAL,
                    spacing=0
                )

                vbox.pack_start(child=Gtk.Button(label="generate_seed_input"), expand=True, fill=True, padding=0)
                self.add(vbox)

            case "wallets":
                self.add(home_view.HomeView(self))

        self.show_all()


if __name__ == "__main__":
    # Create window
    win = Window()

    # Connect window's delete event to terminate application
    win.connect("destroy", Gtk.main_quit)

    # Display window
    win.show_all()

    # Start GTK+ processing loop
    Gtk.main()

