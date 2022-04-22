from datetime import datetime
import pytimeparse
from os import path
import xml.sax
import xml.dom.minidom


class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.trainCount = 0
        self.isInNumb = False
        self.isInStationStart = False
        self.isInStationFinish = False
        self.isInDateStart = False
        self.isInDateFinish = False
        self.isInDatePath = False
        self.t_n = []
        self.s_s = []
        self.s_f = []
        self.d_s = []
        self.d_f = []
        self.flag = False

        self.numb = ""
        self.st_st = ""
        self.st_f = ""
        self.dy_s = ""
        self.dy_f = ""
        self.count = 0

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'train':
            self.flag = True
            self.count = 0
        elif tagName == 'number':
            self.isInNumb = True
        elif tagName == 'station_start':
            self.isInStationStart = True
        elif tagName == 'station_finish':
            self.isInStationFinish = True
        elif tagName == 'date_start':
            self.isInDateStart = True
        elif tagName == 'date_finish':
            self.isInDateFinish = True
        elif tagName == 'date_in_path':
            self.isInDatePath = True

    # Handle endElement
    def endElement(self, tagName):
        if tagName == 'number':
            self.isInNumb = False
        elif tagName == 'station_start':
            self.isInStationStart = False
        elif tagName == 'station_finish':
            self.isInStationFinish = False
        elif tagName == 'date_start':
            self.isInDateStart = False
        elif tagName == 'date_finish':
            self.isInDateFinish = False
        elif tagName == 'date_in_path':
            self.isInDatePath = False
        elif tagName == 'train':
            self.flag = False
            if self.count == 5:
                self.trainCount += 1
                self.t_n.append(self.numb)
                self.s_s.append(self.st_st)
                self.s_f.append(self.st_f)
                self.d_s.append(self.dy_s)
                self.d_f.append(self.dy_f)


    # Handle text data
    def characters(self, chars):
        if self.flag:
            if self.isInNumb:
                self.numb = str(chars)
                self.count += 1
               #self.t_n.append(str(chars))
            if self.isInStationStart:
                self.st_st = str(chars)
                self.count += 1
                #self.s_s.append(str(chars))
            if self.isInStationFinish:
                self.st_f = str(chars)
                self.count += 1
                #self.s_f.append(str(chars))
            if self.isInDateStart:
                year = int(chars[:4])
                month = int(chars[5:7])
                day = int(chars[8:10])
                hour = int(chars[11:13])
                min = int(chars[14:16])
                sec = int(chars[17:19])
                self.dy_s = datetime(year, month, day, hour, min, sec)
                self.count += 1
                #self.d_s.append(datetime(year, month, day, hour, min, sec))
            if self.isInDateFinish:
                year = int(chars[:4])
                month = int(chars[5:7])
                day = int(chars[8:10])
                hour = int(chars[11:13])
                min = int(chars[14:16])
                sec = int(chars[17:19])
                self.dy_f = datetime(year, month, day, hour, min, sec)
                self.count += 1
                #self.d_f.append(datetime(year, month, day, hour, min, sec))


    # Handle startDocument
    def startDocument(self):
        self.trainCount = 0
        self.t_n = []
        self.s_s = []
        self.s_f = []
        self.d_s = []
        self.d_f = []


