import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='Hello, World!')


if __name__ == '__main__':
    TestApp().run()