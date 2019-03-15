# IPK - Počítačové komunikácie a siete

## Projekt č.1 : Varianta 2: Klient pre OpenWeatherMap Api

#### Autor: 
- René Bolf <xbolfr00@stud.fit.vutbr.cz>


## Popis riešeného problému
Úlohou bolo vytvoriť program klient rozhrania OpenWeatherMap, ktorý bude schopný prostredníctvom http dotazov získavať informácie z dátového zdroja.

## Návrh riešenia
#### Knižnice
V projekte sú použité 3 knižnice a to **import socket**, **import sys**, **import json**.
Knižnica socket slúži pre vytvorenie socketu a následne pre komunikáciu. Knižnica sys slúži pre prácu s argumentami a knižnica json slúži pre prácu s JSONom.
#### Implementácia
Hostname je zadaný v tvare "api.openweathermap.org", pretože na stránke <https://openweathermap.org/appid> píšu, že sa nemá použiť IP adresa servera. Port je nastavený na 80, pretože sa jedná o http protokol. Následne do premennej url_string je uložený url odkaz. Táto premenna okrem url odkazu <http://api.openweathermap.org/data/2.5/weather?q=> ,obsahuje aj lokáciu (location), api_key a **&units=metric** aby všetky jednotky boli nastavené ako metrické.
Dôležitou časťou je vytvorenie požiadavky (Get request). Táto požiadavka je uložená v premennej request_command. Požiadavka obsahuje kľúčové slovo GET ktorý žiada o zdroj uvedením jeho URL, verziu http, verzia je nastavená na http/1.1 a kľúčové slovo Host.
Požiadavka musí byť v správnom tvare, ak nie je odošle sa bad request.
```python
request_command = "GET " + url_string + " HTTP/1.1\n" + "Host: " + hostname + "\n\n"
```
#### Vytvorenie socketu
```python
Socket je vytvorený príkazom 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
```
- **socket.AF_INET** - znamená, že sa jedná o verziu IPV4
- **socket.SOCK_STREAM** - znamená, že je to protokol TCP (Transmission Control Protocol) - dáta budu doručené bez straty

```python
Následne pomocou príkazu s.connect((hostname,port)) sa pripojí na server
a príkazom s.send(request_command.encode("utf-8")) sa pošle požiadavka na server
```
Príkazom data = **s.recv(4096)** sa získajú prijímané dáta zo socketu. Číslo **4096** udáva veľkosť buffera, pre najlepšiu zhodu s hardwerom a so sieťou by mala byť nastavená na relatívnu malú mocninu dvojky napríklad 4096. Následne sa príkazom **s.close()** uzavrie spojenie. A následne sa získane dáta orežu a spracujú pomocou knižnice JSON.

## Inštalácia a preklad aplikácie
#### Registrácia a získanie autentizačného kľúču
Je potrebná registrácia na <https://openweathermap.org/>. Po registrácií je potrebné získať autentizačný kľúč API_KEY, ktorý sa používa pri dotazoch pre autentizáciu a pri spúšťaní.
#### Spúšťanie programu
program sa spúšťa pomocou súboru Makefile a to nasledujúcim príkazom:
```MakeFile
make run api_key=<API kľúč> city=<Mesto>
```
Ak chcemme vložiť dvoj slovné mesto, je potreba ho zadať do úvodzoviek napriklad "New York".
## Rozšírenie
Okrem nasledujúcich informáciach o aktualnom počasí: popis počasia, teplota, vlhosť ,tlak, rýchlosť a smer vetru sa vypíšu údaje aj o maximalnej a minimalnej teplote.

## Zdroje
- <https://docs.python.org/2/library/socket.html>
- <https://docs.python.org/2/howto/sockets.html>
- <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>
