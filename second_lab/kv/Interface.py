import os
from datetime import datetime, timedelta

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd_extensions.sweetalert import SweetAlert
from kivymd.uix.screen import MDScreen
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.checkbox import CheckBox


class AddPopup(Popup, Widget):

    model = ObjectProperty()
    controller = ObjectProperty()

    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller
        self.dialog = None

        self._ready = ''

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller
    def get_values(self):
        values = ["Минск", "Гомель", "Могилёв", "Витебск", "Гродно", "Брест",
                        "Бобруйск", "Барановичи", "Борисов", "Пинск", "Орша", "Мозырь",
                        "Солигорск", "Новополоцк", "Лида", "Молодечно", "Полоцк", "Жлобин",
                        "Речица", "Жодино", "Слуцк", "Кобрин", "Волковыск", "Калинковичи",
                        "Рогачев", "Новогрудок", "Лунинец", "Смолевичи", "Мир", "Несвиж"]
        return values

    @property
    def ready(self):
        return self._ready
    @ready.setter
    def ready(self, ready):
        self._ready = ready

    def set_train_numb(self, numb):
        self.controller.set_train_numb(numb)

    def set_station_start(self, values):
        self.ids.spinner_id_start.text = f'{values}'
        self.controller.set_station_start(values)

    def set_station_finish(self, values):
        self.ids.spinner_id_finish.text = f'{values}'
        self.controller.set_station_finish(values)

    def set_date_start(self, date):
        self.controller.set_date_start(date)

    def set_date_finish(self, date):
        self.controller.set_date_finish(date)


    def record_train_info(self):
        self.controller.record_train_info()


    def choose_start_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_start_date_calendar)
        date_dialog.open()

    def set_start_date_calendar(self, instance, value, date_range):
        self.set_date_start(str(value))
        self.ids.start_date_input.text = str(value)

    def choose_finish_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_finish_date_calendar)
        date_dialog.open()

    def set_finish_date_calendar(self, instance, value, date_range):
        self.set_date_finish(str(value))
        self.ids.finish_date_input.text = str(value)

    def dialogs(self, info):
        if info == True:
            self.ready = True
            self.show_dialog()
        elif info == False:
            self.ready = False
            self.show_no_dialog()

    def show_dialog(self):
        self.dialog = SweetAlert().fire(
            "The record has been added!",
            type='success',
        )

    def show_no_dialog(self):
        self.dialog = SweetAlert().fire(
            "ERROR",
            type='failure',
        )

    def closed(self, text):
        self.dialog.dismiss()

    def no_closed(self, text):
        self.dialog.dismiss()




