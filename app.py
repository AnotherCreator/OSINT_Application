import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# DataEntryForm design template provided by https://ttkbootstrap.readthedocs.io/en/latest/gallery/dataentry/
# Modified design template to fit the implementation of 4 APIs selected by our group
class APISelectorPage(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form header
        hdr_txt = "Select the API you would like to use"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_api_buttons()

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
            bootstyle=(PRIMARY, OUTLINE)
        )
        coin_market_cap_btn.pack(side=LEFT, padx=5)

        exchange_rate_converter_btn = ttk.Button(
            master=container,
            text="Exchange Rate Converter",
            bootstyle=(PRIMARY, OUTLINE)
        )
        exchange_rate_converter_btn.pack(side=LEFT, padx=5)

        country_data_btn = ttk.Button(
            master=container,
            text="Exchange Rate Converter",
            bootstyle=(PRIMARY, OUTLINE)
        )
        country_data_btn.pack(side=LEFT, padx=5)

        api4_btn = ttk.Button(
            master=container,
            text="API4",
            bootstyle=(PRIMARY, OUTLINE)
        )
        api4_btn.pack(side=LEFT, padx=5)


###
#   Each class below (4 in total) will correspond to each 'frame' or 'page' that will be rendered by the GUI when
#   the user clicks on an API selector button in the GUI
#
#   Each class, or api form, will take in their respective data entry values required by the API in order to send back
#   a proper response
###
class CoinMarketCapFormPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

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


class ExchangeRateConverterFormPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

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


class CountryDataFormPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

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


class API4Page(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

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
    APISelectorPage(app)
    app.mainloop()
