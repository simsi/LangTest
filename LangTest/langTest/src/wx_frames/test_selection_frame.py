
import wx
import logging

class InformTestExistsPopupWindow(wx.Frame):
    def __init__(self, parent):
        self.logprefix = "InformTestExistsPopupWindow"
        super(InformTestExistsPopupWindow, self).__init__(parent, size=(300, 160))

    def start(self, user_name):
        logging.info("{0}:{1}: start".format(self.logprefix, "start"))
        self.Bind(wx.EVT_CLOSE, self.when_closed)
        self.SetBackgroundColour('WHITE')
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(30)
        hbox.Add(wx.StaticText(self, id=-1, label="\nTest \"" + user_name + "\" already exists,\nplease choose a different test name\n", style=wx.ALIGN_CENTER), flag=wx.CENTER)
        hbox.AddSpacer(30)
        vbox.Add(hbox)
        button_ok = wx.Button(self, -1, 'OK')
        self.Bind(wx.EVT_BUTTON, self.OnButtonOKClicked, button_ok)
        vbox.Add(button_ok, 1, flag=wx.CENTER)
        vbox.Add(wx.StaticText(self, style=wx.ALIGN_CENTER), flag=wx.CENTER)
        self.SetSizerAndFit(vbox)
        self.Centre()
        self.Raise()
        self.MakeModal(True)
        self.Show()

    def OnButtonOKClicked(self, event):
        logging.info("{0}:{1}: user clicked OK".format(self.logprefix, "OnButtonOKClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.MakeModal(False)
        self.Close()

    def when_closed(self, event):
        logging.info("{0}:{1}: user clicked close".format(self.logprefix, "when_closed"))
        self.OnButtonOKClicked(event)

class CreateTestPopupWindow(wx.Frame):
    def __init__(self, parent):
        self.logprefix = "CreateTestPopupWindow"
        super(CreateTestPopupWindow, self).__init__(parent, size=(300, 160))
        
    def start(self, test_name, parent):
        logging.info("{0}:{1}: start".format(self.logprefix, "start"))
        self.parent = parent
        self.test_name = test_name
        self.Bind(wx.EVT_CLOSE, self.when_closed)
        self.SetBackgroundColour('WHITE')
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.StaticText(self, id=-1, label="\nCreate new test \"" + test_name + "\"?\n", style=wx.ALIGN_CENTER), flag=wx.CENTER)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(20)
        button_create = wx.Button(self, -1, 'Create\nand edit')
        self.Bind(wx.EVT_BUTTON, self.OnButtonCreateClicked, button_create)
        hbox.Add(button_create, 1)
        hbox.AddSpacer(20)
        button_dismiss = wx.Button(self, -1, 'Dismiss')
        self.Bind(wx.EVT_BUTTON, self.OnButtonDismissClicked, button_dismiss)
        hbox.Add(button_dismiss, 1)
        hbox.AddSpacer(20)
        box.Add(hbox, flag=wx.CENTER)
        box.Add(wx.StaticText(self, style=wx.ALIGN_CENTER), flag=wx.CENTER)
        self.SetSizerAndFit(box)
        self.Centre()
        self.Raise()
        self.MakeModal(True)
        self.Show()

    def OnButtonCreateClicked(self, event):
        logging.info("{0}:{1}: creating test name: {2}".format(self.logprefix, "OnButtonCreateClicked", self.test_name))
        self.MakeModal(False)
        self.Hide()
        self.parent.create_test(self.test_name)
        self.Close()

    def OnButtonDismissClicked(self, event):
        logging.info("{0}:{1}: user clicked dismiss".format(self.logprefix, "OnButtonDismissClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.MakeModal(False)
        self.Close()
        
    def when_closed(self, event):
        logging.info("{0}:{1}: user clicked close".format(self.logprefix, "when_closed"))
        self.OnButtonDismissClicked(event)

class TestSelectionFrame(wx.Frame):
    def __init__(self):
        self.logprefix = "TestSelectionFrame"
        super(TestSelectionFrame, self).__init__(None, title="Language test", size=(300, 300))

    def start(self, testSelection):
        logging.info("{0}:{1}: start".format(self.logprefix, "start"))
        self.testSelection = testSelection
        self.Bind(wx.EVT_CLOSE, self.when_closed)
        self.SetBackgroundColour('WHITE')
        self.button_to_test_id = dict()
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(wx.StaticText(self, id=-1, label="      ", style=wx.ALIGN_CENTER))
        vbox = wx.BoxSizer(wx.VERTICAL)
        tests = testSelection.get_tests()
        logging.info("{0}:{1}: found {2} tests".format(self.logprefix, "start", len(tests)))
        if tests:
            vbox.Add(wx.StaticText(self, label='\nChoose a test:\n'), flag=wx.CENTER)
            length = 0
            for test in tests:
                if test[4]:
                    length += len(test[4])
                else:
                    length += 1
            grid = wx.FlexGridSizer(length + 1, 7, hgap=50, vgap=10)
            grid.Add(wx.StaticText(self, id=-1, label="\nTest name", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, label="\nCreated on", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, label="\nNumber of items", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, label="\nScore", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, label="\nScore (%)", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, label="\nDone on", style=wx.ALIGN_CENTER))
            grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
            for test in tests:
                grid.Add(wx.StaticText(self, id=-1, label="  " + test[0], style=wx.ALIGN_CENTER))
                grid.Add(wx.StaticText(self, id=-1, label="  " + test[2], style=wx.ALIGN_CENTER))
                grid.Add(wx.StaticText(self, id=-1, label="  " + str(test[3]), style=wx.ALIGN_CENTER))
                isFirst = True
                for score in test[4]:
                    if not isFirst:
                        grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                        grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                        grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                    grid.Add(wx.StaticText(self, id=-1, label=str(score[0]), style=wx.ALIGN_CENTER))
                    grid.Add(wx.StaticText(self, id=-1, label=str(int(((score[0]/float(test[3])) * 100) + 0.5)), style=wx.ALIGN_CENTER))
                    grid.Add(wx.StaticText(self, id=-1, label=score[1], style=wx.ALIGN_CENTER))
                    if isFirst:
                        self.addSelectButton(grid, test[1])
                        isFirst = False
                    else:
                        grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                if isFirst:
                    grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                    grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                    grid.Add(wx.StaticText(self, id=-1, style=wx.ALIGN_CENTER))
                    self.addSelectButton(grid, test[1])
            vbox.Add(grid)
        vbox.Add(wx.StaticText(self, label='\nCreate a new test:\n'), flag=wx.CENTER)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.input_create_test = wx.TextCtrl(self)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnButtonCreateClicked, self.input_create_test)
        hbox.Add(self.input_create_test, 1)
        hbox.AddSpacer(20)
        button_create = wx.Button(self, -1, 'Create')
        self.Bind(wx.EVT_BUTTON, self.OnButtonCreateClicked, button_create)
        hbox.Add(button_create, 1)
        vbox.Add(hbox, flag=wx.CENTER)
        vbox.AddSpacer(60)
        button_quit = wx.Button(self, -1, 'Quit')
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuitClicked, button_quit)
        button_login = wx.Button(self, -1, '<< Back\nto login')
        self.Bind(wx.EVT_BUTTON, self.OnButtonLoginClicked, button_login)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.AddSpacer(30)
        hbox2.Add(button_login, 1)
        hbox2.AddSpacer(60)
        hbox2.Add(button_quit, 1)
        hbox2.AddSpacer(30)
        vbox.Add(hbox2, flag=wx.CENTER)
        vbox.Add(wx.StaticText(self), flag=wx.CENTER)
        hbox3.Add(vbox, flag=wx.CENTER)
        hbox3.Add(wx.StaticText(self, id=-1, label="      ", style=wx.ALIGN_CENTER))
        self.SetSizerAndFit(hbox3)
        self.Centre()
        self.Show()

    def addSelectButton(self, grid, test_id):
        button_select = wx.Button(self, -1, 'Do test')
        self.Bind(wx.EVT_BUTTON, self.OnButtonSelectClicked, button_select)
        logging.info("{0}:{1}: select button has id: {2}".format(self.logprefix, "start", id(button_select)))
        self.button_to_test_id[id(button_select)] = test_id
        grid.Add(button_select)

    def OnButtonSelectClicked(self, event):
        self.Unbind(wx.EVT_CLOSE)
        self.Hide()
        self.testSelection.set_test_id(self.button_to_test_id[id(event.GetEventObject())])
        self.Close()

    def OnButtonCreateClicked(self, event):
        value = self.input_create_test.GetValue()
        if value:
            if not self.testSelection.test_exists(value):
                logging.info("{0}:{1}: test: {2} does not exist".format(self.logprefix, "OnButtonCreateClicked", value))
                self.testSelection.prompt_new_test(value)
            else:
                logging.info("{0}:{1}: test: {2} exists".format(self.logprefix, "OnButtonCreateClicked", value))
                self.testSelection.inform_test_exists(value)

    def when_closed(self, event):
        logging.info("{0}:{1}: user clicked close".format(self.logprefix, "when_closed"))
        self.OnButtonQuitClicked(event)

    def OnButtonQuitClicked(self, event):
        logging.info("{0}:{1}: user clicked quit".format(self.logprefix, "OnButtonQuitClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.Hide()
        self.testSelection.quit()
        self.Close()

    def OnButtonLoginClicked(self, event):
        logging.info("{0}:{1}: user clicked back to login".format(self.logprefix, "OnButtonLoginClicked"))
        self.Unbind(wx.EVT_CLOSE)
        self.Hide()
        self.testSelection.back_to_login()
        self.Close()
    
    def finish(self):
        logging.info("{0}:{1}: finish".format(self.logprefix, "finish"))
        self.Unbind(wx.EVT_CLOSE)
        self.Close()
        