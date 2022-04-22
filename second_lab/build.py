from datetime import datetime

from train_base import TrainBase, ParserToFile, CustomContentHandler
from kv.Interface import MainScreen, AddPopup, SearchPopup, DeletePopup, FoundPopup


class Controller:

    def __init__(self):

        self.model = TrainBase(controller=self)
        self.pars = ParserToFile()
        self.handler = CustomContentHandler()

        self.main_view = MainScreen(controller=self, model=self.model)
        self.add_view = AddPopup(controller=self, model=self.model)
        self.search_view = SearchPopup(controller=self, model=self.model)
        self.delete_view = DeletePopup(controller=self, model=self.model)
        self.found_view = FoundPopup(controller=self, model=self.model)

        self.train_numb = ''
        self.station_start = ''
        self.station_finish = ''
        self.date_start = datetime(10, 1, 1, 0, 0, 0)
        self.date_finish = datetime(10, 1, 2, 0, 0, 0)
        self.date_in_path = self.date_finish - self.date_start

    def set_train_numb(self, numb):
        self.train_numb = str(numb)

    def set_station_start(self, town):
        self.station_start = town

    def set_station_finish(self, town):
        self.station_finish = town

    def set_date_start(self, date):
        if len(str(date)) != 19:
            pass
        else:
            self.date_start = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    def set_date_finish(self, date):
        if len(str(date)) != 19:
            pass
        else:
            self.date_finish = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    def set_train_info(self):
        self.pre_ready = 0
        if self.is_string(self.train_numb) and not self.is_empty(self.train_numb):
            self.pre_ready += 1
        if self.is_station(self.station_start) and not self.is_empty(self.station_start):
            self.pre_ready += 1
        if self.is_station(self.station_finish) and not self.is_empty(self.station_finish):
            self.pre_ready += 1
        if self.is_correct_date(self.date_start.strftime('%Y-%m-%d %H:%M:%S')) and not self.is_empty(self.date_start.strftime('%Y-%m-%d %H:%M:%S')):
            self.pre_ready += 1
        if self.is_correct_date(self.date_finish.strftime('%Y-%m-%d %H:%M:%S')) and not self.is_empty(self.date_finish.strftime('%Y-%m-%d %H:%M:%S')) and self.date_start < self.date_finish:
            self.pre_ready += 1

        if self.pre_ready == 5:
            self.model.add_title(self.train_numb, self.station_start, self.station_finish,
                                 self.date_start, self.date_finish)
            self.train_numb = ''
            self.station_start = ''
            self.station_finish = ''
            self.date_start = datetime(10, 1, 1, 0, 0, 0)
            self.date_finish = datetime(10, 1, 2, 0, 0, 0)
            return True

        else:
            self.train_numb = ''
            self.station_start = ''
            self.station_finish = ''
            self.date_start = datetime(10, 1, 1, 0, 0, 0)
            self.date_finish = datetime(10, 1, 2, 0, 0, 0)
            return False



    def is_string(self, string):
        numbers = '*+-/|,:;_&^%$#@=\'\"'
        for i in string:
            for j in numbers:
                if i == j:
                    return False
        return True

    def is_station(self, string):
        if self.model.station_list.count(string) > 0:
            return True
        else:
            return False

    def is_correct_date(self, date):
        count = 0
        full_date = []
        item = ''
        for i in date:
            if i == '-' or i == ' ' or i == ':':
                count += 1
                full_date.append(item)
                item = ''
            else:
                item += i
        full_date.append(item)

        if len(date) != 19:
            return False
        elif count != 5:
            return False
        elif date[4] == '-' and date[7] == '-' and date[10] == ' ' and date[13] == ':' and date[16] == ':':

            if int(full_date[0]) > 2022 or int(full_date[0]) < 0:
                full_date.clear()
                return False
            elif int(full_date[1]) > 12 or int(full_date[1]) < 0:
                full_date.clear()
                return False
            elif int(full_date[1]) == 2:
                if int(full_date[0]) % 4 == 0 and int(full_date[0]) % 100 != 0 or int(full_date[0]) % 400 == 0:
                    if int(full_date[2]) > 29:
                        full_date.clear()
                        return False
                    else:
                        full_date.clear()
                        return True
                else:
                    if int(full_date[2]) > 28:
                        full_date.clear()
                        return False
                    else:
                        full_date.clear()
                        return True

            elif int(full_date[1]) % 2 == 0:
                if int(full_date[2]) > 30:
                    full_date.clear()
                    return False
                else:
                    full_date.clear()
                    return True
            elif int(full_date[1]) % 2 == 1:
                if int(full_date[2]) > 31:
                    full_date.clear()
                    return False
                else:
                    full_date.clear()
                    return True

            elif int(full_date[3]) > 23 or int(full_date[3]) < 0:
                full_date.clear()
                return False

            elif int(full_date[4]) > 59 or int(full_date[4]) < 0:
                full_date.clear()
                return False

    def is_empty(self, string):
        if len(string) == 0:
            return True
        else:
            return False

    def record_train_info(self):
        correct_check = self.set_train_info()
        if correct_check == True:
            self.add_view.dialogs(True)
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.pars.push_inf(self.model, "test_minidom.xml")
        elif correct_check == False:
            self.add_view.dialogs(False)

    def find_title_by_numb(self, numb):
        if self.is_string(numb):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_numb(numb)
        else:
            self.search_view.wrong_input_dialog()

    def find_title_by_start_st(self, st: str):
        if self.is_string(st):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_start_st(st)
        else:
            self.search_view.wrong_input_dialog()

    def find_title_by_finish_st(self, st: str):
        if self.is_string(st):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_finish_st(st)
        else:
            self.search_view.wrong_input_dialog()

    def find_title_by_start_time(self, start1: datetime, start2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_start_time(start1, start2)
        except ValueError:
            self.search_view.wrong_input_dialog()

    def find_title_by_finish_time(self, finish1: datetime, finish2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_finish_time(finish1, finish2)
        except ValueError:
            self.search_view.wrong_input_dialog()

    def find_title_by_time_in_path(self, time1: datetime, time2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.find_title_by_time_in_path(time1, time2)
        except ValueError:
            self.search_view.wrong_input_dialog()

    def del_title_by_numb(self, numb: str):
        if self.is_string(numb):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_numb(numb)
            self.pars.push_inf(self.model, "test_minidom.xml")
        else:
            self.search_view.wrong_input_dialog()

    def del_title_by_start_st(self, station: str):
        if self.is_string(station):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_start_st(station)
            self.pars.push_inf(self.model, "test_minidom.xml")
        else:
            self.search_view.wrong_input_dialog()

    def del_title_by_finish_st(self, station: str):
        if self.is_string(station):
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_finish_st(station)
            self.pars.push_inf(self.model, "test_minidom.xml")
        else:
            self.search_view.wrong_input_dialog()

    def del_title_by_start_time(self, time1: datetime, time2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_start_time(time1, time2)
            self.pars.push_inf(self.model, "test_minidom.xml")
        except ValueError:
            self.search_view.wrong_input_dialog()

    def del_title_by_finish_time(self, time1: datetime, time2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_finish_time(time1, time2)
            self.pars.push_inf(self.model, "test_minidom.xml")
        except ValueError:
            self.search_view.wrong_input_dialog()

    def del_title_by_time_in_path(self, time1: datetime, time2: datetime):
        try:
            self.model.set_from_file(self.handler, "test_minidom.xml")
            self.model.del_title_by_time_in_path(time1, time2)
            self.pars.push_inf(self.model, "test_minidom.xml")
        except ValueError:
            self.search_view.wrong_input_dialog()

    def get_screen(self):
        return self.main_view