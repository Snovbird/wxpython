import wx
from custom_panel import CustomPanel

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))
        
        # Create a sizer for layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create instances of panels from other modules
        self.panel = CustomPanel(self)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        
        # Set the sizer
        self.SetSizer(self.sizer)
        
        # Create a menu bar
        self.create_menu_bar()
    
    def create_menu_bar(self):
        menu_bar = wx.MenuBar()
        
        # File menu
        file_menu = wx.Menu()
        exit_item = file_menu.Append(wx.ID_EXIT, "Exit", "Exit application")
        
        # Add menus to the menu bar
        menu_bar.Append(file_menu, "File")
        
        # Set the menu bar
        self.SetMenuBar(menu_bar)
        
        # Bind events
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
    
    def on_exit(self, event):
        self.Close()
