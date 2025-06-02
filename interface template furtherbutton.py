import wx

class GridApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Interactive Button Grid", size=(800, 600))
        
        # Main panel
        self.panel = wx.Panel(self)
        
        # Lists to store data
        self.numbers_list = []  # For number button clicks
        self.letters_list = []  # For letter button clicks
        
        # Flag to track current button state (True = numbers, False = letters)
        self.showing_numbers = True
        
        # Store references to buttons for updating labels later
        self.buttons = []
        
        # Create the grid of buttons
        self.create_grid()
        
        # Create status bar
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetStatusText("Ready")
        
        # Center the window
        self.Centre()
        
    def create_grid(self):
        # Create a grid sizer (5 rows, 6 columns)
        grid_sizer = wx.GridSizer(rows=5, cols=6, vgap=5, hgap=5)
        
        # Add buttons 1-25 followed by the 5 special function buttons
        button_count = 1
        for row in range(5):  # 5 rows
            for col in range(6):  # 6 columns
                # Calculate the position in the grid (0-29)
                position = row * 6 + col
                
                if position < 25:
                    # Numbered buttons (1-25)
                    btn = wx.Button(self.panel, label=str(button_count))
                    btn.Bind(wx.EVT_BUTTON, self.on_numbered_button)
                    grid_sizer.Add(btn, 1, wx.EXPAND)
                    self.buttons.append(btn)  # Store reference to button
                    button_count += 1
                else:
                    # Special function buttons
                    func_position = position - 25  # 0-4
                    
                    if func_position == 0:
                        # Button 1: Clear list after confirmation
                        clear_btn = wx.Button(self.panel, label="Clear List")
                        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear_list)
                        grid_sizer.Add(clear_btn, 1, wx.EXPAND)
                    elif func_position == 1:
                        # Button 2: Toggle between numbers and letters
                        self.toggle_btn = wx.Button(self.panel, label="Switch to Letters")
                        self.toggle_btn.Bind(wx.EVT_BUTTON, self.on_toggle_buttons)
                        grid_sizer.Add(self.toggle_btn, 1, wx.EXPAND)
                    elif func_position == 2:
                        # Button 3: Show list
                        show_btn = wx.Button(self.panel, label="Show List")
                        show_btn.Bind(wx.EVT_BUTTON, self.on_show_list)
                        grid_sizer.Add(show_btn, 1, wx.EXPAND)
                    elif func_position == 3:
                        # Button 4: Placeholder
                        placeholder_btn = wx.Button(self.panel, label="Placeholder")
                        placeholder_btn.Bind(wx.EVT_BUTTON, self.on_placeholder)
                        grid_sizer.Add(placeholder_btn, 1, wx.EXPAND)
                    elif func_position == 4:
                        # Button 5: Exit
                        exit_btn = wx.Button(self.panel, label="Exit")
                        exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)
                        grid_sizer.Add(exit_btn, 1, wx.EXPAND)
        
        # Set the sizer for the panel
        self.panel.SetSizer(grid_sizer)
    
    def on_numbered_button(self, event):
        # Get the button
        btn = event.GetEventObject()
        label = btn.GetLabel()
        
        if self.showing_numbers:
            # Add to numbers list
            data = {"Row": "1", "Type": label}
            self.numbers_list.append(data)
            self.status_bar.SetStatusText(f"Added number: {data}")
        else:
            # Add to letters list
            data = {"Row": "1", "Type": label}
            self.letters_list.append(data)
            self.status_bar.SetStatusText(f"Added letter: {data}")
    
    def on_toggle_buttons(self, event):
        # Toggle between numbers and letters
        self.showing_numbers = not self.showing_numbers
        
        if self.showing_numbers:
            # Change to numbers (1-25)
            self.toggle_btn.SetLabel("Switch to Letters")
            for i, btn in enumerate(self.buttons):
                btn.SetLabel(str(i + 1))
                btn.SetBackgroundColour(wx.NullColour)  # Reset to default color (white)
            self.status_bar.SetStatusText("Switched to numbers")
        else:
            # Change to letters (a-y)
            self.toggle_btn.SetLabel("Switch to Numbers")
            for i, btn in enumerate(self.buttons):
                # ASCII: 'a' is 97, so we add 97 to get letters a-y
                letter = chr(97 + i)
                btn.SetLabel(letter)
                btn.SetBackgroundColour("#FFD580")  # Light orange color
            self.status_bar.SetStatusText("Switched to letters")
        
        # Refresh the panel to update button appearance
        self.panel.Refresh()
    
    def on_clear_list(self, event):
        # Show confirmation dialog
        dlg = wx.MessageDialog(
            self, 
            "Are you sure you want to clear the lists?",
            "Confirmation",
            wx.YES_NO | wx.ICON_QUESTION
        )
        
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            # Clear the lists
            self.numbers_list.clear()
            self.letters_list.clear()
            self.status_bar.SetStatusText("Lists cleared")
        
        dlg.Destroy()
    
    def on_show_list(self, event):
        # Create a new frame to display the lists
        list_frame = ListFrame(self, self.numbers_list, self.letters_list)
        list_frame.Show()
    
    def on_placeholder(self, event):
        # Show a placeholder message
        dlg = wx.MessageDialog(
            self,
            "placeholder",
            "Placeholder",
            wx.OK | wx.ICON_INFORMATION
        )
        dlg.ShowModal()
        dlg.Destroy()
    
    def on_exit(self, event):
        # Close the application
        self.Close()


class ListFrame(wx.Frame):
    def __init__(self, parent, numbers_list, letters_list):
        super().__init__(parent, title="Lists Contents", size=(500, 400))
        
        panel = wx.Panel(self)
        
        # Create a notebook with tabs
        notebook = wx.Notebook(panel)
        
        # Create pages for each list
        numbers_page = wx.Panel(notebook)
        letters_page = wx.Panel(notebook)
        
        # Add text controls to each page
        numbers_text = wx.TextCtrl(
            numbers_page,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
        )
        
        letters_text = wx.TextCtrl(
            letters_page,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
        )
        
        # Format and display numbers list
        numbers_content = ""
        for i, item in enumerate(numbers_list):
            numbers_content += f"Item {i+1}: {item}\n"
        
        if not numbers_content:
            numbers_content = "Numbers list is empty"
            
        numbers_text.SetValue(numbers_content)
        
        # Format and display letters list
        letters_content = ""
        for i, item in enumerate(letters_list):
            letters_content += f"Item {i+1}: {item}\n"
        
        if not letters_content:
            letters_content = "Letters list is empty"
            
        letters_text.SetValue(letters_content)
        
        # Set sizers for both pages
        numbers_sizer = wx.BoxSizer(wx.VERTICAL)
        numbers_sizer.Add(numbers_text, 1, wx.ALL | wx.EXPAND, 10)
        numbers_page.SetSizer(numbers_sizer)
        
        letters_sizer = wx.BoxSizer(wx.VERTICAL)
        letters_sizer.Add(letters_text, 1, wx.ALL | wx.EXPAND, 10)
        letters_page.SetSizer(letters_sizer)
        
        # Add the pages to the notebook
        notebook.AddPage(numbers_page, "Numbers")
        notebook.AddPage(letters_page, "Letters")
        
        # Main sizer for the panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 10)
        
        # Add a close button
        close_btn = wx.Button(panel, label="Close")
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        main_sizer.Add(close_btn, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(main_sizer)
        
        # Center the window relative to the parent
        self.Centre()
    
    def on_close(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = GridApp()
    frame.Show()
    app.MainLoop()
