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
                   command=self.login).pack(side='left', padx=10, pady=10)

        # Exchange Rate Converter Button
        ttk.Button(self.btn_frame,
                   text='Exchange Rate Converter',
                   command=self.sign_up).pack(side='left', padx=10, pady=10)

    def login(self):
        CoinMarketCapFormPage(root).pack()
        self.destroy()

    def sign_up(self):
        ExchangeRateConverterFormPage(root).pack()
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

        # Coin Market Cap Button
        ttk.Button(self.btn_frame, text='Coin Market Cap', command=self.cancel).pack(side='left', padx=10, pady=10)

        # Exchange Rate Converter Button
        ttk.Button(self.btn_frame, text='Exchange Rate Converter', command=self.cancel).pack(side='left', padx=10, pady=10)

        # Country Data Button
        ttk.Button(self.btn_frame, text='Country Data', command=self.cancel).pack(side='left', padx=10, pady=10)

        # signup button
        (ttk.Button(self.btn_frame, text='Sign Up', command=self.cancel)
         .pack(side='left', padx=10, pady=10))

    def sign_up(self):
        print('Signed up')
        Login(root).pack()
        self.destroy()

    def cancel(self):
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

        # Coin Market Cap Button
        ttk.Button(self.btn_frame, text='Coin Market Cap', command=self.cancel).pack(side='left', padx=10, pady=10)

        # Exchange Rate Converter Button
        ttk.Button(self.btn_frame, text='Exchange Rate Converter', command=self.cancel).pack(side='left', padx=10,
                                                                                             pady=10)

        # Country Data Button
        ttk.Button(self.btn_frame, text='Country Data', command=self.cancel).pack(side='left', padx=10, pady=10)

        # signup button
        (ttk.Button(self.btn_frame, text='Sign Up', command=self.cancel)
         .pack(side='left', padx=10, pady=10))

    def sign_up(self):
        print('Signed up')
        Login(root).pack()
        self.destroy()

    def cancel(self):
        Login(root).pack()
        self.destroy()


root = ttk.Window("OSINT Application", "superhero", resizable=(False, False))
Login(root).pack()
root.mainloop()
