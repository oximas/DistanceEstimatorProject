from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)

        # Counter label
        self.label = Label(text=str(self.count), font_size=40)

        # Button
        btn = Button(
            text="Increase",
            font_size=32,
            size_hint=(0.4, 0.3),
            pos_hint={"center_x": 0.5}
        )
        btn.bind(on_press=self.increase)

        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def increase(self, instance):
        self.count += 1
        self.label.text = str(self.count)


if __name__ == "__main__":
    CounterApp().run()
