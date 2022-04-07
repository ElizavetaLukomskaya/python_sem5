from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.app import App
#import pytz


class WorkScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()

        # displayworklist = []

        # Density-independent Pixels - An abstract unit that is based on the physical density of the screen. With a density of 1, 1dp is equal to 1px. When running on a higher density screen, the number of pixels used to draw 1dp is scaled up a factor appropriate to the screen’s dpi, and the inverse for a lower dpi. The ratio of dp-to-pixels will change with the screen density, but not necessarily in direct proportion. Using the dp unit is a simple solution to making the view dimensions in your layout resize properly for different screen densities. In others words, it provides consistency for the real-world size of your UI across different devices.
        datatable = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check = True,
            use_pagination=True,
            rows_num=10,
            column_data=[
                ('Номер поезда', dp(20)),
                ('Станция отправления', dp(20)),
                ('Станция прибытия', dp(20)),
                ('Дата и время отправления', dp(20)),
                ('Время в пути', dp(20))
            ],
            #row_data=displayworklist
            row_data=[
               (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
            ]
            ,
            sorted_on='Дата и время отправления',
            sorted_order='ASC'
        )

        datatable.bind(on_row_press=self.row_press)
        self.add_widget(datatable)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)