'''This is just a trial of WxPython for making UI'''

import wx, scipy
import wx.lib.plot as plot

class Plot(wx.Dialog):
    def __init__(self, parent, id, title = "Bifurcation Diagram"):
        wx.Dialog.__init__(self, parent, id, title, size = (200,150))

        self.data = []

        # TODO: make variables N and x adjustable using SpinCtrl
        # dlg = wx.SpinCtrl(self, -1, '1', min=-120, max=120)

        N = 500
        rrange = scipy.linspace(0,1.,N)
        for r in rrange:
            x = 0.65

            for t in range(100):
                y = 4*r*x*(1-x)
                self.data.append((r,y))
                x = y

        btn1 = wx.Button(self,1,'Bifurcation Diagram',(30,30))
        btn4 = wx.Button(self,4,'Quit',(70,80))
        wx.EVT_BUTTON(self,1,self.OnScatter)
        wx.EVT_BUTTON(self,4,self.OnQuit)
        wx.EVT_CLOSE(self,self.OnQuit)

    def OnScatter(self,event):
        frm = wx.Frame(self,-1,'Bifurcation Diagram',size=(600,450))
        client = plot.PlotCanvas(frm)
        markers = plot.PolyMarker(self.data,legend='',colour='red',marker='circle',size=0.2)
        gc = plot.PlotGraphics([markers],'Bifurcation Diagram','r','x')
        client.Draw(gc, xAxis=(0,1), yAxis=(0,1))
        frm.Show(True)

    def OnQuit(self,event):
        self.Destroy()

class TestApp(wx.App):
    def OnInit(self):
        dlg = Plot(None,-1,'Iterations')
        dlg.Show(True)
        return True

app = TestApp(0)
app.MainLoop()

# destroying the objects, so that this script works more than once in IDLEdieses Beispiel
#del frame
del app