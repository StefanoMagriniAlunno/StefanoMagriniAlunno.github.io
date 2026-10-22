# Esercizi Programmazione I

| Blocco | Argomento | Esercizi |
| --- | --- | --- |
| A | Pseudocodice | 15 |
| B | Struttura di un programma e compilazione | 15 |
| C | LEGGI, ASSEGNA e VISUALIZZA | 60 |
| D | IF/ELSE e FOR/WHILE | 45 |
| E | Controllo di flusso e debugging con gdb | 20 |
| F | Tipi di dato, switch e array | 20 |
| G | Array, ordinamento e tempi di esecuzione | 20 |
| H | Matrici e gprof | 20 |
| I | Le funzioni e la documentazione | 20 |
| J | Ricorsione e classi di memorizzazione | 20 |


## Pacchetto A: Pseudocodice

Vediamo qui un esempio di algoritmo in pseudocodice per il calcolo dell'area di un rettangolo. LEGGI acquisisce i dati, ASSEGNA calcola un valore e lo conserva in una variabile, VISUALIZZA mostra il risultato; i nomi delle variabili iniziano con `_`.

```text
INIZIO
    LEGGI _base e _altezza
    ASSEGNA a _area il valore _base x _altezza
    VISUALIZZA _area
FINE
```

### Esercizi (A1-A15)

**A1.** L'algoritmo dell'esempio calcola l'area di un rettangolo di cui legge base e altezza. Modificatelo perche' calcoli il perimetro, sempre leggendo base e altezza. Poi eseguitelo a mano con base $3$ e altezza $7$: che cosa viene visualizzato?

**A2.** Scrivete un algoritmo che legge il lato di un quadrato e ne visualizza l'area. Eseguitelo a mano con lato $4$.

**A3.** Scrivete un algoritmo che legge tre numeri e visualizza la loro media.

**A4.** Scrivete un algoritmo che legge una temperatura C in gradi Celsius e visualizza il valore in gradi Fahrenheit, con $F = \frac95 C + 32$.

**A5.** Le righe di questo algoritmo per l'area del triangolo sono in disordine. Rimettetele nell'ordine giusto.

```text
INIZIO
    VISUALIZZA _area
    LEGGI _altezza
    ASSEGNA a _area il valore _base x _altezza / 2
    LEGGI _base
FINE
```

**A6.** Eseguite a mano l'algoritmo e scrivete cosa viene visualizzato.

```text
INIZIO
    ASSEGNA a _x il valore 5
    ASSEGNA a _y il valore _x+2
    ASSEGNA a _x il valore _y*2
    VISUALIZZA _x
    VISUALIZZA _y
FINE
```

**A7.** Scrivete un algoritmo che legge due numeri e visualizza il maggiore dei due.

**A8.** Scrivete un algoritmo che legge un voto d'esame (da $0$ a $30$) e visualizza "Superato" se il voto e' almeno $18$, altrimenti "Non superato".

**A9.** Scrivete un algoritmo che legge un numero e ne visualizza il valore assoluto.

**A10.** Un accumulatore parte da $0$ e riceve, uno dopo l'altro, i valori $2$, $4$, $6$, $8$, $10$. Completate la tabella con il valore dell'accumulatore dopo ogni passo.

| Valore ricevuto | 2 | 4 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- |
| Accumulatore |  |  |  |  |  |

**A11.** Completate l'algoritmo, che conta quanti numeri positivi vengono letti prima del primo numero minore o uguale a $0$.

```text
INIZIO
    ASSEGNA a _conta il valore 0
    LEGGI _numero
    FINCHE' _numero > 0
        ASSEGNA a _conta il valore ________
        LEGGI _numero
    FINE
    VISUALIZZA ________
FINE
```

**A12.** Scrivete un algoritmo che legge numeri finche' sono positivi e alla fine visualizza la loro somma. Suggerimento: usate un accumulatore, come in A10.

