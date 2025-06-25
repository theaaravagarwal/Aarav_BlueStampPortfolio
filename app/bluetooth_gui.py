import asyncio
import threading
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from bleak import BleakScanner, BleakClient
from bleak.backends.scanner import AdvertisementData

class BluetoothApp:
    def __init__(self, master):
        self.master = master
        master.title("ESP32 BLE Connector")
        master.geometry("800x800")

        self.devices = []
        self.device_dict = {}
        self.selected_device = None
        self.client = None
        self.connected = False
        self.notification_characteristic = None
        self.loop = None

        main_frame = tk.Frame(master)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        title_label = tk.Label(main_frame, text="ESP32 BLE Connector", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 10))
        
        instructions = tk.Label(main_frame, text="Look for devices with 'ESP32' in the name", font=("Arial", 10), fg="blue", wraplength=750)
        instructions.pack(pady=(0, 10))

        self.scan_button = tk.Button(main_frame, text="Scan for BLE Devices", command=self.start_scan, font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.RAISED)
        self.scan_button.pack(pady=10)

        filter_frame = tk.Frame(main_frame)
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(filter_frame, text="Filter:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar()
        self.filter_entry = tk.Entry(filter_frame, textvariable=self.filter_var, width=30)
        self.filter_entry.pack(side=tk.LEFT, padx=(5, 0))
        self.filter_var.trace_add('write', self.filter_devices)

        list_frame = tk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ('Name', 'Address', 'RSSI', 'Type', 'Services')
        self.device_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=8)
        
        self.device_tree.heading('Name', text='Device Name')
        self.device_tree.heading('Address', text='BLE Address')
        self.device_tree.heading('RSSI', text='Signal Strength')
        self.device_tree.heading('Type', text='Device Type')
        self.device_tree.heading('Services', text='Services')
        
        self.device_tree.column('Name', width=200)
        self.device_tree.column('Address', width=150)
        self.device_tree.column('RSSI', width=100)
        self.device_tree.column('Type', width=100)
        self.device_tree.column('Services', width=200)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.device_tree.yview)
        self.device_tree.configure(yscrollcommand=scrollbar.set)
        
        self.device_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.device_tree.bind('<<TreeviewSelect>>', self.on_select)

        connection_frame = tk.Frame(main_frame)
        connection_frame.pack(fill=tk.X, pady=10)
        
        self.connect_button = tk.Button(connection_frame, text="Connect", command=self.connect_device, state=tk.DISABLED, font=("Arial", 12), bg="#2196F3", fg="white")
        self.connect_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.disconnect_button = tk.Button(connection_frame, text="Disconnect", command=self.disconnect_device, state=tk.DISABLED, font=("Arial", 12), bg="#f44336", fg="white")
        self.disconnect_button.pack(side=tk.LEFT)

        comm_frame = tk.Frame(main_frame)
        comm_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(comm_frame, text="Send Message:").pack(side=tk.LEFT)
        self.message_var = tk.StringVar()
        self.message_entry = tk.Entry(comm_frame, textvariable=self.message_var, width=30)
        self.message_entry.pack(side=tk.LEFT, padx=(5, 5))
        
        self.send_button = tk.Button(comm_frame, text="Send", command=self.send_message, state=tk.DISABLED, font=("Arial", 10), bg="#4CAF50", fg="white")
        self.send_button.pack(side=tk.LEFT)

        received_frame = tk.Frame(main_frame)
        received_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        tk.Label(received_frame, text="Messages from ESP32:", font=("Arial", 11, "bold")).pack(anchor=tk.W)
        
        self.received_text = scrolledtext.ScrolledText(received_frame, height=8, width=80, font=("Courier", 10), bg="black", fg="green")
        self.received_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        clear_button = tk.Button(received_frame, text="Clear Messages", command=self.clear_messages,
                               font=("Arial", 10), bg="#FF9800", fg="white")
        clear_button.pack(pady=(5, 0))

        self.status_label = tk.Label(main_frame, text="Status: Not connected", font=("Arial", 11))
        self.status_label.pack(pady=10)

    def start_scan(self):
        self.status_label.config(text="Status: Scanning for BLE devices...")
        self.device_tree.delete(*self.device_tree.get_children())
        self.devices = []
        self.device_dict = {}
        self.scan_button.config(state=tk.DISABLED, text="Scanning...")
        threading.Thread(target=self.scan_devices, daemon=True).start()

    def scan_devices(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            devices = loop.run_until_complete(BleakScanner.discover(timeout=10.0))
            self.devices = devices
            self.device_dict = {f"{d.name or 'Unknown'} [{d.address}]": d for d in devices}
            self.master.after(0, self.update_device_list)
        except Exception as e:
            self.master.after(0, lambda: messagebox.showerror("Scan Error", f"Error during scan: {e}"))
            self.master.after(0, lambda: self.status_label.config(text="Status: Scan failed"))
            self.master.after(0, lambda: self.scan_button.config(state=tk.NORMAL, text="🔍 Scan for BLE Devices"))
        finally:
            loop.close()

    def update_device_list(self):
        self.device_tree.delete(*self.device_tree.get_children())
        esp32_count = 0
        
        for device in self.devices:
            name = device.name or "Unknown"
            address = device.address

            rssi = "N/A"
            if hasattr(device, 'advertisement') and device.advertisement:
                ad_data = device.advertisement
                if hasattr(ad_data, 'rssi'):
                    rssi = ad_data.rssi

            services = "N/A"
            if hasattr(device, 'advertisement') and device.advertisement:
                ad_data = device.advertisement
                if hasattr(ad_data, 'service_uuids') and ad_data.service_uuids:
                    services = ", ".join(ad_data.service_uuids[:2])
            
            device_type = "Unknown"
            if ("SMARTSOLE" in name.upper() or 
                "ESP32" in name.upper() or 
                "ESP" in name.upper() or
                name.upper().startswith("ESP")):
                device_type = "ESP32"
                esp32_count += 1
            elif "PHONE" in name.upper() or "IPHONE" in name.upper() or "ANDROID" in name.upper():
                device_type = "Phone"
            elif "WATCH" in name.upper() or "FITBIT" in name.upper():
                device_type = "Watch"
            elif "AIRPODS" in name.upper() or "HEADPHONES" in name.upper():
                device_type = "Audio"
            
            item = self.device_tree.insert('', tk.END, values=(name, address, rssi, device_type, services))
            
            if device_type == "ESP32":
                self.device_tree.set(item, 'Name', f"🎯 {name}")
        
        status_text = f"Status: Found {len(self.devices)} devices ({esp32_count} ESP32)"
        self.status_label.config(text=status_text)
        self.scan_button.config(state=tk.NORMAL, text="Scan for BLE Devices")

    def filter_devices(self, *args):
        filter_text = self.filter_var.get().lower()
        self.device_tree.delete(*self.device_tree.get_children())
        
        for device in self.devices:
            name = device.name or "Unknown"
            address = device.address
            
            rssi = "N/A"
            if hasattr(device, 'advertisement') and device.advertisement:
                ad_data = device.advertisement
                if hasattr(ad_data, 'rssi'):
                    rssi = ad_data.rssi
            
            services = "N/A"
            if hasattr(device, 'advertisement') and device.advertisement:
                ad_data = device.advertisement
                if hasattr(ad_data, 'service_uuids') and ad_data.service_uuids:
                    services = ", ".join(ad_data.service_uuids[:2])
            
            if (filter_text in name.lower() or 
                filter_text in address.lower() or 
                (filter_text in "esp" and ("esp" in name.lower() or "smartsole" in name.lower()))):
                
                device_type = "Unknown"
                if ("SMARTSOLE" in name.upper() or 
                    "ESP32" in name.upper() or 
                    "ESP" in name.upper() or
                    name.upper().startswith("ESP")):
                    device_type = "ESP32"
                elif "PHONE" in name.upper() or "IPHONE" in name.upper() or "ANDROID" in name.upper():
                    device_type = "Phone"
                elif "WATCH" in name.upper() or "FITBIT" in name.upper():
                    device_type = "Watch"
                elif "AIRPODS" in name.upper() or "HEADPHONES" in name.upper():
                    device_type = "Audio"
                
                item = self.device_tree.insert('', tk.END, values=(name, address, rssi, device_type, services))
                if device_type == "ESP32":
                    self.device_tree.set(item, 'Name', f"🎯 {name}")

    def on_select(self, event):
        selection = self.device_tree.selection()
        if selection:
            item = selection[0]
            values = self.device_tree.item(item, 'values')
            address = values[1]
            for device in self.devices:
                if device.address == address:
                    self.selected_device = device
                    break
            else:
                self.selected_device = None
            if self.selected_device and not self.connected:
                self.connect_button.config(state=tk.NORMAL)
        else:
            self.selected_device = None
            if not self.connected:
                self.connect_button.config(state=tk.DISABLED)

    def connect_device(self):
        if self.selected_device and not self.connected:
            self.status_label.config(text="Status: Connecting...")
            self.connect_button.config(state=tk.DISABLED, text="Connecting...")
            threading.Thread(target=self._connect, daemon=True).start()

    def _connect(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.loop = loop
        try:
            client = BleakClient(self.selected_device.address, loop=loop)
            loop.run_until_complete(client.connect())
            if client.is_connected:
                self.client = client
                self.connected = True
                
                loop.run_until_complete(self.discover_services())
                
                self.master.after(0, lambda: self.status_label.config(text=f"Status: Connected to {self.selected_device.name or self.selected_device.address}"))
                self.master.after(0, lambda: self.connect_button.config(state=tk.DISABLED, text="Connected"))
                self.master.after(0, lambda: self.disconnect_button.config(state=tk.NORMAL))
                self.master.after(0, lambda: self.send_button.config(state=tk.NORMAL))
                self.master.after(0, lambda: self.message_entry.config(state=tk.NORMAL))
            else:
                self.master.after(0, lambda: self.status_label.config(text="Status: Connection failed"))
                self.master.after(0, lambda: self.connect_button.config(state=tk.NORMAL, text="Connect"))
        except Exception as e:
            self.master.after(0, lambda: messagebox.showerror("Connection Error", str(e)))
            self.master.after(0, lambda: self.status_label.config(text="Status: Connection failed"))
            self.master.after(0, lambda: self.connect_button.config(state=tk.NORMAL, text="Connect"))

    def discover_services(self):
        async def _discover():
            try:
                services = await self.client.get_services()
                self.master.after(0, lambda: self.add_received_message("🔍 Discovering services..."))
                
                for service in services:
                    self.master.after(0, lambda s=service: self.add_received_message(f"Service: {s.uuid}"))
                    for char in service.characteristics:
                        self.master.after(0, lambda c=char: self.add_received_message(f"  Characteristic: {c.uuid} - Properties: {c.properties}"))
                        
                        if "notify" in char.properties or "indicate" in char.properties:
                            try:
                                await self.client.start_notify(char.uuid, self.notification_handler)
                                self.notification_characteristic = char.uuid
                                self.master.after(0, lambda uuid=char.uuid: self.add_received_message(f"✅ Notifications enabled for {uuid}"))
                            except Exception as e:
                                self.master.after(0, lambda uuid=char.uuid, error=e: self.add_received_message(f"❌ Failed to enable notifications for {uuid}: {error}"))
                
                if not self.notification_characteristic:
                    self.master.after(0, lambda: self.add_received_message("⚠️ No notification characteristics found"))
                    
            except Exception as e:
                self.master.after(0, lambda error=e: self.add_received_message(f"❌ Service discovery failed: {error}"))
        
        return _discover()

    def notification_handler(self, sender, data):
        try:
            message = data.decode('utf-8')
            self.master.after(0, lambda: self.add_received_message(f"📨 {message}"))
        except UnicodeDecodeError:
            hex_data = ' '.join([f'{b:02x}' for b in data])
            self.master.after(0, lambda: self.add_received_message(f"📨 [HEX] {hex_data}"))

    def disconnect_device(self):
        if self.client and self.connected:
            threading.Thread(target=self._disconnect, daemon=True).start()

    def _disconnect(self):
        try:
            if self.client and self.notification_characteristic and self.client.is_connected:
                try:
                    if self.loop:
                        future = asyncio.run_coroutine_threadsafe(
                            self.client.stop_notify(self.notification_characteristic), 
                            self.loop
                        )
                        future.result(timeout=5.0)
                except Exception:
                    pass
            
            if self.client and self.client.is_connected:
                if self.loop:
                    future = asyncio.run_coroutine_threadsafe(
                        self.client.disconnect(), 
                        self.loop
                    )
                    future.result(timeout=5.0)
            
            self.connected = False
            self.client = None
            self.notification_characteristic = None
            
            if self.loop:
                try:
                    self.loop.close()
                except Exception:
                    pass
                self.loop = None
            
            self.master.after(0, lambda: self.status_label.config(text="Status: Disconnected"))
            self.master.after(0, lambda: self.connect_button.config(state=tk.NORMAL, text="Connect"))
            self.master.after(0, lambda: self.disconnect_button.config(state=tk.DISABLED))
            self.master.after(0, lambda: self.send_button.config(state=tk.DISABLED))
            self.master.after(0, lambda: self.message_entry.config(state=tk.DISABLED))
            self.master.after(0, lambda: self.add_received_message("🔌 Disconnected from ESP32"))
            
        except Exception as disconnect_error:
            error_msg = str(disconnect_error)
            self.master.after(0, lambda: messagebox.showerror("Disconnect Error", error_msg))
            self.master.after(0, lambda: self.status_label.config(text="Status: Disconnect failed"))
            self.connected = False
            self.client = None
            self.notification_characteristic = None
            if self.loop:
                try:
                    self.loop.close()
                except Exception:
                    pass
                self.loop = None
            self.master.after(0, lambda: self.connect_button.config(state=tk.NORMAL, text="Connect"))
            self.master.after(0, lambda: self.disconnect_button.config(state=tk.DISABLED))
            self.master.after(0, lambda: self.send_button.config(state=tk.DISABLED))
            self.master.after(0, lambda: self.message_entry.config(state=tk.DISABLED))

    def send_message(self):
        if self.client and self.connected and self.message_var.get().strip():
            message = self.message_var.get().strip()
            threading.Thread(target=self._send_message, args=(message,), daemon=True).start()

    def _send_message(self, message):
        if not self.loop or not self.client or not self.connected:
            self.master.after(0, lambda: messagebox.showerror("Send Error", "Not connected to device"))
            return
            
        try:
            characteristic_uuids = [
                "beb5483e-36e1-4688-b7f5-ea07361b26a8",
                "0000ffe1-0000-1000-8000-00805f9b34fb",
                "0000ffe0-0000-1000-8000-00805f9b34fb",
            ]
            
            message_bytes = message.encode('utf-8')
            success = False
            
            for uuid in characteristic_uuids:
                try:
                    future = asyncio.run_coroutine_threadsafe(
                        self.client.write_gatt_char(uuid, message_bytes), 
                        self.loop
                    )
                    future.result(timeout=5.0)
                    success = True
                    self.master.after(0, lambda: self.add_received_message(f"📤 Sent via {uuid}: {message}"))
                    break
                except Exception as e:
                    self.master.after(0, lambda uuid=uuid, error=e: self.add_received_message(f"❌ Failed to send via {uuid}: {error}"))
                    continue
            
            if success:
                self.master.after(0, lambda: self.status_label.config(text=f"Status: Message sent: {message}"))
                self.master.after(0, lambda: self.message_var.set(""))
            else:
                self.master.after(0, lambda: messagebox.showerror("Send Error", "Failed to send message via any characteristic"))
            
        except Exception as send_error:
            error_msg = str(send_error)
            self.master.after(0, lambda: messagebox.showerror("Send Error", f"Failed to send message: {error_msg}"))

    def clear_messages(self):
        self.received_text.delete(1.0, tk.END)

    def add_received_message(self, message):
        print(f"DEBUG: {message}")
        self.received_text.insert(tk.END, f"[{self.get_timestamp()}] {message}\n")
        self.received_text.see(tk.END)

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def cleanup(self):
        """Clean up resources when closing the application"""
        if self.client and self.connected:
            try:
                if self.notification_characteristic and self.client.is_connected and self.loop:
                    try:
                        future = asyncio.run_coroutine_threadsafe(
                            self.client.stop_notify(self.notification_characteristic), 
                            self.loop
                        )
                        future.result(timeout=2.0)
                    except Exception:
                        pass
                
                if self.client.is_connected and self.loop:
                    try:
                        future = asyncio.run_coroutine_threadsafe(
                            self.client.disconnect(), 
                            self.loop
                        )
                        future.result(timeout=2.0)
                    except Exception:
                        pass
                
                if self.loop:
                    try:
                        self.loop.close()
                    except Exception:
                        pass
            except Exception:
                pass
            finally:
                self.connected = False
                self.client = None
                self.notification_characteristic = None
                self.loop = None

if __name__ == "__main__":
    root = tk.Tk()
    app = BluetoothApp(root)
    
    def on_closing():
        app.cleanup()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop() 