# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6-dirty)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 786,564 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.icon_fd = wx.StaticBitmap( self.m_panel4, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.icon_fd, 0, wx.ALL|wx.EXPAND, 5 )

        self.yr = wx.StaticText( self.m_panel4, wx.ID_ANY, u"yr icon", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.yr.Wrap( -1 )

        bSizer11.Add( self.yr, 0, wx.ALL, 5 )

        self.yr_icon = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.yr_icon, 0, wx.ALL|wx.EXPAND, 5 )

        self.thoricon = wx.StaticText( self.m_panel4, wx.ID_ANY, u"thoricon", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.thoricon.Wrap( -1 )

        bSizer11.Add( self.thoricon, 0, wx.ALL, 5 )

        self.thoricon_value = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.thoricon_value, 0, wx.ALL|wx.EXPAND, 5 )

        self.freedesktop = wx.StaticText( self.m_panel4, wx.ID_ANY, u"freedesktop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.freedesktop.Wrap( -1 )

        bSizer11.Add( self.freedesktop, 0, wx.ALL, 5 )

        self.freedesktop = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.freedesktop, 0, wx.ALL|wx.EXPAND, 5 )

        self.fa_free = wx.StaticText( self.m_panel4, wx.ID_ANY, u"fa-free", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fa_free.Wrap( -1 )

        bSizer11.Add( self.fa_free, 0, wx.ALL, 5 )

        self.fa_free_value = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.fa_free_value, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button7 = wx.Button( self.m_panel4, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button7, 1, wx.ALL, 5 )

        self.m_button5 = wx.Button( self.m_panel4, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button5, 1, wx.ALL, 5 )

        self.m_button6 = wx.Button( self.m_panel4, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button6, 1, wx.ALL, 5 )


        bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )


        bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

        self.icons = wx.TreeCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT )
        bSizer10.Add( self.icons, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_panel4.SetSizer( bSizer10 )
        self.m_panel4.Layout()
        bSizer10.Fit( self.m_panel4 )
        bSizer9.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.yr_icon.Bind( wx.EVT_TEXT, self.update_icon )
        self.thoricon_value.Bind( wx.EVT_TEXT, self.update_icon )
        self.freedesktop.Bind( wx.EVT_TEXT, self.update_icon )
        self.fa_free_value.Bind( wx.EVT_TEXT, self.update_icon )
        self.m_button7.Bind( wx.EVT_BUTTON, self.save )
        self.m_button5.Bind( wx.EVT_BUTTON, self.new )
        self.m_button6.Bind( wx.EVT_BUTTON, self.remove )
        self.icons.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.change_item )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def update_icon( self, event ):
        event.Skip()




    def save( self, event ):
        event.Skip()

    def new( self, event ):
        event.Skip()

    def remove( self, event ):
        event.Skip()

    def change_item( self, event ):
        event.Skip()


