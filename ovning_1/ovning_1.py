import string                                       #modul i pythons standardbibliotek som innehåller bl.a. a-z 0-9.
    
## Alla variabler
alfabet = string.ascii_lowercase                    #Lägger till a-z i alfabet
siffror = string.digits                             #Lägger till 0-9 i siffror
ormbunke = "".join(reversed(alfabet))               #reversar alfabetet
omvant_siffror = "".join(reversed(siffror))         #reversar siffror


#texten som oversätts, vill du lägga till egen skriv print(decrypt("din text här"))
note = "Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!"       

def decrypt(note):                                  #dekrypt-nyckeln
    """dekrypterar note med a-z mot z-a samt 9-0 till 0-9"""
    resultat = ""                                   #det sparade resultatet av översättningen sparas här
    for bokstav in note:
        if bokstav in alfabet:                      # Kollar det är en bokstav
            position = alfabet.index(bokstav)       # Kollar positionen på tecknet
            bokstav = ormbunke[position]            # Jämför positionen i koden
            resultat += bokstav                     # Lägger till rätt bokstav i ord
        
    
        elif bokstav in siffror:                    #Gör samma som if fast med siffror
            position = siffror.index(bokstav)
            bokstav = omvant_siffror[position]
            resultat += bokstav


        else:                                       # Lägger till tecken som inte är bokstav eller siffra
            resultat += bokstav
    return resultat

    
print(decrypt("abc123"))           
print(decrypt(note))





def test_decrypt():  
    """Första test: se att dekryptnyckeln funkar mot bokstäver"""
    assert decrypt('abba') == 'zyyz'
    
def test_decrypt_stora_bokstaver():
    """Andra test: behålls stora bokstäver?"""
    assert decrypt('AbC') == 'AyC'

def test_special_tecken():
    """tredje test: Funkar det att specialtecken lämnas inklusive mellanslag."""
    assert decrypt('!"#¤%') == '!"#¤%'
    

def test_siffror():
    """Fjärde test: Se att dekrypteringsnyckeln även funkar på siffror."""
    assert decrypt('012') == '987'
    
def test_decrypt_delar_av_note():
    """Femte test: Test mot del av Note."""
    assert decrypt('Aoo blfi yzhv ziv yvolmt gl fh!') == 'All your base are belong to us!'

def test_decrypt_hela_note():
    """Sjätte test: Test mot hela Note."""
    assert decrypt('Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!') == 'Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!'









