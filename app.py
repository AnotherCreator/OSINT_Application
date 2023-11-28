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
