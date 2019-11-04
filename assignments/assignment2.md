# Implementácia algoritmu backpropagation

Cieľom druhého zadania je aplikovať teoretické poznatky o backpropagation v programovej implementácii tohto algoritmu. Vašou úlohou je implementovať algoritmus backpropagation a použiť ho pri trénovaní neurónovej siete. Pri riešení zadania používajte Python 3, funkčnosť Vášho riešenia preukážete trénovaním neurónovej siete pomocou Vami vytvoreného algoritmu backpropagation na ľubovoľnom datasete.

## Štrukúra riešenia
Vaše riešenie sa skladá z troch častí:

1. **implementácia algoritmu backpropagation** – hlavná časť zadania, definuje metódu trénovania neurónovej siete pomocou spätného šírenia chyby. Môže byť implicitnou súčasťou implementácie neurónovej siete z bodu 2. alebo môže byť samostatný modul.
2. **implementácia jednoduchej neurónovej siete** – trieda s možnosťou pridávania vrstiev (ako na cvičení); musí obsahovať základné prvky neurónových sietí:
    * vrstvy
    * aktivačné funkcie
    * predikcia
    * trénovanie (používajte algoritmus backprop z bodu 1.)
3. **ukážka použitia backpropu v trénovaní neurónovej siete** – hlavná funkcia `main`, v ktorej vytvoríte jednoduchú sieť, načítate dataset, a natrénujete neurónovú sieť na tomto datasete. Proces trénovania musíte znázorniť (graficky, alebo výpisom chyby na konzolu, atď.)

## Deadline a odovzdávka
Vaše riešenia odovzdajte do 17. 11. 2019 cez mail na jan.magyar@tuke.sk. Odovzdávate ZIP súbor, ktorý musí obsahovať použitý dataset a Python skript (ak máte viac skriptov, vytvorte súbor `main.py`, ktorý obsahuje hlavnú funkciu). Riešenie musí byť out-of-the-box, t.j. spustiteľné bez konfigurácie a zmien kódu.

## Hodnotenie
Za zadanie môžete získať maximálne 5 bodov, ktoré sa udeľujú nasledovne:

* implementácia algoritmu backpropagation – 2 body
* aplikácia backpropu v neurónovej sieti – 2 bod
* ukážka trénovania neurónovej siete pomocou backpropu – 1 bod

**Pozor: pre získanie bodov musíte mať implementované všetky tri časti aspoň čiastočne!**
