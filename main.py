from datetime import datetime

#otwieranie pliku
file = open("a.txt",encoding="utf8")
fileContent = file.read()
file.close()
#ustalenie daty początkowej zliczania pozytywnych wykonań. Jeżeli data początkowa = data końcowa, to zlicza pozytywne z tego dnia
thStart = "tabela_dane_tytul"
tableHeader = fileContent[fileContent.find(thStart,0):fileContent.find("paginacja_box")]
dateFrom = ""
for i in range(3):
    tableHeader = tableHeader[tableHeader.find("<b>")+3:]
    if i == 2:
        dateFrom = tableHeader[0:10]       
    
#obcinanie wstępne
fileContent = fileContent.strip()
fileContent = fileContent[fileContent.find("class=list",0)+10:fileContent.find("</tbody>",fileContent.find("class=list",0)+11)]


dictWykony = {}
listaWstepna = fileContent.split('<tr class="row100 body">')
listaPrzetworzona = []
counter = 0

#tworzę plik z wynikiem
resultFile = open("result.txt","w")

for i in listaWstepna:
    if counter == 0:
        pass
    else:
    # dla każdego rekordu zbieram takie dane jak zestaw, ostatni pozytywny strzal, sciezka, nazwa tc
        helper = i.find("Notatka z ")
        technologia = i[helper+10:i.find("\n",helper)].replace(":","").strip()
        helper = '<td class="tc_path" style="width: 300px;">'
        helper = i.find(helper)+len(helper)
        sciezka = i[helper:i.find("</td>",helper)]
        tc = sciezka[sciezka.rfind("/")+1:].replace("&gt;",">").replace("&lt;","<").replace('&quot;','"').replace('  ',' ')
        zestaw = sciezka[:sciezka.rfind("/")].replace("&gt;",">").replace("&lt;","<").replace('&quot;','"').replace('  ',' ')
        helper = '<td class="ostatni_pozytywny" style="width: 190px;">'
        dataPozytyw = i[i.find(helper)+len(helper):i.find(helper)+len(helper)+10]
        helper = '<td class="data_wykonu" style="width: 190px;">'
        dataWykonu = i[i.find(helper)+len(helper):i.find(helper)+len(helper)+10]
        pozytyw = 0
        try:
            objDataIn = datetime.strptime(dateFrom,'%Y-%m-%d')
            objDataTc = datetime.strptime(dataPozytyw,'%Y-%m-%d')
            #porównuję, czy ostatni pozytywny strzał mieści się w zakresie regresji, jeśli tak dostanie 1, jeśli nie 0
            if objDataTc >= objDataIn:
                pozytyw = 1
        except:
            pass
            #brak wyniku pozytywnego w przeszłości
        

        #zapisuję do pliku dane każdego tc w formacie TECHNOLOGIA;ZESTAW;TC;CZY_POZYTYWNY
        resultFile.write(technologia+";"+zestaw+";"+tc+";"+str(pozytyw)+"\n")

        #tworzę słownik String-Słownik wyników zbiorczych (Zestaw: Pozytywne:x, negatywne:y)
        if zestaw in dictWykony:
            if pozytyw == 0:
                pass
            else:
                pass
        else:
            if pozytyw == 0:
                dictWykony[zestaw] = {"ok":0,"nok":1}
            else:
                dictWykony[zestaw] = {"ok":1,"nok":0}




    counter += 1
    

resultFile.close()
