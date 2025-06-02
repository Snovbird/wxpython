import wx
import random
import webbrowser
import datetime
import os
import platform
import subprocess
import threading
import time

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My 10-Button GUI", size=(1000, 400))
        
        # Create a panel to hold all components
        self.panel = wx.Panel(self)
        
        # Create a main sizer with some padding
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Add a title
        title = wx.StaticText(self.panel, label="10-Button Application")
        font = title.GetFont()
        font.SetPointSize(14)
        font.SetWeight(wx.BOLD)
        title.SetFont(font)
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 10)
        
        # Create a grid sizer for buttons (5 rows, 2 columns)
        button_sizer = wx.GridSizer(rows=2, cols=5, vgap=10, hgap=10)
        
        # Create 10 buttons with different functions
        self.create_buttons(button_sizer)
        
        # Status bar at the bottom
        self.status_bar = wx.StatusBar(self.panel)
        self.status_bar.SetStatusText("Ready")
        
        # Add the button grid to the main sizer
        main_sizer.Add(button_sizer, 0, wx.ALL | wx.EXPAND, 20)
        main_sizer.Add(self.status_bar, 0, wx.EXPAND)
        
        # Set the main sizer for the panel
        self.panel.SetSizer(main_sizer)
        
        # Center the window on screen
        self.Centre()
        
    def create_buttons(self, sizer):
        # Button 1: Show Date and Time
        btn1 = wx.Button(self.panel, label="Show Date & Time")
        btn1.Bind(wx.EVT_BUTTON, self.on_show_date_time)
        sizer.Add(btn1, 0, wx.EXPAND)
        
        # Button 2: Random Number Generator
        btn2 = wx.Button(self.panel, label="Generate Random Number")
        btn2.Bind(wx.EVT_BUTTON, self.on_random_number)
        sizer.Add(btn2, 0, wx.EXPAND)
        
        # Button 3: Change Background Color
        btn3 = wx.Button(self.panel, label="Change Background Color")
        btn3.Bind(wx.EVT_BUTTON, self.on_change_color)
        sizer.Add(btn3, 0, wx.EXPAND)
        
        # Button 4: Open Website
        btn4 = wx.Button(self.panel, label="Open Website")
        btn4.Bind(wx.EVT_BUTTON, self.on_open_website)
        sizer.Add(btn4, 0, wx.EXPAND)
        
        # Button 5: Show System Info
        btn5 = wx.Button(self.panel, label="System Info")
        btn5.Bind(wx.EVT_BUTTON, self.on_system_info)
        sizer.Add(btn5, 0, wx.EXPAND)
        
        # Button 6: Calculate
        btn6 = wx.Button(self.panel, label="Calculator")
        btn6.Bind(wx.EVT_BUTTON, self.on_calculator)
        sizer.Add(btn6, 0, wx.EXPAND)
        
        # Button 7: File Browser
        btn7 = wx.Button(self.panel, label="Browse Files")
        btn7.Bind(wx.EVT_BUTTON, self.on_browse_files)
        sizer.Add(btn7, 0, wx.EXPAND)
        
        # Button 8: Timer
        btn8 = wx.Button(self.panel, label="Start 5s Timer")
        btn8.Bind(wx.EVT_BUTTON, self.on_timer)
        sizer.Add(btn8, 0, wx.EXPAND)
        
        # Button 9: Text Input
        btn9 = wx.Button(self.panel, label="Text Input")
        btn9.Bind(wx.EVT_BUTTON, self.on_text_input)
        sizer.Add(btn9, 0, wx.EXPAND)
        
        # Button 10: Exit Application
        btn10 = wx.Button(self.panel, label="Exit")
        btn10.Bind(wx.EVT_BUTTON, self.on_exit)
        sizer.Add(btn10, 0, wx.EXPAND)
    
    # Button 1: Show current date and time
    def on_show_date_time(self, event):
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        wx.MessageBox(f"Current Date and Time:\n{date_time}", "Date & Time")
        self.status_bar.SetStatusText(f"Displayed date and time: {date_time}")
    
    # Button 2: Generate random number
    def on_random_number(self, event):
        random_num = random.randint(1, 100)
        wx.MessageBox(f"Random Number: {random_num}", "Random Generator")
        self.status_bar.SetStatusText(f"Generated random number: {random_num}")
    
    # Button 3: Change background color
    def on_change_color(self, event):
        colors = ['#FFD700', '#FF6347', '#7FFFD4', '#DDA0DD', '#90EE90']
        color = random.choice(colors)
        self.panel.SetBackgroundColour(color)
        self.panel.Refresh()
        self.status_bar.SetStatusText(f"Background color changed to: {color}")
    
    # Button 4: Open website
    def on_open_website(self, event):
        webbrowser.open("https://wxpython.org/")
        self.status_bar.SetStatusText("Opened wxPython website")
    
    # Button 5: Show system info
    def on_system_info(self, event):
        info = f"System: {platform.system()}\n"
        info += f"Version: {platform.version()}\n"
        info += f"Machine: {platform.machine()}\n"
        info += f"Processor: {platform.processor()}"
        
        wx.MessageBox(info, "System Information")
        self.status_bar.SetStatusText("Displayed system information")
    
    # Button 6: Calculator dialog
    def on_calculator(self, event):
        dlg = CalculatorDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.status_bar.SetStatusText("Used calculator")
    
    # Button 7: File browser
    def on_browse_files(self, event):
        dlg = wx.FileDialog(self, "Choose a file", wildcard="*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            wx.MessageBox(f"Selected file: {path}", "File Selected")
            self.status_bar.SetStatusText(f"Selected file: {os.path.basename(path)}")
        dlg.Destroy()
    
    # Button 8: 5-second timer
    def on_timer(self, event):
        self.status_bar.SetStatusText("Timer started for 5 seconds...")
        
        # Using a thread to avoid freezing the UI
        def countdown():
            time.sleep(5)
            # We need to use CallAfter since we're in a different thread
            wx.CallAfter(wx.MessageBox, "5 seconds elapsed!", "Timer")
            wx.CallAfter(self.status_bar.SetStatusText, "Timer completed")
        
        threading.Thread(target=countdown).start()
    
    # Button 9: Text input dialog
    def on_text_input(self, event):
        dlg = wx.TextEntryDialog(self, "Enter some text:", "Text Input")
        if dlg.ShowModal() == wx.ID_OK:
            text = dlg.GetValue()
            if text:
                wx.MessageBox(f"You entered: {text}", "Input Result")
                self.status_bar.SetStatusText(f"Text entered: {text}")
            else:
                wx.MessageBox("No text entered", "Input Result")
        dlg.Destroy()
    
    # Button 10: Exit application
    def on_exit(self, event):
        self.Close()


class CalculatorDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Simple Calculator")
        
        # Create the UI components
        panel = wx.Panel(self)
        
        # Create layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # First number
        num1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.num1_label = wx.StaticText(panel, label="First Number:")
        self.num1_input = wx.TextCtrl(panel)
        num1_sizer.Add(self.num1_label, 0, wx.ALL | wx.CENTER, 5)
        num1_sizer.Add(self.num1_input, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(num1_sizer, 0, wx.EXPAND)
        
        # Second number
        num2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.num2_label = wx.StaticText(panel, label="Second Number:")
        self.num2_input = wx.TextCtrl(panel)
        num2_sizer.Add(self.num2_label, 0, wx.ALL | wx.CENTER, 5)
        num2_sizer.Add(self.num2_input, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(num2_sizer, 0, wx.EXPAND)
        
        # Result
        result_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.result_label = wx.StaticText(panel, label="Result:")
        self.result_text = wx.StaticText(panel, label="")
        result_sizer.Add(self.result_label, 0, wx.ALL | wx.CENTER, 5)
        result_sizer.Add(self.result_text, 1, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(result_sizer, 0, wx.EXPAND)
        
        # Operation buttons
        op_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.add_btn = wx.Button(panel, label="Add")
        self.subtract_btn = wx.Button(panel, label="Subtract")
        self.multiply_btn = wx.Button(panel, label="Multiply")
        self.divide_btn = wx.Button(panel, label="Divide")
        
        op_sizer.Add(self.add_btn, 1, wx.ALL, 5)
        op_sizer.Add(self.subtract_btn, 1, wx.ALL, 5)
        op_sizer.Add(self.multiply_btn, 1, wx.ALL, 5)
        op_sizer.Add(self.divide_btn, 1, wx.ALL, 5)
        
        main_sizer.Add(op_sizer, 0, wx.EXPAND)
        
        # Close button
        self.close_btn = wx.Button(panel, label="Close")
        main_sizer.Add(self.close_btn, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(main_sizer)
        
        # Bind events
        self.add_btn.Bind(wx.EVT_BUTTON, self.on_add)
        self.subtract_btn.Bind(wx.EVT_BUTTON, self.on_subtract)
        self.multiply_btn.Bind(wx.EVT_BUTTON, self.on_multiply)
        self.divide_btn.Bind(wx.EVT_BUTTON, self.on_divide)
        self.close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        
        # Fit dialog to its contents
        self.Fit()
    
    def get_numbers(self):
        try:
            num1 = float(self.num1_input.GetValue())
            num2 = float(self.num2_input.GetValue())
            return num1, num2
        except ValueError:
            wx.MessageBox("Please enter valid numbers", "Error")
            return None, None
    
    def on_add(self, event):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.result_text.SetLabel(str(result))
    
    def on_subtract(self, event):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.result_text.SetLabel(str(result))
    
    def on_multiply(self, event):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.result_text.SetLabel(str(result))
    
    def on_divide(self, event):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                wx.MessageBox("Cannot divide by zero", "Error")
            else:
                result = num1 / num2
                self.result_text.SetLabel(str(result))
    
    def on_close(self, event):
        self.EndModal(wx.ID_CANCEL)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
