'''This is just a trial of WxPython for making UI. Functions are non-operational.'''

import wx, os, sys

class MainWindow(wx.Frame):
    def __init__(self, parent = None, id = -1, title = "Test Editor"):
        wx.Frame.__init__(
                self, parent, id, title, size = (400,200),
                style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE
        )

        self.control = wx.TextCtrl(self, -1, style = wx.TE_MULTILINE)
        self.CreateStatusBar()

        menubar = wx.MenuBar()

        filemenu = wx.Menu()
        filemenu.Append(11, "&Directory..", "Open file from directory")
        filemenu.Append(12, "&Open File..", "Open file from directory")
        filemenu.AppendSeparator()
        filemenu.Append(13, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(14, "&Exit", "Terminate the program")
        menubar.Append(filemenu,"&File")

        self.Bind(wx.EVT_MENU, self.OpenDir, id=11)
        self.Bind(wx.EVT_MENU, self.OpenFile, id=12)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=13)
        self.Bind(wx.EVT_MENU, self.OnExit, id=14)

        editmenu = wx.Menu()
        editmenu.Append(21, "&Color", "Color palette")
        editmenu.Append(22, "&Fonts", "Font options")
        editmenu.Append(23, "&Page Setup", "Page setup")
        menubar.Append(editmenu,"&Edit")

        self.Bind(wx.EVT_MENU, self.ChooseColor, id=21)
        self.Bind(wx.EVT_MENU, self.ChooseFont, id=22)
        self.Bind(wx.EVT_MENU, self.PageSetup, id=23)

        extrasmenu = wx.Menu()
        extrasmenu.Append(31, "&Message", "Put some message in here.")
        extrasmenu.Append(32, "&Selection", "Sample selection")
        extrasmenu.Append(33, "&Toggle", "Number Toggle")
        extrasmenu.Append(34, "&Text Entry", "Enter some text here.")
        menubar.Append(extrasmenu,"&Extras")

        self.Bind(wx.EVT_MENU, self.Message, id=31)
        self.Bind(wx.EVT_MENU, self.SingleChoice, id=32)
        self.Bind(wx.EVT_MENU, self.NumberToggle, id=33)
        self.Bind(wx.EVT_MENU, self.TextEntry, id=34)

        self.SetMenuBar(menubar)
        self.Show(True)

    # TODO: Below methods are not fully functional - fix?

    def OpenDir(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You selected: %s\n' % dlg.GetPath())
        dlg.Destroy()

    def OpenFile(self, event):
        dlg = wx.FileDialog(self, "Mamili ka nga..", os.getcwd(), "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                mypath = os.path.basename(path)
                self.SetStatusText("You selected: %s" % mypath)
        dlg.Destroy()

    def OnAbout(self,event):
        message = "A sample editor\n in wxPython"
        caption = "About Sample Editor"
        wx.MessageBox(message, caption, wx.OK)

    def OnExit(self,event):
        self.Close(True)  # Close the frame.

    def ChooseColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            self.SetStatusText('You selected: %s\n' % str(data.GetColour().Get()))
        dlg.Destroy()

    def ChooseFont(self, event):
        default_font = wx.Font(10, wx.SWISS , wx.NORMAL, wx.NORMAL, False, "Verdana")
        data = wx.FontData()
        if sys.platform == 'win32':
            data.EnableEffects(True)
        data.SetAllowSymbols(False)
        data.SetInitialFont(default_font)
        data.SetRange(10, 30)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetFontData()
            font = data.GetChosenFont()
            color = data.GetColour()
            text = 'Face: %s, Size: %d, Color: %s' % (font.GetFaceName(), font.GetPointSize(),  color.Get())
            self.SetStatusText(text)
        dlg.Destroy()

    def PageSetup(self, event):
        dlg = wx.PageSetupDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetPageSetupData()
            tl = data.GetMarginTopLeft()
            br = data.GetMarginBottomRight()
            self.SetStatusText('Margins are: %s %s' % (str(tl), str(br)))
        dlg.Destroy()

    def Message(self, event):
        dlg = wx.MessageDialog(self, 'Put random message here', 'Attention', wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def SingleChoice(self, event):
        continents = ['Africa','Antarctica','Asia','Europe','North America','Oceania','South America']
        dlg = wx.SingleChoiceDialog(self, '7 World Continents', 'Where?', continents, wx.CHOICEDLG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())
        dlg.Destroy()

    def NumberToggle(self, event):
        # wx.StaticText(self, -1, 'r value', (15, 95))
        # wx.SpinCtrl(self, -1, '1', min=-120, max=120)
        # wx.Button(self, 1, 'Ok', (50, 50), (50, 0))
        dlg = wx.SpinCtrl(self, -1, '1', min=-120, max=120)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())
        dlg.Destroy()

    def TextEntry(self, event):
        dlg = wx.TextEntryDialog(self, 'Write here','Write text')
        dlg.SetValue("Default")
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You entered: %s\n' % dlg.GetValue())
        dlg.Destroy()

class TestApp(wx.App):
    def OnInit(self):
        myframe = MainWindow()
        myframe.CenterOnScreen()
        myframe.Show(True)
        return True

app = TestApp()
app.MainLoop()

# destroying the objects, so that this script works more than once in IDLEdieses Beispiel
#del frame
del app