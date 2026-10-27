# Esercizi Programmazione III

| Blocco | Argomento | Esercizi |
| --- | --- | --- |
| R | FILE*, argv e make test | 20 |
| S | qsort e bsearch | 5 |
| T | Integrazione e modularita' | 5 |
| U | Puntatori e memoria dinamica | 5 |


## Pacchetto R: FILE*, argv e make test

Finora i nostri programmi hanno letto i dati dalla tastiera e scritto i risultati sullo schermo. I programmi "veri" lavorano spesso in un altro modo: ricevono le indicazioni direttamente sulla riga di comando, come fa gcc quando scrivete `gcc -o somma somma.c`, e leggono e scrivono file. In questo pacchetto imparate a fare lo stesso. La prima parte (R1-R10) introduce gli argomenti della riga di comando (`argc` e `argv`) e i file (`FILE*`); nella seconda (R11-R20) i programmi vengono controllati automaticamente con un Makefile e il comando `make test`.

Il materiale che accompagna il pacchetto (la cartella `materiale_difficili`) contiene i file di dati della prima parte (nella cartella `parte1_dati`, in cui spostarsi con `cd` per provare gli esempi) e, per ogni esercizio della seconda, una cartella con il Makefile e i test.

### Prima parte: FILE* e argv

Compilate sempre con `gcc -g -Wall -Wextra`. Salvo indicazione diversa, ogni programma di questo pacchetto segue tre regole: i messaggi di errore vanno su `stderr`; in caso di errore (argomenti sbagliati, file che non si apre, dato non valido) il programma termina con codice di uscita $1$; se tutto va bene, con codice $0$. I codici di uscita sono spiegati piu' avanti, nella sezione sui file.

#### Gli argomenti della riga di comando

Se `main` si dichiara cosi', riceve le parole scritte sulla riga di comando:

```c
int main(int argc, char *argv[]) {
    /* ... */
}
```

`argc` e' il numero delle parole, compreso il nome del programma; `argv[0]` e' il nome del programma, `argv[1]` la prima parola dopo, e cosi' via fino a `argv[argc - 1]`. Con il comando `./binomiale 10 3`, per esempio, `argc` vale $3$, `argv[1]` e' `"10"` e `argv[2]` e' `"3"`. A dividere la riga in parole e' il terminale: gli spazi separano le parole, e le virgolette ne tengono insieme piu' di una (`"due tre"` e' una sola parola).

Attenzione: `argv[1]` non e' il numero $10$, ma il testo `"10"`. Per trasformarlo in un numero si usa `sscanf`, che funziona come `scanf` ma legge da un testo invece che dalla tastiera, e come `scanf` restituisce quanti valori e' riuscita a leggere:

```c
if (sscanf(argv[1], "%d", &n) != 1) {
    fprintf(stderr, "Errore: %s non e' un numero intero\n", argv[1]);
    return 1;
}
```

#### Le stringhe, in breve

Un testo come `"10"` o `"dati.txt"` e' una *stringa*: un array di `char` che termina con il carattere speciale `'\0'` (il codice $0$), che ne segna la fine. La stringa `"ciao"` occupa quindi cinque `char`: `'c'`, `'i'`, `'a'`, `'o'` e `'\0'`. Per ora leggete `char *` come "stringa": `argv` e' un array di stringhe, e `argv[1][0]` e' il primo carattere della prima parola. Bastano pochi strumenti:

- `printf("%s", s)` stampa la stringa `s`;
- `strlen(s)` restituisce il numero dei caratteri prima del `'\0'`;
- `strcmp(a, b)` restituisce $0$ se le due stringhe sono uguali (non si confrontano con `==`, come gli array in F14).

Le funzioni `strlen` e `strcmp` sono nella libreria `string.h`.

#### I file

Un file si apre con `fopen`, che restituisce un `FILE *`, cioe' un riferimento al file aperto da usare in tutte le operazioni successive:

```c
FILE *f;
int x;

f = fopen(argv[1], "r");     /* "r" lettura, "w" scrittura, "a" aggiunta in fondo */
if (f == NULL) {
    fprintf(stderr, "Errore: non riesco ad aprire %s\n", argv[1]);
    return 1;
}
while (fscanf(f, "%d", &x) == 1) {
    /* usa x */
}
fclose(f);
```

Se l'apertura non riesce (il file non esiste, oppure non si puo' scrivere in quella cartella), `fopen` restituisce `NULL`, un riferimento "a niente": va sempre controllato. Il modo `"w"` crea il file, oppure lo svuota se esiste gia'; `"a"` scrive in fondo a quello che c'e'.

| Funzione | Cosa fa |
| --- | --- |
| `fscanf(f, "%d", &x)` | come `scanf`, ma legge da `f`; restituisce quanti valori ha letto, $0$ se il dato non e' valido, `EOF` se il file e' finito |
| `fprintf(f, "%d\n", x)` | come `printf`, ma scrive in `f` |
| `fgetc(f)` | legge un carattere e ne restituisce il codice, oppure `EOF` se il file e' finito; il risultato va messo in un `int`, non in un `char` |
| `fputc(c, f)` | scrive il carattere `c` |
| `fclose(f)` | chiude il file; per i file aperti in scrittura e' il momento in cui i dati vengono salvati davvero |

Tre file sono gia' aperti quando il programma parte: `stdin` (la tastiera), `stdout` (lo schermo) e `stderr` (ancora lo schermo, ma riservato ai messaggi di errore). In effetti `printf(...)` e' la stessa cosa di `fprintf(stdout, ...)`, e `scanf(...)` di `fscanf(stdin, ...)`. Il valore restituito da `main` (il *codice di uscita*) segnala com'e' andata: per convenzione $0$ se tutto e' andato bene, un altro numero in caso di errore.

Qualche comando del terminale utile in questo pacchetto:

| Comando | Cosa fa |
| --- | --- |
| `./prog > uscita.txt` | scrive nel file `uscita.txt` quello che il programma stampa su `stdout` |
| `./prog 2> errori.txt` | scrive nel file `errori.txt` quello che il programma stampa su `stderr` |
| `./prog < dati.txt` | il programma legge `dati.txt` come se lo scriveste da tastiera (provatelo con il programma di E8, scrivendo i numeri in un file) |
| `echo $?` | mostra il codice di uscita dell'ultimo programma eseguito (rivedete M11) |
| `cat dati.txt` | mostra il contenuto di un file |
| `diff a.txt b.txt` | mostra le righe diverse tra due file; se non stampa nulla, i file sono identici |
| `wc dati.txt` | conta righe, parole e caratteri di un file |

#### gdb con gli argomenti

Gli argomenti si scrivono dopo `run`, esattamente come sulla riga di comando: `run dati.txt 3`, oppure `run dati.txt < tastiera.txt`. Quando il programma si ferma, gdb mostra anche gli argomenti di `main`, per esempio `main (argc=3, argv=0x7fffffffea48)`. Il numero che compare in `print argv[1]`, per esempio `0x7fffffffecbf "alfa"`, e' l'indirizzo in memoria della stringa e si puo' ignorare; quello che conta e' il testo tra virgolette. Allo stesso modo `print f` mostra l'indirizzo di un `FILE *`, oppure `0x0` se vale `NULL`. Come nei pacchetti precedenti, le domande che usano gdb iniziano con **Con gdb.**

#### Esercizi (R1-R10)

