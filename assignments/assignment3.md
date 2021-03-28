# Optimalizácia neurónovej siete v Kerase

Cieľom tretieho zadania je oboznámiť vás s možnosťami a parametrami neurónových sietí v knižnici Keras. Zadanie sa vypracuje v skupinách 2 alebo 3 študentov. Súčasťou riešenia je Python skript s implementáciou rôznych neurónových sietí v Pythone a report s výsledkami trénovania týchto neurónových sietí.

## Štrukúra riešenia
Pri riešení zadania postupujte nasledovne:

1. **výber datasetu** – nájdite alebo vytvorte dataset, ktorý je dostatočne zložitý na to, aby ste v presnostiach rôznych neurónových sietí videli rozdiel (môžete hľadať [napríklad tu](https://archive.ics.uci.edu/ml/datasets.php) [alebo tu](https://www.kaggle.com/datasets)).
2. **testovanie neurónových sietí s rôznymi topológiami** – natrénujte *minimálne 5* neurónových sietí s rôznymi topológiami (ostatné parametre nemeňte) na datasete z bodu 1 a vyhodnoťte presnosť týchto sietí. Následne vyberte topológiu siete s najvyššou presnosťou.
3. **testovanie neurónových sietí s rôznymi optimalizátormi** – pre topológiu s najvyššou presnosťou vyskúšajte rôzne optimalizátory z knižnice Keras (*minimálne 3*).
4. **testovanie neurónových sietí s rôznymi učiacimi parametermi** – pre topológiu a optimalizátor s najvyššou presnosťou vyskúšajte rôzne učiace parametre (learning rate; *minimálne 5*).
5. **testovanie neurónových sietí s rôznymi aktivačnými funkciami** – pre topológiu, optimalizátor a učiaci parameter s najvyššou presnosťou vyskúšajte rôzne aktivačné funkcie (*minimálne 3*).
6. Výsledky experimentov spíšte do reportu – jedna strana A4, pre všetky nastavenia uveďte hodnoty parametrov a presnosť, pre najlepšiu topológiu a parametre aj konfúznu maticu.

## Deadline a odovzdávka
Vaše riešenia odovzdajte najneskôr do 9. 5. 2021 cez MS Teams. Riešenie následne musíte obhájiť online (budú na to vyhradené cvičenia v 12. a 13. týždni). Odovzdávate ZIP súbor, ktorý musí obsahovať všetky Python skripty. Riešenie musí byť out-of-the-box, t.j. spustiteľné bez konfigurácie a zmien kódu.

## Hodnotenie
Za zadanie môžete získať maximálne 5 bodov, po 1 bod za úlohy 1 až 5.

**Pozor: pre získanie bodov musíte odovzdať aj report!**
