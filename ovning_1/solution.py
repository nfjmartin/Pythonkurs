import string


alfabet = string.ascii_lowercase
ormbunke = "".join(reversed(alfabet))
siffror = string.digits
omvanda_siffror = "".join(reversed(siffror))

note = "Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!"

def solution(note):

    """Här är nyckeln till att dekryptera atbash krypteringen. 
    Atbash i denna form byter plats på små bokstäver så första bokstaven blir sista, näst första blir
    näst sista och så vidare.
    Den kollar position på varje tecken i en for loop och
    byter ut den mot respektive tecken som krävs för att dekryptera note. 
    Casually optimerat till en enda rad per villkor."""

    resultat = ""
    for bokstav in note:
        if bokstav in alfabet: resultat += ormbunke[alfabet.find(bokstav)]           # Omvandlar bokstäverna
   
        elif bokstav in siffror: resultat += omvanda_siffror[siffror.find(bokstav)]  # Omvandlar siffrorna
            
        else: resultat += bokstav                                                    # Lämnar specialtecken
    return resultat

print(solution(note))
    

def test_solution():  
    """Första test: se att dekryptnyckeln funkar mot bokstäver"""
    assert solution('abba') == 'zyyz'
    
def test_stora_bokstaver():
    """Andra test: behålls stora bokstäver?"""
    assert solution('AbC') == 'AyC'

def test_special_tecken():
    """tredje test: Funkar det att specialtecken lämnas inklusive mellanslag."""
    assert solution('!"#¤%') == '!"#¤%'
    

def test_siffror():
    """Fjärde test: Se att dekrypteringsnyckeln även funkar på siffror."""
    assert solution('012') == '987'
    
def test_delar_av_note():
    """Femte test: Test mot del av Note."""
    assert solution('Aoo blfi yzhv ziv yvolmt gl fh!') == 'All your base are belong to us!'

def test_hela_note():
    """Sjätte test: Test mot hela Note."""
    assert solution('Eiz hvieizi äi oåhgz lxs yzxpfkvimz äi izwvizwv. Sprxpz 24 yrgxlrm uöiv nåmwzt po 90:99, zmmzih häoqvi er pfmwfkktrugvimz kå mägvg!') == 'Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!' 





