from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window

Window.size = (360, 600)

# Your layouts.
Builder.load_string(
"""
#:import NoTransition kivy.uix.screenmanager.NoTransition
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import toast kivymd.toast.toast


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<ItemBackdropBackLayer>
    size_hint_y: None
    height: self.minimum_height
    spacing: "10dp"

    canvas:
        Color:
            rgba:
                root.theme_cls.primary_dark if root.selected_item \
                else root.theme_cls.primary_color
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDIconButton:
        icon: root.icon
        theme_text_color: "Custom"
        text_color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1

    MDLabel:
        text: ""
        color: 1, 1, 1, .5 if not root.selected_item else 1, 1, 1, 1

<ItemRoundBackdropBackLayerOfSecondScreen@BoxLayout>
    size_hint_y: None
    height: "40dp"
    spacing: "25dp"
    text: ""
    active: False
    group: ""

    MDCheckbox:
        group: root.group
        size_hint: None, None
        size: "30dp", "30dp"
        pos_hint: {"center_y": .5}
        selected_color: 1, 1, 1, 1
        active: root.active
        #on_active: app.printS(root.text)

    MDLabel:
        text: root.text
        color: 1, 1, 1, .7


<MyBackdropFrontLayer@ScrollView>
    backdrop: None
    backlayer: None

    GridLayout:
        size_hint_y: None
        height: self.minimum_height
        cols: 1
        padding: "2dp"
        spacing: "15dp"

        ItemBackdropFrontLayer:
            text: "Hello World"
            secondary_text: "Hello"
            icon: "language-python"
            
        ItemBackdropFrontLayer:
            text: "Hello World"
            secondary_text: "Hello"
            icon: "language-python"   
        
        MDLabel:
            text: "Label"
            color: 0,0,0,1            
            
<MyBackdropBackLayer@ScreenManager>
    transition: NoTransition()

    Screen:
        name: "sexo screen"
        id: "sexo screen"

        ScrollView:

            GridLayout:
                size_hint_y: None
                height: self.minimum_height
                cols: 1
                padding: "20dp"
                spacing: "10dp"

                MDLabel:
                    text: "Welcome to RemindMe! All your reminders in one place!"
                    color: 1, 1, 1, 1

                Widget:
                    size_hint_y: None
                    height: "15dp"

                MDRectangleFlatIconButton:
                    icon:'book-open-outline'
                    text: "Notes"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.note()
                    on_press: root.manager.current = 'note'
                    
                    
                MDRectangleFlatIconButton:
                    icon: 'clock'
                    text: "Alarm"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.alarm()
                    
                    
                MDRectangleFlatIconButton:
                    icon: 'calendar'
                    text: "Calendar"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.calendar()
                    
                    
                MDRectangleFlatIconButton:
                    icon: 'shopping'
                    text: "List"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.list()

<HomeScreen>
    name: 'home'
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "RemindMe"
        header_text: "RemindMe"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
                
<NoteScreen>
    name: 'notes'
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Notes"
        header_text: "Make Your Notes"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer
                

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
                
                
<AlarmScreen>
    name: 'alarm'
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Alarm"
        header_text: "Set an Alarm"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
                
<CalendarScreen>
    name: 'calendar'
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Calendar"
        header_text: "Schedule Your Events"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
               
<ListScreen>
    name: 'list'
    MDBackdrop:
        id: backdrop
        on_open: print("on_open")
        on_close: print("on_close")
        left_action_items: [['menu', lambda x: self.open()]]
        title: "List"
        
        header_text: "Create a Shopping List"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                backlayer: backlayer
                
    """
)


class HomeScreen(Screen):
    pass


class NoteScreen(Screen):
    pass


class AlarmScreen(Screen):
    pass


class CalendarScreen(Screen):
    pass


class ListScreen(Screen):
    pass



class ItemBackdropBackLayer(ThemableBehavior, BoxLayout):
    icon = StringProperty("android")
    text = StringProperty()
    selected_item = BooleanProperty(False)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            for item in self.parent.children:
                if item.selected_item:
                    item.selected_item = False
            self.selected_item = True
        return super().on_touch_down(touch)




class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(NoteScreen(name='notes'))
        sm.add_widget(AlarmScreen(name='alarm'))
        sm.add_widget(CalendarScreen(name='calendar'))
        sm.add_widget(ListScreen(name='list'))

        return HomeScreen()

    def note(self):
        print("hello")
        return NoteScreen()

    def alarm(self):
        print("hello")
        return AlarmScreen()

    def calendar(self):
        print("hello")
        return CalendarScreen()

    def list(self):
        print("hello")
        return ListScreen()


    def print(self,text):
        print(text)

    def navigation_draw(self):
        print("Navigation")


Test().run()