class logdataread():
    def GetLogKeyWordData(self,filename, keyword):
        file = open(filename, 'r', encoding='utf-8')
        locatdate = []
        for i in file:
            if keyword in str(i):
                locatdate.append(i)
        return locatdate

    def GetSecordinterval(self,filename, keyword):
        file = open(filename, 'r', encoding='utf-8')
        locatdate = []
        for i in file:
            if keyword in str(i):
                line = str(i).split(" ")[0]
                line = line.split(":")
                sce = float(line[0]) * 60 * 60 + float(line[1]) * 60 + float(line[2])
                locatdate.append(round(sce, 3))
        print(locatdate)
        maxsec = 0
        for j in range(len(locatdate) - 1):
            d1 = locatdate[j + 1]
            d2 = locatdate[j]
            if d1 - d2 > maxsec:
                maxsec = d1 - d2
        maxsec = round(maxsec, 3)
        return maxsec