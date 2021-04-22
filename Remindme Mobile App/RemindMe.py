from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ListProperty
from kivymd.uix.dialog import MDDialog
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.audio import SoundLoader
from kivymd.uix.picker import MDDatePicker

l = []
l1 = []
l2 = []
l3 = []

screen_helper = """
MDBoxLayout:   

    orientation:'vertical'
    MDToolbar:
        title: 'RemindME'
        left_action_items: [["format-list-checkbox",lambda x: app.show_alert_dialog()]]          
        font_size: "20dp"


    MDBottomNavigation:
        panel_color: 45/255, 57/255, 69/255, 1
        elevation: 10

        MDBottomNavigationItem:
            name: 'Home'
            text: 'Home'
            icon: 'home-variant'
            on_tab_release: app.navigation_draw()
            MDScreen:
                canvas.before:
                    Rectangle:
                        size: self.size
                        source: "background.png"

            MDProgressBar:
                size_hint_y: None
                height: 5
                value:16.6
                pos_hint: {'center_y': 0.008}

            MDIconButton:
                icon: "notebook"
                user_font_size: "70sp"      
                pos_hint: {'center_x': .18, 'center_y': .45}

            MDIconButton:
                icon: "pen"
                user_font_size: "70sp"    
                pos_hint: {'center_x': .5, 'center_y': .7}


            MDIconButton:
                icon: "calendar-text"
                user_font_size: "70sp"    
                pos_hint: {'center_x': .82, 'center_y': .45}

            MDIconButton:
                icon: "clipboard-list"
                user_font_size: "70sp"      
                pos_hint: {'center_x': .5, 'center_y': .21}


            MDIconButton:
                icon: "bell-circle"
                user_font_size: "175sp"   
                pos_hint: {'center_x': .5, 'center_y': .46}
                on_press: app.play_sound()

            MDLabel:
                text: "WELCOME TO REMINDME !"
                halign: 'center'
                pos_hint: {'center_x': .5, 'center_y': .88}
                font_size: 44
                font_name: 'Pacifico.ttf'

        MDBottomNavigationItem:
            name: 'Notes'
            text: 'Notes'
            icon: 'notebook'
            on_tab_release: app.navigation_draw()
            MDScreen:
                canvas.before:
                    Rectangle:
                        size: self.size
                        source: "background.png"       

            MDProgressBar:
                size_hint_y: None
                height: 5
                value:33.2
                pos_hint: {'center_y': 0.008}
            BoxLayout:
                MDScreen:
                    radius: [25, 0, 0, 0]
                    id: note 
                    ScrollView:
                        GridLayout:
                            id: notes
                            padding: "20dp"
                            spacing: "10dp"
                            size_hint_y: None
                            height: self.minimum_height
                            size_hint_x: None
                            width: self.minimum_width
                            cols:1
                            rows_force_default: True
                            rows_default_height: 40
                            rows_force_default: True
                            rows_default_width: self.minimum_width



        MDBottomNavigationItem:
            name: 'Draw'
            text: 'Draw'
            icon: 'pen'
            on_tab_press: app.navigation_draw()

            Screen: 
                id: paint

            MDProgressBar:
                size_hint_y: None
                height: 5
                value:49.8
                pos_hint: {'center_y': 0.008}             
        
        MDBottomNavigationItem:
            name: 'Calendar'
            text: 'Events'
            icon: 'calendar-text'
            MDScreen:
                canvas.before:
                    Rectangle:
                        size: self.size
                        source: "background.png"

            MDProgressBar:
                size_hint_y: None
                height: 5
                value:83
                pos_hint: {'center_y': 0.008}    
            MDIconButton:
                icon: "calendar-month"
                user_font_size: "150sp"      
                pos_hint: {'center_x': .8, 'center_y': .5}
            BoxLayout:
                MDScreen:
                    radius: [25, 0, 0, 0]
                    id: calendar                 
                    ScrollView:
                        GridLayout: 
                            id: date
                            padding: "10dp"
                            spacing: "5.7dp"
                            size_hint_y: None
                            height: self.minimum_height
                            size_hint_x: None
                            width: self.minimum_width
                            cols:1
                            rows_force_default: True
                            rows_default_height: 40
                            rows_force_default: True
                            rows_default_width: self.minimum_width    


        MDBottomNavigationItem:
            name: 'List'
            text: 'ITEMS'
            icon: 'clipboard-list'
            on_tab_release: app.navigation_draw()
            MDScreen:
                canvas.before:
                    Rectangle:
                        size: self.size
                        source: "background.png"

            MDProgressBar:
                size_hint_y: None
                height: 5
                value:100
                pos_hint: {'center_y': 0.008}    
            Screen:
                ScrollView:
                    GridLayout:
                        id: grid
                        padding: "10dp"
                        spacing: "10dp"
                        cols: 3
                        size_hint_y: None
                        height: self.minimum_height
                        rows_force_default: True
                        rows_default_height: 40

                MDScreen:
                    radius: [25, 0, 0, 0]
                    id: list 



"""