**R1.** Il programma stampa tutti i suoi argomenti.

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    int i;
    printf("argc = %d\n", argc);
    for (i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

```text
$ ./argomenti uno "due tre" 3+4
argc = 4
argv[0] = ./argomenti
argv[1] = uno
argv[2] = due tre
argv[3] = 3+4
```

1. Prevedete l'output, poi eseguite: `./argomenti`, `./argomenti 1 2 3`, `./argomenti "1 2" 3`, `./argomenti '*'` e `./argomenti *.c`. Perche' l'ultimo comando stampa i nomi dei vostri file? Chi ha trasformato `*.c` in quei nomi?
2. **Con gdb.** Mettete un breakpoint sulla prima `printf`, lanciate `run alfa "beta gamma"` e provate `print argv[1]`, `print argv[1][0]` e `print *argv@argc`, che mostra in un colpo solo tutto l'array. Che cosa c'e' in `argv[argc]`, subito dopo l'ultimo argomento?

**R2.** Scrivete un programma `binomiale` che riceve $n$ e $k$ sulla riga di comando e stampa il coefficiente binomiale $\binom{n}{k}$, calcolato in una variabile `long r` con la formula $\binom{n}{i} = \binom{n}{i-1} \cdot \frac{n - i + 1}{i}$, per `i` da $1$ a $k$, cioe' con la riga `r = r * (n - i + 1) / i;`. Requisiti:

- se gli argomenti non sono esattamente due, il programma scrive su `stderr` come si usa (`Uso: ./binomiale n k`) e termina con codice $1$;
- se un argomento non e' un intero, errore e codice $1$. Con `sscanf(argv[1], "%d", &n)` il testo `"10x"` verrebbe accettato come $10$; il trucco e' chiedere anche un carattere in piu': `sscanf(argv[1], "%d%c", &n, &extra)` restituisce $1$ solo se dopo il numero non c'e' nulla;
- deve valere $0 \le k \le n \le 60$ (`#define N_MAX 60`), altrimenti errore e codice $1$;
- se $k > n - k$, conviene calcolare $\binom{n}{n-k}$, che e' uguale e richiede meno passi.

```text
$ ./binomiale 10 3
C(10, 3) = 120
$ ./binomiale 60 30
C(60, 30) = 118264581564861424
$ ./binomiale 10 tre
Errore: n e k devono essere numeri interi
$ echo $?
1
```

1. Perche' a ogni passo la divisione per $i$ e' esatta? E perche' bisogna moltiplicare prima di dividere?
2. Portate `N_MAX` a $70$ e provate `./binomiale 62 31`: il risultato e' negativo. Perche'?
3. **Con gdb.** Sempre con `N_MAX` a $70$, trovate il primo passo in cui `r * (n - i + 1)` supera il massimo di un `long` ($2^{63} - 1 = 9223372036854775807$): mettete sulla riga che aggiorna `r` un breakpoint con la condizione `if r > 9223372036854775807 / (n - i + 1)` e lanciate `run 62 31`. Quanto vale `i` alla prima fermata? Rivedete M18: perche' la condizione si scrive con una divisione?

**R3.** Scrivete un programma `tartaglia` che riceve un numero di righe e il nome di un file, e scrive in quel file le prime righe del triangolo di Tartaglia, calcolate con un solo array come in F10. Requisiti:

- se gli argomenti non sono esattamente due, o se il numero di righe non e' un intero da $1$ a $30$, errore;
- il file si apre in scrittura con `f = fopen(argv[2], "w");`, dove `f` e' una variabile `FILE *`; se l'apertura non riesce, errore;
- sullo schermo il programma stampa soltanto un messaggio di conferma.

```text
$ ./tartaglia 6 triangolo.txt
Scritte 6 righe nel file triangolo.txt
$ cat triangolo.txt
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```

1. Eseguitelo due volte di seguito sullo stesso file, con $6$ e poi con $3$ righe: che cosa contiene il file alla fine? Poi cambiate il modo in `"a"`, cancellate il file con `rm triangolo.txt` e ripetete le due esecuzioni: che cosa contiene ora?
2. Provate a scrivere in una cartella che non esiste, per esempio `./tartaglia 3 /cartella_inesistente/t.txt`: il vostro programma se ne accorge? Che codice di uscita restituisce?
3. **Con gdb.** Mettete un breakpoint sulla riga della `fopen` e stampate `f` prima e dopo l'apertura (con `next`). Ripetete con la cartella inesistente: che cosa vale `f` dopo la `fopen`?

**R4.** Scrivete un programma `statistiche` che legge da un file una sequenza di interi, separati da spazi o a capo, e ne stampa quantita', minimo, massimo, media e varianza (la media dei quadrati meno il quadrato della media), queste ultime due con tre decimali. Requisiti:

- il nome del file e' l'unico argomento; argomenti sbagliati o un file che non si apre sono errori;
- il programma distingue i due modi in cui puo' finire la lettura: se `fscanf` restituisce `EOF` il file e' finito regolarmente; se restituisce $0$ c'e' un dato non valido, e il programma lo segnala e termina con errore;
- anche un file senza numeri e' un errore.

```text
$ cat misure.txt
12 15 9
21 18
        7 30 14
$ ./statistiche misure.txt
Numeri letti: 8
Minimo: 7
Massimo: 30
Media: 15.750
Varianza: 46.938
```

1. Salvate in una variabile `esito` il valore restituito da `fscanf` e stampatelo dopo il ciclo: quanto vale con `misure.txt`? E con `misure_rotte.txt`, che contiene `12 15 9 21 dieci 18`?
2. Il minimo e il massimo partono dal primo numero letto: perche' sarebbe sbagliato farli partire da $0$ (rivedete F15)? Come fate, se il primo numero viene letto dentro il ciclo?
3. Provate con un file che contiene un numero solo (scrivetelo voi) e con il file vuoto `vuoto.txt`: che cosa stampa il vostro programma? Che codice di uscita restituisce?

**R5.** Scrivete un programma `conta` che legge un file carattere per carattere con `fgetc`, mettendo ogni carattere letto nella variabile `c`, e stampa il numero di righe, di parole e di caratteri, seguiti dal nome del file. Requisiti:

- il nome del file e' l'unico argomento; argomenti sbagliati o un file che non si apre sono errori;
- le righe sono gli a capo (`'\n'`) contenuti nel file, come le conta `wc`; i caratteri sono tutti quelli letti, a capo compresi;
- una parola e' una sequenza di caratteri diversi da spazio, tabulazione (`'\t'`) e a capo; per contarle, ricordate se siete dentro o fuori da una parola con `enum posizione {FUORI, DENTRO};`;
- i tre numeri e il nome del file si stampano su una riga, separati da uno spazio.

```text
$ ./conta prova.txt
2 8 43 prova.txt
$ wc prova.txt
 2  8 43 prova.txt
```

1. Il comando `wc` del terminale fa lo stesso conto: confrontate i vostri risultati su qualche file, anche su un vostro programma `.c`.
2. Che valore ha `c` quando il ciclo termina? Perche' `c` deve essere un `int` e non un `char`?
3. **In piu'.** Create un file che contiene un carattere "strano" con `printf 'ab\377cd\n' > strano.txt` e confrontate il vostro programma con `wc -c strano.txt`. Poi dichiarate `c` come `char` e ripetete: quanti caratteri conta ora, e perche'? (Il carattere `\377` ha codice $255$; in un `char`, che sul vostro computer ha segno, diventa $-1$.)

**R6.** Scrivete un programma `cesare` che cifra un intero file di testo con il cifrario di Cesare (F8): `./cesare spostamento ingresso uscita`. Requisiti:

- le lettere minuscole e maiuscole si spostano restando tali; tutti gli altri caratteri (spazi, punteggiatura, cifre, a capo) si copiano invariati;
- lo spostamento puo' essere qualsiasi intero, anche negativo o maggiore di $26$;
- un numero di argomenti diverso da tre, uno spostamento che non e' un intero o un file che non si apre sono errori;
- sullo schermo il programma non stampa nulla, se non in caso di errore.

```text
$ cat chiaro.txt
Alea iacta est, disse Cesare nel 49 a.C.
Zebra!
$ ./cesare 3 chiaro.txt cifrato.txt
$ cat cifrato.txt
Dohd ldfwd hvw, glvvh Fhvduh qho 49 d.F.
Cheud!
```

1. Come trasformate uno spostamento qualsiasi, anche negativo, in uno tra $0$ e $25$? Ricordate che in C il resto di un numero negativo e' negativo. Verificate che $29$ dia lo stesso risultato di $3$.
2. Verificate che cifrare con $3$ e poi con $-3$ restituisca il testo originale: `./cesare -3 cifrato.txt di_nuovo.txt` seguito da `diff chiaro.txt di_nuovo.txt`. Che cosa dovrebbe stampare `diff`?
3. Su una *copia* di un file, provate `./cesare 3 copia.txt copia.txt`: che cosa resta nel file, e perche'? Impedite questo caso confrontando i due nomi con `strcmp`, prima di aprire qualsiasi file.

**R7.** Scrivete un programma `istogramma` che legge voti d'esame e ne disegna l'istogramma. Requisiti:

- se riceve il nome di un file lo legge da li', altrimenti legge da `stdin`: basta partire da `FILE *f = stdin;` e sostituirlo con il file aperto, se c'e' l'argomento (e chiudere `f` alla fine solo se non e' `stdin`); piu' di un argomento, un file che non si apre o un dato non numerico sono errori;
- i voti fuori dall'intervallo da $18$ a $30$ vengono segnalati su `stderr`, con la loro posizione nella sequenza, e non vengono contati;
- ogni riga dell'istogramma contiene il voto, uno spazio e la barra `|`, poi, se il voto compare, uno spazio e un asterisco per ogni volta che compare; l'ultima riga riassume i voti validi e quelli scartati.

```text
$ cat voti.txt
27 30 18 24 33 27 26 30 30 21 28 15 27
$ ./istogramma voti.txt
Voto non valido in posizione 5: 33
Voto non valido in posizione 12: 15
18 | *
19 |
20 |
21 | *
22 |
23 |
24 | *
25 |
26 | *
27 | ***
28 | *
29 |
30 | ***
Voti validi: 11, scartati: 2
```

1. Provate `./istogramma voti.txt`, `./istogramma < voti.txt` e `./istogramma voti.txt > grafico.txt 2> errori.txt`. Che cosa contengono i due file? Perche' e' utile che i messaggi di errore vadano su `stderr`?
2. Senza argomenti e senza `<`, il programma aspetta i voti dalla tastiera: per dirgli che sono finiti si preme Ctrl+D a inizio riga. Provate.

**R8.** Scrivete un programma `serie` che calcola le somme parziali di alcune serie viste nei pacchetti precedenti: `./serie nome n [passo]` (le parentesi quadre indicano un argomento facoltativo). Requisiti:

- il nome puo' essere `armonica` ($\sum 1/k$), `basilea` ($\sum 1/k^2$), `leibniz` ($4 \sum (-1)^{k+1}/(2k-1)$, che tende a $\pi$) o `geometrica` ($\sum 1/2^k$); in tutte le serie $k$ parte da $1$;
- riconoscete il nome con `strcmp` e salvatelo in una variabile `s` di tipo `enum serie {ARMONICA, BASILEA, LEIBNIZ, GEOMETRICA, SCONOSCIUTA};`, poi calcolate i termini con uno `switch`;
- senza il terzo argomento il programma stampa solo la somma dei primi $n$ termini; con il `passo` stampa la somma dopo `passo`, `2 * passo`, `3 * passo`, ... termini, fino a $n$; le somme si stampano con $10$ decimali;
- $n$ e `passo` devono essere interi positivi e `passo` deve dividere $n$; un nome sconosciuto produce un errore che elenca le serie disponibili; anche un numero sbagliato di argomenti e' un errore.

```text
$ ./serie basilea 1000
basilea(1000) = 1.6439345667
$ ./serie leibniz 100000 25000
leibniz(25000) = 3.1415526536
leibniz(50000) = 3.1415726536
leibniz(75000) = 3.1415793203
leibniz(100000) = 3.1415826536
$ ./serie fibonacci 10
Serie sconosciuta: fibonacci (disponibili: armonica, basilea, leibniz, geometrica)
```

1. Perche' non si puo' fare lo `switch` direttamente su `argv[1]`?
2. Con il passo, osservate come si avvicinano ai loro limiti le serie di Basilea e di Leibniz. Quante cifre giuste guadagna Leibniz ogni volta che $n$ viene moltiplicato per $10$?
3. **Con gdb.** Lanciate `run basilea 1000` e fermatevi dopo il riconoscimento del nome: cosa rispondono `print s` e `print/d s`?

**R9.** Il gioco della vita di Conway si gioca su una griglia di celle vive (`#`) o morte (`.`). A ogni generazione una cella viva sopravvive se ha $2$ o $3$ vicine vive (tra le $8$ che la circondano), altrimenti muore; una cella morta nasce se ha esattamente $3$ vicine vive. Le celle fuori dalla griglia sono considerate morte. Scrivete un programma `vita` che legge una griglia da un file, calcola un certo numero di generazioni e scrive la griglia finale in un altro file: `./vita ingresso uscita generazioni`. Requisiti:

- il file contiene sulla prima riga il numero di righe $R$ e di colonne $C$ (da $1$ a $50$), poi la griglia; il file di uscita ha lo stesso formato;
- tenete il numero di colonne nella variabile `C` e le celle nell'array `griglia`. Non avete ancora visto gli array a due dimensioni, ma non servono: la cella di riga $r$ e colonna $c$ si mette nell'elemento `griglia[r * C + c]` di un array lungo $R \cdot C$;
- per leggere le celle saltando gli a capo, usate `fscanf(f, " %c", &ch)` (lo spazio prima di `%c` salta spazi e a capo); se una cella non e' `#` ne' `.`, il programma segnala la riga sbagliata e termina con errore;
- argomenti sbagliati, un numero di generazioni negativo, file che non si aprono o una griglia incompleta sono errori;
- sullo schermo il programma non stampa nulla, se non in caso di errore.

```text
$ cat aliante.txt
6 6
.#....
..#...
###...
......
......
......
$ ./vita aliante.txt dopo4.txt 4
$ cat dopo4.txt
6 6
......
..#...
...#..
.###..
......
......
```

1. Perche' serve un secondo array per la nuova generazione? Che cosa succederebbe aggiornando la griglia mentre la si scorre?
2. **Con gdb.** Mettete un breakpoint sulla prima riga dentro il ciclo delle generazioni e stampate una riga intera della griglia: per esempio `print griglia[2 * C]@C` mostra la terza riga. Perche' funziona?
3. Il *lampeggiatore* (tre celle vive in fila, al centro di una griglia $5 \times 5$) torna uguale ogni due generazioni. Verificatelo con `diff` tra il file di partenza e quello ottenuto dopo $2$ generazioni.
4. Dopo $4$ generazioni l'aliante e' uguale a se stesso, ma spostato di una riga e di una colonna. Dove si trova dopo $12$ generazioni? E che cosa succede quando arriva al bordo?

**R10.** Scrivete un programma `fondi` che riceve i nomi di due file, ciascuno con una sequenza di interi gia' ordinata in modo crescente, e scrive in un terzo file la sequenza ordinata di tutti i numeri, uno per riga: `./fondi primo secondo uscita`. Requisiti:

- non si possono caricare i numeri in un array: il programma legge i due file contemporaneamente, tenendo sempre a disposizione il prossimo numero di ciascuno e scrivendo il piu' piccolo dei due;
- un file di ingresso vuoto e' valido: contiene la sequenza vuota;
- il programma controlla che i file siano davvero ordinati: se trova un numero minore del precedente nello stesso file, lo segnala e termina con errore;
- un dato non numerico, un numero di argomenti diverso da tre o un file che non si apre sono errori;
- alla fine stampa quanti numeri ha scritto.

```text
$ cat quadrati.txt
1 4 9 16 25 36
$ cat cubi.txt
1 8 27
$ ./fondi quadrati.txt cubi.txt tutti.txt
Scritti 9 numeri in tutti.txt
$ cat tutti.txt
1
1
4
8
9
16
25
27
36
```

1. **Con gdb.** Per ciascun file servono due variabili: il prossimo numero e un indicatore che dica se un numero c'e' ancora (cioe' se l'ultima `fscanf` ha restituito $1$). Con un breakpoint dentro il ciclo, seguitele con `display`.
2. Provate con `vuoto.txt` come primo o come secondo file: il risultato e' quello che vi aspettate? Poi provate `./fondi quadrati.txt disordinato.txt tutti.txt`, dove `disordinato.txt` contiene `2 3 5 4 11`: quanti numeri ha gia' scritto il vostro programma quando si accorge dell'errore?
3. Che cosa succede se il file di uscita coincide con uno dei due di ingresso? Impedite questo caso come in R6, prima di aprire qualsiasi file.

### Seconda parte: make test

Quando un programma si fa lungo, provarlo a mano dopo ogni modifica diventa noioso e si finisce per non farlo. In questa parte le prove le fa il computer: ogni cartella del materiale contiene un *Makefile* gia' pronto e una cartella `test` con i casi di prova, e basta il comando `make test` per controllare il programma su tutti i casi. Non serve sapere come e' fatto un Makefile: lo si usa come si usa gcc. Il programma `make` di solito e' installato insieme a gcc; se non lo fosse, si installa con `sudo apt install make`. Su macOS il Makefile usa il comando `gtimeout`, che si installa con `brew install coreutils`; senza, il limite di 5 secondi descritto piu' avanti non c'e', e un programma che non termina blocca `make test` finche' non premete Ctrl+C.

#### I tre comandi

| Comando | Cosa fa |
| --- | --- |
| `make` | compila il programma con `gcc -g -Wall -Wextra`, ma solo se il sorgente e' stato modificato dopo l'ultima compilazione |
| `make test` | compila (se serve) e prova il programma su tutti i casi della cartella `test` |
| `make clean` | cancella l'eseguibile e i file prodotti dai test |

#### Il Makefile

Il Makefile e' uguale in tutte le cartelle, tranne la riga `PROG = ...` con il nome del programma, e non va modificato. Chi e' curioso puo' aprirlo: e' commentato riga per riga. Non ricopiatelo da altri documenti: le righe dei comandi devono iniziare con un TAB, che copiando diventa spesso una serie di spazi (make risponderebbe `missing separator`).

#### Come funzionano i test

Per ogni test, nella cartella `test` ci sono:

- `NOME.arg`, una riga con gli argomenti da passare al programma (un file vuoto vuol dire nessun argomento);
- `NOME.atteso`, l'output che il programma deve stampare su `stdout`, seguito da una riga come `[codice di uscita: 0]`;
- a volte `NOME.in`, il contenuto da leggere da tastiera;
- i file di dati usati negli argomenti.

I messaggi su `stderr` non vengono controllati: il testo degli errori potete sceglierlo voi, ma il codice di uscita deve essere quello giusto, e in caso di errore su `stdout` non deve comparire nulla di piu' di quanto previsto. L'output invece deve coincidere carattere per carattere, spazi e a capo compresi. Prima di scrivere un programma, leggete tutti i file `.arg` e `.atteso` della sua cartella: completano gli esempi del testo.

#### Quando un test fallisce

```text
FALLITO  test/02_decimali    (./media_mobile 2 test/decimali.txt)
1c1
< 1.50
---
> 1.00
```

La riga `FALLITO` riporta il comando eseguito: potete ripeterlo dal terminale. Sotto c'e' il resoconto di `diff`: le righe che iniziano con `<` sono quelle attese, quelle con `>` quelle ottenute. Le righe come `1c1` dicono dove stanno le differenze: a sinistra della lettera ci sono i numeri di riga del file atteso, a destra quelli del file ottenuto; `c` vuol dire righe cambiate, `d` righe che mancano nell'ottenuto, `a` righe in piu'. Per esempio `1c1,2` significa che al posto della riga 1 attesa sono comparse le righe 1 e 2 ottenute. Il file `NOME.ottenuto` resta nella cartella `test` e potete aprirlo. Il codice di uscita da' altri indizi: $124$ significa che il programma e' stato fermato dopo 5 secondi (quasi sempre un ciclo infinito), mentre un numero maggiore di $128$ significa che il programma e' andato in crash ($136$ per una divisione per zero, $139$ o $135$ per un accesso alla memoria non valido, $134$ per un `assert` fallito o per una scrittura fuori da un array scoperta dal programma stesso).

Per capire *perche'* un test fallisce, ripetete il comando dal terminale; se non basta, usate gdb con gli stessi argomenti (per esempio `run 2 test/decimali.txt`) oppure aggiungete qualche `printf` di controllo.

#### Esercizi (R11-R20)

**R11.** Primo incontro con `make`. Nella cartella `R11_mcd` trovate il Makefile, i test e un programma gia' completo e corretto, `mcd.c`, che calcola il massimo comun divisore e il minimo comune multiplo di tutti i numeri positivi contenuti in un file.

```text
$ ./mcd test/esempio.txt
MCD = 6
mcm = 180
```

1. Spostatevi nella cartella con `cd` e guardate i test: `ls test`, poi `cat test/01_esempio.arg test/01_esempio.atteso`. Quali situazioni controllano i nove test?
2. Date `make` e poi `make test`: devono risultare $9$ test superati su $9$. Che cosa risponde `make` se lo date una seconda volta senza modificare il programma?
3. Ora rompete il programma, una modifica alla volta, lanciate `make test` e leggete il resoconto; dopo ogni prova rimettete il programma com'era.
    - Nella `printf` finale scrivete `M.C.D. =` al posto di `MCD =`. Quali test falliscono? Che cosa vi dice il `diff`?
    - Togliete il controllo sul file senza numeri. Quale test fallisce, e che cosa compare nella riga del codice di uscita?
4. Date `make clean` e guardate che cosa e' rimasto nella cartella.

**R12.** Trova gli errori con `make test`. Nella cartella `R12_media_mobile` c'e' il programma `media_mobile.c`, che contiene tre errori. Il programma dovrebbe funzionare cosi'. Si lancia con `./media_mobile k file`, dove $k$ e' un intero tra $1$ e $100$. Legge gli interi del file e, a partire dal $k$-esimo, stampa con due decimali la media degli ultimi $k$ numeri letti (la *media mobile*), una per riga; i $k$ numeri vengono tenuti in un array usato in modo circolare. Alla fine stampa la media mobile piu' alta, indicando le posizioni del primo e dell'ultimo numero di quella finestra (a parita' vale la prima). Se i numeri sono meno di $k$, se un dato non e' valido o se gli argomenti sono sbagliati, il programma termina con codice $1$.

```text
$ ./media_mobile 2 test/decimali.txt
1.50
3.00
5.50
Media mobile massima: 5.50 (numeri da 3 a 4)
```

1. Lanciate `make test`: quanti test falliscono? Per ciascun test fallito, leggete il `diff` e formulate un'ipotesi sull'errore prima di guardare il codice.
2. Per ogni ipotesi, cercate la riga sbagliata ripetendo il test con gli stessi argomenti, con gdb oppure con qualche `printf` di controllo. Correggete un errore alla volta e rilanciate `make test` dopo ogni correzione.
3. Il test `01_interi` viene superato anche dal programma sbagliato. Perche'? Che cosa insegna questo sui test?
4. Spiegate perche' l'indice `pos` dell'array circolare si aggiorna con `pos = (pos + 1) % k`.

**R13.** Scrivete il programma `romani.c` nella cartella `R13_romani`, in modo che superi tutti i test. Il programma riceve il nome di un file che contiene interi e, per ciascuno, stampa la sua scrittura in numeri romani. Requisiti:

- i numeri da $1$ a $3999$ si stampano come `12 = XII`; quelli fuori da questo intervallo non si possono scrivere e si segnalano su `stdout`, come `0: fuori intervallo`; non e' un errore, e il codice di uscita resta $0$;
- se incontra un dato non valido, il programma si ferma con errore, dopo aver stampato le righe dei numeri precedenti;
- un file vuoto non produce nessuna riga (codice $0$);
- un numero di argomenti diverso da uno o un file che non si apre sono errori.

```text
$ cat test/fuori.txt
0 -7 4000 12
$ ./romani test/fuori.txt
0: fuori intervallo
-7: fuori intervallo
4000: fuori intervallo
12 = XII
$ ./romani test/base.txt
1 = I
4 = IV
9 = IX
14 = XIV
40 = XL
90 = XC
400 = CD
900 = CM
1994 = MCMXCIV
2026 = MMXXVI
3999 = MMMCMXCIX
```

Suggerimento: preparate due array paralleli, uno con i valori $1000, 900, 500, 400, \dots, 4, 1$ e uno con i simboli corrispondenti. Per i simboli potete usare un array di stringhe, come `argv`: `char *simboli[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};`.

**R14.** Riprendete il programma di R5 e trasformatelo nel programma `conta.c` della cartella `R14_conta`, che accetta opzioni e piu' file, come il vero `wc`: `./conta [-r] [-p] [-c] file...`. Requisiti:

- le opzioni `-r`, `-p` e `-c` scelgono che cosa stampare (righe, parole, caratteri) e possono comparire in qualsiasi ordine e in qualsiasi posizione, anche dopo i nomi dei file; senza opzioni si stampano tutti e tre i numeri;
- i numeri si stampano sempre nell'ordine righe, parole, caratteri, ciascuno seguito da uno spazio, e poi il nome del file;
- se sulla riga di comando ci sono piu' nomi di file, alla fine c'e' una riga di totali con la parola `totale` al posto del nome, anche se qualcuno dei file non si apre;
- un file che non si apre viene segnalato su `stderr` e saltato, ma alla fine il codice di uscita e' $1$;
- un'opzione sconosciuta (qualsiasi argomento che inizia con `-` e non e' tra le tre) e la mancanza di file sono errori, con codice $1$.

```text
$ ./conta test/dante.txt test/numeri.txt
3 19 104 test/dante.txt
2 5 10 test/numeri.txt
5 24 114 totale
$ ./conta -c -r test/dante.txt
3 104 test/dante.txt
```

Il programma deve scorrere gli argomenti due volte: la prima per raccogliere le opzioni, la seconda per elaborare i file.

**R15.** Questa volta i test li scrivete voi. Nella cartella `R15_ordina` c'e' il programma `ordina.c`, che dovrebbe rispettare questi requisiti:

- legge gli interi di un file (al massimo $100$) e li stampa in ordine crescente, uno per riga: `./ordina [-r] [-u] file`;
- con l'opzione `-r` li stampa in ordine decrescente; con `-u` ogni numero compare una sola volta, anche se nel file e' ripetuto (`3 1 3 2` diventa `1 2 3`); le due opzioni si possono combinare e possono stare in qualsiasi posizione;
- un file vuoto non produce nessuna riga (codice $0$);
- un file con piu' di $100$ numeri, un dato non valido, un'opzione sconosciuta, un numero di file diverso da uno o un file che non si apre sono errori.

I due test forniti vengono superati, ma il programma contiene due errori.

1. Scrivete almeno sei nuovi test, ciascuno con il suo file di dati, il file `.arg` e il file `.atteso` calcolato a mano, pensando ai casi difficili: file vuoto, un solo numero, numeri negativi, numeri ripetuti con e senza `-u`, `-r` e `-u` insieme, un file con piu' di $100$ numeri. Chiamateli `03_...`, `04_...` e cosi' via, perche' vengano eseguiti in ordine. Ricordate che ogni `.atteso` termina con la riga del codice di uscita e un a capo. Per creare il file di $101$ numeri potete usare il terminale: `seq 101 > test/troppi.txt` scrive i numeri da $1$ a $101$, uno per riga.
2. Lanciate `make test`. I vostri test trovano degli errori? Prima di correggere il programma, controllate che non sia sbagliato il test.
3. Trovate gli errori e correggeteli. Uno dei due puo' far scrivere il programma fuori dall'array (F11): quale?
4. Che cosa rende un insieme di test "buono"? Il vostro avrebbe trovato gli errori di R12?

**R16.** Il cifrario di Vigenere generalizza quello di Cesare: invece di uno spostamento fisso usa una parola chiave, e ogni lettera del testo si sposta della quantita' indicata dalla lettera corrispondente della chiave (`a` o `A` vale $0$, `b` vale $1$, e cosi' via), ricominciando dall'inizio della chiave quando e' finita. Con la chiave `lemon`, `ATTACKATDAWN` diventa `LXFOPVEFRNHR`. Scrivete il programma `vigenere.c` nella cartella `R16_vigenere`: `./vigenere -c|-d chiave ingresso uscita`, dove `-c` cifra e `-d` decifra. Requisiti:

- come in R6, le lettere restano minuscole o maiuscole e gli altri caratteri si copiano invariati; la chiave avanza di una posizione solo quando si cifra una lettera;
- la chiave puo' contenere solo lettere, maiuscole o minuscole, con lo stesso significato; altrimenti errore e codice $1$;
- se il nome del file di uscita e' `-`, il programma scrive su `stdout` (e alla fine non lo chiude): e' una convenzione diffusa nei comandi del terminale, ed e' cosi' che i test controllano il risultato;
- un'opzione diversa da `-c` e `-d`, un numero sbagliato di argomenti, un file che non si apre o un file di uscita uguale a quello di ingresso sono errori, con codice $1$. L'ultimo controllo va fatto prima di aprire i file: il test `08_stesso_file` usa una copia, `test/copia.txt`, che un programma sbagliato svuoterebbe.

```text
$ ./vigenere -c lemon test/attacco.txt -
LXFOPVEFRNHR
$ ./vigenere -c Roma test/frase.txt -
Zz pauc q' tioftf, rusjs Oejode.
```

Per scorrere la chiave vi servono la sua lunghezza (`strlen`) e un contatore delle lettere cifrate: la lettera della chiave da usare e' quella di posto `contatore % lunghezza`.

**R17.** Scrivete il programma `sudoku.c` nella cartella `R17_sudoku`, che controlla una griglia di sudoku. Requisiti:

- il file contiene $81$ cifre da `0` a `9`, disposte in $9$ righe; `0` indica una casella vuota e non conta come ripetizione; le cifre di una riga possono essere separate da spazi;
- il programma controlla, in quest'ordine, le righe dalla prima all'ultima, poi le colonne da sinistra a destra, poi i riquadri $3 \times 3$, numerati da $1$ a $9$ da sinistra a destra e dall'alto in basso; anche righe e colonne si numerano da $1$;
- alla prima cifra ripetuta stampa che cosa ha trovato, come `Riga 4: il 2 compare due volte` (oppure `Colonna ...` o `Riquadro ...`), e termina con codice $2$;
- se non trova errori stampa `Griglia valida e completa`, oppure `Griglia valida, caselle vuote: ` seguito dal numero di caselle vuote, con codice $0$;
- un file che non si apre, un carattere diverso da cifre, spazi e a capo, un numero di cifre diverso da $81$ o un numero di argomenti diverso da uno producono codice $1$.

```text
$ ./sudoku test/completa.txt
Griglia valida e completa
$ ./sudoku test/parziale.txt
Griglia valida, caselle vuote: 51
$ ./sudoku test/riga.txt
Riga 4: il 2 compare due volte
$ ./sudoku test/riquadro.txt
Riquadro 1: il 3 compare due volte
```

Mettete la griglia in un array di $81$ elementi, con la casella di riga $r$ e colonna $c$ in posizione `r * 9 + c` (come in R9). La parte piu' delicata sono i riquadri: per il riquadro $b$ (da $0$ a $8$) e la sua casella $k$ (da $0$ a $8$), scrivete su carta le formule della riga e della colonna, poi controllatele, per esempio con gdb (`display` su `r` e `c`) mentre il programma scorre un riquadro. Per sapere se una cifra e' gia' comparsa, usate un array `visto[10]` da azzerare all'inizio di ogni riga, colonna o riquadro.

**R18.** Scrivete il programma `polinomi.c` nella cartella `R18_polinomi`, che fa calcoli su polinomi a coefficienti interi letti da file. Ogni file contiene il grado $n$ (da $0$ a $20$) e poi gli $n + 1$ coefficienti, dal termine noto $a_0$ fino ad $a_n$. Requisiti:

- `./polinomi valuta file x` stampa il valore del polinomio in $x$ intero (schema di Horner, F17), con il formato `p(3) = 5`;
- `./polinomi derivata file` stampa la derivata;
- `./polinomi somma file1 file2` e `./polinomi prodotto file1 file2` stampano la somma e il prodotto;

- i polinomi si stampano dal grado piu' alto al piu' basso, saltando i coefficienti nulli. Il primo termine ha il segno `-` attaccato se e' negativo; gli altri sono preceduti da ` + ` o ` - ` e scritti con il coefficiente in valore assoluto. Un coefficiente $1$ o $-1$ non si scrive, tranne nel termine noto. La potenza si scrive `x^3`, `x^2`, `x` per il primo grado e niente per il termine noto. Il polinomio nullo si stampa `0`;
- un'operazione sconosciuta, un numero sbagliato di argomenti, una $x$ che non e' un intero, un file che non si apre o un file malformato (grado fuori intervallo, coefficienti mancanti o non numerici) sono errori, con codice $1$.

```text
$ cat test/p.txt
3
-1 2 -6 2
$ ./polinomi derivata test/p.txt
6x^2 - 12x + 2
$ ./polinomi prodotto test/p.txt test/q.txt
-2x^5 + 6x^4 - 5x^2 + 2x - 1
$ ./polinomi somma test/x.txt test/q.txt
-x^2 + x + 1
```

Riconoscete l'operazione con `strcmp` e un `enum`. Attenzione al grado del risultato: nella somma i coefficienti piu' alti possono annullarsi (il test `06_somma_nulla` somma un polinomio e il suo opposto). La stampa dei polinomi ha molti casi particolari: quando un test fallisce, in gdb mettete un breakpoint condizionato sul ciclo di stampa per fermarvi proprio sul termine che esce sbagliato.

**R19.** Scrivete il programma `labirinto.c` nella cartella `R19_labirinto`, che trova il percorso piu' breve in un labirinto. Requisiti:

- il file contiene sulla prima riga il numero di righe e di colonne (da $1$ a $40$), poi il labirinto: `#` e' un muro, `.` una casella libera, `S` la partenza ed `E` l'uscita; ci si muove in orizzontale e in verticale;
- il programma stampa la lunghezza del percorso minimo, come `Percorso minimo: 11 passi` (al singolare, `Percorso minimo: 1 passo`), e poi il labirinto con il percorso segnato da `*` (esclusi `S` ed `E`);
- se l'uscita non si puo' raggiungere, stampa soltanto `Uscita irraggiungibile`; in entrambi i casi il codice e' $0$;
- un file senza `S` o senza `E`, con piu' di una `S` o di una `E`, con caratteri diversi da quelli previsti o incompleto, un file che non si apre o un numero di argomenti diverso da uno producono codice $1$.

```text
$ ./labirinto test/esempio.txt
Percorso minimo: 11 passi
S.#....
*##.##.
***#***
.#***#E
...#...
```

Il metodo da usare e' la *visita in ampiezza*. Si parte da `S` a distanza $0$; poi si esaminano le caselle in ordine di distanza: ogni casella libera, non ancora raggiunta, vicina di una casella a distanza $d$ si trova a distanza $d + 1$. Le caselle in attesa di essere esaminate stanno in una *coda*: un array con due indici, `testa` (la prossima da esaminare) e `fondo` (dove aggiungere le nuove). Servono altri due array lunghi quanto il labirinto: `dist`, con la distanza di ogni casella ($-1$ se non ancora raggiunta), e `prec`, con la casella da cui ciascuna e' stata raggiunta, che permette di ripercorrere il cammino all'indietro da `E` a `S`. Perche' il percorso stampato sia unico, i vicini di una casella si esaminano sempre nell'ordine: su, giu', sinistra, destra.

**R20.** **Sfida.** La compressione. La codifica *run-length* (RLE) sostituisce ogni sequenza di caratteri uguali con la sua lunghezza seguita dal carattere: `aaab` diventa `3a1b`, e anche gli a capo e gli spazi si codificano allo stesso modo. Scrivete il programma `rle.c` nella cartella `R20_rle`: `./rle -c ingresso uscita` comprime, `./rle -d ingresso uscita` decomprime, e `-` come uscita vuol dire `stdout` (R16). Requisiti:

- un testo da comprimere non puo' contenere cifre, perche' renderebbero ambigua la decompressione;
- un testo da decomprimere deve essere una sequenza di coppie numero positivo e carattere; un carattere senza numero davanti, un numero $0$ o un numero alla fine del file sono errori;
- in caso di errore il programma non deve scrivere nulla nel file di uscita e termina con codice $1$. Per riuscirci servono due passate: la prima controlla il contenuto senza scrivere, poi `rewind(f)` riporta la lettura all'inizio del file e la seconda passata scrive. Il file di uscita si apre solo dopo la prima passata, cosi' in caso di errore un file gia' esistente non viene svuotato;
- opzioni e argomenti sbagliati, file che non si aprono e file di uscita uguale a quello di ingresso sono errori, con codice $1$.

```text
$ cat test/testo_1.txt
aaabccccccccccccd

  xx
$ ./rle -c test/testo_1.txt -
3a1b12c1d2
2 2x1
```

(Nell'output compresso, `1d2` seguito da un a capo significa: una `d`, poi due a capo.)

1. Scrivete il programma e fate passare tutti i test.
2. I test controllano compressione e decompressione separatamente. Controllate che vadano d'accordo: comprimete ciascun file `test/testo_*.txt` in un file di prova, decomprimete il risultato e confrontatelo con l'originale usando `diff`. Che cosa deve stampare `diff`, se tutto funziona?
3. Aggiungete almeno due test vostri, uno per la compressione e uno per un errore di formato nella decompressione. Attenzione: un editor aggiunge quasi sempre un a capo alla fine del file, e in un file da decomprimere quell'a capo e' un carattere senza numero davanti. Per creare un file `.rle` esattamente come lo volete, usate `printf`, per esempio `printf '3a2b' > test/mio.rle`.
4. Su quali testi la compressione RLE allunga il file invece di accorciarlo? Usate `wc -c` per confrontare le lunghezze.


## Pacchetto S: qsort e bsearch

Nei Pacchetti G e H avete scritto a mano ordinamenti e ricerche, e con `time` e gprof avete visto quanto possono costare. La libreria standard (Pacchetto O) ne offre due versioni pronte, in `stdlib.h`: `qsort` ordina un array e `bsearch` ci cerca un valore con la ricerca binaria. Sono veloci: `qsort` usa algoritmi molto piu' furbi dei tre dei Pacchetti G e H, e quando il numero di elementi raddoppia il suo tempo cresce di poco piu' del doppio, non di quattro volte. Funzionano con array di qualsiasi tipo, e proprio per questo chiedono un piccolo sforzo: bisogna scrivere una *funzione* che dica come confrontare due elementi. Cominciamo da li'.

Gli esercizi di questo pacchetto sono pochi e lunghi, e riprendono tutto: gli argomenti della riga di comando, i file e `make test` del Pacchetto R, `time`, `-O2` e gprof dei Pacchetti G e H, la libreria standard del Pacchetto O. Nel materiale (la cartella `materiale_difficili`) c'e' una cartella per ogni esercizio: quelle di S1, S2 e S5 contengono il Makefile e i test, come in R11-R20; quelle di S3 e S4 i file di dati. Valgono le regole di R: compilate con `gcc -g -Wall -Wextra`, i messaggi di errore vanno su `stderr` e in caso di errore il programma termina con codice $1$.

### Le funzioni, in breve

Una funzione e' un pezzo di programma con un nome, che riceve dei valori e ne restituisce uno. Anche `main` e' una funzione.

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

- La prima riga dice il tipo del valore restituito (`int`), il nome della funzione (`quadrato`) e, tra parentesi, i *parametri*, ciascuno con il suo tipo.
- `return` termina la funzione e restituisce il valore.
- La funzione si scrive prima di `main`, cosi' quando `main` la usa il compilatore la conosce gia'.
- Una funzione puo' chiamarne un'altra, scritta piu' in alto.
- I parametri sono copie: se la funzione cambia `x`, la variabile `a` di `main` non cambia. Le variabili dichiarate dentro una funzione esistono solo li'; quelle dichiarate prima di tutte le funzioni, come gli array grandi di H6, sono visibili da tutte.

Per ora basta questo: le funzioni sono il tema del Pacchetto I dell'eserciziario facile.

### Ordinare con qsort

`qsort` non sa come confrontare gli elementi dell'array: glielo dice una funzione scritta da noi, il *comparatore*, che riceve due elementi e restituisce un numero negativo se il primo deve venire prima del secondo, positivo se deve venire dopo, $0$ se per l'ordinamento sono equivalenti. Ecco la ricetta per un array di `int` in ordine crescente:

```c
#include <stdlib.h>

int confronta(const void *a, const void *b) {
    int x = *(const int *) a;       /* il primo elemento da confrontare */
    int y = *(const int *) b;       /* il secondo */
    if (x < y) {
        return -1;
    } else if (x > y) {
        return 1;
    } else {
        return 0;
    }
}

/* in main, per ordinare i primi n elementi dell'array v: */
qsort(v, n, sizeof(v[0]), confronta);
```

`qsort` riceve l'array, il numero di elementi da ordinare, la dimensione in byte di un elemento (con `sizeof`, come in F1 e N14) e il nome del comparatore, che chiamera' tutte le volte che gli serve confrontare due elementi. Le due righe che definiscono `x` e `y` sono la parte misteriosa: `a` e `b` non sono gli elementi, ma i loro *indirizzi* in memoria, e `*(const int *) a` vuol dire "l'`int` che si trova all'indirizzo `a`". Per ora leggetele come una formula da copiare, come `char *argv[]` in R; i puntatori sono un argomento che incontrerete piu' avanti. Per un array di `double` basta scrivere `double` al posto di `int` nelle due righe (e come tipo di `x` e `y`). Per l'ordine decrescente basta scambiare `-1` e `1`.

### Cercare con bsearch

`bsearch` esegue la ricerca binaria di F20 in un array *gia' ordinato* con lo stesso comparatore. Riceve l'indirizzo del valore da cercare (`&x`, come in `scanf`), poi gli stessi argomenti di `qsort`. Restituisce l'indirizzo dell'elemento trovato, oppure `NULL` (come `fopen` in R) se il valore non c'e'. Anche qui c'e' una piccola ricetta: se l'elemento e' stato trovato, la sua posizione nell'array e' `p - v`.

```c
int *p;
int x = 42;
p = bsearch(&x, v, n, sizeof(v[0]), confronta);
if (p == NULL) {
    printf("%d non c'e'\n", x);
} else {
    printf("%d e' in posizione %d\n", x, (int) (p - v));
}
```

Se il valore compare piu' volte, `bsearch` puo' restituire uno qualsiasi degli elementi uguali.

### gdb e gprof con le funzioni

- `break confronta` (con il nome di una funzione al posto del numero di riga) ferma il programma all'inizio della funzione, ogni volta che viene chiamata.
- **Comando nuovo: `bt`** (*backtrace*). Quando il programma e' fermo dentro una funzione, `bt` mostra la catena delle chiamate che l'hanno portato li': in cima la funzione in cui si trova, sotto quella che l'ha chiamata, e cosi' via fino a `main`.
- gprof senza `-l` mostra il tempo per funzione, ma solo per le funzioni compilate con `-pg`, cioe' le vostre: il tempo passato dentro `qsort` e `bsearch`, che fanno parte della libreria, non lo vede, e nemmeno conta le volte che `qsort` chiama il vostro comparatore. Per sapere quante volte viene chiamato, usate un contatore: una variabile `long` dichiarata prima delle funzioni, che il comparatore aumenta di uno a ogni chiamata. Il resoconto per righe (`-l`) resta invece utile per i cicli scritti da voi.

### Esercizi (S1-S5)

**S1.** Scrivete il programma `ordina.c` nella cartella `S1_ordina`, che legge gli interi di un file e li stampa ordinati con `qsort`, uno per riga: `./ordina [-r] [-a | -c] file`. Requisiti:

- senza opzioni, l'ordine e' crescente;
- con `-a` i numeri si ordinano per valore assoluto crescente; a parita' di valore assoluto, viene prima il negativo ($-3$ prima di $3$);
- con `-c` si ordinano per ultima cifra crescente (l'ultima cifra del valore assoluto: per $-12$ e' $2$); a parita' di ultima cifra, per valore crescente;
- con `-r` la sequenza ottenuta si stampa al contrario, dall'ultimo elemento al primo; `-r` si puo' combinare con `-a` o con `-c`;
- le opzioni possono stare in qualsiasi posizione, e al massimo una tra `-a` e `-c`;
- i numeri sono al massimo $1000000$, in un array dichiarato prima delle funzioni; un file vuoto non produce nessuna riga (codice $0$); potete supporre che con `-a` e `-c` il file non contenga $-2147483648$, il cui valore assoluto non entra in un `int` (F2);
- un numero di file diverso da uno, un'opzione sconosciuta, `-a` insieme a `-c`, un file che non si apre, un dato non valido o piu' di $1000000$ numeri sono errori, con codice $1$.

Scrivete un comparatore per ogni criterio: `confronta_valore`, `confronta_assoluto` e `confronta_cifra`. Negli ultimi due, in caso di parita', potete restituire direttamente `confronta_valore(a, b)`.

```text
$ cat test/numeri.txt
3 -1 4 1 -5 9 2 -6 5 3
$ ./ordina -a test/numeri.txt
-1
1
2
3
3
4
-5
5
-6
9
```

1. Fate passare tutti i $14$ test.
2. Un compagno ha scritto `confronta_valore` in una riga sola: `return x - y;`. Provatela: quale test fallisce, e perche'? (Rivedete F2.) Si puo' scrivere comunque il comparatore in una riga, senza rischi? Suggerimento: quanto vale `(x > y) - (x < y)`?
3. **Con gdb.** Mettete un breakpoint con `break confronta_valore`, lanciate `run test/numeri.txt` e date `bt`: da chi e' stata chiamata la funzione? (I nomi delle funzioni interne di `qsort` possono cambiare da un computer all'altro.) Dopo due `next`, che cosa valgono `x` e `y`?
4. Contate le chiamate a `confronta_valore` con un contatore `long chiamate`, dichiarato prima delle funzioni, e stampatelo alla fine con `fprintf(stderr, ...)`: perche' su `stderr` e non su `stdout`? Per avere file grandi, scrivete un programmino `genera.c` che riceve $N$ sulla riga di comando e stampa $N$ numeri casuali (`srand(1)` e `rand()`), uno per riga; per esempio `./genera 1000000 > milione.txt`. Completate la tabella: le chiamate sono vicine a $N \log_2 N$? Quanti confronti farebbe il selection sort di G16?

| $N$ | $1000$ | $100000$ | $1000000$ |
| --- | --- | --- | --- |
| Chiamate a `confronta_valore` |  |  |  |
| $N \log_2 N$ (circa) | $10^4$ | $1.7 \cdot 10^6$ | $2 \cdot 10^7$ |
| Confronti del selection sort |  |  |  |

5. **Con time.** Quanto impiega `./ordina milione.txt > ordinati.txt`? Confrontate con l'insertion sort di G17 su $40000$ numeri. Misurate anche il tempo con $500000$ numeri: per quanto si moltiplica il tempo quando $N$ raddoppia?

**S2.** Nella cartella `S2_comuni` c'e' il programma `comuni.c`, corretto ma lento: `./comuni [-l] primo secondo` legge gli interi di due file (al massimo $1000000$ ciascuno) e stampa quanti numeri del primo file compaiono anche nel secondo; i numeri ripetuti nel primo file si contano ogni volta. Con `-l`, che puo' stare in qualsiasi posizione, stampa prima anche questi numeri, uno per riga, nell'ordine del primo file. Un numero di file diverso da due, un'opzione sconosciuta, un file che non si apre, un dato non valido o troppi numeri sono errori.

```text
$ cat test/a.txt
7 3 12 7 5 20 1 8
$ cat test/b.txt
1 2 3 5 8 13 21
$ ./comuni -l test/a.txt test/b.txt
3
5
1
8
Presenti nel secondo file: 4 su 8
```

1. Lanciate `make test`: quale test fallisce, e con quale codice di uscita? Rivedete la seconda parte del Pacchetto R: che cosa significa? Lanciate a mano quel test con `time` (ci vuole pazienza): quanto impiega il programma?
2. **Con gprof.** Con il resoconto per righe, sui file del test grande: quale riga occupa quasi tutto il tempo? Circa quante volte viene eseguita?
3. Riscrivete la parte di ricerca usando `qsort` e `bsearch`: ordinate una volta sola l'array del secondo file, poi cercate con `bsearch` ogni numero del primo. Tutti i $10$ test devono passare. Perche' si puo' ordinare il secondo file e non il primo?
4. Contate, come in S1, le chiamate al comparatore nel test grande e confrontatele con una stima: quanti confronti servono, circa, per ordinare il secondo file ($N_2 \log_2 N_2$), e quanti per le $N_1$ ricerche binarie?
5. **Con time.** Quanto impiega ora il programma sul test grande?
6. **In piu'.** Se si potessero ordinare entrambi i file, non servirebbe nemmeno `bsearch`: basterebbero due indici che avanzano insieme, come nella fusione di G6. Scrivete questa versione, che con `-l` stampa i numeri comuni in ordine crescente. Quanti confronti fa, dopo gli ordinamenti?

**S3.** La media e' molto sensibile ai valori sbagliati: basta un errore di battitura per spostarla di molto. Per questo in statistica si usano spesso i *quartili*, che si calcolano sui dati ordinati. Scrivete un programma `quantili.c` (che usa `math.h`: compilatelo con `-lm`, O1) che riceve il nome di un file di numeri reali e stampa: quanti sono, minimo, primo quartile, mediana, terzo quartile, massimo, media e deviazione standard (come in O8), tutti con due decimali, e infine i *valori anomali*. Requisiti:

- i numeri, al massimo $1000000$, si leggono in un array `double` e si ordinano con `qsort`;
- il quantile di livello $p$ (con $p$ uguale a $0$, $0.25$, $0.5$, $0.75$ e $1$ per minimo, quartili, mediana e massimo) si calcola cosi', con l'array ordinato `v` di `n` elementi: $h = (n - 1) \cdot p$, $k$ e' la parte intera di $h$ (`floor`), e il quantile vale `v[k] + (h - k) * (v[k + 1] - v[k])`, oppure semplicemente `v[k]` se $k = n - 1$;
- detta $IQR$ la differenza tra terzo e primo quartile, un valore e' anomalo se e' minore di $Q_1 - 1.5 \cdot IQR$ o maggiore di $Q_3 + 1.5 \cdot IQR$; i valori anomali si stampano in ordine crescente, dopo gli estremi dell'intervallo, oppure si stampa `nessuno`;
- un numero di argomenti diverso da uno, un file che non si apre, un dato non valido, un file senza numeri o troppi numeri sono errori.

Il file `tempi.txt` della cartella `S3_quantili` contiene i tempi di reazione, in millisecondi, di $25$ persone a un segnale luminoso; due misure sono state registrate male.

```text
$ ./quantili tempi.txt
Valori letti: 25
Minimo: 268.00
Primo quartile: 288.00
Mediana: 299.00
Terzo quartile: 315.00
Massimo: 1450.00
Media: 374.68
Deviazione standard: 261.42
Valori anomali (fuori da [247.50, 355.50]): 1020.00 1450.00
```

1. Controllate a mano la mediana e i quartili, contando sui dati ordinati. Con un numero pari di dati, che cosa calcola la formula per la mediana?
2. Togliete dal file i due valori anomali: di quanto cambia la media? E la mediana? Quale delle due descrive meglio il tempo di reazione tipico?
3. Un compagno ha scritto il comparatore cosi': `return (int) (x - y);`. Con `tempi.txt` sembra funzionare, ma con il file `piccoli.txt`, che contiene numeri tra $0$ e $1$, stampa un minimo piu' grande del massimo. **Con gdb.** Fermatevi nel comparatore, con `break` seguito dal suo nome, e dopo qualche `next` provate `print x - y` e `print (int) (x - y)`: che cosa crede `qsort` di tutte le coppie?
4. Modificate il programma di O10 perche' stampi i suoi $100000$ numeri, uno per riga con `%f`, invece delle statistiche, e salvateli con `./campana > normali.txt`. Per la curva a campana con media $0$ e deviazione standard $1$, i quartili valgono circa $-0.674$ e $0.674$, e i valori anomali sono circa lo $0.7\%$: e' quello che trovate?
5. **Con time.** Con un milione di numeri (portate `N` a $1000000$ in O10), quanto impiega il programma? Usando i tempi di G17, stimate quanto impiegherebbe se ordinasse con l'insertion sort.

**S4.** Riprendiamo i giudici e i candidati di H2, questa volta con una classifica completa. Scrivete un programma `classifica.c` che riceve il nome di un file e stampa la classifica dei candidati. Requisiti:

- il file contiene sulla prima riga il numero di giudici (da $1$ a $20$) e il numero di candidati (da $1$ a $100$), poi una riga per giudice con i voti, da $0$ a $5$, che ha dato ai candidati, nell'ordine;
- i candidati si ordinano per punteggio totale decrescente; a parita' di totale, per numero di voti $5$ ricevuti, decrescente; a parita' anche di questo, per numero di candidato crescente (i candidati si numerano da $1$);
- per ogni candidato si stampano la posizione, il numero, il totale e il numero di voti $5$, con il formato `"%4d %9d %6d %6d\n"`, sotto l'intestazione `Pos. Candidato Totale Voti 5`;
- due candidati con lo stesso totale e lo stesso numero di voti $5$ sono a pari merito e hanno la stessa posizione; il candidato successivo prende la posizione che gli spetterebbe contando tutti quelli che lo precedono (come nello sport: $1, 1, 3, \dots$);
- argomenti sbagliati, un file che non si apre, numeri di giudici o candidati fuori intervallo, un voto mancante, non numerico o fuori da $0$-$5$ sono errori; per un voto sbagliato, il messaggio indica giudice e candidato.

Per ordinare i candidati con `qsort`, mettete i loro dati in una matrice `int dati[MAX_C][3]`, una riga per candidato con numero, totale e voti $5$, e ordinate le righe: `qsort(dati, c, sizeof(dati[0]), confronta);`. Ogni elemento dell'array e' una riga intera, quindi nel comparatore la ricetta cambia un poco: `const int *r1 = (const int *) a;` permette di leggere la prima riga come `r1[0]`, `r1[1]` e `r1[2]`, e lo stesso per `r2` con `b`.

```text
$ ./classifica voti.txt
Pos. Candidato Totale Voti 5
   1         2     21      2
   1         4     21      2
   3         6     20      1
   4         9     19      2
   5         7     19      1
   5         8     19      1
   7        12     19      0
   8        10     18      1
   8        11     18      1
  10         1     17      1
  11         3     12      0
  12         5      8      0
```

1. Con il file `voti_errati.txt` il programma deve terminare con un errore, indicando il giudice $3$ e il candidato $8$.
2. **Con gdb.** Fermatevi subito prima di `qsort` e date `print dati[0]` e `print dati[0]@3`. Poi fermatevi nel comparatore e, dopo due `next` (cosi' `r1` e `r2` hanno un valore), provate `print *r1@3` e `print *r2@3`: quali candidati sta confrontando `qsort`?
3. Lo standard del C non garantisce che `qsort` lasci nell'ordine di partenza gli elementi che il comparatore considera equivalenti (si dice che non e' *stabile*), anche se sul vostro computer puo' sembrare che lo faccia. Che cosa potrebbe succedere alla classifica senza il terzo criterio, quello sul numero di candidato?
4. Aggiungete, dopo quella dei candidati, la classifica dei giudici, dal piu' severo (meno punti assegnati in tutto) al piu' generoso, a parita' per numero di giudice crescente, con un secondo comparatore.

**S5.** **Sfida.** Il problema delle *tre somme*: dato un insieme di numeri interi tutti diversi, trovare tutte le terne di numeri che hanno somma $0$. Scrivete il programma `tresomme.c` nella cartella `S5_tresomme`: `./tresomme [-1 | -2 | -3] file`. Requisiti:

- i numeri del file, al massimo $100000$, sono compresi tra $-100000000$ e $100000000$ (cosi' la somma di tre numeri sta in un `int`) e devono essere tutti diversi; altrimenti e' un errore;
- il programma ordina i numeri con `qsort` e stampa le terne $a < b < c$ con $a + b + c = 0$, una per riga (`-6 -1 7`), in ordine crescente di $a$ e, a parita' di $a$, di $b$; alla fine stampa `Terne: ` seguito dal numero di terne;
- il metodo si sceglie con l'opzione, che puo' stare in qualsiasi posizione (senza opzione si usa `-3`):
    - `-1`: tre cicli uno dentro l'altro, sulle posizioni $i < j < k$ dell'array ordinato;
    - `-2`: due cicli su $i < j$, e per il terzo numero, che deve valere $-(a + b)$, una ricerca con `bsearch` tra gli elementi che seguono la posizione $j$; ricetta: l'array che comincia dalla posizione `j + 1` si scrive `v + j + 1`, e ha `n - j - 1` elementi;
    - `-3`: per ogni $i$, due indici, `sinistra` che parte da $i + 1$ e `destra` che parte da $n - 1$; finche' `sinistra < destra`, se la somma dei tre numeri e' $0$ si stampa la terna e si spostano entrambi gli indici verso il centro, se e' minore di $0$ si aumenta `sinistra`, altrimenti si diminuisce `destra`;
- un numero di file diverso da uno, un'opzione sconosciuta, piu' di un metodo, un file che non si apre, un dato non valido, un numero fuori intervallo o ripetuto, troppi numeri sono errori.

```text
$ cat test/piccolo.txt
-4 7 2 -1 0 3 -6 5 1 -2 9
$ ./tresomme test/piccolo.txt
-6 -1 7
-6 1 5
-4 -1 5
-4 1 3
-2 -1 3
-2 0 2
-1 0 1
Terne: 7
```

1. Fate passare tutti gli $11$ test. Due di essi usano il file `test/grande.txt`, con $4000$ numeri: provate a lanciare a mano il metodo `-1` su quel file. Perche' non c'e' un test grande per il metodo `-1`?
2. Perche', con l'array ordinato, i tre metodi stampano le terne nello stesso ordine? E perche' serve che i numeri siano tutti diversi?
3. Spiegate perche' il metodo `-3` non perde nessuna terna. Suggerimento: se la somma e' minore di $0$, quale dei tre numeri conviene cambiare per farla crescere? Il numero `v[sinistra]` potrebbe ancora far parte di una terna con `v[i]` e un elemento a sinistra di `destra`?
4. **Con time.** La cartella `dati` contiene file di numeri tutti diversi, da $1000$ a $32000$ numeri. Completate la tabella, misurando ogni metodo solo nelle caselle senza trattino (per il metodo `-1` con $4000$ numeri ci vuole pazienza), e per ogni metodo calcolate per quanto si moltiplica il tempo quando $N$ raddoppia. Quante volte, circa, viene eseguito il ciclo piu' interno del metodo `-1`? E quante volte, in tutto, il ciclo del metodo `-3`?

| $N$ | $1000$ | $2000$ | $4000$ | $8000$ | $16000$ | $32000$ |
| --- | --- | --- | --- | --- | --- | --- |
| Metodo `-1` |  |  |  | - | - | - |
| Metodo `-2` | - |  |  |  |  | - |
| Metodo `-3` | - | - |  |  |  |  |

5. **Con time.** Compilate a mano con `-O2` e ripetete la misura del metodo `-1` con $2000$ e $4000$ numeri: l'ottimizzazione cambia il fattore con cui cresce il tempo? Che cosa conta di piu', il compilatore o l'algoritmo?
6. **Con gprof.** Con il metodo `-1` e il file di $2000$ numeri, il resoconto per righe mostra dove passa il tempo. Con il metodo `-2`, invece, gran parte del tempo e' dentro `bsearch`: che cosa mostra gprof, e perche' (rivedete l'introduzione del pacchetto)?


## Pacchetto T: Integrazione e modularita'

Tutti i programmi che avete scritto finora stavano in un file solo. I programmi veri no: sono fatti di decine, a volte migliaia di file, e nessuno li guarda tutti insieme. In questo pacchetto si vede perche', e soprattutto **come** quei pezzi diventano un programma unico.

Non vi chiederemo di inventare la divisione in moduli, che e' un mestiere a se': i moduli ve li diamo noi, gia' scritti e documentati. Quello che dovete portare a casa e' un'altra cosa: che cosa sta in un file `.h` e che cosa in un `.c`, che cosa fa ciascuna delle fasi che costruiscono il programma, e come si legge un messaggio di errore per capire *quale* fase si e' lamentata. E' la differenza tra un errore che vi blocca per un pomeriggio e uno che risolvete in trenta secondi.

Nel materiale (la cartella `materiale_difficili`) c'e' una cartella per ogni esercizio, con i moduli gia' pronti e il Makefile. I test ci sono solo in `T1_vettore` e in `T5_rapporto`, che sono gli esercizi in cui scrivete del codice; nelle altre tre cartelle i comandi utili sono soltanto `make` e `make clean`. Valgono le regole di R: compilate con `gcc -g -Wall -Wextra`, i messaggi di errore vanno su `stderr` e in caso di errore il programma termina con codice $1$.

**Due avvertenze prima di cominciare, da leggere adesso e non dopo.**

*Se il vostro gcc e' la versione 14 o piu' recente* (lo dice `gcc --version`), una chiamata a una funzione mai dichiarata non e' piu' un avviso ma un errore, e due esercizi di questo pacchetto si reggono proprio su quell'avviso. In T2 e in T3, dove il testo ve lo dira', aggiungete al comando il flag `-Wno-error=implicit-function-declaration`, che riporta il comportamento a quello delle versioni precedenti. Il flag e' accettato da tutte le versioni, quindi potete metterlo sempre senza pensarci.

*Se lavorate su macOS*, i messaggi del collegatore sono diversi da quelli riportati qui, che sono quelli di Linux e di WSL: al posto di `undefined reference to 'x'` leggerete `Undefined symbols for architecture ...`, al posto di `multiple definition of 'x'` leggerete `duplicate symbol '_x'`, e il collegatore si chiama `ld` ma senza il percorso `/usr/bin/`. Anche `nm` si comporta un po' diversamente: antepone un `_` a ogni nome, quindi vedrete `_main` al posto di `main`. Le lettere, che sono la cosa che conta, sono le stesse.

### Perche' spezzare un programma in piu' file

Tre motivi, in ordine di importanza crescente.

- **Si ricompila solo cio' che e' cambiato.** Un programma di centomila righe in un file solo va ricompilato tutto a ogni virgola spostata. Diviso in cinquanta file, se ne ricompila uno.
- **Ogni file e' un'idea sola.** Chi cerca il calcolo della mediana apre `statistiche.c` e non gli altri quarantanove. Chi lo modifica sa di non poter rompere nient'altro, purche' non cambi il modo in cui si chiama.
- **Un modulo si riusa senza copiarlo.** Questo lo state facendo da B1: `printf` non l'avete mai scritta e non ne avete mai visto il codice, eppure la usate. Di `stdio.h` conoscete solo le dichiarazioni; il corpo delle funzioni e' altrove, gia' compilato. Un modulo vostro funziona allo stesso identico modo.

### Dichiarazione e definizione

E' la distinzione su cui si regge tutto il pacchetto, e la conoscete gia' da I senza saperlo.

- Una **dichiarazione** dice che qualcosa esiste e come si usa, senza crearlo. Il prototipo `double media(int v[], int n);` e' una dichiarazione: basta al compilatore per controllare le chiamate.
- Una **definizione** e' la cosa vera: il corpo della funzione tra graffe, o la variabile che occupa spazio in memoria.

Di una stessa funzione ci possono essere **tante dichiarazioni** (una in ogni file che la usa) ma **una sola definizione** in tutto il programma. Da qui la divisione del lavoro:

| File | Che cosa contiene | Chi lo legge |
| --- | --- | --- |
| `vettore.h` (intestazione, o *header*) | le dichiarazioni: prototipi, `#define`, `typedef` e `struct` che compaiono nei prototipi, con la documentazione Doxygen | il compilatore, ogni volta che qualcuno scrive `#include "vettore.h"`; e voi, per sapere come si usa il modulo |
| `vettore.c` | le definizioni: i corpi delle funzioni | il compilatore, una volta sola |

Nell'intestazione, quindi, **non** si scrivono corpi di funzioni ne' variabili: finirebbero duplicati in ogni file che la include, e il collegamento fallirebbe. In T2 e T3 vedrete succedere esattamente questo.

### Le quattro fasi, finalmente per esteso

In B10 avevate messo in ordine quattro fasi: editing, compilazione, link, esecuzione. Adesso potete vederle una per una, perche' con piu' file non si possono piu' confondere.

| Fase | Comando | Che cosa entra | Che cosa esce |
| --- | --- | --- | --- |
| Precompilazione | `gcc -E main.c` | `main.c` | un unico testo in cui ogni `#include` e' stato sostituito dal contenuto del file e ogni macro e' stata espansa |
| Compilazione | `gcc -c main.c` | un `.c` (gia' precompilato) | `main.o`, il *file oggetto*: il codice macchina di quel file soltanto, con dei buchi dove si chiamano funzioni che stanno altrove |
| Collegamento | `gcc -o prog main.o vettore.o` | tutti i `.o` e le librerie | l'eseguibile `prog`, con i buchi riempiti |
| Esecuzione | `./prog` | l'eseguibile | il risultato |

Due conseguenze che vi serviranno a leggere i messaggi di errore:

- il compilatore lavora su **un file per volta** e non sa niente degli altri. Se chiamate una funzione che non ha mai visto dichiarata, se ne lamenta subito (`implicit declaration`); ma se la dichiarazione c'e', si fida e va avanti, anche se la definizione non esiste da nessuna parte;
- il collegatore (*linker*) vede **tutti** i `.o` insieme e non sa piu' niente del C: conosce solo nomi. Se un nome manca dice `undefined reference`, se ne trova due uguali dice `multiple definition`. Un errore che nomina `/usr/bin/ld` o una di queste due frasi viene sempre dal collegamento, mai dalla compilazione.

### Guardare dentro un file oggetto

Il comando `nm` elenca i nomi contenuti in un `.o`. Ogni riga ha una lettera che dice di che cosa si tratta:

```text
$ nm main.o
0000000000000000 T main
                 U vettore_media
                 U vettore_minimo
```

(L'elenco qui sopra e' accorciato: `nm` stampa anche i nomi che vengono dalla libreria standard, come `printf` e `fopen`, e li ordina alfabeticamente.)

- `T` (*text*) e' una funzione **definita** qui e visibile dagli altri file;
- `D` e' una variabile definita qui, con un valore iniziale, visibile dagli altri;
- `B` e' una variabile definita qui senza valore iniziale, visibile dagli altri;
- `U` (*undefined*) e' un nome **usato** qui ma definito altrove: e' uno dei buchi che il collegamento deve riempire;
- le stesse lettere **minuscole** (`t`, `d`, `b`) indicano qualcosa che e' definito qui ma **non** e' visibile dagli altri file: ci si arriva con `static`, come vedrete in T3;
- i nomi che iniziano con due trattini bassi, come `__assert_fail`, non li avete scritti voi: li aggiungono le macro e il compilatore, e si possono ignorare. Per toglierli di mezzo: `nm main.o | grep -v __`.

Se `nm` non e' installato lo si ottiene con `sudo apt install binutils`; non e' indispensabile per svolgere gli esercizi, ma e' il modo piu' diretto per capire che cosa sta succedendo.

### Le guardie di inclusione

Un'intestazione puo' finire inclusa due volte senza che nessuno l'abbia chiesto: basta che `main.c` includa sia `punto.h` sia `segmento.h`, e che `segmento.h` a sua volta includa `punto.h`. Il preprocessore copia il testo tutte le volte che glielo si chiede, e il compilatore si trova `struct punto` definita due volte: `error: redefinition of 'struct punto'`.

La soluzione e' una formula che troverete in cima a ogni intestazione del mondo:

```c
#ifndef PUNTO_H          /* se PUNTO_H non e' ancora stato definito... */
#define PUNTO_H          /* ...definiscilo, e prosegui */

/* ... contenuto dell'intestazione ... */

#endif
```

La prima volta `PUNTO_H` non esiste, quindi il contenuto viene copiato e il nome viene definito; la seconda volta il nome c'e' gia' e il preprocessore salta tutto fino a `#endif`. Il nome si sceglie dal nome del file, in maiuscolo: e' solo una convenzione, ma due intestazioni con la stessa guardia si cancellerebbero a vicenda.

### `#include "mio.h"` e `#include <stdio.h>`

Le virgolette dicono a gcc di cercare il file **accanto al sorgente**, e solo dopo tra le intestazioni di sistema; le parentesi angolari di cercarlo **solo** tra quelle di sistema. Per le vostre intestazioni servono le virgolette.

### static ed extern tra file diversi

In J avevate lasciato in sospeso due parole. Adesso hanno senso, perche' adesso i file sono piu' di uno.

- `static` davanti a una funzione o a una variabile **globale** non ne cambia la vita, ne cambia la *visibilita'*: quel nome esiste solo dentro il suo file, e gli altri non possono nominarlo nemmeno sapendo come si chiama. E' il modo di dire "questo e' un attrezzo mio, non fa parte di quello che offro". Nel `.h` non compare.
- `extern` davanti a una variabile e' una **dichiarazione**: dice "questa variabile esiste, ma e' definita altrove". Si scrive nell'intestazione; la definizione, senza `extern`, sta in uno e un solo `.c`. Cosi' tutti i file che includono l'intestazione vedono la stessa identica variabile.

Per le funzioni `extern` non serve: un prototipo e' gia' una dichiarazione, e in un'intestazione e' sottinteso.

### Il Makefile a piu' oggetti

Il Makefile di questo pacchetto e' diverso da quello di R e S, perche' qui il programma nasce da piu' sorgenti. Le righe che contano sono tre:

```make
PROG = statistiche
OGGETTI = main.o vettore.o
INTESTAZIONI = vettore.h

$(PROG): $(OGGETTI)
	$(CC) $(CFLAGS) -o $(PROG) $(OGGETTI)

%.o: %.c $(INTESTAZIONI)
	$(CC) $(CFLAGS) -c $<
```

La prima regola e' il collegamento: l'eseguibile dipende dai `.o`, quindi va rifatto se uno di loro e' piu' recente. La seconda e' la compilazione, scritta una volta per tutti i file: `%.o: %.c` si legge "un qualsiasi `.o` si ottiene dal `.c` che ha lo stesso nome", e `$<` significa "il primo file da cui dipende", cioe' quel `.c`.

Notate `$(INTESTAZIONI)` nella seconda regola: dice che un `.o` va rifatto **anche** quando cambia un'intestazione. Make non legge i sorgenti e non sa che cosa includono: se non glielo dite, non se ne accorge. In T4 vedrete che cosa succede quando ce lo si dimentica.

### Controlli sugli array durante l'esecuzione

Un ultimo strumento, che non c'entra con i moduli ma che da qui in avanti vi conviene tenere a portata di mano. Il flag `-fsanitize=address` aggiunge al programma dei controlli che scattano **mentre il programma gira**, e che segnalano gli accessi fuori da un array, quelli che `-Wall` non puo' vedere perche' dipendono dai dati:

```bash
gcc -g -Wall -Wextra -fsanitize=address -o prog main.c vettore.c
```

Se il programma esce da un array si ferma da solo con un messaggio che inizia con `ERROR: AddressSanitizer: stack-buffer-overflow` e dice in quale funzione e a quale riga. Rallenta parecchio l'esecuzione, quindi si usa mentre si sviluppa e non nella versione finale. Provatelo anche sui programmi dei pacchetti precedenti: e' il modo piu' rapido per scoprire un indice sbagliato.

### Esercizi (T1-T5)

**T1.** Nella cartella `T1_vettore` trovate un modulo gia' pronto, `vettore.h` e `vettore.c`, il Makefile e i test. Manca il `main.c`, e lo scrivete voi.

Il programma si chiama `statistiche`, riceve sulla riga di comando il nome di un file di interi e stampa cinque righe:

```text
$ cat test/numeri.txt
3 1 4 1 5
9 2 6 5 3
$ ./statistiche test/numeri.txt
Numeri letti: 10
Minimo: 1
Massimo: 9
Media: 3.90
Sopra la media: 5
Ordinati: 1 1 2 3 3 4 5 5 6 9
```

Requisiti:

- i numeri sono al massimo `VETTORE_MAX`, che e' definito nell'intestazione: non scrivete $1000$ a mano nel `main`;
- "Sopra la media" conta i valori **strettamente** maggiori della media;
- l'ordinamento lo fa il modulo, non voi;
- l'ultima riga e' la parola `Ordinati:` seguita, per ogni elemento, da uno spazio e dal numero, **senza spazio finale**: in C si ottiene con `printf("Ordinati:");` e poi `printf(" %d", v[i]);` dentro il ciclo. I test confrontano l'output carattere per carattere, e uno spazio di troppo in fondo alla riga li fa fallire senza che si veda niente;
- un numero di argomenti diverso da uno, un file che non si apre, un file senza numeri, un dato non valido o piu' di `VETTORE_MAX` numeri sono errori, con messaggio su `stderr` e codice di uscita $1$. Attenzione al confine: un file con **esattamente** `VETTORE_MAX` numeri e' valido e va elaborato, non rifiutato. Un ciclo scritto come `while (n < VETTORE_MAX && fscanf(...) == 1)` seguito da un controllo su `feof` sbaglia proprio su quel caso: capite perche' prima di scrivere il vostro, e guardate il test `07_limite`.

**Scrivete il `main.c` senza mai aprire `vettore.c`.** Vi serve solo `vettore.h`: e' esattamente la situazione di I2, ma questa volta il corpo delle funzioni non e' nemmeno nello stesso file.

1. Quali informazioni vi ha dato `vettore.h` che non avreste potuto indovinare? Elencate, per una funzione a vostra scelta, tutto cio' che avete ricavato dalla sua documentazione.
2. Costruite il programma a mano, in tre comandi, e guardate che cosa compare nella cartella dopo ciascuno:

```bash
gcc -g -Wall -Wextra -c main.c
gcc -g -Wall -Wextra -c vettore.c
gcc -g -Wall -Wextra -o statistiche main.o vettore.o
```

Poi fate `make clean` e `make`: esegue gli stessi tre comandi. Confrontateli uno per uno. L'ordine in cui vengono compilati i due `.c` non conta, mentre il collegamento deve per forza venire per ultimo: perche'?

3. Ripetete il collegamento dimenticando un pezzo: `gcc -g -Wall -Wextra -o statistiche main.o`. Il messaggio nomina `/usr/bin/ld` e ripete cinque volte `undefined reference to ...`. Quale fase si e' lamentata? Perche' la compilazione di `main.c`, poco fa, non aveva detto niente, visto che quelle funzioni non erano nel file?
4. `gcc -g -Wall -Wextra -o statistiche main.c vettore.c` costruisce il programma in un comando solo, senza lasciare nessun `.o`. Funziona, ed e' comodo con due file. Perche' non si fa con duecento? (La risposta e' il primo dei tre motivi del riquadro iniziale.)
5. `make test` deve dare $7$ test superati su $7$. Se qualcuno fallisce, leggete il `.arg` e il `.atteso` del caso che non passa: completano i requisiti qui sopra.

**T2.** Nella cartella `T2_fasi` c'e' lo stesso modulo di T1 e un `main.c` gia' scritto e funzionante. Qui non si scrive codice: si guarda che cosa fanno le prime tre fasi, rompendole una per volta, e poi a che cosa servono le guardie di inclusione.

**Prima fase.** Lanciate `gcc -E main.c -o main.i` e aprite `main.i`.

1. `main.c` ha $21$ righe, `main.i` ne ha circa $850$. Da dove arrivano tutte le altre? Cercate dentro `main.i` il prototipo di `vettore_media`: lo trovate verso il fondo, perche' il contenuto di `stdio.h` viene prima. Le righe che iniziano con `#` sono annotazioni per il compilatore e si possono ignorare, come in N.
2. Nel file originale non compare mai il numero $1000$. In `main.i` invece si', in una `printf`: chi ce l'ha messo, e in quale fase? Rileggete B11.

**Seconda fase.** Copiate `main.c` in `senza_include.c` e togliete la riga `#include "vettore.h"`, poi compilate con `gcc -g -Wall -Wextra -c senza_include.c`.

3. Escono parecchi messaggi, ma di due tipi soli: cinque `warning: implicit declaration of function ...`, uno per ogni funzione del modulo, e un solo `error: 'VETTORE_MAX' undeclared`. Perche' l'unico errore vero e' quello sulla costante, mentre per le funzioni il compilatore si limita ad avvisare? Che cosa riesce a fare senza la dichiarazione di una funzione, e che cosa invece non puo' assolutamente fare senza una `#define`?

(Se il vostro gcc e' la versione 14 o piu' recente, anche gli avvisi sulle funzioni sono errori: aggiungete `-Wno-error=implicit-function-declaration` al comando, come dice la premessa del pacchetto, e tornerete a vedere la differenza tra i due casi.)

**Terza fase.** Copiate `main.c` in `include_del_c.c` e sostituite `#include "vettore.h"` con `#include "vettore.c"`. Poi costruite in due passi, per avere sotto gli occhi i file oggetto:

```bash
gcc -g -Wall -Wextra -c include_del_c.c vettore.c
gcc -g -Wall -Wextra -o rotto include_del_c.o vettore.o
```

4. Adesso i messaggi dicono `multiple definition of 'vettore_minimo'` e nominano `/usr/bin/ld`. Seguite il ragionamento: che cosa ha copiato il preprocessore dentro `include_del_c.c`? Quante definizioni di `vettore_minimo` esistono, alla fine, e in quali file oggetto? Controllate con `nm include_del_c.o` e `nm vettore.o`. Da qui la regola: **nelle intestazioni si mettono le dichiarazioni, mai le definizioni**.
5. Provate `gcc -g -Wall -Wextra -o rotto include_del_c.c`, cioe' senza `vettore.c` e in un comando solo. Questa volta funziona. Spiegate perche', e dite perche' resta comunque una pessima idea. (Che cosa succede se un secondo file include anche lui `vettore.c`?)

**Le guardie.** Nella sottocartella `guardie` ci sono quattro file: `punto.h` e `segmento.h`, **senza** guardie di inclusione, i rispettivi `.c`, e `prova.c`, che le include tutte e due.

6. Costruite con `gcc -g -Wall -Wextra -o prova prova.c punto.c segmento.c`: compare `error: redefinition of 'struct punto'`. Leggete le prime righe del messaggio, quelle che iniziano con `In file included from`: raccontano il percorso che ha fatto il preprocessore. Disegnate su carta l'albero delle inclusioni e segnate quante volte arriva `punto.h`.
7. Aggiungete le guardie a `punto.h` (in `punto_con_guardia.h` trovate la versione gia' fatta, ma scrivetele voi) e ricostruite: il programma stampa `lunghezza al quadrato: 25`. Qui la guardia su `punto.h` e' bastata, perche' nessuno include `segmento.h` due volte. Immaginate pero' di aggiungere un terzo file, `figura.h`, che include anche lui `segmento.h`, e un `main.c` che include `segmento.h` e `figura.h`: che cosa succederebbe? Mettete la guardia anche a `segmento.h` e spiegate in una riga perche' si scrivono **sempre**, anche quando sembrano inutili.
8. **In piu'.** I comandi dei punti precedenti non lasciano nessun `.o`: per averli date `gcc -g -Wall -Wextra -c punto.c segmento.c`. Poi `nm punto.o` e `nm segmento.o`: quali nomi sono `T` e quali `U` in ciascuno dei due? Quale dei due file oggetto ha un buco che l'altro riempie?

**T3.** Nella cartella `T3_contatore` c'e' un modulo che tiene un contatore: `contatore.h`, `contatore.c` e un `main.c` che lo usa. Aprite tutti e tre.

```text
$ make
$ ./contatore_prova
Con passo 1, dopo 5 aumenti: 5
Con passo 10, dopo altri 5: 55
```

Dentro `contatore.c` sono definiti sei nomi, e due non compaiono nell'intestazione: la variabile `quante` e la funzione `valido` sono `static`, mentre la variabile `contatore_passo` e le tre funzioni restano visibili dagli altri file.

1. Perche' `quante` e' `static` e `contatore_passo` no? Guardate l'intestazione e rispondete in termini di "che cosa offre il modulo a chi lo usa".
2. `contatore.h` contiene `extern int contatore_passo;` e `contatore.c` contiene `int contatore_passo = 1;`. Quale delle due righe e' la dichiarazione e quale la definizione? Che cosa succederebbe se togliessimo `extern` dall'intestazione? (Lo vedrete tra poco, al punto 6.)
3. Costruite `rotto_static.c`, che e' fatto apposta per non funzionare, con `gcc -g -Wall -Wextra -o rotto rotto_static.c contatore.c`. Escono due messaggi: prima `warning: implicit declaration of function 'valido'`, che e' il fenomeno di T2.3, e poi `undefined reference to 'valido'`, che viene dal collegamento. Ma `valido` esiste, ed e' dentro `contatore.c` che avete appena compilato: perche' il collegatore non la trova? (Anche qui, con gcc 14 o piu' recente serve `-Wno-error=implicit-function-declaration`: altrimenti ci si ferma al primo messaggio e il collegamento non parte nemmeno.)
4. Adesso, in `rotto_static.c`, sostituite la riga di `valido` con `printf("quante: %ld\n", quante);` e ricompilate. Questa volta l'errore e' `error: 'quante' undeclared`, e arriva **prima**, dalla compilazione. Perche' i due casi si comportano diversamente? (Pensate a che cosa il compilatore e' disposto a fare con un nome di funzione che non conosce, e che cosa invece non puo' fare con un nome di variabile. Ripensate al punto 3 di T2.)
5. Date `nm contatore.o` e confrontate le lettere:

```text
0000000000000030 r __PRETTY_FUNCTION__.0
                 U __assert_fail
000000000000002d T contatore_aumenta
0000000000000017 T contatore_azzera
0000000000000000 D contatore_passo
000000000000008b T contatore_valore
0000000000000000 b quante
0000000000000000 t valido
```

Le prime due righe non le avete scritte voi: le aggiunge la macro `assert`, e si tolgono di mezzo con `nm contatore.o | grep -v __`. Delle sei che restano, quali nomi sono in maiuscolo e quali in minuscolo? Che cosa hanno in comune i due minuscoli? Rileggete il riquadro su `nm` e spiegate il collegamento con `static`.

6. Nella sottocartella `doppia` c'e' l'errore classico di chi comincia: in `comune.h` sta scritto `int totale;` invece di `extern int totale;`. Costruite con `gcc -g -Wall -Wextra -o prova prova.c a.c b.c`: compaiono due `multiple definition of 'totale'`. Quante copie di `totale` sono state create, e da chi? Correggete, aggiungendo `extern` nell'intestazione e la definizione in **uno solo** dei file `.c`, e verificate che il programma stampi `totale: 11`.
7. **In piu'.** Nel modulo `contatore` manca un controllo: niente impedisce a chi lo usa di scrivere `contatore_passo = -5;`, e l'`assert` dentro `contatore_aumenta` fa morire il programma. Provate. Come si potrebbe togliere a chi usa il modulo la possibilita' di sbagliare? Basta rispondere a parole, senza scrivere il codice: e' la stessa idea delle funzioni costruttrici di P13, e la strada e' rendere `static` anche `contatore_passo` e offrire al suo posto due funzioni nell'intestazione.

**T4.** Nella cartella `T4_make` c'e' un programma su tre sorgenti, `main.c`, `etichette.c` e `somma.c`, con due intestazioni. Ci sono anche due Makefile: quello buono, `Makefile`, e uno fatto apposta per sbagliare, `Makefile_incompleto`, che si usa scrivendo `make -f Makefile_incompleto`. L'unica differenza tra i due e' la riga delle dipendenze dei `.o`.

```text
$ make
gcc -g -Wall -Wextra -c main.c
gcc -g -Wall -Wextra -c etichette.c
gcc -g -Wall -Wextra -c somma.c
gcc -g -Wall -Wextra -o tabella main.o etichette.o somma.o
$ ./tabella
Valori a passo di 10:
  riga 0: 0
  riga 1: 10
  riga 2: 20
  riga 3: 30
  riga 4: 40
Somma: 100
```

1. Date `make` una seconda volta, senza toccare niente: risponde `make: 'tabella' is up to date.` e non compila nulla. Come fa a saperlo? (Guardate le date dei file con `ls -l --time-style=full-iso`, o semplicemente `ls -l`.)
2. Date `touch somma.c`, che non cambia il contenuto del file ma ne aggiorna la data, e poi `make`. Quali comandi esegue? Perche' `main.c` ed `etichette.c` non vengono ricompilati, e perche' il collegamento invece si rifa' comunque?
3. Con il Makefile **buono**, cambiate `#define PASSO 10` in `#define PASSO 25` dentro `etichette.h` e date `make`: vengono ricompilati tutti e tre i `.o`. Perche' anche `somma.c`, che non usa `PASSO` e non include nemmeno `etichette.h`? Il programma stampa ora `Valori a passo di 25` e le righe $0$, $25$, $50$, $75$, $100$, con `Somma: 250`: tutto coerente.
4. Adesso il guasto. Rimettete `PASSO` a $10$, poi:

```bash
make -f Makefile_incompleto clean
make -f Makefile_incompleto
```

Cambiate di nuovo `PASSO` in $25$ dentro `etichette.h` e date ancora `make -f Makefile_incompleto`: risponde `up to date` e **non ricompila niente**. Lanciate `./tabella`: stampa ancora i valori vecchi. Perche'? Che cosa sa, make, dei file che un sorgente include?

5. Il guasto peggiore. Senza toccare altro, date `touch etichette.c` (come se aveste modificato anche quel file) e poi `make -f Makefile_incompleto`. Questa volta ricompila `etichette.o`, ma non `main.o`. Il programma stampa:

```text
Valori a passo di 10:
  riga 0: 0
  riga 1: 25
  riga 2: 50
  riga 3: 75
  riga 4: 100
Somma: 100
```

L'intestazione della tabella dice $10$, le righe vanno di $25$ in $25$ e la somma e' quella di $10$. Spiegate riga per riga da quale file oggetto viene ciascuno dei tre numeri. Nessun compilatore ha protestato e nessun test avrebbe potuto accorgersene guardando i sorgenti: perche' questo tipo di guasto e' particolarmente insidioso?

6. Correggete `Makefile_incompleto` aggiungendo la dipendenza mancante, poi rifate la prova del punto 4: ora funziona. Confrontate la vostra correzione con il `Makefile` buono.
7. **In piu'.** La regola `%.o: %.c $(INTESTAZIONI)` dice che **ogni** `.o` dipende da **tutte** le intestazioni, anche da quelle che non include: e' il motivo per cui al punto 3 e' stato ricompilato anche `somma.o`. E' una semplificazione grossolana ma prudente: ricompila qualcosa in piu', e non dimentica mai niente. Che cosa succederebbe, invece, con una regola che si dimentica qualcosa? Nei progetti veri le dipendenze non si scrivono a mano: gcc sa calcolarle da solo, perche' lui i sorgenti li legge. Provate `gcc -MMD -c main.c` e aprite il file `main.d` che compare: contiene una riga sola, `main.o: main.c etichette.h somma.h`, cioe' esattamente la dipendenza che a make serviva. Poi date `make clean`, perche' quel comando ha ricompilato `main.o` senza i vostri flag abituali.

**T5.** **Sfida.** La cartella `T5_rapporto` contiene tre moduli gia' pronti, un'intestazione senza il suo `.c`, il Makefile e i test. Il programma, `rapporto`, legge da un file dei valori interi tra $0$ e $99$ e ne stampa un resoconto con l'istogramma.

I moduli forniti sono:

| Modulo | Che cosa offre |
| --- | --- |
| `lettura.h` / `lettura.c` | `lettura_da_file`, che apre un file, ne legge gli interi in un array e restituisce quanti ne ha letti, oppure $-1$ in caso di errore (e il messaggio su `stderr` lo scrive lui) |
| `ordina.h` / `ordina.c` | `ordina_crescente`, che ordina un array di interi usando `qsort` (S) |
| `statistiche.h` / `statistiche.c` | il tipo `Statistiche` e `statistiche_calcola`, che restituisce media, mediana, minimo e massimo di un array **gia' ordinato** |

Manca `istogramma.c`: l'intestazione `istogramma.h` c'e' ed e' documentata, e dovete scrivere voi le due funzioni che dichiara. Poi scrivete il `main.c` che mette insieme i quattro moduli.

```text
$ cat test/voti.txt
45 52 61 38 55 49 72 58 44 51
67 29 56 63 47 81 53 42 59 35
$ ./rapporto test/voti.txt
Valori letti: 20
Minimo: 29
Massimo: 81
Media: 52.85
Mediana: 52.50
Istogramma:
[ 0- 9]  0 |
[10-19]  0 |
[20-29]  1 |#
[30-39]  2 |##
[40-49]  5 |#####
[50-59]  7 |#######
[60-69]  3 |###
[70-79]  1 |#
[80-89]  1 |#
[90-99]  0 |
```

Requisiti:

- l'array e' grande `LETTURA_MAX` elementi e l'istogramma ha `ISTOGRAMMA_CLASSI` classi: tutte e due le costanti vengono dalle intestazioni, non scrivetele a mano;
- `statistiche_calcola` vuole l'array **gia' ordinato**: la documentazione lo dice, e dall'ordine in cui chiamate le funzioni dipende il risultato;
- un numero di argomenti diverso da uno e un file senza valori sono errori del `main`, con codice $1$; gli altri errori li riconosce `lettura_da_file`, che restituisce $-1$ e ha gia' scritto il messaggio: al `main` resta solo da terminare con codice $1$ senza stampare altro;
- `make test` deve dare $8$ test superati su $8$.

1. Prima di scrivere una riga, disegnate su carta lo schema delle inclusioni: quali file includono quali intestazioni, e in che ordine `main` chiama le funzioni dei quattro moduli. Confrontatelo con la progettazione top-down di I10: qual e' qui il problema grande, e quali i sottoproblemi che i quattro moduli risolvono?
2. Aprite `statistiche.h`: contiene un `typedef struct`, e non solo dei prototipi. Perche' quel tipo **deve** stare nell'intestazione e non in `statistiche.c`? Provate a spostarlo e leggete il messaggio.
3. Aprite `ordina.c`: il comparatore `confronta` e' `static`, e non compare in `ordina.h`. Perche' e' la scelta giusta? Che cosa cambierebbe, per chi usa il modulo, se fosse pubblico?
4. Dei quattro moduli, tre li avete ricevuti e uno lo avete scritto. Tornate con la memoria a **mentre scrivevate** `istogramma.c` e `main.c`, prima dei due punti qui sopra: quante volte avete dovuto aprire un file `.c` che non fosse il vostro? Se la risposta e' zero, le intestazioni hanno fatto il loro mestiere. Se non e' zero, quale informazione mancava nella documentazione?
5. Il Makefile elenca cinque oggetti. Date `make clean` e poi `make`, e contate le compilazioni; poi `touch istogramma.c` e `make`: quante ne restano? Quanto avreste ricompilato, con tutto il programma in un file solo?
6. **In piu'.** Il modulo `ordina` ordina solo in modo crescente. Aggiungete `ordina_decrescente` e fate stampare al `main` anche i tre valori piu' alti. Quali file dovete toccare, e quali no? E quali `.o` ricompila `make`?
7. **In piu'.** `lettura_da_file` accetta solo valori tra $0$ e $99$, e l'istogramma ha dieci classi da dieci: $10 \times 10 = 100$, e il conto torna. Ma le due intestazioni non si parlano, e nessuna delle due dice che quel conto deve tornare. Provate ad allargare l'intervallo in `lettura.c`, ammettendo i valori fino a $999$, e date in pasto al programma un file che contiene $150$: `istogramma_conta` calcola la classe $15$ e scrive in `conteggi[15]`, cioe' fuori da un array di dieci elementi. Il programma non protesta e il risultato e' imprevedibile.
 Ricostruite con `-fsanitize=address`, come spiegato nel riquadro qui sopra, e il programma si ferma da solo segnalando `stack-buffer-overflow` dentro `istogramma_conta`. (Il messaggio dice `READ`, non `WRITE`: `conteggi[15]++` legge la casella prima di riscriverla, e il controllo scatta gia' sulla lettura.) Quando avete finito, **rimettete $99$ in `lettura.c`**, date `make clean` e `make`, e controllate che `make test` torni a dare $8$ su $8$.

Come si potrebbe fare in modo che quel conto non possa sbagliare? Pensate a quale delle due intestazioni dovrebbe dipendere dall'altra, e a che cosa potrebbe controllare un `assert` dentro `istogramma_conta`.


## Pacchetto U: Puntatori e memoria dinamica

I puntatori li state usando da due pacchetti senza che nessuno ve li abbia presentati. `char *argv[]` in R, `FILE *f` in tutti i programmi che aprono un file, `const void *` nelle funzioni di confronto di S: in ciascuno di quei casi c'era una stella, e l'avete scritta fidandovi. Questo pacchetto spiega che cosa significa, e poi mostra la cosa che i puntatori rendono possibile e che finora avete sempre aggirato: **chiedere memoria mentre il programma gira**.

Il motivo per cui conviene farlo lo conoscete gia' bene. In T1 il modulo `vettore` aveva una costante `VETTORE_MAX` uguale a $1000$, e il programma rifiutava i file piu' lunghi; in R e in S ogni programma ha un `#define` che fissa un limite deciso da chi scrive, non da chi usa. In U3 quel limite sparisce.

Il materiale di questo pacchetto sta nelle cartelle da `U1_scambia` a `U5_lista`. Il Makefile e' lo stesso del Pacchetto T, e `make test` funziona allo stesso modo. Compilate sempre con `gcc -g -Wall -Wextra`; da U3 in poi serve anche `valgrind`, che e' nuovo, mentre `-fsanitize=address` lo avete gia' usato in T5.

### Un indirizzo e' un numero

Ogni variabile di un programma sta da qualche parte nella memoria, e quel "da qualche parte" e' un numero: l'**indirizzo** del primo byte che occupa. Un *puntatore* e' una variabile che contiene un indirizzo.

Servono tre notazioni, e sono tutte e tre la stessa stella letta in posti diversi:

```c
int x = 42;
int *p;        /* p e' un puntatore a int: contiene l'indirizzo di un int */
p = &x;        /* & prende l'indirizzo di x                               */
printf("%d\n", *p);   /* * segue il puntatore: stampa 42                  */
*p = 7;        /* scrive 7 dentro x, passando per p                       */
```

- nella **dichiarazione**, `int *p` si legge "`*p` e' un `int`", cioe' "`p` e' l'indirizzo di un `int`";
- `&x` si legge "l'indirizzo di `x`";
- `*p`, in un'espressione, si legge "il valore all'indirizzo `p`".

Un puntatore che non punta a niente vale `NULL`, che e' definito in `stdio.h` e in `stdlib.h`. Seguire un puntatore `NULL` e' comportamento indefinito, e in pratica fa terminare il programma con `Segmentation fault`: e' il modo in cui il sistema vi dice che avete chiesto l'indirizzo zero. Per stampare un indirizzo si usa `%p`, con il valore convertito a `void *`:

```c
printf("x sta in %p\n", (void *)&x);
```

Gli indirizzi cambiano a ogni esecuzione, quindi un programma che li stampa non e' verificabile con `make test`. Quello che **non** cambia sono le loro differenze: e' su quelle che lavora U2.

### I puntatori che avete gia' usato

| Dove | Che cosa e' | Che cosa significa |
| --- | --- | --- |
| `scanf("%d", &n)` | `&n` | l'indirizzo di `n`, perche' `scanf` deve **scrivere** dentro `n` |
| `char *argv[]` | array di puntatori a `char` | ogni `argv[i]` e' l'indirizzo del primo carattere di una parola |
| `FILE *f` | puntatore a una struttura della libreria | l'indirizzo di un oggetto che non dovete guardare dentro |
| `int confronta(const void *a, const void *b)` | due indirizzi di tipo ignoto | `qsort` non sa che cosa sta ordinando: vi passa gli indirizzi |
| `strcpy(d, s)` | due indirizzi di `char` | i nomi degli array sono indirizzi, come si vede qui sotto |

La prima riga e' quella che spiega I12. Un sottoprogramma riceve **copie** dei parametri, quindi non puo' cambiare le variabili del chiamante; `scanf` ci riesce perche' non riceve `n` ma il suo indirizzo. Quando in I avete scritto uno `scambia` che non scambiava, vi mancava esattamente questo. In U1 lo rimettete a posto.

### Puntatori e array

In C il nome di un array, usato in un'espressione, **vale l'indirizzo del suo primo elemento**. Da questo discende tutto il resto:

- `v[i]` e' solo un modo comodo di scrivere `*(v + i)`: le due notazioni sono intercambiabili;
- `v + i` non somma `i` byte ma `i` **elementi**: con un array di `int`, `v + 1` e' quattro byte piu' avanti. L'aritmetica dei puntatori sa quanto e' grande cio' che viene puntato;
- la differenza di due puntatori dentro lo stesso array e' il numero di elementi che li separa, non di byte;
- passare un array a una funzione **non lo copia**, perche' quello che viene copiato e' l'indirizzo. E' la risposta alla domanda rimasta in sospeso in I7 e in P17: una `struct` passata per valore viene copiata tutta (tutti e novantasei i byte del `Polinomio` di P17, a ogni chiamata), un array no, e la differenza e' qui;
- dentro la funzione, quindi, `sizeof` sul parametro **non** da' la dimensione dell'array, ma quella di un puntatore. Per questo le funzioni che ricevono un array ricevono sempre anche `n`.

```c
void f(int v[]) {
    printf("%d\n", (int)sizeof(v));   /* 8: e' un puntatore */
}

int main(void) {
    int v[8];
    printf("%d\n", (int)sizeof(v));   /* 32: sono 8 int */
    f(v);
    return 0;
}
```

`int v[]` e `int *v`, scritti come **parametro**, sono la stessa identica cosa; scritti come **dichiarazione di variabile** sono due cose diverse (il primo riserva lo spazio, il secondo no).

### Chiedere memoria durante l'esecuzione

Finora tutta la memoria dei vostri programmi era decisa prima di partire: le variabili e gli array avevano una taglia scritta nel sorgente. Le quattro funzioni di `stdlib.h` che seguono permettono invece di chiederne quando serve e quanta serve.

| Funzione | Che cosa fa |
| --- | --- |
| `malloc(byte)` | chiede `byte` byte e restituisce l'indirizzo del primo, oppure `NULL` |
| `calloc(quanti, byte)` | come `malloc` per `quanti * byte` byte, ma li azzera |
| `realloc(p, byte)` | cambia la dimensione del blocco `p`, conservandone il contenuto |
| `free(p)` | restituisce al sistema il blocco `p` |

La forma da imparare a memoria e' questa:

```c
int *v = malloc((size_t)n * sizeof(int));
if (v == NULL) {
    fprintf(stderr, "memoria esaurita\n");
    return 1;
}
/* ... usare v come un normale array di n interi: v[0], ..., v[n-1] ... */
free(v);
```

Tre avvertenze:

- **si scrive `sizeof(int)`, non $4$.** Il programma deve restare giusto su un computer in cui `int` ne occupa otto;
- **il valore restituito va sempre controllato.** `malloc` restituisce `NULL` quando non ce la fa, e seguire quel `NULL` fa morire il programma lontano dal punto in cui e' nato l'errore;
- **`realloc` puo' spostare il blocco**, quindi il vecchio indirizzo dopo la chiamata non vale piu'. Il risultato si raccoglie in una variabile nuova, perche' se `realloc` fallisce restituisce `NULL` e il blocco vecchio e' ancora da liberare:

```c
int *nuovo = realloc(v, (size_t)capacita * sizeof(int));
if (nuovo == NULL) {
    free(v);          /* v e' ancora valido: va liberato */
    return NULL;
}
v = nuovo;
```

**Chi chiede, libera.** La memoria ottenuta con `malloc` resta occupata finche' qualcuno non chiama `free`: non sparisce alla fine della funzione, come fanno invece le variabili locali. Quando una funzione restituisce un blocco appena ottenuto, deve dire nella documentazione che la responsabilita' passa al chiamante: e' quello che fa l'`@post` di `lettura_interi` in U3.

### I quattro errori, e i due strumenti per vederli

| Errore | Che cosa succede |
| --- | --- |
| **perdita** (*leak*) | si chiede memoria e non si libera mai: il programma cresce finche' non finisce la memoria |
| **doppia liberazione** | si chiama `free` due volte sullo stesso blocco: il programma muore, a volte molto dopo |
| **uso dopo la liberazione** | si legge o si scrive un blocco gia' liberato: i valori sono casuali |
| **scrittura oltre il limite** | si scrive in `v[n]` di un blocco di `n` elementi: si rovina la memoria accanto |

Hanno tutti e quattro la stessa caratteristica sgradevole: **il programma sembra funzionare**. Nessuno dei quattro e' segnalato da `gcc` in modo affidabile, e i test di `make test` li superano tutti. Servono strumenti che controllino la memoria durante l'esecuzione, e ce ne sono due:

```bash
gcc -g -Wall -Wextra -fsanitize=address -o prova prova.c    # poi ./prova
valgrind --leak-check=full ./prova
```

Il primo lo conoscete gia' dal Pacchetto T, dove serviva a scoprire gli accessi fuori da un array: gli stessi controlli valgono per la memoria chiesta con `malloc`, e in piu' alla fine del programma `-fsanitize=address` elenca i blocchi mai liberati. Il secondo, `valgrind`, e' nuovo: non richiede di ricompilare, trova le stesse cose piu' lentamente, e il suo riepilogo finale distingue la memoria **definitely lost** da quella **still reachable**. Usateli entrambi almeno una volta in U4, e poi tenete l'abitudine di passare sotto `valgrind` ogni programma che chiama `malloc`.

### Esercizi (U1-U5)

**U1.** Nella cartella `U1_scambia` trovate il modulo `scambio.h` e `scambio.c`, il Makefile e i test; manca `main.c`, che scrivete voi. Il modulo offre quattro sottoprogrammi: `scambio_per_valore`, lasciato apposta com'era in I12 e quindi inutile; `scambio_scambia`, che funziona; `scambio_dividi`, che restituisce quoziente e resto insieme; e `scambio_ordina_tre`.

Il programma `scambia` riceve tre interi sulla riga di comando e stampa esattamente questo:

```text
$ ./scambia 17 5 3
Prima:            a = 17, b = 5
Per valore:       a = 17, b = 5
17 / 5 = 3 con resto 2
Con i puntatori:  a = 5, b = 17
Ordinati:         3 5 17
```

Con un numero di argomenti diverso da tre, stampa su `stderr` la riga `Uso: ./scambia a b c` e termina con codice $1$. La divisione va fatta **prima** dello scambio, e con il divisore uguale a zero stampa `7 / 0: divisione per zero` al posto della riga della divisione.

1. Leggete `scambio.c` e confrontate i corpi di `scambio_per_valore` e di `scambio_scambia`: sono la stessa sequenza di tre assegnazioni, con tre stelle in piu'. Dite, riga per riga, su che cosa agiscono le assegnazioni nei due casi.
2. Nel `main`, la prima chiamata si scrive `scambio_per_valore(a, b)` e la seconda `scambio_scambia(&a, &b)`. Provate a scrivere `scambio_scambia(a, b)` e riportate l'errore di gcc. E con `scambio_per_valore(&a, &b)`?
3. **Con gdb.** Mettete un punto di arresto su `scambio_scambia` ed eseguite `print a`, `print *a`, `print &a` e, risalendo con `up`, `print &a` nel `main`. Quali due di questi quattro comandi stampano lo stesso numero? Spiegate perche'.
4. `scambio_dividi` e' il modo in cui in C una funzione "restituisce due valori": uno con `return` e gli altri scrivendo dove le viene detto. Confrontatelo con la soluzione di P, dove una `struct` con due campi faceva lo stesso lavoro. Quali sono i vantaggi e gli svantaggi dei due modi?
5. Il valore restituito da `scambio_dividi` e' $0$ o $1$ e dice se la divisione si poteva fare. E' la stessa convenzione di `scanf`, che restituisce quanti valori e' riuscito a leggere. Che cosa succede nel `main` se non lo controllate e `b` vale zero? Provate: `q` e `r` che valori hanno?
6. `scambio_ordina_tre` chiama `scambio_scambia` tre volte. Dimostrate che tre scambi bastano sempre, elencando i sei ordini possibili di tre numeri diversi e seguendo l'algoritmo su ciascuno.
7. **In piu'.** Aggiungete al modulo `void scambio_ruota(int *a, int *b, int *c)`, che sposta il valore di `*a` in `*b`, quello di `*b` in `*c` e quello di `*c` in `*a`. Quante variabili di appoggio servono? Verificate che applicandola tre volte si torni al punto di partenza.

**U2.** Nella cartella `U2_indirizzi` trovate il modulo `indirizzi.h` e `indirizzi.c`; manca `main.c`. Il modulo somma un array in tre modi diversi (con `v[i]`, con `*(v + i)` e scorrendo con un puntatore da un indirizzo all'altro), stampa le distanze fra gli elementi, e misura `sizeof` del parametro.

Il programma `indirizzi` riceve da uno a sedici interi sulla riga di comando, li mette in un array `int v[16]` dichiarato dentro `main`, e stampa:

```text
$ ./indirizzi 3 1 4 1 5 9 2 6
sizeof(v) dentro main:        64 byte
sizeof(v) dentro la funzione: 8 byte
sizeof(int):                  4 byte
caselle secondo main:         16
numeri letti:                 8

somma con v[i]:       31
somma con *(v + i):   31
somma scorrendo:      31
somma della meta' destra: 22

v[0] =   3   &v[0] - &v[0] = 0   in byte: 0
v[1] =   1   &v[1] - &v[0] = 1   in byte: 4
...
v[7] =   6   &v[7] - &v[0] = 7   in byte: 28
```

La "meta' destra" e' `indirizzi_somma_scorrendo(v + n / 2, v + n)`. Con zero argomenti o con piu' di sedici, il programma stampa su `stderr` `Uso: ./indirizzi n1 n2 ... (da 1 a 16 numeri)` e termina con codice $1$.

1. Compilando il modulo, gcc produce un avviso: `'sizeof' on array function parameter 'v' will return size of 'const int *'`. Non e' un difetto da correggere, e' l'argomento dell'esercizio. Riscrivetelo con parole vostre e dite perche' il compilatore puo' accorgersene.
2. `sizeof(v)` vale $64$ nel `main` e $8$ nella funzione. Da dove vengono i due numeri? Quale dei due dipende da `#define MAX 16` e quale dal computer?
3. Le tre somme danno lo stesso risultato. Guardate i tre corpi in `indirizzi.c`: `v[i]`, `*(v + i)` e `*p` con `p++`. Spiegate perche' sono la stessa cosa, e dite quale delle tre scrivereste nel vostro codice.
4. Nella tabella finale, la terza colonna e' sempre quattro volte la seconda. Perche' `&v[i] - &v[0]` vale `i` e non `4 * i`? Che cosa dovrebbe fare il compilatore per ottenere quel numero, sapendo che gli indirizzi sono byte?
5. Cambiate l'array in `double v[16]` (e tutto il resto di conseguenza). Quali numeri della tabella cambiano, e quali no? Prevedeteli prima di eseguire.
6. `indirizzi_somma_scorrendo(v, v + n)` riceve un indirizzo **oltre** l'ultimo elemento. Lo standard C garantisce che calcolare quell'indirizzo sia lecito, ma non che si possa seguire. Guardate il ciclo: dove viene usato `fine`, e dove **non** viene usato?
7. **In piu'.** Scrivete `int indirizzi_cerca(const int *inizio, const int *fine, int valore)` che restituisce la distanza dal primo elemento, oppure $-1$. Poi provate a scriverne una versione che restituisce direttamente un puntatore al valore trovato, o `NULL`: e' cosi' che funziona `bsearch` di S.

**U3.** Nella cartella `U3_dinamico` trovate `lettura.h`, il `main.c` gia' scritto, il Makefile e i test. Manca `lettura.c`: lo scrivete voi, ed e' il primo modulo che chiede memoria.

Il modulo deve leggere da un file **tutti** gli interi che contiene, senza nessun limite fissato nel sorgente: niente `VETTORE_MAX`. La strategia e' obbligatoria, perche' i test controllano anche quante volte l'array e' stato ingrandito: si parte da una capacita' di $4$ elementi e la si **raddoppia** ogni volta che si riempie.

```text
$ ./somma test/numeri.txt
Numeri letti: 10
Minimo: 1
Massimo: 9
Somma: 39
Ingrandimenti: 2
Primi cinque: 3 1 4 1 5

$ ./somma test/grande.txt
Numeri letti: 20000
Minimo: -1000
Massimo: 1000
Somma: -75376
Ingrandimenti: 13
Primi cinque: -337 941 -692 -192 333
```

`lettura_interi` restituisce `NULL`, scrivendo $-1$ in `*quanti`, se il file contiene un dato non valido, se la memoria non basta, o se il file e' vuoto; in tutti e tre i casi deve liberare quello che aveva gia' chiesto.

1. Verificate i due numeri della riga `Ingrandimenti`. Partendo da $4$ e raddoppiando, quali capacita' si attraversano per arrivare a contenere $10$ elementi? E $20000$? Scrivete la formula generale in funzione di `n`.
2. Il totale degli elementi copiati dai vari `realloc` e' $4 + 8 + 16 + \dots$ fino all'ultima capacita'. Sommate la serie geometrica e dite quanto costa, in funzione di `n`, tutta la crescita. Qual e' la classe? (E' il motivo per cui si raddoppia invece di aggiungere una casella per volta.)
3. Provate a crescere **di uno** invece che raddoppiando, su `grande.txt`. Quanti `realloc` vengono fatti, e quanti elementi vengono copiati in tutto? Misurate il tempo delle due versioni con `time`.
4. Il modulo di T1 rifiutava i file con piu' di $1000$ numeri; questo legge `grande.txt` che ne ha $20000$. Rileggete in `vettore.h` di T1 il commento della costante `VETTORE_MAX` e dite quale riga della documentazione sparisce qui, e quale compare al suo posto.
5. **Con valgrind.** Eseguite `valgrind --leak-check=full ./somma test/numeri.txt`. Deve dire `All heap blocks were freed`. Poi togliete la chiamata a `lettura_libera` nel `main` e rieseguite: quanti byte risultano persi, e corrispondono a quelli che avevate chiesto?
6. Il `main` controlla `if (v == NULL)`. Togliete il controllo e provate con `test/vuoto.txt`: che cosa succede, e a quale riga? Confrontate con il caso in cui il controllo c'e'.
7. **In piu'.** Il blocco finale ha una capacita' che e' una potenza di due, quindi quasi sempre piu' grande del necessario: con $20000$ elementi ne occupa $32768$. Aggiungete alla fine di `lettura_interi` un `realloc` che la riduce esattamente a `n`, e dite quanti byte si risparmiano nel caso peggiore. Perche' quel `realloc` non puo' fallire in modo pericoloso?

**U4.** Nella cartella `U4_memoria` ci sono quattro programmi indipendenti, `uno.c`, `due.c`, `tre.c` e `quattro.c`. Tutti e quattro **calcolano la cosa giusta** e tre su quattro terminano senza lamentarsi; ciascuno contiene uno dei quattro errori della tabella piu' sopra, uno per programma. Il Makefile offre `make`, `make asan` e `make valgrind`.

Per ciascuno: eseguitelo, osservate che l'output e' corretto, trovate l'errore con gli strumenti, correggetelo, e verificate che `valgrind` non dica piu' niente.

```text
$ ./uno
Somma dei quadrati fino a 100: 338350

$ ./due 4 8 15 16 23 42
Media: 18.00
free(): double free detected in tcache 2
Aborted

$ ./tre 5
Diagonale: 1606917908 4 9 16 25
Somma: 225

$ ./quattro 10
Somma dei primi 10 dispari: 100
```

1. Associate ciascun programma a uno dei quattro errori, **prima** di usare gli strumenti. Due si riconoscono gia' dall'output riportato qui sopra: quali, e da che cosa?
2. Eseguite `make valgrind ARG=10` e leggete i quattro rapporti. Per `uno`, valgrind dice `definitely lost: 39,999,600 bytes in 99,999 blocks` e, una riga piu' sotto, `still reachable: 400 bytes in 1 blocks`: da dove vengono questi numeri? (Il programma chiama la funzione $100000$ volte, su array di $100$ interi.) Sommate i blocchi persi e quello ancora raggiungibile: quante chiamate sono?
3. Eseguite `make asan` e rieseguite i quattro. I messaggi sono `leaked in ... allocation(s)`, `attempting double-free`, `heap-use-after-free` e `heap-buffer-overflow`. Confrontateli con le vostre risposte al punto 1.
4. Uno dei quattro errori viene segnalato **anche da gcc**, in compilazione, con l'avviso `pointer 't' may be used after 'free'`. Quale? Perche' il compilatore riesce a vedere quello e non gli altri tre? (Guardate quanto distano, nel sorgente, la `free` e l'uso sbagliato.)
5. In `due.c` l'errore non e' in una riga ma in una **decisione di progetto**: `media` libera l'array che ha ricevuto. Spiegate perche' e' una pessima idea e correggete senza spostare la `free` di posto nel `main`. Che cosa andrebbe scritto nella documentazione di `media` se si volesse davvero tenere quel comportamento?
6. In `tre.c` la prima stampa della diagonale e' un numero diverso a ogni esecuzione, ma gli altri quattro sono giusti. Spiegate perche' il blocco liberato contiene ancora i valori di prima, tranne che all'inizio. (Suggerimento: chi gestisce la memoria libera usa i primi byte del blocco per i propri appunti.)
7. In `quattro.c` la scrittura e' una sola casella oltre il limite, e il programma termina regolarmente. Provate con `n` molto piu' grande e ripetete qualche volta: termina sempre? **In piu'.** Questo e' l'errore piu' pericoloso dei quattro: spiegate perche', confrontandolo con una perdita di memoria.

**U5.** **Sfida.** Nella cartella `U5_lista` ci sono `lista.h`, il `main.c` gia' scritto, il Makefile e i test; manca `lista.c`, che scrivete voi. E' la prima struttura dati che non e' un array: una **lista concatenata**, cioe' una catena di nodi in cui ciascuno contiene un valore e l'indirizzo del successivo.

```c
typedef struct nodo {
    int valore;
    struct nodo *successivo;
} Nodo;
```

Una lista vuota e' `NULL`, l'ultimo nodo ha `successivo` uguale a `NULL`. Ogni sottoprogramma che puo' cambiare la testa della lista la restituisce, e chi chiama riassegna: `l = lista_togli(l, 5);`.

```text
$ ./lista 5 3 9 1 3 7
In testa:   7 3 1 9 3 5
Lunghezza:  6
Rovesciata: 5 3 9 1 3 7
Contiene 5: 1
Contiene 999: 0
Senza 5:   3 9 1 3 7
Senza 999:  3 9 1 3 7
Ordinata:   1 3 3 5 7 9
Lunghezza:  6
```

1. La dichiarazione contiene `struct nodo *successivo;` **dentro** la definizione di `struct nodo`: una struttura che contiene se stessa. Spiegate perche' questo e' lecito mentre `Nodo successivo;` non lo sarebbe. (Pensate a quanto dovrebbe valere `sizeof(Nodo)` nei due casi.)
2. Dentro la struttura si scrive `struct nodo *` e non `Nodo *`. Perche'? Provate a scrivere `Nodo *successivo;` e riportate l'errore.
3. `lista_inserisci_in_testa` costa sempre lo stesso, qualunque sia la lunghezza della lista; `lista_inserisci_ordinato` no. Scrivete le due classi di complessita' e dite che cosa costa invece l'inserimento in testa in un **array**.
4. Scrivete `lista_rovescia` senza chiamare `malloc`: servono tre puntatori, `precedente`, `corrente` e `dopo`. Seguitela a mano sulla lista `7 3 1`, disegnando le frecce dopo ogni giro. Perche' serve `dopo`?
5. `lista_togli` ha due casi: il valore e' in testa, oppure no. Perche' il primo va trattato a parte? Che cosa va liberato, e in quale ordine rispetto all'aggiornamento di `successivo`? (Invertite i due e guardate che cosa dice `-fsanitize=address`.)
6. **Con valgrind.** `valgrind --leak-check=full ./lista 5 3 9 1 3 7` deve dire `All heap blocks were freed`. Se non lo dice, i byte persi sono un multiplo di `sizeof(Nodo)`: quanti nodi avete dimenticato, e dove?
7. Confrontate la lista con l'array dinamico di U3 su quattro operazioni: inserire in testa, inserire in coda, leggere l'elemento di posto `i`, e la memoria occupata per elemento. Costruite la tabella e dite, per ciascuna riga, chi vince. Quanto occupa un `Nodo` rispetto a un `int`?
8. **In piu'.** Scrivete `Nodo *lista_fondi(Nodo *a, Nodo *b)` che, date due liste **ordinate**, ne costruisce una sola ordinata riusando i nodi che gia' esistono, senza nessun `malloc` e senza nessuna `free`. E' la fusione di G6, fatta con le frecce invece che con gli indici: qui, a differenza di G6, non serve un terzo contenitore. Perche'?
