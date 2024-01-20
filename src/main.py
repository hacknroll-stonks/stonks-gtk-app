import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from views import home_view, generate_seed_input_view, generate_seed_confirmation_view, seed_view, wallets_view, wallet_address_view
from gpio import buttons

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Stonks")
        # self.set_default_size(2360, 1460)
        self.set_default_size(400, 300)

        self.add_css("styles/style.css")

        # Connect window's delete event to terminate application
        self.connect("destroy", Gtk.main_quit)

        # Render Home view on new window initialization
        # self.add(home_view.HomeView(self))
        self.add(wallet_address_view.WalletAddressView(self, {"public_key": "1234"}))
        self.show_all()


    @staticmethod
    def add_css(css_file_path):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        provider.load_from_path(css_file_path)

    def navigate_to(self, path, data):
        self.remove(self.get_child())

        if path == "home":
            self.add(home_view.HomeView(self))

        elif path == "generate_seed_input":
            self.add(generate_seed_input_view.GenerateSeedInputView(self))

        elif path == "generate_seed_confirmation":
            self.add(generate_seed_confirmation_view.GenerateSeedConfirmationView(self, data))

        elif path == "seed":
            self.add(seed_view.SeedView(self, data))

        elif path == "wallets":
            self.add(wallets_view.WalletsView(self))

        elif path == "wallet_address":
            self.add(wallet_address_view.WalletAddressView(self, data))

        self.show_all()


if __name__ == "__main__":
    # Create window
    win = Window()
    buttons.bind_buttons(win)
    # Start GTK+ processing loop
    Gtk.main()