note = """
MDRaisedButton:
    text: "+ ADD NOTE"
    font_name: 'JosefinSans-Regular.ttf'
    text_color: 0,0,0,1
    md_bg_color: app.theme_cls.accent_color
    ripple_effect: False
    user_font_size: "140sp"   
    pos_hint: {'center_x':0.8286,'center_y':0.045}
    on_release: app.new_note()   
    elevation: 10
    ripple_color: app.theme_cls.primary_color
"""
new_note = """
MDTextField:
    hint_text: "New Note   "
    font_name: 'Roboto-Light.ttf'
    mode: "rectangle"
    helper_text: "write something (then tap on screen)"
    helper_text_mode: "on_focus"
    line_color_normal: app.theme_cls.accent_color
    multiline: True
    size_hint_x: None
    width: 400
"""

new_event = """
MDRaisedButton:
    text: "+ ADD EVENT"
    font_name: 'JosefinSans-Regular.ttf'
    text_color: 0,0,0,1
    md_bg_color: app.theme_cls.accent_color
    pos_hint: {'center_x':0.8286,'center_y':0.045}
    on_release: app.show_date_picker()
    elevation: 10
    ripple_color: app.theme_cls.primary_color
"""
new_description = """
MDTextField:
    hint_text: "Description"
    helper_text: "write something (then tap on screen)"
    font_name: 'Roboto-Light.ttf'
    helper_text_mode: "on_focus"
    line_color_normal: app.theme_cls.accent_color
    size_hint_y: None
    height: 50  
    size_hint_x: None
    width: 400
    multiline: True
"""
item = """
MDTextField:
    hint_text: "ITEM"
    multiline: True
    font_name: 'Roboto-Light.ttf'
    hint_text_color: 0,0,0,1
    line_color_normal: app.theme_cls.accent_color
    helper_text: "enter item"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.17,'center_y':0.1}
    size_hint_x: None
    width: 130
"""
amount = """
MDTextField:
    hint_text: "AMOUNT"
    multiline: True
    font_name: 'Roboto-Light.ttf'
    hint_text_color: 0,0,0,1
    line_color_normal: app.theme_cls.accent_color
    helper_text: "enter amount"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x':0.83,'center_y':0.1}
    size_hint_x: None
    width: 130
"""
add_list = """
MDRaisedButton:
    text: "+ ADD ITEM"
    font_name: 'JosefinSans-Regular.ttf'
    text_color: 0,0,0,1
    md_bg_color: app.theme_cls.accent_color
    pos_hint: {'center_x': .5, 'center_y': .082}
    elevation: 10
    size_hint_x: None
    width: 100
    on_release: app.show_data()
    ripple_color: app.theme_cls.primary_color
"""


