
import wx
import logging

class EditTestFrame(wx.Frame):
    def __init__(self):
        self.logprefix = "EditTestFrame"
        super(EditTestFrame, self).__init__(None, title="Language test", size=(300, 800))

    def start(self, editTest):
        logging.info("{0}:{1}: start".format(self.logprefix, "start"))
        self.editTest = editTest
        self.Bind(wx.EVT_CLOSE, self.when_closed)
        self.SetBackgroundColour('WHITE')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(wx.StaticText(self, label='\nView and edit items:\n'), flag=wx.CENTER)
        grid = wx.FlexGridSizer(2, 4, hgap=20)
        self.firstEditStaticText = wx.StaticText(self)
        self.secondEditStaticText = wx.StaticText(self)
        self.button_switch = wx.Button(self, -1)
        self.Bind(wx.EVT_BUTTON, self.OnDeToEnSwitch, self.button_switch)
        if self.editTest.getDeToEn():
            self.firstEditStaticText.SetLabel('\nGerman:\n')
            self.secondEditStaticText.SetLabel('\nEnglish:\n')
            self.button_switch.SetLabel('Switch to\nEnglish to German')
        else:
            self.firstEditStaticText.SetLabel('\nEnglish:\n')
            self.secondEditStaticText.SetLabel('\nGerman:\n')
            self.button_switch.SetLabel('Switch to\nGerman to English')
        grid.Add(self.firstEditStaticText, flag=wx.CENTER)
        grid.Add(self.secondEditStaticText, flag=wx.CENTER)
        grid.Add(self.button_switch)
        grid.Add(wx.StaticText(self))
        self.firstEditText = wx.TextCtrl(self, size=(250, 50), style = wx.TE_MULTILINE)
        self.secondEditText = wx.TextCtrl(self, size=(250, 50), style = wx.TE_MULTILINE)
        self.button_next_item = wx.Button(self, -1, label='Show first item')
        self.button_previous_item = wx.Button(self, -1, label='Show previous item')
        grid.Add(self.firstEditText, flag=wx.CENTER)
        grid.Add(self.secondEditText, flag=wx.CENTER)
        grid.Add(self.button_next_item, flag=wx.CENTER)
        grid.Add(self.button_previous_item, flag=wx.CENTER)
        vbox.Add(grid, flag=wx.CENTER)
        vbox.Add(wx.StaticText(self, label='\nSearch for an item in the test:\n'), flag=wx.CENTER)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.input_search_term = wx.TextCtrl(self)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnButtonSearchClicked, self.input_search_term)
        hbox.Add(self.input_search_term, 1)
        hbox.AddSpacer(20)
        self.button_search = wx.Button(self, -1, 'Search')
        self.Bind(wx.EVT_BUTTON, self.OnButtonSearchClicked, self.button_search)
        hbox.Add(self.button_search, 1)
        vbox.Add(hbox, flag=wx.CENTER)
        vbox.Add(wx.StaticText(self, label='\nAppend an item to the test:\n'), flag=wx.CENTER)
        grid2 = wx.FlexGridSizer(2, 4, hgap=20)
        self.firstAppendStaticText = wx.StaticText(self)
        self.secondAppendStaticText = wx.StaticText(self)
        self.button_switch2 = wx.Button(self, -1)
        self.Bind(wx.EVT_BUTTON, self.OnDeToEnSwitch, self.button_switch2)
        if self.editTest.getDeToEn():
            self.firstAppendStaticText.SetLabel('\nGerman:\n')
            self.secondAppendStaticText.SetLabel('\nEnglish:\n')
            self.button_switch2.SetLabel('Switch to\nEnglish to German')
        else:
            self.firstAppendStaticText.SetLabel('\nEnglish:\n')
            self.secondAppendStaticText.SetLabel('\nGerman:\n')
            self.button_switch2.SetLabel('Switch to\nGerman to English')
        grid2.Add(self.firstAppendStaticText, flag=wx.CENTER)
        grid2.Add(self.secondAppendStaticText, flag=wx.CENTER)
        grid2.Add(self.button_switch2)
        grid2.Add(wx.StaticText(self), flag=wx.CENTER)
        self.firstAppendText = wx.TextCtrl(self, size=(250, 50), style = wx.TE_MULTILINE)
        self.secondAppendText = wx.TextCtrl(self, size=(250, 50), style = wx.TE_MULTILINE)
        self.button_append_item = wx.Button(self, -1, label='Append')
        grid2.Add(self.firstAppendText, flag=wx.CENTER)
        grid2.Add(self.secondAppendText, flag=wx.CENTER)
        grid2.Add(self.button_append_item, flag=wx.CENTER)
        self.nItems_text = wx.StaticText(self, 
                                         label='Number of items\n      in test: {0}\n'.format(self.editTest.getNumberOfItems()), 
                                         style=wx.ALIGN_LEFT)
        grid2.Add(self.nItems_text, flag=wx.ALIGN_LEFT)
        vbox.Add(grid2, flag=wx.CENTER)
        vbox.Add(wx.StaticText(self, label='\nMultiple item operations:\n'), flag=wx.CENTER)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.button_import = wx.Button(self, -1, 'Import from file')
        self.button_export = wx.Button(self, -1, 'Export to file')
        self.button_clear = wx.Button(self, -1, 'Clear test')
        hbox2.Add((270,-1))
        hbox2.Add(self.button_import, flag=wx.CENTER)
        hbox2.Add((30,-1))
        hbox2.Add(self.button_export, flag=wx.CENTER)
        hbox2.Add((30,-1))
        hbox2.Add(self.button_clear, flag=wx.CENTER)
        hbox2.Add((270,-1))
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER)
        vbox.AddSpacer(60)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        button_quit = wx.Button(self, -1, 'Quit')
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuitClicked, button_quit)
        self.button_start_test = wx.Button(self, -1, 'Start test')
        button_test_selection = wx.Button(self, -1, '<< Back\nto login')
        self.Bind(wx.EVT_BUTTON, self.OnButtonTestSelectionClicked, button_test_selection)
        hbox3.AddSpacer(30)
        hbox3.Add(button_test_selection, 1)
        hbox3.AddSpacer(60)
        hbox3.Add(self.button_start_test, 1)
        hbox3.AddSpacer(60)
        hbox3.Add(button_quit, 1)
        hbox3.AddSpacer(30)
        vbox.Add(hbox3, flag=wx.CENTER)
        if not self.editTest.getNumberOfItems():
            self.firstEditText.Disable()
            self.secondEditText.Disable()
            self.button_switch.Disable()
            self.button_next_item.Disable()
            self.button_previous_item.Disable()
            self.input_search_term.Disable()
            self.button_search.Disable()
            self.button_export.Disable()
            self.button_clear.Disable()
            self.button_start_test.Disable()
        self.SetSizerAndFit(vbox)
        self.Centre()
        self.Show()
        
    def OnDeToEnSwitch(self, event):
        self.editTest.switchDeToEn()
        if self.editTest.getDeToEn():
            logging.info("{0}:{1}: DeToEn: {2}".format(self.logprefix, "OnDeToEnSwitch", "True"))
            self.button_switch.SetLabel('Switch to\nEnglish to German')
            self.button_switch2.SetLabel('Switch to\nEnglish to German')
            self.firstEditStaticText.SetLabel('\nGerman:\n')
            self.secondEditStaticText.SetLabel('\nEnglish:\n')
            self.firstAppendStaticText.SetLabel('\nGerman:\n')
            self.secondAppendStaticText.SetLabel('\nEnglish:\n')
        else:
            logging.info("{0}:{1}: DeToEn: {2}".format(self.logprefix, "OnDeToEnSwitch", "False"))
            self.button_switch.SetLabel('Switch to\nGerman to English')
            self.button_switch2.SetLabel('Switch to\nGerman to English')
            self.firstEditStaticText.SetLabel('\nEnglish:\n')
            self.secondEditStaticText.SetLabel('\nGerman:\n')
            self.firstAppendStaticText.SetLabel('\nEnglish:\n')
            self.secondAppendStaticText.SetLabel('\nGerman:\n')
        
    def OnButtonSearchClicked(self, event):
        logging.info("{0}:{1}: user clicked search".format(self.logprefix, "OnButtonSearchClicked"))

    def OnButtonQuitClicked(self, event):
        logging.info("{0}:{1}: user clicked quit".format(self.logprefix, "OnButtonQuitClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.Hide()
        self.editTest.quit()
        self.Close()

    def OnButtonTestSelectionClicked(self, event):
        logging.info("{0}:{1}: user clicked back to login".format(self.logprefix, "OnButtonTestSelectionClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.Hide()
        self.editTest.back_to_test_selection()
        self.Close()
    
    def when_closed(self, event):
        logging.info("{0}:{1}: user clicked close".format(self.logprefix, "when_closed"))
        self.OnButtonQuitClicked(event)
