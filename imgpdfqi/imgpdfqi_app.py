import wx
from imgpdfqi.i_gui_app import ImgPdfQiGui


def main():
    app = wx.App()
    frame = ImgPdfQiGui(None)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
