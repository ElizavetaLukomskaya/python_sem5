from kivymd.app import MDApp

from build import Controller
from train_base import CustomContentHandler, ParserToFile, TrainBase
from datetime import datetime

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Controller()

    def build(self):
        handler = CustomContentHandler()
        ptf = ParserToFile()
        train_base = TrainBase(self.controller)
        train_base.set_from_file(handler, "test_minidom.xml")
        ptf.push_inf(train_base, "test_minidom.xml")
        return self.controller.get_screen()


MyApp().run()