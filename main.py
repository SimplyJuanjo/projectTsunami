import kivy

print(kivy.__version__)

from kivy.app import App
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window 

Window.size = (325, 650) #this is temporal to make it look alike a phone in the PC


class TournamentBox(BoxLayout):
    #create a on_click function for the button to add a new team in the scrollview
    def add_team(self):
        print("adding team")
    def edit_teams(self):
        print("editing team")
    def delete_teams(self):
        print("deleting team")
    def start_tournament(self):
        print("starting tournament")
    pass

class TournamentScreen(Screen):
    pass

class TournamentSettings(Screen):
    def on_slider_mode(self, value):
        if value == 0:
            self.ids.slider_label_mode.text = "Mode: Pro"
            self.ids.switch_ko_pro.disabled = False
            self.ids.switch_ko_master.disabled = True
            self.ids.switch_label_ko_master.text = "Master/KO"
            self.ids.switch_ko_advanced.disabled = True
            self.ids.switch_label_ko_advanced.text = "Advanced/KO"
        elif value == 1:
            self.ids.slider_label_mode.text = "Mode: Pro + Master"
            self.ids.switch_ko_pro.disabled = False
            self.ids.switch_ko_master.disabled = False
            self.ids.switch_ko_advanced.disabled = True
            self.ids.switch_label_ko_advanced.text = "Advanced/KO"
        elif value == 2:
            self.ids.slider_label_mode.text = "Mode: Pro + Master + Advanced"
            self.ids.switch_ko_pro.disabled = False
            self.ids.switch_ko_master.disabled = False
            self.ids.switch_ko_advanced.disabled = False
    def on_switch_ko_pro(self, value):
        if value == True:
            self.ids.switch_label_ko_pro.text = "Pro Single KO"
        else:
            self.ids.switch_label_ko_pro.text = "Pro Double KO"
    def on_switch_ko_master(self, value):
        if value == True:
            self.ids.switch_label_ko_master.text = "Master Single KO"
        else:
            self.ids.switch_label_ko_master.text = "Master Double KO"
    def on_switch_ko_advanced(self, value):
        if value == True:
            self.ids.switch_label_ko_advanced.text = "Advanced Single KO"
        else:
            self.ids.switch_label_ko_advanced.text = "Advanced Double KO"
    def on_switch_classification(self, value):
        if value == True:
            self.ids.switch_label_classification.text = "Groups+Brackets"
        else:
            self.ids.switch_label_classification.text = "Only Brackets"
    def on_switch_groups(self, value):
        if value == True:
            self.ids.switch_label_groups.text = "Groups play 1 by 1"
        else:
            self.ids.switch_label_groups.text = "All Groups play at once"
    pass

class MainScreen(Screen):
    pass

class StartScreen(Screen):
    pass

class TournamentManagerApp(App):
    def build(self):
        self.title = "Tournament Manager"
        #self.icon = "icon.png"
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(TournamentScreen(name='tournament'))
        sm.add_widget(TournamentSettings(name='settings'))
        return sm


if __name__ == '__main__':
    TournamentManagerApp().run()