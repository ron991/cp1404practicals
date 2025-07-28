"""
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class ConvertMiles(App):
    output_km = StringProperty()

    def build(self):
        """Build Kivy app"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')