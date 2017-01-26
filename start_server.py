from datawarehouse.server import main
from threading import Thread

class nod():
    def __init__(self, port):
        self.port=port
        self.thread1 = Thread(target=self.pornire)

    def pornire(self):
        if __name__ == '__main__':
            main(port_server=self.port)

    def run(self):
        self.thread1.start()

    def stop(self):
        self.thread1.join()

nodes = [nod(7777), nod(8888), nod(9999)]

for node in nodes:
    node.run()
for node in nodes:
    node.stop()