class TrainBase(object):
    def __init__(self, controller):
        self.train_numb = []
        self.station_start = []
        self.station_finish = []
        self.date_start = []
        self.date_finish = []
        self.date_in_path = []
        self.size = 0

        self._all_info_list = []
        self.found_trains = []

        self.controller = controller

        self.station_list = ["Минск", "Гомель", "Могилёв", "Витебск", "Гродно", "Брест",
                        "Бобруйск", "Барановичи", "Борисов", "Пинск", "Орша", "Мозырь",
                        "Солигорск", "Новополоцк", "Лида", "Молодечно", "Полоцк", "Жлобин",
                        "Речица", "Жодино", "Слуцк", "Кобрин", "Волковыск", "Калинковичи",
                        "Рогачев", "Новогрудок", "Лунинец", "Смолевичи", "Мир", "Несвиж"]



    def add_title(self, t_n: str, s_s: str, s_f: str, d_s: datetime, d_f: datetime):
        if d_f > d_s:
            self._trains = {}
            self.train_numb.append(t_n)
            self._trains['train numb'] = t_n
            self.station_start.append(s_s)
            self._trains['start station'] = s_s
            self.station_finish.append(s_f)
            self._trains['finish station'] = s_f
            self.date_start.append(d_s)
            self._trains['start time'] = d_s
            self.date_finish.append(d_f)
            self._trains['finish time'] = d_f
            date = d_f - d_s
            self.date_in_path.append(date)
            self._trains['time in path'] = date
            self.size += 1

            self._all_info_list.append(self._trains)
            self.add_into_main_table(self._all_info_list)

    def return_all_info_list(self):
        return self._all_info_list

    def return_searched_amount(self, amount):
        self.controller.search_view.return_searched_amount(amount)

    def delete_from_main_table(self, deleted_list):
        self.controller.main_view.delete_from_main_table(deleted_list)

    def return_deleted_amount(self, amount):
        self.controller.delete_view.return_deleted_amount(amount)

    def find_title_by_numb(self, numb: str):
        amount = 0
        self.found_trains = []
        for i in range(self.size):
            pre_list = []
            if self.train_numb[i] == numb:
                amount += 1
                pre_list.append(self.train_numb[i])
                pre_list.append(self.station_start[i])
                pre_list.append(self.station_finish[i])
                pre_list.append(self.date_start[i])
                pre_list.append(self.date_finish[i])
                pre_list.append(self.date_in_path[i])
                self.found_trains.append(pre_list)
        self.return_searched_amount(amount)


    def find_title_by_start_st(self, station: str):
        amount = 0
        self.found_trains = []
        for i in range(self.size):
            pre_list = []
            if self.station_start[i] == station:
                amount += 1
                pre_list.append(self.train_numb[i])
                pre_list.append(self.station_start[i])
                pre_list.append(self.station_finish[i])
                pre_list.append(self.date_start[i])
                pre_list.append(self.date_finish[i])
                pre_list.append(self.date_in_path[i])
                self.found_trains.append(pre_list)
        self.return_searched_amount(amount)

    def find_title_by_finish_st(self, station: str):
        amount = 0
        self.found_trains = []
        for i in range(self.size):
            pre_list = []
            if self.station_finish[i] == station:
                amount += 1
                pre_list.append(self.train_numb[i])
                pre_list.append(self.station_start[i])
                pre_list.append(self.station_finish[i])
                pre_list.append(self.date_start[i])
                pre_list.append(self.date_finish[i])
                pre_list.append(self.date_in_path[i])
                self.found_trains.append(pre_list)
        self.return_searched_amount(amount)

    def find_title_by_start_time(self, time1, time2):
        if time1 <= time2:
            amount = 0
            time1 = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
            time2 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
            self.found_trains = []
            for i in range(self.size):
                pre_list = []
                if self.date_start[i] >= time1 and self.date_start[i] <= time2:
                    amount += 1
                    pre_list.append(self.train_numb[i])
                    pre_list.append(self.station_start[i])
                    pre_list.append(self.station_finish[i])
                    pre_list.append(self.date_start[i])
                    pre_list.append(self.date_finish[i])
                    pre_list.append(self.date_in_path[i])
                    self.found_trains.append(pre_list)
            self.return_searched_amount(amount)
        else:
            return -1

    def find_title_by_finish_time(self, time1, time2):
        if time1 <= time2:
            amount = 0
            time1 = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
            time2 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
            self.found_trains = []
            for i in range(self.size):
                pre_list = []
                if self.date_finish[i] >= time1 and self.date_finish[i] <= time2:
                    amount += 1
                    pre_list.append(self.train_numb[i])
                    pre_list.append(self.station_start[i])
                    pre_list.append(self.station_finish[i])
                    pre_list.append(self.date_start[i])
                    pre_list.append(self.date_finish[i])
                    pre_list.append(self.date_in_path[i])
                    self.found_trains.append(pre_list)
            self.return_searched_amount(amount)
        else:
            return -1

    def find_title_by_time_in_path(self, time1, time2):
        if time1 <= time2:
            amount = 0
            self.found_trains = []
            for i in range(self.size):
                pre_list = []
                if pytimeparse.parse(str(self.date_in_path[i])) >= time1 and pytimeparse.parse(str(self.date_in_path[i])) <= time2:
                    amount += 1
                    pre_list.append(self.train_numb[i])
                    pre_list.append(self.station_start[i])
                    pre_list.append(self.station_finish[i])
                    pre_list.append(self.date_start[i])
                    pre_list.append(self.date_finish[i])
                    pre_list.append(self.date_in_path[i])
                    self.found_trains.append(pre_list)
            self.return_searched_amount(amount)
        else:
            return -1


    def del_title_by_numb(self, numb: str):
        amount = 0
        new_info = []
        for i in range(self.size, 0, -1):
            if self.train_numb[i - 1] == numb:
                self.del_title(i - 1)
                amount += 1
            else:
                new_info.append(self._all_info_list[i-1])

        self._all_info_list = new_info
        self.delete_from_main_table(self._all_info_list)
        self.return_deleted_amount(amount)

    def del_title_by_start_st(self, station: str):
        amount = 0
        new_info = []
        for i in range(self.size, 0, -1):
            if self.station_start[i - 1] == station:
                self.del_title(i - 1)
                amount += 1
            else:
                new_info.append(self._all_info_list[i - 1])

        self._all_info_list = new_info
        self.delete_from_main_table(self._all_info_list)
        self.return_deleted_amount(amount)

    def del_title_by_finish_st(self, station: str):
        amount = 0
        new_info = []
        for i in range(self.size, 0, -1):
            if self.station_finish[i - i] == station:
                self.del_title(i - i)
                amount += 1
            else:
                new_info.append(self._all_info_list[i-1])

        self._all_info_list = new_info
        self.delete_from_main_table(self._all_info_list)
        self.return_deleted_amount(amount)

    def del_title_by_start_time(self, time1, time2):
        new_info = []
        time1 = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
        if time1 <= time2:
            amount = 0
            for i in range(self.size, 0, -1):
                if self.date_start[i - 1] >= time1 and self.date_start[i - 1] <= time2:
                    self.del_title(i - 1)
                    amount += 1
                else:
                    new_info.append(self._all_info_list[i - 1])

            self._all_info_list = new_info
            self.delete_from_main_table(self._all_info_list)
            self.return_deleted_amount(amount)
        else:
            return -1

    def del_title_by_finish_time(self, time1, time2):
        new_info = []
        time1 = datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
        time2 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
        if time1 <= time2:
            amount = 0
            for i in range(self.size, 0, -1):
                if self.date_finish[i - 1] >= time1 and self.date_finish[i - 1] <= time2:
                    self.del_title(i - 1)
                    amount += 1
                else:
                    new_info.append(self._all_info_list[i - 1])

            self._all_info_list = new_info
            self.delete_from_main_table(self._all_info_list)
            self.return_deleted_amount(amount)
        else:
            return -1

    def del_title_by_time_in_path(self, time1, time2):
        new_info = []
        if time1 <= time2:
            amount = 0
            for i in range(self.size, 0, -1):
                if pytimeparse.parse(str(self.date_in_path[i - 1])) >= time1 and pytimeparse.parse(str(self.date_in_path[i - 1])) <= time2:
                    self.del_title(i - 1)
                    amount += 1
                else:
                    new_info.append(self._all_info_list[i - 1])

            self._all_info_list = new_info
            self.delete_from_main_table(self._all_info_list)
            self.return_deleted_amount(amount)
        else:
            return -1

    def del_title(self, index: int):
        if index < len(self.train_numb):
            self.train_numb.pop(index)
            self.station_start.pop(index)
            self.station_finish.pop(index)
            self.date_start.pop(index)
            self.date_finish.pop(index)
            self.date_in_path.pop(index)
            self.size -= 1
        else:
            return -1

    def set_from_file(self, handler: CustomContentHandler, filename: str):
        xml.sax.parse(filename, handler)
        for i in range(handler.trainCount):
            flag = True
            for j in range(self.size):
                if handler.t_n[i] == self.train_numb[j] and handler.s_s[i] == self.station_start[j] and handler.s_f[i] \
                        == self.station_finish[j] and handler.d_s[i] == self.date_start[j] and handler.d_f[i] \
                        == self.date_finish[j]:

                    flag = False
                    break
            if flag:
                self.add_title(handler.t_n[i], handler.s_s[i], handler.s_f[i], handler.d_s[i], handler.d_f[i])


    def add_into_main_table(self, train_list):
        self.controller.main_view.add_into_main_table(train_list)