**A13.** Un algoritmo deve avere quattro proprieta': **finitezza** (e' formato da un numero finito di istruzioni), **determinismo** (le istruzioni non sono ambigue: chiunque le esegua, con gli stessi dati, ottiene lo stesso risultato), **generalita'** (risolve una famiglia di problemi, non un caso solo) ed **eseguibilita'** (ogni azione si puo' davvero eseguire con i mezzi a disposizione). Ognuno di questi quattro "algoritmi" ne viola una, e ogni proprieta' e' violata da uno solo di essi. Dite quale.

1. "Leggi un numero; se e' grande visualizza *Grande*."
2. Un algoritmo che dovrebbe calcolare l'area di *qualsiasi* rettangolo, scritto cosi': "Assegna a Base il valore 3, ad Altezza il valore 5, visualizza Base\*Altezza".
3. "Visualizza l'ultima cifra decimale di $\pi$."
4. "Visualizza 1; visualizza 2; visualizza 3; e cosi' via, con un'istruzione per ogni numero naturale."

**A14.** Eseguite a mano l'algoritmo. Completate la tabella con i valori di _somma e _i alla fine di ogni giro del ciclo, poi dite cosa viene visualizzato e quante volte viene eseguito il ciclo.

```text
INIZIO
    ASSEGNA a _i il valore 1
    ASSEGNA a _somma il valore 0
    FINCHE' _i <= 4
        ASSEGNA a _somma il valore _somma + _i
        ASSEGNA a _i il valore _i + 1
    FINE
    VISUALIZZA _somma
FINE
```

| Giro | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| _somma |  |  |  |  |
| _i |  |  |  |  |

**A15.** Scrivete un algoritmo che legge un numero e visualizza "Positivo", "Negativo" oppure "Zero". Suggerimento: i casi sono tre, quindi un solo SE non basta; dentro l'ALTRIMENTI di un primo SE potete scriverne un secondo.

```text
SE _numero > 0 ALLORA
    ...
ALTRIMENTI
    ...
FINE
```


## Pacchetto B: Struttura di un programma e compilazione

Vediamo qui la struttura che hanno tutti i programmi C: il richiamo delle librerie, la funzione `main` con il suo corpo e il valore di ritorno.

```c
#include <stdio.h>

int main(void) {
    // codice
    return 0;
}
```

Per compilare il file sorgente `area.c` ed eseguire il programma ottenuto si usano due comandi:

```bash
gcc -o area area.c
./area
```

### Esercizi (B1-B15)

**B1.** Completate lo scheletro con le parole mancanti.

```c
#include <________>

int ________(void) {
    // codice
    return ___;
}
```

**B2.** Rimettete in ordine le righe per ottenere un programma che funziona.

```c
    return 0;
}
#include <stdio.h>
    printf("Ciao!\n");
int main(void) {
```

**B3.** Per ogni riga del programma, scrivete a cosa serve.

```c
#include <stdio.h>
int main(void) {
    int area, base;
    base = 3;
    /* calcolo dell'area di un rettangolo di altezza 5 */
    area = base * 5;
    printf("Area = %d\n", area);
    return 0;
}
```

**B4.** Scrivete un programma completo, con la struttura vista sopra, che visualizza la frase `Ciao, mondo!`.

**B5.** Scrivete un programma che visualizza il vostro nome su una riga e il vostro cognome sulla riga successiva.

**B6.** Quale valore restituisce `main` quando il programma termina con successo? Che cosa comunica al sistema un valore diverso?

**B7.** Quali di questi nomi vanno bene per un file sorgente C, cioe' si possono scrivere cosi' come sono nel comando `gcc` visto sopra? Per quelli sbagliati, dite perche'.

- `esercizio1.c`
- `esercizio 1.c`
- `area.txt`
- `area_rettangolo.c`
- `area.c.txt`

**B8.** Scrivete il comando `gcc` che compila il file `perimetro.c` producendo l'eseguibile `perimetro`, poi il comando per eseguirlo.

**B9.** Nel comando `gcc -o calcolo media.c`, qual e' il file sorgente? Come si chiamera' il programma eseguibile?

**B10.** Mettete in ordine le quattro fasi: Link, Editing, Esecuzione, Compilazione. Poi abbinate ogni descrizione alla sua fase. Nota, la precompilazione fa parte della compilazione.

| Descrizione | Fase |
| --- | --- |
| Il contenuto di `stdio.h` viene copiato dentro il sorgente |  |
| Il programmatore scrive il codice e lo salva in un file `.c` |  |
| Vengono segnalati gli errori di sintassi |  |
| Il codice delle librerie usate viene unito al nostro |  |
| Il programma viene caricato in memoria |  |

**B11.** Il preprocessore sostituisce le costanti definite con `#define`. Come diventa l'ultima riga dopo la precompilazione?

```c
#define PI 3.14159
/* ... */
circonferenza = 2 * PI * raggio;
```

**B12.** Quali parti di questo codice vengono ignorate dal compilatore?

```c
/* Programma che calcola
   il doppio di un numero */
int main(void) {
    int n, doppio;   // dichiarazioni
    n = 21;
    doppio = 2 * n;  // doppio = 42
    return 0;
}
```

**B13.** Il programma compila e stampa `Perimetro = 16`, ma e' difficile da leggere: al compilatore non interessa come andiamo a capo, a chi legge il codice si'. Riscrivetelo con un'istruzione per riga e l'indentazione corretta.

```c
#include <stdio.h>
int main(void) { int lato; lato = 4;
printf("Perimetro = %d\n", 4 * lato); return 0; }
```

**B14.** Aggiungete i commenti a questo programma: uno su piu' righe all'inizio, che spiega cosa fa il programma, e uno su una sola riga accanto a ogni istruzione di calcolo.

```c
#include <stdio.h>

int main(void) {
    int base, altezza, area;
    base = 6;
    altezza = 4;
    area = base * altezza / 2;
    printf("Area = %d\n", area);
    return 0;
}
```

**B15.** Salvate il programma di B4 nel file `saluto.c`, compilatelo con `gcc -o saluto saluto.c` ed eseguitelo. Poi cambiate il messaggio in `Ciao, Ferrara!`, salvate il file e rieseguite `./saluto` senza ricompilare. Cosa viene stampato? Perche'?

## Pacchetto C: LEGGI, ASSEGNA e VISUALIZZA

Con variabili, espressioni, `printf` e `scanf` si possono gia' scrivere programmi completi: leggono dei dati dalla tastiera, fanno un calcolo e mostrano il risultato. Vediamo qui un esempio: l'area di un rettangolo con base e altezza scelte dall'utente.

```c
#include <stdio.h>

int main(void) {
    int base, altezza, area;
    printf("Inserisci base e altezza: ");
    scanf("%d %d", &base, &altezza);
    area = base * altezza;
    printf("Area = %d\n", area);
    return 0;
}
```

Per controllare come funzionano tipi di dato, operatori, `printf` e `scanf` potete consultare [cppreference](https://it.cppreference.com/c), il manuale di riferimento del linguaggio C.

### Esercizi (C1-C40)

#### Variabili e tipi di dato

**C1.** Per ogni nome, dite se e' un nome di variabile valido in C. Se non lo e', scrivete quale regola viola.

| Nome | Valido? | Perche' |
| --- | --- | --- |
| `base` |  |  |
| `2lato` |  |  |
| `_temp` |  |  |
| `area totale` |  |  |
| `area_totale` |  |  |
| `int` |  |  |
| `Altezza` |  |  |
| `x1` |  |  |
| `media-voti` |  |  |
| `perimetro!` |  |  |
| `return` |  |  |
| `lato2` |  |  |

**C2.** Questo frammento non compila. Perche'?

```c
int base;
Base = 3;
```

**C3.** Scegliete il tipo piu' adatto (`int`, `float`, `double`, `char`) per ciascun dato. `float` e `double` servono entrambi per i numeri con la virgola: scegliete `double` solo quando serve molta precisione.

| Dato | Tipo |
| --- | --- |
| Numero di studenti in aula |  |
| Prezzo di un caffe' in euro |  |
| Iniziale del vostro nome |  |
| Il numero $\pi$ con $15$ cifre decimali |  |
| Anno di nascita |  |
| Media dei voti d'esame |  |
| Voto di un singolo esame |  |

**C4.** Scrivete le dichiarazioni per: una variabile intera `n`; due variabili `float` di nome `x` e `y` in una sola riga; una variabile `char` di nome `lettera`; una variabile `double` di nome `epsilon`.

**C5.** In C si puo' dichiarare una variabile e darle subito un valore: `int base; base = 3;` e `int base = 3;` hanno lo stesso effetto. Riscrivete in una sola riga `float prezzo; prezzo = 1.20;` e `char c; c = 'x';`.

**C6.** Quale di queste tre righe assegna correttamente la lettera m alla variabile `lettera` di tipo `char`?

```c
lettera = m;
lettera = 'm';
lettera = "m";
```

**C7.** Cosa contiene `n` alla fine? Provate a indovinare, poi verificate al computer con una `printf`.

```c
int n;
n = 3.9;
```

**C8.** Il programma funziona, ma i nomi non aiutano a capire cosa calcola. Riscrivetelo con nomi significativi.

```c
#include <stdio.h>
int main(void) {
    float a, b, c;
    a = 6;
    b = 4;
    c = a * b / 2;
    printf("%f\n", c);
    return 0;
}
```

#### Assegnamento ed espressioni

L'operatore `=` non e' l'uguale della matematica: calcola il valore a destra e lo scrive nella variabile a sinistra.

**C9.** Completate la tabella con il valore di `a` e `b` dopo ogni riga. Scrivete "?" se la variabile non ha ancora un valore.

```c
int a, b;
a = 4;
b = a + 3;
a = b * 2;
b = b - a;
```

| Dopo la riga | a | b |
| --- | --- | --- |
| `a = 4;` |  |  |
| `b = a + 3;` |  |  |
| `a = b * 2;` |  |  |
| `b = b - a;` |  |  |

**C10.** Stesso esercizio con tre variabili.

```c
int x, y, z;
x = 2;
y = x * x;
z = y + x;
x = z - y;
```

| Dopo la riga | x | y | z |
| --- | --- | --- | --- |
| `x = 2;` |  |  |  |
| `y = x * x;` |  |  |  |
| `z = y + x;` |  |  |  |
| `x = z - y;` |  |  |  |

**C11.** In matematica $x = x + 1$ non ha soluzioni; in C e' un'istruzione normalissima. Quanto vale `x` alla fine?

```c
int x;
x = 5;
x = x + 1;
x = x * 2;
```

**C12.** La variabile `somma` fa da accumulatore. Scrivete il suo valore dopo ogni riga.

```c
int somma;
somma = 0;
somma = somma + 1;
somma = somma + 2;
somma = somma + 3;
somma = somma + 4;
```

**C13.** Vogliamo scambiare i valori di `a` (che vale $3$) e `b` (che vale $8$). Perche' queste due righe non funzionano? Scrivete una versione corretta usando una terza variabile `temp`.

```c
a = b;
b = a;
```

**C14.** Divisione tra interi. Prevedete il valore di `q` e di `r`, poi verificate al computer. Cosa cambia se scrivete `r = 7.0 / 2;`?

```c
int a, b, q;
float r;
a = 7;
b = 2;
q = a / b;
r = a / b;
```

**C15.** Calcolate il valore di ciascuna espressione tra interi, rispettando la precedenza degli operatori.

1. `2 + 3 * 4`
2. `(2 + 3) * 4`
3. `10 - 4 - 3`
4. `20 / 4 * 2`
5. `20 / (4 * 2)`

**C16.** Traducete in C queste formule; `x`, `a`, `b`, `h`, `r` sono variabili gia' dichiarate. Attenzione: in C il simbolo `^` **non** e' l'elevamento a potenza.

1. $a^2 + b^2$
2. $(a + b) / 2$
3. $3x^2 - 2x + 1$
4. $b \cdot h / 2$
5. $2 \pi r$, con $\pi \approx 3.14159$

**C17.** Per calcolare la media di `a = 4` e `b = 8` qualcuno scrive `media = a + b / 2;`. Quanto vale `media`? Correggete l'espressione.

**C18.** Prevedete il valore stampato, poi correggete il programma perche' stampi la media giusta, cioe' `26.333334`.

```c
int v1, v2, v3;
float media;
v1 = 24;
v2 = 27;
v3 = 28;
media = (v1 + v2 + v3) / 3;
printf("%f\n", media);
```

**C19.** Quali di questi assegnamenti sono corretti in C?

```c
x = 5;
5 = x;
y = x + 1;
x + 1 = y;
area = base * altezza;
base * altezza = area;
```

#### Output con printf

`printf` stampa il testo tra virgolette e sostituisce ogni formattatore con un valore, nell'ordine in cui compaiono.

**C20.** Completate la tabella dei formattatori.

| Tipo | Formattatore |
| --- | --- |
| `int` |  |
| `float` |  |
| `double` |  |
| `char` |  |

**C21.** Scrivete esattamente cosa compare sullo schermo nei due casi. Qual e' la differenza?

```c
/* caso 1 */
printf("Ciao");
printf("mondo");

/* caso 2 */
printf("Ciao\n");
printf("mondo\n");
```

**C22.** Cosa stampano le due `printf`? Qual e' la differenza?

```c
int base;
base = 3;
printf("Base:%d\n", base);
printf("Base: %d\n", base);
```

**C23.** Cosa stampa questa riga? Disegnate l'output rispettando gli spazi.

```c
printf("x\ty\n1\t2\n");
```

**C24.** Prevedete l'output: quante cifre decimali compaiono?

```c
float prezzo;
prezzo = 2.5;
printf("Prezzo: %f euro\n", prezzo);
```

**C25.** Con `a = 3` e `b = 4`, cosa stampa questa riga?

```c
printf("%d + %d = %d\n", a, b, a + b);
```

**C26.** Con `base = 3` e `altezza = 5`, cosa stampa questa riga? E' quello che voleva il programmatore?

```c
printf("Base: %d, Altezza: %d\n", altezza, base);
```

**C27.** Scrivete una sola `printf` per ciascuno di questi output.

1. `Area = 15`, usando la variabile intera `area`.
2. `Lato: 4` su una riga e `Perimetro: 16` sulla riga sotto, usando le variabili `lato` e `perimetro`.
3. Questa tabellina, con le colonne separate da una tabulazione:

```text
n	n*n
1	1
2	4
3	9
```

**C28.** Completate il programma perche' stampi `Iniziale: M`.

```c
char iniziale;
iniziale = ____;
printf("Iniziale: ____\n", iniziale);
```

**C29.** Con una o piu' `printf`, disegnate questo rettangolo di asterischi. Poi disegnate anche il triangolo.

```text
*****
*   *
*****

*
**
***
****
```

#### Input con scanf

`scanf` legge un valore dalla tastiera e lo scrive in una variabile: e' l'istruzione LEGGI del Pacchetto A. Tre regole:

- Davanti al nome della variabile va la `&`: dice a `scanf` dove scrivere il valore. Dimenticarla e' l'errore piu' comune.
- Tra le virgolette vanno solo i formattatori, niente testo e niente `\n`: il messaggio per l'utente si stampa prima, con `printf`.
- I formattatori sono quelli di `printf`, con un'eccezione: per un `double` in `scanf` serve `%lf`, non `%f`.

Negli output attesi, i numeri dopo i due punti sono quelli digitati dall'utente.

**C30.** Completate il programma, che legge un intero e lo ristampa.

```c
int n;
printf("Inserisci un numero: ");
scanf("____", ____n);
printf("Hai inserito %d\n", n);
```

**C31.** Completate la tabella con il formattatore da usare in `scanf`.

| Tipo della variabile | Formattatore in scanf |
| --- | --- |
| `int` |  |
| `float` |  |
| `double` |  |
| `char` |  |

**C32.** Scrivete un programma che chiede l'eta' e la ristampa.

```text
Quanti anni hai? 19
Hai 19 anni
```

**C33.** Trova l'errore. Subito dopo aver inserito il numero, il programma va in crash: di solito il terminale scrive `Segmentation fault`.

```c
int n;
printf("Inserisci un numero: ");
scanf("%d", n);
printf("Hai inserito %d\n", n);
```

**C34.** Trova l'errore. Inserendo `1.5`, il programma non stampa `Il doppio e' 3.000000`.

```c
double x;
printf("Inserisci un numero decimale: ");
scanf("%f", &x);
printf("Il doppio e' %f\n", 2 * x);
```

**C35.** Trova l'errore. Il programma non mostra nessun messaggio e, qualunque numero si inserisca, stampa un valore a caso.

```c
int n;
scanf("Inserisci un numero: %d", &n);
printf("Hai inserito %d\n", n);
```

#### Calcolatori interattivi

Per ogni programma scrivete prima l'algoritmo in pseudocodice, come nel Pacchetto A, poi il codice completo.

**C36.** Scrivete un programma che legge base e altezza di un rettangolo e ne stampa il perimetro: e' l'algoritmo di A1 tradotto in C.

```text
Inserisci base: 3
Inserisci altezza: 5
Perimetro = 16
```

**C37.** Leggete due interi con una sola `scanf` e stampate somma, differenza e prodotto. Suggerimento: `scanf("%d %d", &a, &b);`

```text
Inserisci due numeri: 7 3
Somma = 10
Differenza = 4
Prodotto = 21
```

**C38.** Traducete in C l'algoritmo di A3 per tre voti interi, con una variabile `float` per la media. Attenzione alla divisione intera, come in C18.

```text
Inserisci tre voti: 24 27 28
Media = 26.333334
```

**C39.** Traducete in C l'algoritmo di A4, con variabili `double` per le temperature.

```text
Temperatura in gradi C: 37.5
37.500000 gradi C = 99.500000 gradi F
```

**C40.** **Sfida.** All'universita' la media e' pesata sui crediti (CFU), cioe' ogni voto conta tanto quanti sono i crediti del suo esame. Scrivete un programma che legge due voti con i rispettivi crediti e stampa la media pesata $\frac{v_1 c_1 + v_2 c_2}{c_1 + c_2}$. Attenzione, anche qui, alla divisione intera.

```text
Primo voto e crediti: 24 6
Secondo voto e crediti: 30 9
Media pesata = 27.600000
```

### Trova l'errore (C41-C50)

Ogni programma contiene un errore (C50 ne contiene due). Trovatelo, correggetelo e dite di che tipo e': **sintattico** se gcc si rifiuta di compilare, **progettuale** se il programma compila e parte, ma fa la cosa sbagliata. Il tipo non e' indicato: capirlo fa parte dell'esercizio. Provate prima su carta, poi verificate compilando con `gcc -Wall`, che segnala anche alcuni errori progettuali. Attenzione: anche un errore che sembra di battitura e' progettuale, se gcc accetta il programma lo stesso.

**C41.** Il programma calcola l'area di un rettangolo ed e' stato tradotto dallo pseudocodice del Pacchetto A. Con base $3$ e altezza $5$ deve stampare `Area = 15`.

```c
#include <stdio.h>

int main(void) {
    int base, altezza, area;
    printf("Inserisci base e altezza: ");
    scanf("%d %d", &base, &altezza);
    area = base x altezza;
    printf("Area = %d\n", area);
    return 0;
}
```

**C42.** Anche questo programma calcola l'area di un rettangolo: con base $3$ e altezza $5$ deve stampare `Area = 15`.

```c
#include <stdio.h>

int main(void) {
    int base, altezza, area;
    area = base * altezza;
    printf("Inserisci base e altezza: ");
    scanf("%d %d", &base, &altezza);
    printf("Area = %d\n", area);
    return 0;
}
```

**C43.** Il programma calcola il perimetro di un quadrato: con lato $4$ deve stampare `Perimetro = 16`.

```c
#include <stdio.h>

int main(void) {
    Int lato, perimetro;
    printf("Inserisci il lato: ");
    scanf("%d", &lato);
    perimetro = 4 * lato;
    printf("Perimetro = %d\n", perimetro);
    return 0;
}
```

**C44.** Il programma calcola quanto costano tre caffe' da $2,50$ euro l'uno: deve stampare `Tre caffe' costano 7.500000 euro`.

```c
#include <stdio.h>

int main(void) {
    float prezzo, totale;
    prezzo = 2,50;
    totale = prezzo * 3;
    printf("Tre caffe' costano %f euro\n", totale);
    return 0;
}
```

**C45.** Il programma somma due numeri: con $7$ e $3$ deve stampare `Somma = 10`.

```c
#include <stdio.h>

int main(void) {
    int a, b, somma;
    printf("Inserisci due numeri: ");
    scanf("%d %d", &a, &b);
    somma = a + b;
    printf("Somma = %d\n, somma);
    return 0;
}
```

**C46.** Il programma chiede base e altezza separatamente: con $3$ e $5$ deve stampare `Area = 15`.

```c
#include <stdio.h>

int main(void) {
    int base, altezza, area;
    printf("Inserisci base: ");
    scanf("%d", &base);
    printf("Inserisci altezza: ");
    scanf("%d", &base);
    area = base * altezza;
    printf("Area = %d\n", area);
    return 0;
}
```

**C47.** Il programma calcola il diametro di un cerchio: con raggio $2.5$ deve stampare `Diametro = 5.000000`.

```c
#include <stdio.h>

int main(void) {
    printf("Inserisci il raggio: ");
    scanf("%lf", &raggio);
    double raggio, diametro;
    diametro = 2 * raggio;
    printf("Diametro = %f\n", diametro);
    return 0;
}
```

**C48.** Il programma calcola l'area di un quadrato: con lato $3$ deve stampare `Area = 9`.

```c
#include <stdio.h>

int main(void) {
    int lato, area;
    printf("Inserisci il lato del quadrato: ");
    scanf("%d", &lato);
    area = lato^2;
    printf("Area = %d\n", area);
    return 0;
}
```

**C49.** Il programma applica uno sconto del 20%: con un prezzo di $50$ euro deve stampare `Con lo sconto del 20 per cento: 40.000000 euro`.

```c
#include <stdio.h>

int main(void) {
    float prezzo, finale;
    printf("Prezzo di listino: ");
    scanf("%f", &prezzo);
    finale = prezzo * (1 - 20 / 100);
    printf("Con lo sconto del 20 per cento: %f euro\n", finale);
    return 0;
}
```

**C50.** Due errori, uno sintattico e uno progettuale. Il programma traduce la formula di A4, $F = \frac95 C + 32$: con $37.5$ gradi Celsius deve stampare `37.500000 gradi C = 99.500000 gradi F`.

```c
#include <stdio.h>

int main(void) {
    double c, f;
    printf("Temperatura in gradi C: ");
    scanf("%lf", &c)
    f = 9 / 5 * c + 32;
    printf("%f gradi C = %f gradi F\n", c, f);
    return 0;
}
```

### Mini-programmi (C51-C60)

Ogni programma legge i dati con `scanf`, fa i calcoli e stampa il risultato. Scrivete prima l'algoritmo in pseudocodice, poi il codice; provate anche con valori diversi da quelli dell'esempio.

**C51.** Convertitore da chilometri a miglia, sapendo che un miglio equivale a $1.609$ km. Usate variabili `double`; nell'esempio, la distanza di una maratona.

```text
Distanza in km: 42.195
42.195000 km = 26.224363 miglia
```

**C52.** Prezzo con IVA al 22%: il programma legge il prezzo senza IVA e stampa l'IVA e il prezzo finale. Per stampare solo due cifre decimali usate `%.2f` al posto di `%f`.

```text
Prezzo senza IVA: 50
IVA = 11.00 euro
Prezzo finale = 61.00 euro
```

**C53.** Punto medio del segmento con estremi $A(x_1, y_1)$ e $B(x_2, y_2)$: $M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$.

```text
Coordinate di A: 1 2
Coordinate di B: 5 8
Punto medio: (3.000000, 5.000000)
```

**C54.** Area del trapezio, $\frac{(B + b) \cdot h}{2}$, con le tre misure lette da una sola `scanf`. Attenzione alle parentesi.

```text
Base maggiore, base minore e altezza: 8 4 3
Area del trapezio = 18.000000
```

**C55.** Il programma legge una durata in minuti e la scrive in ore e minuti senza usare l'operatore `%`, che vedrete nel Pacchetto D: bastano la divisione tra interi, la moltiplicazione e la sottrazione.

```text
Durata in minuti: 135
135 minuti = 2 ore e 15 minuti
```

**C56.** Il programma legge le iniziali di nome e cognome in due variabili `char` e le stampa puntate. Suggerimento: leggete ogni carattere con `scanf(" %c", &nome);`, con uno spazio prima di `%c`; senza, la seconda `scanf` legge l'invio premuto dopo la prima lettera.

```text
Iniziale del nome: M
Iniziale del cognome: R
Le tue iniziali: M.R.
```

**C57.** Cambio di valuta: il programma legge un importo in euro e il tasso di cambio, e stampa l'importo in dollari con due decimali.

```text
Importo in euro: 100
Tasso di cambio (dollari per 1 euro): 1.08
100.00 euro = 108.00 dollari
```

**C58.** Soluzione dell'equazione di primo grado $ax + b = 0$, cioe' $x = -b/a$. Supponete $a \neq 0$: il caso $a = 0$ si potra' gestire piu' avanti, con `if`.

```text
Coefficienti a e b di ax + b = 0: 2 6
x = -3.000000
```

**C59.** Retta per due punti: dati $A(x_1, y_1)$ e $B(x_2, y_2)$ con $x_1 \neq x_2$, stampate il coefficiente angolare $m = \frac{y_2 - y_1}{x_2 - x_1}$ e il termine noto $q = y_1 - m x_1$ della retta $y = mx + q$.

```text
Coordinate di A: 1 2
Coordinate di B: 3 8
m = 3.000000
q = -1.000000
```

**C60.** **Sfida.** Il programma legge un numero di tre cifre e stampa le sue cifre, la loro somma e il numero scritto al contrario. Come in C55, non usate l'operatore `%`.

```text
Inserisci un numero di tre cifre: 472
Cifre: 4 7 2
Somma delle cifre = 13
Al contrario: 274
```

## Pacchetto D: IF/ELSE e FOR/WHILE

Con `if` ed `else` un programma puo' scegliere cosa fare; con `for` e `while` puo' ripetere delle istruzioni. Sono il SE e il FINCHE' del Pacchetto A. Vediamo qui un esempio che li usa entrambi: la somma dei numeri da $1$ a $n$, calcolata solo se $n$ e' positivo.

```c
#include <stdio.h>

int main(void) {
    int n, i, somma;
    printf("Inserisci n: ");
    scanf("%d", &n);
    if (n > 0) {
        somma = 0;
        for (i = 1; i <= n; i = i + 1) {
            somma = somma + i;
        }
        printf("Somma da 1 a %d = %d\n", n, somma);
    } else {
        printf("Serve un numero positivo\n");
    }
    return 0;
}
```

La corrispondenza con lo pseudocodice e' diretta:

| Pseudocodice | C |
| --- | --- |
| `SE condizione ALLORA ... ALTRIMENTI ... FINE` | `if (condizione) { ... } else { ... }` |
| `FINCHE' condizione ... FINE` | `while (condizione) { ... }` |

Il `for` e' un modo compatto di scrivere un ciclo che conta: `for (i = 1; i <= 10; i = i + 1)` ripete il corpo con `i` che vale $1, 2, \dots, 10$. Le tre parti, separate da `;`, sono il valore iniziale, la condizione per continuare e l'aggiornamento; `i = i + 1` si puo' scrivere anche `i++`.

Operatori per scrivere le condizioni:

- `==` uguale, `!=` diverso, `<` minore, `>` maggiore, `<=` minore o uguale, `>=` maggiore o uguale. Attenzione: `=` e' l'assegnamento, il confronto e' `==`.
- `&&` e' la "e" (vera se entrambe le condizioni sono vere), `||` e' la "o" (vera se almeno una e' vera), `!` e' la negazione.
- `%` da' il resto della divisione tra interi: `7 % 2` vale $1$. Un numero `n` e' pari se `n % 2 == 0`.

Se un programma non si ferma piu', interrompetelo con Ctrl+C. Come per il Pacchetto C, su [cppreference](https://it.cppreference.com/c) trovate la descrizione di `if`, `for` e `while`.

### Esercizi (D1-D20)

#### IF/ELSE

Negli output attesi, i numeri dopo i due punti sono quelli digitati dall'utente.

**D1.** Con `x = 4` e `y = 7`, dite se ogni condizione e' vera o falsa.

1. `x < y`
2. `x == 4`
3. `y != 7`
4. `x >= 4`
5. `x + 3 == y`
6. `x > 0 && y > 10`
7. `x > 0 || y > 10`
8. `!(x == 4)`

**D2.** Calcolate: `7 % 2`, `8 % 2`, `17 % 5`, `20 % 4`, `3 % 7`.

**D3.** Traducete in C l'algoritmo di A8: il programma legge un voto e stampa `Superato` oppure `Non superato`.

```text
Inserisci il voto: 24
Superato
```

**D4.** Il programma legge un intero e dice se e' pari o dispari.

```text
Inserisci un numero intero: 17
17 e' dispari
```

**D5.** Traducete in C l'algoritmo di A7.

```text
Inserisci due numeri: 12 9
Il maggiore e' 12
```

**D6.** Traducete in C l'algoritmo di A9.

```text
Inserisci un numero: -5
|-5| = 5
```

**D7.** Prevedete l'output.

```c
int x = 10;
if (x > 5) {
    printf("A\n");
}
if (x > 8) {
    printf("B\n");
} else {
    printf("C\n");
}
if (x > 20) {
    printf("D\n");
}
```

**D8.** Il programma legge dividendo e divisore e fa la divisione solo se il divisore non e' $0$; altrimenti stampa `Non posso eseguire la divisione`. Con $10$ e $4$ deve stampare `Quoziente = 2.500000`.

```text
Dividendo: 10
Divisore: 0
Non posso eseguire la divisione
```

**D9.** Il programma legge un numero e stampa, su righe separate, se e' multiplo di $3$, se e' multiplo di $4$ e se e' multiplo di entrambi. Stampa solo le frasi vere: se il numero non e' multiplo ne' di $3$ ne' di $4$, dopo la lettura non stampa nulla.

```text
Inserisci un numero: 12
12 e' multiplo di 3
12 e' multiplo di 4
12 e' multiplo di 3 e di 4

Inserisci un numero: 9
9 e' multiplo di 3

Inserisci un numero: 7
```

**D10.** Traducete in C l'algoritmo di A15 (Positivo, Negativo o Zero). Come nello pseudocodice, i casi sono tre: mettete un secondo `if` dentro l'`else` del primo. Provate con un numero positivo, uno negativo e con $0$.

```text
Inserisci un numero: -7
Negativo
```

#### FOR/WHILE

**D11.** Prevedete l'output.

```c
int i;
i = 1;
while (i <= 5) {
    printf("%d\n", i);
    i = i + 1;
}
```

**D12.** Conto alla rovescia con un `while`: il programma chiede da che numero partire, conta fino a $1$ e poi stampa `Via!`.

```text
Da quanto conto? 5
5
4
3
2
1
Via!
```

**D13.** Quante volte viene eseguito il corpo di ciascun ciclo?

| Ciclo | Volte |
| --- | --- |
| `for (i = 0; i < 10; i = i + 1)` |  |
| `for (i = 1; i <= 10; i = i + 1)` |  |
| `for (i = 1; i < 10; i = i + 1)` |  |
| `for (i = 0; i <= 10; i = i + 2)` |  |
| `for (i = 10; i > 0; i = i - 1)` |  |
| `for (i = 5; i < 5; i = i + 1)` |  |

**D14.** Il programma chiede un numero e ne stampa la tabellina da $1$ a $10$ con un `for`.

```text
Di quale numero vuoi la tabellina? 6
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
```

**D15.** Stampate su una riga i numeri pari da $2$ a $20$. Fatelo in due modi: con un `for` a passo $2$, oppure a passo $1$ con un `if` e l'operatore `%`.

```text
2 4 6 8 10 12 14 16 18 20
```

**D16.** Il programma legge $n$ e calcola la somma dei numeri da $1$ a $n$ con un ciclo e un accumulatore. Per controllo stampa anche il risultato della formula di Gauss $\frac{n(n+1)}{2}$.

```text
Inserisci n: 100
Somma con il ciclo = 5050
Somma con la formula = 5050
```

**D17.** Completate la tabella con il valore di `somma` alla fine di ogni giro. Che cosa calcola il programma?

```c
int i, somma;
somma = 0;
for (i = 1; i <= 4; i = i + 1) {
    somma = somma + i * i;
}
```

| Giro (valore di i) | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| somma |  |  |  |  |

**D18.** Il programma legge $n$ e stampa $n!$. Attenzione: da che valore deve partire un accumulatore che moltiplica invece di sommare? Provate con $5$ e con $13$: il risultato di $13!$ e' giusto? Controllatelo con una calcolatrice.

```text
Inserisci n: 5
5! = 120
```

**D19.** Traducete in C gli algoritmi di A11 e A12 insieme: il programma legge numeri finche' sono positivi, poi stampa quanti erano e la loro somma.

```text
Inserisci un numero (0 o negativo per finire): 4
Inserisci un numero (0 o negativo per finire): 7
Inserisci un numero (0 o negativo per finire): 2
Inserisci un numero (0 o negativo per finire): 0
Hai inserito 3 numeri positivi, la somma e' 13
```

**D20.** Il programma legge $n$ e conta quanti multipli di $3$ ci sono tra $1$ e $n$: un `if` dentro un `for`.

```text
Fino a che numero? 100
Tra 1 e 100 ci sono 33 multipli di 3
```

### Trova l'errore (D21-D30)

Ogni programma contiene un errore (D30 ne contiene due). Trovatelo, correggetelo e dite di che tipo e': **sintattico** se gcc si rifiuta di compilare, **progettuale** se il programma compila e parte, ma fa la cosa sbagliata. Il tipo non e' indicato: capirlo fa parte dell'esercizio. Provate prima su carta, poi verificate compilando con `gcc -Wall`.

**D21.** Il programma dice se il numero inserito e' zero: con $0$ deve stampare `Hai inserito zero`.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
    if (n = 0) {
        printf("Hai inserito zero\n");
    } else {
        printf("Hai inserito un numero diverso da zero\n");
    }
    return 0;
}
```

**D22.** Il programma stampa i numeri da $1$ a $10$, uno per riga.

```c
#include <stdio.h>

int main(void) {
    int i;
    for (i = 1, i <= 10, i = i + 1) {
        printf("%d\n", i);
    }
    return 0;
}
```

**D23.** Il programma controlla che un voto sia compreso tra $0$ e $30$: con $45$ deve stampare `Voto non valido`.

```c
#include <stdio.h>

int main(void) {
    int voto;
    printf("Inserisci il voto: ");
    scanf("%d", &voto);
    if (0 <= voto <= 30) {
        printf("Voto valido\n");
    } else {
        printf("Voto non valido\n");
    }
    return 0;
}
```

**D24.** Il programma legge cinque numeri e ne stampa la somma: con $1, 2, 3, 4, 5$ deve stampare `Somma = 15`.

```c
#include <stdio.h>

int main(void) {
    int i, numero, somma;
    somma = 0;
    for (i = 1; i <= 5; i = i + 1) {
        printf("Numero %d: ", i);
        scanf("%d", numero);
        somma = somma + numero;
    }
    printf("Somma = %d\n", somma);
    return 0;
}
```

**D25.** Il programma stampa le somme parziali $1, 3, 6, 10, 15$, una per riga.

```c
#include <stdio.h>

int main(void) {
    int i, somma;
    somma = 0;
    for (i = 1; i <= 5; i = i + 1)
        somma = somma + i;
        printf("Somma parziale: %d\n", somma);
    return 0;
}
```

**D26.** Il programma dice se l'esame e' superato: con $24$ deve stampare `Superato`, con $15$ `Non superato`.

```c
#include <stdio.h>

int main(void) {
    int voto;
    printf("Inserisci il voto: ");
    scanf("%d", &voto);
    if (voto >= 18);
        printf("Superato\n");
    else
        printf("Non superato\n");
    return 0;
}
```

**D27.** Conto alla rovescia da $10$ a $1$, poi `Via!`.

```c
#include <stdio.h>

int main(void) {
    int i;
    i = 10;
    while (i > 0) {
        printf("%d\n", i);
        i = i + 1;
    }
    printf("Via!\n");
    return 0;
}
```

**D28.** Il programma calcola la media di $n$ voti: con i tre voti $24, 27, 28$ deve stampare `Media = 26.333334`.

```c
#include <stdio.h>

int main(void) {
    int n, i, voto, somma;
    float media;
    printf("Quanti voti? ");
    scanf("%d", &n);
    somma = 0;
    for (i = 1; i <= n; i = i + 1) {
        printf("Voto %d: ", i);
        scanf("%d", &voto);
        somma = somma + voto;
    }
    media = somma / n;
    printf("Media = %f\n", media);
    return 0;
}
```

**D29.** Il programma accetta solo numeri da $1$ a $10$: con $45$ deve stampare `Fuori intervallo`.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Inserisci un numero da 1 a 10: ");
    scanf("%d", &n);
    if (n < 1 && n > 10) {
        printf("Fuori intervallo\n");
    } else {
        printf("Hai scelto %d\n", n);
    }
    return 0;
}
```

**D30.** Due errori. Il programma calcola il fattoriale: con $5$ deve stampare `5! = 120`.

```c
#include <stdio.h>

int main(void) {
    int n, i, fattoriale;
    printf("Inserisci n: ");
    scanf("%d", &n);
    fattoriale = 0;
    for (i = 1; i =< n; i = i + 1) {
        fattoriale = fattoriale * i;
    }
    printf("%d! = %d\n", n, fattoriale);
    return 0;
}
```

### Mini-programmi (D31-D40)

Scrivete prima l'algoritmo in pseudocodice, poi il codice; provate anche con valori diversi da quelli dell'esempio.

**D31.** Un anno e' bisestile se e' divisibile per $4$ ma non per $100$, oppure se e' divisibile per $400$. Il programma legge un anno e dice se e' bisestile; provate anche con $1900$ (non bisestile), $2000$ (bisestile) e $2023$.

```text
Inserisci un anno: 2024
2024 e' bisestile
```

**D32.** Il programma legge tre numeri e stampa il maggiore. Suggerimento: partite da `massimo = a` e confrontatelo con gli altri due.

```text
Inserisci tre numeri: 4 9 7
Il maggiore e' 9
```

**D33.** Per l'equazione $ax^2 + bx + c = 0$, il programma legge $a$, $b$, $c$, calcola il discriminante $\Delta = b^2 - 4ac$ e dice quante soluzioni reali ci sono. I casi sono tre: come in D10, usate un `if` dentro l'`else`. Provate anche con $1, 2, 1$ e con $1, 0, 1$.

```text
Coefficienti a, b, c: 1 -3 2
Delta = 1
Due soluzioni reali distinte
```

**D34.** Riprendete C58 e gestite anche il caso $a = 0$: se anche $b = 0$ ogni $x$ e' soluzione (`Infinite soluzioni`), altrimenti non ce n'e' nessuna (`Nessuna soluzione`). Provate con $2, 6$, con $0, 5$ e con $0, 0$.

```text
Coefficienti a e b di ax + b = 0: 0 5
Nessuna soluzione
```

**D35.** In C non esiste l'operatore di potenza: il programma legge base ed esponente (intero, non negativo) e calcola la potenza con un ciclo.

```text
Base ed esponente: 2 10
2 elevato a 10 = 1024
```

**D36.** Il programma legge un numero, stampa tutti i suoi divisori e poi quanti sono.

```text
Inserisci un numero: 36
Divisori di 36: 1 2 3 4 6 9 12 18 36
Sono 9 divisori
```

**D37.** Un numero e' primo se ha esattamente due divisori. Partendo da D36, il programma dice se il numero letto e' primo. Provate con $97$, $91$ e $1$.

```text
Inserisci un numero: 97
97 e' primo
```

**D38.** Generalizzate C60 a numeri con quante cifre volete: in un `while`, `n % 10` da' l'ultima cifra e `n / 10` la toglie. Il programma stampa quante cifre ha il numero e la loro somma.

```text
Inserisci un numero positivo: 90517
Cifre: 5
Somma delle cifre = 22
```

**D39.** "Indovina il numero": il numero segreto e' fissato nel codice (per esempio $42$); il programma chiede un tentativo finche' l'utente non indovina, dice ogni volta `Troppo alto` o `Troppo basso` e alla fine stampa quanti tentativi sono serviti. Suggerimento: per i due messaggi bastano due `if` separati.

```text
Indovina il numero (da 1 a 100): 50
Troppo alto
Indovina il numero (da 1 a 100): 30
Troppo basso
Indovina il numero (da 1 a 100): 42
Indovinato in 3 tentativi!
```

**D40.** **Sfida.** Il programma legge un'altezza e disegna un triangolo di asterischi, con due `for` uno dentro l'altro (riprendete C29).

```text
Altezza del triangolo: 4
*
**
***
****
```

### Dallo pseudocodice al C (D41-D45)

Questi algoritmi sono piu' lunghi di quelli visti finora. Prima di scrivere il codice, eseguiteli a mano con i valori dell'esempio, segnando in una tabella come cambiano le variabili a ogni giro, come in A14. Poi traducete riga per riga: LEGGI diventa `scanf`, VISUALIZZA diventa `printf`, SE diventa `if`, FINCHE' diventa `while`. "Il resto di _a diviso _b" si scrive `a % b`.

**D41.** Statistiche su una sequenza di numeri, terminata da $0$. Attenzione alla divisione intera nella media.

```text
INIZIO
    ASSEGNA a _conta il valore 0
    ASSEGNA a _somma il valore 0
    LEGGI _numero
    ASSEGNA a _massimo il valore _numero
    ASSEGNA a _minimo il valore _numero
    FINCHE' _numero diverso da 0
        ASSEGNA a _somma il valore _somma + _numero
        ASSEGNA a _conta il valore _conta + 1
        SE _numero > _massimo ALLORA
            ASSEGNA a _massimo il valore _numero
        FINE
        SE _numero < _minimo ALLORA
            ASSEGNA a _minimo il valore _numero
        FINE
        LEGGI _numero
    FINE
    SE _conta > 0 ALLORA
        VISUALIZZA _conta, _massimo, _minimo e _somma / _conta
    ALTRIMENTI
        VISUALIZZA "Nessun numero inserito"
    FINE
FINE
```

```text
Inserisci un numero (0 per finire): 4
Inserisci un numero (0 per finire): 9
Inserisci un numero (0 per finire): -2
Inserisci un numero (0 per finire): 7
Inserisci un numero (0 per finire): 0
Numeri inseriti: 4
Massimo: 9
Minimo: -2
Media: 4.500000
```

**D42.** L'algoritmo di Euclide, uno dei piu' antichi che si conoscano, calcola il massimo comune divisore di due numeri positivi; dal MCD si ricava poi il minimo comune multiplo.

```text
INIZIO
    LEGGI _a e _b
    ASSEGNA a _x il valore _a
    ASSEGNA a _y il valore _b
    FINCHE' _y diverso da 0
        ASSEGNA a _r il valore del resto di _x diviso _y
        ASSEGNA a _x il valore _y
        ASSEGNA a _y il valore _r
    FINE
    ASSEGNA a _mcd il valore _x
    ASSEGNA a _mcm il valore _a x _b / _mcd
    VISUALIZZA _mcd e _mcm
FINE
```

```text
Inserisci due numeri positivi: 84 36
MCD(84, 36) = 12
mcm(84, 36) = 252
```

**D43.** Si parte da un numero positivo: se e' pari lo si divide per $2$, se e' dispari lo si moltiplica per $3$ e si aggiunge $1$, e si ripete finche' si arriva a $1$. Nessuno e' ancora riuscito a dimostrare che, partendo da qualsiasi numero, si arrivi sempre a $1$: e' la congettura di Collatz. Provate anche con $27$.

```text
INIZIO
    LEGGI _n
    ASSEGNA a _passi il valore 0
    FINCHE' _n diverso da 1
        VISUALIZZA _n
        SE _n e' pari ALLORA
            ASSEGNA a _n il valore _n / 2
        ALTRIMENTI
            ASSEGNA a _n il valore 3 x _n + 1
        FINE
        ASSEGNA a _passi il valore _passi + 1
    FINE
    VISUALIZZA 1
    VISUALIZZA _passi
FINE
```

```text
Inserisci un numero positivo: 6
6 3 10 5 16 8 4 2 1
Passi: 8
```

**D44.** Conversione in binario, la "lingua" dei computer. Le cifre binarie si ottengono come resti delle divisioni successive per $2$ e vengono composte in un numero che, letto in base $10$, ha le stesse cifre. Provate anche con $1023$ e con $1024$: perche' con $1024$ il risultato e' sbagliato?

```text
INIZIO
    LEGGI _n
    ASSEGNA a _originale il valore _n
    ASSEGNA a _binario il valore 0
    ASSEGNA a _posizione il valore 1
    FINCHE' _n > 0
        ASSEGNA a _cifra il valore del resto di _n diviso 2
        ASSEGNA a _binario il valore _binario + _cifra x _posizione
        ASSEGNA a _posizione il valore _posizione x 10
        ASSEGNA a _n il valore _n / 2
    FINE
    VISUALIZZA _originale e _binario
FINE
```

```text
Inserisci un numero da 0 a 1023: 13
13 in binario: 1101
```

**D45.** Il metodo di Erone (o babilonese) calcola la radice quadrata di un numero $a > 0$: si parte da una stima $x$ e la si migliora ripetendo $x = \frac{1}{2}\left(x + \frac{a}{x}\right)$, finche' $x^2$ e' abbastanza vicino ad $a$. Usate variabili `double`.

```text
INIZIO
    LEGGI _a
    ASSEGNA a _x il valore _a
    ASSEGNA a _passi il valore 0
    ASSEGNA a _errore il valore 1
    FINCHE' _errore > 0.000001
        ASSEGNA a _x il valore (_x + _a / _x) / 2
        ASSEGNA a _passi il valore _passi + 1
        ASSEGNA a _errore il valore _x x _x - _a
        SE _errore < 0 ALLORA
            ASSEGNA a _errore il valore -_errore
        FINE
    FINE
    VISUALIZZA _x e _passi
FINE
```

```text
Inserisci un numero positivo: 2
Radice quadrata di 2.000000 = 1.414214 (in 4 passi)
```

## Pacchetto E: Controllo di flusso e debugging con gdb

Finora, quando un programma dava un risultato sbagliato, potevamo solo rileggere il codice o aggiungere qualche `printf`. In questo pacchetto, accanto ai nuovi esercizi su scelte e cicli, conosciamo due aiutanti che rendono la caccia agli errori piu' semplice: gli **avvisi del compilatore** e il **debugger** `gdb`. Nessuno dei due e' indispensabile per scrivere un programma: servono a capire piu' in fretta perche' non fa quello che vorremmo. Il centro di ogni esercizio resta il programma.

### Gli avvisi del compilatore

Da qui in avanti compilate sempre aggiungendo due opzioni (*flag*):

```bash
gcc -Wall -Wextra -o media media.c
```

`-Wall` attiva gli avvisi (*warning*) piu' importanti: segnalano righe che compilano, ma che quasi sicuramente contengono un errore. `-Wextra` ne aggiunge altri, non compresi in `-Wall`. Un warning ha questa forma:

```text
media.c:10:9: warning: suggest parentheses around assignment used as truth value [-Wparentheses]
```

`media.c:10:9` significa: file `media.c`, riga $10$, colonna $9$. Tra parentesi quadre c'e' il nome dell'avviso. A differenza di un errore (`error`), un warning non blocca la compilazione: l'eseguibile viene creato lo stesso. Pero' un warning segnala quasi sempre un errore progettuale, quindi d'ora in poi la regola e': **un programma e' finito solo quando compila senza warning**. Se compaiono molti messaggi, partite dal primo: spesso gli altri sono una sua conseguenza.

### Il debugger gdb

Un debugger esegue il programma sotto il nostro controllo: possiamo fermarlo su una riga, farlo avanzare un'istruzione alla volta e guardare il valore delle variabili in ogni momento, senza aggiungere nemmeno una `printf`. Su Ubuntu si installa con `sudo apt install gdb`. Lo useremo a partire da E2. Ne bastano pochi comandi, presentati uno alla volta quando servono e riassunti alla fine del pacchetto. Le domande che usano gdb iniziano con **Con gdb.** e di solito sono l'ultima domanda dell'esercizio: servono a guardare il programma dall'interno, mentre funziona.

### Esercizi (E1-E10)

#### Primi passi con warning e gdb

**E1.** Spostatevi con `cd` nella cartella in cui salverete i file di questo pacchetto (`pwd` vi dice in che cartella vi trovate) e salvate il programma nel file `media.c`. Il programma deve calcolare la media di tre voti e scrivere `Media perfetta!` solo se tutti e tre i voti sono $30$.

```c
#include <stdio.h>

int main(void) {
    int v1, v2, v3, somma;
    double media;
    printf("Inserisci tre voti: ");
    scanf("%d %d %d", &v1, &v2, &v3);
    media = (v1 + v2 + v3) / 3.0;
    printf("Media = %d\n", media);
    if (media = 30) {
        printf("Media perfetta!\n");
    }
    return 0;
}
```

1. Compilatelo con `gcc -o media media.c`, poi con `gcc -Wall -Wextra -o media media.c`. Quanti warning compaiono nei due casi? (Il gcc di Ubuntu attiva alcuni avvisi anche senza flag, quindi il primo numero puo' non essere zero; su altri sistemi i numeri possono essere diversi.)
2. Per ogni warning indicate riga e colonna e spiegate con parole vostre che cosa segnala. Eseguite il programma con $24$, $27$, $28$: quali warning corrispondono a un comportamento sbagliato che vedete davvero?
3. Correggete il programma finche' la compilazione con i due flag non produce piu' nessun messaggio.

**E2.** Il programma somma i primi $n$ numeri dispari. Salvatelo nel file `dispari.c`.

```c
#include <stdio.h>

int main(void) {
    int n, k, dispari, somma;
    printf("Quanti numeri dispari? ");
    scanf("%d", &n);
    somma = 0;
    for (k = 1; k <= n; k++) {
        dispari = 2 * k - 1;
        somma += dispari;
    }
    printf("Somma dei primi %d dispari = %d\n", n, somma);
    return 0;
}
```

**Primo contatto con gdb.** Per usare gdb il programma va compilato con un terzo flag, `-g`, che aggiunge all'eseguibile le informazioni che servono al debugger (i nomi delle variabili, i numeri di riga). D'ora in poi compilate sempre con `gcc -g -Wall -Wextra`. Per avviare gdb scrivete `gdb ./dispari`: compare il prompt `(gdb)`, che aspetta i vostri comandi. Per ora ne bastano due.

| Comando | Cosa fa |
| --- | --- |
| `run` | esegue il programma, esattamente come `./dispari` |
| `quit` | esce da gdb |

```text
$ gcc -g -Wall -Wextra -o dispari dispari.c
$ gdb ./dispari
(gdb) run
Starting program: /home/studente/esercizi/dispari
Quanti numeri dispari? 6
Somma dei primi 6 dispari = 36
[Inferior 1 (process 4321) exited normally]
(gdb) quit
```

Su Ubuntu, al primo `run`, gdb puo' chiedere `Enable debuginfod for this session? (y or [n])`: rispondete `n`. Puo' anche stampare qualche riga informativa in piu', come `[Thread debugging using libthread_db enabled]`: potete ignorarla.

1. Eseguite il programma con $n = 1, 2, 3, 4, 5, 6$: che numeri ottenete? Formulate una congettura sulla somma dei primi $n$ numeri dispari, controllatela con $n = 100$ e dimostratela per induzione.
2. **Con gdb.** Ripetete qualche prova dentro gdb, dando di nuovo `run`: il programma si comporta come dal terminale? Che cosa scrive gdb quando il programma termina?

**E3.** Prevedete il valore delle quattro variabili dopo ogni riga e completate la tabella su carta, scrivendo "?" se la variabile non ha ancora un valore.

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 2, c, d;
    c = a++;
    d = ++b;
    a += d;
    b *= c - 1;
    c -= a / 3;
    d = b--;
    d /= 4;
    a %= 4;
    c = --d * 2;
    printf("a = %d, b = %d, c = %d, d = %d\n", a, b, c, d);
    return 0;
}
```

| Dopo la riga | a | b | c | d |
| --- | --- | --- | --- | --- |
| `c = a++;` |  |  |  |  |
| `d = ++b;` |  |  |  |  |
| `a += d;` |  |  |  |  |
| `b *= c - 1;` |  |  |  |  |
| `c -= a / 3;` |  |  |  |  |
| `d = b--;` |  |  |  |  |
| `d /= 4;` |  |  |  |  |
| `a %= 4;` |  |  |  |  |
| `c = --d * 2;` |  |  |  |  |

**Comandi nuovi: `break` e `print`.** `break 10` mette un *breakpoint* (punto di arresto) sulla riga $10$: quando l'esecuzione arriva a quella riga, il programma si ferma e gdb aspetta i vostri comandi. Mentre il programma e' fermo, `print x` mostra il valore della variabile `x`. Ecco un esempio con il programma di E2, dove la riga $10$ e' `somma += dispari;`:

```text
(gdb) break 10
Breakpoint 1 at 0x11ee: file dispari.c, line 10.
(gdb) run
Starting program: /home/studente/esercizi/dispari
Quanti numeri dispari? 6

Breakpoint 1, main () at dispari.c:10
10              somma += dispari;
(gdb) print k
$1 = 1
(gdb) print somma
$2 = 0
```

Attenzione: quando gdb si ferma su una riga, quella riga **non e' ancora stata eseguita**. Per questo, nell'esempio, `somma` vale ancora $0$. Torniamo al programma del codice di **E3**.

1. La riga `b *= c - 1;` equivale a `b = b * c - 1;` oppure a `b = b * (c - 1);`?
2. In quali righe la posizione di `++` o `--`, prima o dopo la variabile, cambia il risultato?
3. **Con gdb.** Mettete un breakpoint sulla riga della `printf` (il numero di riga lo leggete nell'editor), lanciate il programma e stampate `a`, `b`, `c` e `d`: coincidono con l'ultima riga della vostra tabella? Se no, spostate il breakpoint piu' in alto, per esempio sulla riga `d = b--;`, e cercate il punto in cui la tabella e il programma si separano.

#### Scelte e cicli sotto la lente

**E4.** Scrivete un programma che legge le coordinate intere di un punto del piano e stampa `Origine`, `Su un asse`, `Primo quadrante`, `Secondo quadrante`, `Terzo quadrante` oppure `Quarto quadrante`, con una sola catena di `else if` che controlla i casi in quest'ordine.

```text
Coordinate del punto: -3 -2
Terzo quadrante
```

**Comando nuovo: `next`.** Quando il programma e' fermo, `next` esegue la riga corrente e si ferma sulla successiva, mostrandola. Cosi' si segue il programma un passo alla volta e si vede quali righe vengono eseguite e quali saltate.

1. Quando il programma arriva al ramo del terzo quadrante, cosa sa gia' di `x` e `y`? Basta scrivere `else if (x < 0)` invece di `else if (x < 0 && y < 0)`? Perche'?
2. **Con gdb.** Mettete un breakpoint sulla riga del primo `if`, lanciate il programma con il punto $(-3, -2)$ e avanzate con `next`: quante condizioni vengono controllate, compresa quella vera? E con il punto $(0, 5)$?

**E5.** Il programma conta le cifre di un numero, come in D38.

```c
#include <stdio.h>

int main(void) {
    int n, cifre;
    printf("Inserisci un numero non negativo: ");
    scanf("%d", &n);
    cifre = 0;
    while (n > 0) {
        n /= 10;
        cifre++;
    }
    printf("Cifre: %d\n", cifre);
    return 0;
}
```

**Comando nuovo: `continue`.** Riprende l'esecuzione fino al prossimo breakpoint, o fino alla fine del programma. Con un breakpoint dentro un ciclo, il programma si ferma a ogni giro. Un trucco: premendo Invio senza scrivere nulla, gdb ripete l'ultimo comando.

1. Eseguitelo con $90517$ e con $0$. Con $0$ il risultato e' corretto? Perche' il corpo del ciclo non viene mai eseguito?
2. Riscrivete il ciclo con un `do while` e ripetete la prova con $0$. Esiste un numero positivo per cui le due versioni danno risultati diversi?
3. **Con gdb.** Con la nuova versione, mettete un breakpoint sulla riga `n /= 10;` e lanciate con $90517$. A ogni fermata stampate `n` e `cifre`, poi date `continue`, e completate la tabella.

| Fermata | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| `n` |  |  |  |  |  |
| `cifre` |  |  |  |  |  |

**E6.** Il programma calcola la somma dei cubi da $1$ a $n$.

```c
#include <stdio.h>

int main(void) {
    int n, i, cubi;
    printf("Inserisci n: ");
    scanf("%d", &n);
    cubi = 0;
    for (i = 1; i <= n; i++) {
        cubi += i * i * i;
    }
    printf("Somma dei cubi da 1 a %d = %d\n", n, cubi);
    return 0;
}
```

1. Riscrivete il ciclo prima con un `while` e poi con un `do while`, in due programmi `cubi_while.c` e `cubi_do.c`. Trasformate il `for` direttamente: `i = 1;` prima del ciclo, lo stesso corpo seguito da `i++;` e la stessa condizione `i <= n`.
2. Confrontate i risultati con la formula di Nicomaco $\left(\frac{n(n+1)}{2}\right)^2$ per qualche valore di $n$. Poi provate $n = 0$: quale versione da' un risultato diverso dalle altre, e perche'?
3. Il corpo del `for` e' una sola istruzione, quindi le graffe si possono omettere. Toglietele e ricompilate con i tre flag: cambia qualcosa? Perche' conviene metterle lo stesso?
4. **Con gdb.** Per ciascuna delle tre versioni mettete un breakpoint sulla `printf` finale, lanciate con $n = 5$ e stampate `i`. Quanto vale dopo il ciclo? Perche' non vale $5$?

**E7.** Con un interesse annuo del $5\%$, dopo un anno il capitale e' moltiplicato per $1.05$. Il programma calcola in quanti anni il capitale raddoppia.

```c
#include <stdio.h>
#define OBIETTIVO 2.0

int main(void) {
    const double TASSO = 0.05;
    double capitale = 1.0;
    int anni = 0;
    while (capitale < OBIETTIVO) {
        capitale *= 1 + TASSO;
        anni++;
    }
    printf("Con un tasso del %.0f%% il capitale raddoppia in %d anni\n", TASSO * 100, anni);
    return 0;
}
```

**Comando nuovo: il breakpoint con condizione.** `break 10 if capitale > 1.5` ferma il programma alla riga $10$ solo quando la condizione e' vera; la condizione si scrive come in C.

1. Eseguitelo. Nella `printf`, `%%` stampa il simbolo `%`. La "regola del 72" dice che, con un tasso del $t\%$, il capitale raddoppia in circa $72/t$ anni: cambiate `TASSO` e confrontate per $3\%$, $6\%$ e $8\%$, poi rimettete il $5\%$.
2. **Con gdb.** Mettete un breakpoint sulla riga `anni++;` con la condizione `if capitale > 1.5`: quanto valgono `capitale` e `anni` alla prima fermata? In quale anno il capitale supera per la prima volta una volta e mezza quello iniziale? Ricordate che la riga `anni++;` non e' ancora stata eseguita. Gia' che ci siete, provate `print TASSO` e `print OBIETTIVO`: perche' gdb conosce solo il primo? (Rivedete B11.)

**E8.** Il programma chiede quanti numeri verranno inseriti e li legge uno alla volta con un `for`. Questa volta ogni numero va confrontato con il precedente: il programma conta quante volte la sequenza sale e quante scende, e alla fine dice se e' strettamente crescente (sale a ogni passo, cioe' le salite sono $n - 1$), strettamente decrescente (le discese sono $n - 1$) o nessuna delle due, controllando i casi in quest'ordine. Le tre frasi finali sono `La sequenza e' strettamente crescente`, `La sequenza e' strettamente decrescente` e `La sequenza non e' strettamente monotona`. Il primo numero va letto prima del ciclo, direttamente nella variabile `prec`, che ricorda il numero precedente; gli altri si leggono nella variabile `x` e si confrontano con una catena `if (x > prec) ... else if (x < prec)`, cosi' due numeri uguali non contano ne' come salita ne' come discesa. Commentate il programma, con almeno un commento per ogni parte: lettura, confronti, risultato.

```text
Quanti numeri? 7
Numero 1: 3
Numero 2: 5
Numero 3: 5
Numero 4: 8
Numero 5: 2
Numero 6: 9
Numero 7: 1
Salite: 3, discese: 2
La sequenza non e' strettamente monotona
```

1. Cosa stampa il programma con un solo numero ($n = 1$)? Dal punto di vista matematico ha ragione?
2. **Con gdb.** Mettete un breakpoint sulla riga `if (x > prec)`, con la condizione `if x < prec`, e inserite i numeri dell'esempio: quante volte si ferma il programma? Quanto valgono `x` e `prec` a ogni fermata?

**E9.** Il programma conta i punti a coordinate intere $(x, y)$ dentro il cerchio di centro l'origine e raggio $r$, cioe' quelli con $x^2 + y^2 \le r^2$.

```c
#include <stdio.h>

int main(void) {
    int r, x, y, punti;
    printf("Raggio: ");
    scanf("%d", &r);
    punti = 0;
    for (x = -r; x <= r; x++) {
        for (y = -r; y <= r; y++) {
            if (x * x + y * y <= r * r) {
                punti++;
            }
        }
    }
    printf("Punti a coordinate intere nel cerchio: %d\n", punti);
    printf("Rapporto punti / r^2 = %f\n", 1.0 * punti / (r * r));
    return 0;
}
```

1. Quante volte viene controllata la condizione dell'`if` con $r = 10$? Prevedetelo, poi verificatelo aggiungendo al programma un contatore `controlli`.
2. Provate con $r = 100$ e $r = 1000$: a quale numero si avvicina il rapporto? Perche'?
3. **Con gdb.** Mettete un breakpoint sulla riga dell'`if` con la condizione `if x == 0 && y == 0` e lanciate con $r = 10$: quanto vale `punti` quando il ciclo arriva al centro del cerchio? Sapendo che il totale e' $317$, sapreste prevederlo senza gdb? Suggerimento: pensate alla simmetria rispetto all'origine.

**E10.** Il programma stampa i numeri di Fibonacci da $F(2)$ a $F(50)$, ricordando solo gli ultimi due.

```c
#include <stdio.h>

int main(void) {
    int k, prec, corr, succ;
    prec = 0;
    corr = 1;
    for (k = 2; k <= 50; k++) {
        succ = prec + corr;
        prec = corr;
        corr = succ;
        printf("F(%d) = %d\n", k, corr);
    }
    return 0;
}
```

1. Eseguitelo: da quale riga in poi i numeri sono chiaramente sbagliati? Un `int` occupa $4$ byte e il suo valore massimo e' $2^{31} - 1 = 2147483647$ (lo rivedrete nel Pacchetto F): calcolate a mano $F(47) = F(45) + F(46)$ e confrontatelo con questo massimo.
2. Controllare che i numeri non diventino negativi basta a trovare tutti i valori sbagliati? Guardate $F(48)$.
3. **Con gdb.** Invece di cercare a occhio, fate fermare gdb da solo: un breakpoint sulla riga della `printf` con la condizione `if corr < 0`. Quanto vale `k` alla fermata?

### Trova l'errore (E11-E15)

Ogni programma contiene un errore (E14 ne contiene due). Trovatelo, correggetelo e dite se e' **sintattico** o **progettuale**, come nei pacchetti C e D. Questa volta avete due aiutanti: compilate sempre con `gcc -g -Wall -Wextra` e leggete i messaggi; se il compilatore tace, seguite il programma con i comandi di gdb che conoscete.

**E11.** Il programma conta i numeri da $1$ a $1000$ che sono multipli di $7$ ma non di $5$: deve stampare `Multipli di 7 non divisibili per 5: 114`. Compilatelo prima senza flag e poi con `-Wall -Wextra`: cosa cambia?

```c
#include <stdio.h>

int main(void) {
    int n, conta;
    conta = 0;
    for (n = 1; n <= 1000; n++) {
        if (n % 7 == 0 && n % 5 != 0);
            conta++;
    }
    printf("Multipli di 7 non divisibili per 5: %d\n", conta);
    return 0;
}
```

**E12.** Il programma conta le potenze di $2$ (cioe' $1, 2, 4, 8, \dots$) minori o uguali a $n$: con $100$ deve stampare `Potenze di 2 minori o uguali a 100: 7`. Invece, dopo aver inserito il numero, non stampa nulla e non termina.

**Novita': Ctrl+C dentro gdb.** Se un programma eseguito dentro gdb non si ferma piu', premete Ctrl+C: il programma viene sospeso (non chiuso) e potete usare i comandi che conoscete, come se si fosse fermato su un breakpoint.

Lanciatelo in gdb, inserite $100$, aspettate un paio di secondi e premete Ctrl+C: quanto valgono `potenza` e `conta`? Date qualche `next`: le variabili cambiano?

```c
#include <stdio.h>

int main(void) {
    int n, potenza, conta;
    printf("Inserisci un numero positivo: ");
    scanf("%d", &n);
    potenza = 0;
    conta = 0;
    while (potenza <= n) {
        potenza *= 2;
        conta++;
    }
    printf("Potenze di 2 minori o uguali a %d: %d\n", n, conta);
    return 0;
}
```

**E13.** Il programma somma i reciproci dei quadrati, $\frac{1}{1^2} + \frac{1}{2^2} + \dots + \frac{1}{N^2}$. Al crescere di $N$ la somma si avvicina a $\frac{\pi^2}{6} \approx 1.644934$ (e' il problema di Basilea, risolto da Eulero): con $N = 1000$ il programma deve stampare `Somma dei reciproci dei quadrati fino a 1000: 1.643935`. gcc segnala due errori, ma l'errore vero e' uno solo: quale? Il primo messaggio indica una riga che sembra corretta; leggete con attenzione anche il secondo e le righe `note`.

```c
#include <stdio.h>
#define N 1000;

int main(void) {
    int k;
    double somma = 0;
    for (k = 1; k <= N; k++) {
        somma += 1.0 / (k * k);
    }
    printf("Somma dei reciproci dei quadrati fino a %d: %f\n", N, somma);
    printf("Il valore esatto della serie e' pi^2/6 = 1.644934...\n");
    return 0;
}
```

**In piu'.** Dopo la correzione, portate `N` a $100000$. Il risultato dovrebbe migliorare, invece il programma stampa `inf`. Mettete un breakpoint sulla riga della somma con la condizione `if k * k <= 0`: per quale `k` si ferma? Cosa mostra `print k * k`? Correggete scrivendo `1.0 / k / k`.

**E14.** Due errori, uno sintattico e uno progettuale. Il programma chiede quanti numeri leggere (da $1$ a $10$) e ne calcola la media: con i numeri $4$, $6$, $8$ deve stampare `Media = 6.000000`. Corretto l'errore sintattico, per trovare l'altro mettete un breakpoint sulla riga che aggiorna `somma` dentro il ciclo e, a ogni fermata, stampate `somma` e `x` prima di andare avanti con `continue`: come cambia `somma` da un giro all'altro?

```c
#include <stdio.h>

int main(void) {
    int n, i, x, somma;
    do {
        printf("Quanti numeri (da 1 a 10)? ");
        scanf("%d", &n);
    } while (n < 1 || n > 10)
    somma = 0;
    for (i = 1; i <= n; i++) {
        printf("Numero %d: ", i);
        scanf("%d", &x);
        somma =+ x;
    }
    printf("Media = %f\n", 1.0 * somma / n);
    return 0;
}
```

**E15.** Il programma deve stampare i numeri triangolari $T(n) = 1 + 2 + \dots + n$ per $n$ da $1$ a $8$, cioe' $1, 3, 6, 10, \dots$, ma stampa $1, 4, 10, 20, \dots$ Nessun warning: tocca a gdb. Mettete un breakpoint sulla riga `somma += j;` con la condizione `if j == 1`, cosi' gdb si ferma all'inizio di ogni nuovo conto: quanto vale `somma` in quei momenti, e quanto dovrebbe valere? Curiosita': anche i numeri stampati per errore hanno un nome, sono i numeri tetraedrici. Sapreste dire perche'?

```c
#include <stdio.h>

int main(void) {
    int n, j, somma;
    somma = 0;
    for (n = 1; n <= 8; n++) {
        for (j = 1; j <= n; j++) {
            somma += j;
        }
        printf("T(%d) = %d\n", n, somma);
    }
    return 0;
}
```

### Dallo pseudocodice al C (E16-E20)

Come in D41-D45, prima eseguite l'algoritmo a mano con i valori dell'esempio, segnando in una tabella come cambiano le variabili, poi traducetelo. Traducete `ALTRIMENTI SE` con `else if` e `RIPETI ... FINCHE'` con `do while`; gli operatori `NON`, `E` e `O` sono `!`, `&&` e `||`. Usate `++`, `+=` e `/=` dove rendono il codice piu' compatto.

**Comando nuovo: `display`.** `display x` funziona come `print x`, ma ripete la stampa da solo a ogni fermata. Con un breakpoint dentro il ciclo, qualche `display` e una serie di `continue`, gdb scrive la tabella al posto vostro: se non coincide con quella fatta a mano, l'errore e' nella traduzione oppure nei conti.

**E16.** La radice numerica di un numero si ottiene sommandone le cifre, poi sommando le cifre del risultato, e cosi' via finche' resta una sola cifra: $987654321 \to 45 \to 9$. L'algoritmo contiene un ciclo dentro un altro ciclo.

```text
INIZIO
    LEGGI _n
    ASSEGNA a _r il valore _n
    FINCHE' _r > 9
        ASSEGNA a _somma il valore 0
        FINCHE' _r > 0
            ASSEGNA a _somma il valore _somma + il resto di _r diviso 10
            ASSEGNA a _r il valore _r / 10
        FINE
        ASSEGNA a _r il valore _somma
    FINE
    VISUALIZZA _n e _r
FINE
```

```text
Inserisci un numero positivo: 987654321
La radice numerica di 987654321 e' 9
```

1. Confrontate la radice numerica con il resto della divisione per $9$, per qualche numero come $2026$, $99$ e $1234$: che relazione c'e'? E' il principio su cui si basa la "prova del nove".
2. **Con gdb.** Mettete un breakpoint sulla riga che corrisponde a `ASSEGNA a _r il valore _somma` e date `display somma`: quali somme intermedie compaiono per $987654321$?

**E17.** L'algoritmo calcola il numero di Fibonacci $F(n)$ ricordando solo gli ultimi due termini, come in E10.

```text
INIZIO
    LEGGI _n
    ASSEGNA a _a il valore 0
    ASSEGNA a _b il valore 1
    ASSEGNA a _k il valore 1
    FINCHE' _k < _n
        ASSEGNA a _c il valore _a + _b
        ASSEGNA a _a il valore _b
        ASSEGNA a _b il valore _c
        ASSEGNA a _k il valore _k + 1
    FINE
    VISUALIZZA _n e _b
FINE
```

```text
Inserisci n: 10
F(10) = 55
```

**Con gdb.** Mettete un breakpoint sulla prima riga del corpo del ciclo. A ogni fermata `a` e `b` contengono due termini consecutivi, $F(k-1)$ e $F(k)$, quindi $a + b = F(k+1)$. Anche `display` accetta espressioni: usate `display k` e `display a * (a + b) - b * b`, cosi' gdb calcola a ogni fermata $F(k-1) F(k+1) - F(k)^2$. Che valori ottenete? E' l'identita' di Cassini: come si scrive il risultato in funzione di $k$?

**E18.** Sommando i divisori propri di $n$ (tutti tranne $n$ stesso) si classificano i numeri: $n$ e' **perfetto** se la somma e' uguale a $n$, come $6 = 1 + 2 + 3$; **abbondante** se e' maggiore, come $12$, che ha somma $1 + 2 + 3 + 4 + 6 = 16$; **difettivo** se e' minore. Traducete entrambi i FINCHE' con dei `for`.

```text
INIZIO
    LEGGI _limite
    ASSEGNA a _abbondanti il valore 0
    ASSEGNA a _perfetti il valore 0
    ASSEGNA a _difettivi il valore 0
    ASSEGNA a _n il valore 1
    FINCHE' _n <= _limite
        ASSEGNA a _somma il valore 0
        ASSEGNA a _d il valore 1
        FINCHE' _d < _n
            SE il resto di _n diviso _d e' 0 ALLORA
                ASSEGNA a _somma il valore _somma + _d
            FINE
            ASSEGNA a _d il valore _d + 1
        FINE
        SE _somma > _n ALLORA
            ASSEGNA a _abbondanti il valore _abbondanti + 1
        ALTRIMENTI SE _somma = _n ALLORA
            ASSEGNA a _perfetti il valore _perfetti + 1
            VISUALIZZA "Perfetto:" e _n
        ALTRIMENTI
            ASSEGNA a _difettivi il valore _difettivi + 1
        FINE
        ASSEGNA a _n il valore _n + 1
    FINE
    VISUALIZZA _abbondanti, _perfetti e _difettivi
FINE
```

```text
Fino a che numero? 100
Perfetto: 6
Perfetto: 28
Abbondanti: 22, perfetti: 2, difettivi: 76
```

**Con gdb.** I primi numeri abbondanti ($12, 18, 20, 24, \dots$) sono tutti pari. Esiste un numero abbondante dispari? Lanciate il programma con limite $1000$ e un breakpoint sulla riga che incrementa `abbondanti`, con la condizione `if n % 2 == 1`: qual e' il primo? Quanto vale la somma dei suoi divisori propri?

**E19.** Il metodo di Newton permette di calcolare $\frac{1}{a}$ senza fare divisioni: partendo da una stima $s$, la formula $s \cdot (2 - a \cdot s)$ ne produce una migliore. Il metodo funziona se la stima iniziale e' compresa tra $0$ e $\frac{2}{a}$: per questo l'algoritmo accetta solo valori di $a$ tra $1$ e $10$ e parte da $0.1$. Usate variabili `double` e, per stampare $9$ cifre decimali, `%.9f`.

```text
INIZIO
    RIPETI
        LEGGI _a
    FINCHE' _a < 1 O _a > 10
    ASSEGNA a _stima il valore 0.1
    ASSEGNA a _passi il valore 0
    RIPETI
        ASSEGNA a _vecchia il valore _stima
        ASSEGNA a _stima il valore _stima x (2 - _a x _stima)
        ASSEGNA a _passi il valore _passi + 1
        ASSEGNA a _diff il valore _stima - _vecchia
        SE _diff < 0 ALLORA
            ASSEGNA a _diff il valore -_diff
        FINE
    FINCHE' _diff > 0.000000001
    VISUALIZZA _a, _stima e _passi
FINE
```

```text
Inserisci un numero da 1 a 10: 7
1/7.000000 = 0.142857143 (in 5 passi)
```

1. **Con gdb.** Mettete un breakpoint sulla riga che calcola `diff` e a ogni fermata date `print stima`, che mostra tutte le cifre. Confrontate con il valore vero $\frac{1}{7} = 0.142857142857\dots$: quante cifre giuste ci sono dopo ogni passo? Come cresce il numero di cifre giuste da un passo all'altro?
2. **In piu'.** Cosa succede se la stima iniziale e' $0.3$?

**E20.** In C il valore di una condizione e' un numero: $1$ se e' vera, $0$ se e' falsa. Per questo con due cicli si possono costruire le tabelle di verita'. L'algoritmo verifica una delle leggi di De Morgan: $\lnot(a \land b) = \lnot a \lor \lnot b$.

```text
INIZIO
    ASSEGNA a _uguali il valore 0
    ASSEGNA a _a il valore 0
    FINCHE' _a <= 1
        ASSEGNA a _b il valore 0
        FINCHE' _b <= 1
            ASSEGNA a _sinistra il valore NON (_a E _b)
            ASSEGNA a _destra il valore (NON _a) O (NON _b)
            VISUALIZZA _a, _b, _sinistra e _destra
            SE _sinistra = _destra ALLORA
                ASSEGNA a _uguali il valore _uguali + 1
            FINE
            ASSEGNA a _b il valore _b + 1
        FINE
        ASSEGNA a _a il valore _a + 1
    FINE
    VISUALIZZA _uguali
FINE
```

```text
a b  !(a && b)  !a || !b
0 0  1          1
0 1  1          1
1 0  1          1
1 1  0          0
Le due espressioni coincidono in 4 righe su 4
```

1. **Con gdb.** `print` funziona anche senza lanciare il programma: gdb fa da calcolatrice, con le regole del C. Prevedete e poi verificate il risultato di `print 5 && 3`, `print !7`, `print (3 > 2) + (5 > 1)` e `print 3 > 2 > 1`. L'ultimo risultato vi ricorda un errore del Pacchetto D?
2. **In piu'.** Aggiungete una terza variabile `c` (tre cicli, otto righe) e verificate la proprieta' distributiva $a \land (b \lor c) = (a \land b) \lor (a \land c)$.

### Riepilogo dei comandi gdb

| Comando | Cosa fa | Visto in |
| --- | --- | --- |
| `gcc -g -Wall -Wextra` | compila con gli avvisi e con le informazioni per gdb | E1, E2 |
| `gdb ./programma` | avvia gdb sul programma, senza eseguirlo | E2 |
| `run` | esegue il programma | E2 |
| `quit` | esce da gdb | E2 |
| `break 10` | ferma il programma alla riga $10$, prima di eseguirla | E3 |
| `print x` | mostra il valore di `x` o di un'espressione | E3 |
| `next` | esegue una riga e si ferma sulla successiva | E4 |
| `continue` | riprende fino al prossimo breakpoint; Invio ripete l'ultimo comando | E5 |
| `break 10 if condizione` | si ferma alla riga $10$ solo se la condizione e' vera | E7 |
| Ctrl+C | sospende un programma che non si ferma piu' | E12 |
| `display x` | stampa `x` a ogni fermata | E16 |

## Pacchetto F: Tipi di dato, switch e array

Continuate a compilare con `gcc -g -Wall -Wextra`. Con gli array gdb diventa ancora piu' comodo, perche' mostra in un colpo solo il contenuto di un intero vettore: basta una piccola aggiunta a `print`, che vedrete in F3.

### Tipi di dato e conversioni

| Tipo | Byte (di solito) | Valori | Formattatore |
| --- | --- | --- | --- |
| `char` | $1$ | un carattere, cioe' un codice da $0$ a $255$ | `%c` |
| `short` | $2$ | da $-32768$ a $32767$ | `%d` |
| `int` | $4$ | da $-2^{31}$ a $2^{31} - 1$ | `%d` |
| `unsigned int` | $4$ | da $0$ a $2^{32} - 1$ | `%u` |
| `long` | $8$ | da $-2^{63}$ a $2^{63} - 1$ | `%ld` |
| `float` | $4$ | numeri reali, circa $6$ cifre significative | `%f` |
| `double` | $8$ | numeri reali, circa $15$ cifre significative | `%f` (`%lf` in `scanf`) |

I valori massimi e minimi sono definiti nella libreria `limits.h`: per esempio `INT_MAX` e' il piu' grande `int`. Un `char` e' un piccolo intero: il carattere `'A'` e' il numero $65$ del codice ASCII, `'a'` e' $97$, la cifra `'0'` e' $48$, e l'ordine e' quello lessicografico (cifre, poi maiuscole, poi minuscole). Per questo con i caratteri si possono fare i conti: `'a' + 1` e' `'b'`.

Il compilatore sa calcolare solo espressioni omogenee, con operandi dello stesso tipo. Se i tipi sono diversi, converte automaticamente l'operando "piu' piccolo" seguendo l'ordine `char` $\to$ `int` $\to$ `float` $\to$ `double` (conversione implicita). Con un *cast* si forza invece la conversione (conversione esplicita): `(double) somma / n` converte `somma` in `double` prima di dividere, mentre `(int) 3.99` vale $3$.

### Il costrutto switch

Con `switch` si sceglie tra piu' casi in base al valore di un'espressione intera o di un carattere:

```c
switch (scelta) {
    case 'a':
        printf("Hai scelto a\n");
        break;
    case 'b':
    case 'B':
        printf("Hai scelto b\n");
        break;
    default:
        printf("Scelta non valida\n");
}
```

Il `break` chiude il caso: se manca, l'esecuzione prosegue nel caso successivo. A volte e' voluto, come per `'b'` e `'B'` qui sopra, che condividono le stesse istruzioni; quando non e' voluto, `-Wextra` lo segnala con il warning `this statement may fall through`. Il ramo `default` viene eseguito se nessun caso corrisponde.

### Gli array

Un array (o vettore) contiene un numero fissato di valori dello stesso tipo, identificati da un indice che parte da $0$:

```c
#define N 5

int v[N];                          /* v[0], v[1], ..., v[4] */
int primi[N] = {2, 3, 5, 7, 11};   /* dichiarazione con i valori iniziali */
int conta[10] = {0};               /* gli elementi non elencati valgono 0 */

for (i = 0; i < N; i++) {          /* lettura */
    scanf("%d", &v[i]);
}
for (i = 0; i < N; i++) {          /* stampa */
    printf("%d ", v[i]);
}
```

La dimensione si scrive di solito con una `#define`, cosi' per cambiarla basta modificare una riga. Il C non controlla gli indici: scrivere `v[5]` in un array di $5$ elementi non da' errori di compilazione, ma legge o scrive memoria che non appartiene all'array, con risultati imprevedibili o con il crash del programma.

### Gli array nello pseudocodice

Nello pseudocodice `_v[_i]` indica l'elemento di posto `_i` del vettore `_v`, e c'e' una nuova forma di ciclo:

| Pseudocodice | C |
| --- | --- |
| `PER _i DA 0 A _n - 1 ... FINE` | `for (i = 0; i <= n - 1; i++) { ... }`, cioe' `for (i = 0; i < n; i++)` |
| `PER _i DA _n - 1 A 0, ALL'INDIETRO ... FINE` | `for (i = n - 1; i >= 0; i--) { ... }` |

### Esercizi (F1-F10)

#### Tipi di dato

**F1.** Per ogni espressione scrivete su carta il risultato che vi aspettate, poi verificate. Il modo piu' rapido e' la calcolatrice di gdb vista in E20: avviatelo su uno qualsiasi dei vostri eseguibili, per esempio `gdb ./dispari`, e senza dare `run` scrivete `print` seguito dall'espressione. L'eseguibile serve a gdb solo per sapere quanto sono grandi i tipi sul vostro computer: senza, potrebbe usare dimensioni diverse.

1. Dimensioni: `sizeof(char)`, `sizeof(short)`, `sizeof(int)`, `sizeof(long)`, `sizeof(float)`, `sizeof(double)`.
2. Conversioni: `7 / 2`, `7.0 / 2`, `(double) 7 / 2`, `(double) (7 / 2)`, `(int) 3.99`, `(int) -3.99`, `'a' + 1`, `'a' + 1.5`. Di che tipo e' il risultato degli ultimi due?
3. Caratteri (tenete sotto mano la tabella ASCII): `'A'`, `'7' - '0'`, `'a' - 'A'`, `'g' - 32`, `'R' < 'B'`, `'x' - '4'`. A quali caratteri corrispondono i numeri $71$ e $68$?
4. Precedenze: `2 + 3 * 4 % 5`, `10 - 4 - 3 * 2`, `!0 + 1`, `1 + 2 == 3 && 4 > 5 || 1`.
5. Precisione: `1.542342 / 7` e `(float) 1.542342 / 7`. Fino a quale cifra coincidono i due risultati?

Infine: come si trasforma una lettera minuscola nella maiuscola corrispondente? E la cifra `'7'` nel numero $7$?

**F2.** Il programma raddoppia $40$ volte tre variabili di tipo diverso, che partono tutte da $1$.

```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    int k;
    short s = 1;
    unsigned int u = 1;
    long l = 1;
    printf("Massimi: short %d, int %d, unsigned %u, long %ld\n", SHRT_MAX, INT_MAX, UINT_MAX, LONG_MAX);
    for (k = 1; k <= 40; k++) {
        s *= 2;
        u *= 2;
        l *= 2;
        printf("2^%d:  short %d  unsigned %u  long %ld\n", k, s, u, l);
    }
    return 0;
}
```

1. Eseguitelo: quali sono i valori massimi dei tipi? Da quale riga `short` e `unsigned` smettono di dare risultati corretti, e che cosa stampano? Perche' `unsigned` diventa $0$ proprio a quel passo?
2. **Con gdb.** Fatevi fermare dove `short` sbaglia per la prima volta: un breakpoint sulla riga della `printf` con la condizione `if s < 0`. Quanto vale `k`? E che valore assume `s` nel giro successivo?

#### Primi array

**F3.** Il programma calcola i salti tra numeri primi consecutivi.

```c
#include <stdio.h>
#define N 10

int main(void) {
    int primi[N] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int salti[N - 1];
    int i;
    for (i = 0; i < N - 1; i++) {
        salti[i] = primi[i + 1] - primi[i];
    }
    printf("Salti tra primi consecutivi: ");
    for (i = 0; i < N - 1; i++) {
        printf("%d ", salti[i]);
    }
    printf("\n");
    return 0;
}
```

**Comando nuovo: `print` con gli array.** `print primi` mostra tutto l'array, `print primi[4]` un solo elemento e `print primi[2]@4` quattro elementi a partire da `primi[2]`.

1. Aggiungete $31$ tra le graffe senza cambiare `N`: cosa dice gcc? E se tra le graffe lasciate solo i primi $8$ numeri, che valore hanno gli ultimi due elementi?
2. Che cosa succederebbe se il primo ciclo arrivasse fino a `i < N` invece che a `i < N - 1`?
3. **Con gdb.** Mettete un breakpoint sul primo `for` e provate `print primi`, `print primi[2]@4` e `print salti`: cosa contiene `salti` prima del ciclo? Provate anche `print primi[10]`: gdb protesta? Che cosa vi dice questo sul C?

**F4.** Il programma legge $n$ numeri in un array `v` (con $n$ da $1$ a $20$, controllato con un `do while`) e poi li inverte *nello stesso array*, senza usarne un secondo: scambia il primo con l'ultimo, il secondo con il penultimo, e cosi' via (per lo scambio rivedete C13). Usate due indici, `i` che parte da $0$ e `j` che parte da $n - 1$, e scambiate finche' `i < j`, avvicinandoli a ogni passo con `i++` e `j--`.

```text
Quanti numeri (da 1 a 20)? 7
v[0] = 1
v[1] = 2
v[2] = 3
v[3] = 4
v[4] = 5
v[5] = 6
v[6] = 7
Al contrario: 7 6 5 4 3 2 1
```

1. Quante volte avviene lo scambio con $n = 7$? E con $n = 8$? E in generale?
2. Cosa succede se la condizione del ciclo diventa `i < n`? Prevedetelo, poi provate.
3. **Con gdb.** Mettete un breakpoint sulla prima riga dello scambio e usate `display v[0]@n`: come cambia l'array a ogni fermata?

**F5.** In $\mathbb{R}^n$ il prodotto scalare di $u$ e $v$ e' $u \cdot v = u_1 v_1 + \dots + u_n v_n$, e $|u|^2 = u \cdot u$; due vettori sono ortogonali se il loro prodotto scalare e' $0$. Il programma legge la dimensione $n$ (al massimo `DIM_MAX`, che vale $10$) e le componenti intere di due vettori, e stampa prodotto scalare, norme al quadrato e se i vettori sono ortogonali. Chiamate le variabili `u`, `v`, `scalare`, `norma_u` e `norma_v`.

```text
Dimensione (da 1 a 10): 3
Componenti di u: 1 2 3
Componenti di v: 4 -5 2
u . v = 0
|u|^2 = 14, |v|^2 = 45
I vettori sono ortogonali
```

1. Con due vettori non ortogonali scelti da voi, verificate la disuguaglianza di Cauchy-Schwarz $(u \cdot v)^2 \le |u|^2 |v|^2$. Quando vale l'uguaglianza?
2. **Con gdb.** Fermatevi dopo la lettura e date `print u`: perche' gdb stampa $10$ numeri, e che cosa sono gli ultimi? Mostrate solo la parte utile con `print u[0]@n`.

**F6.** Un numero e' pandigitale se contiene tutte e dieci le cifre almeno una volta, come $9876543210$. Il programma legge un intero positivo di tipo `long` (con `%ld` in `scanf` e in `printf`) e conta quante volte compare ogni cifra nell'array `int cont[10] = {0};`: l'ultima cifra `n % 10` fa aumentare `cont[n % 10]`, poi `n /= 10` la toglie. Contate le cifre con un `do while`, come in E5, e con un secondo `do while` richiedete il numero finche' non e' positivo.

```text
Inserisci un intero positivo: 1099511627776
Cifra:  0 1 2 3 4 5 6 7 8 9
Volte:  1 3 1 0 0 1 2 3 0 2
Cifre mancanti: 3 4 8
Il numero non e' pandigitale
```

1. Cambiate la `scanf` in `scanf("%d", &n)`: cosa dice `-Wall`?
2. Perche' bisogna accettare solo numeri positivi? Ricordate che il resto della divisione di un numero negativo e' negativo: quale elemento di `cont` verrebbe aumentato?
3. **Con gdb.** Dichiarate `n` come `int` (con `%d`) e inserite $9876543210$: con un breakpoint subito dopo la lettura, che valore contiene `n`? Perche'?

#### switch e caratteri

**F7.** Su un vettore si possono definire diverse norme: la **norma 1** e' la somma dei valori assoluti delle componenti; la **norma euclidea** e' la radice quadrata della somma dei quadrati (qui ne calcoliamo il quadrato, per restare tra gli interi); la **norma del massimo** e' il piu' grande dei valori assoluti. Il programma lavora sul vettore fissato `int v[6] = {3, -1, 4, -1, 5, -9};`, legge una sola scelta con `scanf(" %c", &scelta)` e con uno `switch` calcola e stampa la norma scelta. Scrivete i casi in quest'ordine: `'1'`, `'2'`, poi `'m'` e `'M'`, due casi con le stesse istruzioni, e infine il `default`, che stampa `Scelta non valida`. Ogni caso calcola e stampa la sua norma, poi termina con `break`.

```text
Norma (1 = somma, 2 = quadrato della euclidea, m = massimo): 1
Norma 1 = 23

Norma (1 = somma, 2 = quadrato della euclidea, m = massimo): 2
Norma euclidea al quadrato = 133

Norma (1 = somma, 2 = quadrato della euclidea, m = massimo): M
Norma del massimo = 9

Norma (1 = somma, 2 = quadrato della euclidea, m = massimo): x
Scelta non valida
```

**Comando nuovo: i formati di `print`.** Dopo `print` si puo' indicare come mostrare il valore: `print/d x` lo mostra come numero, `print/c x` come carattere.

1. Togliete il `break` alla fine del caso `'1'` e ricompilate con i tre flag: cosa dice gcc? Cosa stampa ora il programma scegliendo `1`?
2. Dichiarate `scelta` come `double`, letta con `%lf`: cosa dice gcc dello `switch`?
3. **Con gdb.** Fermatevi sulla riga dello `switch` dopo aver scelto `2`: cosa stampano `print scelta`, `print/d scelta` e `print scelta == '2'`? Che differenza c'e' tra `2` e `'2'`?

**F8.** Il cifrario di Cesare sposta ogni lettera di $k$ posti nell'alfabeto, ricominciando da `a` dopo la `z`: con $k = 3$, `a` diventa `d` e `z` diventa `c`. Con i caratteri si fanno i conti: `c - 'a'` e' la posizione della lettera `c` nell'alfabeto (da $0$ a $25$), quindi la lettera cifrata e' `'a' + (c - 'a' + k) % 26`. Il programma legge una parola di `L` lettere minuscole (con `#define L 6`) in un array di `char`, un carattere alla volta con `scanf(" %c", &parola[i])`, poi legge $k$ e stampa la parola cifrata con `%c`.

```text
Parola di 6 lettere minuscole: codice
Spostamento: 3
Messaggio cifrato: frglfh
```

1. Provate con una parola che contiene una `z`, come `zigzag`: a che cosa serve il `% 26`?
2. Decifrate `frglfh` con lo stesso programma: quale spostamento serve? Perche' conviene usare $26 - k$ invece di $-k$?
3. Cosa succede se la parola contiene un carattere che non e' una lettera minuscola, come in `zebra!`?
4. **Con gdb.** Con un breakpoint sul ciclo di cifratura, date `print parola` e `print/d parola`: che cosa mostrano?

#### Ricerche e trasformazioni

**F9.** Scrivete un programma che contiene le prime $30$ cifre di $\pi$ in un array (con `#define N 30`),

```c
int pi[N] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9,
             3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7};
```

legge una cifra nella variabile `cifra` e stampa quante volte compare e la posizione (l'indice) della prima volta. Usate una variabile `prima` che parte da $-1$, il valore che significa "non ancora trovata", e la aggiornate solo la prima volta che trovate la cifra; il contatore si chiama `volte`.

```text
Cifra da cercare: 7
La cifra 7 compare 2 volte; la prima volta in posizione 13

Cifra da cercare: 0
La cifra 0 non compare tra le prime 30 cifre di pi
```

1. Perche' $-1$ e' una buona scelta per dire "non trovata"? Andrebbe bene $0$?
2. **Con gdb.** Mettete un breakpoint sulla riga del confronto con la condizione `if pi[i] == cifra`, cosi' gdb si ferma solo quando trova la cifra: per la cifra $7$, a quali valori di `i` si ferma?

**F10.** **Sfida.** Il triangolo di Tartaglia. Numeriamo le righe da $0$: la riga $n$ contiene gli $n + 1$ coefficienti $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$, e ogni riga si ottiene dalla precedente con la regola $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$. Basta un solo array `riga` di $30$ elementi: si parte dalla riga $0$, cioe' `{1, 0, 0, ...}`, e per passare dalla riga $n - 1$ alla riga $n$ si esegue `riga[k] += riga[k - 1]` per `k` che va da `n` fino a $1$, all'indietro. Usate proprio `n` per il numero della riga e `k` per la posizione. Il programma legge quante righe stampare (da $1$ a $30$, con un `do while`) e le stampa a partire dalla riga $0$.

```text
Quante righe (da 1 a 30)? 8
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
```

1. Cosa succede se l'aggiornamento va in avanti, con `k` da $1$ a `n`? Partendo dalla riga $1$, cioe' `{1, 1, 0}`, prevedete la riga $2$, poi provate. Curiosita': gli ultimi numeri delle righe sbagliate ($1, 2, 5, 14, 42, \dots$) sono i numeri di Catalan.
2. Nella riga $7$ (l'ottava stampata, `1 7 21 35 35 21 7 1`) tutti i numeri tranne gli $1$ agli estremi sono multipli di $7$. Succede in ogni riga $p$ con $p$ primo? Controllate sulle righe stampate. E con una riga non prima, come la $6$?
3. **Con gdb.** Mettete un breakpoint sul ciclo che stampa la riga e usate `display riga[0]@(n+1)`: a ogni fermata vedete la riga $n$ appena calcolata.

### Trova l'errore (F11-F15)

Ogni programma contiene un errore (F14 ne contiene due). Come nel Pacchetto E: correggetelo e dite se e' sintattico o progettuale. Con gli array molti errori non producono nessun messaggio e il risultato puo' cambiare da un'esecuzione all'altra: in questi casi gdb aiuta molto.

**F11.** Il programma somma i primi $6$ termini della progressione geometrica di ragione $3$: deve stampare `Somma dei primi 6 termini = 364`, perche' la somma vale $\frac{3^6 - 1}{2} = 364$. Eseguitelo due o tre volte: cosa notate? In gdb, con un breakpoint condizionato sulla riga della somma (`if i == 6`), stampate `termini[i]` e `somma`.

```c
#include <stdio.h>

int main(void) {
    int termini[6] = {1, 3, 9, 27, 81, 243};
    int i, somma = 0;
    for (i = 1; i <= 6; i++) {
        somma += termini[i];
    }
    printf("Somma dei primi 6 termini = %d\n", somma);
    return 0;
}
```

**F12.** Il programma deve stampare i coefficienti del polinomio $2x^3 - 6x^2 + 2x - 1$ dal grado piu' alto al piu' basso, cioe' `Coefficienti dal grado 3 al grado 0: 2 -6 2 -1`. Invece va in crash, e a volte senza stampare nemmeno un coefficiente (quello che non e' ancora stato mandato a capo si perde nel crash).

**Novita': il crash dentro gdb.** Se il programma va in crash mentre gira dentro gdb, gdb si ferma sulla riga dell'errore con un messaggio come `Program received signal SIGSEGV, Segmentation fault.` (quando l'indirizzo sbagliato e' molto lontano, come in questo esercizio, puo' comparire invece `SIGBUS, Bus error.`), e potete guardare le variabili come a un breakpoint.

Leggete il warning di `-Wextra`, poi lanciate il programma in gdb con `run`: su quale riga si ferma? Quanto vale `i`, e che relazione c'e' con $2^{32}$? Perche' proprio quel valore?

```c
#include <stdio.h>

int main(void) {
    int coeff[4] = {-1, 2, -6, 2};
    unsigned int i;
    printf("Coefficienti dal grado 3 al grado 0:");
    for (i = 3; i >= 0; i--) {
        printf(" %d", coeff[i]);
    }
    printf("\n");
    return 0;
}
```

**F13.** Il programma conta vocali e consonanti della parola `matematica`: deve stampare `Vocali: 5, consonanti: 5`. Leggete il warning, poi in gdb fermatevi sullo `switch` quando `i` vale $1$ (`break NUMERO_RIGA if i == 1`) e seguite il percorso con `next`. Perche' i casi `'a'`, `'e'`, `'i'` e `'o'`, che non contengono istruzioni, non producono warning?

```c
#include <stdio.h>
#define L 10

int main(void) {
    char parola[L] = {'m', 'a', 't', 'e', 'm', 'a', 't', 'i', 'c', 'a'};
    int i, vocali = 0, consonanti = 0;
    for (i = 0; i < L; i++) {
        switch (parola[i]) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                vocali++;
            default:
                consonanti++;
        }
    }
    printf("Vocali: %d, consonanti: %d\n", vocali, consonanti);
    return 0;
}
```

**F14.** Due errori, uno sintattico e uno progettuale. Il programma legge un vettore `v` e dice se e' uguale al vettore $u = (1, 2, 3)$: inserendo `1 2 3` deve stampare `v e' uguale a u`. Corretto l'errore sintattico, leggete il warning (compare da gcc 12 in poi) e controllate con gdb `print u`, `print v` e `print u == v`. Il confronto `u == v` non confronta gli elementi, ma la posizione dei due array nella memoria: correggetelo con un ciclo e una variabile che parte da $1$ e diventa $0$ alla prima differenza.

```c
#include <stdio.h>
#define N 3

int main(void) {
    int u[N], v[N];
    int i;
    u = {1, 2, 3};
    printf("Componenti di v: ");
    for (i = 0; i < N; i++) {
        scanf("%d", &v[i]);
    }
    if (u == v) {
        printf("v e' uguale a u\n");
    } else {
        printf("v e' diverso da u\n");
    }
    return 0;
}
```

**F15.** Il programma calcola i valori di $f(x) = -(x - 3)^2 - 1$ per $x = 0, 1, \dots, 6$ e ne cerca il massimo: deve stampare `Il massimo di f e' -1, in x = 3`. Nessun warning. Con gdb stampate l'array `valori` e seguite `massimo` con `display` durante il secondo ciclo. Con quale valore conviene inizializzare `massimo` perche' il programma funzioni con qualsiasi funzione?

```c
#include <stdio.h>
#define N 7

int main(void) {
    int valori[N];
    int x, massimo, x_max;
    for (x = 0; x < N; x++) {
        valori[x] = -(x - 3) * (x - 3) - 1;
    }
    massimo = 0;
    x_max = 0;
    for (x = 0; x < N; x++) {
        if (valori[x] > massimo) {
            massimo = valori[x];
            x_max = x;
        }
    }
    printf("Il massimo di f e' %d, in x = %d\n", massimo, x_max);
    return 0;
}
```

### Dallo pseudocodice al C (F16-F20)

Traducete come in E16-E20, con le dimensioni degli array in una `#define`, e usate gdb per confrontare le vostre tabelle con l'esecuzione vera. `scambia _x e _y` significa scambiare i valori delle due variabili, con una variabile d'appoggio come in C13.

**F16.** Il crivello di Eratostene trova tutti i numeri primi fino a $100$: si parte supponendo che tutti i numeri siano primi, poi per ogni primo $i$ si cancellano i suoi multipli, a partire da $i^2$. L'array `primo` ha $101$ elementi, da `primo[0]` a `primo[100]`: `primo[k]` vale $1$ se $k$ e' (ancora) considerato primo, $0$ se e' stato cancellato.

```text
INIZIO
    PER _i DA 0 A 100
        ASSEGNA a _primo[_i] il valore 1
    FINE
    ASSEGNA a _primo[0] il valore 0
    ASSEGNA a _primo[1] il valore 0
    PER _i DA 2 A 10
        SE _primo[_i] = 1 ALLORA
            ASSEGNA a _j il valore _i x _i
            FINCHE' _j <= 100
                ASSEGNA a _primo[_j] il valore 0
                ASSEGNA a _j il valore _j + _i
            FINE
        FINE
    FINE
    ASSEGNA a _conta il valore 0
    PER _i DA 0 A 100
        SE _primo[_i] = 1 ALLORA
            VISUALIZZA _i
            ASSEGNA a _conta il valore _conta + 1
        FINE
    FINE
    VISUALIZZA _conta
FINE
```

```text
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
Primi fino a 100: 25
```

1. Perche' basta che `_i` arrivi fino a $10$? E perche' la cancellazione dei multipli di `_i` puo' partire da $i^2$?
2. **Con gdb.** Mettete un breakpoint sulla riga che cancella i multipli (`primo[j] = 0` nella vostra traduzione) con la condizione `if j == 91`: quanto vale `i` quando $91$ viene cancellato? E' il piu' piccolo fattore primo di $91$? Ripetete con `if j == 60`: quante volte viene cancellato $60$, e da quali primi?

**F17.** Per calcolare $p(x) = a_n x^n + \dots + a_1 x + a_0$ conviene riscriverlo come $(\dots((a_n x + a_{n-1}) x + a_{n-2}) x + \dots) x + a_0$: e' lo schema di Horner, che usa solo $n$ moltiplicazioni. I coefficienti vanno in un array, con `a[i]` coefficiente di $x^i$; controllate con un `do while` che il grado sia tra $0$ e `GRADO_MAX` (che vale $10$).

```text
INIZIO
    LEGGI _grado
    PER _i DA 0 A _grado
        LEGGI _a[_i]
    FINE
    LEGGI _x
    ASSEGNA a _r il valore _a[_grado]
    PER _i DA _grado - 1 A 0, ALL'INDIETRO
        ASSEGNA a _r il valore _r x _x + _a[_i]
    FINE
    VISUALIZZA _x e _r
FINE
```

```text
Grado del polinomio (da 0 a 10): 3
Coefficiente di x^0: -1
Coefficiente di x^1: 2
Coefficiente di x^2: -6
Coefficiente di x^3: 2
Valore di x: 3
p(3) = 5
```

1. **Con gdb.** Mettete un breakpoint sulla riga dentro il ciclo e usate `display r`: quali valori ha `r` alle fermate?
2. Dividete $p(x)$ per $x - 3$ con la regola di Ruffini e confrontate i coefficienti del quoziente e il resto con i valori di `r` alle fermate e con il risultato finale: che cosa notate?
3. Il ciclo all'indietro usa la condizione `i >= 0`: perche' qui `i` deve essere un `int` e non un `unsigned`? Rivedete F12.

**F18.** L'ordinamento a bolle (*bubble sort*) confronta gli elementi vicini e li scambia se sono nell'ordine sbagliato: a ogni passata il piu' grande tra quelli non ancora sistemati "sale" fino al suo posto, come una bolla. Controllate con un `do while` che $n$ sia tra $2$ e `MAX`, che vale $20$.

```text
INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    ASSEGNA a _scambi il valore 0
    PER _passata DA 1 A _n - 1
        PER _i DA 0 A _n - 1 - _passata
            SE _v[_i] > _v[_i + 1] ALLORA
                scambia _v[_i] e _v[_i + 1]
                ASSEGNA a _scambi il valore _scambi + 1
            FINE
        FINE
    FINE
    VISUALIZZA _v e _scambi
FINE
```

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Ordinati: 0 1 2 4 5 8
Scambi: 9
```

1. Perche' nella passata numero `_passata` basta arrivare fino a $n - 1 - passata$?
2. Una *inversione* e' una coppia di posizioni $i < j$ con $v_i > v_j$. Contate a mano le inversioni di $(5, 1, 4, 2, 8, 0)$ e confrontatele con il numero di scambi. Di quanto cambia il numero di inversioni a ogni scambio di due elementi vicini?
3. Quanti scambi servono per $(1, 2, 3, 4, 5)$? E per $(5, 4, 3, 2, 1)$?
4. **Con gdb.** Mettete un breakpoint sulla riga dell'`if` con la condizione `if i == 0`, cosi' gdb si ferma all'inizio di ogni passata, e guardate l'array con `display v[0]@n`: dove si trova il massimo dopo la prima passata? E il secondo piu' grande dopo la seconda?

**F19.** Il programma scrive un numero in una base da $2$ a $16$, usando le cifre da `0` a `9` e poi le lettere da `A` a `F`. Rispetto a D44 le cifre vengono salvate in un array e stampate dall'ultima alla prima, quindi non ci sono piu' problemi di grandezza: provate anche con $1024$ in base $2$. L'array `cifre` ha `MAX_CIFRE` elementi, con `MAX_CIFRE` uguale a $32$.

```text
INIZIO
    LEGGI _n e _b
    ASSEGNA a _originale il valore _n
    ASSEGNA a _quante il valore 0
    RIPETI
        ASSEGNA a _cifre[_quante] il valore del resto di _n diviso _b
        ASSEGNA a _n il valore _n / _b
        ASSEGNA a _quante il valore _quante + 1
    FINCHE' _n > 0
    PER _i DA _quante - 1 A 0, ALL'INDIETRO
        SE _cifre[_i] < 10 ALLORA
            VISUALIZZA il carattere '0' + _cifre[_i]
        ALTRIMENTI
            VISUALIZZA il carattere 'A' + _cifre[_i] - 10
        FINE
    FINE
FINE
```

```text
Numero (non negativo) e base (da 2 a 16): 2024 16
2024 in base 16: 7E8
```

1. Perche' `'0' + cifre[i]` e' il carattere della cifra? Quale carattere si ottiene da `'A' + 14 - 10`?
2. Perche' `MAX_CIFRE` vale $32$? Per la base $16$ basterebbero meno elementi?
3. **Con gdb.** Fermatevi prima della stampa e date `print cifre[0]@quante`: in che ordine sono le cifre? Curiosita': gdb sa gia' scrivere un numero in base $16$ e in base $2$, con `print/x originale` e `print/t originale`.

**F20.** La ricerca binaria (o dicotomica) trova un valore in un array ordinato dimezzando a ogni passo la zona in cui puo' trovarsi, come quando si cerca una parola nel dizionario. L'array `primi` contiene i $25$ primi minori di $100$ trovati in F16, in ordine; `_N` vale $25$ e la divisione per $2$ e' quella tra interi.

```text
INIZIO
    LEGGI _x
    ASSEGNA a _sinistra il valore 0
    ASSEGNA a _destra il valore _N - 1
    ASSEGNA a _posizione il valore -1
    ASSEGNA a _passi il valore 0
    FINCHE' _sinistra <= _destra E _posizione = -1
        ASSEGNA a _medio il valore (_sinistra + _destra) / 2
        ASSEGNA a _passi il valore _passi + 1
        SE _primi[_medio] = _x ALLORA
            ASSEGNA a _posizione il valore _medio
        ALTRIMENTI SE _primi[_medio] < _x ALLORA
            ASSEGNA a _sinistra il valore _medio + 1
        ALTRIMENTI
            ASSEGNA a _destra il valore _medio - 1
        FINE
    FINE
    SE _posizione = -1 ALLORA
        VISUALIZZA _x "non e' tra i primi minori di 100" e _passi
    ALTRIMENTI
        VISUALIZZA _x, _posizione e _passi
    FINE
FINE
```

```text
Numero da cercare: 61
61 e' in posizione 17 (5 passi)

Numero da cercare: 60
60 non e' tra i primi minori di 100 (5 passi)
```

1. Completate a mano la tabella per $x = 61$.

| Passo | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| `sinistra` |  |  |  |  |  |
| `destra` |  |  |  |  |  |
| `medio` |  |  |  |  |  |
| `primi[medio]` |  |  |  |  |  |

2. **Con gdb.** Controllate la tabella con un breakpoint sulla riga del primo confronto e `display` su `sinistra`, `destra`, `medio` e `primi[medio]`.
3. Quanti passi servono al massimo con $25$ elementi? Provate qualche valore. E quanti ne servirebbero con $1000$ elementi? E con la ricerca lineare di F9?
4. Con $x = 60$ il ciclo termina perche' `sinistra` supera `destra`: quanto valgono alla fine?

### Riepilogo dei nuovi comandi gdb

| Comando | Cosa fa | Visto in |
| --- | --- | --- |
| `print v`, `print v[1]@3` | mostrano un array intero o una sua parte | F3 |
| `print/d x`, `print/c x` | mostrano un valore come numero o come carattere | F7 |
| (crash) | se il programma va in crash, gdb si ferma sulla riga dell'errore | F12 |


## Pacchetto G: Array, ordinamento e tempi di esecuzione

Negli ultimi pacchetti gli array sono diventati i protagonisti: li avete fatti scorrere, cercare, ordinare. In questo pacchetto li usiamo anche con decine di migliaia di elementi, e ci facciamo una domanda nuova: **quanto tempo impiega il programma?** Due programmi che stampano lo stesso risultato possono impiegare uno un millesimo di secondo e l'altro dieci secondi. Per accorgersene basta un comando del terminale, `time`. Come gdb nei Pacchetti E ed F, `time` non e' il centro degli esercizi: e' un aiutante, che permette di guardare i programmi da un altro punto di vista, quello della velocita'. Le domande che lo usano iniziano con **Con time.** Continuate a compilare con `gcc -g -Wall -Wextra`; gdb resta a disposizione, e qualche domanda lo usa ancora.

### Il comando time

Scritto prima di un comando, `time` lo esegue normalmente e alla fine dice quanto tempo e' passato:

```text
$ time ./bolle
Numeri ordinati: 20000
Confronti: 199990000
Scambi: 100491769
Ordinamento corretto

real    0m0.712s
user    0m0.689s
sys     0m0.004s
```

- `real` e' il tempo trascorso dall'avvio alla fine, come lo misurerebbe un cronometro. Comprende anche le attese: il tempo in cui il programma aspetta che scriviate un numero, e quello in cui il processore lavora per altri programmi: il sistema operativo divide il processore tra tutti i programmi in esecuzione, un pezzetto per volta.
- `user` e' il tempo in cui il processore ha eseguito davvero le istruzioni del vostro programma. E' il numero che useremo per confrontare i programmi.
- `sys` e' il tempo in cui il sistema operativo ha lavorato per conto del programma, per esempio per stampare sullo schermo. Nei nostri esercizi sara' quasi sempre vicino a zero.

Tre regole per misurare bene:

- ripetete ogni misura tre volte e tenete il tempo `user` piu' piccolo: le misure cambiano un po' da un'esecuzione all'altra, perche' nel frattempo il computer fa anche altro;
- differenze di pochi millesimi di secondo non significano nulla;
- i vostri tempi saranno diversi da quelli dei compagni e da quelli scritti qui, perche' dipendono dal computer: quello che conta e' il confronto tra due programmi sullo stesso computer.

### Numeri casuali con un seme fisso

Per provare un ordinamento su $40000$ numeri non li scriveremo a mano: li faremo generare a `rand`. Ricordate: `rand()` (dalla libreria `stdlib.h`) restituisce un intero tra $0$ e `RAND_MAX`, quindi `rand() % 300` e' un numero da $0$ a $299$ e `1 + rand() % 300` un numero da $1$ a $300$. La sequenza dei numeri dipende dal *seme*, che si sceglie con `srand`: con lo stesso seme si ottengono sempre gli stessi numeri. `srand(time(NULL))` cambia il seme a ogni esecuzione; in questo pacchetto useremo quasi sempre un seme fisso, `srand(1)`, perche' per confrontare due programmi serve farli lavorare sugli stessi dati. Su Linux (e su WSL) la sequenza che parte da un certo seme e' la stessa su tutti i computer: per questo potrete controllare i vostri risultati con quelli scritti nel testo.

### Esercizi (G1-G10)

#### Primi passi con time

**G1.** Le temperature di una giornata sono state misurate ogni ora, dalle $0$ alle $23$. Scrivete un programma che le legge in un array `double temp[ORE]` (con `#define ORE 24`), poi stampa la temperatura massima e la minima, ciascuna con l'ora in cui e' stata misurata, e la media con due decimali. Se la massima, o la minima, compare piu' volte, stampate la prima ora in cui compare.

```text
Temperatura alle ore 0: 9.5
Temperatura alle ore 1: 9.0
...
Temperatura alle ore 23: 10.0

Massima: 19.5 alle ore 14
Minima: 7.5 alle ore 5
Media: 12.92
```

**Novita': leggere i dati da un file.** Scrivere $24$ numeri a ogni prova e' noioso. Salvate i numeri in un file di testo, per esempio `temperature.txt`, separati da spazi o da a capo:

```text
9.5 9.0 8.5 8.0 8.0 7.5 8.0 9.5 11.0 13.0 15.0 16.5
18.0 19.0 19.5 19.5 19.0 17.5 15.5 14.0 12.5 11.5 10.5 10.0
```

Poi lanciate il programma con `./temperature < temperature.txt`: il simbolo `<` fa leggere a `scanf` il contenuto del file, come se lo scriveste da tastiera. Le domande del programma compaiono lo stesso, ma tutte di seguito sulla stessa riga, perche' nessuno preme Invio.

1. L'*operatore condizionale* `c ? x : y` vale `x` se la condizione `c` e' vera e `y` altrimenti, e si puo' scrivere dovunque serva un valore: la riga `massima = temp[ora] > massima ? temp[ora] : massima;` aggiorna cosi' la massima senza scrivere un `if`. Basta questa riga anche per sapere a che ora e' stata misurata la massima? Perche'?
2. Con questi dati la massima, $19.5$, compare due volte, alle ore $14$ e $15$. Quale confronto nell'`if` fa stampare l'ora $14$, e quale farebbe stampare l'ora $15$?
3. **Con time.** Lanciate `time ./temperature` e scrivete le temperature a mano (bastano numeri qualsiasi), poi lanciate `time ./temperature < temperature.txt`. Confrontate `real` e `user` nei due casi: perche' nel primo caso `real` e' tanto piu' grande, mentre `user` resta quasi zero in entrambi?

**G2.** Il programma genera `N` numeri casuali da $1$ a `MAX_VAL` e conta quante volte esce ciascun valore, con un array di contatori come in F6.

```c
#include <stdio.h>
#include <stdlib.h>
#define N 3000
#define MAX_VAL 300

int main(void) {
    int v[N];
    int quante[MAX_VAL + 1] = {0};
    int i, x, piu, meno, mai;
    srand(1);
    for (i = 0; i < N; i++) {
        v[i] = 1 + rand() % MAX_VAL;
    }
    printf("Primi 10 valori:");
    for (i = 0; i < 10; i++) {
        printf(" %d", v[i]);
    }
    printf("\n");
    for (i = 0; i < N; i++) {
        quante[v[i]]++;
    }
    piu = 1;
    meno = 1;
    mai = 0;
    for (x = 1; x <= MAX_VAL; x++) {
        if (quante[x] > quante[piu]) {
            piu = x;
        }
        if (quante[x] < quante[meno]) {
            meno = x;
        }
        if (quante[x] == 0) {
            mai++;
        }
    }
    printf("Valore piu' frequente: %d (uscite: %d)\n", piu, quante[piu]);
    printf("Valore meno frequente: %d (uscite: %d)\n", meno, quante[meno]);
    printf("Valori mai usciti: %d\n", mai);
    return 0;
}
```

```text
Primi 10 valori: 284 287 178 116 294 236 287 193 250 122
Valore piu' frequente: 229 (uscite: 21)
Valore meno frequente: 192 (uscite: 1)
Valori mai usciti: 0
```

1. Eseguite il programma due volte: i numeri cambiano? Sostituite `srand(1)` con `srand(2)`: che cosa cambia? Poi provate `srand(time(NULL))` (serve `#include <time.h>`): `time(NULL)` restituisce il numero di secondi passati dal 1 gennaio 1970. (La funzione `time` del C non ha niente a che fare con il comando `time` del terminale: hanno solo lo stesso nome.) Salvate il programma come `casuali.c` e lanciatelo due volte a qualche secondo di distanza, poi due volte di fila con il comando `./casuali; ./casuali` (il `;` esegue i due comandi uno dopo l'altro). Che cosa notate nel secondo caso, e perche'? Alla fine rimettete `srand(1)`.
2. Quali valori puo' produrre `rand() % MAX_VAL`? Perche' l'array `quante` ha `MAX_VAL + 1` elementi, e quale elemento non viene mai usato?
3. In media, quante volte vi aspettate che esca ciascun valore? Portate `N` a $300000$: in proporzione alla media, le differenze tra il valore piu' frequente e il meno frequente diventano piu' grandi o piu' piccole?
4. Negli esperimenti di questo pacchetto useremo sempre `srand(1)`. Perche' e' utile, quando si confrontano i tempi di due programmi, che i numeri generati siano sempre gli stessi?

**G3.** Il programma simula `LANCI` lanci di due dadi (con `#define LANCI 30`) e salva in un array `int somma[LANCI]` la somma dei due dadi di ogni lancio, calcolata con `(1 + rand() % 6) + (1 + rand() % 6)`. Il seme si legge da tastiera, nella variabile `seme`, e si passa a `srand`. Il programma stampa i lanci, poi il valore piu' piccolo e il piu' grande, ciascuno con la posizione (l'indice) in cui compare per la prima volta, e infine tutte le posizioni in cui compare il valore piu' grande.

```text
Seme: 1
Lanci: 7 6 8 6 6 5 5 11 2 10 9 8 6 5 4 7 2 10 7 7 8 10 5 6 7 11 5 7 6 7
Minimo: 2 (prima volta in posizione 8)
Massimo: 11 (prima volta in posizione 7)
Il massimo compare nelle posizioni: 7 25
```

1. Per stampare tutte le posizioni del massimo servono due cicli: il primo per trovare il massimo, il secondo per cercarlo. Perche' non basta il primo?
2. Un compagno propone di calcolare la somma dei due dadi con `2 + rand() % 11`, che da' anch'essa un numero da $2$ a $12$. Portate `LANCI` a $36000$, togliete la stampa dei lanci e contate, con un array di contatori come in G2, quante volte escono il $2$ e il $7$ con i due metodi. Che cosa notate? In quanti modi si puo' ottenere $7$ con due dadi? E $2$? Quale dei due metodi simula davvero due dadi?

#### Rotazioni, somme e fusioni

**G4.** Scrivete un programma `rotazione_a.c` che riempie un array di `N` interi (con `#define N 10`) con `v[i] = i`, legge un intero `k` non negativo (controllato con un `do while`) e ruota l'array a destra di `k` posti, ripetendo `k` volte la rotazione di un posto: l'ultimo elemento si salva in una variabile `ultimo`, tutti gli altri si spostano a destra di una posizione e `ultimo` va al posto del primo. Alla fine il programma stampa i primi $10$ elementi.

```text
Di quanti posti ruoto a destra? 3
Primi 10 elementi: 7 8 9 0 1 2 3 4 5 6
```

Poi scrivete `rotazione_b.c`, che ottiene lo stesso risultato in un altro modo: copia ogni elemento `v[i]` direttamente nella sua posizione finale di un secondo array `w`, cioe' in `w[(i + k) % N]`, e alla fine ricopia `w` in `v`.

1. Verificate che i due programmi diano lo stesso risultato con $k = 3$, $k = 10$ e $k = 13$. Perche' con $k = 13$ si ottiene lo stesso risultato di $k = 3$? A che cosa serve il `% N` in `rotazione_b.c`?
2. Dopo una rotazione di $k$ posti, con $0 \le k < N$, quale numero si trova in posizione $i$? Distinguete i casi $i \ge k$ e $i < k$.
3. Vediamo ora la rotazione a sinistra. Con $N = 10$, una rotazione a sinistra di $3$ posti equivale a una rotazione a destra di quanti posti?
4. **Con time.** Portate `N` a $100000$ in entrambi i programmi e misurate i tempi con $k = 20000$ (i primi $10$ elementi devono essere `80000 80001 ... 80009`). Quante volte, circa, ciascuno dei due programmi assegna un valore a un elemento di un array? Per quale dei due il tempo dipende da $k$?

**G5.** Le somme prefisse di un array `v` sono i numeri `s[i] = v[0] + v[1] + ... + v[i]`. Scrivete un programma che, per l'array `int v[N] = {3, 1, 4, 1, 5, 9, 2, 6};` (con `#define N 8`), calcola le somme prefisse in un array `s` con un solo ciclo e le stampa. Poi legge due posizioni `a` e `b`, con $0 \le a \le b \le N - 1$ (controllate con un `do while`), e stampa la somma `v[a] + ... + v[b]` usando solo l'array `s`, senza nessun ciclo.

```text
Somme prefisse: 3 4 8 9 14 23 25 31
Posizioni a e b (0 <= a <= b <= 7): 2 5
Somma da v[2] a v[5] = 19
```

1. Perche' basta un solo ciclo per calcolare tutte le somme prefisse? Quante addizioni servono?
2. Come si ottiene la somma da `v[a]` a `v[b]` a partire da `s`? Attenzione al caso $a = 0$.
3. **Con time.** Le somme prefisse servono quando le somme da calcolare sono tante. Scrivete il programma `richieste.c`, con `#define N 100000` e `#define Q 20000`, che riempie l'array e genera `Q` richieste casuali come qui sotto, sommando nella variabile `long totale` i risultati di tutte le richieste.

```c
srand(1);
for (i = 0; i < N; i++) {
    v[i] = 1 + rand() % 100;
}
totale = 0;
for (r = 0; r < Q; r++) {
    a = rand() % N;
    b = rand() % N;
    if (a > b) {
        t = a;
        a = b;
        b = t;
    }
    /* qui aggiungete a totale la somma da v[a] a v[b] */
}
printf("Totale delle richieste: %ld\n", totale);
```

Scrivetene due versioni: nella prima la somma di ogni richiesta si calcola con un ciclo da `a` a `b`; nella seconda con le somme prefisse, salvate in un array `long s[N]` prima del ciclo delle richieste. Entrambe devono stampare `Totale delle richieste: 33753101055`. Misurate i tempi delle due versioni. Al massimo, quante addizioni fa ciascuna?

**G6.** La *fusione* (merge) di due array si puo' presentare come una concatenazione: in un terzo array, abbastanza grande, si copiano gli elementi del primo e poi quelli del secondo. Il programma parte da due array gia' ordinati in modo crescente,

```c
int a[NA] = {2, 5, 8, 13, 21};
int b[NB] = {1, 3, 8, 9, 30, 34};
```

con `#define NA 5` e `#define NB 6`, e costruisce l'array `c` di `NA + NB` elementi in due modi, stampandolo ogni volta.

- **Concatenazione**. Dopo la stampa, il programma controlla con un ciclo se `c` e' ordinato in modo crescente e stampa `(ordinato)` oppure `(non ordinato)`.
- **Fusione ordinata.** Si usano tre indici che partono da $0$: `i` per `a`, `j` per `b` e `k` per `c`. Finche' entrambi gli array hanno ancora elementi da copiare, si confrontano `a[i]` e `b[j]`: se `a[i] <= b[j]` si copia `a[i]` in `c[k]` e si avanza `i`, altrimenti si copia `b[j]` e si avanza `j`; in entrambi i casi si avanza `k`. Quando uno dei due array e' finito, si copiano in fondo a `c` gli elementi rimasti dell'altro. Anche qui, dopo la stampa, il programma controlla se `c` e' ordinato.

```text
Concatenazione: 2 5 8 13 21 1 3 8 9 30 34 (non ordinato)
Fusione ordinata: 1 2 3 5 8 8 9 13 21 30 34 (ordinato)
```

1. Dopo il ciclo principale della fusione servono due cicli per gli elementi rimasti, uno per `a` e uno per `b`. Perche' ne viene eseguito al massimo uno? Con questi due array, quale?
2. Contate con una variabile `confronti` i confronti tra `a[i]` e `b[j]`: quanti sono? Possono mai essere piu' di `NA + NB - 1`? Perche'?
3. I due array contengono entrambi un $8$. Con il confronto `a[i] <= b[j]`, quale dei due $8$ finisce prima in `c`, quello di `a` o quello di `b`? E con `a[i] < b[j]`?

#### Ordinare, contare, cercare

**G7.** Il programma ordina `N` numeri casuali con l'ordinamento a bolle di F18 e conta i confronti e gli scambi; alla fine controlla che l'array sia davvero ordinato.

```c
#include <stdio.h>
#include <stdlib.h>
#define N 5000

int main(void) {
    int v[N];
    int i, passata, t, ordinato;
    long confronti = 0, scambi = 0;
    srand(1);
    for (i = 0; i < N; i++) {
        v[i] = rand();
    }
    for (passata = 1; passata <= N - 1; passata++) {
        for (i = 0; i <= N - 1 - passata; i++) {
            confronti++;
            if (v[i] > v[i + 1]) {
                t = v[i];
                v[i] = v[i + 1];
                v[i + 1] = t;
                scambi++;
            }
        }
    }
    ordinato = 1;
    for (i = 0; i < N - 1; i++) {
        if (v[i] > v[i + 1]) {
            ordinato = 0;
        }
    }
    printf("Numeri ordinati: %d\n", N);
    printf("Confronti: %ld\n", confronti);
    printf("Scambi: %ld\n", scambi);
    if (ordinato) {
        printf("Ordinamento corretto\n");
    } else {
        printf("Ordinamento SBAGLIATO\n");
    }
    return 0;
}
```

1. Prima di eseguirlo, prevedete il numero di confronti con $N = 5000$: nella prima passata se ne fanno $N - 1$, nella seconda $N - 2$, e cosi' via fino a $1$. Ricordate la formula di Gauss (D16).
2. Gli scambi sono circa la meta' dei confronti. Sapreste spiegare perche'? Suggerimento: in F18 avete visto che gli scambi sono tanti quante le inversioni; in un array di numeri casuali, ogni coppia di elementi ha la stessa probabilita' di essere in ordine o in disordine.
3. **Con time.** Completate la tabella. Quando `N` raddoppia, per quanto si moltiplicano i confronti? E il tempo? (Non aspettatevi lo stesso numero preciso: il tempo dipende anche da come il processore usa la memoria, ma deve crescere piu' o meno come i confronti.) Prevedete il tempo per $N = 80000$; se avete pazienza, verificatelo.

| `N` | 5000 | 10000 | 20000 | 40000 |
| --- | --- | --- | --- | --- |
| Confronti |  |  |  |  |
| Tempo `user` |  |  |  |  |

**Novita': `break` dentro un ciclo.** Lo conoscete dallo `switch` del Pacchetto F, dove chiude un caso. Scritto dentro un `for` o un `while`, `break` interrompe subito il ciclo: l'esecuzione riprende dalla prima istruzione dopo la graffa che lo chiude. Serve quando si e' trovato quello che si cercava e continuare a girare sarebbe solo tempo perso.

**G8.** Quanti valori diversi ci sono in un array? Il programma lo scopre cosi': per ogni elemento cerca lo stesso valore tra gli elementi che lo precedono, fermandosi con `break` appena lo trova; se non lo trova, il valore compare li' per la prima volta e viene contato.

```c
#include <stdio.h>
#include <stdlib.h>
#define N 1000
#define MAX_VAL 1000

int main(void) {
    int v[N];
    int i, j, distinti;
    srand(1);
    for (i = 0; i < N; i++) {
        v[i] = 1 + rand() % MAX_VAL;
    }
    distinti = 0;
    for (i = 0; i < N; i++) {
        for (j = 0; j < i; j++) {
            if (v[j] == v[i]) {
                break;
            }
        }
        if (j == i) {
            distinti++;
        }
    }
    printf("Valori distinti: %d su %d\n", distinti, N);
    return 0;
}
```

1. Dopo il ciclo interno, perche' `j == i` significa "il valore non era ancora comparso"?
2. Eseguitelo con `N` e `MAX_VAL` uguali a $1000$, poi entrambi uguali a $10000$: che percentuale di valori distinti ottenete? (Curiosita': quando `N` e `MAX_VAL` sono uguali e molto grandi, la percentuale si avvicina a $1 - \frac{1}{e} \approx 63.2\%$.)

**Novita': i livelli di ottimizzazione.** Un programma C si puo' tradurre in linguaggio macchina in tanti modi. Senza indicazioni, gcc usa il livello `-O0` (zero ottimizzazioni): ogni riga del programma viene tradotta fedelmente, nell'ordine in cui e' scritta, ed e' per questo che gdb riesce a seguirla. Con il flag `-O2` gcc lavora di piu': riordina i calcoli, tiene le variabili nei *registri*, le poche celle velocissime dentro il processore, invece che in memoria, elimina i calcoli inutili. Il programma fa la stessa cosa, ma di solito molto piu' in fretta. Esistono anche `-O1` e `-O3`, ma `-O2` e' il livello piu' usato. Si scrive come gli altri flag:

```bash
gcc -O2 -Wall -Wextra -o distinti_O2 distinti.c
```

Con `-O2` gcc fa anche qualche controllo in piu', e su Ubuntu puo' comparire un warning nuovo sulle `scanf`, `ignoring return value of 'scanf'`: vi ricorda che `scanf` restituisce un valore che si potrebbe controllare. Per ora potete ignorarlo.

3. **Con time.** Portate `N` a $50000$ e `MAX_VAL` a $1000000$, poi compilate due eseguibili, `distinti_O0` (senza flag di ottimizzazione) e `distinti_O2` (con `-O2`). Il risultato cambia? Quante volte e' piu' veloce la versione `-O2`?
4. **In piu'.** Compilate questo programma con e senza `-O2` e misurate i due tempi.

```c
#include <stdio.h>

int main(void) {
    long i, somma = 0;
    for (i = 0; i < 1000000000; i++) {
        somma += i;
    }
    printf("Somma = %ld\n", somma);
    return 0;
}
```

La versione `-O2` impiega qualche millesimo di secondo: e' possibile che faccia un miliardo di addizioni? Che cosa avra' fatto gcc? (Ripensate alla formula di Gauss.) E' anche un avvertimento: quando misurate un programma compilato con `-O2`, controllate che faccia davvero il lavoro che volete misurare.

**G9.** Scrivete un programma che contiene la parola *abracadabra* in un array di caratteri,

```c
char frase[L] = {'a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'};
```

con `#define L 11`, legge un carattere `c` con `scanf(" %c", &c)` e stampa quante volte compare e in quali posizioni. Contate le occorrenze nella variabile `volte` con un primo ciclo; poi, se `volte` non e' zero, stampate le posizioni con un secondo ciclo.

```text
Carattere da cercare: a
Il carattere a compare 5 volte, nelle posizioni: 0 3 5 7 10

Carattere da cercare: z
Il carattere z non compare
```

1. Scrivete una seconda versione che cerca solo la prima posizione del carattere e si ferma con `break` appena la trova. Quanti confronti fa questa versione cercando `a`? E cercando `c` e `z`?
2. **Con gdb.** Compilate la prima versione con `gcc -g -O2 -Wall -Wextra`, mettete un breakpoint sulla riga `volte++;` e lanciate il programma cercando `a`. gdb mette il breakpoint proprio sulla riga che avete chiesto? Quando il programma si ferma, che cosa rispondono `print volte`, `print i` e `print frase`? Avanzate con qualche `next`: le righe vengono eseguite nell'ordine in cui sono scritte? Ripetete tutto compilando senza `-O2`: perche' per usare gdb conviene compilare senza ottimizzazioni?

**G10.** Ricerca lineare o ricerca binaria? Il programma contiene in un array i primi `N` numeri pari, `v[i] = 2 * i` (con `#define N 100000`), quindi l'array e' ordinato. Poi esegue `Q` ricerche (con `#define Q 10000`) di numeri casuali, generati dopo `srand(1)` con `x = rand() % (2 * N)`, e alla fine stampa quante ricerche hanno avuto successo e il numero totale di *passi*, cioe' di giri del ciclo di ricerca, compreso quello in cui `x` viene trovato: aumentate il contatore `passi` come prima istruzione del corpo del ciclo. Scrivetene due versioni: la prima usa la ricerca lineare, che scorre l'array dall'inizio e si ferma con `break` appena trova `x`; la seconda usa la ricerca binaria di F20.

```text
Trovati: 5087 su 10000
Passi: 745236093
```

1. Prima di eseguire: piu' o meno, quante ricerche vi aspettate che abbiano successo? Perche'?
2. Le due versioni devono trovare gli stessi numeri: controllate che la seconda stampi anche lei `Trovati: 5087 su 10000`. Quanti passi fa? Quanti ne fa, al massimo, una singola ricerca binaria su $100000$ elementi?
3. **Con time.** Misurate i tempi delle due versioni.
4. La ricerca binaria e' sempre migliore? Che cosa richiede, che la ricerca lineare non richiede?

### Trova l'errore (G11-G15)

Ogni programma contiene un errore (G15 ne contiene due). Come nei Pacchetti E ed F: trovatelo, correggetelo e dite se e' **sintattico** o **progettuale**. Compilate sempre con `gcc -g -Wall -Wextra`. Attenzione: in uno di questi programmi l'errore non cambia il risultato, ma solo il tempo, e per accorgersene serve `time`.

**G11.** Il programma deve fare lo *shift a destra*: tutti gli elementi si spostano di una posizione verso destra, l'ultimo si perde e il primo resta ripetuto due volte. Deve stampare `a a b c d`, invece stampa `a a a a a`. Nessun warning.

```c
#include <stdio.h>
#define N 5

int main(void) {
    char vett[N] = {'a', 'b', 'c', 'd', 'e'};
    int i;
    for (i = 1; i < N; i++) {
        vett[i] = vett[i - 1];
    }
    for (i = 0; i < N; i++) {
        printf("%c ", vett[i]);
    }
    printf("\n");
    return 0;
}
```

**Con gdb.** Mettete un breakpoint sulla riga `vett[i] = vett[i - 1];`, date `display vett` e andate avanti con `continue`: come cambia l'array a ogni giro? Correggete il programma cambiando soltanto l'intestazione del primo `for`.

**G12.** Il programma deve simulare $10$ lanci di un dado. Invece stampa dieci volte lo stesso numero (che cambia, da un'esecuzione all'altra, solo se si aspetta qualche secondo). Nessun warning. Rileggete G2. Lanciando il programma molte volte, puo' capitare, raramente, che compaiano due numeri diversi: in quale situazione?

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main(void) {
    int dadi[N];
    int i;
    for (i = 0; i < N; i++) {
        srand((unsigned) time(NULL));
        dadi[i] = 1 + rand() % 6;
    }
    printf("Lanci:");
    for (i = 0; i < N; i++) {
        printf(" %d", dadi[i]);
    }
    printf("\n");
    return 0;
}
```

**G13.** Il programma ordina l'array con l'*insertion sort* (G17): deve stampare `Ordinati: 0 1 2 4 5 8`, invece stampa `Ordinati: 5 0 1 2 4 8`. Nessun warning. Eseguite a mano il primo giro del `for` (con $i = 1$): con quale elemento non viene mai confrontata la chiave?

```c
#include <stdio.h>
#define N 6

int main(void) {
    int vett[N] = {5, 1, 4, 2, 8, 0};
    int i, j, chiave;
    for (i = 1; i < N; i++) {
        chiave = vett[i];
        j = i - 1;
        while (j > 0 && vett[j] > chiave) {
            vett[j + 1] = vett[j];
            j = j - 1;
        }
        vett[j + 1] = chiave;
    }
    printf("Ordinati:");
    for (i = 0; i < N; i++) {
        printf(" %d", vett[i]);
    }
    printf("\n");
    return 0;
}
```

**G14.** Il programma ordina con il *bubble sort ottimizzato* (G18) un array di $50000$ elementi *quasi ordinato*: contiene i numeri da $0$ a $49999$ in ordine, tranne i primi due, che sono scambiati. Il risultato e' giusto. Ma il bubble sort ottimizzato dovrebbe accorgersi che l'array e' quasi ordinato: dopo la prima passata e' gia' tutto a posto, la seconda passata non fa nessuno scambio e l'algoritmo si ferma. Il programma dovrebbe quindi terminare in un attimo.

```c
#include <stdio.h>
#define N 50000

int main(void) {
    int v[N];
    int i, passata, scambiato, t, ordinato;
    for (i = 0; i < N; i++) {
        v[i] = i;
    }
    v[0] = 1;
    v[1] = 0;
    scambiato = 0;
    for (passata = 1; passata <= N - 1; passata++) {
        for (i = 0; i <= N - 1 - passata; i++) {
            if (v[i] > v[i + 1]) {
                t = v[i];
                v[i] = v[i + 1];
                v[i + 1] = t;
                scambiato = 1;
            }
        }
        if (scambiato == 0) {
            break;
        }
    }
    ordinato = 1;
    for (i = 0; i < N - 1; i++) {
        if (v[i] > v[i + 1]) {
            ordinato = 0;
        }
    }
    if (ordinato) {
        printf("Array ordinato: %d %d %d ... %d\n", v[0], v[1], v[2], v[N - 1]);
    } else {
        printf("Array NON ordinato\n");
    }
    return 0;
}
```

**Con time.** Misurate il tempo: e' davvero un attimo? Aggiungete un contatore `passate` e stampatelo alla fine: quante passate fa il programma, e quante dovrebbe farne? Dopo la correzione, misurate di nuovo il tempo.

**G15.** Due errori, uno sintattico e uno progettuale. Il programma controlla se l'array e' ordinato in modo crescente: deve stampare `L'array non e' ordinato`, perche' $9 > 4$. Correggete l'errore sintattico completando l'operatore ternario con `: 0`: ora il programma stampa `L'array e' ordinato`. Seguite il valore di `ordinato` giro per giro, su carta o con gdb: quale coppia di elementi decide davvero il risultato?

```c
#include <stdio.h>
#define N 5

int main(void) {
    int v[N] = {2, 9, 4, 7, 8};
    int i, ordinato;
    ordinato = 1;
    for (i = 0; i < N - 1; i++) {
        ordinato = v[i] <= v[i + 1] ? 1;
    }
    if (ordinato) {
        printf("L'array e' ordinato\n");
    } else {
        printf("L'array non e' ordinato\n");
    }
    return 0;
}
```

### Dallo pseudocodice al C (G16-G20)

Traducete come in F16-F20: prima eseguite l'algoritmo a mano con i valori dell'esempio, poi scrivete il codice, con le dimensioni degli array in una `#define`. Due promemoria per lo pseudocodice: `scambia _x e _y` si traduce con tre assegnazioni e una variabile d'appoggio (C13), mentre `ESCI DAL CICLO` si traduce con `break`, che avete incontrato in G8. Nei primi tre esercizi il programma legge `_n` (da $2$ a `MAX`, che vale $20$, controllato con un `do while`) e poi gli `_n` numeri, come in F18.

**G16.** Il *selection sort* (ordinamento per selezione): a ogni giro cerca il piu' piccolo tra gli elementi non ancora sistemati e lo scambia con il primo di essi.

```text
INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    ASSEGNA a _scambi il valore 0
    PER _j DA 0 A _n - 2
        ASSEGNA a _k il valore _j
        PER _i DA _j + 1 A _n - 1
            SE _v[_i] < _v[_k] ALLORA
                ASSEGNA a _k il valore _i
            FINE
        FINE
        SE _k diverso da _j ALLORA
            scambia _v[_j] e _v[_k]
            ASSEGNA a _scambi il valore _scambi + 1
        FINE
    FINE
    VISUALIZZA _v e _scambi
FINE
```

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Ordinati: 0 1 2 4 5 8
Scambi: 3
```

1. Eseguite a mano l'algoritmo con `5 1 4 2 8 0` e completate la tabella con l'array alla fine di ogni giro del PER esterno.

| `_j` | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Array |  |  |  |  |  |

2. Con lo stesso array, il bubble sort di F18 fa $9$ scambi. Perche' il selection sort ne fa al massimo $n - 1$? Quanti confronti tra `_v[_i]` e `_v[_k]` fa invece? Il numero di confronti dipende dall'ordine iniziale dei numeri?
3. **Con time.** Copiate il programma in `selezione_tempo.c`: togliete la lettura, riempite un array di $40000$ elementi con `srand(1)` e `rand()` come in G7, e stampate solo il numero di scambi, che deve essere $39986$. Confrontate il tempo con quello di G7 per lo stesso `N`: i confronti sono gli stessi, ma quale dei due programmi e' piu' veloce? Perche'?

**G17.** L'*insertion sort* (ordinamento per inserimento): ogni elemento, la *chiave*, viene inserito al suo posto nella parte gia' ordinata, spostando a destra di una posizione gli elementi piu' grandi.

```text
INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    ASSEGNA a _spostamenti il valore 0
    PER _i DA 1 A _n - 1
        ASSEGNA a _chiave il valore _v[_i]
        ASSEGNA a _j il valore _i - 1
        FINCHE' _j >= 0 E _v[_j] > _chiave
            ASSEGNA a _v[_j + 1] il valore _v[_j]
            ASSEGNA a _spostamenti il valore _spostamenti + 1
            ASSEGNA a _j il valore _j - 1
        FINE
        ASSEGNA a _v[_j + 1] il valore _chiave
    FINE
    VISUALIZZA _v e _spostamenti
FINE
```

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Ordinati: 0 1 2 4 5 8
Spostamenti: 9
```

1. Con `5 1 4 2 8 0` gli spostamenti sono $9$, come gli scambi del bubble sort in F18 e come le inversioni dell'array. E' una coincidenza? Quante inversioni corregge ogni spostamento?
2. In C, se la prima condizione di un `&&` e' falsa, la seconda non viene nemmeno calcolata. Perche', allora, nella condizione del FINCHE' il controllo `_j >= 0` deve venire prima di `_v[_j] > _chiave`?
3. **Con time.** Copiate il programma in `inserimento_tempo.c`, con un array di $40000$ elementi. Al posto dei numeri il programma legge il tipo di array: `1` ordinato (`v[i] = i`), `2` rovesciato (`v[i] = N - i`), `3` casuale (`srand(1)` e `v[i] = rand()`). Completate la tabella, guardando il tempo `user`: perche' qui non conviene guardare `real`? (Ricordate G1.)

| Tipo di array | Ordinato | Rovesciato | Casuale |
| --- | --- | --- | --- |
| Spostamenti |  |  |  |
| Tempo `user` |  |  |  |

4. Con l'array casuale, confrontate gli spostamenti con gli scambi di G7 con $N = 40000$: che cosa notate, e perche'? Perche' con l'array rovesciato il tempo e' circa il doppio che con quello casuale? E perche' con l'array ordinato il programma e' quasi istantaneo?

**G18.** Il *bubble sort ottimizzato*: se in una passata non avviene nessuno scambio, l'array e' gia' ordinato e si puo' smettere.

```text
INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    ASSEGNA a _passate il valore 0
    PER _passata DA 1 A _n - 1
        ASSEGNA a _passate il valore _passate + 1
        ASSEGNA a _scambiato il valore 0
        PER _i DA 0 A _n - 1 - _passata
            SE _v[_i] > _v[_i + 1] ALLORA
                scambia _v[_i] e _v[_i + 1]
                ASSEGNA a _scambiato il valore 1
            FINE
        FINE
        SE _scambiato = 0 ALLORA
            ESCI DAL CICLO
        FINE
    FINE
    VISUALIZZA _v e _passate
FINE
```

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Ordinati: 0 1 2 4 5 8
Passate: 5
```

1. Con `5 1 4 2 8 0` l'ottimizzazione non fa risparmiare nessuna passata. Quante passate servono con `1 2 3 4 5 6`?
2. *Lepri e tartarughe.* Provate con `6 1 2 3 4 5` e con `2 3 4 5 6 1`: quante passate servono? In una passata, di quante posizioni puo' spostarsi verso destra un elemento grande? E verso sinistra un elemento piccolo?
3. **Con gdb.** Mettete un breakpoint sulla riga del `break` e, quando il programma si ferma, date `print passata`. Con `6 1 2 3 4 5`, in quale passata si ferma? Con `2 3 4 5 6 1` il programma si ferma sul breakpoint? Perche'?

**G19.** Il *counting sort* (ordinamento per conteggio) ordina numeri interi compresi tra $1$ e `MAX_VAL` senza mai confrontarli tra loro: conta quante volte compare ogni valore, come in G2, e poi riscrive l'array.

```text
INIZIO
    PER _x DA 1 A MAX_VAL
        ASSEGNA a _quante[_x] il valore 0
    FINE
    PER _i DA 0 A _n - 1
        ASSEGNA a _quante[_v[_i]] il valore _quante[_v[_i]] + 1
    FINE
    ASSEGNA a _k il valore 0
    PER _x DA 1 A MAX_VAL
        PER _c DA 1 A _quante[_x]
            ASSEGNA a _v[_k] il valore _x
            ASSEGNA a _k il valore _k + 1
        FINE
    FINE
FINE
```

Il programma riempie un array di `N` elementi (con `#define N 40000`) con `srand(1)` e `v[i] = 1 + rand() % MAX_VAL`, con `#define MAX_VAL 300`, lo ordina con l'algoritmo, controlla che sia ordinato come in G7 e stampa tre elementi.

```text
Ordinamento corretto
v[0] = 1, v[20000] = 152, v[39999] = 300
```

1. Eseguite a mano l'algoritmo con l'array `3 1 2 3 3 1` e `MAX_VAL` uguale a $3$: quanto valgono `_quante[1]`, `_quante[2]` e `_quante[3]` dopo il secondo PER? Quante volte viene eseguita l'assegnazione `ASSEGNA a _v[_k] il valore _x`, in tutto?
2. **Con time.** Ordinate lo stesso array (stesso `N`, stessi valori da $1$ a $300$) anche con l'insertion sort di G17 e confrontate i tempi. Poi portate `N` a $1000000$ nel counting sort: quanto tempo serve?
3. Perche' il counting sort non e' adatto a ordinare i numeri di G7, generati con `rand()` senza `%`? Quanto dovrebbe essere grande l'array `quante`?

**G20.** **Sfida.** La rotazione a destra di `_k` posti si puo' fare sul posto, senza un secondo array e con circa `_N` scambi, rovesciando tre volte un tratto dell'array, con il metodo dei due indici di F4: si rovescia tutto l'array, poi il tratto dei primi `_k` elementi, poi il tratto dei restanti. Per rovesciare il tratto che va dalla posizione `_a` alla posizione `_b` si usano due indici, come in F4:

```text
ASSEGNA a _i il valore _a
ASSEGNA a _j il valore _b
FINCHE' _i < _j
    scambia _v[_i] e _v[_j]
    ASSEGNA a _i il valore _i + 1
    ASSEGNA a _j il valore _j - 1
FINE
```

L'algoritmo completo, con l'array riempito con `v[i] = i` come in G4, e':

```text
INIZIO
    LEGGI _k (non negativo)
    ASSEGNA a _k il valore del resto di _k diviso _N
    rovescia il tratto da 0 a _N - 1
    rovescia il tratto da 0 a _k - 1
    rovescia il tratto da _k a _N - 1
    VISUALIZZA i primi 10 elementi di _v
FINE
```

Non avete ancora visto le funzioni, quindi il ciclo che rovescia un tratto va scritto tre volte, cambiando solo i valori iniziali di `i` e `j`.

```text
Di quanti posti ruoto a destra? 3
Primi 10 elementi: 7 8 9 0 1 2 3 4 5 6
```

1. Eseguite a mano l'algoritmo con $N = 7$ e $k = 3$, partendo da `0 1 2 3 4 5 6`: scrivete l'array dopo ciascuno dei tre rovesciamenti. Ottenete la stessa rotazione di G4?
2. Perche' funziona? Suggerimento: dopo il primo rovesciamento, dove sono finiti gli ultimi `_k` elementi dell'array di partenza, e in che ordine?
3. Che cosa succede con $k = 0$? E con $k = N$? Controllate che il programma non faccia nulla di strano.
4. **Con time.** Con $N = 100000$ e $k = 20000$, confrontate il tempo con quello delle due versioni di G4. Quanti scambi fa, in tutto? Rispetto a `rotazione_b.c`, che cosa risparmia?


## Pacchetto H: Matrici e gprof

Le matrici sono gli array a due dimensioni, e le avete appena incontrate. In questo pacchetto le usiamo per un po' di algebra lineare (trasposta, traccia, prodotto, determinante) e per qualche gioco, e conosciamo il secondo aiutante della sessione: **gprof**. `time` dice quanto dura un programma intero; gprof dice *dove* passa il tempo, riga per riga. Le domande che lo usano iniziano con **Con gprof.** Anche qui gli aiutanti accompagnano gli esercizi senza esserne il centro: `time` continua a comparire, e gdb, che mostra le matrici molto bene, ogni tanto torna utile. Compilate sempre con `gcc -g -Wall -Wextra`.

### Le matrici, in breve

```c
#define R 3
#define C 4

int m[R][C];                          /* R righe e C colonne */
int id[2][2] = {{1, 0}, {0, 1}};      /* valori iniziali, una riga alla volta */

for (i = 0; i < R; i++) {             /* scorre le righe */
    for (j = 0; j < C; j++) {         /* scorre le colonne della riga i */
        printf("%4d", m[i][j]);       /* %4d: ogni numero occupa 4 caratteri */
    }
    printf("\n");
}
```

L'elemento `m[i][j]` sta nella riga `i` e nella colonna `j`, entrambe numerate da $0$. Come per gli array, il C non controlla gli indici. Con `%4d` ogni numero occupa sempre $4$ caratteri, aggiungendo spazi a sinistra: cosi' le colonne restano allineate.

### Esercizi (H1-H10)

#### Le operazioni tra matrici

**H1.** Il programma dichiara la matrice `int m[R][C]`, con `#define R 4` e `#define C 5`, la riempie con `m[i][j] = i + j` e la stampa con `%4d`.

```text
   0   1   2   3   4
   1   2   3   4   5
   2   3   4   5   6
   3   4   5   6   7
```

1. In quali posizioni si trovano gli elementi che valgono $4$? Che figura formano, nella matrice, gli elementi uguali tra loro?
2. Modificate il programma perche' stampi la tavola pitagorica, una matrice $10 \times 10$ con righe e colonne numerate da $1$ a $10$: quanto deve valere `m[i][j]`? Perche' la tavola e' simmetrica rispetto alla diagonale principale?
3. Tornate a $R = 4$ e $C = 5$ e riempite la matrice con numeri casuali da $1$ a $300$, dopo `srand(1)`. La prima riga deve essere `284 287 178 116 294`.
4. **Con gdb.** Con la matrice casuale, mettete un breakpoint sul ciclo di stampa e provate `print m`, `print m[1]` e `print m[1][2]`. Come mostra gdb una matrice? Che cos'e', per gdb, `m[1]`?

**H2.** In un concorso di intelligenza, `GIUDICI` giudici (con `#define GIUDICI 4`) danno a ciascuno dei `CANDIDATI` candidati (con `#define CANDIDATI 6`) un voto da $0$ a $5$. Nella matrice dei voti ogni riga corrisponde a un giudice e ogni colonna a un candidato:

```c
int voti[GIUDICI][CANDIDATI] = {
    {3, 5, 2, 4, 1, 5},
    {4, 4, 3, 5, 2, 4},
    {2, 5, 1, 3, 0, 4},
    {5, 3, 4, 5, 2, 3}
};
```

Il programma stampa il punteggio totale di ogni candidato, il candidato piu' intelligente (quello con il punteggio piu' alto) e il giudice piu' severo (quello che ha assegnato meno punti in tutto). Giudici e candidati si numerano da $1$; a parita', vale il primo.

```text
Punteggi dei candidati: 14 17 10 17 5 16
Candidato piu' intelligente: 2 (17 punti)
Giudice piu' severo: 3 (15 punti assegnati)
```

1. Per calcolare il punteggio di un candidato si somma una colonna. Quale indice varia nel ciclo interno? E per i punti assegnati da un giudice?
2. I candidati $2$ e $4$ sono a pari merito. Modificate il programma perche' stampi tutti i candidati con il punteggio piu' alto: `Candidati piu' intelligenti: 2 4`. Suggerimento: come in G3, servono due cicli.
3. Il giudice piu' severo e' anche quello che ha dato il voto piu' basso? Deve essere sempre cosi'?

**H3.** Il programma riempie una matrice `a` di `R` righe e `C` colonne (con `#define R 3` e `#define C 5`) con numeri casuali da $1$ a $300$, dopo `srand(1)`, riga per riga. Poi calcola la trasposta in una seconda matrice `t`, con `t[j][i] = a[i][j]`, e le stampa entrambe.

```text
Matrice:
 284 287 178 116 294
 236 287 193 250 122
  63 128 291 260 264
Trasposta:
 284 236  63
 287 287 128
 178 193 291
 116 250 260
 294 122 264
```

1. Come va dichiarata la matrice `t`? Che cosa succederebbe dichiarandola `int t[R][C]`?
2. Calcolate in una terza matrice la trasposta di `t` e controllate con un ciclo che sia uguale ad `a`, con una variabile che parte da $1$ e diventa $0$ alla prima differenza (F14). Il programma deve stampare `La trasposta della trasposta e' uguale alla matrice di partenza`.
3. Una matrice quadrata uguale alla sua trasposta si dice *simmetrica*. Scrivete una matrice simmetrica $3 \times 3$ in cui i numeri sopra la diagonale principale sono tutti diversi tra loro.

**H4.** Il programma lavora su matrici quadrate di ordine `N` (con `#define N 4`). Dopo `srand(1)` riempie, riga per riga, una matrice `a` con numeri casuali da $1$ a $300$, e subito dopo, nello stesso modo, una matrice `b`. Poi stampa la matrice `a` e la sua traccia, cioe' la somma degli elementi della diagonale principale; legge un intero `k`, stampa la matrice `k` per `a` e la sua traccia; infine stampa la traccia di `b` e quella della somma `a + b`.

```text
Matrice A:
 284 287 178 116
 294 236 287 193
 250 122  63 128
 291 260 264 227
Traccia di A: 810
Moltiplicatore k: 3
Matrice kA:
 852 861 534 348
 882 708 861 579
 750 366 189 384
 873 780 792 681
Traccia di kA: 2430
Traccia di B: 476
Traccia di A + B: 1286
```

1. Spiegate perche' la traccia di $kA$ e' $k$ volte la traccia di $A$, e perche' la traccia di $A + B$ e' la somma delle due tracce.
2. Per calcolare la traccia basta un solo ciclo. Un compagno usa invece due cicli, uno dentro l'altro, e un `if (i == j)`: quanti elementi controlla, con $N = 4$? E con $N = 1000$?
3. Perche' la traccia e' definita solo per le matrici quadrate?

**H5.** Il prodotto riga per colonna: se $A$ ha `R` righe e `C` colonne e $B$ ha `C` righe e `P` colonne, il prodotto $AB$ ha `R` righe e `P` colonne, e il suo elemento di riga `i` e colonna `j` e' la somma dei prodotti `a[i][k] * b[k][j]`, per `k` da $0$ a `C - 1`. Scrivete un programma che, con `#define R 2` e `#define C 3`, calcola e stampa i prodotti $AB$ e $BA$ delle matrici

```c
int a[R][C] = {{1, 2, 0}, {3, -1, 4}};
int b[C][R] = {{2, 1}, {0, 5}, {-3, 2}};
```

e le loro tracce.

```text
AB:
   2  11
  -6   6
BA:
   5   3   4
  15  -5  20
   3  -8   8
Traccia di AB: 8
Traccia di BA: 8
```

1. Che dimensioni hanno $AB$ e $BA$? Potrebbero mai essere uguali, per queste due matrici?
2. Quante moltiplicazioni servono per calcolare $AB$? E $BA$? In generale, quante ne servono per moltiplicare una matrice $R \times C$ per una $C \times P$?
3. Le due tracce sono uguali: e' un caso? Cambiate qualche numero in `a` e in `b` e ricontrollate.

#### Matrici grandi: time e gprof

**H6.** Una domanda che viene naturale: *e' piu' veloce scorrere una matrice per righe, per colonne, o e' indifferente?* Questo programma risponde con un esperimento: somma tutti gli elementi di una matrice $4000 \times 4000$, scorrendola per righe o per colonne a scelta dell'utente. Un solo calcolo dura pochi centesimi di secondo, troppo poco per misurarlo bene: per questo il programma lo ripete `VOLTE` volte.

**Novita': matrici molto grandi.** Un array dichiarato dentro `main` vive in una zona di memoria riservata al programma, lo *stack*, che su Linux e' grande di solito $8$ MB: un array piu' grande non ci sta e il programma va in crash. Gli array molto grandi, come questa matrice di $16$ milioni di `int`, si dichiarano quindi prima di `main`, fuori da tutte le graffe. Cosi' possono essere grandi quanto la memoria del computer, e i loro elementi partono da $0$. Il perche' lo vedrete piu' avanti, quando parlerete di classi di memorizzazione.

```c
#include <stdio.h>
#define N 4000
#define VOLTE 10

int m[N][N];

int main(void) {
    int i, j, giro, scelta;
    long somma;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            m[i][j] = (i + j) % 10;
        }
    }
    printf("1 = per righe, 2 = per colonne: ");
    scanf("%d", &scelta);
    somma = 0;
    for (giro = 0; giro < VOLTE; giro++) {
        if (scelta == 1) {
            for (i = 0; i < N; i++) {
                for (j = 0; j < N; j++) {
                    somma += m[i][j];
                }
            }
        } else {
            for (j = 0; j < N; j++) {
                for (i = 0; i < N; i++) {
                    somma += m[i][j];
                }
            }
        }
    }
    printf("Somma: %ld\n", somma);
    return 0;
}
```

1. Prima di eseguirlo, calcolate la somma che deve stampare. Suggerimento: quanto vale la somma di una riga?
2. **Con time.** Completate la tabella con il tempo `user`, compilando il programma senza ottimizzazioni e con `-O2` (G8). Quale modo e' piu' veloce? L'ottimizzazione riesce a rimediare all'ordine sfavorevole?

| | Per righe | Per colonne |
| --- | --- | --- |
| Senza ottimizzazioni |  |  |
| Con `-O2` |  |  |

3. In memoria gli elementi di una matrice stanno uno dopo l'altro, riga per riga: prima tutta la riga $0$, poi tutta la riga $1$, e cosi' via. Quando il processore legge un elemento dalla RAM, ne porta nella *cache*, una memoria piccola e velocissima che sta dentro il processore, anche i vicini che lo seguono in memoria. Con queste due informazioni, spiegate i tempi della tabella.
4. Spostate la dichiarazione `int m[N][N];` dentro `main`, ricompilate ed eseguite: che cosa succede? Quanti MB occupa la matrice, sapendo che un `int` occupa $4$ byte?

**Novita': gprof.** `time` dice quanto dura un programma intero. Per sapere *dove* il programma passa il tempo serve un *profiler*: noi useremo gprof, che di solito e' installato insieme a gcc. I passi sono tre:

```bash
gcc -g -pg -Wall -Wextra -o gemelli gemelli.c   # 1. compilare aggiungendo -pg
./gemelli                                       # 2. eseguire: viene creato il file gmon.out
gprof -b -l ./gemelli gmon.out                  # 3. leggere il resoconto
```

Con `-pg`, mentre il programma gira, cento volte al secondo viene annotata la riga che si sta eseguendo; alla fine le annotazioni finiscono nel file `gmon.out`. Il comando `gprof` le riassume: `-l` chiede il resoconto riga per riga, `-b` toglie le lunghe spiegazioni. Il resoconto ha questa forma:

```text
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  Ts/call  Ts/call  name    
 84.96      0.96     0.96                             main (gemelli.c:12 @ 1275)
 15.04      1.13     0.17                             main (gemelli.c:11 @ 129d)
```

Bastano la prima colonna, la percentuale del tempo totale, e il numero di riga che segue il nome del file: qui la riga $12$ occupa l'$85\%$ del tempo e la riga $11$ il resto. Le altre colonne e il numero dopo la `@` si possono ignorare. Tre avvertenze:

- i numeri cambiano un po' da un'esecuzione all'altra, come quelli di `time`;
- se il programma dura pochi centesimi di secondo, le annotazioni sono poche e le percentuali poco affidabili; sotto un centesimo non c'e' nessuna annotazione, e gprof risponde `no time accumulated`;
- il file `gmon.out` viene riscritto ogni volta che eseguite un programma compilato con `-pg`.

Di solito gprof si usa per sapere quanto tempo passa in ciascuna *funzione* del programma: senza `-l` vedreste solo una riga con `main`, perche' i nostri programmi hanno solo quella. Quando vedrete le funzioni, anche il resoconto senza `-l` diventera' utile.

**H7.** Due primi si dicono *gemelli* se differiscono di $2$, come $3$ e $5$, $11$ e $13$, $41$ e $43$ (non si sa se le coppie di primi gemelli siano infinite). Il programma segna in un array i numeri primi fino a `LIMITE`, provando tutti i divisori come in D37, poi conta i primi e le coppie di primi gemelli.

```c
#include <stdio.h>
#define LIMITE 100000

int main(void) {
    int primo[LIMITE + 1];
    int n, d, primi, gemelli;
    primo[0] = 0;
    primo[1] = 0;
    for (n = 2; n <= LIMITE; n++) {
        primo[n] = 1;
        for (d = 2; d < n; d++) {
            if (n % d == 0) {
                primo[n] = 0;
                break;
            }
        }
    }
    primi = 0;
    gemelli = 0;
    for (n = 2; n <= LIMITE; n++) {
        if (primo[n] == 1) {
            primi++;
            if (n + 2 <= LIMITE && primo[n + 2] == 1) {
                gemelli++;
            }
        }
    }
    printf("Primi fino a %d: %d\n", LIMITE, primi);
    printf("Coppie di primi gemelli: %d\n", gemelli);
    return 0;
}
```

```text
Primi fino a 100000: 9592
Coppie di primi gemelli: 1224
```

1. **Con gprof.** Il resoconto mostrato nella novita' qui sopra e' proprio quello di questo programma: ripetetelo sul vostro computer. Le percentuali sono simili? Che cosa fanno le due righe che occupano tutto il tempo?
2. Non serve provare tutti i divisori fino a $n - 1$: basta arrivare finche' $d \cdot d \le n$, cioe' scrivere `d * d <= n` nella condizione del ciclo. Perche'? Suggerimento: se $n = a \cdot b$ con $a \le b$, quanto puo' essere grande $a$?
3. **Con time.** Confrontate i tempi delle due versioni.
4. **Con gprof.** Ripetete il resoconto con la nuova versione: che cosa risponde gprof, e perche'? Portate `LIMITE` a $2000000$, spostando l'array `primo` prima di `main` come in H6. Il programma deve stampare $148933$ primi e $14871$ coppie di gemelli. Ora gprof ha qualcosa da dire? La riga piu' lenta e' la stessa di prima?
5. **Con time.** Sempre con `LIMITE` uguale a $2000000$, segnate i primi con il crivello di Eratostene (F16) invece che con i divisori: quanto tempo serve ora?

**H8.** Il prodotto di due matrici grandi. Scrivete un programma che, con `#define N 1000`, riempie due matrici $N \times N$ con `a[i][j] = (i + j) % 10` e `b[i][j] = (i * j) % 10`, calcola il prodotto `c` come in H5 e stampa la traccia di `c`. Le tre matrici vanno dichiarate prima di `main` (H6).

```text
Traccia del prodotto: 16000000
```

Poi scrivete una seconda versione, che prima calcola la trasposta di `b` in una quarta matrice `bt`, come in H3, e poi calcola `c[i][j]` come somma dei prodotti `a[i][k] * bt[j][k]`. Il risultato deve essere lo stesso.

1. Nella prima versione, mentre `k` varia, la matrice `a` viene letta lungo una riga. E `b`? E `bt`, nella seconda versione?
2. Quante moltiplicazioni fa il programma, in tutto? Quante assegnazioni costa, in piu', il calcolo di `bt`?
3. **Con time.** Completate la tabella. Rivedete H6: perche' la seconda versione e' piu' veloce, anche se fa piu' lavoro?

| | Prima versione | Con la trasposta |
| --- | --- | --- |
| Senza ottimizzazioni |  |  |
| Con `-O2` |  |  |

#### Matrici speciali e giochi

**H9.** Una matrice quadrata si dice *diagonale* se tutti gli elementi fuori dalla diagonale principale sono $0$; *identita'* se e' diagonale e tutti gli elementi della diagonale sono $1$; *triangolare superiore* se tutti gli elementi sotto la diagonale principale (quelli con $i > j$) sono $0$; *simmetrica* se `m[i][j] == m[j][i]` per ogni `i` e `j` (H3). Scrivete un programma che, per una matrice $4 \times 4$ scritta nel codice, stampa quali di queste proprieta' ha. Per ogni proprieta' usate una variabile che parte da $1$ e diventa $0$ al primo elemento che la viola (F14). Provatelo con le quattro matrici qui sotto, cambiando ogni volta i valori iniziali nel codice.

```c
int a[N][N] = {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
int b[N][N] = {{2, 0, 0, 0}, {0, 5, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 7}};
int c[N][N] = {{1, 2, 3, 4}, {0, 5, 6, 7}, {0, 0, 8, 9}, {0, 0, 0, 1}};
int d[N][N] = {{1, 2, 3, 4}, {2, 5, 6, 7}, {3, 6, 8, 9}, {4, 7, 9, 1}};
```

```text
Identita': no
Diagonale: no
Triangolare superiore: si'
Simmetrica: no
```

(L'esempio e' l'output con la matrice `c`.)

1. Completate la tabella con le risposte del vostro programma.

| Matrice | Identita' | Diagonale | Triangolare superiore | Simmetrica |
| --- | --- | --- | --- | --- |
| `a` |  |  |  |  |
| `b` |  |  |  |  |
| `c` |  |  |  |  |
| `d` |  |  |  |  |

2. Una matrice diagonale e' sempre triangolare superiore? E simmetrica?
3. Per controllare la simmetria, il vostro programma confronta tutte le $16$ coppie `m[i][j]` e `m[j][i]`. Quali confronti sono inutili? Quanti ne bastano, con $N = 4$?
4. Una matrice simmetrica e triangolare superiore e' per forza diagonale? Perche'?

**H10.** Il gioco del tris si gioca su una griglia $3 \times 3$: due giocatori, `X` e `O`, scrivono a turno il loro simbolo in una casella vuota, e vince chi riempie per primo una riga, una colonna o una diagonale. Comincia sempre `X`. Scrivete un programma che, per una griglia `char g[3][3]` scritta nel codice (con `.` per le caselle vuote), stampa:

- `Griglia impossibile`, se il numero delle `X` non e' uguale a quello delle `O` o a quello delle `O` piu' uno (comincia `X` e si gioca a turno);
- altrimenti `Vince X`, `Vince O` oppure `Nessun vincitore`.

Una riga, una colonna o una diagonale e' vincente se le sue tre caselle contengono lo stesso simbolo e non sono vuote. Provate il programma con queste griglie, scritte una riga alla volta:

| Griglia | Righe | Risultato |
| --- | --- | --- |
| 1 | `XXX`, `OO.`, `...` | `Vince X` |
| 2 | `XOX`, `XO.`, `.O.` | `Vince O` |
| 3 | `XOO`, `.X.`, `..X` | `Vince X` |
| 4 | `XOX`, `XOO`, `OXX` | `Nessun vincitore` |
| 5 | `OOO`, `X..`, `...` | `Griglia impossibile` |

Per esempio, la prima griglia si scrive `char g[3][3] = {{'X', 'X', 'X'}, {'O', 'O', '.'}, {'.', '.', '.'}};`.

1. Quante sono, in tutto, le righe, le colonne e le diagonali da controllare?
2. Nella griglia 2 ci sono tre `X` e tre `O`: chi ha fatto l'ultima mossa? E nella griglia 1?
3. Scrivete una griglia in cui sia `X` sia `O` hanno tre simboli in fila, con il numero di `X` e di `O` corretto: e' una partita possibile? Perche'?

### Trova l'errore (H11-H15)

Ogni programma contiene un errore (H14 ne contiene due). Correggetelo e dite se e' sintattico o progettuale. In H15 l'errore non cambia il risultato, ma il tempo: per trovarlo, questa volta, usate gprof.

**H11.** Il programma deve stampare la matrice di $3$ righe e $5$ colonne

```text
   0   1   2   3   4
  10  11  12  13  14
  20  21  22  23  24
```

invece stampa $5$ righe di $3$ numeri, e le ultime due contengono numeri strani, che cambiano da un'esecuzione all'altra. Nessun warning.

```c
#include <stdio.h>
#define R 3
#define C 5

int main(void) {
    int m[R][C];
    int i, j;
    for (i = 0; i < R; i++) {
        for (j = 0; j < C; j++) {
            m[i][j] = 10 * i + j;
        }
    }
    for (i = 0; i < C; i++) {
        for (j = 0; j < R; j++) {
            printf("%4d", m[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

**Con gdb.** Mettete un breakpoint sulla riga `printf("%4d", m[i][j]);` con la condizione `if i == 3`. Quando il programma si ferma, che cosa mostra `print m`? La matrice e' stata riempita correttamente? E che cosa mostra `print m[3]`?

**H12.** Il programma deve trasporre la matrice *sul posto*, cioe' senza una seconda matrice, scambiando ogni elemento `m[i][j]` con `m[j][i]`. Deve stampare `1 4 7`, `2 5 8`, `3 6 9`, invece stampa la matrice di partenza, senza nessun cambiamento. Nessun warning. Quante volte viene scambiato `m[0][1]` con `m[1][0]`? Correggete il programma cambiando soltanto l'intestazione del ciclo interno.

```c
#include <stdio.h>
#define N 3

int main(void) {
    int m[N][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int i, j, t;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            t = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = t;
        }
    }
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%4d", m[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

**H13.** Il programma calcola il prodotto di due matrici $2 \times 2$: deve stampare `19 22` e `43 50`, invece stampa `19 41` e `84 134`. Nessun warning. Che relazione c'e' tra i numeri giusti e quelli stampati?

```c
#include <stdio.h>
#define N 2

int main(void) {
    int a[N][N] = {{1, 2}, {3, 4}};
    int b[N][N] = {{5, 6}, {7, 8}};
    int c[N][N];
    int i, j, k, somma;
    somma = 0;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                somma += a[i][k] * b[k][j];
            }
            c[i][j] = somma;
        }
    }
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%4d", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

**H14.** Due errori, uno sintattico e uno progettuale. Il programma calcola il punteggio di ogni candidato, come in H2, con $3$ giudici e $4$ candidati: deve stampare $9$, $14$, $6$ e $12$ punti. Corretto l'errore sintattico, stampa $10$, $11$ e $8$ punti per i primi tre candidati, e un numero strano per il quarto.

```c
#include <stdio.h>
#define GIUDICI 3
#define CANDIDATI 4

int main(void) {
    int voti[GIUDICI][CANDIDATI] = {{3, 5, 2, 4}; {4, 4, 3, 5}; {2, 5, 1, 3}};
    int i, j, somma;
    for (j = 0; j < CANDIDATI; j++) {
        somma = 0;
        for (i = 0; i < GIUDICI; i++) {
            somma += voti[j][i];
        }
        printf("Candidato %d: %d punti\n", j + 1, somma);
    }
    return 0;
}
```

**H15.** Il programma conta quanti elementi di una matrice $1000 \times 1000$ di numeri casuali sono maggiori della media della loro riga. Il risultato e' giusto, `Elementi maggiori della media della loro riga: 499751 su 1000000`, ma il programma impiega qualche secondo, mentre dovrebbe essere quasi istantaneo.

```c
#include <stdio.h>
#include <stdlib.h>
#define R 1000
#define C 1000

int m[R][C];

int main(void) {
    int i, j, k, conta;
    double somma, media;
    srand(1);
    for (i = 0; i < R; i++) {
        for (j = 0; j < C; j++) {
            m[i][j] = rand() % 100;
        }
    }
    conta = 0;
    for (i = 0; i < R; i++) {
        for (j = 0; j < C; j++) {
            somma = 0;
            for (k = 0; k < C; k++) {
                somma += m[i][k];
            }
            media = somma / C;
            if (m[i][j] > media) {
                conta++;
            }
        }
    }
    printf("Elementi maggiori della media della loro riga: %d su %d\n", conta, R * C);
    return 0;
}
```

**Con gprof.** Quale riga occupa quasi tutto il tempo? Quante volte viene calcolata la media di ciascuna riga, e quante volte basterebbe calcolarla? Correggete il programma, controllate che il risultato non cambi e misurate il nuovo tempo con `time`.

### Dallo pseudocodice al C (H16-H20)

Come in G16-G20: prima eseguite l'algoritmo a mano, poi traducetelo. Nello pseudocodice una matrice si scrive come in C: `_q[_i][_j]` e' l'elemento di riga `_i` e colonna `_j`.

**H16.** Un *quadrato magico* di ordine $n$ contiene i numeri da $1$ a $n^2$, disposti in modo che tutte le righe, tutte le colonne e le due diagonali abbiano la stessa somma. Per $n$ dispari esiste un metodo semplice, noto dal Seicento: si mette $1$ al centro della prima riga, e ogni numero successivo nella casella in alto a destra del precedente. Se si esce dalla matrice si rientra dal lato opposto; se la casella e' gia' occupata, si scende invece di una casella sotto il numero precedente.

```text
INIZIO
    LEGGI _n (dispari, da 1 a 15)
    PER _i DA 0 A _n - 1
        PER _j DA 0 A _n - 1
            ASSEGNA a _q[_i][_j] il valore 0
        FINE
    FINE
    ASSEGNA a _i il valore 0
    ASSEGNA a _j il valore _n / 2
    PER _k DA 1 A _n x _n
        ASSEGNA a _q[_i][_j] il valore _k
        ASSEGNA a _r il valore del resto di _i - 1 + _n diviso _n
        ASSEGNA a _c il valore del resto di _j + 1 diviso _n
        SE _q[_r][_c] diverso da 0 ALLORA
            ASSEGNA a _r il valore del resto di _i + 1 diviso _n
            ASSEGNA a _c il valore _j
        FINE
        ASSEGNA a _i il valore _r
        ASSEGNA a _j il valore _c
    FINE
    VISUALIZZA _q
FINE
```

```text
Ordine del quadrato (dispari, da 1 a 15): 3
   8   1   6
   3   5   7
   4   9   2
```

1. Eseguite a mano l'algoritmo con $n = 3$: in quali passi la casella in alto a destra e' gia' occupata? In quali si rientra dal lato opposto?
2. Perche' per la riga sopra si scrive `_i - 1 + _n` e non semplicemente `_i - 1`? Rivedete F8.
3. Aggiungete al programma un controllo che calcola le somme di tutte le righe, di tutte le colonne e delle due diagonali, e stampa `Il quadrato e' magico` se sono tutte uguali. Provate con $n = 5$, $7$ e $9$. Quanto vale la somma comune? Sapreste ricavare la formula $\frac{n(n^2 + 1)}{2}$? Suggerimento: quanto vale la somma di tutti i numeri da $1$ a $n^2$?
4. **Con gdb.** Con $n = 5$, mettete un breakpoint sulla riga `q[i][j] = k;` con la condizione `if k == 6`: in quale casella va il $6$? Perche' non va in alto a destra del $5$?

**H17.** Su una griglia di `R` righe e `C` colonne si parte dalla casella in alto a sinistra e ci si muove solo verso destra o verso il basso. In quanti modi si puo' arrivare in ciascuna casella? Nella prima riga e nella prima colonna c'e' un solo cammino; in ogni altra casella si arriva o da sopra o da sinistra, quindi i cammini sono la somma di quelli delle due caselle.

```text
INIZIO
    PER _i DA 0 A _R - 1
        PER _j DA 0 A _C - 1
            SE _i = 0 O _j = 0 ALLORA
                ASSEGNA a _p[_i][_j] il valore 1
            ALTRIMENTI
                ASSEGNA a _p[_i][_j] il valore _p[_i - 1][_j] + _p[_i][_j - 1]
            FINE
        FINE
    FINE
    VISUALIZZA _p
FINE
```

Con `#define R 6` e `#define C 6`, e la stampa con `%6d`:

```text
     1     1     1     1     1     1
     1     2     3     4     5     6
     1     3     6    10    15    21
     1     4    10    20    35    56
     1     5    15    35    70   126
     1     6    21    56   126   252
```

1. Ritrovate nella matrice il triangolo di Tartaglia di F10: dove stanno le righe del triangolo? Quale coefficiente binomiale e' `p[i][j]`?
2. Ora alcune caselle sono bloccate, e da li' non si puo' passare. La griglia e' scritta in una matrice di caratteri, con `#` per le caselle bloccate:

```c
char g[R][C] = {
    {'.', '.', '.', '.', '.'},
    {'.', '#', '.', '#', '.'},
    {'.', '.', '.', '.', '.'},
    {'#', '.', '#', '.', '.'},
    {'.', '.', '.', '.', '.'}
};
```

(con `R` e `C` uguali a $5$). In una casella bloccata i cammini sono $0$; nella casella di partenza sono $1$; in ogni altra casella sono la somma dei cammini della casella sopra (se esiste) e di quella a sinistra (se esiste). Modificate il programma: in quanti modi si arriva in basso a destra? (Devono essere $8$.) Per sommare "la casella sopra, se esiste" potete usare l'operatore ternario: `(i > 0 ? p[i - 1][j] : 0)`.
3. Senza caselle bloccate, portate `R` e `C` a $18$ e stampate solo l'ultimo elemento: e' giusto? Il valore esatto e' $\binom{34}{17} = 2333606220$. Rivedete E10 e la tabella dei tipi del Pacchetto F, e correggete il programma.

**H18.** Il determinante di una matrice quadrata si puo' calcolare con l'eliminazione di Gauss: con delle sottrazioni tra righe, che non cambiano il determinante, si rende la matrice triangolare superiore (H9), e a quel punto il determinante e' il prodotto degli elementi della diagonale. Ogni scambio di due righe cambia il segno del determinante.

```text
INIZIO
    LEGGI _n e gli elementi della matrice _a, riga per riga
    ASSEGNA a _det il valore 1
    PER _k DA 0 A _n - 1
        ASSEGNA a _p il valore _k
        FINCHE' _p < _n E _a[_p][_k] = 0
            ASSEGNA a _p il valore _p + 1
        FINE
        SE _p = _n ALLORA
            ASSEGNA a _det il valore 0
            ESCI DAL CICLO
        FINE
        SE _p diverso da _k ALLORA
            scambia la riga _p e la riga _k di _a
            ASSEGNA a _det il valore -_det
        FINE
        PER _i DA _k + 1 A _n - 1
            ASSEGNA a _f il valore _a[_i][_k] / _a[_k][_k]
            PER _j DA _k A _n - 1
                ASSEGNA a _a[_i][_j] il valore _a[_i][_j] - _f x _a[_k][_j]
            FINE
        FINE
        ASSEGNA a _det il valore _det x _a[_k][_k]
    FINE
    VISUALIZZA _det
FINE
```

Usate variabili `double` per la matrice, per `_det` e per `_f`; `_n` va da $1$ a `MAX`, che vale $10$, controllato con un `do while`. "Scambia la riga `_p` e la riga `_k`" significa scambiare, per ogni colonna `j`, gli elementi `a[p][j]` e `a[k][j]`.

```text
Dimensione (da 1 a 10): 3
2 1 3
0 -1 4
1 2 5
Determinante = -19.000000
```

1. Controllate il risultato dell'esempio con la regola di Sarrus. Poi provate con la matrice `0 1 2`, `1 0 3`, `4 -3 8`: il risultato deve essere $-2$. Perche' qui serve uno scambio di righe?
2. La terza riga della matrice `3 7 2`, `5 1 4`, `8 8 6` e' la somma delle prime due, quindi il determinante e' $0$. Che cosa stampa il programma? Stampate il determinante con `%.20f` e spiegate che cosa e' successo (rivedete F1, domanda 5).
3. **Con time.** Copiate il programma in `determinante_tempo.c`, con la matrice dichiarata prima di `main` e grande $N \times N$ (con `#define N`), riempita con `srand(1)` e `rand() % 10` al posto della lettura. Misurate il tempo con $N = 400$, $800$ e $1600$: per quanto si moltiplica il tempo quando $N$ raddoppia? Perche'? Non preoccupatevi se il determinante stampato e' `inf` (E13): e' un numero troppo grande per un `double`.
4. **Con gprof.** Con $N = 800$, quale riga occupa quasi tutto il tempo?

**H19.** I numeri di Fibonacci si possono calcolare con le potenze della matrice $Q = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$: si dimostra (per induzione) che $Q^n = \begin{pmatrix} F(n+1) & F(n) \\ F(n) & F(n-1) \end{pmatrix}$. L'algoritmo parte dalla matrice identita' e la moltiplica $n$ volte per $Q$.

```text
INIZIO
    LEGGI _n
    ASSEGNA a _P la matrice identita' 2 x 2
    PER _t DA 1 A _n
        ASSEGNA a _S il prodotto _P x _Q
        ASSEGNA a _P il valore _S
    FINE
    VISUALIZZA _P[0][1]
    VISUALIZZA _P[0][0] x _P[1][1] - _P[0][1] x _P[1][0]
FINE
```

Usate matrici `long` $2 \times 2$; il prodotto si calcola con i tre cicli di H5, e "assegna a `_P` il valore `_S`" va fatto elemento per elemento, con due cicli.

```text
Inserisci n: 10
F(10) = 55
Determinante di Q^10 = 1
```

1. Verificate che il programma dia gli stessi numeri di E17 per $n$ da $1$ a $10$.
2. Il determinante di $Q$ vale $-1$, e il determinante di un prodotto e' il prodotto dei determinanti. Quanto vale allora il determinante di $Q^n$? Confrontate con l'identita' di Cassini di E17.
3. Fino a quale $n$ il programma stampa $F(n)$ giusto? Confrontate con E10, dove con gli `int` ci si fermava a $F(46)$. Attenzione: anche quando i numeri diventano sbagliati, il determinante stampato continua a valere $1$ o $-1$, quindi non e' un controllo affidabile.

**H20.** **Sfida.** Nel 1963 il matematico Stanislaw Ulam, durante una conferenza noiosa, scrisse i numeri interi lungo una spirale e cerchio' i numeri primi: con sua sorpresa, i primi tendevano a disporsi lungo delle linee diagonali. Il programma riempie una matrice $N \times N$, con $N$ dispari, mettendo $1$ al centro e proseguendo a spirale in senso antiorario: un passo a destra, uno in su, due a sinistra, due in giu', tre a destra, tre in su, e cosi' via.

```text
INIZIO
    ASSEGNA a _i il valore _N / 2
    ASSEGNA a _j il valore _N / 2
    ASSEGNA a _k il valore 1
    ASSEGNA a _u[_i][_j] il valore 1
    ASSEGNA a _lato il valore 1
    ASSEGNA a _dir il valore 0
    FINCHE' _k < _N x _N
        PER _volta DA 1 A 2
            PER _passo DA 1 A _lato
                SE _k < _N x _N ALLORA
                    ASSEGNA a _i il valore _i + _di[_dir]
                    ASSEGNA a _j il valore _j + _dj[_dir]
                    ASSEGNA a _k il valore _k + 1
                    ASSEGNA a _u[_i][_j] il valore _k
                FINE
            FINE
            ASSEGNA a _dir il valore del resto di _dir + 1 diviso 4
        FINE
        ASSEGNA a _lato il valore _lato + 1
    FINE
FINE
```

La direzione `_dir` vale $0$ per destra, $1$ per su, $2$ per sinistra e $3$ per giu'; i due array `int di[4] = {0, -1, 0, 1};` e `int dj[4] = {1, 0, -1, 0};` dicono di quanto cambiano la riga e la colonna con un passo in quella direzione. Con $N = 5$ e la stampa con `%4d` si ottiene:

```text
  17  16  15  14  13
  18   5   4   3  12
  19   6   1   2  11
  20   7   8   9  10
  21  22  23  24  25
```

1. Controllate la spirale con $N = 5$. Perche' serve il controllo `SE _k < _N x _N`? Che cosa succederebbe senza, nell'ultimo tratto?
2. Su quale diagonale si trovano i quadrati dei numeri dispari, $1, 9, 25, \dots$? Perche'?
3. Ora la spirale di Ulam: segnate in un array `primo` i numeri primi fino a $N^2$ con il crivello di F16, e stampate la matrice con un carattere per casella, `#` se il numero e' primo e `.` altrimenti, senza spazi. Provate con $N = 41$: vedete le diagonali? (Gli array di questo esercizio sono piccoli: possono restare dentro `main`.)

### Riepilogo di time e gprof

| Comando | Cosa fa | Visto in |
| --- | --- | --- |
| `./prog < dati.txt` | il programma legge `dati.txt` come se lo scriveste da tastiera | G1 |
| `time ./prog` | esegue il programma e alla fine stampa i tempi `real`, `user` e `sys` | G1 |
| `./prog1; ./prog2` | esegue due comandi uno dopo l'altro | G2 |
| `gcc -O2` | compila con le ottimizzazioni; senza indicazioni gcc usa `-O0`, il livello adatto a gdb | G8 |
| `gcc -pg` | prepara il programma per gprof: eseguendolo si crea il file `gmon.out` | H6 |
| `gprof -b -l ./prog gmon.out` | mostra quanta parte del tempo occupa ciascuna riga | H6 |


## Pacchetto I: Le funzioni e la documentazione

Fino a qui ogni programma e' stato un `main` unico, che faceva tutto: leggere, calcolare, stampare. Da qui in avanti impariamo a spezzarlo in **funzioni**, cioe' pezzi di programma con un nome, che ricevono dei valori e ne restituiscono uno. In questo pacchetto le usiamo in lungo e in largo, e impariamo a corredarle di una cosa che a prima vista sembra superflua: la loro **documentazione**. Chi scrive una funzione la capisce mentre la scrive; chi la usa un mese dopo, o chi la usa senza averla scritta, ha bisogno di sapere che cosa fa, che cosa vuole e che cosa restituisce, senza dover leggere il codice. Per questo esistono regole fisse su come scrivere quel commento, e noi useremo le piu' diffuse nel mondo del C: quelle di **Doxygen**.

### Le funzioni, in breve

```c
#include <stdio.h>

int quadrato(int x) {               /* riceve un int, che dentro si chiama x, e restituisce un int */
    return x * x;
}

int main(void) {
    int a = 7;
    printf("%d\n", quadrato(a) + quadrato(3));   /* stampa 58 */
    return 0;
}
```

- La prima riga della funzione dice il tipo del valore restituito (`int`), il nome (`quadrato`) e, tra parentesi, i *parametri*, ciascuno con il suo tipo.
- `return` termina subito la funzione e restituisce il valore. Una funzione che non restituisce niente si dichiara `void` e non ha `return` (oppure ha un `return;` senza valore).
- I parametri sono **copie**: se la funzione cambia `x`, la variabile `a` di `main` non cambia.
- Le variabili dichiarate dentro una funzione esistono solo li', e nascono e muoiono a ogni chiamata.
- Una funzione puo' chiamarne un'altra, e il risultato di una chiamata puo' essere usato come valore (`int y = quadrato(3);`) oppure come argomento di un'altra chiamata (`quadrato(quadrato(3))`).
- `main` e' una funzione come le altre: riceve `void` e restituisce un `int`, il codice di uscita che avete usato nel Pacchetto B.

### I prototipi

Il compilatore legge il file dall'alto in basso: quando incontra `quadrato(a)` dentro `main`, deve gia' sapere che cosa e' `quadrato`. Ci sono due modi.

- Scrivere la funzione **prima** di `main`, come nell'esempio qui sopra.
- Scrivere prima solo il **prototipo**, cioe' la riga d'intestazione seguita da `;`, e rimandare il corpo dopo `main`:

```c
#include <stdio.h>

int quadrato(int x);          /* prototipo: attenzione al ; */

int main(void) {
    printf("%d\n", quadrato(7));
    return 0;
}

int quadrato(int x) {         /* definizione */
    return x * x;
}
```

Il secondo modo e' comodo quando le funzioni sono tante: in cima al file si vede l'elenco di tutto quello che il programma sa fare. In questo pacchetto useremo i prototipi quasi sempre.

### Passare un array a una funzione

Un array si passa scrivendo `[]` dopo il nome del parametro, e **il numero di elementi va passato a parte**: dentro la funzione non c'e' nessun modo di sapere quanto e' lungo `v`.

```c
double media(int v[], int n) {
    int i;
    double somma = 0;
    for (i = 0; i < n; i++) {
        somma += v[i];
    }
    return somma / n;
}
```

C'e' pero' una differenza importante rispetto agli altri parametri: **l'array non viene copiato**. La funzione lavora proprio sull'array del chiamante, quindi se lo modifica, la modifica resta anche dopo il `return`. Lo vedrete in I7.

Capitera' di vedere il prototipo di una funzione che riceve un array scritto cosi': `void printfv(float *, int);`. Le due forme, `float *v` e `float v[]`, sono lo stesso parametro scritto in due modi: noi useremo sempre la seconda, che si legge piu' facilmente. (Il perche' siano la stessa cosa lo capirete studiando i puntatori.)

### Documentare con Doxygen

Doxygen e' un programma che legge i file sorgente, raccoglie i commenti scritti in un formato preciso e ne ricava un sito consultabile. A noi, per ora, non interessa generare il sito: ci interessa il **formato**, perche' e' lo stesso che trovate in quasi tutto il codice C scritto da altri, e perche' obbliga a dire le tre cose che servono davvero.

```c
/**
 * @brief Calcola la media dei primi n elementi di un array.
 *
 * @param v Array di interi.
 * @param n Numero di elementi da considerare; deve essere maggiore di zero.
 * @return La media aritmetica dei primi n elementi di v.
 */
double media(int v[], int n) {
    /* ... */
}
```

Le regole sono poche:

- il blocco si apre con `/**` (due asterischi, non uno) e si chiude con `*/`, e sta **subito sopra** la funzione, senza righe vuote in mezzo;
- `@brief` e' una frase sola che dice **che cosa fa** la funzione, non come la fa;
- c'e' un `@param` per ogni parametro, con lo stesso nome che compare nell'intestazione, e dice che cosa rappresenta e quali valori sono ammessi;
- `@return` dice che cosa viene restituito. Su una funzione `void` non si scrive.

Due aggiunte facoltative, che useremo quando servono: `@pre` per una condizione che chi chiama deve garantire, e `@note` per un'avvertenza. Nel codice altrui troverete anche `\brief` e `\param` con la barra rovesciata: e' esattamente la stessa cosa.

Per vedere che aspetto ha una documentazione vera, generata da Doxygen a partire da commenti come questi, guardate la [documentazione di LAPACK](https://netlib.org/lapack/explore-html/), una libreria di algebra lineare usata in tutto il mondo scientifico; la pagina `dgesv.f` e la corrispondente [pagina del sorgente](https://netlib.org/lapack/explore-html/d8/d72/dgesv_8f_source.html) mostrano lo stesso testo prima e dopo. Le regole complete stanno nel [manuale di Doxygen](https://doxygen.nl/manual/docblocks.html).

### gdb e le funzioni

Tre comandi che da ora in poi servono spesso.

| Comando | Che cosa fa |
| --- | --- |
| `break media` | ferma il programma all'inizio della funzione `media`, tutte le volte che viene chiamata |
| `bt` | *backtrace*: mostra la catena delle chiamate, dalla funzione in cui vi trovate fino a `main` |
| `finish` | esegue il resto della funzione, torna al chiamante e stampa il valore restituito |

### Esercizi (I1-I10)

#### Leggere la documentazione

I primi tre esercizi non chiedono di scrivere programmi, ma di leggere. Rispondete su carta e poi, se volete, controllate scrivendo il codice.

**I1.** Qui sotto ci sono tre funzioni di cui conoscete solo il prototipo e la documentazione: il corpo non c'e', e non serve.

```c
/**
 * @brief Calcola il numero di giorni di un mese.
 *
 * @param mese Numero del mese, da 1 a 12.
 * @param anno Anno a cui il mese appartiene; deve essere maggiore di zero.
 * @return Il numero di giorni del mese indicato: 31 per gennaio, marzo, maggio,
 *         luglio, agosto, ottobre e dicembre; 30 per aprile, giugno, settembre
 *         e novembre; 28 per febbraio, che pero' ne ha 29 negli anni bisestili,
 *         cioe' quelli divisibili per 4, esclusi quelli divisibili per 100 ma
 *         non per 400.
 */
int giorni_del_mese(int mese, int anno);

/**
 * @brief Calcola il resto della divisione di a per b, sempre non negativo.
 *
 * @param a Dividendo.
 * @param b Divisore; deve essere maggiore di zero.
 * @return L'unico numero r, con 0 <= r < b, tale che a - r sia un multiplo di b.
 * @note L'operatore % del C da' un risultato diverso quando a e' negativo:
 *       -7 % 3 vale -1.
 */
int resto_positivo(int a, int b);

/**
 * @brief Conta gli elementi di un array maggiori di una soglia.
 *
 * @param v Array di interi.
 * @param n Numero di elementi di v da esaminare; deve essere maggiore di zero.
 * @param soglia Valore con cui confrontare gli elementi.
 * @return Quanti, tra i primi n elementi di v, sono strettamente maggiori di soglia.
 */
int conta_maggiori(int v[], int n, int soglia);
```

1. Completate la tabella leggendo solo i prototipi.

| Funzione | Quanti parametri | Tipo del valore restituito |
| --- | --- | --- |
| `giorni_del_mese` |  |  |
| `resto_positivo` |  |  |
| `conta_maggiori` |  |  |

2. Quanto valgono `giorni_del_mese(2, 1900)`, `giorni_del_mese(2, 2000)` e `giorni_del_mese(4, 2026)`? La documentazione basta per rispondere a tutte e tre?
3. Quanto valgono `resto_positivo(7, 3)`, `resto_positivo(-7, 3)` e `resto_positivo(-6, 3)`? Per ciascuno controllate che il risultato rispetti **entrambe** le condizioni scritte in `@return`.
4. Con `int v[5] = {3, 12, 10, 40, 7};`, quanto valgono `conta_maggiori(v, 5, 10)`, `conta_maggiori(v, 3, 10)` e `conta_maggiori(v, 5, 40)`? Attenzione alla parola *strettamente*.
5. Ogni funzione ha almeno un parametro con una condizione che chi chiama deve rispettare: elencatele. Che cosa promette la documentazione se la condizione non viene rispettata, per esempio con `resto_positivo(7, 0)`?

**In piu'.** Aprite la [documentazione di LAPACK](https://netlib.org/lapack/explore-html/) e cercate la routine `dgesv`, che risolve un sistema lineare. Trovate l'elenco dei parametri e il loro significato, poi aprite la pagina del sorgente: riconoscete i `\brief` e i `\param[in]` da cui quella pagina e' stata generata? (Il codice e' scritto in Fortran, un altro linguaggio: guardate soltanto i commenti in cima, che sono quello che ci interessa.)

**I2.** Il programma qui sotto contiene quattro funzioni gia' scritte e documentate, ma non il `main`. Scrivetelo voi, leggendo **solo** i blocchi di documentazione: il corpo delle funzioni serve a far funzionare il programma, e potete coprirlo con un foglio.

```c
#include <stdio.h>

/**
 * @brief Conta le cifre di un numero.
 *
 * @param n Numero di cui contare le cifre; deve essere maggiore di zero.
 * @return Quante cifre ha n scritto in base dieci.
 */
int cifre(int n) {
    int c = 0;
    do {
        c++;
        n /= 10;
    } while (n != 0);
    return c;
}

/**
 * @brief Somma le cifre di un numero.
 *
 * @param n Numero di cui sommare le cifre; deve essere maggiore di zero.
 * @return La somma delle cifre di n scritto in base dieci.
 */
int somma_cifre(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

/**
 * @brief Dice se un numero e' primo.
 *
 * @param n Numero da controllare.
 * @return 1 se n e' primo, 0 altrimenti. I numeri minori di 2 non sono primi.
 */
int e_primo(int n) {
    int i;
    if (n < 2) {
        return 0;
    }
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

/**
 * @brief Rovescia le cifre di un numero.
 *
 * @param n Numero da rovesciare; deve essere maggiore di zero.
 * @return Il numero ottenuto leggendo le cifre di n da destra a sinistra.
 */
int inverti(int n) {
    int r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}
```

Il `main` legge un numero intero positivo e stampa, in quest'ordine: quante cifre ha, la somma delle cifre, se e' primo, il numero rovesciato e se e' palindromo (cioe' se si legge uguale nei due versi). Per le due righe che finiscono con `si` o `no` servono un `if` e un `else`, con una `printf` per ramo.

```text
Inserisci un numero positivo: 1234
Cifre: 4
Somma delle cifre: 10
E' primo: no
Rovesciato: 4321
E' palindromo: no
```

```text
Inserisci un numero positivo: 131
Cifre: 3
Somma delle cifre: 5
E' primo: si
Rovesciato: 131
E' palindromo: si
```

1. Per rispondere all'ultima domanda non c'e' una funzione apposta: quale avete usato, e con che confronto?
2. Nessuna delle quattro funzioni stampa niente: tutte le `printf` stanno nel `main`. Perche' e' una buona idea? Pensate a che cosa succederebbe se voleste usare `somma_cifre` dentro un altro programma che non deve stampare nulla.
3. Aggiungete una riga che stampa la somma delle cifre del numero rovesciato. Quante chiamate servono, e in che ordine? Provate con qualche numero: che cosa notate rispetto alla somma delle cifre di partenza, e perche'?
4. Tutte e quattro le funzioni chiedono `n` maggiore di zero. Che cosa restituisce `cifre(0)`? E `somma_cifre(0)`? Sono d'accordo tra loro? (Non e' un errore del programma: fuori dal contratto, la documentazione non promette niente.)

**I3.** In ciascuno dei tre casi la documentazione e il codice non dicono la stessa cosa. **La documentazione e' il contratto gia' concordato: e' il codice a dover cambiare.**

```c
/**
 * @brief Restituisce il piu' grande tra due interi.
 *
 * @param a Primo intero.
 * @param b Secondo intero.
 * @return Il maggiore tra a e b; se sono uguali, quel valore.
 */
int massimo(int a, int b) {
    if (a > b) {
        return b;
    }
    return a;
}
```

```c
/**
 * @brief Somma i primi n elementi di un array.
 *
 * @param v Array di interi.
 * @param n Numero di elementi da sommare; deve essere maggiore di zero.
 * @return La somma di v[0], v[1], ..., v[n-1].
 */
int somma(int v[], int n) {
    int i, s = 0;
    for (i = 0; i <= n; i++) {
        s += v[i];
    }
    return s;
}
```

```c
/**
 * @brief Dice se un numero e' pari.
 *
 * @param n Numero da controllare.
 * @return 1 se n e' pari, 0 se e' dispari.
 */
int pari(int n) {
    return n % 2;
}
```

Per provare la seconda funzione usate questo `main`, che secondo la documentazione deve stampare $10$:

```c
int main(void) {
    int v[4] = {1, 2, 3, 4};
    printf("somma = %d\n", somma(v, 4));
    return 0;
}
```

1. Per ciascuna funzione, scrivete in una riga che cosa promette la documentazione e che cosa fa invece il codice.
2. Per ciascuna, indicate una chiamata che mostra la differenza, con il valore promesso e quello ottenuto. Per la seconda, eseguite il `main` qui sopra tre o quattro volte di fila: stampa sempre lo stesso numero? Che cosa sta sommando, oltre ai quattro elementi dell'array? (Puo' anche capitare che stampi proprio $10$: una somma giusta per caso non vuol dire che la funzione sia giusta.)
3. Correggete i tre corpi perche' rispettino la documentazione, poi scrivete un `main` che li prova.
4. **In piu'.** Prima della correzione, quanto vale `pari(-3)`? Non e' ne' $1$ ne' $0$: perche'? (La risposta sta nella `@note` di `resto_positivo`, che avete letto in I1: in C il resto di un numero negativo e' negativo.)

#### Scrivere le prime funzioni

**I4.** Scrivete `massimo.c`, che legge tre numeri interi e stampa il piu' grande. Il programma contiene due funzioni. La prima e' `int massimo(int a, int b)`, scritta cosi':

```c
int massimo(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}
```

La seconda e' `int massimo3(int a, int b, int c)`, che restituisce il maggiore tra tre e **non contiene nessun `if`**, perche' si appoggia soltanto a `massimo`. Mettete i due prototipi prima di `main` e le due definizioni dopo.

```text
Inserisci tre numeri interi: 4 9 2
Il massimo e' 9
```

1. Scritto cosi', `massimo3` chiama `massimo` esattamente due volte: scrivete la riga del `return`. Confrontatela con la soluzione che non usa funzioni, dove il massimo tra tre numeri si ottiene con due `if` annidati e quattro rami: quante righe risparmiate?
2. Aggiungete `int massimo4(int a, int b, int c, int d)`, anch'essa senza `if`, che usa `massimo3` e `massimo`. Quante chiamate a `massimo` avvengono in tutto quando il `main` chiama `massimo4`?
3. Con i tre numeri uguali, per esempio `5 5 5`, il programma stampa $5$. Guardando il corpo di `massimo` scritto qui sopra, quando `a` e `b` sono uguali viene restituito `a` o `b`? E se il confronto fosse `a >= b`? Il valore stampato cambierebbe?
4. **Con gdb.** Compilate con `-g` e aprite gdb. Mettete `break massimo`, lanciate `run` e inserite i tre numeri: il programma si ferma. Date `bt`: quante righe vedete, e in che ordine? Date `finish`: che valore stampa gdb? Poi `continue`: dove si ferma la seconda volta?

**I5.** Scrivete `primi_speciali.c`, che legge un numero `n` e stampa tutti i numeri primi da $2$ a `n` la cui somma delle cifre e' a sua volta un numero primo, separati da uno spazio, e infine quanti sono. Il programma ha due funzioni, `int e_primo(int n)` e `int somma_cifre(int n)`, con i prototipi prima di `main`.

```text
Fino a quale numero? 50
2 3 5 7 11 23 29 41 43 47
Quanti: 10
```

1. Scrivete la condizione dell'`if` dentro il ciclo del `main`: `e_primo` vi compare due volte, con quali argomenti? Contate poi, con una variabile, quante volte viene chiamata in tutto fino a $50$: sono $64$ e non $98$, perche' quando la prima condizione di un `&&` e' falsa la seconda non viene nemmeno calcolata (lo avete visto in G17).
2. Che cosa deve restituire `e_primo(1)`? E `e_primo(0)`? In I2 avete letto il contratto di una funzione con lo stesso nome, che su questo punto e' esplicito: adottate la stessa convenzione, scrivetela in un commento sopra la funzione (in I8 quel commento diventera' documentazione vera) e controllate che il vostro codice la rispetti davvero, provando i due valori.
3. Il ciclo di `e_primo` si ferma quando `i * i > n` invece di arrivare fino a `n - 1`. Perche' e' corretto? Con $n = 97$, quanti giri fa il ciclo nei due casi?
4. Fino a $100$ i numeri stampati sono $14$. Verificatelo, e controllate a mano che $61$ e $67$ siano nell'elenco mentre $59$ e $71$ no.

**I6.** Scrivete `potenza.c` con due funzioni: `int moltiplica(int a, int b)`, che calcola il prodotto usando **soltanto** l'addizione e un ciclo `for`, e `int potenza(int base, int esp)`, che calcola la potenza usando **soltanto** `moltiplica`. Il `main` legge due numeri interi non negativi (controllati con un `do while`) e stampa il prodotto e le due potenze.

```text
Due numeri interi non negativi: 3 4
3 x 4 = 12
3^4 = 81
4^3 = 64
```

1. In `moltiplica(a, b)` il ciclo gira `b` volte e ogni giro fa un'addizione. Quante addizioni fa `moltiplica(3, 4)`? E quante ne fa in tutto il calcolo di `potenza(3, 4)`, se `potenza` e' scritta come `r = moltiplica(r, base);` ripetuto `esp` volte? Verificate contando le addizioni con una variabile dichiarata **fuori da tutte le funzioni**, che `moltiplica` aumenta di uno a ogni giro e il `main` stampa alla fine. Una variabile scritta li' e' vista da tutte le funzioni del file e si chiama *globale*: l'avete gia' incontrata in H6, per gli array grandi, e nel Pacchetto J vedrete per bene quando conviene e quando fa danni.
2. Quanto restituisce `moltiplica(5, 0)`? E `potenza(5, 0)`? Dentro le due funzioni la variabile del risultato parte da valori diversi, $0$ e $1$: spiegate perche', partendo dalle due risposte precedenti.
3. Con `b` negativo il ciclo di `moltiplica` non parte nemmeno: che cosa restituisce? E' il motivo per cui il `main` deve rifiutare i numeri negativi.
4. **In piu'.** Provate `potenza(3, 20)`: il risultato e' $-808182895$, cioe' negativo. Quanto vale davvero $3^{20}$? Confrontate con `INT_MAX` e ripensate a F2.

**I7.** Scrivete `vettore_funzioni.c`, che legge $10$ numeri interi in un array `int v[N]` (con `#define N 10`) e usa quattro funzioni:

- `void stampa(int v[], int n)`, che stampa gli elementi separati da uno spazio e poi va a capo;
- `double media(int v[], int n)`, che restituisce la media;
- `int minimo(int v[], int n)`, che restituisce l'elemento piu' piccolo;
- `void raddoppia(int v[], int n)`, che moltiplica per due ogni elemento e non restituisce niente.

Il `main` stampa l'array, la media con due decimali e il minimo, poi chiama `raddoppia` e stampa di nuovo l'array.

```text
Inserisci 10 numeri interi: 3 1 4 1 5 9 2 6 5 3
Array: 3 1 4 1 5 9 2 6 5 3
Media: 3.90
Minimo: 1
Dopo raddoppia: 6 2 8 2 10 18 4 12 10 6
```

1. `raddoppia` e' `void` e non restituisce niente, eppure l'array stampato dopo e' cambiato. Una funzione `scambia` che riceve due `int`, invece, non riesce a scambiare le variabili del chiamante, e in I12 lo vedrete succedere. Qual e' la differenza tra i due casi? (La risposta e' nel riquadro sugli array: una delle due cose viene copiata, l'altra no.)
2. Dentro `media`, la variabile che accumula la somma e' un `double`. Provate a dichiararla `int`: con questi dieci numeri il programma stampa `3.00` invece di `3.90`. Perche'? (E' lo stesso inciampo di I14.)
3. Togliete il parametro `n` da `minimo` e usate direttamente `N` dentro la funzione: il programma continua a funzionare. Perche' e' comunque una cattiva idea? Pensate a che cosa succede se nello stesso programma volete il minimo di un array di $5$ elementi.
4. **In piu'.** Stampate `(int) sizeof(v)` dentro `main` e dentro `stampa`: in `main` vale $40$, nella funzione $8$. Compilate con `-Wall`: gcc vi avverte con un messaggio che contiene `will return size of 'int *'`. L'array non viene copiato, alla funzione arriva solo l'indicazione di dove si trova, e quella occupa $8$ byte: ecco perche' `n` va passato a parte.

#### Scrivere la documentazione

**I8.** Tornate sulle funzioni che avete scritto in I4, I5 e I6 e aggiungete a ciascuna il blocco Doxygen: `massimo`, `massimo3`, `massimo4`, `e_primo`, `somma_cifre`, `moltiplica`, `potenza`. Ecco il modello, gia' fatto per una di loro:

```c
/**
 * @brief Calcola il prodotto di due interi usando solo l'addizione.
 *
 * @param a Primo fattore.
 * @param b Secondo fattore; deve essere maggiore o uguale a zero.
 * @return Il prodotto a * b.
 */
int moltiplica(int a, int b) {
    /* ... */
}
```

Quando usate i prototipi, il blocco va messo **sopra il prototipo**, in cima al file: e' li' che lo cerca chi vuole usare la funzione senza leggerne il corpo.

1. In I5 avete deciso che cosa deve restituire `e_primo(1)`. Scrivetelo adesso in `@return`, in modo che un lettore lo sappia senza provare.
2. In `moltiplica` la condizione su `b` non e' un capriccio: che cosa succede se qualcuno chiama `moltiplica(5, -2)`? Un lettore che ha solo la documentazione sa di non doverlo fare?
3. Il `@brief` deve dire *che cosa fa*, non *come*. Riscrivete questi due in modo corretto: "Calcola la potenza con un ciclo che moltiplica esp volte" e "Controlla n % i per ogni i da 2 fino alla radice".
4. Scambiate il file con un compagno e provate a usare le sue funzioni leggendo solo i blocchi `/** */`. Dove vi siete dovuti fermare a guardare il codice? Quella e' esattamente la riga che manca nella documentazione.

**I9.** Questa volta si scrive prima il contratto e poi il codice. Ecco tre funzioni descritte a parole:

- una funzione che dice se un intero e' un quadrato perfetto;
- una funzione che conta quante volte un valore compare tra i primi `n` elementi di un array;
- una funzione che, dati due interi, stampa a schermo la divisione con resto nella forma `17 = 5 x 3 + 2`, e non restituisce niente.

**Primo passo:** scrivete solo il blocco Doxygen e il prototipo di ciascuna, senza una riga di codice. **Secondo passo:** scrivete i corpi, rispettando quello che avete promesso. **Terzo passo:** scrivete il `main` che le prova, usando l'array `int v[8] = {3, 1, 4, 1, 5, 9, 2, 6};` e contando le occorrenze del valore $1$.

```text
Inserisci un numero: 49
49 e' un quadrato perfetto
Occorrenze di 1 nell'array: 2
Inserisci due numeri: 17 5
17 = 5 x 3 + 2
```

```text
Inserisci un numero: 50
50 non e' un quadrato perfetto
Occorrenze di 1 nell'array: 2
Inserisci due numeri: 20 4
20 = 4 x 5 + 0
```

1. Sulla terza funzione non si scrive `@return`: perche'? E qual e' il suo tipo?
2. Due casi limite non compaiono negli esempi: che cosa deve fare la prima funzione con un numero negativo, e la terza se il secondo numero e' zero? Non c'e' una risposta unica: scegliete voi, ma decidete **prima** di scrivere il codice, mettete la scelta nella documentazione e poi scrivete il codice che la rispetta. Quello che conta non e' quale scelta fate, ma che codice e documentazione dicano la stessa cosa.
3. Durante il secondo passo avete dovuto tornare indietro a cambiare la documentazione? Per quale funzione, e che cosa vi era sfuggito mentre la scrivevate?

**I10.** Mettiamo insieme tutto. Scrivete `statistiche.c`, che legge $10$ numeri interi e dice quanti stanno sopra la media. Il programma e' diviso in quattro funzioni documentate, e `main` non contiene nessun ciclo:

- `void leggi(int v[], int n)`, che riempie l'array leggendo da tastiera;
- `void stampa(int v[], int n)`, come in I7;
- `double media(int v[], int n)`, come in I7;
- `int conta_sopra(int v[], int n, double soglia)`, che conta gli elementi strettamente maggiori di `soglia`.

```text
Inserisci 10 numeri interi: 3 1 4 1 5 9 2 6 5 3
Array: 3 1 4 1 5 9 2 6 5 3
Media: 3.90
Sopra la media: 5
```

1. Elencate in ordine le funzioni che `main` chiama. Questo modo di procedere si chiama progettazione *top-down*: si parte dal problema grande, lo si spezza in sottoproblemi piu' semplici e si da' a ciascuno la sua funzione, finche' ognuna e' abbastanza piccola da scriversi in poche righe. Qual e' qui il problema di partenza, e quali i sottoproblemi?
2. `conta_sopra` riceve la soglia come parametro invece di calcolare la media al suo interno. Scrivete le due righe del `main` che la usano, poi spiegate che cosa potete fare con questa versione e non potreste fare con l'altra. (Suggerimento: provate a contare quanti elementi superano $4.5$.)
3. `leggi` riempie l'array e non restituisce niente, esattamente come `raddoppia` in I7. Funziona per lo stesso motivo: quale?
4. **Con gdb.** In gdb mettete `break conta_sopra`, lanciate il programma e, quando si ferma, date `bt` e poi `print soglia`. gdb risponde `3.8999999999999999`: un `double` non riesce a contenere esattamente $3.9$, e `printf` con `%.2f` ve lo aveva nascosto arrotondando. Date poi `finish`: che numero restituisce la funzione?

### Trova l'errore (I11-I15)

Ogni programma contiene un errore. Trovatelo, correggetelo e dite se e' **sintattico** o **progettuale**, come nei pacchetti precedenti. (I15 fa eccezione: li' l'errore non sta nel codice, e capirete subito perche' non rientra in nessuna delle due categorie.) Compilate sempre con `gcc -g -Wall -Wextra` e leggete i messaggi; dove il compilatore tace, usate gdb con i comandi del riquadro.

**I11.** Il programma deve stampare il doppio del numero inserito. gcc dice qualcosa gia' senza flag, e con `-Wall -Wextra` lo ripete: leggete il messaggio, che contiene le parole `implicit declaration`. A seconda della versione di gcc, il programma viene costruito lo stesso (fino a gcc 13) oppure non viene costruito affatto (da gcc 14 in poi, dove lo stesso problema e' diventato un errore).

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Inserisci un numero intero: ");
    scanf("%d", &n);
    printf("Il doppio di %d e' %d\n", n, doppio(n));
    return 0;
}

int doppio(int x) {
    return 2 * x;
}
```

1. Che cosa non sa il compilatore quando arriva alla riga della `printf`? Ricordate che legge il file dall'alto in basso.
2. Correggetelo in due modi diversi, entrambi descritti nel riquadro sui prototipi, e dite quale dei due preferite se il programma avesse venti funzioni.

**I12.** Il programma dovrebbe scambiare il contenuto di due variabili e stampare `x = 8, y = 3`. Invece stampa `x = 3, y = 8`: la funzione sembra giusta, ma non succede niente.

```c
#include <stdio.h>

void scambia(int a, int b) {
    int t;
    t = a;
    a = b;
    b = t;
}

int main(void) {
    int x = 3, y = 8;
    scambia(x, y);
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

1. Mettete una `printf` alla fine di `scambia` che stampa `a` e `b`: lo scambio li' dentro e' avvenuto o no? Allora che cosa e' andato perduto al `return`?
2. **Con gdb.** Mettete `break scambia`, poi `print x` e `print a`: che cosa risponde gdb al primo comando, e perche'?
3. Con quello che sapete, questa funzione non si puo' aggiustare cosi' com'e'. Riscrivetela nella forma `void scambia(int v[], int i, int j)`, che scambia due elementi di un array, e cambiate il `main` perche' usi un array di due elementi. Adesso funziona: che cosa e' cambiato? (Ripensate a I7.)

**I13.** La funzione deve restituire $1$ per i numeri positivi, $-1$ per i negativi e $0$ per lo zero, e il programma deve stampare `-1`, `0` e `1`. Stampa invece, al posto dello zero, un numero senza senso, che puo' anche cambiare da un computer all'altro. gcc lo dice chiaramente: il messaggio contiene `control reaches end of non-void function`.

```c
#include <stdio.h>

int segno(int n);

int main(void) {
    printf("segno(-5) = %d\n", segno(-5));
    printf("segno(0)  = %d\n", segno(0));
    printf("segno(7)  = %d\n", segno(7));
    return 0;
}

int segno(int n) {
    if (n > 0) {
        return 1;
    } else if (n < 0) {
        return -1;
    }
}
```

1. Seguite i tre casi con il dito: per quale valore di `n` l'esecuzione arriva in fondo alla funzione senza incontrare nessun `return`? Che cosa restituisce, allora?
2. Correggetelo, e scrivete il blocco Doxygen di `segno`: nel `@return` devono comparire tutti e tre i casi.
3. Perche' per le funzioni `void` questo errore non esiste?

**I14.** Il programma deve stampare la media dei cinque numeri, cioe' `Media: 2.80`. Stampa invece `Media: 2.00`, e gcc non dice una parola.

```c
#include <stdio.h>
#define N 5

double media(int v[], int n);

int main(void) {
    int v[N] = {3, 1, 4, 1, 5};
    printf("Media: %.2f\n", media(v, N));
    return 0;
}

double media(int v[], int n) {
    int i, somma = 0;
    for (i = 0; i < n; i++) {
        somma += v[i];
    }
    return somma / n;
}
```

1. Quanto vale `somma` alla fine del ciclo? Quanto vale l'espressione `somma / n` **prima** di essere trasformata in `double` dal `return`?
2. La funzione e' dichiarata `double` e il `return` restituisce davvero un `double`: perche' allora il valore e' sbagliato? In quale punto preciso si perde il resto della divisione?
3. Correggetelo in due modi: cambiando il tipo di `somma`, oppure lasciandolo `int` e modificando solo la riga del `return`. Verificate che entrambi diano `2.80`.
4. Il problema non c'entra con le funzioni: la stessa riga dentro `main` sbaglierebbe allo stesso modo. Che cosa aggiungono qui le funzioni, dal punto di vista di chi cerca l'errore? (Pensate a dove si guarda per primo quando una media e' sbagliata.)

**I15.** Questa volta il programma funziona: compila senza un fiato e stampa `3 9 6`, cioe' i multipli di tre contenuti nell'array. A essere sbagliata e' la documentazione.

```c
#include <stdio.h>
#define N 8

/**
 * @brief Conta i multipli di tre tra i primi n elementi di un array.
 *
 * @param vettore Array di interi da esaminare.
 * @param quanti Numero di elementi da esaminare.
 * @param divisore Numero di cui cercare i multipli.
 * @return Quanti elementi sono multipli di tre.
 */
void stampa_multipli(int v[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        if (v[i] % 3 == 0) {
            printf("%d ", v[i]);
        }
    }
    printf("\n");
}

int main(void) {
    int v[N] = {3, 1, 4, 1, 5, 9, 2, 6};
    stampa_multipli(v, N);
    return 0;
}
```

1. Elencate **tutti** i punti in cui la documentazione non corrisponde alla funzione: ce ne sono cinque. Guardate il verbo del `@brief`, i nomi dei `@param`, il numero dei `@param` e la presenza del `@return`.
2. Perche' gcc non segnala niente, nemmeno con `-Wall -Wextra`? Che differenza c'e' tra questo errore e quello di I11?
3. Riscrivete il blocco perche' descriva la funzione che c'e'.
4. **In piu'.** La strada opposta: tenete la documentazione e cambiate la funzione perche' la rispetti. Dovete scrivere `int conta_multipli(int v[], int n, int divisore)`, che non stampa niente e restituisce il conteggio, e adattare `main` perche' stampi il risultato. Con questo array e `divisore` uguale a $3$ deve stampare $3$; con `divisore` uguale a $5$, $1$. Quale delle due versioni e' piu' riutilizzabile?

### Dallo pseudocodice al C (I16-I20)

Lo pseudocodice sa descrivere anche i sottoprogrammi. La forma e' questa:

```text
SOTTOPROGRAMMA _massimo(_a, _b)
    SE _a > _b ALLORA
        RESTITUISCI _a
    FINE
    RESTITUISCI _b
FINE

INIZIO
    LEGGI _x e _y
    ASSEGNA a _m il valore _massimo(_x, _y)
    VISUALIZZA _m
FINE
```

I sottoprogrammi si scrivono prima dell'INIZIO, `RESTITUISCI` diventa `return` e la chiamata si scrive come in C. Come sempre: prima eseguite l'algoritmo a mano con i valori dell'esempio, poi scrivete il codice. Da qui in avanti ogni funzione che traducete va corredata del suo blocco Doxygen.

**I16.** L'algoritmo di Euclide per il massimo comun divisore, usato per ridurre una frazione ai minimi termini.

```text
SOTTOPROGRAMMA _mcd(_a, _b)
    FINCHE' _b diverso da 0
        ASSEGNA a _r il valore del resto di _a diviso _b
        ASSEGNA a _a il valore _b
        ASSEGNA a _b il valore _r
    FINE
    RESTITUISCI _a
FINE

INIZIO
    LEGGI _num e _den
    ASSEGNA a _d il valore _mcd(_num, _den)
    VISUALIZZA _num, _den, _num / _d e _den / _d
FINE
```

```text
Numeratore e denominatore: 84 126
84/126 = 2/3
```

1. Eseguite a mano `_mcd(84, 126)` e completate la tabella con i valori di `_a` e `_b` all'inizio di ogni giro, piu' una colonna finale per quando il ciclo si ferma.

| | giro 1 | giro 2 | giro 3 | fine |
| --- | --- | --- | --- | --- |
| `_a` |  |  |  |  |
| `_b` |  |  |  |  |

2. Al primo giro `_a` e `_b` si scambiano di posto, perche' il resto di $84$ diviso $126$ e' $84$. L'algoritmo funziona lo stesso anche se i due numeri sono dati nell'ordine "sbagliato": quanti giri costa?
3. Dentro il sottoprogramma, `_a` e `_b` vengono modificati a ogni giro. Eppure il `main` stampa ancora $84$ e $126$ nella prima parte della riga: perche'? (E' il motivo per cui il `main` puo' calcolare `_num / _d` senza aver perso `_num`.)
4. **In piu'.** Che cosa restituisce `_mcd(5, 0)`? E `_mcd(0, 5)`? Seguite l'algoritmo a mano in entrambi i casi e dite quanti giri fa il ciclo nei due. In matematica si pone $\gcd(a, 0) = a$: l'algoritmo e' d'accordo?

**I17.** Numeri palindromi, cioe' che si leggono uguali nei due versi.

```text
SOTTOPROGRAMMA _inverti(_n)
    ASSEGNA a _r il valore 0
    FINCHE' _n > 0
        ASSEGNA a _r il valore _r x 10 + il resto di _n diviso 10
        ASSEGNA a _n il valore _n / 10
    FINE
    RESTITUISCI _r
FINE

SOTTOPROGRAMMA _e_palindromo(_n)
    SE _n = _inverti(_n) ALLORA
        RESTITUISCI 1
    FINE
    RESTITUISCI 0
FINE

INIZIO
    LEGGI _a e _b
    ASSEGNA a _quanti il valore 0
    PER _n DA _a A _b
        SE _e_palindromo(_n) = 1 ALLORA
            VISUALIZZA _n
            ASSEGNA a _quanti il valore _quanti + 1
        FINE
    FINE
    VISUALIZZA _quanti
FINE
```

```text
Da quale numero a quale numero? 100 200
101 111 121 131 141 151 161 171 181 191
Quanti: 10
```

1. Quanto vale `_inverti(1200)`? E quindi `_e_palindromo(1200)`? Esiste un numero maggiore di zero che finisce con uno zero e che sia palindromo?
2. `_e_palindromo` restituisce $1$ oppure $0$, e il `main` la confronta con $1$. In C si puo' scrivere piu' brevemente `if (e_palindromo(n))`: perche' funziona lo stesso? (Ripensate alle condizioni del Pacchetto D.)
3. Contate i palindromi da $1$ a $1000$: sono $108$. Verificatelo con il programma, poi ricavate lo stesso numero a mano, contando separatamente quelli di una, due e tre cifre.
4. **In piu'.** Partite da un numero, sommategli il suo rovesciato e ripetete finche' non ottenete un palindromo: con $87$ servono $4$ somme e si arriva a $4884$. Scrivete il programma che le conta e provatelo su tutti i numeri da $10$ a $200$, fermandovi in ogni caso dopo $30$ somme. Il numero e il suo rovesciato vanno dichiarati `long` (con `%ld` in `printf`): le somme crescono in fretta e per alcuni numeri, come $89$ e $98$, un `int` non basta piu' e i valori diventano negativi. Uno solo, da $10$ a $200$, raggiunge il limite delle $30$ somme senza arrivare a un palindromo: quale? Per quel numero, il $196$, nessuno e' ancora riuscito a dimostrare che a un palindromo ci si arrivi mai.

**I18.** Massimo di un array e conteggio sopra una soglia.

```text
SOTTOPROGRAMMA _massimo_v(_v, _n)
    ASSEGNA a _m il valore _v[0]
    PER _i DA 1 A _n - 1
        SE _v[_i] > _m ALLORA
            ASSEGNA a _m il valore _v[_i]
        FINE
    FINE
    RESTITUISCI _m
FINE

SOTTOPROGRAMMA _conta_maggiori(_v, _n, _soglia)
    ASSEGNA a _c il valore 0
    PER _i DA 0 A _n - 1
        SE _v[_i] > _soglia ALLORA
            ASSEGNA a _c il valore _c + 1
        FINE
    FINE
    RESTITUISCI _c
FINE

INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    ASSEGNA a _m il valore _massimo_v(_v, _n)
    ASSEGNA a _quanti il valore _conta_maggiori(_v, _n, _m / 2)
    VISUALIZZA _m e _quanti
FINE
```

Il programma legge `_n` (da $2$ a `MAX`, che vale $20$, controllato con un `do while`) e poi gli `_n` numeri, come in F18.

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Massimo: 8
Maggiori di 4: 2
```

1. `_m / 2` e' una divisione tra interi: con questi dati vale $4$. Quali due numeri dell'array vengono contati? Se il massimo fosse $9$ la soglia sarebbe ancora $4$: quale numero reale viene perso per strada?
2. `_conta_maggiori` conta gli elementi **strettamente** maggiori della soglia. Con questi dati, quanti sarebbero se il confronto fosse `>=`?
3. Il massimo viene sempre contato? Provate con un array di tutti zeri, per esempio `0 0 0`: il massimo e' $0$, la soglia e' $0$ e il conteggio e' $0$. Per quali valori del massimo il massimo stesso rientra nel conteggio?
4. `_conta_maggiori` e' la stessa funzione documentata in I1. Confrontate la documentazione che avete scritto voi con quella di I1: dice le stesse cose?

**I19.** Punti dentro un cerchio, senza mai calcolare una radice quadrata.

```text
SOTTOPROGRAMMA _distanza2(_x1, _y1, _x2, _y2)
    RESTITUISCI (_x2 - _x1) x (_x2 - _x1) + (_y2 - _y1) x (_y2 - _y1)
FINE

INIZIO
    LEGGI _cx, _cy e _r
    LEGGI _n
    ASSEGNA a _dentro il valore 0
    PER _i DA 0 A _n - 1
        LEGGI _x e _y
        SE _distanza2(_x, _y, _cx, _cy) <= _r x _r ALLORA
            ASSEGNA a _dentro il valore _dentro + 1
        FINE
    FINE
    VISUALIZZA _dentro
FINE
```

Tutte le coordinate e il raggio sono interi.

```text
Centro e raggio: 0 0 5
Quanti punti? 4
0 0
3 4
5 1
-2 -2
Dentro o sul bordo: 3
```

1. Il sottoprogramma restituisce il **quadrato** della distanza, e il confronto avviene con `_r x _r`. Perche' il risultato e' lo stesso che confrontare la distanza con il raggio? (Vale perche' entrambe le quantita' sono non negative.) Elencate due vantaggi di questa scelta rispetto al calcolo della radice.
2. Il punto $(3, 4)$ dista esattamente $5$ dal centro: sta sul bordo. Con `<` al posto di `<=` quanti punti verrebbero contati?
3. Quale dei quattro punti resta fuori, e di quanto? Confrontate `_distanza2` con `_r x _r` per quel punto.
4. **In piu'.** Quanti punti a coordinate intere stanno dentro il cerchio di raggio $10$ centrato nell'origine, bordo compreso? Scrivete un programma con due cicli annidati, da $-10$ a $10$: il risultato e' $317$. Confrontatelo con l'area del cerchio, $\pi r^2 \approx 314.16$. Provate anche con raggio $100$ e confrontate con $31415.9$: l'errore cresce o resta piccolo rispetto all'area?

**I20.** **Sfida.** Il triangolo di Tartaglia, calcolato con i coefficienti binomiali.

```text
SOTTOPROGRAMMA _binomiale(_n, _k)
    SE _k > _n - _k ALLORA
        ASSEGNA a _k il valore _n - _k
    FINE
    ASSEGNA a _r il valore 1
    PER _i DA 1 A _k
        ASSEGNA a _r il valore _r x (_n - _k + _i) / _i
    FINE
    RESTITUISCI _r
FINE

INIZIO
    LEGGI _righe
    PER _n DA 0 A _righe - 1
        PER _k DA 0 A _n
            VISUALIZZA _binomiale(_n, _k)
        FINE
        vai a capo
    FINE
FINE
```

```text
Quante righe? 6
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```

1. La prima riga del sottoprogramma sostituisce `_k` con `_n - _k` quando `_k` e' grande. Verificate con la tabella che $\binom{n}{k} = \binom{n}{n-k}$, e dite quanti giri risparmia questa riga nel calcolo di $\binom{10}{8}$.
2. Dentro il ciclo c'e' una divisione tra interi, `/ _i`, eppure il risultato e' sempre esatto. Il motivo e' che dopo $i$ giri la variabile `_r` vale $\binom{n-k+i}{i}$, che e' un numero intero. Verificatelo a mano sui quattro giri del calcolo di $\binom{9}{4} = 126$, scrivendo il valore di `_r` dopo ogni giro.
3. Aggiungete al programma una variabile `long` che somma i numeri di ogni riga e la stampa in fondo alla riga stessa. Che cosa ottenete? Spiegate il risultato contando in due modi i sottoinsiemi di un insieme di $n$ elementi.
4. **In piu'.** Portate il programma a $31$ righe: nell'ultima c'e' un numero sbagliato, ed e' negativo. E' quello centrale, $\binom{30}{15}$, che vale $155117520$ e in un `int` entrerebbe comodamente. Che cosa e' uscito dall'`int`, allora? Guardate l'espressione `_r x (_n - _k + _i)` **prima** della divisione. Cambiate il tipo di `_r` in `long`: adesso la prima riga sbagliata e' quella con $n = 62$.

### Riepilogo di Doxygen e dei nuovi comandi gdb

| Tag | Che cosa dice | Visto in |
| --- | --- | --- |
| `/** ... */` | apre e chiude il blocco di documentazione, subito sopra la funzione o il prototipo | riquadro |
| `@brief` | una frase sola: che cosa fa la funzione, non come | riquadro, I8 |
| `@param nome` | che cosa rappresenta un parametro e quali valori sono ammessi | riquadro, I1 |
| `@return` | che cosa viene restituito; sulle funzioni `void` non si scrive | riquadro, I9 |
| `@pre` | una condizione che chi chiama deve garantire | I8 |
| `@note` | un'avvertenza per chi legge | I1 |

| Comando | Cosa fa | Visto in |
| --- | --- | --- |
| `break nome_funzione` | ferma il programma a ogni chiamata di quella funzione | I4 |
| `bt` | mostra la catena delle chiamate, fino a `main` | I4, I10 |
| `finish` | finisce la funzione corrente e stampa il valore restituito | I4, I10 |
| `gcc -Wall` | tra gli altri, segnala `implicit declaration` e `control reaches end of non-void function` | I11, I13 |


## Pacchetto J: Ricorsione e classi di memorizzazione

Una funzione puo' chiamare un'altra funzione. Puo' anche chiamare **se stessa**: e' la **ricorsione**. E' un'idea potente e, a prima vista, sospetta: come fa una funzione a usare un risultato che sta ancora calcolando? La risposta sta in dove vivono le variabili, e cioe' nel secondo tema di questo pacchetto, le **classi di memorizzazione**. Sono la risposta alla domanda "quando nasce e quando muore questa variabile, e chi la vede?", e chiudono anche un conto lasciato aperto in H6, dove gli array grandi dovevano essere dichiarati prima di `main` senza che fosse ancora chiaro il perche'.

### La ricorsione, in breve

Una funzione ricorsiva ha sempre due parti:

- uno o piu' **casi base**, che danno la risposta senza chiamare nessuno;
- uno o piu' **casi ricorsivi**, che chiamano la funzione stessa su un problema **piu' piccolo**, cioe' piu' vicino al caso base.

```c
long fattoriale(int n) {
    if (n == 0) {        /* caso base */
        return 1;
    }
    return n * fattoriale(n - 1);   /* caso ricorsivo: n - 1 e' piu' vicino a 0 */
}
```

Se manca il caso base, o se il caso ricorsivo non si avvicina mai al caso base, la funzione non finisce mai: in J11 e J12 vedrete che cosa succede allora.

Mentre `fattoriale(5)` aspetta il risultato di `fattoriale(4)`, le due chiamate esistono **nello stesso momento**, e ciascuna ha la sua copia di `n`: una vale $5$, l'altra $4$. Le chiamate si impilano una sull'altra, e quando una finisce viene tolta dalla pila e l'esecuzione riprende da dove si era interrotta. In gdb, `bt` mostra proprio questa pila.

### Dove vivono le variabili

Ogni variabile ha un posto in cui sta, un momento in cui nasce, uno in cui muore e un insieme di funzioni che la vedono. L'insieme di queste proprieta' si chiama **classe di memorizzazione**.

**Variabile locale.** E' quella che usate da sempre: dichiarata dentro una funzione (o dentro un blocco), nasce quando l'esecuzione arriva alla dichiarazione e muore all'uscita. Ogni chiamata ha la sua. **Non viene inizializzata**: se non le assegnate un valore, contiene quello che per caso si trovava in quella cella di memoria. La parola chiave sarebbe `auto`, ma nessuno la scrive mai, perche' e' il comportamento normale.

**Variabile locale `static`.** Si scrive `static` davanti alla dichiarazione, dentro la funzione. Cambia tutto tranne la visibilita': ne esiste **una sola copia**, che nasce prima di `main` e muore alla fine del programma, quindi **sopravvive tra una chiamata e l'altra**; vale $0$ all'inizio, e se c'e' un'inizializzazione (`static int k = 5;`) questa viene eseguita **una volta sola**, non a ogni chiamata. Continua pero' a essere visibile solo dentro quella funzione.

```c
int prossimo_id(void) {
    static int ultimo = 0;   /* una sola copia, nasce a 0, sopravvive */
    ultimo++;
    return ultimo;           /* restituisce 1, poi 2, poi 3, ... */
}
```

**Variabile globale.** Dichiarata fuori da tutte le funzioni, come gli array grandi di H6. Vive per tutto il programma, vale $0$ all'inizio ed e' visibile a **tutte** le funzioni del file. Comoda e pericolosa: e' buona regola usarne il meno possibile, e J15 mostra esattamente perche'. Resta giusta quando il dato e' davvero di tutto il programma, come la matrice su cui lavorano tutte le funzioni, o un contatore che il `main` deve poter azzerare.

Tre parole che incontrerete e che qui vi bastano a riconoscere:

- `static` davanti a una variabile **globale** non ne cambia la vita, ma la rende privata del file in cui e' scritta: ha senso solo quando i file sono piu' di uno, e lo vedrete negli esercizi difficili;
- `extern` dichiara una variabile che e' definita in un altro file: stessa storia, stesso rimando;
- `register` chiedeva al compilatore di tenere la variabile nel processore invece che in memoria. Oggi i compilatori decidono da soli e la ignorano: la trovate solo in codice vecchio.

### Due zone di memoria

Le variabili locali vivono in una zona chiamata **pila** (in inglese *stack*): a ogni chiamata di funzione ci si appoggia sopra un pezzetto con i parametri e le variabili locali di quella chiamata, e al `return` lo si toglie. La pila e' **piccola**: il suo limite si legge con

```bash
ulimit -s
```

che su Linux risponde di solito `8192`, cioe' $8192$ KB, cioe' $8 \cdot 1024 \cdot 1024 = 8388608$ byte.

Le variabili globali e le `static`, invece, non stanno nella pila: hanno una zona tutta loro, preparata una volta per tutte all'avvio del programma e grande quanto serve. Da qui due conseguenze che vedrete in questo pacchetto:

- un array di qualche milione di elementi dentro `main` non ci sta nella pila e fa morire il programma (J9): e' il motivo per cui in H6 stava prima di `main`;
- una ricorsione troppo profonda riempie la pila di chiamate e fa morire il programma allo stesso modo (J11 e J16).

### Esercizi (J1-J10)

**J1.** Scrivete `fattoriale.c`, che stampa una tabella dei fattoriali da $0$ a $20$ calcolati in due modi: con una funzione ricorsiva `long fattoriale_r(int n)` e con una iterativa `long fattoriale_i(int n)` che usa un `for`. Le due colonne devono coincidere.

```text
 0! = 1                      1
 1! = 1                      1
 2! = 2                      2
...
19! = 121645100408832000     121645100408832000
20! = 2432902008176640000    2432902008176640000
```

1. Quante chiamate a `fattoriale_r` avvengono in tutto quando il `main` calcola `fattoriale_r(5)`? Elencatele.
2. **Con gdb.** Date `break fattoriale_r if n == 0`, poi `run`. Quando il programma si ferma, date `bt`: quante righe compaiono per il calcolo di `fattoriale_r(5)`? Leggetele dal basso verso l'alto e dite chi ha chiamato chi. Poi date `print n` e `finish`.
3. Portate la tabella a $21$: l'ultima riga e' negativa, in **entrambe** le colonne. Quanto vale davvero $21!$? Confrontate con `LONG_MAX` di `limits.h`, che vale $9223372036854775807$.
4. Le due versioni fanno lo stesso numero di moltiplicazioni. Quale delle due vi sembra piu' facile da leggere? E quale delle due, secondo voi, consuma piu' memoria mentre lavora? (La risposta sta nel riquadro sulle due zone di memoria.)

**J2.** Quante volte viene chiamata davvero una funzione ricorsiva? Per scoprirlo le diamo una memoria.

```c
#include <stdio.h>

long fattoriale(int n) {
    static long chiamate = 0;
    chiamate++;
    if (n == 0) {
        printf("Chiamate finora: %ld\n", chiamate);
        return 1;
    }
    return n * fattoriale(n - 1);
}

int main(void) {
    printf("5! = %ld\n", fattoriale(5));
    printf("7! = %ld\n", fattoriale(7));
    return 0;
}
```

```text
Chiamate finora: 6
5! = 120
Chiamate finora: 14
7! = 5040
```

1. Il primo numero stampato e' $6$: elencate le sei chiamate. Il secondo e' $14$ e non $8$: che cosa e' successo a `chiamate` tra la prima e la seconda riga del `main`?
2. Togliete `static`, lasciando `long chiamate = 0;`. Adesso il programma stampa `Chiamate finora: 1` tutte e due le volte, e gcc non protesta. Che cosa conta, ora, quella variabile?
3. Rimettete `static`. L'inizializzazione `= 0` viene eseguita una volta sola, non a ogni chiamata: se fosse eseguita a ogni chiamata, che cosa stamperebbe il programma? (Avete appena visto la risposta al punto 2.)
4. **In piu'.** Per avere la seconda riga a $8$ bisognerebbe azzerare il contatore tra le due chiamate del `main`. Con `static` dentro la funzione non si puo': perche'? Quale delle classi di memorizzazione del riquadro lo permetterebbe? (La usiamo in J3.)

**J3.** La successione di Fibonacci scritta in modo ricorsivo e' elegante, breve e disastrosa. Qui il contatore e' una variabile globale, cosi' il `main` puo' azzerarlo prima di ogni prova.

```c
#include <stdio.h>

long chiamate;                      /* globale: all'inizio vale 0 */

long fib(int n) {
    chiamate++;
    if (n < 2) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    int n;
    long f;
    for (n = 0; n <= 30; n += 5) {
        chiamate = 0;
        f = fib(n);
        printf("fib(%2d) = %-9ld chiamate: %ld\n", n, f, chiamate);
    }
    return 0;
}
```

```text
fib( 0) = 0         chiamate: 1
fib( 5) = 5         chiamate: 15
fib(10) = 55        chiamate: 177
fib(15) = 610       chiamate: 1973
fib(20) = 6765      chiamate: 21891
fib(25) = 75025     chiamate: 242785
fib(30) = 832040    chiamate: 2692537
```

1. Il valore `f` viene calcolato in una riga a parte e solo dopo stampato. Non e' un capriccio: se scrivessimo `printf("...", n, fib(n), chiamate);` il C non garantisce in quale ordine calcola i suoi argomenti, e `chiamate` potrebbe essere letta prima che `fib` venga eseguita. Provate e guardate che cosa stampa il vostro compilatore.
2. Guardate la colonna delle chiamate: ogni volta che `n` cresce di $5$, le chiamate crescono di circa quante volte? Confrontate con la colonna dei valori di `fib`.
3. Il numero di chiamate per `fib(n)` vale esattamente $2 \cdot fib(n+1) - 1$. Verificatelo su tre righe della tabella, sapendo che $fib(6) = 8$, $fib(16) = 987$ e $fib(31) = 1346269$.
4. **Con time.** Scrivete la versione iterativa `long fib_i(int n)`, che calcola i valori uno dopo l'altro con un ciclo e due variabili d'appoggio, e aggiungete $35$ e $40$ alla tabella. Misurate il tempo delle due versioni per `fib(40)`: quante chiamate fa la ricorsiva? E quanti giri fa l'iterativa? Dove sta sprecando tempo la ricorsiva? (Suggerimento: per calcolare `fib(30)` serve `fib(28)`, e la ricorsiva lo calcola piu' di una volta.)

**J4.** Non e' la ricorsione a essere lenta, ma il modo in cui si divide il problema. Scrivete `potenze.c` con due funzioni ricorsive che calcolano $base^{esp}$ con `esp` non negativo:

- `long potenza(long base, int esp)`: se `esp` e' $0$ restituisce $1$, altrimenti restituisce `base * potenza(base, esp - 1)`;
- `long potenza_veloce(long base, int esp)`: se `esp` e' $0$ restituisce $1$; altrimenti calcola **una volta sola** `mezzo = potenza_veloce(base, esp / 2)` e restituisce `mezzo * mezzo` se `esp` e' pari, `base * mezzo * mezzo` se e' dispari.

Due contatori globali, uno per funzione, contano le chiamate. Il programma stampa la tabella di $2^{esp}$ per `esp` uguale a $1, 2, 4, 8, 16, 32$.

```text
esp   2^esp          chiamate potenza   chiamate veloce
  1   2                            2                 2
  2   4                            3                 3
  4   16                           5                 4
  8   256                          9                 5
 16   65536                       17                 6
 32   4294967296                  33                 7
```

1. Per `potenza`, il numero di chiamate e' sempre `esp + 1`: perche'? Per `potenza_veloce`, confrontate la colonna con il numero di cifre binarie di `esp`.
2. Perche' `mezzo` deve essere calcolato una volta sola in una variabile? Provate a scrivere invece `return potenza_veloce(base, esp / 2) * potenza_veloce(base, esp / 2);` e guardate il contatore: quante chiamate con `esp` uguale a $16$? La funzione e' ancora "veloce"?
3. Provate `potenza_veloce(2, 1000000)`: fa $21$ chiamate e risponde subito (il risultato non ha senso, perche' esce da un `long`, ma le chiamate si contano lo stesso). Provate ora `potenza(2, 1000000)`: il programma muore con `Segmentation fault`. Che cosa si e' riempito? Rileggete il riquadro sulle due zone di memoria.
4. Allungate la tabella oltre $32$, una potenza di due per volta e poi di uno in uno: fino a quale `esp` il valore di $2^{esp}$ resta positivo? Confrontate con `LONG_MAX` di `limits.h`, che vale $9223372036854775807$.

**J5.** Due classici in versione ricorsiva. Scrivete `ricorsive.c` con:

- `int mcd(int a, int b)`: se `b` e' $0$ restituisce `a`, altrimenti restituisce `mcd(b, a % b)`;
- `int somma_cifre(int n)`: se `n` e' minore di $10$ restituisce `n`, altrimenti restituisce `n % 10 + somma_cifre(n / 10)`.

Il `main` legge due interi positivi e stampa il massimo comun divisore e la somma delle cifre di entrambi.

```text
Due numeri interi positivi: 84 126
mcd(84, 126) = 42
Somma delle cifre di 84: 12
Somma delle cifre di 126: 9
```

1. Mettete accanto questo `mcd` e quello iterativo di I16 e scrivete i valori di `a` e `b` a ogni passo per la coppia $(84, 126)$: sono gli stessi? Che cosa fa qui il `return`, al posto delle tre assegnazioni del ciclo?
2. Quante chiamate fa `somma_cifre(999999)`? E `somma_cifre(7)`? In generale, da che cosa dipende il numero di chiamate?
3. La *radice numerica* di un numero si ottiene sommandone le cifre, e poi sommando le cifre del risultato, finche' non resta una cifra sola: per $12345$ si ottiene $15$ e poi $6$. Scrivete `int radice_numerica(int n)`, anch'essa ricorsiva, che restituisce `n` se e' minore di $10$ e altrimenti si richiama su `somma_cifre(n)`. Verificate su qualche numero che il risultato coincida sempre con $1 + (n - 1) \bmod 9$.
4. Documentate le tre funzioni. Per `mcd` e `somma_cifre` la condizione sui parametri va in `@pre`: che cosa succede a `somma_cifre` se `n` e' negativo? Provate.

**J6.** La ricerca binaria di F20, scritta in modo ricorsivo. L'array e' dichiarato prima delle funzioni e contiene i primi quindici numeri primi, gia' ordinati.

```c
#include <stdio.h>
#define N 15

long chiamate;
int primi[N] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};

int cerca(int v[], int sinistra, int destra, int x) {
    int m;
    chiamate++;
    if (sinistra > destra) {
        return -1;
    }
    m = (sinistra + destra) / 2;
    if (v[m] == x) {
        return m;
    }
    if (v[m] > x) {
        return cerca(v, sinistra, m - 1, x);
    }
    return cerca(v, m + 1, destra, x);
}
```

Il `main` legge un numero, azzera `chiamate`, chiama `cerca(primi, 0, N - 1, x)` e stampa il risultato. L'array globale si chiama `primi` e il parametro della funzione si chiama `v`: sono nomi diversi apposta, per il motivo che vedrete in J8.

```text
Che numero cerco? 31
31 si trova in posizione 10 (chiamate: 4)
```

```text
Che numero cerco? 30
30 non c'e' (chiamate: 5)
```

1. Seguite a mano la ricerca di $31$ e completate la tabella con i valori di `sinistra`, `destra` e `m` a ogni chiamata.

| chiamata | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| `sinistra` |  |  |  |  |
| `destra` |  |  |  |  |
| `m` |  |  |  |  |

2. Ci sono due casi base: quale ferma la ricerca quando il numero c'e', e quale quando non c'e'? Cercate $19$: quante chiamate bastano, e perche' cosi' poche?
3. Al massimo quante chiamate servono su un array di $15$ elementi? Provate a cercare un numero piu' piccolo di tutti e uno piu' grande di tutti, e contate.
4. **In piu'.** `sinistra` e `destra` sono parametri e non variabili locali senza valore iniziale: perche' e' necessario? Che cosa dovrebbe sapere ogni chiamata, e da chi lo riceve?
5. **In piu'.** Scambiate due elementi di `primi`, per esempio il $5$ e il $43$, e cercate il $5$: che cosa risponde il programma? La funzione e' sbagliata, o lo e' l'uso che ne state facendo? (Rileggete il `@pre` che dovreste averle scritto.)

**J7.** Due funzioni che ricordano, senza ricorsione di mezzo.

```c
#include <stdio.h>

int prossimo_id(void) {
    static int ultimo = 0;
    ultimo++;
    return ultimo;
}

double media_corrente(double x) {
    static double somma = 0;
    static int quanti = 0;
    somma += x;
    quanti++;
    return somma / quanti;
}

int main(void) {
    int i, id;
    double x, m;
    printf("Inserisci 5 numeri: ");
    for (i = 0; i < 5; i++) {
        scanf("%lf", &x);
        id = prossimo_id();
        m = media_corrente(x);
        printf("#%d  valore %.2f  media corrente %.2f\n", id, x, m);
    }
    return 0;
}
```

```text
Inserisci 5 numeri: 10 20 30 40 50
#1  valore 10.00  media corrente 10.00
#2  valore 20.00  media corrente 15.00
#3  valore 30.00  media corrente 20.00
#4  valore 40.00  media corrente 25.00
#5  valore 50.00  media corrente 30.00
```

1. `media_corrente` riceve un solo numero per volta, e non sa quanti ne ha gia' visti: eppure calcola la media di tutti. Dove sono conservati, tra una chiamata e l'altra, la somma e il conteggio?
2. Togliete `static` da `somma` e da `quanti`: adesso la colonna della media corrente stampa i valori $10.00$, $20.00$, $30.00$, $40.00$, $50.00$. Perche' proprio quelli?
3. `prossimo_id` e `media_corrente` hanno ciascuna le proprie variabili `static`, e nessuna delle due vede quelle dell'altra. Aggiungete a `prossimo_id` un secondo contatore chiamato anch'esso `quanti`: il programma compila lo stesso? Che cosa vi dice questo sulla visibilita' delle `static` locali?
4. **Con gdb.** Mettete `break prossimo_id` e lanciate il programma. Alla **prima** fermata date `print ultimo`: quanto vale, prima ancora che la funzione abbia fatto qualcosa? Date `continue` e, alla seconda fermata, ripetete `print ultimo`. La variabile e' stata ricreata o era ancora li'?

**J8.** Chi vede che cosa. Prevedete l'output su carta **prima** di eseguire.

```c
#include <stdio.h>

int conta = 100;             /* globale */

void f(void) {
    int conta = 1;           /* locale: nasconde la globale dentro f */
    conta++;
    printf("dentro f: conta = %d\n", conta);
}

void g(void) {
    conta++;                 /* qui non c'e' nessuna locale: si usa la globale */
    printf("dentro g: conta = %d\n", conta);
}

int main(void) {
    f();
    g();
    f();
    g();
    printf("in main: conta = %d\n", conta);
    return 0;
}
```

1. Scrivete le cinque righe che vi aspettate, poi eseguite e confrontate. Dove vi siete sbagliati?
2. `f` stampa due volte lo stesso numero, `g` no. Spiegate la differenza nei termini del riquadro: quando nasce e quando muore la variabile stampata da `f`?
3. Aggiungete `static` davanti alla locale di `f`. Adesso `f` stampa $2$ e poi $3$: perche'? E la globale, alla fine, quanto vale?
4. Togliete l'inizializzazione della locale di `f`, lasciando `int conta;`. Compilate con `-Wall -Wextra`: che cosa segnala gcc? Togliete invece `= 100` dalla globale: gcc dice niente, e il programma stampa comunque numeri sensati. Perche' le globali partono da $0$ e le locali no?
5. **In piu'.** Compilate con `gcc -Wall -Wextra -Wshadow`: il messaggio contiene `shadows a global declaration`. Che cosa vi sta consigliando, questo flag, sul nome da dare alla locale di `f`?

**J9.** L'array che non ci sta. Il programma riempie una matrice $2000 \times 2000$ e somma la diagonale: dovrebbe stampare `Somma della diagonale: 3998000`. Invece muore subito con `Segmentation fault`, e gcc non aveva segnalato niente.

```c
#include <stdio.h>
#define N 2000

int main(void) {
    int m[N][N];
    int i, j;
    long somma = 0;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            m[i][j] = i + j;
        }
    }
    for (i = 0; i < N; i++) {
        somma += m[i][i];
    }
    printf("Somma della diagonale: %ld\n", somma);
    return 0;
}
```

1. Quanti byte occupa `m`? (Un `int` ne occupa $4$.) Quanti megabyte sono? Confrontate con il risultato di `ulimit -s`.
2. **Con gdb.** Eseguitelo dentro gdb: che messaggio compare? gdb indica la riga di `main`, non quella dell'assegnamento, perche' il programma muore prima ancora di cominciare, nel momento in cui la funzione si riserva il suo spazio sulla pila. Quanti assegnamenti ha fatto in tutto, allora?
3. Ci sono due correzioni, e funzionano entrambe: spostare la dichiarazione di `m` **prima** di `main`, oppure lasciarla dentro `main` scrivendo `static int m[N][N];`. Provatele tutte e due e verificate che stampino $3998000$. Che differenza resta tra le due, per una funzione diversa da `main` che volesse usare `m`?
4. Lasciate la dichiarazione dentro `main` senza `static` e provate `N` uguale a $1000$, poi $1400$, poi $1500$: il programma regge fino a poco meno di $1448$. Verificate che $1448$ sia all'incirca la radice quadrata di $8388608 / 4$, cioe' di quanti `int` stanno nella pila.
5. E' esattamente il motivo per cui in H6 l'array grande era dichiarato prima di `main`. Rileggete quell'esercizio: adesso sapreste spiegare la nota in una riga?

**J10.** La Torre di Hanoi: tre pioli, `n` dischi di diametro diverso impilati sul primo, dal piu' grande in basso. Si sposta un disco per volta, prendendolo dalla cima di una pila, e non si puo' mai appoggiare un disco su uno piu' piccolo. Per spostare `n` dischi da un piolo a un altro basta saper spostare `n - 1` dischi: li si sposta sul piolo d'appoggio, si sposta il disco grande a destinazione, e si rimettono sopra gli `n - 1`.

```c
#include <stdio.h>

long mosse;

void hanoi(int n, int da, int a, int appoggio) {
    if (n == 0) {
        return;
    }
    hanoi(n - 1, da, appoggio, a);
    mosse++;
    printf("Sposta il disco %d dal piolo %d al piolo %d\n", n, da, a);
    hanoi(n - 1, appoggio, a, da);
}
```

Il `main` legge `n`, azzera `mosse`, chiama `hanoi(n, 1, 3, 2)` e stampa il totale.

```text
Quanti dischi? 3
Sposta il disco 1 dal piolo 1 al piolo 3
Sposta il disco 2 dal piolo 1 al piolo 2
Sposta il disco 1 dal piolo 3 al piolo 2
Sposta il disco 3 dal piolo 1 al piolo 3
Sposta il disco 1 dal piolo 2 al piolo 1
Sposta il disco 2 dal piolo 2 al piolo 3
Sposta il disco 1 dal piolo 1 al piolo 3
Mosse: 7
```

1. Provate con $1$, $2$, $3$ e $4$ dischi e completate la tabella delle mosse. Che formula riconoscete? Giustificatela a partire dalle tre righe della funzione: se $M(n)$ e' il numero di mosse per `n` dischi, quanto vale $M(n)$ in funzione di $M(n-1)$?

| Dischi | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Mosse |  |  |  |  |

2. La funzione ha quattro parametri, e nelle due chiamate ricorsive i tre pioli compaiono in ordine diverso. Spiegate a parole le due chiamate: nella prima, quale piolo fa da destinazione e quale da appoggio? E nella seconda?
3. **Con time.** Togliete la `printf` e provate con $20$ dischi: le mosse sono $1048575$. Quanto ci mette? Riprovate con $25$ dischi: il tempo cresce di quante volte?
4. La leggenda vuole che dei monaci stiano spostando $64$ dischi, e che il mondo finisca quando avranno finito. Quante mosse servono? A una mossa al secondo, quanti anni? (Vi servira' un numero molto piu' grande di quello che entra in un `long`: fate il conto a parte, sapendo che un anno ha circa $3.15 \cdot 10^7$ secondi.)
5. Documentate `hanoi`. Che cosa scrivete in `@return`?

### Trova l'errore (J11-J15)

Come sempre: trovate l'errore, correggetelo e dite se e' **sintattico** o **progettuale**. Qui gcc vi aiuta in due casi su cinque, e in tutti e due solo se glielo chiedete per bene: negli altri tre tace anche con tutti i flag accesi.

**Novita': le stampe perdute.** Quando un programma muore di colpo con `Segmentation fault`, le ultime righe che aveva stampato possono non comparire: le stampe vengono raccolte in un magazzino (il *buffer*) e scritte sullo schermo un po' alla volta, e quello che era nel magazzino va perso. Se lanciate il programma dal terminale le righe compaiono quasi sempre, perche' li' il magazzino si svuota a ogni a capo; se invece mandate l'output in un file con `>`, spariscono. Ricordatevelo quando un programma sembra non aver stampato niente.

**J11.** Il programma deve stampare `Somma da 1 a 5: 15`. Non stampa niente e muore con `Segmentation fault`. Questa volta gcc lo aveva avvisato: il messaggio contiene `infinite recursion detected`.

```c
#include <stdio.h>

long somma_fino_a(int n) {
    return n + somma_fino_a(n - 1);
}

int main(void) {
    printf("Somma da 1 a 5: %ld\n", somma_fino_a(5));
    return 0;
}
```

1. Delle due parti che ogni funzione ricorsiva deve avere, quale manca? Scrivete i valori di `n` nelle prime otto chiamate: dove dovrebbe fermarsi, e invece dove va?
2. **Con gdb.** Lanciate il programma, aspettate che si fermi e date `bt`: che cosa mostra? (Sono tante righe: fermate l'elenco con `q`.) Che cosa si e' riempito?
3. Correggetelo aggiungendo il caso base, e verificate che stampi $15$.
4. **In piu'.** Dopo la correzione, provate `somma_fino_a(1000000)`: muore di nuovo. Il caso base adesso c'e': perche' non basta?

**J12.** Il programma stampa i fattoriali da $5$ a $0$. Le prime cinque righe compaiono correttamente, poi il programma muore con `Segmentation fault`. Questa volta gcc tace: la ricorsione non e' infinita per ogni valore, e il compilatore non puo' saperlo.

```c
#include <stdio.h>

long fattoriale(int n) {
    if (n == 1) {
        return 1;
    }
    return n * fattoriale(n - 1);
}

int main(void) {
    int n;
    for (n = 5; n >= 0; n--) {
        printf("%d! = %ld\n", n, fattoriale(n));
    }
    return 0;
}
```

1. Il caso base c'e'. Perche' allora `fattoriale(5)` funziona e `fattoriale(0)` no? Scrivete i valori di `n` nelle chiamate generate da `fattoriale(0)`.
2. Ci sono due correzioni possibili, `n <= 1` oppure `n == 0`: scrivetele entrambe e dite che cosa restituiscono, con ciascuna, `fattoriale(0)` e `fattoriale(-3)`.
3. Quale delle due correzioni rende vera la frase "`fattoriale(n)` e' definita per ogni `n` maggiore o uguale a zero" e **nient'altro**? Scrivete il `@pre` corrispondente.
4. Salvate questo programma come `fattoriale_giu.c` per non confonderlo con quello di J1, poi lanciatelo mandando l'output in un file, con `./fattoriale_giu > uscita.txt`, e guardate il file: le cinque righe ci sono? Rileggete la novita' qui sopra.

**J13.** Il programma deve contare i numeri pari in due array e stampare `Pari in a: 2` e `Pari in b: 4`. Stampa invece $2$ e $6$, e gcc non dice niente.

```c
#include <stdio.h>

int conta_pari(int v[], int n) {
    static int quanti = 0;
    int i;
    for (i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            quanti++;
        }
    }
    return quanti;
}

