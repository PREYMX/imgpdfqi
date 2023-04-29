# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ImgPdfQi
###########################################################################

class ImgPdfQi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ImgPdfQi", pos = wx.DefaultPosition, size = wx.Size( 415,483 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.filepicker_pdf = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer1.Add( self.filepicker_pdf, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.lbl_server = wx.StaticText( self, wx.ID_ANY, u"Servidor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_server.Wrap( -1 )

		gSizer2.Add( self.lbl_server, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.txtctrl_server = wx.TextCtrl( self, wx.ID_ANY, u"localhost\\COMPAC17", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.txtctrl_server, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl_username = wx.StaticText( self, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_username.Wrap( -1 )

		gSizer2.Add( self.lbl_username, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.txtctrl_username = wx.TextCtrl( self, wx.ID_ANY, u"sa", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.txtctrl_username, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl_psw = wx.StaticText( self, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_psw.Wrap( -1 )

		gSizer2.Add( self.lbl_psw, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.txtctrl_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer2.Add( self.txtctrl_password, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl_database = wx.StaticText( self, wx.ID_ANY, u"Base de datos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_database.Wrap( -1 )

		gSizer2.Add( self.lbl_database, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND, 5 )

		self.lbl_odbc = wx.StaticText( self, wx.ID_ANY, u"Odbc driver", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_odbc.Wrap( -1 )

		gSizer2.Add( self.lbl_odbc, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.txtctrl_odbc = wx.TextCtrl( self, wx.ID_ANY, u"ODBC Driver 17 for SQL Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.txtctrl_odbc, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.btn_test = wx.Button( self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_test, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )

		self.lbl_sql = wx.StaticText( self, wx.ID_ANY, u"Sql", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_sql.Wrap( -1 )

		bSizer1.Add( self.lbl_sql, 0, wx.ALL, 5 )

		self.txtctrl_sql = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1.Add( self.txtctrl_sql, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_ok = wx.Button( self, wx.ID_ANY, u"Procesar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_ok, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


