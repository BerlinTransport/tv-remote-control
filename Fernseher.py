#Paul Teumer
#08.01.2019
#Fernsehbedinung

class Fernseher:
    def __init__(self):
        self.__programme = ["ARD","ZDF","RBB","SAT1","RTL","PRO7","KABEL1","ARTE","NDR"]
        self.__programm = 0
        self.__vol = 25
        self.__an = True
    def anaus(self):
        if self.__an == True:
            self.__an = False
            return "OFF"
        else:
            self.__an = True
            return "ON"
    def ProgrammPlus(self):
        if self.__programm < len(self.__programme)-1 and self.__an==True:
            self.__programm = self.__programm+1
            return self.__programm
        elif self.__an==True:
            self.__programm = 0
            return self.__programm
        else:
            return "OFF"
    def ProgrammMinus(self):
        if self.__programm != 0 and self.__an==True:
            self.__programm = self.__programm - 1
            return self.__programm
        elif self.__an==True:
            self.__programm = len(self.__programme) - 1
            return self.__programm
        else:
            return "OFF"
    def VolPlus(self):
        if self.__vol != 100 and self.__an==True:
            self.__vol = self.__vol + 5
            return self.__vol
        elif self.__an==True and self.__vol==100:
            return self.__vol
        elif self.__an!=True:
            return "OFF"
    def VolMinus(self):
        if self.__vol != 0 and self.__an==True:
            self.__vol = self.__vol - 5
            return self.__vol
        elif self.__an==True and self.__vol==0:
            return self.__vol
        elif self.__an!=True:
            return "OFF"
