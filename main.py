from kivy.app import App
from kivy.lang import Builder

# Creating The Design File
designFile = Builder.load_file("design.kv")

# Creating The App
class QuoteMe(App):
    def build(self):
        return ""

# Mainloop
if __name__ == "__main__":
    QuoteMe().run()