int main(void) {
    int a[4] = {1, 2, 3, 4};
    int b[4] = {2, 4, 6, 8};
    printf("Pari in a: %d\n", conta_pari(a, 4));
    printf("Pari in b: %d\n", conta_pari(b, 4));
    return 0;
}
```

1. Da dove arriva il $6$? Scomponetelo nei due contributi.
2. In J2 e J7 la parola `static` era esattamente quello che serviva, qui rovina tutto. Qual e' la differenza tra quei casi e questo? Rispondete completando la frase: "`static` serve quando la funzione deve ricordare ... , e fa danni quando ogni chiamata deve ... ".
3. Correggetelo e verificate che stampi $2$ e $4$.
4. **In piu'.** Una correzione sbagliata: lasciare `static` e aggiungere `quanti = 0;` come prima riga della funzione. Il programma stampa i numeri giusti. A che cosa serve, a quel punto, la parola `static`?

**J14.** Il programma deve stampare `Somma: 14`. Compilato come al solito, con `gcc -g -Wall -Wextra`, gcc tace e il programma stampa... dipende. Sul mio computer ha stampato proprio $14$; sul vostro potrebbe stampare un numero enorme, oppure $14$ anche lui.

```c
#include <stdio.h>
#define N 5

int somma(int v[], int n) {
    int i, s;
    for (i = 0; i < n; i++) {
        s += v[i];
    }
    return s;
}

