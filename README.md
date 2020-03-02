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
| Týždeň 2<br>24. 2. - 1. 3.   |           | [perceptrón](labs/lab02-perceptron.ipynb)                          |                          |
| Týždeň 3<br>2. 3. - 8. 3.    |           | [multilayer perceptron](labs/lab03-multilayer-perceptron.ipynb)    |                          |
| Týždeň 4<br>9. 3. - 15. 3.   |           | odvodenie backpropagation algoritmu                                | zverejnenie zadania 2    |
| Týždeň 5<br>16. 3. - 22. 3.  |           | predspracovanie údajov, metodológia trénovania NS, vyhodnotenie NS | odovzdávka zadania 1     |
| Týždeň 6<br>23. 3. - 29. 3.  |           | prezentácia článkov                                                |                          |
| Týždeň 7<br>30. 3. - 5. 4.   |           | nekontrolované učenie                                              | zverejnenie zadania 3    |
| Týždeň 8<br>6. 4. - 12. 4.   |           | Hebbovo učenie                                                     | odovzdávka zadania 2     |
| Týždeň 9<br>13. 4. - 19. 4.  |           | Veľká Noc                                                          |                          |
| Týždeň 10<br>20. 4. - 26. 4. |           | NS v Tensorflow a Keras                                            | zverejnenie zadania 4    |
| Týždeň 11<br>27. 4. - 3. 5.  |           | autoenkódery                                                       |                          |
| Týždeň 12<br>4. 5. - 10. 5.  |           | odovzdanie zadaní 3 a 4                                            | odovzdávka zadania 3 a 4 |
| Týždeň 13<br>11. 5. - 17. 5. |           | zápočtový týždeň                                                   |                          |

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
2. implementácia algoritmu backpropagation (10 b)
3. implementácia nekontrolovaného učenia pomocou Kohonenovej siete (10 b),
4. trénovanie neurónovej siete pre klasifikáciu pomocou knižnice Keras (5 b).

Otázky na skúšku nájdete [tu](exam/otazky_ZNS_skuska.pdf).

## Odporúčaná literatúra <a name="textbooks"></a>

* SINČÁK, ANDREJKOVÁ: Neuronové siete I., Inžiniersky prístup, Elfa, Košice, 1996 - [1. diel](lectures/Neuronove_siete_1.pdf), [2. diel](lectures/Neuronove_siete_2.pdf)
* KRÖSE, van der SMAGT: [An Introduction to Neural Networks](lectures/An_Introduction_to_Neural_Networks.pdf)
* [Stuttgart Neural Network Simulator v4.2 User Manual](lectures/SNNS_v4.2._Manual.pdf)
* HAYKIN: Neural Networks: A Comprehensive Foundation, MacMillan, 1994
* ďalšie zdroje budú dodané na prednáškach