class SearchPopup(Popup, Widget):
    dialog = None
    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller

        self.train_numb = ''
        self.station_start = ''
        self.station_finish = ''
        self.date_start = datetime(10, 10, 10, 10, 10, 10)
        self.date_start1 = datetime(10, 10, 10, 10, 10, 10)
        self.date_finish = datetime(10, 10, 10, 10, 10, 10)
        self.date_finish1 = datetime(10, 10, 10, 10, 10, 10)
        self.date_in_path = self.date_finish - self.date_start
        self.date_in_path1 = self.date_finish1 - self.date_start1

        self.options = []


    def set_search_train_numb(self, numb):
        self.train_numb = str(numb)

    def set_search_start_station(self, station):
        self.station_start = str(station)

    def set_search_finish_station(self, station):
        self.station_finish = str(station)

    def set_search_start_date(self, date: datetime):
        self.date_start = date

    def set_search_start_date1(self, date: datetime):
        self.date_start1 = date

    def set_search_finish_date(self, date: datetime):
        self.date_finish = date

    def set_search_finish_date1(self, date: datetime):
        self.date_finish1 = date

    def set_search_date_in_path(self, date: timedelta):
        self.date_in_path = date

    def set_search_date_in_path1(self, date: timedelta):
        self.date_in_path1 = date

    def stations(self):
        values = ["Минск", "Гомель", "Могилёв", "Витебск", "Гродно", "Брест",
                        "Бобруйск", "Барановичи", "Борисов", "Пинск", "Орша", "Мозырь",
                        "Солигорск", "Новополоцк", "Лида", "Молодечно", "Полоцк", "Жлобин",
                        "Речица", "Жодино", "Слуцк", "Кобрин", "Волковыск", "Калинковичи",
                        "Рогачев", "Новогрудок", "Лунинец", "Смолевичи", "Мир", "Несвиж"]
        return values

    def choose_search_start_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_start_date_calendar)
        date_dialog.open()

    def set_start_date_calendar(self, instance, value, date_range):
        self.set_search_start_date(value)
        self.ids.start_date_search.text = str(value)

    def choose_search_start_date1(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_start_date_calendar1)
        date_dialog.open()

    def set_start_date_calendar1(self, instance, value, date_range):
        self.set_search_start_date1(value)
        self.ids.start_date_search1.text = str(value)

    def choose_search_finish_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_finish_date_calendar)
        date_dialog.open()

    def set_finish_date_calendar(self, instance, value, date_range):
        self.set_search_finish_date(value)
        self.ids.finish_date_search.text = str(value)

    def choose_search_finish_date1(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_finish_date_calendar1)
        date_dialog.open()

    def set_finish_date_calendar1(self, instance, value, date_range):
        self.set_search_finish_date1(value)
        self.ids.finish_date_search1.text = str(value)


    def find_title_by_numb(self):
        self.controller.find_title_by_numb(self.train_numb)
    def find_title_by_start_st(self):
        self.controller.find_title_by_start_st(self.station_start)
    def find_title_by_finish_st(self):
        self.controller.find_title_by_finish_st(self.station_finish)
    def find_title_by_start_time(self):
        self.controller.find_title_by_start_time(self.date_start, self.date_start1)
    def find_title_by_finish_time(self):
        self.controller.find_title_by_finish_time(self.date_finish, self.date_finish1)
    def find_title_by_time_in_path(self):
        self.controller.find_title_by_time_in_path(self.date_in_path, self.date_in_path1)


    def return_searched_amount(self, count):
        self.show_dialog(count)

    def set_properties(self, instance, value, option1):
        if value == True:
            self.options.append(option1)
        else:
            self.options.clear()

    def set_properties_date(self, instance, value, option1, option2):
        if value == True:
            self.options.append(option1)
            self.options.append(option2)
        else:
            self.options.clear()

    def search(self):
        if len(self.options) == 0:
            self.empty_dialog()
        elif self.options[0] == 'train numb' and self.train_numb != '':
            self.find_title_by_numb()
        elif self.options[0] == 'start station' and self.station_start != '':
            self.find_title_by_start_st()
        elif self.options[0] == 'finish station' and self.station_finish != '':
            self.find_title_by_finish_st()
        elif self.options[0] == 'start time' and self.options[1] == 'start time1' and self.date_start != datetime(10, 10, 10, 10, 10, 10):
            self.find_title_by_start_time()
        elif self.options[0] == 'finish time' and self.options[1] == 'finish time1' and self.date_finish != datetime(10, 10, 10, 10, 10, 10):
            self.find_title_by_finish_time()
        elif self.options[0] == 'time in path' and self.options[1] == 'time in path1':
            self.find_title_by_time_in_path()
        else:
            self.empty_input_dialog()

    def show_dialog(self, count):
        if count == 0:
            self.dialog = MDDialog(
                title='Поиск рейса',
                text='Записи не были найдены',
                buttons=[
                    MDFlatButton(text='Ok', on_release=self.closed)
                ]
            )
        else:
            self.dialog = MDDialog(
                title='Поиск рейса',
                text=f'Количество найденных записей: {count}',
                buttons=[
                    MDFlatButton(text='Ok', on_release=self.closed_yes)
                ]
            )
        self.dialog.open()

    def empty_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please choose searching options",
            type='failure',
            buttons=[
                MDFlatButton(text='Ok', on_release=self.closed)
            ]
        )

    def empty_input_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please enter the search data",
            type='failure',
            buttons=[
                MDFlatButton(text='Ok', on_release=self.closed)
            ]
        )

    def wrong_input_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please enter correct data",
            type='failure',
            buttons=[
                MDFlatButton(text='Ok', on_release=self.closed)
            ]
        )

    def closed_yes(self, text):
        self.dialog.dismiss()
        o = FoundPopup(controller = self, model = self.model)
        o.open()

    def closed(self, text):
        self.dialog.dismiss()