int main(void) {
    int v[N] = {3, 1, 4, 1, 5};
    printf("Somma: %d\n", somma(v, N));
    return 0;
}
```

1. Qual e' l'errore? Rileggete la parte del riquadro che riguarda le variabili locali e il loro valore iniziale.
2. Se sul vostro computer il programma stampa il risultato giusto, l'errore c'e' lo stesso: perche' e' pericoloso un errore che "a volte funziona"?
3. Ricompilate aggiungendo `-O2`, il flag delle ottimizzazioni che avete incontrato in G8: adesso gcc segnala il problema con un messaggio che contiene `may be used uninitialized`. Perche' senza `-O2` non se ne accorgeva? Quell'avviso nasce da un'analisi che gcc fa solo quando ottimizza. (In J8 gcc ci era riuscito anche senza `-O2`, ma li' la variabile veniva letta nella riga subito dopo la dichiarazione; qui la lettura e' dentro un ciclo, e per arrivarci gcc deve prima mettere in fila tutti i calcoli.)
4. Correggetelo nel modo giusto. Poi provate una correzione sbagliata: togliete `s` dalle variabili locali e dichiaratela globale, prima delle funzioni. Il programma stampa $14$. Aggiungete pero' una seconda chiamata, `somma(v, N)` di nuovo, e stampatene il risultato: che cosa succede, e a quale esercizio appena fatto somiglia?

**J15.** Il programma deve stampare la somma di ciascuna delle tre righe della matrice, cioe' $6$, $22$ e $38$. Stampa invece una riga sola e termina regolarmente, senza nessun errore.

```c
#include <stdio.h>
#define R 3
#define C 4

