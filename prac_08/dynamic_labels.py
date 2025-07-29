"""
Dynamic labels Week 8 practical
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabels(App):
    """Main program for dynamic labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Ron", "James", "Kelly"]

    def build(self):
        """Build main app."""
        self.title = "Dynamic Labels"
        self.root =  Builder.load_file("dynamic_labels.kv")
        return self.root








