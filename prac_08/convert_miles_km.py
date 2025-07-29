"""
Convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMiles(App):
    output_km = StringProperty()

    def build(self):
        """Build Kivy app."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation of conversion. """
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_results(miles)

    def handle_increment(self, text, change):
        """Handle up and down button press with increments."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_results(self, miles):
        """Update results."""
        print("update results")
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to kilometers."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMiles().run()