int i;                         /* un indice "comodo", buono per tutti */
int m[R][C];

void riempi(void) {
    int j;
    for (i = 0; i < R; i++) {
        for (j = 0; j < C; j++) {
            m[i][j] = i * C + j;
        }
    }
}

int somma_riga(int riga) {
    int s = 0;
    for (i = 0; i < C; i++) {
        s += m[riga][i];
    }
    return s;
}

int main(void) {
    int riga, s;
    riempi();
    for (i = 0; i < R; i++) {
        riga = i;
        s = somma_riga(riga);
        printf("Somma della riga %d: %d\n", riga, s);
    }
    return 0;
}
```

1. Quanto vale `i` subito dopo il `return` di `somma_riga`? Perche' allora il ciclo del `main` finisce dopo un solo giro?
2. Correggetelo dichiarando `i` come variabile locale in ciascuna delle tre funzioni, e verificate che stampi $6$, $22$ e $38$.
3. Nel programma ci sono due variabili globali, `i` e `m`, ma una sola e' un errore. Che cosa distingue una globale sensata da una sbagliata? (Chiedetevi: questo dato e' davvero di tutto il programma, o e' un attrezzo che serve solo dentro un ciclo?)
4. **In piu'.** Questo e' il motivo per cui l'uso delle variabili globali e' sconsigliato. Riscrivete il programma in modo che `m` non sia globale ma venga passata come parametro: `void riempi(int m[][C])` e `int somma_riga(int m[][C], int riga)`. (Una matrice si passa indicando tutte le dimensioni tranne la prima.) Adesso quante variabili globali restano?

### Dallo pseudocodice al C (J16-J20)

Anche lo pseudocodice puo' essere ricorsivo: un SOTTOPROGRAMMA puo' chiamare se stesso, esattamente come in C. Come sempre, prima eseguite l'algoritmo a mano, poi scrivete il codice; ogni funzione tradotta va documentata.

**J16.** La somma dei primi `n` interi, in tre modi.

```text
SOTTOPROGRAMMA _somma(_n)
    SE _n = 0 ALLORA
        RESTITUISCI 0
    FINE
    RESTITUISCI _n + _somma(_n - 1)
