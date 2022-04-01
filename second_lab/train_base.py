from datetime import date, time, datetime, timedelta
import xml.sax

class TrainBase(object):

    def __init__(self):
        self.train_numb = []
        self.station_start = []
        self.station_finish = []
        self.date_start = []
        self.date_finish = []
        self.date_in_path = []

    def print_all(self):
        print('| Train Number | Start | Finish | Time1 | Time2 | End Time |')
        for i in range(len(self.train_numb)):
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

    def find_title_by_numb(self, numb: str):
        amount = 0
        print('Searching by train number: ')
        for i in range(len(self.train_numb)):
            if self.train_numb[i] == numb:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_start_st(self, station: str):
        amount = 0
        print('Searching by start station: ')
        for i in range(len(self.station_start)):
            if self.station_start[i] == station:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_finish_st(self, station: str):
        amount = 0
        print('Searching by finish station: ')
        for i in range(len(self.station_finish)):
            if self.station_finish[i] == station:
                self.print_title(i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def find_title_by_start_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Searching by start time: ')
            for i in range(len(self.date_start)):
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
            for i in range(len(self.date_finish)):
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
            for i in range(len(self.date_in_path)):
                if self.date_in_path[i] >= time1 and self.date_in_path[i] <= time2:
                    self.print_title(i)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def del_title_by_numb(self, numb: str):
        amount = 0
        print('Deleting by train number: ')
        for i in range(len(self.train_numb), 0, -1):
            if self.train_numb[i-1] == numb:
                self.del_title(i-1)
                amount += 1
        print('Delete ' + str(amount) + ' Titles')

    def del_title_by_start_st(self, station: str):
        amount = 0
        print('Searching by start station: ')
        for i in range(len(self.station_start), 0, -1):
            if self.station_start[i-1] == station:
                self.del_title(i-1)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def del_title_by_finish_st(self, station: str):
        amount = 0
        print('Searching by finish station: ')
        for i in range(len(self.station_finish), 0, -1):
            if self.station_finish[i - i] == station:
                self.del_title(i - i)
                amount += 1
        print('Find ' + str(amount) + ' Titles')

    def del_title_by_start_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by start time: ')
            for i in range(len(self.date_start), 0, -1):
                if self.date_start[i - 1] >= time1 and self.date_start[i -1 ] <= time2:
                    self.del_title(i - 1)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def del_title_by_finish_time(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by finish time: ')
            for i in range(len(self.date_finish), 0, -1):
                if self.date_finish[i - 1] >= time1 and self.date_finish[i -1] <= time2:
                    self.del_title(i - 1)
                    amount += 1
            print('Find ' + str(amount) + ' Titles')
        else:
            print('Incorrect data')

    def find_title_by_time_in_path(self, time1: datetime, time2: datetime):
        if time1 <= time2:
            amount = 0
            print('Deleting by start time: ')
            for i in range(len(self.date_in_path), 0, -1):
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
        else:
            print('Incorrect data, Can\'t remove')

    def read_from_file(self):
        pass

    def write_to_file(self):
        pass

import xml.sax

class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.postCount = 0
        self.entryCount = 0
        self.isInTitle = False
        self.isInEntry = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'blogposts':
            print('Blogposts title: ' + attrs['title'])
        elif tagName == 'post':
            self.postCount += 1
        elif tagName == 'entry':
            self.entryCount += 1
        elif tagName == 'title':
            self.isInTitle = True
        elif tagName == 'entry':
            self.isInEntry = True

    # Handle endElement
    def endElement(self, tagName):
        if tagName == 'title':
            self.isInTitle = False
        elif tagName == 'entry':
            self.isInEntry = False

    # Handle text data
    def characters(self, chars):
        if self.isInTitle:
            print('Title: ' + chars)
        elif self.isInEntry:
            print('Entry: ' + chars)

    # Handle startDocument
    def startDocument(self):
        print('About to start!')

    # Handle endDocument
    def endDocument(self):
        print('Finishing up!')


