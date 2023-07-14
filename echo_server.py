import socket
from marvelmind import MarvelmindHedge
import sys

HOST = "192.168.88.48"
PORT = 65432

def main():
    hedge = MarvelmindHedge(tty = "COM13", adr=61, baud=115200)
    if (len(sys.argv) > 1):
        hedge.tty = sys.argv[1]
    hedge.start()  # start thread

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        try:
            conn, addr = s.accept()

            with conn:
                print(f"Connected by {addr}")
                while True:
                    try:
                        data = ''
                        hedge.dataEvent.wait(1)
                        hedge.dataEvent.clear()

                        if (hedge.positionUpdated):
                            data_m = hedge.position()
                            echo_client = conn.recv(1024)
                            if not echo_client:
                                break
                            for dat in data_m:
                                print(dat)
                                data += str(dat)
                                data += ' '
                        conn.sendall(data.encode('utf-8'))

                    except KeyboardInterrupt:
                        hedge.stop()  # stop and close serial port
                        sys.exit()
        except:
            hedge.stop()  # stop and close serial port
            sys.exit()
            conn.close()
            s.close()
            print('Session stop')

    hedge.stop()  # stop and close serial port
    sys.exit()
    conn.close()
    s.close()
    print('Session stop')

main()

