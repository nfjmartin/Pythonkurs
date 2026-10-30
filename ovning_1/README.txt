Dag: 14 augusti, 21:35.
Våra servrar har kapats av okänd identitet. De har dock lämnat en note, efter kort sökarbete insåg jag de hade satt atbash dekryptering. Jag byggde ett enkelt skript för att enkelt kunna dekryptera meddelandet och det lyder:

"Era servrar är låsta och backuperna är raderade. Skicka 75 bitcoin före måndag kl 09:00, annars säljer vi kunduppgifterna på nätet!"

Filosofin bakom skriptet: Bygg så det funkar, optimera sedan, addera vid behov. 
Började med tanken att jag kör bara if satser på varje bokstav. Men insåg snabbt att bara plocka ut alfabetet a-z samt siffror 0-9 via import string Köra omvändning på dem så kan jag kan jämföra alfabetet och ormbunke för att få ut resultatet. 
Så efter att räkna ut hur man byter plats på bokstäverna och siffrorna samt lämna stora bokstäver och specialtecken så kunde jag få ut koden. Men det räckte inte för mig, jobbar under press, behöver ett enkelt script som jag sen även kan visa för cheferna för att kunna advancera på företaget. 
Jag tar denna uppgift och gör migsjälv oumbärlig på företaget. 
Deras förlust kan visa sig vara min lilla guldgruva! Så då påbörjades optimeringen. Från samtal med min mellanchef Johan Andersson där han utmanade mig att optimera koden, så tog jag lite amfetamin i form av ADHD medicin och satte igång och resultatet är en for loop som går igenom alla bokstäver, if, elif och else som fångar upp bokstäver, siffror och allt annat. Varje villkor kunde optimeras till en enda rad.

Onödig men jävligt stilren addering:
För att köra skriptet kör du uv(eller python) run solution.py i kommandotolken, då får du en fråga om du vill avkoda Note, 
som är den hemliga koden. Eller om du vill avkoda något annat meddelande. Följ instruktionerna.
