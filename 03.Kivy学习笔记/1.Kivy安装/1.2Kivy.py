from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# 定义一个登录界面类
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        # 添加用户名标签
        self.add_widget(Label(text='User Name'))
        # 添加用户名输入框
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        # 添加密码标签
        self.add_widget(Label(text='password'))
        # 添加密码输入框
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


# 定义一个应用程序类
class MyApp(App):

    def build(self):
        # 返回登录界面
        return LoginScreen()


# 运行应用程序
if __name__ == '__main__':
    MyApp().run()