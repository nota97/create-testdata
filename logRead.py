import wx  # 导入wxPython
import logdataread
import os


class Frame(wx.Frame):  # 定义GUI框架类

    wildcard = '文本文件(*.txt)|*.txt|所有文件(*.*)|*.*'

    # 框架初始化方法


    def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition,

                 title='日志关键字搜索展示'):

        wx.Frame.__init__(self, parent, id, title,

                          pos, size=(600, 300))

        self.panel = wx.Panel(self)

        self.openBtn = wx.Button(self.panel, -1, '请选择日志文件', pos=(50, 100))

        self.openBtn.Bind(wx.EVT_BUTTON, self.OnOpen)

        self.saveAsBtn = wx.Button(self.panel, -1, '另存为', pos=(200, 100))

        self.saveAsBtn.Bind(wx.EVT_BUTTON, self.OnSaveAs)

        self.st1 = wx.StaticText(self.panel, label="请输入关键字：", pos=(50,155))
        self.tx1 = wx.TextCtrl(self.panel, pos=(150,150))
        self.bt1 = wx.Button(self.panel, label="查询", id=1, pos=(300,150))
        self.Bind(wx.EVT_BUTTON, self.btn_click)
        self.file = ""
        self.savefile =""
        self.numinterval = wx.StaticText(self.panel, label="", pos=(50,200))


    def OnOpen(self, event):

        dlg = wx.FileDialog(self, message='打开文件',

                            defaultDir='',

                            defaultFile='',

                            wildcard=self.wildcard,

                            style=wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.file = dlg.GetPath()

            dlg.Destroy()

    def OnSaveAs(self, event):

        dlg = wx.FileDialog(self, '另存为', os.getcwd(),

                            defaultFile='我的文件.txt',

                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,

                            wildcard=self.wildcard)

        if dlg.ShowModal() == wx.ID_OK:
            self.savefile = dlg.GetPath()

            dlg.Destroy()

    def btn_click(self, event):
        id = event.GetId()
        if id == 1 and self.file != "":
            num = logdataread.logdataread().GetSecordinterval(self.file, self.tx1.GetValue())
            interval="最大时间差:"+str(num)
            self.numinterval.SetLabel(interval)
            data = logdataread.logdataread().GetLogKeyWordData(self.file, self.tx1.GetValue())
            frame1 = nameFrame()
            frame1.Show()
            logdata=""
            for i in data:
                frame1.st2.AppendText(str(i))
        else:
            print("请选择日志文件")


class App(wx.App):  # 定义应用程序类

    def OnInit(self):  # 类初始化方法

        self.frame = Frame()

        self.frame.Show(True)

        self.SetTopWindow(self.frame)  # 设置顶层框架

        return True


class nameFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title="关键字日志",
            size=(800, 1000)
        )
        self.panel = wx.Panel(parent=self)
        self.st1 = wx.StaticText(self.panel, label="")
        self.st2 = wx.TextCtrl(self.panel, size = (770,950),style=wx.TE_MULTILINE )
        # self.box = wx.StaticBox(self.panel, label="")


def main():  # 定义主函数用于启动GUI界面

    app = App()

    app.MainLoop()


if __name__ == '__main__':  # 使用__name__检测当前模块

    main()
