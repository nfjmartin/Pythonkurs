import string
    
## Alla variabler
alfabet = string.ascii_lowercase
siffror = string.digits
ormbunke = "".join(reversed(alfabet)) 
omvant_siffror = "".join(reversed(siffror))



note = "Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv."       #texten som oversätts, vill du lägga till egen skriv decrypt("din text här")

def decrypt(note):
    resultat = ""
    for bokstav in note:
        if bokstav in alfabet:                      # Kollar det är en bokstav
            position = alfabet.index(bokstav)       # Kollar positionen på tecknet
            bokstav = ormbunke[position]            # Jämför positionen i koden
            resultat += bokstav                          # Lägger till rätt bokstav i ord
        
    
        elif bokstav in siffror:    
            position = siffror.index(bokstav)
            bokstav = omvant_siffror[position]
            resultat += bokstav


        else:                                       # Lägger till tecken som inte är bokstav
            resultat += bokstav
    return resultat

    
print(decrypt("abc123"))           
print(decrypt(note))





def test_decrypt():  
    assert decrypt('abba') == 'zyyz'
    

def test_decrypt_stora_bokstaver():
    assert decrypt('AbC') == 'AyC'

def test_special_tecken():
    assert decrypt('!"#¤%') == '!"#¤%'
    assert decrypt('Aoo blfi yzhv ziv yvolmt gl fh!') == 'All your base are belong to us!'

def test_siffror():
    assert decrypt('012') == '987'
    assert decrypt('Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!') == 'Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!'












