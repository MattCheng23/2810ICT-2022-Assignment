# -*- coding: utf-8 -*-
import wx
import wx.xrc
import wx.adv


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(350, 400))
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label="Offence-Code :", pos=(20, 30))
        self.editqu = wx.TextCtrl(panel, value="E.g 74703", pos=(20, 50), size=(220, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editqu)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editqu)

        self.quote = wx.StaticText(panel, label="Date:", pos=(20, 80))

        # A button
        self.button = wx.Button(panel, label="Search", pos=(200, 270))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # the edit control - one line version.
        self.lbldd = wx.StaticText(panel, label="DD:", pos=(20, 110))
        self.editdd = wx.TextCtrl(panel, value="01", pos=(100, 110), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editdd)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editdd)

        self.lblmm = wx.StaticText(panel, label="MM:", pos=(20, 140))
        self.editmm = wx.TextCtrl(panel, value="05", pos=(100, 140), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editmm)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editmm)

        self.lblyy = wx.StaticText(panel, label="YYYY:", pos=(20, 170))
        self.edityy = wx.TextCtrl(panel, value="2013", pos=(100, 170), size=(140, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edityy)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.edityy)

        self.lblpe = wx.StaticText(panel, label="Type of Traffic penaty:", pos=(20, 200))
        self.editpe = wx.TextCtrl(panel, value="E.g Speeding", pos=(20, 230), size=(200, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editpe)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editpe)

        self.Show(True)

    def OnClick(self, event):
        print(" Click on object with Id %d\n" % event.GetId())

    def EvtText(self, event):
        print('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        print('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Search For Traffic Penalty")
    app.MainLoop()
