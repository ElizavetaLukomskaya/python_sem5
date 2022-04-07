from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivy.core.window import Window
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
import os
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from workscreen import WorkScreen
from kivymd.uix.label import MDLabel

Window.size = (800, 600)

class HomeScreen(Screen):
    pass

class WorkScreen(Screen):
    pass

class add_data_screen(Screen):
    pass

class remove_data_screen(Screen):
    pass

class search_data_screen(Screen):
    pass

class change_data_screen(Screen):
    pass

class error_screen(Screen):
    pass

class MainApp(MDApp):
    if os.path.isfile("profile_source.txt"):
        with open("profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "майк.jpg"
    else:
        img_source_path = "майк.jpg"

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style = 'Dark'

    def add_data(self, instance):
        print(self.add_data.text)
        self.add_data.bind(text=on_text)

    def on_text(instance, value):
        s = value,
        print(s)
    def remove_data(self, obj):
        print(self.add_data.text)

    def search_data(self, obj):
        print(self.add_data.text)

    def change_data(self, obj):
        print(self.add_data.text)

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    # def go_to_favorite_train(self):


    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

        if screen_name == 'home_screen':
            self.root.ids.titlename.title = 'Main'

        if screen_name == 'work_screen':
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = 'Train Schedule'
            #datatable_page = self.root.ids.work_screen.ids.datatable

            # try:
            #     for w in datatable_page.walk():
            #         if w.__class__ == WorkScreen:
            #             print("remove MD Data Table widget")
            #             datatable_page.remove_widget(w)
            #         else:
            #             print("No widget to remove")
            #             continue
            # except:
            #     print("Something is wrong")
            #     pass

            # Instantiate the road work data table
            #self.datatable = TrainSchedule(totaldata=self.total_trains_response)
            # Add train data table to the work screen
            #datatable_page.add_widget(self.datatable)

            if screen_name == 'add_data_screen':
                self.root.ids.titlename.title = 'Adding....'

            if screen_name == 'remove_data_screen':
                self.root.ids.titlename.title = 'Removing....'

            if screen_name == 'search_data_screen':
                self.root.ids.titlename.title = 'Searching....'

            if screen_name == 'change_data_screen':
                self.root.ids.titlename.title = 'Changing....'

            if screen_name == 'error_screen':
                self.root.ids.titlename.title = 'Main'


MainApp().run()