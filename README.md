# Neurónové siete

**Neurónové siete** je kurz ponúknutý v druhom ročníku bakalárskeho štúdia pre študijný program Inteligentné systémy. Kurz nadväzuje na kurzy [Základy inteligencie systémov](http://www.cloudai.sk/courses-zis/) a [Umelá inteligencia](http://www.cloudai.sk/umela-inteligencia/). Venuje sa umelým neurónovým sieťam, ich typom a využitiu.

Informačný list predmetu je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Odkazy na pomocné materiály](#links)
3. [Hodnotenie](#grading)
4. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

**Vzhľadom na pretrvávajúce opatrenia v súvislosti s pandémiou COVID-19 všetky prednášky a cvičenia sú online až do odvolania.**

Prednáška z predmetu je v utorok o 13:30 v miestnosti S07 (bývalá PC5) v budove PK6. Cvičenia sú v pondelok o 7:30 v miestnosti 102 v budove V4 a o 10:50 v miestnosti 147 v budove V4. Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester.

| Týždeň                       | Prednáška | Cvičenie                                                           | Zadania                  |
|------------------------------|-----------|--------------------------------------------------------------------|--------------------------|
| Týždeň 1<br>15. 2. - 21. 2.  | Úvod do neurónových sietí  | [matematické základy neurónových sietí](labs/lab01-basic-maths.pdf)         | [zverejnenie zadania 1](assignments/assignment1.md)    |
| Týždeň 2<br>22. 2. - 28. 2.   | Biologické aspekty modelovania NS, výpočtová a virtuálna inteligencia, NS ako prostriedok UI, základné prvky topológie NS, stratégie učenia NS | [perceptrón](labs/lab02-Perceptron.ipynb) |                          |
| Týždeň 3<br>1. 3. - 7. 3.    | Globálna stabilita NS, konvergencia NS, typy riešených úloh pomocou NS, kontrolované učenie na FF NS, perceptrón, konvergenčná teoréma, XOR problém, terminologický problém perceptrónu | [multilayer perceptron](labs/lab03-multilayer-perceptron.ipynb) |                          |
| Týždeň 4<br>8. 3. - 14. 3.   | Wienerove filtre, metóda najstrmšieho zostupu, metóda najmenšej kvadratickej chyby, Adaline, delta pravidlo | [odvodenie backpropagation algoritmu](https://brilliant.org/wiki/backpropagation/)<br>[príklad](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)        | [zverejnenie zadania 2](assignments/assignment2.md) |
| Týždeň 5<br>15. 3. - 21. 3.  | Metóda spätného šírenia chyby (backpropagation), BP cez čas, metódy urýchlenia konvergencie BP, funkcionálne linky, RBF siete, metóda kaskádnej korelácie BP | [predspracovanie údajov, metodológia trénovania NS, vyhodnotenie NS](labs/lab05-training-methodology.ipynb) | odovzdávka zadania 1     |
| Týždeň 6<br>22. 3. - 28. 3.  | Dôležité poznámky k návrhu NS | [NS v Tensorflow a Keras](labs/lab06-tensorflow-and-keras.ipynb)                |                          |
| Týždeň 7<br>29. 3. - 4. 4.   | Nekontrolované učenie na FF NS, konkurenčné učenie, MAXNET, Kohonenove siete, Ojove adaptačné pravidlo | prezentácia článkov                                                | zverejnenie zadania 3    |
| Týždeň 8<br>5. 4. - 11. 4.   | Veľká Noc | Veľká Noc                                                          |                          |
| Týždeň 9<br>12. 4. - 18. 4.  | Hybridné metódy učenia na FF NS, counterpropagation, time-delay vstupy na FF NS, rekurentné NS, Hopfieldova NS | nekontrolované učenie | odovzdávka zadania 2       |
| Týždeň 10<br>19. 4. - 25. 4. | Kontrolované učenie na RC NS, BP na RC NS, Jordanove a Elmanove siete | autoenkódery  | zverejnenie zadania 4 |
| Týždeň 11<br>26. 4. - 2. 5.  | Nekontrolované učenie na RC NS, ART NS | Hebbovo učenie |                          |
| Týždeň 12<br>3. 5. - 19. 5.  | Hybridné prístupy k učeniu, učenie na základe stavu systému | odovzdanie zadaní 3 a 4                                            | odovzdávka zadania 3 a 4 |
| Týždeň 13<br>10. 5. - 16. 5. | Modulárne NS, základné princípy multiagentových systémov | zápočtový týždeň                                                   |                          |

## Odkazy na pomocné materiály <a name="links"></a>
* [Návod na inštaláciu Pythonu](labs/lab00-getting-started.md)
* [Java Neural Network Simulator](http://www.ra.cs.uni-tuebingen.de/software/JavaNNS/welcome_e.html?fbclid=IwAR3abC_9BxqT_dxwxxD5Qq8uzBY9sIUcnm2_d36JHIrx1k2i4Y1DBm-bVEA)
* [Online Perceptron Training](https://www.cs.utexas.edu/~teammco/misc/perceptron/?fbclid=IwAR1qWNnD9VUoORzx5y0H7_lqo028lquC_B00CCsQelNAInh6GSelRM6YYTQ)
* [Principles of training multi-layer neural network using backpropagation](http://home.agh.edu.pl/~vlsi/AI/backp_t_en/backprop.html)
* [The Back Propagation Algorithm](lectures/The_Back_Propagation_Algorithm.pdf)

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov aj zo zápočtu aj zo skúšky.

Počas semestra odovzdá každý študent štyri zadania:

1. [prehľadový článok o možnostiach využitia neurónových sietí](assignments/assignment1.md) (15 b),
2. [implementácia algoritmu backpropagation](assignments/assignment2.md) (10 b)
3. trénovanie neurónovej siete pre klasifikáciu pomocou knižnice Keras (5 b),
4. implementácia nekontrolovaného učenia pomocou Kohonenovej siete (10 b).

Podmienkou pre získanie zápočtu je dokončenie online kurzu UI do 12. 3. 2021 a následné poskytnutie feedbacku o kvalite kurzu. Bližšie informácie budú zverejnené v prvom týždni semestra.

Priebežné hodnotenie nájdete [v tomto dokumente](https://docs.google.com/spreadsheets/d/136G83LJc4GKVlvZxxBLwh4AEXameV242nDkN86aO_nI/edit?usp=sharing).

Otázky na skúšku nájdete [tu](exam/skuska_otazky.pdf). Podrobnejšie informácie k realizácii skúšky [sú dostupné tu](exam/exam_info.md).

## Odporúčaná literatúra <a name="textbooks"></a>

* SINČÁK, ANDREJKOVÁ: Neuronové siete I., Inžiniersky prístup, Elfa, Košice, 1996 - [1. diel](lectures/Neuronove_siete_1.pdf), [2. diel](lectures/Neuronove_siete_2.pdf)
* KRÖSE, van der SMAGT: [An Introduction to Neural Networks](lectures/An_Introduction_to_Neural_Networks.pdf)
* [Stuttgart Neural Network Simulator v4.2 User Manual](lectures/SNNS_v4.2._Manual.pdf)
* HAYKIN: Neural Networks: A Comprehensive Foundation, MacMillan, 1994
* ďalšie zdroje budú dodané na prednáškach