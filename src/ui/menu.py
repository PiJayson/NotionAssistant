from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from utils.database_factory import DatabaseFactory

class Menu(App):
    def __init__(self, database_factory: DatabaseFactory, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.database_factory = database_factory
    
    def build(self):
        # Create a vertical box layout
        layout = BoxLayout(orientation='vertical')

        # Create a label to display the text
        self.text_label = Label(text="Hello, Kivy!", font_size=24, halign='center', valign='middle', size_hint=(1, 0.8))

        # Create a button to change the text
        self.change_text_button = Button(text="Change Text", size_hint=(1, 0.2))
        self.change_text_button.bind(on_press=self.change_text)

        # Add the label and button to the layout
        layout.add_widget(self.text_label)
        layout.add_widget(self.change_text_button)

        return layout

    def change_text(self, instance):
        # Change the text when the button is pressed
        task_database = self.database_factory.get_task_database()
        rows = task_database.get_rows(5, task_database.get_properties().DUE.value, False)
        
        self.text_label.text = ""
        for row in rows:
            self.text_label.text += row.get_task_name() + "\n"