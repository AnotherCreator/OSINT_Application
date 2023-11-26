import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# DataEntryForm design template provided by https://ttkbootstrap.readthedocs.io/en/latest/gallery/dataentry/
# Modified design template to fit the implementation of 4 APIs selected by our group
class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # Form API Selector Buttons
        # api1_button = ttk.Button(app, text="Coin Market Cap", bootstyle=(SUCCESS, OUTLINE))
        # api1_button.pack(side=LEFT, padx=5, pady=10)
        #
        # api2_button = ttk.Button(app, text="Exchange Rate Converter", bootstyle=(SUCCESS, OUTLINE))
        # api2_button.pack(side=LEFT, padx=5, pady=10)
        #
        # api3_button = ttk.Button(app, text="Country Data", bootstyle=(SUCCESS, OUTLINE))
        # api3_button.pack(side=LEFT, padx=5, pady=10)
        #
        # api4_button = ttk.Button(app, text="API 4", bootstyle=(SUCCESS, OUTLINE))
        # api4_button.pack(side=LEFT, padx=5, pady=10)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

        # form header
        # hdr_txt = "Please enter your contact information"
        # hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        # hdr.pack(fill=X, pady=10)

        # form entries
        self.create_api_buttons()
        self.create_form_entry("name", self.name)
        self.create_form_entry("address", self.address)
        self.create_form_entry("phone", self.phone)
        self.create_buttonbox()

    # These 4 buttons will correspond to each API data source being used in this project
    # When a button is pressed, it should display their own specific data entry forms required for the API
    # to send back a proper response
    #
    # When the 'submit' button is pressed, the data inside the forms will be sent in the format required by the API
    # and will be received by the app to properly display in the GUI
    def on_coin_market_cap_button_press(self):
        return

    def on_exchange_rate_converter_button_press(self):
        return

    def on_country_data_button_press(self):
        return

    def on_api4_button_press(self):
        return

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_api_buttons(self):
        """Create the API selector buttonboxes"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        coin_market_cap_btn = ttk.Button(
            master=container,
            text="Coin Market Cap API",
            command=self.on_coin_market_cap_button_press(),
            bootstyle=(PRIMARY, OUTLINE)
        )
        coin_market_cap_btn.pack(side=LEFT, padx=5)

        exchange_rate_converter_btn = ttk.Button(
            master=container,
            text="Exchange Rate Converter",
            command=self.on_exchange_rate_converter_button_press(),
            bootstyle=(PRIMARY, OUTLINE)
        )
        exchange_rate_converter_btn.pack(side=LEFT, padx=5)

        country_data_btn = ttk.Button(
            master=container,
            text="Exchange Rate Converter",
            command=self.on_country_data_button_press(),
            bootstyle=(PRIMARY, OUTLINE)
        )
        country_data_btn.pack(side=LEFT, padx=5)

        api4_btn = ttk.Button(
            master=container,
            text="API4",
            command=self.on_api4_button_press(),
            bootstyle=(PRIMARY, OUTLINE)
        )
        api4_btn.pack(side=LEFT, padx=5)

    # Create the "Submit" and "Cancel" buttons to send data to the API or to completely quit the application
    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Quit",
            command=self.on_quit,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        print("Name:", self.name.get())
        print("Address:", self.address.get())
        print("Phone:", self.phone.get())
        return self.name.get(), self.address.get(), self.phone.get()

    def on_quit(self):
        """Cancel and close the application."""
        self.quit()


if __name__ == "__main__":
    app = ttk.Window("OSINT Application", "superhero", resizable=(False, False))

    DataEntryForm(app)
    app.mainloop()
