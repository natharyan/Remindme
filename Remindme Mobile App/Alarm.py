from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from kivy.core.window import Window

Window.size = (360, 600)

KV = '''
FloatLayout:
    

    MDRaisedButton:
        text: "Set an Alarm"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
        elevation: 10
    
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        '''
        The method returns the set time.

        :type instance: <kivymd.uix.picker.MDTimePicker object>
        :type time: <class 'datetime.time'>
        '''

        print(time)



Test().run()
