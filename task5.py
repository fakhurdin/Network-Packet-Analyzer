import tkinter as tk
from tkinter import scrolledtext
import threading
import scapy.all as scapy
from scapy.layers import http

def sniff_packet(packet_list):
    try:
        while capture_flag:
            packet = scapy.sniff(count=1)[0]
            update_list(packet, packet_list)
    except Exception as e:
        print(f"An error occurred while sniffing packet: {e}")

def update_list(packet, packet_list):
    try:
        if packet.haslayer(http.HTTPRequest):
            info = f"HTTP Request: {packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path}"
        else:
            info = f"Src: {packet[scapy.IP].src} -> Dst: {packet[scapy.IP].dst}  Protocol: {packet.getlayer(scapy.IP).proto}"
        packet_list.insert(tk.END, info + "\n")
    except Exception as e:
        print(f"An error occurred while updating packet list: {e}")

def start_capture(packet_list):
    global capture_flag
    capture_flag = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    capture_thread = threading.Thread(target=sniff_packet, args=(packet_list,), daemon=True)
    capture_thread.start()

def stop_capture():
    global capture_flag
    capture_flag = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Network Packet Analyzer")

start_button = tk.Button(root, text="Start Capture", command=lambda: start_capture(packet_list))
stop_button = tk.Button(root, text="Stop Capture", command=stop_capture, state=tk.DISABLED)

packet_list = scrolledtext.ScrolledText(root)

# Layout
start_button.pack()
stop_button.pack()
packet_list.pack()

capture_flag = False  # Flag to control packet capture

root.mainloop()
