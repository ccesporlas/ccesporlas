import wx

class ButtonColumn ( wxPanel ):
    '''Create aligned column of equal-sized buttons with distinct labels and OnClick destinations.

    Illustrates use of nested classes for creating a collection of controls.
    '''
    class aButton ( wxButton ):
        '''Nested button class for use by ButtonColumn class.'''
        def __init__ ( self, parent, label, whotocall ):
            """Expects reference to 'ButtonColumn', list of labels for buttons and list of functions to be called for OnClick events"""
            id = wxNewId ( )
            wxButton.__init__ ( self, parent, id, label, wxDefaultPosition, wxDefaultSize, 1 )
            self.whotocall = whotocall
            EVT_BUTTON ( self, id, self.OnClick )

        def OnClick ( self, event ):
            if self.whotocall: self.whotocall ( )

    def __init__ ( self, parent, width, buttons, Bottom = 0 ):
        """Expects reference to 'parent' of 'ButtonColumn', button column 'width', list of button descriptor tuples, and number of buttons to be displayed at the bottom of the column.

        Each button descriptor consists of a label for the button and a reference to the function to be called when the button is clicked.
        """
        wxPanel.__init__ ( self, parent, -1, wxDefaultPosition, ( 100, 200 ) )
        self.parent = parent

        """Create the upper collection of buttons"""
        previous = None
        for button in buttons [ 0 : len ( buttons ) -Bottom ]:
            oneButton = self.aButton ( self, button [ 0 ], button [ 1 ] )
            lc = wxLayoutConstraints ( )
            lc.left.SameAs ( self, wxLeft, 5 )
            lc.right.SameAs ( self, wxRight, 5 )
            lc.height.AsIs ( )
            if previous: lc.top.SameAs ( previous, wxBottom, 5 )
            else: lc.top.SameAs ( self, wxTop, 5 )
            oneButton.SetConstraints ( lc )
            previous = oneButton

        """Create the lower collection of buttons"""
        buttons.reverse ( )
        previous = None
        for button in buttons [ 0 : Bottom ]:
            oneButton = self.aButton ( self, button [ 0 ], button [ 1 ] )
            lc = wxLayoutConstraints ( )
            lc.left.SameAs ( self, wxLeft, 5 )
            lc.right.SameAs ( self, wxRight, 5 )
            lc.height.AsIs ( )
            if previous: lc.bottom.SameAs ( previous, wxTop, 5 )
            else: lc.bottom.SameAs ( self, wxBottom, 5 )
            oneButton.SetConstraints ( lc )
            previous = oneButton

if __name__ == '__main__':
    class TestFrame(wxFrame):
        def __init__(self):
            wxFrame.__init__ (
                self, None, -1, "Button Column Test",
                size = ( 450, 300 ),
                style = wxDEFAULT_FRAME_STYLE | wxNO_FULL_REPAINT_ON_RESIZE
                )
            self.SetAutoLayout ( true )
            buttons = [
                ( 'OK', self.OKClicked, ),
                ( 'Cancel', self.CancelClicked, ),
                ( 'Re-invert', self.ReinvertClicked, ),
                ( 'Exit', self.ExitClicked, ),
                ]

            self.tp = ButtonColumn ( self, 45, buttons, 2 )
            lc = wxLayoutConstraints ( )
            lc.right.SameAs ( self, wxRight)
            lc.width.AsIs ( )
            lc.top.SameAs ( self, wxTop )
            lc.bottom.SameAs ( self, wxBottom )
            self.tp.SetConstraints ( lc )

            self.CreateStatusBar ( )

        def OKClicked ( self ):
            print("OKClicked")

        def CancelClicked ( self ):
            print("CancelClicked")

        def ReinvertClicked ( self ):
            print("ReInvertClicked")

        def ExitClicked ( self ):
            self.Close ( )

    app = wxPySimpleApp()
    frame = TestFrame()
    frame.Show(true)
    app.MainLoop()
