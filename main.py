from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import socket
#import sys

class TestApp(App):
    def __init__(self):
        App.__init__(self)
        self.l = ""
        self.showData = ""

    def build(self):
        layout = FloatLayout()

        connectbtn = Button(text="Connect", pos_hint={'center_x': 0.2, 'center_y': 0.9},
                                size_hint=(.15, .1), on_press=self.cconnect)
        layout.add_widget(connectbtn)

        disconnectbtn = Button(text="Disconnect", pos_hint={'center_x': 0.8, 'center_y': 0.9},
                                size_hint=(.15, .1), on_press=self.cdisconnect)
        layout.add_widget(disconnectbtn)

        upbtn = Button(text='Up', font_size=20, pos_hint={'center_x': 0.5, 'center_y': 0.65},
                        size_hint=(.1, .1), on_press=self.up_press)
        layout.add_widget(upbtn)

        dwnbtn = Button(text='Down', font_size=20, pos_hint={'center_x': 0.5, 'center_y': 0.35},
                            size_hint=(.1, .1), on_press=self.dwn_press)
        layout.add_widget(dwnbtn)

        rbtn = Button(text='Right', font_size=20, pos_hint={'center_x': 0.65, 'center_y': 0.5},
                    size_hint=(.1, .1), on_press=self.r_press)
        layout.add_widget(rbtn)

        lbtn = Button(text='Left', font_size=20, pos_hint={'center_x': 0.35, 'center_y': 0.5},
                    size_hint=(.1, .1), on_press=self.l_press)
        layout.add_widget(lbtn)
        return layout

    def cconnect(self, obj):
        try:
            # Create a TCP/IP socket for client
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            self.server_address = ('localhost', 10000)
            self.client.connect(self.server_address)
            print("Connecting to localhost, port 10000")
            self.showData = "Connected !"
            Clock.schedule_interval(self.send_client, 0.3)
        except:
            self.showData = "Cannot Connect to Server.."
            print("Cannot Connect to Server..")

    def cdisconnect(self, obj):
        Clock.unschedule(self.send_client)
        self.client.close()
        self.showData = "Not Connected to server.."
        print("Disconnected from the Server..")

    def up_press(self, obj):
        #l.append(+1)
        self.l = 'U'
        print('Up button is pressed')

    def dwn_press(self, obj):
        #l.append(-1)
        self.l = 'D'
        print('Down button is pressed')

    def r_press(self, obj):
        #l.append(+2)
        self.l = 'R'
        print('Right button is pressed')

    def l_press(self, obj):
        #l.append(-2)
        self.l = 'L'
        print('Left button is pressed')

    def send_client(self,obj):
        val = ""
        if self.l == "":
            val = "Q"
        else :
            val = self.l
        self.l = ""
        try:
            print("Sending Message", val)
            # Send string as bytes to server
            self.client.sendall(str.encode(val))
        except:
            self.showData = "Error while sending data to server.."
            print("Error while sending data to server..")

TestApp().run()
