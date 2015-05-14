__author__ = 'jamesma'

import asyncore
import socket
from cStringIO import StringIO
import logging

class SocketClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.read_buffer = StringIO()
        self.logger = logging.getLogger()
        self.write_buffer = ""
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.set_reuse_addr()
        #self.bind((host, port))
        #self.listen(5)
        self.output_handler = None
        self.connect((host, port))

    def write_to_buffer(self, msg):
        self.write_buffer = msg

    def append_to_buffer(self, msg):
        self.write_buffer += msg

    def __write_buffer_n_send__(self, command):
        self.write_to_buffer(command)
        asyncore.loop(timeout=1, count=1)

    def handle_connect(self):
        #print('handle_connect()')
        return

    def handle_close(self):
        print('Server closed connection.')
        self.close()

    def writable(self):
        is_writable = (len(self.write_buffer) > 0)
        #if is_writable:
            #print('writable() -> %s', is_writable)
        return is_writable

    def readable(self):
        #print('readable() -> True')
        return True

    def handle_write(self):
        sent = self.send(self.write_buffer)
        #print "handle_write() -> ", self.write_buffer[:sent]
        self.write_buffer = self.write_buffer[sent:]

    def handle_read(self):
        data = self.recv(8192)
        #print 'handle_read()->%d bytes' % len(data), ":", data
        #self.read_buffer.write(data)
        if self.output_handler is not None:
            self.output_handler(data)

    def shutdown(self):
        self.write_buffer = ""
        self.close()

    def set_data_handler(self, handler):
        self.output_handler = handler

    @staticmethod
    def loop():
        asyncore.loop()