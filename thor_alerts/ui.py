# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6-dirty)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class PreferencesDialog
###########################################################################

class PreferencesDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Preferences"), pos = wx.DefaultPosition, size = wx.Size( 440,256 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        preferences_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.hub_settings = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        hub_spacer = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText4 = wx.StaticText( self.hub_settings, wx.ID_ANY, _(u"Hub URL"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        hub_spacer.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.input_HubURL = wx.TextCtrl( self.hub_settings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
        hub_spacer.Add( self.input_HubURL, 0, wx.ALL|wx.EXPAND, 5 )


        self.hub_settings.SetSizer( hub_spacer )
        self.hub_settings.Layout()
        hub_spacer.Fit( self.hub_settings )
        self.m_notebook2.AddPage( self.hub_settings, _(u"Hub"), False )
        self.icon_set = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.current_icon_set_label = wx.StaticText( self.icon_set, wx.ID_ANY, _(u"The current iconset is <b>THORICON</b>"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.current_icon_set_label.SetLabelMarkup( _(u"The current iconset is <b>THORICON</b>") )
        self.current_icon_set_label.Wrap( -1 )

        bSizer11.Add( self.current_icon_set_label, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

        self.m_staticText7 = wx.StaticText( self.icon_set, wx.ID_ANY, _(u"Click a button to change your icons!"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer11.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.set_thoricons_button = wx.Button( self.icon_set, wx.ID_ANY, _(u"THORICON"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.set_thoricons_button.SetBitmap( wx.ArtProvider.GetBitmap( "sun-cloud-rain_heavy-lightning", wx.ART_MENU ) )
        bSizer12.Add( self.set_thoricons_button, 1, wx.ALL|wx.EXPAND, 5 )

        self.set_freedesktop_button = wx.Button( self.icon_set, wx.ID_ANY, _(u"Freedesktop"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.set_freedesktop_button.SetBitmap( wx.ArtProvider.GetBitmap( "weather-showers-scattered-storm-day", wx.ART_BUTTON ) )
        self.set_freedesktop_button.Enable( False )

        bSizer12.Add( self.set_freedesktop_button, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )


        self.icon_set.SetSizer( bSizer11 )
        self.icon_set.Layout()
        bSizer11.Fit( self.icon_set )
        self.m_notebook2.AddPage( self.icon_set, _(u"Icons"), True )
        self.notification_settings = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.checkbox_TrayIcon = wx.CheckBox( self.notification_settings, wx.ID_ANY, _(u"Close to system tray"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.checkbox_TrayIcon, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_toggleBtn1 = wx.ToggleButton( self.notification_settings, wx.ID_ANY, _(u"Trigger demo notification"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_toggleBtn1.SetValue( True )
        bSizer7.Add( self.m_toggleBtn1, 0, wx.EXPAND|wx.ALL, 5 )


        self.notification_settings.SetSizer( bSizer7 )
        self.notification_settings.Layout()
        bSizer7.Fit( self.notification_settings )
        self.m_notebook2.AddPage( self.notification_settings, _(u"Notifications"), False )

        preferences_sizer.Add( self.m_notebook2, 1, wx.EXPAND|wx.ALL, 5 )

        dialog_buttons = wx.StdDialogButtonSizer()
        self.dialog_buttonsOK = wx.Button( self, wx.ID_OK )
        dialog_buttons.AddButton( self.dialog_buttonsOK )
        self.dialog_buttonsCancel = wx.Button( self, wx.ID_CANCEL )
        dialog_buttons.AddButton( self.dialog_buttonsCancel )
        dialog_buttons.Realize()

        preferences_sizer.Add( dialog_buttons, 0, wx.SHAPED|wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.SetSizer( preferences_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.set_thoricons_button.Bind( wx.EVT_BUTTON, self.set_thoricon )
        self.set_freedesktop_button.Bind( wx.EVT_BUTTON, self.set_freedesktop )
        self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.on_notification_test )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def set_thoricon( self, event ):
        event.Skip()

    def set_freedesktop( self, event ):
        event.Skip()

    def on_notification_test( self, event ):
        event.Skip()


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Thor"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 500,300 ), wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Thor"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.thor_status_label = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.thor_status_label.Wrap( 1 )

        bSizer4.Add( self.thor_status_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gSizer1 = wx.GridSizer( 0, 2, 0, 5 )

        weather_sizer = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Weather:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        weather_sizer.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.weather_icon = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_NORMAL_FILE, wx.ART_CMN_DIALOG ), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.weather_icon.SetMinSize( wx.Size( 64,64 ) )

        weather_sizer.Add( self.weather_icon, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.weather_headline = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Unknown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.weather_headline.Wrap( -1 )

        self.weather_headline.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        weather_sizer.Add( self.weather_headline, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        gSizer1.Add( weather_sizer, 1, wx.EXPAND, 5 )

        self.alerts_container = wx.ScrolledWindow( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.alerts_container.SetScrollRate( 5, 5 )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


        self.alerts_container.SetSizer( bSizer10 )
        self.alerts_container.Layout()
        bSizer10.Fit( self.alerts_container )
        gSizer1.Add( self.alerts_container, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )


        bSizer8.Add( bSizer4, 1, wx.EXPAND, 5 )

        buttons = wx.BoxSizer( wx.HORIZONTAL )

        self.preferences_button = wx.Button( self.m_panel3, wx.ID_ANY, _(u"Preferences"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.preferences_button.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EDIT, wx.ART_BUTTON ) )
        buttons.Add( self.preferences_button, 0, wx.ALL, 5 )


        buttons.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.close_button = wx.Button( self.m_panel3, wx.ID_CLOSE, _(u"Hide"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.close_button.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_CLOSE, wx.ART_BUTTON ) )
        buttons.Add( self.close_button, 0, wx.ALL, 5 )

        self.quit_button = wx.Button( self.m_panel3, wx.ID_EXIT, _(u"Quit"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.quit_button.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_BUTTON ) )
        buttons.Add( self.quit_button, 0, wx.ALL, 5 )


        bSizer8.Add( buttons, 0, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer8 )
        self.m_panel3.Layout()
        bSizer8.Fit( self.m_panel3 )
        bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer3 )
        self.Layout()
        self.status_update_timer = wx.Timer()
        self.status_update_timer.SetOwner( self, self.status_update_timer.GetId() )
        self.status_update_timer.Start( 1000 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.preferences_button.Bind( wx.EVT_BUTTON, self.show_preferences )
        self.close_button.Bind( wx.EVT_BUTTON, self.on_close )
        self.quit_button.Bind( wx.EVT_BUTTON, self.on_quit )
        self.Bind( wx.EVT_TIMER, self.update_status, id=self.status_update_timer.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def show_preferences( self, event ):
        event.Skip()


    def on_quit( self, event ):
        event.Skip()

    def update_status( self, event ):
        event.Skip()


###########################################################################
## Class AboutFrame
###########################################################################

class AboutFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


