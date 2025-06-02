import wx
from main_frame import MainFrame

class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, title="My Application")
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
