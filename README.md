# IPK - Počítačové komunikácie a siete

## Projekt č.1 : Varianta 2: Klient pre OpenWeatherMap Api

#### Autor: 
- René Bolf <xbolfr00@stud.fit.vutbr.cz>


## Popis riešeného problému
Úlohou bolo vytvoriť program klient rozhrania OpenWeatherMap, ktorý bude schopný prostredníctvom http dotazov získavať informácie z dátového zdroja.

## Návrh riešenia
#### Knižnice
V projekte sú použité 3 knižnice a to **import socket**, **import sys**, **import json**.
Knižnica socket slúži pre vytvorenie socketu a následne pre komunikáciu. Knižnica sys slúži pre prácu s argumentami a knižnica json slúži pre prácu s jsonom.
#### Implementácia
Hostname je zadaný v tvare "api.openweathermap.org", pretože na stránke <https://openweathermap.org/appid> píšu, že sa nemá použiť IP adresa servera. Port je nastavený na 80, pretože sa jedná o http protokol. Následne som si vytvoril premennú, do ktorého som uložil url odkaz <http://api.openweathermap.org/data/2.5/weather?q=> , lokáciu (location), api_key a **&units=metric** aby všetky jednotky boli metrické.
Dôležitou časťou je vytvorenie požiadavky (Get request). Táto požiadavka je uložená v premennej request_command. Požiadavka obsahuje kľúčové slovo GETm ktorý žiada o zdroj uvedením jeho URL, verzia http je nastavená na http/1.1 a kľúčové slovo Host.
Požiadavka musí byť v správnom tvare, ak nie odošle sa bad request.
```python
request_command = "GET " + url_string + " HTTP/1.1\n" + "Host: " + hostname + "\n\n"
```
#### Vytvorenie socketu
Socket je vytvorený príkazom 
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
```
- **socket.AF_INET** - znamená, že sa jedná o verziu IPV4
- **socket.SOCK_STREAM** - znamená, že je to protokol TCP (Transmission Control Protocol) - dáta budu doručené bez straty

```python
Následne som sa pripojil na server pomocou príkazu 
s.connect((hostname,port)) 
a príkazom s.send(request_command.encode("utf-8")) som poslal požiadavku na server
```
Príkazom data = s.recv(4096) získame prijímané dáta zo socketu. Číslo 4096 udáva veľkosť buffera, pre najlepšiu zhodu s hardwerom a so sieťou by mala byť relatívne malá mocnina 2 napríklad 4096. Následne sa príkazom s.close() uzavrie spojenie. A následne sa získane dáta orežu a spracujú pomocou knižnice json.




## Inštalácia a preklad aplikácie
Je potrebná registrácia na <https://openweathermap.org/>. Po registrácií je potrebné získať autentizačný kľúč API_KEY, ktorý sa používa pri dotazoch pre autentizáciu a pri spúšťaní.
program sa spúšťa pomocou súboru Makefile a to nasledujúcim príkazom:
```MakeFile
make run api_key=<API kľúč> city=<Mesto>
```
Ak chcemme vložiť dvoj slovné mesto, je potreba ho zadať do úvodzoviek napriklad "New York".
## Rozšírenie
Okrem nasledujúcich informáciach o aktualnom počasí: popis počasia, teplota, vlhosť ,tlak, rýchlosť a smer vetru sa vypíšu údaje aj o maximalnej a minimalnej teplote.