class HomeScreen(Screen):
    pass


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(255 / 255, 20 / 255, 147 / 255)
            d = 2
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))  # line is dictionary

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class DraftApp(MDApp):
    dialog = None
    sound = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.accent_palette = "Orange"
        self.theme_cls.primary_hue = "A400"

        return Builder.load_string(screen_helper)

    def on_start(self):
        self.painter = MyPaintWidget()


        clrbtn = MDFloatingActionButton(icon='delete-empty', pos_hint={'center_x': .1, 'center_y': .075},
                                        padding='10 sp', ripple_color=self.theme_cls.primary_color)  # dictionary use
        clrbtn.bind(on_release=self.paint_clear)
        self.emp = MDLabel(text="", size_hint_y=None, height=30)
        self.emp1 = MDLabel(text="", size_hint_y=None, height=40)
        self.emp2 = MDLabel(text="", size_hint_y=None, height=40)
        self.Num = MDLabel(text="No.", font_style="H6", size_hint=(None, None), width=70, height=20)
        self.Item = MDLabel(text="    ITEM ", font_style="H6", size_hint_y=None, height=20)
        self.Amount = MDLabel(text=" AMOUNT ", font_style="H6", size_hint_y=None, height=20)
        self.s1 = MDLabel(text="", font_style="H6", size_hint=(None, None), width=50, height=20)
        self.s2 = MDLabel(text="__________", font_style="H6", size_hint_y=None, height=20)
        self.s3 = MDLabel(text="__________", font_style="H6", size_hint_y=None, height=20)
        self.notebtn = Builder.load_string(note)
        self.eventbtn = Builder.load_string(new_event)
        self.itembtn = Builder.load_string(item)
        self.amountbtn = Builder.load_string(amount)
        self.addbtn = Builder.load_string(add_list)

        self.root.ids.paint.add_widget(self.painter)
        self.root.ids.paint.add_widget(clrbtn)
        self.root.ids.list.add_widget(self.itembtn)
        self.root.ids.list.add_widget(self.amountbtn)
        self.root.ids.list.add_widget(self.addbtn)
        self.root.ids.grid.add_widget(self.Num)
        self.root.ids.grid.add_widget(self.Item)
        self.root.ids.grid.add_widget(self.Amount)
        self.root.ids.grid.add_widget(self.s1)
        self.root.ids.grid.add_widget(self.s2)
        self.root.ids.grid.add_widget(self.s3)
        self.root.ids.note.add_widget(self.notebtn)
        self.root.ids.calendar.add_widget(self.eventbtn)
        self.root.ids.date.add_widget(self.emp2)
        self.note = Builder.load_string(new_note)
        self.root.ids.notes.add_widget(self.note)

    def show_alert_dialog(self):  # information
        if not self.dialog:
            self.dialog = MDDialog(
                title="ALL YOUR REMINDERS IN ONE PLACE:",
                text="NOTES:-  \nmultiline text notes:- tap on new note to add note\nDRAW:-  \ndrawing notes:- make drawing notes and then tap on clear button to clear screen\nEVENT PLANNER:-  \nplan events:- tap new event button to add new event\nLIST:-  \ncreate shopping/grocery list (list is scrollable):- type item and amount and then tap add item button",
                buttons=[
                    MDFlatButton(
                        text="CONTINUE", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ], size_hint=(0.9, 1)
            )
        self.dialog.open()

    t = 1

    def show_data(self):  # for list
        self.item = MDRaisedButton(text=self.itembtn.text, text_color=self.theme_cls.primary_color,
                                   size_hint_y=None,
                                   height=40)
        self.amount = MDRaisedButton(text=self.amountbtn.text, text_color=self.theme_cls.primary_color,
                                     size_hint_y=None,
                                     height=40)
        self.no_text = MDLabel(text=str(self.t) + ".", text_color=self.theme_cls.accent_color, size_hint=(None, None),
                               width=50, height=40)
        self.root.ids.grid.add_widget(self.no_text)
        self.root.ids.grid.add_widget(self.item)
        self.root.ids.grid.add_widget(self.amount)
        self.itembtn.text = ""
        self.amountbtn.text = ""
        global t
        self.t += 1
        return

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def paint_clear(self, obj):
        self.painter.canvas.clear()

    def navigation_draw(self):
        print("Navigation")

    l1 = ListProperty([])

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        l1.append(date)  # use of list
        if len(l1) == 5:
            note = Builder.load_string(new_description)
            event = MDRaisedButton(text=str(len(l1)) + ') ' + str(l1[len(l1) - 1]))
            self.label = MDLabel(text="SCROLL DOWN:", font_name='Roboto-Light.ttf', size_hint_y=None, height=13)
            self.root.ids.date.add_widget(self.label)
            self.root.ids.date.add_widget(event)
            self.root.ids.date.add_widget(note)
        else:
            note = Builder.load_string(new_description)
            event = MDRaisedButton(text=str(len(l1)) + ') ' + str(l1[len(l1) - 1]))
            self.root.ids.date.add_widget(event)
            self.root.ids.date.add_widget(note)

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    z = 1

    def new_note(self):
        if self.z == 6:
            self.label = MDLabel(text="SCROLL DOWN:", font_name='Roboto-Light.ttf', size_hint_y=None, height=40)
            note = Builder.load_string(new_note)
            self.root.ids.notes.add_widget(self.label)
            self.root.ids.notes.add_widget(note)
            self.z += 1
        else:
            note = Builder.load_string(new_note)
            self.root.ids.notes.add_widget(note)
            self.z += 1

    def play_sound(self):
        self.sound = SoundLoader.load('chime.wav')
        self.sound.play()


DraftApp().run()
