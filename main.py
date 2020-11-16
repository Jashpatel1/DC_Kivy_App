from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
import socket
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# import sys
# class MyButton(Button):
#     def on_release(self):
#         new_button = Button(text = 'hello')
#         self.ids.float_1.add_widget(new_button)

class TestApp(App):
    def __init__(self):
        App.__init__(self)
        self.l = ""
        self.showData = ""
        self.flag = False
        self.layout = FloatLayout()
        self.new_button = Button(background_color = (0,0,0,0),text = 'Connected to Server!',color = (0,0,0,1),pos_hint = {'center_x': 0.5, 'center_y' : 0.8},size_hint= (.20,.1))
        self.serverError = Button(background_color=(0, 0, 0, 0), text='Cannot connect to Server!', color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(.20, .1))
        self.serverDisconnected = Button(background_color=(0, 0, 0, 0), text='Disconnected from Server!', color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(.20, .1))
        self.img =  Image(source = 'bground.jpg',allow_stretch = True, keep_ratio = True)

    def build(self):
        #layout = FloatLayout()
        #layout2 = FloatLayout()
        #new_button = Button(text = 'hello',pos_hint = {'center_x': 0.5, 'center_y' : 0.9},size_hint= (.15,.1))
        self.layout.add_widget(self.img)
        connectbtn = Button(background_color = (255,255,0,0.4),text="Connect", pos_hint={'center_x': 0.2, 'center_y': 0.8},
                            size_hint=(.15, .1), on_press=self.cconnect,on_release = self.ccnn)
        self.layout.add_widget(connectbtn)

        disconnectbtn = Button(background_color = (255,255,0,0.4),text="Disconnect",pos_hint={'center_x': 0.8, 'center_y': 0.8},
                               size_hint=(.15, .1), on_press=self.cdisconnect)
        self.layout.add_widget(disconnectbtn)

        upbtn = Button(background_color = (0,0,0,0.7),text='Up', font_size=20, pos_hint={'center_x': 0.5, 'center_y': 0.45},
                       size_hint=(.1, .1), on_press=self.up_press)
        self.layout.add_widget(upbtn)

        dwnbtn = Button(background_color = (0,0,0,0.7),text='Down', font_size=20, pos_hint={'center_x': 0.5, 'center_y': 0.15},
                        size_hint=(.1, .1), on_press=self.dwn_press)
        self.layout.add_widget(dwnbtn)

        rbtn = Button(background_color = (0,0,0,0.7),text='Right', font_size=20, pos_hint={'center_x': 0.65, 'center_y': 0.3},
                      size_hint=(.1, .1), on_press=self.r_press)
        self.layout.add_widget(rbtn)

        lbtn = Button(background_color = (0,0,0,0.7),text='Left', font_size=20, pos_hint={'center_x': 0.35, 'center_y': 0.3},
                      size_hint=(.1, .1), on_press=self.l_press)
        self.layout.add_widget(lbtn)
        return self.layout

    def ccnn(self, obj):
        self.flag = True

    def cconnect(self, obj):
        try:
            # Create a TCP/IP socket for client
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            self.server_address = ('192.168.0.104', 10000)
            self.client.connect(self.server_address)
            print("Connecting to localhost, port 10000")
            # conn = Label(text="Connected")
            self.layout.remove_widget(self.serverDisconnected)
            self.layout.remove_widget(self.serverError)
            self.layout.add_widget(self.new_button)
            Clock.schedule_interval(self.send_client, 0.3)
        except:
            self.layout.remove_widget(self.new_button)
            self.layout.remove_widget(self.serverDisconnected)
            self.layout.add_widget(self.serverError)
            print("Cannot Connect to Server..")

    def cdisconnect(self, obj):
        Clock.unschedule(self.send_client)
        self.client.close()
        self.showData = "Not Connected to server.."
        self.layout.remove_widget(self.new_button)
        self.layout.remove_widget(self.serverError)
        self.layout.add_widget(self.serverDisconnected)
        print("Disconnected from the Server..")

    def up_press(self, obj):
        # l.append(+1)
        self.l = 'U'
        print('Up button is pressed')

    def dwn_press(self, obj):
        # l.append(-1)
        self.l = 'D'
        print('Down button is pressed')

    def r_press(self, obj):
        # l.append(+2)
        self.l = 'R'
        print('Right button is pressed')

    def l_press(self, obj):
        # l.append(-2)
        self.l = 'L'
        print('Left button is pressed')

    def send_client(self, obj):
        val = ""
        if self.l == "":
            val = "Q"
        else:
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