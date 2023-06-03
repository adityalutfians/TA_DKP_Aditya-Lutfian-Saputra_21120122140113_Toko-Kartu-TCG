from tkinter import *
from tkinter import messagebox


class PokemonTCGShop:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pokemon TCG Card Shop")
        self.root.geometry("400x320")
        self.root.config(background="#ffcb05")

        self.jenis_box = ["Silver Tempest", "Vivid Voltage", "Lost Origin", "Shining Fates"]
        self.harga_box = [2700000, 1200000, 3300000, 1800000]
        self.pilih_box = StringVar()
        self.pilih_box.set(self.jenis_box[0])
        self.banyak_box = IntVar()
        self.metode_bayar = StringVar()
        self.metode_bayar.set("Transfer Bank")


        self.label_judul = Label(self.root, 
                                 text="Pokemon TCG Card Shop", 
                                 font=("Times New Roman", 16),
                                 bg="#ffcb05"
                                )
        self.label_judul.pack(pady=10)


        self.label_box = Label(self.root, 
                               text="Pilih Jenis Box:", 
                               font=("Arial", 10),
                               bg="#ffcb05"
                              )
        self.label_box.pack(pady=5)


        self.menu_box = OptionMenu(self.root, self.pilih_box, *self.jenis_box)
        self.menu_box.config(bg="#c7a008",activebackground="#c7a008",highlightthickness=0)
        self.menu_box.pack()


        self.label_total = Label(self.root, 
                                 text="Jumlah Box:", 
                                 font=("Arial", 10),
                                 bg="#ffcb05"
                                )
        self.label_total.pack(pady=5)


        self.entry_total = Entry(self.root, textvariable=self.banyak_box, bg="#c7a008")
        self.entry_total.pack()


        self.label_pembayaran = Label(self.root, 
                                      text="Metode Pembayaran:", 
                                      font=("Arial", 10),
                                      bg="#ffcb05",
                                     )
        self.label_pembayaran.pack(pady=5)


        self.radiobutton_bank = Radiobutton(self.root, 
                                            text="Transfer Bank", 
                                            variable=self.metode_bayar, 
                                            value="Transfer Bank", 
                                            font=("Arial", 8),
                                            bg="#ffcb05",
                                            activebackground="#ffcb05"
                                           )
        self.radiobutton_bank.pack()


        self.radiobutton_cod = Radiobutton(self.root, 
                                           text="COD", 
                                           variable=self.metode_bayar, 
                                           value="COD", 
                                           font=("Arial", 8),
                                           bg="#ffcb05",
                                           activebackground="#ffcb05"
                                          )
        self.radiobutton_cod.pack()


        self.button_pesan = Button(self.root, 
                                   text="Pesan", 
                                   command=self.total_box_dipilih, 
                                   font=("Comic Sans", 10), 
                                   fg="#ffcb05", 
                                   bg="#2a75bb", 
                                   activebackground="#3c5aa6",
                                   activeforeground="#c7a008", 
                                  )
        self.button_pesan.pack(pady=10)


    def calculate_total_price(self):
        box_dipilih_index = self.jenis_box.index(self.pilih_box.get())
        price = self.harga_box[box_dipilih_index]
        total_price = self.banyak_box.get() * price
        return total_price 


    def total_box_dipilih(self):
        if self.banyak_box.get() <= 0:
            messagebox.showerror(title="Error", message="Jumlah pesanan box harus lebih besar dari 0!")
            return
        if self.banyak_box.get() > 5:
            messagebox.showinfo(title="info", message="Maaf, maksimal pembelian adalah 5 box")
            return


        harga = self.calculate_total_price()


        info_pembelian = messagebox.askyesno("Informasi box yang dibeli",
                                             f"Jenis box: {self.pilih_box.get()}\n"
                                             f"Jumlah box: {self.banyak_box.get()}\n"
                                             f"Metode Pembayaran: {self.metode_bayar.get()}\n"
                                             f"Total Harga: Rp.{harga}\n\n"
                                             "Apakah Anda ingin melanjutkan pembelian?")


        if info_pembelian == True:
            messagebox.showinfo(title="Informasi Pesanan", message="Pesanan berhasil diproses!")
            self.close_shop()
        else:
            self.reset_shop()


    def close_shop(self):
        for widget in self.root.winfo_children():
            widget.quit()


    def reset_shop(self):
        self.pilih_box.set(self.jenis_box[0])
        self.banyak_box.set(0)
        self.metode_bayar.set("Transfer Bank")


pokemon = PokemonTCGShop()
pokemon.root.mainloop()