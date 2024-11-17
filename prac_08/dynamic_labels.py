from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """App to dynamically create Labels from a list of names."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Initialize list."""
        super().__init__(**kwargs)
        self.names = ["Lin Pyae", "Zizi", "Poypoy"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add to the layout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()