class ParserToFile():
    def __init__(self):
        pass

    def push_inf(self, base: TrainBase, filename: str):

        self.doc = xml.dom.minidom.Document()
        self.stuff = self.doc.createElement('trains')

        for i in range(base.size):
            self.train1 = self.doc.createElement("train")

            self.numb = self.doc.createElement("number")
            self.numb1 = self.doc.createTextNode(base.train_numb[i])
            self.numb.appendChild(self.numb1)
            self.train1.appendChild(self.numb)

            self.st_st = self.doc.createElement("station_start")
            self.st_st1 = self.doc.createTextNode(base.station_start[i])
            self.st_st.appendChild(self.st_st1)
            self.train1.appendChild(self.st_st)

            self.st_f = self.doc.createElement("station_finish")
            self.st_f1 = self.doc.createTextNode(base.station_finish[i])
            self.st_f.appendChild(self.st_f1)
            self.train1.appendChild(self.st_f)

            self.d_st = self.doc.createElement("date_start")
            self.d_st1 = self.doc.createTextNode(str(base.date_start[i]))
            self.d_st.appendChild(self.d_st1)
            self.train1.appendChild(self.d_st)

            self.d_f = self.doc.createElement("date_finish")
            self.d_f1 = self.doc.createTextNode(str(base.date_finish[i]))
            self.d_f.appendChild(self.d_f1)
            self.train1.appendChild(self.d_f)

            self.d_p = self.doc.createElement("date_in_path")
            self.d_p1 = self.doc.createTextNode(str(base.date_in_path[i]))
            self.d_p.appendChild(self.d_p1)
            self.train1.appendChild(self.d_p)

            self.stuff.appendChild(self.train1)

        self.doc.appendChild(self.stuff)

        with open(filename, "w") as out:
            self.doc.writexml(out, indent="    ", addindent="    ", newl="\n", encoding="windows-1251")
