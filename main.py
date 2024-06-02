from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.animation import Animation

class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, 1)
        self.width = 200
        self.add_widget(Button(text='Button 1'))
        self.add_widget(Button(text='Button 2'))
        self.add_widget(Button(text='Button 3'))

class MainApp(App):
    def build(self):
        self.root = BoxLayout(orientation='horizontal')
        self.sidebar = Sidebar()
        self.main_content = Image(source='background.jpg', allow_stretch=True)
        self.toggle_button = Button(size_hint=(None, None), size=(50, 50), on_press=self.toggle_sidebar)
        self.root.add_widget(self.sidebar)
        self.root.add_widget(self.main_content)
        self.root.add_widget(self.toggle_button)
        return self.root

    def toggle_sidebar(self, instance):
        if self.sidebar.width > 0:
            anim = Animation(width=0, t='out_expo', duration=0.5)
        else:
            anim = Animation(width=200, t='out_expo', duration=0.5)
        anim.start(self.sidebar)

if __name__ == '__main__':
    MainApp().run()