class DeletePopup(Popup, Widget):
    def __init__(self, controller, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.controller = controller
        self.dialog = None

        self.train_numb = ''
        self.station_start = ''
        self.station_finish = ''
        self.date_start = datetime(10, 10, 10, 10, 10, 10)
        self.date_start1 = datetime(10, 10, 10, 10, 10, 10)
        self.date_finish = datetime(10, 10, 10, 10, 10, 10)
        self.date_finish1 = datetime(10, 10, 10, 10, 10, 10)
        self.date_in_path = self.date_finish - self.date_start
        self.date_in_path1 = self.date_finish1 - self.date_start1

        self._check_option = 0

        self.options = []

    def set_delete_train_numb(self, numb):
        self.train_numb = str(numb)

    def set_delete_start_station(self, station):
        self.station_start = str(station)

    def set_delete_finish_station(self, station):
        self.station_finish = str(station)

    def set_delete_start_date(self, date: datetime):
        self.date_start = date

    def set_delete_start_date1(self, date: datetime):
        self.date_start1 = date

    def set_delete_finish_date(self, date: datetime):
        self.date_finish = date

    def set_delete_finish_date1(self, date: datetime):
        self.date_finish1 = date

    def set_delete_date_in_path(self, date: timedelta):
        self.date_in_path = date

    def set_delete_date_in_path1(self, date: timedelta):
        self.date_in_path1 = date

    def stations(self):
        values = ["Минск", "Гомель", "Могилёв", "Витебск", "Гродно", "Брест",
                        "Бобруйск", "Барановичи", "Борисов", "Пинск", "Орша", "Мозырь",
                        "Солигорск", "Новополоцк", "Лида", "Молодечно", "Полоцк", "Жлобин",
                        "Речица", "Жодино", "Слуцк", "Кобрин", "Волковыск", "Калинковичи",
                        "Рогачев", "Новогрудок", "Лунинец", "Смолевичи", "Мир", "Несвиж"]
        return values


    def choose_delete_start_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_start_date_calendar)
        date_dialog.open()

    def set_start_date_calendar(self, instance, value, date_range):
        self.set_delete_start_date(value)
        self.ids.start_date_delete.text = str(value)

    def choose_delete_start_date1(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_start_date_calendar1)
        date_dialog.open()

    def set_start_date_calendar1(self, instance, value, date_range):
        self.set_delete_start_date1(value)
        self.ids.start_date_delete1.text = str(value)

    # set birth date by calendar widget
    def choose_delete_finish_date(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_finish_date_calendar)
        date_dialog.open()

    def set_finish_date_calendar(self, instance, value, date_range):
        self.set_delete_finish_date(value)
        self.ids.finish_date_delete.text = str(value)

    def choose_delete_finish_date1(self):
        date_dialog = MDDatePicker(min_year=2022, max_year=2032)
        date_dialog.bind(on_save=self.set_finish_date_calendar1)
        date_dialog.open()

    def set_finish_date_calendar1(self, instance, value, date_range):
        self.set_delete_finish_date1(value)
        self.ids.finish_date_delete1.text = str(value)



    def del_title_by_numb(self):
        self.controller.del_title_by_numb(self.train_numb)

    def del_title_by_start_st(self):
        self.controller.del_title_by_start_st(self.station_start)

    def del_title_by_finish_st(self):
        self.controller.del_title_by_finish_st(self.station_finish)

    def del_title_by_start_time(self):
        self.controller.del_title_by_start_time(self.date_start, self.date_start1)

    def del_title_by_finish_time(self):
        self.controller.del_title_by_finish_time(self.date_finish, self.date_finish1)

    def del_title_by_time_in_path(self):
        self.controller.del_title_by_time_in_path(self.date_in_path, self.date_in_path1)

    def return_deleted_amount(self, count):
        if count == 0:
            self.show_none_dialog()
        else:
            self.show_dialog(count)

    def set_properties(self, instance, value, option1):
        if value == True:
            self.options.append(option1)
        else:
            self.options.clear()

    def set_properties_date(self, instance, value, option1, option2):
        if value == True:
            self.options.append(option1)
            self.options.append(option2)
        else:
            self.options.clear()

    @property
    def check_option(self):
        return self._check_option
    @check_option.setter
    def check_option(self, option):
        self._check_option = option

    def delete(self):
        if len(self.options) == 0:
            self.empty_dialog()
        elif self.options[0] == 'train numb' and self.train_numb != '':
            self._check_option = 1
            self.del_title_by_numb()

        elif self.options[0] == 'start station' and self.station_start != '':
            self._check_option = 2
            self.del_title_by_start_st()

        elif self.options[0] == 'finish station' and self.station_finish != '':
            self._check_option = 3
            self.del_title_by_finish_st()

        elif self.options[0] == 'start time' and self.options[1] == 'start time1' and self.date_start != datetime(10, 10, 10, 10, 10, 10):
            self._check_option = 4
            self.del_title_by_start_time()

        elif self.options[0] == 'finish time' and self.options[1] == 'finish time1' and self.date_finish != datetime(10, 10, 10, 10, 10, 10):
            self._check_option = 5
            self.del_title_by_finish_time()

        elif self.options[0] == 'time in path' and self.options[1] == 'time in path1' and self.date_in_path != datetime(10, 10, 10, 10, 10, 10):
            self._check_option = 6
            self.del_title_by_time_in_path()
        else:
            self.empty_input_dialog()

    def show_dialog(self, count):
            self.dialog = SweetAlert().fire(
                f"Deleted {count} records",
                type='success',
            )

    def empty_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please choose delete options",
            type='failure',
        )

    def show_none_dialog(self):
            self.dialog = SweetAlert().fire(
                "No records have been deleted!",
                type='failure',
            )

    def empty_input_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please enter delete data",
            type='failure',
        )

    def wrong_input_dialog(self):
        self.dialog = SweetAlert().fire(
            "Please enter correct data",
            type='failure',
        )


    def closed(self, text):
        self.dialog.dismiss()

    def closed_empty(self, text):
        self.options = []
        self.dialog.dismiss()


