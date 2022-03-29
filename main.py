#create an app with kivy

import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import ScrollView

#display a welcome windows app

class WelcomeWindow(App):
    def build(self):
        self.title = 'Welcome to MyApp'
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to Tsunami Tournament Manager!', font_size=40)
        button = Button(text='Click to add user!', font_size=40)
        button.bind(on_press=self.show_textinput)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def show_textinput(self, instance):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Please enter your team:', font_size=30)
        textinput = TextInput(text='', multiline=False)
        textinput.bind(on_text_validate=self.validate_input)
        layout.add_widget(label)
        layout.add_widget(textinput)
        popup = Popup(title='Add New Team', content=layout, size_hint=(None, None), size=(400, 400))
        popup.open()

    def validate_input(self, instance):
        name = instance.text
        popup.dismiss()
        popup = Popup(title='Name', content=Label(text='Welcome, {}'.format(name)), size_hint=(None, None), size=(400, 400))
        popup.open()

    

if __name__ == "__main__":

    WelcomeWindow().run()