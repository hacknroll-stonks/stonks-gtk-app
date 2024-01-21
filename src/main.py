import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from views import home_view
from views.wallets import wallets_view, wallet_address_view
from views.generate_seed import generate_seed_confirmation_view, seed_view, generate_seed_input_view
from views.payments import payment


# from gpio import buttons, keyboard

class Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="Stonks")
        self.set_default_size(1920, 1080)

        self.add_css("styles/style.css")

        # Connect window's delete event to terminate application
        self.connect("destroy", Gtk.main_quit)

        # Render Home view on new window initialization
        self.add(home_view.HomeView(self))
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
        # self.remove(self.get_child())
        self.get_child().destroy()

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

        elif path == "payment":
            fake_data = {
                "transaction_id": "123",
                "address_from": "123",
                "address_to": "123",
                "value": "123",
                "fee": "123"
            }
            self.add(payment.PaymentView(self, fake_data))

        self.show_all()


if __name__ == "__main__":
    # Create window
    win = Window()
    # buttons.bind_buttons(win)
    # keyboard.bind(win)

    # Start GTK+ processing loop
    Gtk.main()

