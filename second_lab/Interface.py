import math

from kivy.metrics import dp

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivymd.uix.datatables import MDDataTable
# from kivy.uix.popup import Popup



class Application(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.datatable = MDDataTable # name for table with data
        self.mainlayout = BoxLayout()
        self.menu_of_tables()


        self.current_page = 1
        self.records_on_page = 5

    #Main menu of tables
    def menu_of_tables(self, obj=None):
        self.mainlayout.clear_widgets()
        table_buttons = BoxLayout()
        table_buttons.orientation = 'vertical'

        #Create new table
        new_table = BoxLayout(padding=30)
        create_new_table_button = MDFlatButton(text='Create new table')
        table_title = TextInput(text='Table name',multiline=False)
        new_table.add_widget(table_title)
        new_table.add_widget(create_new_table_button)
        create_new_table_button.bind(on_release=self.create_new_table)
        table_buttons.add_widget(new_table)

    def create_new_table(self, obj=None):
        name = self.mainlayout.children[0].children[0].children[1].text
        name = name.replace(' ', '')
        self.datatable = MDDataTable(name)
        self.mainlayout.clear_widgets()
        self.workplace()

    def open_table(self, button):



    # Creating a structure of workplace
    def workplace(self, obj=None):
        self.mainlayout.clear_widgets()
        self.ini_table_widget()

        menu = BoxLayout(orientation='vertical')
        workin_area = BoxLayout(orientation='vertical', size_hint=(4, 1))

        menu.add_widget(self.ini_table_tools)
        workin_area.add_widget(self.ini_table_widget())

        self.mainlayout.add_widget(menu)
        self.mainlayout.add_widget(workin_area)

    # Initialization of table widgets
    def ini_table_widget(self):
        place_of_table_and_pages = BoxLayout(orientation='vertical')

        table_widget = GridLayout()
        table_widget.cols = len(self.datatable.columns)  # columns - name of variable for columns in table file

        column_data = list()

        for column in self.datatable.columns:
            column_data.append((column.title, dp(int((Screen.size[0] / 20)/len(self.datatable.columns)))))

        print(column_data)

        row_data = list()

        for index in range((self.current_page - 1) * self.records_on_page, self.current_page * self.records_on_page):
            if index < len(self.datatable.records): # records - name of variable for recorded data in table file
                row_data.append(tuple(self.datatable.records[index].elements))

        # Next page, last page and other buttons
        pages_buttons = BoxLayout(size_hint_y=0.1)
        first_page = MDFlatButton(text='<<')
        last_page = MDFlatButton(text='>>')
        previous_page = MDFlatButton(text='<')
        second_page = MDFlatButton(text='>')

        first_page.bind(on_release=self.first_page)
        last_page.bind(on_release=self.last_page)
        previous_page.bind(on_release=self.previous_page)
        second_page.bind(on_release=self.second_page)

        pages_buttons.add_widget(first_page)
        pages_buttons.add_widget(previous_page)
        pages_buttons.add_widget(second_page)
        pages_buttons.add_widget(last_page)

        place_of_table_and_pages(table_widget)
        place_of_table_and_pages(pages_buttons)

        return place_of_table_and_pages

    def first_page(self, obj=None):
        self.current_page = 1
        self.workplace()

    def last_page(self, obj=None):
        self.current_page = math.ceil(len(self.datatable.records)/self.records_on_page)
        self.workplace()

    def previous_page(self, obj=None):
        if self.current_page > 1:
            self.current_page -= 1
            self.workplace()

    def previous_page(self, obj=None):
        if self.current_page < math.ceil(len(self.datatable.records)/self.records_on_page):
            self.current_page += 1
            self.workplace()





    def build(self):
        self.title = 'Train Schedule'
        self.theme_cls.theme_style = 'Dark'

        return self.mainwindow


if __name__ == '__main__':
    Application().run()