class FoundPopup(Popup, Widget):
    def __init__(self,controller,model, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.found_list = self.model.found_trains

        self.table = MDDataTable(
                                 use_pagination=True,
                                 column_data=[
                                     ("[font=kv\Montserrat-Light]Номер поезда[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция отправления[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция \nприбытия[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Дата и время отправления[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Дата и время прибытия[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Время в пути[/font]", dp(40))], size_hint=(1, 0.95),row_data=self.add_info())
        self.add_widget(self.table)

    def add_info(self):
        return self.model.found_trains

    def return_all_info_list(self):
        return self.model.return_all_info_list()

    def check_info(self, instance, train_info):
        InformationPopup(train_info, main=self).open()

    def close_train_info_window(self):
        self.remove_widget(self.table)

    def add_into_table(self):
        self.remove_widget(self.table)
        self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.5},
                                 use_pagination=True,
                                 check=True,
                                 column_data=[
                                     ("[font=kv\Montserrat-Light]Номер поезда[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция отправления[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция \nприбытия[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Дата и время отправления[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Дата и время прибытия[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Время в пути[/font]", dp(40))], size_hint=(1, 0.7),
                                 row_data=self.add_table_data(self.found_list))

        self.table.bind(on_check_press=self.check_info)
        self.add_widget(self.table)

    def add_table_data(self, list):
        table_train_list = []
        for item in list:
            train_list = []
            train_list.append(item[0])
            train_list.append(item[1])
            train_list.append(item[2])
            train_list.append(item[3])
            train_list.append(item[4])
            train_list.append(item[5])
            table_train_list.append(train_list)

        return table_train_list

class InformationPopup(Popup):
    def __init__(self, train_info, main, **kwargs):
        super().__init__(**kwargs)
        self.train_info = train_info
        self.main = main
        self._all_info_list = main.return_all_info_list()


        self.train_numb = train_info[0]
        self.station_start = train_info[1]
        self.station_finish = train_info[2]
        self.date_start = train_info[3]
        self.date_finish = train_info[4]
        self.date_in_path = train_info[5]

        self.ids.train_numb.text = self.train_numb
        self.ids.station_start.text = self.station_start
        self.ids.station_finish.text = self.station_finish
        self.ids.date_start.text = self.date_start
        self.ids.date_finish.text = self.date_finish
        self.ids.date_in_path.text = self.date_in_path

    def close_train_info_window(self):
        self.dismiss()
        self.main.close_train_info_window()


