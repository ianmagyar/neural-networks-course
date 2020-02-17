# Lab 0: Getting started

V rámci tohto predmetu budeme programovať v jazyku Python. Python je multiparadigmový jazyk, ktorý nám umožní rýchlu implementáciu a testovanie neurónových sietí. Zároveň podporuje najmodernejšie knižnice pre podporu hlbokého učenia a na vytváranie jednoduchých neurónových sietí - TensorFlow a Keras. V tomto návode vám ukážeme ako si pripravíte programátorské prostredie pre semester.

## Krok 1: Inštalácia Pythonu
Na tomto predmete použijeme Python 3, ktorú si môžete stiahnuť z [web stránky jazyka](https://www.python.org/downloads/). My ale odporúčame nainštalovať inú distribúciu Pythonu [Anaconda](https://www.anaconda.com), ktorá obsahuje niekoľko predinštalovaných knižníc pre prácu s údajmi a strojové učenie.

### Krok 1.1: Nainštalujte si Anacondu
Anaconda je voľne dostupná z [tejto stránky](https://www.anaconda.com/distribution/). Dávajte si pozor, aby ste nainštalovali verziu s Pythonom 3.

### Krok 1.2: Vytvorte virtuálne prostredie s Pythonom 3.7
Anaconda je dostupná iba pre najnovšie verzie Pythonu, teda v čase písania tohto návodu 3.7. Python aj Anaconda ale umožnia vytvorenie virtuálnych prostredí. Predstavte si to ako sandbox, v ktorom môžete mať nainštalované ľubovoľné knižnice a nástroje bez toho aby ste ovplyvnili hlavné prostredie. Práca s virtuálnymi prostrediami ďalej zabráni tomu, aby ste znefunkčnili inštaláciu Pythonu. V prípade problémov s virtuálnym prostredí viete ho jednoducho vymazať a vytvoriť nové.

Vytvorenie virtuálneho prostredie je veľmi jednoduché (podrobný návod [tu](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python)). Spustite príkazový riadok Anacondy (Anaconda Prompt) s admin právami a zadajte príkaz

```conda create --name VENV_NAME python=3.7```

kde `VENV_NAME` je názov virtuálneho prostredia a parameter `python` špecifikuje verziu jazyka. Aby ste mohli pracovať s virtuálnym prostredím, musíte ho aktivovať príkazom:

```conda activate VENV_NAME```

kde `VENV_NAME` je názov prostredia. Deaktivujete ho príkazom:

```conda deactivate```

### Krok 1.3: Nastavenie interpretera
Ak vaše kódy chcete spustiť cez príkazový riadok, robte to cez Anaconda prompt a nezabudnite aktivovať virtuálne prostredie. Alternatívnym riešením je nastavenie cesty ku virtuálnemu prostrediu.

Po aktivácii vyžadovaného virtuálneho prostredia zadajte príkaz

```where python```

Zobrazí sa vám niekoľko absolútnych ciest, nás zaujíma cesta ku súboru `python.exe` vo virtuálnom prostredí, napr.

```C:\ProgramData\Anaconda3\envs\deeplearning\python.exe```

Posledná úloha ktorá vám ostáva je pridanie tejto cesty do systémovej premennej Path (návod k tomu nájdete [tu](https://docs.telerik.com/teststudio/features/test-runners/add-path-environment-variables)). Pre jednoznačné použitie viacerých Python interpreterov vám odporúčame premenovať `python.exe` napr. na `python36.exe`. Tým pádom pri spustení kódu môžete použiť príkaz `python36` a kód sa vám spustí bez toho aby ste museli aktivovať virtuálne prostredie.

Ak na spustenie kódu používate IDE, nastavte správny interpreter v projekte.

### Krok 1.4: Aktualizujte vybrané knižnice
Cez príkazový riadok Anacondy (uistite sa že vaše virtuálne prostredie je aktivované) aktualizujte niektoré knižnice, ktoré budeme používať počas semestra (ak knižnice ešte nemáte nainštalované, tieto príkazy ich nainštalujú):

```
pip install numpy --upgrade
pip install matplotlib --upgrade
pip install scipy --upgrade
pip install sklearn --upgrade
```

## Krok 2: Inštalácia TensorFlow a Keras
TensorFlow a Keras ako aj ďalšie knižnice nainštalujete pomocou `pip`. Do príkazového riadku Anacondy (uistite sa že vaše virtuálne prostredie je aktivované) zadajte príkazy:

```
pip install tensorflow
pip install keras
```

Knižnice `TensorFlow` a `Keras` sa nainštalujú automaticky spolu s potrebnými závislosťami. V prípade problémov sa obráťte na stránky [TensorFlow](https://www.tensorflow.org/install/pip) a [Keras](https://keras.io/#installation).

## Krok 3: Skontrolujte si inštaláciu
V príkazovom riadku Anacondy spusťte Python zadaním príkazu `python` (alebo názov podľa bodu 1.3) a následne skúsťte naimportovať nainštalované knižnice:

```
import tensorflow
import keras
```

Prvý import môže potrvať niekoľko sekúnd. Ak počas importu sa vyskytnú problémy s niektorou knižnicou, potrebujete si ju aktualizovať podľa príkazov uvedených v bode 1.4.

Python zastavíte zadaním príkazu `exit()`.