from datetime import datetime
from train_base import TrainBase, CustomContentHandler, ParserToFile
import xml.sax, xml.dom.minidom


handler = CustomContentHandler()
ptf = ParserToFile()
train_base = TrainBase()

train_base.set_from_file(handler, "test_minidom.xml")

train_base.print_all()

train_base.add_title('2','12','13', datetime(10,10,10,10,10,10), datetime(402,11,11,11,11,11))
train_base.add_title('19','12','13', datetime(10,10,10,10,10,10), datetime(403,1,29,11,11,11))
train_base.add_title('12','12','13', datetime(10,10,10,10,10,10), datetime(404,1,29,11,11,11))
train_base.add_title('7','12','13', datetime(10,10,10,10,10,10), datetime(405,1,29,11,11,11))
train_base.add_title('4','12','13', datetime(10,10,10,10,10,10), datetime(423,1,29,11,11,11))

train_base.print_all()
print("Trains ", train_base.size)

ptf.push_inf(train_base, "test_minidom.xml")

print("Trains ", train_base.size)