"""
清华大学的镜像源地址下载安装(速度快）：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

Kivy安装
最简单的方法是安装 kivy-team 提供的 PyPi 轮子的当前稳定版本

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple "kivy[base]" kivy_examples

要额外安装支持音频/视频的 Kivy，请安装Kivy 的依赖项。kivy[base,media]kivy[full]
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple "kivy[media]"
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple " kivy[full]"
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__()
        self.background_color = None
        self.size = None
        self.pos = None

    def build(self):
        layout = BoxLayout()
        label = Label(text='Hello, World!')
        layout.add_widget(label)
     
        self.title = 'Magic Spider'
        self.size = (800, 200)
        self.background_color = (0.1, 0.1, 0.1, 1)
        return layout


TestApp().run()