FINE

INIZIO
    LEGGI _n
    VISUALIZZA _somma(_n)
    VISUALIZZA _n x (_n + 1) / 2
FINE
```

Aggiungete al programma un contatore globale delle chiamate, come in J3.

```text
Fino a quale numero? 10
Somma ricorsiva: 55
Formula n(n+1)/2: 55
Chiamate: 11
```

1. Eseguite a mano `_somma(4)`: scrivete la catena delle chiamate scendendo, e poi i valori restituiti risalendo.
2. Le chiamate per `_somma(n)` sono `n + 1`: perche' non `n`? Verificate con il contatore per $n = 10$ e $n = 100$.
3. Provate con $n = 100000$: funziona. Provate con $n = 200000$: `Segmentation fault`. Che cosa si e' riempito, e perche' con la formula il problema non si pone? Fate un conto a spanne: se ogni chiamata occupa qualche decina di byte nella pila, quante chiamate ci stanno in $8$ MB?
4. Scrivete anche la versione con un ciclo `for`. Delle tre, qual e' la piu' veloce, quale la piu' breve e quale rischia di morire? Nella documentazione di `_somma` tradotta in C, scrivete un `@note` che avverte del limite su `n`.

**J17.** La moltiplicazione "contadina", che usa solo addizioni e divisioni per due.

```text
SOTTOPROGRAMMA _prodotto(_a, _b)
    SE _b = 0 ALLORA
        RESTITUISCI 0
    FINE
    SE _b e' pari ALLORA
        RESTITUISCI _prodotto(_a + _a, _b / 2)
    FINE
    RESTITUISCI _a + _prodotto(_a + _a, _b / 2)
