from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy_garden.mapview import MapView


Window.size = (480, 853)
Window.title = "AirBank"

class Container(AnchorLayout):
    Builder.load_string



class AirBankApp(MDApp):
    theme_cls = ThemeManager()
    title = 'AirBank'


    def build(self):
        self.theme_cls.primary_palette = "Gray"


        return Container()


if __name__ == '__main__':
    AirBankApp().run()