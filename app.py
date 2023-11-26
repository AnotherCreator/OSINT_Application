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
        ttk.Button(self.btn_frame,
                   text='Coin Market Cap',
                   command=self.coin_market_cap_btn_press).pack(side='left', padx=10, pady=10)

        # Exchange Rate Converter Button
        ttk.Button(self.btn_frame,
                   text='Exchange Rate Converter',
                   command=self.exchange_rate_converter_btn_press).pack(side='left', padx=10, pady=10)

        # Country Data Button
        ttk.Button(self.btn_frame,
                   text='Country Data',
                   command=self.exchange_rate_converter_btn_press).pack(side='left', padx=10, pady=10)

        # API 4 Button
        ttk.Button(self.btn_frame,
                   text='API 4',
                   command=self.exchange_rate_converter_btn_press).pack(side='left', padx=10, pady=10)

    def coin_market_cap_btn_press(self):
        CoinMarketCapFormPage(root).pack()
        self.destroy()

    def exchange_rate_converter_btn_press(self):
        ExchangeRateConverterFormPage(root).pack()
        self.destroy()

    def country_data_btn_press(self):
        ExchangeRateConverterFormPage(root).pack()
        self.destroy()

    def api4(self):
        api4(root).pack()
        self.destroy()


class CoinMarketCapFormPage(ttk.Frame):
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
        Login(root).pack()
        self.destroy()

    # Return to the API selector page
    def back(self):
        Login(root).pack()
        self.destroy()


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
        Login(root).pack()
        self.destroy()

    # Return to the API selector page
    def back(self):
        Login(root).pack()
        self.destroy()


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
        Login(root).pack()
        self.destroy()

    # Return to the API selector page
    def back(self):
        Login(root).pack()
        self.destroy()


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
        Login(root).pack()
        self.destroy()

    # Return to the API selector page
    def back(self):
        Login(root).pack()
        self.destroy()


if __name__ == "__main__":
    root = ttk.Window("OSINT Application", "superhero", resizable=(False, False))
    Login(root).pack()
    root.mainloop()