FINE

INIZIO
    LEGGI _a e _b
    VISUALIZZA _prodotto(_a, _b)
FINE
```

Il `main` legge due interi, con il secondo non negativo (controllato con un `do while`), e stampa il prodotto e il numero di chiamate, contate come in J16.

```text
Due numeri interi (il secondo non negativo): 13 11
13 x 11 = 143
Chiamate: 5
```

1. Completate la tabella con i valori di `_a` e `_b` nelle cinque chiamate generate da `_prodotto(13, 11)`. Nell'ultima riga scrivete si' o no a seconda che quella chiamata aggiunga `_a` al risultato, cioe' che sia finita nel ramo dei dispari.

| chiamata | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| `_a` |  |  |  |  |  |
| `_b` |  |  |  |  |  |
| aggiunge `_a`? |  |  |  |  |  |

2. Scrivete $11$ in base due: $1011$. Confrontate le sue cifre, lette da destra a sinistra, con l'ultima riga della tabella. Che cosa notate?
3. Con `_b` uguale a $1000000$ le chiamate sono $21$. Confrontate con I6, dove per moltiplicare servivano `b` addizioni: quante ne servivano li' con $b = 1000000$?
4. **In piu'.** Perche' il caso dispari funziona? Verificate l'identita' a mano: se `_b` e' dispari, allora `_b / 2` (divisione tra interi) vale $(b-1)/2$, e quindi $a + 2a \cdot \frac{b-1}{2} = ab$. Provate anche `_prodotto(13, 0)` e dite perche' il caso base restituisce $0$ e non $1$.

**J18.** Scrivere un numero in base due, stampando le cifre **al ritorno** dalle chiamate.

```text
SOTTOPROGRAMMA _binario(_n)
    SE _n > 1 ALLORA
        _binario(_n / 2)
    FINE
    VISUALIZZA il resto di _n diviso 2
