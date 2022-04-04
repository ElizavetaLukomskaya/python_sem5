from datetime import date, time, datetime, timedelta
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

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'trains':
            print('Trains')
        elif tagName == 'train':
            self.trainCount += 1
            print('New train ', self.trainCount)
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
            print('End train')

    # Handle text data
    def characters(self, chars):
        if self.isInNumb:
            self.t_n.append(str(chars))
            print('Numb: ' + chars)
        if self.isInStationStart:
            self.s_s.append(str(chars))
            st_st = chars
            print('Station Start: ' + st_st)
        if self.isInStationFinish:
            self.s_f.append(str(chars))
            st_f = chars
            print('Station Start: ' + st_f)
        if self.isInDateStart:
            d_st = chars
            print('Date Start: ' + d_st)
            year = int(chars[:4])
            month = int(chars[5:7])
            day = int(chars[8:10])
            hour = int(chars[11:13])
            min = int(chars[14:16])
            sec = int(chars[17:19])
            self.d_s.append(datetime(year, month, day, hour, min, sec))
        if self.isInDateFinish:
            d_f = chars
            print('Date Finish: ' + d_f)
            year = int(chars[:4])
            month = int(chars[5:7])
            day = int(chars[8:10])
            hour = int(chars[11:13])
            min = int(chars[14:16])
            sec = int(chars[17:19])
            self.d_f.append(datetime(year, month, day, hour, min, sec))
        if self.isInDatePath:
            #self.train_base.date_in_path.append(self.train_base.date_finish[self.trainCount - 1] - self.train_base.date_start[self.trainCount - 1])
            print('Date in Path: ' + chars)


    # Handle startDocument
    def startDocument(self):
        print('About to start!')
        self.trainCount = 0

    '''# Handle endDocument
    def endDocument(self):
        print('Finishing up!')'''


class TrainBase(object):
    def __init__(self):
        self.train_numb = []
        self.station_start = []
        self.station_finish = []
        self.date_start = []
        self.date_finish = []
        self.date_in_path = []
        self.size = 0

    def print_all(self):
        print('| Train Number | Start | Finish | Time1 | Time2 | End Time |')
        for i in range(self.size):
            self.print_title(i)

    def print_title(self, index: int):
        print(end='| ')
        print(self.train_numb[index], end=' | ')
        print(self.station_start[index], end=' | ')
        print(self.station_finish[index], end=' | ')
        print(self.date_start[index], end=' | ')
        print(self.date_finish[index], end=' | ')
        print(self.date_in_path[index], end=' |\n')

    def add_title(self, t_n: str, s_s: str, s_f: str, d_s: datetime, d_f: datetime):
        self.train_numb.append(t_n)
        self.station_start.append(s_s)
        self.station_finish.append(s_f)
        self.date_start.append(d_s)
        self.date_finish.append(d_f)
        date = d_f - d_s
        self.date_in_path.append(date)

        self.size += 1

    def find_title_by_numb(self, numb: str):
        amount = 0
        print('Searching by train number: ')
        for i in range(self.size):
            if self.train_numb[i] == numb:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_start_st(self, station: str):
        amount = 0
        print('Searching by start station: ')
        for i in range(self.size):
            if self.station_start[i] == station:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_finish_st(self, station: str):
        amount = 0
        print('Searching by finish station: ')
        for i in range(self.size):
            if self.station_finish[i] == station:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_start_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Searching by start time: ')
            for i in range(self.size):
                if self.date_start[i] >= time1 and self.date_start[i] <= time2:
                    self.print_title(i)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def find_title_by_finish_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Searching by finish time: ')
            for i in range(self.size):
                if self.date_finish[i] >= time1 and self.date_finish[i] <= time2:
                    self.print_title(i)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def find_title_by_time_in_path(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Searching by finish time: ')
            for i in range(self.size):
                if self.date_in_path[i] >= time1 and self.date_in_path[i] <= time2:
                    self.print_title(i)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def del_title_by_numb(self, numb: str):
        amount = 0
        print('Deleting by train number: ')
        for i in range(self.size, 0, -1):
            if self.train_numb[i - 1] == numb:
                self.del_title(i - 1)
                amount += 1
        print('Delete ' + str(amount) + ' Titles')

    def del_title_by_start_st(self, station: str):
        amount = 0
        print('Searching by start station: ')
        for i in range(self.size, 0, -1):
            if self.station_start[i - 1] == station:
                self.del_title(i - 1)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def del_title_by_finish_st(self, station: str):
        amount = 0
        print('Searching by finish station: ')
        for i in range(self.size, 0, -1):
            if self.station_finish[i - i] == station:
                self.del_title(i - i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def del_title_by_start_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by start time: ')
            for i in range(self.size, 0, -1):
                if self.date_start[i - 1] >= time1 and self.date_start[i - 1] <= time2:
                    self.del_title(i - 1)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def del_title_by_finish_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by finish time: ')
            for i in range(self.size, 0, -1):
                if self.date_finish[i - 1] >= time1 and self.date_finish[i - 1] <= time2:
                    self.del_title(i - 1)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def del_title_by_time_in_path(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by start time: ')
            for i in range(self.size, 0, -1):
                if self.date_in_path[i - 1] >= time1 and self.date_in_path[i - 1] <= time2:
                    self.print_title(i - 1)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

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
            print('Incorrect data, Can\'t remove')

    def set_from_file(self, handler: CustomContentHandler, filename: str):
        xml.sax.parse(filename, handler)
        for i in range(handler.trainCount):
            self.add_title(handler.t_n[i], handler.s_s[i], handler.s_f[i], handler.d_s[i], handler.d_f[i])


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
            self.doc.writexml(out, indent="   ", addindent="    ", newl="\n", encoding="UTF-8")
