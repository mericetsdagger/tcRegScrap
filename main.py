#otwieranie pliku
file = open("a.txt")
fileContent = file.read()

#ustalenie daty początkowej zliczania pozytywnych wykonań. Jeżeli data początkowa = data końcowa, to zlicza pozytywne z tego dnia
thStart = "tabela_dane_tytul"
tableHeader = fileContent[fileContent.find(thStart,0):fileContent.find("paginacja_box")]
dateFrom = tableHeader[find

print(tableHeader)

#obcinanie wstępne
fileContent = fileContent.strip()
fileContent = fileContent[fileContent.find("class=list",0):fileContent.find("</tbody>",fileContent.find("class=list",0))]




dictWykony = {}
listaWstepna = fileContent.split('<td class="nazwa_PT"')
listaPrzetworzona = []
counter = 0
for i in listaWstepna:

    if "ostatni_pozytywny" in i:
            
                
        przypadek = i[i.find('style="width: 300px;">')+22:i.find('</td>')].replace("&gt;",">").replace("&lt;","<").replace('&quot;','"').replace('  ',' ')
        dataPozytyw = i[i.find('<td class="ostatni_pozytywny" style="width: 190px;">')+len('<td class="ostatni_pozytywny" style="width: 190px;">'):i.find('<td class="ostatni_pozytywny" style="width: 190px;">')+len('<td class="ostatni_pozytywny" style="width: 190px;">')+10]
        dictWykony[przypadek] = dataPozytyw

print(dictWykony)
