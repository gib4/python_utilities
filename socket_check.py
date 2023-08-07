import socket
import psutil

def is_rdp_active(host, port):
    # Check if the RDP port is listening
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    sock.close()

    if result != 0:
        print(f"Connection to {host}:{port} unsuccessful. RDP is not active.")
        return False

    # Check for active RDP sessions
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'winlogon.exe':
            try:
                session_id = int(proc.info['pid'])
                if session_id > 0:
                    print(f"An active RDP session (ID: {session_id}) is detected.")
                    return True
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass

    print("No active RDP sessions detected.")
    return False

# Usage
is_rdp_active('10.120.4.1', 3389)  # Replace with the target machine's IP address and RDP port number