class HelperPopup(Popup):
    pass


class TooltipCheckBox(CheckBox, MDTooltip):
    pass


class TooltipButton(Button, MDTooltip):
    pass


class MainScreen(MDScreen):

    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self,model,controller, **kw):
        super().__init__(**kw)
        self.dialog=None

        self.controller = controller
        self.model = model
        self._all_info_list = self.model.return_all_info_list()

        self.current_train_info = []

        self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.5},
                                 use_pagination=True,
                                 check = True,
                                 column_data=[
                                     ("[font=kv\Montserrat-Light]Номер поезда[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция отправления[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция \nприбытия[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Дата и время отправления[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Дата и время прибытия[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Время в пути[/font]", dp(40))], size_hint=(1, 0.7),
                                 row_data=self.add_table_data())
        self.table.bind(on_check_press=self.check_info)
        self.add_widget(self.table)



    def dismiss_warning(self):
        self.remove_widget(self.w)

    def show_menu(self):
        pass

    def return_all_info_list(self):
        return self.model.return_all_info_list()

    def check_info(self, instance, pet_info):
        InformationPopup(pet_info, main=self).open()

    def close_train_info_window(self):
        self.remove_widget(self.table)
        self.add_into_main_table(self._all_info_list)

    def add_table_data(self):
        table_train_list=[]
        for item in self._all_info_list:
            train_list = []
            train_list.append(item['train numb'])
            train_list.append(item['start station'])
            train_list.append(item['finish station'])
            train_list.append(item['start time'])
            train_list.append(item['finish time'])
            train_list.append(item['time in path'])
            table_train_list.append(train_list)

        return table_train_list

    def delete_from_main_table(self, train):
        self.remove_widget(self.table)
        self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.5},
                                 use_pagination=True,
                                 check = True,
                                 column_data=[
                                     ("[font=kv\Montserrat-Light]Номер поезда[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция отправления[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция \nприбытия[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Дата и время отправления[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Дата и время прибытия[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Время в пути[/font]", dp(40))], size_hint=(1, 0.7),
                                 row_data=self.add_table_data_deleted(train))
        self.table.bind(on_check_press=self.check_info)
        self.add_widget(self.table)

    def add_table_data_deleted(self, trains):
        table_train_list = []
        for item in trains:
            train_list = []
            train_list.append(item['train numb'])
            train_list.append(item['start station'])
            train_list.append(item['finish station'])
            train_list.append(item['start time'])
            train_list.append(item['finish time'])
            train_list.append(item['time in path'])
            table_train_list.append(train_list)

        return table_train_list

    def add_into_main_table(self, train_list):
        self.remove_widget(self.table)
        self.table = MDDataTable(pos_hint={'center_y': 0.58, 'center_x': 0.5},
                                 use_pagination=True,
                                 check = True,
                                 column_data=[
                                     ("[font=kv\Montserrat-Light]Номер поезда[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция отправления[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Станция \nприбытия[/font]", dp(30)),
                                     ("[font=kv\Montserrat-Light]Дата и время отправления[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Дата и время прибытия[/font]", dp(50)),
                                     ("[font=kv\Montserrat-Light]Время в пути[/font]", dp(40))], size_hint=(1, 0.7),
                                 row_data=self.add_table_data_added(train_list))

        self.table.bind(on_check_press=self.check_info)
        self.add_widget(self.table)

    def add_table_data_added(self, train_list):
        table_train_list = []
        self._all_info_list = train_list
        for item in train_list:
            train_list = []
            train_list.append(item['train numb'])
            train_list.append(item['start station'])
            train_list.append(item['finish station'])
            train_list.append(item['start time'])
            train_list.append(item['finish time'])
            train_list.append(item['time in path'])
            table_train_list.append(train_list)

        return table_train_list

    def return_model(self):
        return self.model
    def return_controller(self):
        return self.controller


Builder.load_file(os.path.join(os.path.dirname(__file__), "Interface.kv"))