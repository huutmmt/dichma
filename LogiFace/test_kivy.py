from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.username_label = Label(text='Username:')
        self.username_input = TextInput()
        
        self.password_label = Label(text='Password:')
        self.password_input = TextInput(password=True)
        
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
    
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Điều kiện kiểm tra đăng nhập ở đây
        if username == 'admin' and password == 'password':
            self.manager.current = 'success'
        else:
            print('Đăng nhập thất bại!')

class SuccessScreen(Screen):
    def __init__(self, **kwargs):
        super(SuccessScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Đăng nhập thành công!'))

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen()
        self.success_screen = SuccessScreen(name='success')
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.success_screen)
        return self.sm

if __name__ == '__main__':
    MyApp().run()
