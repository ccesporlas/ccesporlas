import wx

class MainWindow(wx.Frame):
    def __init__(self, parent = None, id = -1, title = "Small Editor"):
        wx.Frame.__init__(
            self, parent, id ,title, size = (400,200),
            style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE
        )
        self.control = wx.TextCtrl(self, -1, style = wx.TE_MULTILINE)
        #--- START NEW CODE: ---------------------------------------------------
        self.CreateStatusBar()
        #------ Setting up the menu.
        filemenu = wx.Menu()
        filemenu.Append(-1, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(-1, "E&xit", "Terminate the program")
        #------ Creating the menu.
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        self.SetMenuBar(menubar)
        #--- END NEW CODE ------------------------------------------------------
        self.Show(True)

app = wx.PySimpleApp()
frame = MainWindow()
app.MainLoop()
