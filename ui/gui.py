from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle

class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, 1)
        self.width = 200
        self.is_visible = True

        with self.canvas.before:
            Color(0, 0, 1, 1)  # set the color to blue
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)
        for i in range(5):  # add 5 buttons as an example
            btn = Button(text=f'Button {i+1}', size_hint_y=None, height=40)
            self.add_widget(self.btn)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def toggle(self, instance):
        if self.is_visible:
            anim = Animation(width=0, d=0.5)
            for btn in self.buttons:
                anim += Animation(opacity=0, d=0.5)
            anim.start(self)
            self.is_visible = False
        else:
            anim = Animation(width=200, d=0.5)
            for btn in self.buttons:
                anim += Animation(opacity=1, d=0.5)
            anim.start(self)
            self.is_visible = True

class MyApp(App):
    def build(self):
        root = FloatLayout()
        sidebar = Sidebar()
        toggle_button = Button(text='Toggle', size_hint=(None, None), size=(50, 50),
                               pos_hint={'right': 1}, on_press=sidebar.toggle)
        root.add_widget(sidebar)
        root.add_widget(toggle_button)
        return root

if __name__ == '__main__':
    MyApp().run()