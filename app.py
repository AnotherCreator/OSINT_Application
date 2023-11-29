from tkinter import Tk, Frame, Button, Entry, Label
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Login(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.parent = parent

        # form header
        hdr_txt = "Select the API you would like to use"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # data frame
        self.data_frame = Frame(self)
        self.data_frame.pack(pady=10)

        # button frame
        self.btn_frame = Frame(self)
        self.btn_frame.pack()

        # Coin Market Cap Button
        (ttk.Button(self.btn_frame,
                    text='Coin Market Cap',  # Button name
                    # Function that button executes on press - only use function name without ending '()'
                    command=self.coin_market_cap_btn_press)
         .pack(side='left', padx=10, pady=10))

        # Exchange Rate Converter Button
        (ttk.Button(self.btn_frame,
                    text='Exchange Rate Converter',
                    command=self.exchange_rate_converter_btn_press)
         .pack(side='left', padx=10, pady=10))

        # Country Data Button
        (ttk.Button(self.btn_frame,
                    text='Country Data',
                    command=self.country_data_btn_press)
         .pack(side='left', padx=10, pady=10))

        # API 4 Button
        (ttk.Button(self.btn_frame,
                    text='API 4',
                    command=self.api4)
         .pack(side='left', padx=10, pady=10))

    # Functions that execute when user clicks any of the API selectors on the main menu
    def coin_market_cap_btn_press(self):
        self.destroy()  # This will 'destroy' the current frame, in this case, the API selection page on API press
        CoinMarketCapFormPage(root).pack()  # This will call the respective API frame to create a new page

    def exchange_rate_converter_btn_press(self):
        self.destroy()
        ExchangeRateConverterFormPage(root).pack()

    def country_data_btn_press(self):
        self.destroy()
        ExchangeRateConverterFormPage(root).pack()

    def api4(self):
        self.destroy()
        api4(root).pack()


class CoinMarketCapFormPage(ttk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent

        # Form Variables
        # Will use 'Bitcoin / BTC / 1' as default values unless changes by user in the
        # '# form entries' section
        self.coin_full_name = ttk.StringVar(value="Bitcoin")
        self.coin_abbreviation = ttk.StringVar(value="BTC")
        self.coin_number_ranking = ttk.IntVar(value=1)

        # form header
        hdr_txt = "Get Coin Data using either it's full name, abbreviation, or ranking"
        hdr = ttk.Label(master=self, text=hdr_txt)
        hdr.pack(fill=X, pady=10)

        # data frame
        self.data_frame = Frame(self)
        self.data_frame.pack(pady=10)

        # form entries
        self.create_form_entry("Crypto Coin Full Name", self.coin_full_name)
        self.create_form_entry("Crypto Coin Abbreviation", self.coin_abbreviation)
        self.create_form_entry("Crypto Coin Ranking", self.coin_number_ranking)

        # button frame
        self.btn_frame = Frame(self)
        self.btn_frame.pack()

        # Back Button
        ttk.Button(self.btn_frame, text='Back',
                   command=self.back).pack(side='left', padx=10, pady=10)

        # Submit button
        ttk.Button(self.btn_frame, text='Submit',
                   command=self.submit).pack(side='left', padx=10, pady=10)

    # Form entry styling
    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title())
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    # INSERT ANY API ACTIONS WITHIN THE FOLLOWING 'submit' FUNCTION
    def submit(self):
        print("Crypto Coin Full Name:", self.coin_full_name.get())
        print("Crypto Coin Abbreviation:", self.coin_abbreviation.get())
        print("Crypto Coin Ranking:", self.coin_number_ranking.get())

        self.destroy()
        Login(root).pack()

    # Return to the API selector page
    def back(self):
        self.destroy()
        Login(root).pack()


class ExchangeRateConverterFormPage(ttk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent

        # data frame
        self.data_frame = Frame(self)
        self.data_frame.pack(pady=10)

        # username:
        Label(self.data_frame, text='Test:').pack()
        # username entry
        self.username = Entry(self.data_frame)
        self.username.pack()

        # password:
        Label(self.data_frame, text='Password:').pack()
        # password entry
        self.password = Entry(self.data_frame)
        self.password.pack()

        # button frame
        self.btn_frame = Frame(self)
        self.btn_frame.pack()

        # Back Button
        ttk.Button(self.btn_frame, text='Back',
                   command=self.back).pack(side='left', padx=10, pady=10)

        # Submit button
        ttk.Button(self.btn_frame, text='Submit',
                   command=self.submit).pack(side='left', padx=10, pady=10)

    # INSERT ANY API ACTIONS WITHIN THE FOLLOWING 'submit' FUNCTION
    def submit(self):
        self.destroy()
        Login(root).pack()

    # Return to the API selector page
    def back(self):
        self.destroy()
        Login(root).pack()


class CountryDataFormPage(ttk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent

        # data frame
        self.data_frame = Frame(self)
        self.data_frame.pack(pady=10)

        # username:
        Label(self.data_frame, text='Test:').pack()
        # username entry
        self.username = Entry(self.data_frame)
        self.username.pack()

        # password:
        Label(self.data_frame, text='Password:').pack()
        # password entry
        self.password = Entry(self.data_frame)
        self.password.pack()

        # button frame
        self.btn_frame = Frame(self)
        self.btn_frame.pack()

        # Back Button
        ttk.Button(self.btn_frame, text='Back',
                   command=self.back).pack(side='left', padx=10, pady=10)

        # Submit button
        ttk.Button(self.btn_frame, text='Submit',
                   command=self.submit).pack(side='left', padx=10, pady=10)

    # INSERT ANY API ACTIONS WITHIN THE FOLLOWING 'submit' FUNCTION
    def submit(self):
        self.destroy()
        Login(root).pack()

    # Return to the API selector page
    def back(self):
        self.destroy()
        Login(root).pack()


class api4(ttk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.parent = parent

        # data frame
        self.data_frame = Frame(self)
        self.data_frame.pack(pady=10)

        # username:
        Label(self.data_frame, text='Test:').pack()
        # username entry
        self.username = Entry(self.data_frame)
        self.username.pack()

        # password:
        Label(self.data_frame, text='Password:').pack()
        # password entry
        self.password = Entry(self.data_frame)
        self.password.pack()

        # button frame
        self.btn_frame = Frame(self)
        self.btn_frame.pack()

        # Back Button
        ttk.Button(self.btn_frame, text='Back',
                   command=self.back).pack(side='left', padx=10, pady=10)

        # Submit button
        ttk.Button(self.btn_frame, text='Submit',
                   command=self.submit).pack(side='left', padx=10, pady=10)

    # INSERT ANY API ACTIONS WITHIN THE FOLLOWING 'submit' FUNCTION
    def submit(self):
        self.destroy()
        Login(root).pack()

    # Return to the API selector page
    def back(self):
        self.destroy()
        Login(root).pack()


if __name__ == "__main__":
    root = ttk.Window("OSINT Application", "superhero", resizable=(False, False))
    Login(root).pack()
    root.mainloop()
