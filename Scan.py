import socket      #socket: for network communication
import threading   #threading: to scan multiple ports faster

target = input("Enter target IP: ")
ports = [21, 22, 23, 25, 53, 80, 443, 8080] # You can add more ports as needed

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:         #Exception handling: to skip closed ports
        pass

for port in ports:
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

       #CLI input and output formatting
