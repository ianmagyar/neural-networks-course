# Optimalizácia neurónovej siete v Kerase

Cieľom štvrtého zadanie je oboznámiť sa s možnosťami a parametrami neurónových sietí v knižnici Keras. Zadanie sa vypracujú v skupinách 2 alebo 3 študentov. Súčasťou riešenia je Python skript s implementáciou rôznych neurónových sietí v Pythone a report s výsledkami trénovania týchto neurónových sietí.

## Štrukúra riešenia
Pri riešení zadania postupujte nasledovne:

1. **výber datasetu** – nájdite alebo vytvorte dataset, ktorý je dostatočne zložitý na to, aby ste v presnosti rôznych neurónových sietí našli rozdiely.
2. **testovanie neurónových sietí s rôznymi topológiami** – natrénujte minimálne 5 neurónových sietí s rôznymi topológiami (ostatné parametre ponechajte rovnaké) na datasete z bodu 1 a vyhodnoťte presnosť týchto sietí. Následne vyberte topológiu siete s najvyššou presnosťou.
3. **testovanie neurónových sietí s rôznymi optimizátormi** – pre topológiu s najvyššou presnosťou vyskúšajte rôzne optimizátory z knižnice Keras (minimálne 3).
4. **testovanie neurónových sietí s rôznymi učiacimi parametermi** – pre topológiu a optimizátor s najvyššou presnosťou vyskúšajte rôzne učiace parametre (learning rate; minimálne 5).
5. **testovanie neurónových sietí s rôznymi aktivačnými funkciami** – pre topológiu, optimizátor a učiaci parameter s najvyššou presnosťou vyskúšajte rôzne aktivačné funkcie (minimálne 3).
6. Výsledky experimentov spíšte do reportu (presnosť alebo celé konfúzne matice).

## Deadline a odovzdávka
Vaše riešenia odovzdajte do 20. 12. 2019 cez mail na jan.magyar@tuke.sk, následne zadanie musíte obhájiť aj osobne (budú na to vyhradené cvičenia v 12. a 13. týždni). Odovzdávate ZIP súbor, ktorý musí obsahovať všetky Python skripty. Riešenie musí byť out-of-the-box, t.j. spustiteľné bez konfigurácie a zmien kódu.

## Hodnotenie
Za zadanie môžete získať maximálne 10 bodov, po 2 body za úlohy 1 až 5. **Pozor: pre získanie bodov musíte odovzdať aj report!**
