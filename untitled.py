#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):

    arr = ""
    length = 0

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()


    def operations(self, arr):
        def addition(x,y):
            total = float(x) + float(y)
            total = str(total)
            self.display.WriteText(total)
            return (str(total))
        def subtraction(x,y):
            total = float(x) - float(y)
            total = str(total)
            self.display.WriteText(total)
        def multiplication(x,y):
            i = 0
            total = 0
            while int(i) <= int(y-1):
                total += x
                i += 1
            total = str(total)
            self.display.WriteText(total)
            return (str(float(total)))
        def division(x,y):
            i = float(x) / float(y)
            i = str(i)
            self.display.WriteText(i)
        def exponents(x,y):
            i = 1
            count = 0
            x = float(x)
            y = float(y)
            while count < y:
                count += 1
                i *= x
                power = i
                if count == y:
                    power = str(power)
                    self.display.WriteText(power)
        def modulo(x,y):
            i = float(x) % float(y)
            i = str(i)
            self.display.WriteText(i)
        def bin_octal(x):
            x = str(x)
            if "." in x:
                [side_a, side_b] = str(x).split(".")
                count = 0
                output1 = ""
                output2 = ""

                if len(side_a) % 3 == 1:
                    side_a = side_a + "00"
                elif len(side_a) % 3 == 2:
                    side_a = side_a + "0"

                if len(side_b) % 3 == 1:
                    side_b = side_b + "00"
                elif len(side_b) % 3 == 2:
                    side_b = side_b + "0"

                for index in range(0, len(side_a), 3):
                    cur_group = side_a[index: index+3]
                    if cur_group == "000":
                        output1 = output1 + "0"
                    elif cur_group == "001":
                        output1 = output1 + "1"
                    elif cur_group == "010":
                        output1 = output1 + "2"
                    elif cur_group == "011":
                        output1 = ouput1 + "3"
                    elif cur_group == "100":
                        output1 = output1 + "4"
                    elif cur_group == "101":
                        output1 = output1 + "5"
                    elif cur_group == "110":
                        output1 = output1 + "6"
                    elif cur_group == "111":
                        output1 = output1 + "7"

                for index in range(0, len(side_b), 3):
                    cur_group = side_b[index: index + 3]
                    if cur_group == "000":
                        output2 = output2 + "0"
                    elif cur_group == "001":
                        output2 = output2 + "1"
                    elif cur_group == "010":
                        output2 = output2 + "2"
                    elif cur_group == "011":
                        output2 = ouput2 + "3"
                    elif cur_group == "100":
                        output2 = output2 + "4"
                    elif cur_group == "101":
                        output2 = output2 + "5"
                    elif cur_group == "110":
                        output2 = output2 + "6"
                    elif cur_group == "111":
                        output2 = output2 + "7"

                self.display.WriteText(output1 + "." + output2)

                count += 3
            else:
                side_a = str(x)
                count = 0
                output1 = ""
                output2 = ""

                if len(side_a) % 3 == 1:
                    side_a = side_a + "00"
                elif len(side_a) % 3 == 2:
                    side_a = side_a + "0"

                for index in range(0, len(side_a), 3):
                    cur_group = side_a[index: index+3]
                    if cur_group == "000":
                        output1 = output1 + "0"
                    elif cur_group == "001":
                        output1 = output1 + "1"
                    elif cur_group == "010":
                        output1 = output1 + "2"
                    elif cur_group == "011":
                        output1 = ouput1 + "3"
                    elif cur_group == "100":
                        output1 = output1 + "4"
                    elif cur_group == "101":
                        output1 = output1 + "5"
                    elif cur_group == "110":
                        output1 = output1 + "6"
                    elif cur_group == "111":
                        output1 = output1 + "7"

                self.display.WriteText(output1 + "." + output2)

                count += 3
        def binhexd(x):
            x = str(x)
            if "." in x:
                [side_a, side_b] = str(x).split(".")
                count = 0
                output1 = ""
                output2 = ""

                if len(side_a) % 4 == 1:
                    side_a = side_a + "000"
                elif len(side_a) % 4 == 2:
                    side_a = side_a + "00"
                elif len(side_a) % 4 == 3:
                    side_a = side_a + "0"

                if len(side_b) % 4 == 1:
                    side_b = side_b + "000"
                elif len(side_b) % 4 == 2:
                    side_b = side_b + "00"
                elif len(side_b) % 4 == 3:
                    side_b = side_b + "0"

                for index in range(0, len(side_a), 4):
                    cur_group = side_a[index: index + 4]
                    if cur_group == "0000":
                        output1 = output1 + "0"
                    elif cur_group == "0001":
                        output1 = output1 + "1"
                    elif cur_group == "0010":
                        output1 = output1 + "2"
                    elif cur_group == "0011":
                        output1 = ouput1 + "3"
                    elif cur_group == "0100":
                        output1 = output1 + "4"
                    elif cur_group == "0101":
                        output1 = output1 + "5"
                    elif cur_group == "0110":
                        output1 = output1 + "6"
                    elif cur_group == "0111":
                        output1 = output1 + "7"
                    elif cur_group == "1000":
                        output1 = output1 + "8"
                    elif cur_group == "1001":
                        output1 = output1 + "9"
                    elif cur_group == "1010":
                        output1 = output1 + "A"
                    elif cur_group == "1011":
                        output1 = output1 + "B"
                    elif cur_group == "1100":
                        output1 = output1 + "C"
                    elif cur_group == "1101":
                        output1 = output1 + "D"
                    elif cur_group == "1110":
                        output1 = output1 + "E"
                    elif cur_group == "1111":
                        output1 = output1 + "F"

                for index in range(0, len(side_b), 4):
                    cur_group = side_b[index: index + 4]
                    if cur_group == "0000":
                        output2 = output2 + "0"
                    elif cur_group == "0001":
                        output2 = output2 + "1"
                    elif cur_group == "0010":
                        output2 = output2 + "2"
                    elif cur_group == "0011":
                        output2 = ouput2 + "3"
                    elif cur_group == "0100":
                        output2 = output2 + "4"
                    elif cur_group == "0101":
                        output2 = output2 + "5"
                    elif cur_group == "0110":
                        output2 = output2 + "6"
                    elif cur_group == "0111":
                        output2 = output2 + "7"
                    elif cur_group == "1000":
                        output2 = output2 + "8"
                    elif cur_group == "1001":
                        output2 = output2 + "9"
                    elif cur_group == "1010":
                        output2 = output2 + "A"
                    elif cur_group == "1011":
                        output2 = output2 + "B"
                    elif cur_group == "1100":
                        output2 = output2 + "C"
                    elif cur_group == "1101":
                        output2 = output2 + "D"
                    elif cur_group == "1110":
                        output2 = output2 + "E"
                    elif cur_group == "1111":
                        output2 = output2 + "F"

                    self.display.WriteText(output1 + "." + output2)

                    count += 4
            else:
                [side_a] = str(x)
                count = 0
                output1 = ""
                output2 = ""

                if len(side_a) % 4 == 1:
                    side_a = side_a + "000"
                elif len(side_a) % 4 == 2:
                    side_a = side_a + "00"
                elif len(side_a) % 4 == 3:
                    side_a = side_a + "0"

                for index in range(0, len(side_a), 4):
                    cur_group = side_a[index: index + 4]
                    if cur_group == "0000":
                        output1 = output1 + "0"
                    elif cur_group == "0001":
                        output1 = output1 + "1"
                    elif cur_group == "0010":
                        output1 = output1 + "2"
                    elif cur_group == "0011":
                        output1 = ouput1 + "3"
                    elif cur_group == "0100":
                        output1 = output1 + "4"
                    elif cur_group == "0101":
                        output1 = output1 + "5"
                    elif cur_group == "0110":
                        output1 = output1 + "6"
                    elif cur_group == "0111":
                        output1 = output1 + "7"
                    elif cur_group == "1000":
                        output1 = output1 + "8"
                    elif cur_group == "1001":
                        output1 = output1 + "9"
                    elif cur_group == "1010":
                        output1 = output1 + "A"
                    elif cur_group == "1011":
                        output1 = output1 + "B"
                    elif cur_group == "1100":
                        output1 = output1 + "C"
                    elif cur_group == "1101":
                        output1 = output1 + "D"
                    elif cur_group == "1110":
                        output1 = output1 + "E"
                    elif cur_group == "1111":
                        output1 = output1 + "F"

                    self.display.WriteText(output1)

                    count += 4
        def bindec(x):
            count = 0
            answer3 = 0
            while x > 0:
                length = len(str(x)) - 1
                num1 = 10**length
                x -= num1
                answer3 += 2**length
                count += 1
            answer3 = str(answer3)
            self.display.WriteText(answer3)
        if "+" in arr:
            a = arr.split("+")
            addition(float(a[0]), float(a[-1]))
        if "-" in arr:
            a = arr.split("-")
            subtraction(float(a[0]), float(a[-1]))
        if "X" in arr:
            a = arr.split("X")
            multiplication(float(a[0]), float(a[-1]))
        if "/" in arr:
            a = arr.split("/")
            division(float(a[0]), float(a[-1]))
        if "**" in arr:
            a = arr.split("**")
            exponents(float(a[0]), float(a[-1]))
        if "%" in arr:
            a = arr.split("%")
            modulo(float(a[0]), float(a[-1]))
        if "boct" in arr:
            a = arr.split("boct")
            bin_octal(float(a[0]))
        if "bhex" in arr:
            a = arr.split("bhex")
            binhexd(float(a[0]))
        if "bdec" in arr:
            a = arr.split("bdec")
            bindec(float(a[0]))

    def InitUI(self):

        menubar = wx.MenuBar(wx.EXPAND)
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.EXPAND)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(7, 4, 5, 5)

        self.res = wx.Button(self, label='Cls')
        self.back = wx.Button(self, label='Bck')
        self.close = wx.Button(self, label='Close')
        self.seven = wx.Button(self, label='7')
        self.eight = wx.Button(self, label='8')
        self.nine = wx.Button(self, label='9')
        self.divide = wx.Button(self, label='/')
        self.four = wx.Button(self, label='4')
        self.five = wx.Button(self, label='5')
        self.six = wx.Button(self, label='6')
        self.multiply = wx.Button(self, label='*')
        self.one = wx.Button(self, label='1')
        self.two = wx.Button(self, label='2')
        self.three = wx.Button(self, label='3')
        self.sub = wx.Button(self, label='-')
        self.zero = wx.Button(self, label='0')
        self.dec = wx.Button(self, label='.')
        self.equal = wx.Button(self, label='=')
        self.add = wx.Button(self, label='+')
        self.bindeci = wx.Button(self, label='BD')
        self.modu = wx.Button(self, label='%')
        self.powered = wx.Button(self, label='**')
        self.binhexi = wx.Button(self, label='BH')
        self.binoct = wx.Button(self, label='BO')
        self.minimax = wx.Button(self, label='MinMax')

        self.Bind(wx.EVT_BUTTON, self.onButton_Dec, self.dec)
        self.Bind(wx.EVT_BUTTON, self.onButton_0, self.zero)
        self.Bind(wx.EVT_BUTTON, self.onButton_1, self.one)
        self.Bind(wx.EVT_BUTTON, self.onButton_2, self.two)
        self.Bind(wx.EVT_BUTTON, self.onButton_3, self.three)
        self.Bind(wx.EVT_BUTTON, self.onButton_4, self.four)
        self.Bind(wx.EVT_BUTTON, self.onButton_5, self.five)
        self.Bind(wx.EVT_BUTTON, self.onButton_6, self.six)
        self.Bind(wx.EVT_BUTTON, self.onButton_7, self.seven)
        self.Bind(wx.EVT_BUTTON, self.onButton_8, self.eight)
        self.Bind(wx.EVT_BUTTON, self.onButton_9, self.nine)
        self.Bind(wx.EVT_BUTTON, self.onButton_Addition, self.add)
        self.Bind(wx.EVT_BUTTON, self.onButton_Subtraction, self.sub)
        self.Bind(wx.EVT_BUTTON, self.onButton_Multiplication, self.multiply)
        self.Bind(wx.EVT_BUTTON, self.onButton_Division, self.divide)
        self.Bind(wx.EVT_BUTTON, self.onButton_Modulo, self.modu)
        self.Bind(wx.EVT_BUTTON, self.onButton_Exponent, self.powered)
        self.Bind(wx.EVT_BUTTON, self.onButton_Division, self.divide)
        self.Bind(wx.EVT_BUTTON, self.onButton_Equal, self.equal)
        self.Bind(wx.EVT_BUTTON, self.onButton_Res, self.res)
        self.Bind(wx.EVT_BUTTON, self.onButton_Binoct, self.binoct)
        self.Bind(wx.EVT_BUTTON, self.onButton_Binhex, self.binhexi)
        self.Bind(wx.EVT_BUTTON, self.onButton_Bindec, self.bindeci)
        self.Bind(wx.EVT_BUTTON, self.onButton_Back, self.back)
        self.Bind(wx.EVT_BUTTON, self.onButton_Close, self.close)

        gs.AddMany([(self.res, 0, wx.EXPAND),
        (wx.StaticText(self), wx.EXPAND),
        (self.close, 0, wx.EXPAND),
        (self.back, 0, wx.EXPAND),
        (self.seven, 0, wx.EXPAND),
        (self.eight, 0, wx.EXPAND),
        (self.nine, 0, wx.EXPAND),
        (self.divide, 0, wx.EXPAND),
        (self.four, 0, wx.EXPAND),
        (self.five, 0, wx.EXPAND),
        (self.six, 0, wx.EXPAND),
        (self.multiply, 0, wx.EXPAND),
        (self.one, 0, wx.EXPAND),
        (self.two, 0, wx.EXPAND),
        (self.three, 0, wx.EXPAND),
        (self.sub, 0, wx.EXPAND),
        (self.zero, 0, wx.EXPAND),
        (self.dec, 0, wx.EXPAND),
        (self.equal, 0, wx.EXPAND),
        (self.add, 0, wx.EXPAND),
        (self.bindeci, 0, wx.EXPAND),
        (self.modu, 0, wx.EXPAND),
        (self.powered, 0, wx.EXPAND),
        (self.binhexi, 0, wx.EXPAND),
        (wx.StaticText(self), wx.EXPAND),
        (self.binoct, 0, wx.EXPAND),
        (self.minimax, 0, wx.EXPAND)])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


    def onButton_Dec(self, event):
        self.display.WriteText(".")
        self.arr += "."
        self.length += 1

    def onButton_0(self, event):
        self.display.WriteText("0")
        self.arr += "0"
        self.length += 1

    def onButton_1(self, event):
        self.display.WriteText("1")
        self.arr += "1"
        self.length += 1

    def onButton_2(self, event):
        self.display.WriteText("2")
        self.arr += "2"
        self.length += 1

    def onButton_3(self, event):
        self.display.WriteText("3")
        self.arr += "3"
        self.length += 1

    def onButton_4(self, event):
        self.display.WriteText("4")
        self.arr += "4"
        self.length += 1

    def onButton_5(self, event):
        self.display.WriteText("5")
        self.arr += "5"
        self.length += 1

    def onButton_6(self, event):
        self.display.WriteText("6")
        self.arr += "6"
        self.length += 1

    def onButton_7(self, event):
        self.display.WriteText("7")
        self.arr += "7"
        self.length += 1

    def onButton_8(self, event):
        self.display.WriteText("8")
        self.arr += "8"
        self.length += 1

    def onButton_9(self, event):
        self.display.WriteText("9")
        self.arr += "9"
        self.length += 1

    def onButton_Addition(self, event):
        self.display.WriteText(' + ')
        self.arr += "+"
        self.length += 1

    def onButton_Subtraction(self, event):
        self.display.WriteText(" - ")
        self.arr += "-"
        self.length += 1

    def onButton_Multiplication(self, event):
        self.display.WriteText(" X ")
        self.arr += "X"
        self.length += 1

    def onButton_Division(self, event):
        self.display.WriteText(" / ")
        self.arr += "/"
        self.length += 1

    def onButton_Exponent(self, event):
        self.display.WriteText(" ** ")
        self.arr += "**"
        self.length += 1

    def onButton_Modulo(self, event):
        self.display.WriteText(" % ")
        self.arr += "%"
        self.length += 1

    def onButton_Bindec(self, event):
        self.display.WriteText(" --> ")
        self.arr += "bdec"
        self.length += 1

    def onButton_Binhex(self, event):
        self.display.WriteText(" --> ")
        self.arr += "bhex"
        self.length += 1

    def onButton_Binoct(self, event):
        self.display.WriteText(" --> ")
        self.arr += "boct"
        self.length += 1

    def onButton_minmax(self, event):
        self.display.WriteText(" --> ")

    def onButton_Equal(self, event):
        self.display.WriteText(' = ')
        self.operations(self.arr)

    def onButton_Res(self, event):
        self.display.Clear()
        self.arr = ""

    def list_to_string (self, lst):
        count = 0
        string = ""
        while count < len(lst) - 1:
            string += lst[count]
            count += 1
        return string

    def onButton_Back(self,event):
        self.arr = (self.list_to_string(self.arr))
        self.display.Clear()
        self.display.WriteText(self.arr)

    def onButton_Close(self, event):
        quit()




def main():

    app = wx.App()
    ex = Example(None, title='Calculator')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
