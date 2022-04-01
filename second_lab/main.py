from datetime import datetime
from train_base import TrainBase, CustomContentHandler
import xml.sax

def main():
    handler = CustomContentHandler()
    xml.sax.parse('myfile.xml', handler)
    print(f'There were {handler.postCount} post elements')
    print(f'There were {handler.entryCount} entry elements')


base = TrainBase()
base.add_title('2','12','13', datetime(10,10,10,10,10,10), datetime(402,11,11,11,11,11))
base.add_title('1','12','13', datetime(10,10,10,10,10,10), datetime(403,1,29,11,11,11))
base.add_title('2','12','13', datetime(10,10,10,10,10,10), datetime(404,1,29,11,11,11))
base.add_title('2','12','13', datetime(10,10,10,10,10,10), datetime(405,1,29,11,11,11))
base.add_title('1','12','13', datetime(10,10,10,10,10,10), datetime(406,1,29,11,11,11))

base.print_all()
base.del_title_by_numb('2')
base.print_all()

if __name__ == '__main__':
    main()
