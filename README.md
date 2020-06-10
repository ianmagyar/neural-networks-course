# Neurónové siete

**Neurónové siete** je kurz ponúknutý v druhom ročníku bakalárskeho štúdia pre študijný program Inteligentné systémy. Kurz nadväzuje na kurzy [Základy inteligencie systémov](http://www.cloudai.sk/courses-zis/) a [Umelá inteligencia](http://www.cloudai.sk/umela-inteligencia/). Venuje sa umelým neurónovým sieťam, ich typov a využitiu.

Informačný list predmetu je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

Pridajte sa do [facebook skupiny predmetu](https://www.facebook.com/groups/2627782910654322/).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Odkazy na pomocné materiály](#links)
3. [Hodnotenie](#grading)
4. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

Prednáška z predmetu je v utorok o 13:30 v miestnosti S07 (bývalá PC5) v budove PK6. Cvičenia sú v pondelok o 7:30 v miestnosti 102 v budove V4 a o 10:50 v miestnosti 147 v budove V4. Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester.

| Týždeň                       | Prednáška | Cvičenie                                                           | Zadania                  |
|------------------------------|-----------|--------------------------------------------------------------------|--------------------------|
| Týždeň 1<br>17. 2. - 23. 2.  | [Úvod do neurónových sietí](lectures/Lecture01-Introduction-to-Neural-Networks.pdf)           | [matematické základy neurónových sietí](labs/lab01-maths.pdf)         | [zverejnenie zadania 1](assignments/assignment1.md)    |
| Týždeň 2<br>24. 2. - 1. 3.   | Biologické aspekty modelovania NS, výpočtová a virtuálna inteligencia, NS ako prostriedok UI, základné prvky topológie NS, stratégie učenia NS | [perceptrón](labs/lab02-perceptron.ipynb)                          |                          |
| Týždeň 3<br>2. 3. - 8. 3.    | Globálna stabilita NS, konvergencia NS, typy riešených úloh pomocou NS, kontrolované učenie na FF NS, perceptrón, konvergenčná teoréma, XOR problém, terminologický problém perceptrónu | [multilayer perceptron](labs/lab03-multilayer-perceptron.ipynb)    |                          |
| Týždeň 4<br>9. 3. - 15. 3.   | Wienerove filtre, metóda najstrmšieho zostupu, metóda najmenšej kvadratickej chyby, Adaline, delta pravidlo | [odvodenie backpropagation algoritmu](https://brilliant.org/wiki/backpropagation/)                                | [zverejnenie zadania 2](assignments/assignment2.md)    |
| Týždeň 5<br>16. 3. - 22. 3.  | Metóda spätného šírenia chyby (backpropagation), BP cez čas, metódy urýchlenia konvergencie BP, funkcionálne linky, RBF siete, metóda kaskádnej korelácie BP | [predspracovanie údajov, metodológia trénovania NS, vyhodnotenie NS](labs/lab05-training-methodology.ipynb) | odovzdávka zadania 1     |
| Týždeň 6<br>23. 3. - 29. 3.  | Dôležité poznámky k návrhu NS | [NS v Tensorflow a Keras](labs/lab06-tensorflow-and-keras.ipynb)                                            |                          |
| Týždeň 7<br>30. 3. - 5. 4.   | Nekontrolované učenie na FF NS, konkurenčné učenie, MAXNET, Kohonenove siete, Ojove adaptačné pravidlo | prezentácia článkov                                                | [zverejnenie zadania 3](assignments/assignment3.md)    |
| Týždeň 8<br>6. 4. - 12. 4.   | Hybridné metódy učenia na FF NS, counterpropagation, time-delay vstupy na FF NS, rekurentné NS, Hopfieldova NS | [nekontrolované učenie](labs/lab08-unsupervised-learning.ipynb) |                     |
| Týždeň 9<br>13. 4. - 19. 4.  | Veľká Noc | Veľká Noc                                                          | odovzdávka zadania 2       |
| Týždeň 10<br>20. 4. - 26. 4. | Kontrolované učenie na RC NS, BP na RC NS, Jordanove a Elmanove siete | [autoenkódery](labs/lab10-autoencoders.ipynb)                                                       | [zverejnenie zadania 4](assignments/assignment4.md)    |
| Týždeň 11<br>27. 4. - 3. 5.  | Nekontrolované učenie na RC NS, ART NS | [Hebbovo učenie](labs/lab11-hebbian-learning.ipynb)   |                          |
| Týždeň 12<br>4. 5. - 10. 5.  | Hybridné prístupy k učeniu, učenie na základe stavu systému | odovzdanie zadaní 3 a 4                                            | odovzdávka zadania 3 a 4 |
| Týždeň 13<br>11. 5. - 17. 5. | Modulárne NS, základné princípy multiagentových systémov | zápočtový týždeň                                                   |                          |

## Odkazy na pomocné materiály <a name="links"></a>
* [Návod na inštaláciu Pythona](labs/lab00-getting-started.md)
* [Java Neural Network Simulator](http://www.ra.cs.uni-tuebingen.de/software/JavaNNS/welcome_e.html?fbclid=IwAR3abC_9BxqT_dxwxxD5Qq8uzBY9sIUcnm2_d36JHIrx1k2i4Y1DBm-bVEA)
* [Online Perceptron Training](https://www.cs.utexas.edu/~teammco/misc/perceptron/?fbclid=IwAR1qWNnD9VUoORzx5y0H7_lqo028lquC_B00CCsQelNAInh6GSelRM6YYTQ)
* [Principles of training multi-layer neural network using backpropagation](http://home.agh.edu.pl/~vlsi/AI/backp_t_en/backprop.html)
* [The Back Propagation Algorithm](lectures/The_Back_Propagation_Algorithm.pdf)

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov aj zo zápočtu aj zo skúšky.

Počas semestra odovzdá každý študent štyri zadania:

1. [prehľadový článok o možnostiach využitia neurónových sietí](assignments/assignment1.md) (15 b),
2. [implementácia algoritmu backpropagation](assignments/assignment2.md) (10 b)
3. [trénovanie neurónovej siete pre klasifikáciu pomocou knižnice Keras](assignments/assignment3.md) (5 b),
4. [implementácia nekontrolovaného učenia pomocou Kohonenovej siete](assignments/assignment4.md) (10 b).

Priebežné hodnotenie nájdete [v tomto dokumente](https://docs.google.com/spreadsheets/d/1L86NKW3RjyRSYsCOR5Fwe9VssCVYbkIjRHbMLBWxlBg/edit?usp=sharing).

Otázky na skúšku nájdete [tu](exam/skuska_otazky.pdf). Podrobnejšie informácie k realizácii skúšky [sú dostupné tu](exam/exam_info.md).

Otázky z predošlých termínov:

* 3\. 6\. 2020 - [skupina A](exam/3-6-2020A.pdf); [skupina B](exam/3-6-2020B.pdf)
* [5. 6. 2020](exam/5-6-2020.pdf)
* [10. 6. 2020](exam/10-6-2020.pdf)

## Odporúčaná literatúra <a name="textbooks"></a>

* SINČÁK, ANDREJKOVÁ: Neuronové siete I., Inžiniersky prístup, Elfa, Košice, 1996 - [1. diel](lectures/Neuronove_siete_1.pdf), [2. diel](lectures/Neuronove_siete_2.pdf)
* KRÖSE, van der SMAGT: [An Introduction to Neural Networks](lectures/An_Introduction_to_Neural_Networks.pdf)
* [Stuttgart Neural Network Simulator v4.2 User Manual](lectures/SNNS_v4.2._Manual.pdf)
* HAYKIN: Neural Networks: A Comprehensive Foundation, MacMillan, 1994
* ďalšie zdroje budú dodané na prednáškach