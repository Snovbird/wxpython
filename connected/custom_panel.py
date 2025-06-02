import wx

class CustomPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create some controls
        self.text = wx.StaticText(self, label="Enter your name:")
        self.input = wx.TextCtrl(self)
        self.button = wx.Button(self, label="Say Hello")
        
        # Create a sizer for layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, 0, wx.ALL, 5)
        sizer.Add(self.input, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.button, 0, wx.ALL, 5)
        
        # Set the sizer
        self.SetSizer(sizer)
        
        # Bind events
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
    
    def on_button_click(self, event):
        name = self.input.GetValue()
        if name:
            wx.MessageBox(f"Hello, {name}!", "Greeting")
        else:
            wx.MessageBox("Please enter your name first!", "Warning")
