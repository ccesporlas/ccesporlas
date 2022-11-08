import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(200, 100))

        wx.StaticText(self, -1, 'r value', (15, 95))
        wx.SpinCtrl(self, -1, '1', min=-120, max=120)
        wx.Button(self, 1, 'Ok', (50, 50), (50, 0))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=1)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnClose(self, event):
        self.Close()

app = wx.App(0)
MyDialog(None, -1, 'vary r value')
app.MainLoop()
