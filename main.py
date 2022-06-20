from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# Creating The Design File
designFile = Builder.load_file("design.kv")

# Creating The App
class QuoteMe(App):
    def build(self):
        Window.size = (350,550)
        return designFile

# Mainloop
if __name__ == "__main__":
    QuoteMe().run()