# experimenting with wxPython's DrawRectangle()
# the rectangle is filled with the brush color
# tested with Python24 and wxPython26     vegaseat    19oct2005

import random
import wx
import time

class MyPanel(wx.Panel):
    """ class MyPanel creates a panel to draw on, inherits wx.Panel """
    def __init__(self, parent, id):
        # create a panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        
        # start the paint event for DrawRectangle() and FloodFill()
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def OnPaint(self, evt):
        """set up the device context (DC) for painting"""
        self.dc = wx.PaintDC(self)
        self.dc.Clear()
        self.dc.BeginDrawing()
        self.dc.SetPen(wx.Pen("BLACK",1))
        # draw a few colorful rectangles ...
        for k in xrange(100):
            # set random RGB color for brush
            r = random.randrange(256)
            g = random.randrange(256)
            b = random.randrange(256)
            self.dc.SetBrush(wx.Brush((r, g, b), wx.SOLID))
            # set random x, y, w, h for rectangle
            w = random.randint(10, width1/2)
            h = random.randint(10, height1/2)
            x = random.randint(0, width1 - w)
            y = random.randint(0, height1 - h)
            self.dc.DrawRectangle(x, y, w, h)
            time.sleep(0.002)  # delay
            str1 = "Drawing %d Rectangles ..." % (99 - k)
            frame.SetTitle(str1)
        self.dc.EndDrawing()
        # free up the device context now
        del self.dc
        
        
height1 = 350
width1 = 400

app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID
frame = wx.Frame(None, -1, "Drawing 99 Rectangles ...", size = (width1, height1))
# call the derived class, -1 is default ID
MyPanel(frame,-1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()
