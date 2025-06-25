import asyncio
import threading
import tkinter as tk
from tkinter import messagebox
from bleak import BleakScanner, BleakClient

class BluetoothApp:
    def __init__(self, master):
        self.master = master
        master.title("ESP32 Bluetooth Connector")
        master.geometry("400x400")

        self.devices = []
        self.device_dict = {}
        self.selected_device = None
        self.client = None

        self.scan_button = tk.Button(master, text="Scan for Devices", command=self.start_scan)
        self.scan_button.pack(pady=10)

        self.device_listbox = tk.Listbox(master, width=50)
        self.device_listbox.pack(pady=10)
        self.device_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.connect_button = tk.Button(master, text="Connect", command=self.connect_device, state=tk.DISABLED)
        self.connect_button.pack(pady=10)

        self.status_label = tk.Label(master, text="Status: Not connected")
        self.status_label.pack(pady=10)

    def start_scan(self):
        self.status_label.config(text="Status: Scanning...")
        self.device_listbox.delete(0, tk.END)
        self.devices = []
        self.device_dict = {}
        threading.Thread(target=self.scan_devices, daemon=True).start()

    def scan_devices(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        devices = loop.run_until_complete(BleakScanner.discover(timeout=5.0))
        self.devices = devices
        self.device_dict = {f"{d.name or 'Unknown'} [{d.address}]": d for d in devices}
        self.master.after(0, self.update_device_list)

    def update_device_list(self):
        self.device_listbox.delete(0, tk.END)
        for name in self.device_dict:
            self.device_listbox.insert(tk.END, name)
        self.status_label.config(text="Status: Scan complete")

    def on_select(self, event):
        selection = self.device_listbox.curselection()
        if selection:
            device_name = self.device_listbox.get(selection[0])
            self.selected_device = self.device_dict[device_name]
            self.connect_button.config(state=tk.NORMAL)
        else:
            self.selected_device = None
            self.connect_button.config(state=tk.DISABLED)

    def connect_device(self):
        if self.selected_device:
            self.status_label.config(text="Status: Connecting...")
            threading.Thread(target=self._connect, daemon=True).start()

    def _connect(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            client = BleakClient(self.selected_device.address, loop=loop)
            loop.run_until_complete(client.connect())
            if client.is_connected:
                self.client = client
                self.master.after(0, lambda: self.status_label.config(text=f"Status: Connected to {self.selected_device.name or self.selected_device.address}"))
            else:
                self.master.after(0, lambda: self.status_label.config(text="Status: Connection failed"))
        except Exception as e:
            self.master.after(0, lambda: messagebox.showerror("Connection Error", str(e)))
            self.master.after(0, lambda: self.status_label.config(text="Status: Connection failed"))

if __name__ == "__main__":
    root = tk.Tk()
    app = BluetoothApp(root)
    root.mainloop() 