FINE

INIZIO
    LEGGI _n
    _binario(_n)
    vai a capo
FINE
```

`_binario` non restituisce niente: in C sara' `void binario(int n)`. Il programma legge un intero maggiore di zero.

```text
Numero da convertire: 13
1101
```

1. Eseguite a mano `_binario(13)`: scrivete prima la catena delle chiamate ($13$, $6$, $3$, $1$) e poi, risalendo, la cifra che ciascuna stampa. Perche' le cifre escono nell'ordine giusto?
2. Spostate la VISUALIZZA **prima** della chiamata ricorsiva e riprovate con $13$: il programma stampa $1011$. Che cosa avete ottenuto? Con quali numeri le due versioni darebbero lo stesso risultato?
3. La chiamata ricorsiva avviene quando `_n > 1`: il caso base e' quindi `_n` uguale a $0$ oppure a $1$, e in quel caso si stampa soltanto. Provate a cambiare la condizione in `_n > 0`: con $13$ il programma stampa $01101$. Da dove viene lo zero in testa?
4. Quante cifre ha la scrittura binaria di `_n`? Verificate che coincida con il numero di chiamate, contandole con una variabile globale, per $n = 1$, $n = 13$, $n = 100$ e $n = 1000$.

**J19.** Il massimo di un array calcolato dividendo l'array a meta'.

```text
SOTTOPROGRAMMA _massimo(_v, _sinistra, _destra)
    SE _sinistra = _destra ALLORA
        RESTITUISCI _v[_sinistra]
    FINE
    ASSEGNA a _m il valore (_sinistra + _destra) / 2
    ASSEGNA a _a il valore _massimo(_v, _sinistra, _m)
    ASSEGNA a _b il valore _massimo(_v, _m + 1, _destra)
    SE _a > _b ALLORA
        RESTITUISCI _a
    FINE
    RESTITUISCI _b
FINE

INIZIO
    LEGGI _n
    PER _i DA 0 A _n - 1
        LEGGI _v[_i]
    FINE
    VISUALIZZA _massimo(_v, 0, _n - 1)
FINE
```

Il programma legge `_n` (da $2$ a `MAX`, che vale $20$) e poi gli `_n` numeri, e conta le chiamate con una variabile globale.

```text
Quanti numeri (da 2 a 20)? 6
5 1 4 2 8 0
Massimo: 8
Chiamate: 11
```

1. Disegnate l'albero delle chiamate per `_massimo(_v, 0, 5)`: ogni nodo porta la coppia (`_sinistra`, `_destra`). Quante foglie ha? Quanti nodi in tutto?
2. Le chiamate sono sempre $2n - 1$. Verificatelo con $n = 2$, $n = 4$ e $n = 8$ (dovete ottenere $3$, $7$ e $15$) e spiegatelo con l'albero del punto precedente: quante foglie, e quanti nodi interni?
3. Il massimo di I18 si trovava con un ciclo e $n - 1$ confronti. Qui i confronti sono ancora $n - 1$, ma in piu' ci sono $2n - 1$ chiamate di funzione. Quale delle due versioni usereste, e perche'? (Non tutte le soluzioni ricorsive sono migliori: questa e' piu' elegante ma non piu' efficiente.)
4. **In piu'.** Il pezzo di sinistra arriva fino a `_m` incluso e quello di destra parte da `_m + 1`. Provate a far partire il pezzo di destra da `_m`: con due elementi il programma non finisce piu'. Seguite a mano `_massimo(_v, 0, 1)` e spiegate perche'.

**J20.** **Sfida.** Quanti cammini ci sono dall'angolo in alto a sinistra di una griglia a quello in basso a destra, muovendosi solo verso il basso e verso destra? Se la griglia ha `_r` righe e `_c` colonne di passi, ogni cammino e' una sequenza di `_r` passi in giu' e `_c` passi a destra.

```text
SOTTOPROGRAMMA _cammini(_r, _c)
    SE _r = 0 O _c = 0 ALLORA
        RESTITUISCI 1
    FINE
    RESTITUISCI _cammini(_r - 1, _c) + _cammini(_r, _c - 1)
FINE

INIZIO
    LEGGI _r e _c
    VISUALIZZA _cammini(_r, _c)
FINE
```

Il programma conta anche le chiamate, con una variabile globale.

```text
Righe e colonne della griglia: 8 8
Cammini: 12870
Chiamate: 25739
```

1. Confrontate `_cammini(8, 8)` con il $\binom{16}{8}$ che sapete calcolare da I20: coincidono. Perche'? (Un cammino e' una sequenza di $16$ passi di cui $8$ in giu': quanti modi ci sono di scegliere quali?)
2. Perche' il caso base restituisce $1$ e non $0$? Che cosa significa, in termini di cammini, essere arrivati sull'ultima riga?
3. **Con time.** Provate con una griglia $15 \times 15$: i cammini sono $155117520$ e le chiamate oltre trecento milioni. Quanto ci mette? Provate poi $16 \times 16$: di quante volte cresce il tempo?
4. Il programma ricalcola infinite volte le stesse cose: `_cammini(3, 3)` viene chiamata moltissime volte, e ogni volta rifa' tutto da capo. Diamogli una memoria. Dichiarate prima delle funzioni una matrice `long memoria[MAX][MAX]` (con `#define MAX 31`), che all'inizio vale tutta zero, e scrivete una seconda funzione:

```text
SOTTOPROGRAMMA _cammini_m(_r, _c)
    ASSEGNA a _chiamate il valore _chiamate + 1
    SE _r = 0 O _c = 0 ALLORA
        RESTITUISCI 1
    FINE
    SE _memoria[_r][_c] diverso da 0 ALLORA
        RESTITUISCI _memoria[_r][_c]
    FINE
    ASSEGNA a _memoria[_r][_c] il valore _cammini_m(_r - 1, _c) + _cammini_m(_r, _c - 1)
    RESTITUISCI _memoria[_r][_c]
FINE
```

Con la griglia $8 \times 8$ le chiamate passano da $25739$ a $129$. Provate anche $15 \times 15$ e $30 \times 30$: quanto ci mette adesso?

5. Due domande sulla memoria. Primo: perche' `memoria` deve essere dichiarata **prima** delle funzioni, e non come variabile locale di `_cammini_m`? (Due motivi, e li trovate tutti e due nel riquadro sulle classi di memorizzazione.) Secondo: perche' basta il controllo `diverso da 0` per sapere se un valore e' gia' stato calcolato?

### Riepilogo delle classi di memorizzazione

| Dove si dichiara | Come si scrive | Quando nasce e muore | Valore iniziale | Chi la vede |
| --- | --- | --- | --- | --- |
| Dentro una funzione | `int x;` | a ogni chiamata; muore al `return` | nessuno: contiene spazzatura | solo quella funzione, solo quella chiamata |
| Dentro una funzione | `static int x;` | una volta sola, prima di `main`; muore alla fine | $0$ | solo quella funzione, ma e' sempre la stessa |
| Fuori da ogni funzione | `int x;` | una volta sola, prima di `main`; muore alla fine | $0$ | tutte le funzioni del file |
| Fuori da ogni funzione | `static int x;` | come sopra | $0$ | tutte le funzioni del file, e nessun altro file |
| Fuori da ogni funzione, ma definita altrove | `extern int x;` | nasce e muore con il programma, nel file che la definisce | quello deciso dove e' definita | il file che la dichiara cosi'; la variabile resta una sola |

E i comandi nuovi di questi due pacchetti:

| Comando | Che cosa fa | Visto in |
| --- | --- | --- |
| `break nome_funzione` | ferma il programma a ogni chiamata di quella funzione | I4 |
| `bt` | mostra la catena delle chiamate fino a `main` | I4, J1 |
| `finish` | finisce la funzione corrente e stampa il valore restituito | I4, I10 |
| `break f if n == 0` | ferma la funzione solo quando la condizione e' vera | J1 |
| `ulimit -s` | dice quanto e' grande la pila, in KB | J9 |
| `gcc -Wshadow` | segnala le variabili locali che nascondono una globale | J8 |
