# Esercizi Programmazione II

| Blocco | Argomento | Esercizi |
| --- | --- | --- |
| M | else if, do while, const e assert | 20 |
| N | break, continue, enum e macro | 20 |
| O | La libreria standard | 10 |
| P | struct, typedef e union | 20 |
| Q | Operatori bit a bit e stringhe | 10 |


## Pacchetto M: else if, do while, const e assert

### else if

Con `else if` si scrive una scelta tra piu' di due casi senza annidare gli `if`. Le condizioni vengono controllate in ordine e si esegue solo il primo ramo vero.

```c
if (voto < 18) {
    printf("Insufficiente\n");
} else if (voto <= 23) {
    printf("Sufficiente\n");
} else {
    printf("Buono o piu'\n");
}
```

### do while

Il `do while` controlla la condizione alla fine, quindi il corpo viene eseguito almeno una volta: e' il ciclo naturale per chiedere un dato finche' non e' valido. Attenzione al `;` dopo la condizione.

```c
do {
    printf("Voto (0-30): ");
    scanf("%d", &voto);
} while (voto < 0 || voto > 30);
```

### const

Una variabile dichiarata `const` non si puo' piu' modificare: se ci si prova, gcc si rifiuta di compilare. Per convenzione il nome si scrive in maiuscolo.

```c
const double IVA = 0.22;
```

### assert

`assert` (dalla libreria `assert.h`) controlla una condizione che *deve* essere vera: se e' falsa, il programma si ferma subito con un messaggio che indica la riga. Serve a scoprire gli errori di chi scrive il programma, non a controllare l'input dell'utente.

```c
#include <assert.h>
/* ... */
assert(divisore != 0);
```

### Il valore restituito da scanf

`scanf` restituisce il numero di valori che e' riuscita a leggere: se l'utente scrive `abc` quando serve un intero, `scanf("%d", &n)` restituisce $0$.

```c
if (scanf("%d", &n) != 1) {
    printf("Errore: non hai inserito un numero\n");
    return 1;
}
```

### Esercizi (M1-M20)

#### else if e condizioni

**M1.** Il programma legge tre lati interi e stampa `Non e' un triangolo`, `Equilatero`, `Isoscele` oppure `Scaleno`, usando `else if`. Tre segmenti formano un triangolo solo se sono positivi e ciascuno e' minore della somma degli altri due (disuguaglianza triangolare). Quale controllo deve venire per primo, e perche'? Provate con $3, 3, 3$, con $3, 3, 5$, con $3, 4, 5$ e con $1, 2, 3$.

```text
Lati del triangolo: 3 4 5
Scaleno
```

**M2.** Trova l'errore. Con $30$ il programma deve stampare `Ottimo`, con $25$ `Buono`.

```c
#include <stdio.h>

int main(void) {
    int voto;
    printf("Voto: ");
    scanf("%d", &voto);
    if (voto >= 18) {
        printf("Sufficiente\n");
    } else if (voto >= 24) {
        printf("Buono\n");
    } else if (voto >= 28) {
        printf("Ottimo\n");
    } else {
        printf("Insufficiente\n");
    }
    return 0;
}
```

**M3.** Trova l'errore. Con $a = 5$ e $b = -1$ il programma stampa `a non e' positivo`, e con $a = -5$ e $b = 3$ non stampa nulla. A quale `if` appartiene davvero l'`else`?

```c
#include <stdio.h>

int main(void) {
    int a, b;
    printf("Inserisci a e b: ");
    scanf("%d %d", &a, &b);
    if (a > 0)
        if (b > 0)
            printf("a e b sono positivi\n");
    else
        printf("a non e' positivo\n");
    return 0;
}
```

**M4.** Prevedete cosa succede con $n = 10$ e $d = 5$, poi con $n = 10$ e $d = 0$. Le due versioni sembrano equivalenti: perche' non lo sono? Suggerimento: se la prima condizione di un `&&` e' falsa, la seconda non viene nemmeno calcolata.

```c
#include <stdio.h>

int main(void) {
    int n, d;
    printf("Inserisci n e d: ");
    scanf("%d %d", &n, &d);
    /* versione A */
    if (d != 0 && n % d == 0) {
        printf("A: %d divide %d\n", d, n);
    } else {
        printf("A: %d non divide %d\n", d, n);
    }
    /* versione B */
    if (n % d == 0 && d != 0) {
        printf("B: %d divide %d\n", d, n);
    } else {
        printf("B: %d non divide %d\n", d, n);
    }
    return 0;
}
```

**M5.** Trova l'errore. Con $7$ il programma funziona, ma con $-3$ stampa `-3 e' pari`.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Inserisci un numero intero: ");
    scanf("%d", &n);
    if (n % 2 == 1) {
        printf("%d e' dispari\n", n);
    } else {
        printf("%d e' pari\n", n);
    }
    return 0;
}
```

#### do while e numeri reali

**M6.** Dallo pseudocodice al C. In questo algoritmo (lo stesso di A12) la lettura compare due volte: prima del ciclo e alla fine del corpo. Traducetelo in C con un `do while`, in modo che `scanf` compaia una volta sola. Attenzione: il numero che fa terminare la sequenza non va sommato. Quale delle due versioni preferite, e perche'?

```text
INIZIO
    ASSEGNA a _somma il valore 0
    LEGGI _numero
    FINCHE' _numero > 0
        ASSEGNA a _somma il valore _somma + _numero
        LEGGI _numero
    FINE
    VISUALIZZA _somma
FINE
```

**M7.** Dallo pseudocodice al C. Traducete in C l'algoritmo, che calcola la somma della serie armonica $H_n = 1 + \frac{1}{2} + \dots + \frac{1}{n}$. Con $n = 10$ deve stampare `H(10) = 2.928968`: se la vostra traduzione da' un altro valore, cercate il motivo. **In piu'.** Scrivete un secondo programma che trova quanti termini servono perche' la somma superi $5$.

```text
INIZIO
    LEGGI _n
    ASSEGNA a _somma il valore 0
    ASSEGNA a _i il valore 1
    FINCHE' _i <= _n
        ASSEGNA a _somma il valore _somma + 1 / _i
        ASSEGNA a _i il valore _i + 1
    FINE
    VISUALIZZA _somma
FINE
```

**M8.** Prevedete cosa stampa il programma, poi eseguitelo (`%.20f` stampa $20$ cifre decimali). Correggete il confronto usando una tolleranza: dichiarate `const double EPS = 0.000000001;` e considerate uguali due numeri se la loro differenza, in valore assoluto, e' minore di `EPS`.

```c
#include <stdio.h>

int main(void) {
    double a, b;
    a = 0.1;
    b = 0.2;
    if (a + b == 0.3) {
        printf("Uguali\n");
    } else {
        printf("Diversi\n");
    }
    printf("%.20f\n", a + b);
    return 0;
}
```

**M9.** Trova l'errore. Il ciclo dovrebbe stampare $0.0, 0.1, \dots, 0.9$ e poi `Fine`, ma non si ferma. Rivedete M8.

```c
#include <stdio.h>

int main(void) {
    double x;
    for (x = 0.0; x != 1.0; x = x + 0.1) {
        printf("%f\n", x);
    }
    printf("Fine\n");
    return 0;
}
```

**M10.** Il programma legge un importo in euro, in una variabile `double euro`, e indica il numero minimo di monete per pagarlo (da $2$ e $1$ euro, da $50$, $20$, $10$, $5$, $2$ e $1$ centesimo), stampando solo le monete che usa. Conviene convertire subito l'importo in centesimi interi, in una variabile `int centesimi`, con `centesimi = euro * 100 + 0.5;`. Provate a togliere il `+ 0.5` e inserite $4.35$ oppure $8.20$: cosa succede, e perche' il `+ 0.5` lo evita?

```text
Importo in euro: 4.35
Totale: 435 centesimi
2 da 2 euro
1 da 20 centesimi
1 da 10 centesimi
1 da 5 centesimi
```

#### Controllare i dati: scanf e assert

**M11.** Il programma legge un intero e ne stampa il doppio; se l'utente non scrive un numero, stampa un messaggio di errore e termina restituendo $1$. Provate con `21`, con `abc` e con `12abc`: cosa succede nell'ultimo caso? Su Linux e macOS, subito dopo l'esecuzione, il comando `echo $?` mostra il valore restituito da `main`.

```text
Inserisci un numero intero: abc
Errore: non hai inserito un numero
```

**M12.** Trova l'errore. Se l'utente scrive `abc`, il programma ripete la domanda all'infinito. Perche'? Correggetelo come in M11.

```c
#include <stdio.h>

int main(void) {
    int n;
    n = -1;
    do {
        printf("Inserisci un numero da 1 a 10: ");
        scanf("%d", &n);
    } while (n < 1 || n > 10);
    printf("Hai scelto %d\n", n);
    return 0;
}
```

**M13.** Dallo pseudocodice al C. Questa e' la versione originale dell'algoritmo di Euclide, con le sottrazioni al posto del resto. Traducetela in C e confrontate il numero di passi con quello di D42, a cui aggiungerete un contatore dei giri del ciclo, per esempio con $1000$ e $1$. Cosa succede se uno dei due numeri e' $0$? Aggiungete una validazione con `do while` e, subito prima del ciclo, un `assert` che dichiari che i numeri sono positivi.

```text
INIZIO
    LEGGI _a e _b
    ASSEGNA a _passi il valore 0
    FINCHE' _a diverso da _b
        SE _a > _b ALLORA
            ASSEGNA a _a il valore _a - _b
        ALTRIMENTI
            ASSEGNA a _b il valore _b - _a
        FINE
        ASSEGNA a _passi il valore _passi + 1
    FINE
    VISUALIZZA _a e _passi
FINE
```

```text
Inserisci due numeri positivi: 84 36
MCD = 12 (in 4 passi)
```

**M14.** Dallo pseudocodice al C. L'algoritmo calcola la radice quadrata intera di $n$, cioe' il piu' grande $k$ con $k^2 \le n$. Traducetelo in C, validando che $n$ non sia negativo, e aggiungete dopo il ciclo `assert(k * k <= n && (k + 1) * (k + 1) > n);`, che controlla che il risultato sia davvero quello giusto. Poi "rompete" il programma, sostituendo `<=` con `<` nella condizione del ciclo, e provate con $49$: cosa succede?

```text
INIZIO
    LEGGI _n
    ASSEGNA a _k il valore 0
    FINCHE' (_k + 1) x (_k + 1) <= _n
        ASSEGNA a _k il valore _k + 1
    FINE
    VISUALIZZA _k
FINE
```

```text
Inserisci un numero non negativo: 50
Radice intera di 50 = 7
```

**M15.** Per ogni situazione, dite se va gestita con un controllo dell'input (`if` o `do while`), con il valore restituito da `scanf` oppure con un `assert`.

1. L'utente inserisce un numero di studenti negativo.
2. Dopo il ciclo di M14, deve valere $k^2 \le n < (k+1)^2$.
3. L'utente scrive `abc` quando il programma chiede un numero.
4. Dopo un `do while` che accetta solo voti da $0$ a $30$, il voto deve essere compreso tra $0$ e $30$.
5. Il divisore inserito dall'utente e' $0$.

#### Mettere insieme i pezzi

**M16.** Scomposizione in fattori primi: il programma legge un numero maggiore di $1$ e lo divide per $2$ finche' puo', poi per $3$, e cosi' via, stampando ogni divisore trovato. Perche' non serve controllare che i divisori provati siano primi?

```text
Inserisci un numero maggiore di 1: 360
360 = 2 2 2 3 3 5
```

**M17.** Dallo pseudocodice al C. Metodo di bisezione. La funzione $f(x) = x^3 - x - 2$ vale $-2$ in $1$ e $4$ in $2$: per il teorema degli zeri ha una radice tra $1$ e $2$. L'algoritmo dimezza l'intervallo finche' non e' piu' corto della tolleranza. Traducetelo in C, con la tolleranza in una costante `const double EPS` e un contatore dei passi. Quanti passi servirebbero con una tolleranza dieci volte piu' piccola? Provate a prevederlo prima di eseguire.

```text
INIZIO
    ASSEGNA a _sinistra il valore 1
    ASSEGNA a _destra il valore 2
    FINCHE' _destra - _sinistra > 0.000001
        ASSEGNA a _medio il valore (_sinistra + _destra) / 2
        ASSEGNA a _valore il valore _medio x _medio x _medio - _medio - 2
        SE _valore > 0 ALLORA
            ASSEGNA a _destra il valore _medio
        ALTRIMENTI
            ASSEGNA a _sinistra il valore _medio
        FINE
    FINE
    VISUALIZZA (_sinistra + _destra) / 2
FINE
```

```text
Radice: 1.521380 (in 20 passi)
```

**M18.** In D18 il fattoriale di $13$ usciva sbagliato senza nessun avviso. Rendete il programma robusto: prima di ogni moltiplicazione controllate che il risultato stia in un `int`, confrontandolo con `INT_MAX` (il massimo di un `int`, definito in `limits.h`), e in caso contrario stampate un errore e terminate. Perche' il controllo si scrive `fattoriale > INT_MAX / i` e non `fattoriale * i > INT_MAX`?

```text
Inserisci n (non negativo): 13
Overflow: 13! non entra in un int
```

**M19.** Il programma legge tre numeri positivi e ne calcola il minimo comune multiplo, sapendo che $\mathrm{mcm}(a, b, c) = \mathrm{mcm}(\mathrm{mcm}(a, b), c)$ e che $\mathrm{mcm}(a, b) = \frac{a \cdot b}{\mathrm{MCD}(a, b)}$. Dovrete scrivere due volte il ciclo di Euclide: quando vedrete le funzioni, lo scriverete una volta sola. Perche' conviene calcolare `a / mcd * b` invece di `a * b / mcd`?

```text
Tre numeri positivi: 4 6 10
mcm(4, 6, 10) = 60
```

**M20.** **Sfida.** Una calcolatrice per numeri interi che non si lasci mettere in difficolta'. Requisiti:

- un menu in un `do while`, con le operazioni divisione intera, resto, potenza e MCD, e la scelta $0$ per uscire;
- scelte fuori menu segnalate con un messaggio, usando due costanti `const` per la scelta piu' piccola ($0$) e per la piu' grande ($4$);
- ogni `scanf` controllata: se l'utente non scrive numeri, il programma termina con un errore e restituisce $1$;
- divisione e resto rifiutano il divisore $0$, la potenza rifiuta gli esponenti negativi, il MCD accetta solo numeri positivi;
- almeno un `assert` dove siete sicuri che una condizione debba essere vera;
- all'uscita, il numero di operazioni eseguite con successo.

```text
1) Divisione intera  2) Resto  3) Potenza  4) MCD  0) Esci
Scelta: 2
Due numeri interi: 17 0
Errore: il secondo numero non puo' essere 0
1) Divisione intera  2) Resto  3) Potenza  4) MCD  0) Esci
Scelta: 3
Due numeri interi: 2 10
2 elevato a 10 = 1024
1) Divisione intera  2) Resto  3) Potenza  4) MCD  0) Esci
Scelta: 0
Operazioni eseguite: 1
```

## Pacchetto N: break, continue, enum e macro

Questo pacchetto aggiunge le istruzioni `break` e `continue`, le enumerazioni (`enum`) e le macro con parametri, insieme al flag `-E`, che mostra il lavoro del preprocessore. Compilate sempre con `gcc -g -Wall -Wextra`. Come nei Pacchetti E ed F, gdb vi accompagna quando serve a vedere cio' che l'output non mostra, con i soli comandi gia' visti (li trovate riassunti alla fine di quei pacchetti); le domande che lo usano iniziano con **Con gdb.** Negli esercizi scrivete `break` e `continue` su una riga a se', dentro le graffe dell'`if`, come negli esempi qui sotto: alcune domande con gdb mettono un breakpoint proprio su quelle righe.

### break e continue

`break` fa uscire subito dal ciclo in cui si trova. `continue` salta il resto del corpo e passa al giro successivo: in un `for` esegue comunque l'aggiornamento (per esempio `i++`) e poi controlla la condizione; in un `while` o in un `do while` passa direttamente alla condizione.

```c
for (d = 2; d * d <= n; d++) {
    if (n % d == 0) {
        break;              /* trovato un divisore: inutile proseguire */
    }
}

for (i = 1; i <= 20; i++) {
    if (i % 3 == 0) {
        continue;           /* salta i multipli di 3 */
    }
    printf("%d ", i);
}
```

Due avvertenze. Se i cicli sono uno dentro l'altro, `break` e `continue` agiscono solo su quello piu' interno. E un `break` dentro uno `switch` chiude lo `switch`, non il ciclo che lo contiene. Con `break` si puo' anche scrivere un ciclo "infinito" che si interrompe dall'interno, `while (1) { ... }`: la condizione $1$ e' sempre vera.

| Pseudocodice | C |
| --- | --- |
| `ESCI DAL CICLO` | `break;` |
| `PASSA AL GIRO SUCCESSIVO` | `continue;` |

### Le enumerazioni

Un'enumerazione da' un nome a un gruppo di costanti intere:

```c
enum seme {CUORI, QUADRI, FIORI, PICCHE};      /* valgono 0, 1, 2, 3 */
enum mese {GENNAIO = 1, FEBBRAIO, MARZO};      /* 1, 2, 3: si puo' scegliere da dove partire */

enum seme s = FIORI;
if (s == FIORI) {
    printf("Fiori!\n");
}
```

Il codice diventa piu' leggibile (`s == FIORI` invece di `s == 2`) e alcuni errori si vedono meglio: se uno `switch` su una variabile di tipo `enum` dimentica un caso e non ha il `default`, `-Wall` lo segnala. A differenza delle costanti create con `#define`, i nomi di un `enum` arrivano fino a gdb: `print s` risponde `FIORI` e `print/d s` risponde $2$.

### Le macro con parametri e il flag -E

Con `#define` si possono scrivere anche macro con parametri, che si usano come funzioni:

```c
#define QUADRATO(x) ((x) * (x))
#define PARI(n) ((n) % 2 == 0)

y = QUADRATO(a + 1);
if (PARI(y)) {
    printf("pari\n");
}
```

Il preprocessore non calcola nulla: sostituisce il testo prima della compilazione, quindi `QUADRATO(a + 1)` diventa `((a + 1) * (a + 1))`. Per questo ogni parametro e l'intera macro vanno messi tra parentesi, e un argomento che modifica una variabile, come `i++`, rischia di essere eseguito piu' di una volta. Una macro lunga si puo' spezzare su piu' righe terminando ogni riga, tranne l'ultima, con `\`.

Il flag `-E` ferma gcc subito dopo il preprocessore e mostra il risultato:

```bash
gcc -E quadrato.c -o quadrato.i
```

Il file `quadrato.i` comincia con centinaia di righe che vengono da `stdio.h`; il vostro programma, con le macro gia' sostituite, e' in fondo (in VS Code ci si arriva con Ctrl+Fine). Le righe che iniziano con `#` sono annotazioni per il compilatore e si possono ignorare. Da terminale c'e' una scorciatoia: `gcc -E quadrato.c | tail -n 20` mostra solo le ultime $20$ righe.

Le macro non arrivano a gdb: `print QUADRATO(3)` risponde `No symbol "QUADRATO" in current context`, come `print OBIETTIVO` in E7. Per vedere che cosa ne ha fatto il preprocessore serve `-E`.

Nelle macro torna comodo l'operatore condizionale `?:`: `c ? x : y` vale `x` se la condizione `c` e' vera, `y` altrimenti. Per esempio:

```c
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(x) ((x) < 0 ? -(x) : (x))
```

### Esercizi (N1-N20)

#### break e continue

**N1.** Il programma cerca il piu' piccolo divisore di $n$ maggiore di $1$ e si ferma con `break` appena lo trova.

```c
#include <stdio.h>

int main(void) {
    int n, d;
    printf("Inserisci un intero maggiore di 1: ");
    scanf("%d", &n);
    for (d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            break;
        }
    }
    if (d * d <= n) {
        printf("%d non e' primo: il suo piu' piccolo divisore e' %d\n", n, d);
    } else {
        printf("%d e' primo\n", n);
    }
    return 0;
}
```

1. Dopo il ciclo il programma non sa se il `break` e' scattato: lo deduce dalla condizione `d * d <= n`. Perche' funziona? E perche' basta cercare i divisori finche' $d^2 \le n$?
2. Togliete il `break`: cosa stampa il programma con $391$? Perche'?
3. **Con gdb.** Prevedete il valore di `d` dopo il ciclo per $n = 391$, $397$, $1024$ e $999983$ (che e' primo), poi verificate con un breakpoint sull'`if` che segue il ciclo.

**N2.** Il programma somma i numeri da $1$ a `LIMITE` che non sono divisibili ne' per $2$ ne' per $3$, saltando gli altri con due `continue`.

```c
#include <stdio.h>
#define LIMITE 100

int main(void) {
    int i, somma = 0, quanti = 0;
    for (i = 1; i <= LIMITE; i++) {
        if (i % 2 == 0) {
            continue;
        }
        if (i % 3 == 0) {
            continue;
        }
        somma += i;
        quanti++;
    }
    printf("Da 1 a %d ci sono %d numeri non divisibili ne' per 2 ne' per 3; la loro somma e' %d\n", LIMITE, quanti, somma);
    return 0;
}
```

1. Prevedete quante volte viene eseguito ciascuno dei due `continue` e quanti numeri vengono sommati. Suggerimento: principio di inclusione-esclusione.
2. Quanto valgono `quanti` e `somma` considerando solo i numeri da $1$ a $49$? Prevedetelo, poi verificate portando `LIMITE` a $49$.
3. **Con gdb.** Con un breakpoint sul primo `if` e la condizione `if i == 9`, seguite il percorso con `next`: quale `continue` scatta? E per $i = 12$?

**N3.** Trova l'errore. E' il programma di N2 riscritto con un `while`: compila senza warning, ma non stampa nulla e non termina. Lanciatelo in gdb, fermatelo con Ctrl+C e stampate `i`; con qualche `next`, quali righe vengono eseguite? Correggete il programma. Perche' con il `for` di N2 il problema non si presentava?

```c
#include <stdio.h>

int main(void) {
    int i = 1, somma = 0, quanti = 0;
    while (i <= 100) {
        if (i % 2 == 0 || i % 3 == 0) {
            continue;
        }
        somma += i;
        quanti++;
        i++;
    }
    printf("Da 1 a 100 ci sono %d numeri non divisibili ne' per 2 ne' per 3; la loro somma e' %d\n", quanti, somma);
    return 0;
}
```

**N4.** Esiste una sola terna pitagorica $a < b < c$ con $a + b + c = 1000$. Il programma la cerca con due cicli e, appena la trova, la stampa ed esce con `break`.

```c
#include <stdio.h>
#define PERIMETRO 1000

int main(void) {
    int a, b, c;
    for (a = 1; a < PERIMETRO / 3; a++) {
        for (b = a + 1; b < PERIMETRO / 2; b++) {
            c = PERIMETRO - a - b;
            if (a * a + b * b == c * c) {
                printf("Terna: %d %d %d\n", a, b, c);
                break;
            }
        }
    }
    printf("Ricerca finita\n");
    return 0;
}
```

1. **Con gdb.** L'output e' giusto, ma il `break` ferma davvero la ricerca? Mettete un breakpoint sulla riga `printf("Ricerca finita\n");` e stampate `a` e `b`: che valori hanno, e perche'?
2. Aggiungete un contatore `prove` delle coppie $(a, b)$ esaminate e stampatelo alla fine: quante coppie esamina il programma? Tenete questa modifica.
3. Correggete il programma con una variabile `trovata`, che vale $0$ e diventa $1$ quando trovate la terna, e un secondo `break` nel ciclo esterno. Ripetete la prova del punto 1: ora quanto valgono `a` e `b` alla fine? Quante coppie esamina ora il programma, e quante ne avete risparmiate?

**N5.** Scrivete un programma che legge voti d'esame, uno alla volta nella variabile `voto`, finche' l'utente non scrive $0$, e li salva in un array di al massimo `MAX_VOTI` elementi (con `#define MAX_VOTI 50`); alla fine stampa quanti voti sono validi, quanti sono stati scartati e la media dei validi con due decimali (se non ci sono voti validi, al posto della media stampa `Nessun voto valido`). Usate un ciclo `while (1)` con questi controlli, in quest'ordine:

- se `scanf` non riesce a leggere un numero (rivedete M11), `break`;
- se il voto e' $0$, `break`;
- se il voto e' fuori dall'intervallo da $18$ a $30$, contatelo tra gli scartati e `continue`;
- se l'array e' pieno, `break`; altrimenti salvate il voto.

```text
Voti (0 per finire): 28 30 17 24 31 30 0 27
Voti validi: 4, scartati: 2
Media: 28.00
```

1. Provate con i numeri dell'esempio, scritti tutti su una riga: perche' il $27$ non viene letto? E con `25 26 x 27`? Quale `break` chiude il ciclo nei due casi?
2. **Con gdb.** Togliete il controllo sul valore restituito da `scanf` e inserite `25 17 x`: il programma non termina piu'. Fermatelo con Ctrl+C: quanto vale `voto`, e quali righe si ripetono (`next`)? Perche'?

**N6.** Dallo pseudocodice al C. La congettura di Goldbach (1742, ancora aperta) afferma che ogni numero pari maggiore di $2$ e' somma di due numeri primi. L'algoritmo la verifica per tutti i pari fino a $N = 100$: per ogni $n$ cerca il piu' piccolo primo $p$ tale che anche $n - p$ sia primo, e stampa i casi in cui questo $p$ batte il record precedente. I primi si riconoscono con il vettore `_primo` costruito dal crivello di Eratostene, come in F16. Come in C, se il PER arriva alla fine senza uscire, `_p` vale `_n / 2 + 1`.

```text
INIZIO
    costruisci il vettore _primo fino a _N con il crivello di Eratostene (F16)
    ASSEGNA a _record il valore 0
    ASSEGNA a _n il valore 4
    FINCHE' _n <= _N
        PER _p DA 2 A _n / 2
            SE _primo[_p] = 0 ALLORA
                PASSA AL GIRO SUCCESSIVO
            FINE
            SE _primo[_n - _p] = 1 ALLORA
                ESCI DAL CICLO
            FINE
        FINE
        SE _p > _n / 2 ALLORA
            VISUALIZZA "Controesempio alla congettura di Goldbach:" e _n
        ALTRIMENTI SE _p > _record ALLORA
            ASSEGNA a _record il valore _p
            VISUALIZZA _n "=" _p "+" _n - _p
        FINE
        ASSEGNA a _n il valore _n + 2
    FINE
FINE
```

```text
4 = 2 + 2
6 = 3 + 3
12 = 5 + 7
30 = 7 + 23
98 = 19 + 79
```

1. Per $n = 98$ il programma prova i valori di $p$ da $2$ a $19$: quali vengono scartati dal `PASSA AL GIRO SUCCESSIVO`, e quali arrivano al secondo controllo?
2. **Con gdb.** Verificate la risposta con un breakpoint sulla riga del `continue`, la condizione `if n == 98` e `display p`.
3. Perche' il ciclo interno e' un PER e non un FINCHE'? Pensate a che cosa farebbe `PASSA AL GIRO SUCCESSIVO` in un FINCHE' con l'aggiornamento di `_p` in fondo al corpo (rivedete N3).
4. Portate $N$ a $10000$: quali nuovi record compaiono?

#### Enumerazioni

**N7.** Il 1 gennaio 2026 e' un giovedi'. Il programma calcola in quali mesi del 2026 il giorno 13 cade di venerdi'.

```c
#include <stdio.h>

enum giorno {LUNEDI, MARTEDI, MERCOLEDI, GIOVEDI, VENERDI, SABATO, DOMENICA};

int main(void) {
    int durata[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    enum giorno primo = GIOVEDI;
    enum giorno tredici;
    int mese, quanti = 0;
    for (mese = 1; mese <= 12; mese++) {
        tredici = (primo + 12) % 7;
        if (tredici == VENERDI) {
            printf("Venerdi' 13 nel mese %d\n", mese);
            quanti++;
        }
        primo = (primo + durata[mese - 1]) % 7;
    }
    printf("Nel 2026 i venerdi' 13 sono %d\n", quanti);
    return 0;
}
```

1. Perche' `(primo + 12) % 7` e' il giorno della settimana del 13? E perche' `(primo + durata[mese - 1]) % 7` e' quello del primo giorno del mese successivo?
2. **Con gdb.** Mettete un breakpoint sulla riga `if (tredici == VENERDI)` e lanciate il programma: cosa rispondono `print primo`, `print/d primo` e `print tredici`? In che giorno cade il 13 gennaio 2026?
3. **Con gdb.** I nomi dell'`enum` si possono usare anche nelle condizioni: con un breakpoint sulla stessa riga e la condizione `if tredici == VENERDI`, stampando `mese` a ogni fermata, trovate i mesi con un venerdi' 13 senza guardare l'output. Perche' non si potrebbe fare se `VENERDI` fosse definito con `#define`?
4. **In piu'.** In quale anno, dopo il 2026, il 13 gennaio cadra' di venerdi'? Servono gli anni bisestili (D31).

**N8.** Leggendo le cifre di un numero binario da sinistra a destra, ogni nuova cifra $b$ trasforma il numero $x$ letto finora in $2x + b$; quindi il resto $r$ della divisione per $3$ diventa il resto di $2r + b$. Per sapere se un numero binario e' divisibile per $3$ basta quindi ricordare il resto: e' un *automa* con tre stati. Scrivete un programma con `enum stato {RESTO0, RESTO1, RESTO2};` e una variabile `s` di tipo `enum stato`, che parte da `RESTO0`. Il programma legge le cifre un carattere alla volta con `scanf("%c", &c)`: l'a capo chiude la lettura (`break`), gli spazi si saltano (`continue`), qualsiasi altro carattere diverso da `0` e `1` produce un messaggio di errore e fa terminare il programma con `return 1`. Il passaggio da uno stato all'altro si fa con uno `switch` su `s`, senza `default` (lo stato puo' valere solo i tre valori dell'`enum`), seguendo la tabella.

| Stato attuale | Cifra 0 | Cifra 1 |
| --- | --- | --- |
| `RESTO0` | `RESTO0` | `RESTO1` |
| `RESTO1` | `RESTO2` | `RESTO0` |
| `RESTO2` | `RESTO1` | `RESTO2` |

```text
Numero in base 2: 1101 0110
Letti 8 bit: resto della divisione per 3 = 1
Il numero non e' divisibile per 3
```

1. Ricavate la tabella dalla regola $r \to 2r + b$: per esempio, perche' da `RESTO1` con la cifra $0$ si va in `RESTO2`?
2. Togliete di proposito uno dei tre `case`: cosa dice `-Wall`?
3. Perche' lo stesso programma funziona anche con numeri di cento cifre, che non entrerebbero in nessun tipo intero?
4. **Con gdb.** Mettete un breakpoint sulla riga dello `switch`, date `display c` e `display s` e inserite `110110`: completate la tabella con i valori a ogni fermata (lo stato e' quello prima della transizione). In quale stato finisce l'automa? Che numero e' `110110` in base $10$?

| Fermata | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| `c` |  |  |  |  |  |  |
| `s` |  |  |  |  |  |  |

**N9.** Un trucco comune: aggiungere in fondo a un `enum` un nome che conta gli elementi precedenti, e usarlo come dimensione di un array. Il programma classifica i numeri da $1$ a $100$ come in E18.

```c
#include <stdio.h>
#define LIMITE 100

enum tipo {DIFETTIVO, PERFETTO, ABBONDANTE, NUM_TIPI};

int main(void) {
    int conteggio[NUM_TIPI] = {0};
    int n, d, somma;
    enum tipo t;
    for (n = 1; n <= LIMITE; n++) {
        somma = 0;
        for (d = 1; d <= n / 2; d++) {
            if (n % d == 0) {
                somma += d;
            }
        }
        if (somma < n) {
            t = DIFETTIVO;
        } else if (somma == n) {
            t = PERFETTO;
        } else {
            t = ABBONDANTE;
        }
        conteggio[t]++;
    }
    for (t = DIFETTIVO; t < NUM_TIPI; t++) {
        switch (t) {
            case DIFETTIVO:
                printf("Difettivi: ");
                break;
            case PERFETTO:
                printf("Perfetti: ");
                break;
            case ABBONDANTE:
                printf("Abbondanti: ");
                break;
            case NUM_TIPI:
                break;
        }
        printf("%d\n", conteggio[t]);
    }
    return 0;
}
```

1. Perche' `NUM_TIPI` vale proprio il numero dei tipi? Che vantaggio c'e' a usarlo come dimensione dell'array e come limite del ciclo finale?
2. **Con gdb.** Con un breakpoint sulla riga `conteggio[t]++;` e la condizione `if t == PERFETTO`, trovate i numeri perfetti fino a $100$ stampando `n` a ogni fermata. Alla seconda fermata, che cosa mostra `print conteggio`?
3. Aggiungete un tipo `QUASI_PERFETTO` (somma dei divisori propri uguale a $n - 1$) tra `DIFETTIVO` e `PERFETTO`, senza toccare lo `switch`: cosa dice `-Wall`? Poi completate il programma, `switch` compreso, e tenete la modifica: quali numeri quasi perfetti trovate? Attenzione all'ordine dei controlli sulla somma. (Curiosita': non si sa se ne esistano altri oltre a quelli che vedrete.)
4. Nello `switch` c'e' un caso `NUM_TIPI` che non fa nulla. Se lo sostituiste con un `default`, il warning del punto 3 comparirebbe ancora? Che cosa conviene, allora?

**N10.** Trova l'errore. Due errori: uno lo segnala `-Wall`, l'altro si vede eseguendo il programma. Inserendo le scelte `1 7 3 5 0`, anche tutte su una riga, il programma dovrebbe calcolare il quadrato di $7$ e l'opposto di $5$, poi salutare e terminare. Invece la scelta $3$ non produce nulla e, dopo `Arrivederci!`, il menu ricompare e il programma non termina.

```c
#include <stdio.h>

enum voce {ESCI, QUADRATO, CUBO, OPPOSTO};

int main(void) {
    int scelta, x;
    enum voce v;
    while (1) {
        printf("0) Esci  1) Quadrato  2) Cubo  3) Opposto\nScelta: ");
        scanf("%d", &scelta);
        v = scelta;
        switch (v) {
            case ESCI:
                printf("Arrivederci!\n");
                break;
            case QUADRATO:
                printf("Numero: ");
                scanf("%d", &x);
                printf("%d al quadrato = %d\n", x, x * x);
                break;
            case CUBO:
                printf("Numero: ");
                scanf("%d", &x);
                printf("%d al cubo = %d\n", x, x * x * x);
                break;
        }
    }
    return 0;
}
```

**Con gdb.** Mettete un breakpoint sulla riga dello `switch`, scegliete $0$ e seguite con `next` che cosa succede dopo il `break` del caso `ESCI`. Correggete entrambi gli errori.

**N11.** Trova l'errore. Il programma legge il numero di un mese e ne stampa i giorni e la stagione. Con $3$ stampa $30$ giorni (marzo ne ha $31$), con $2$ stampa `primavera` e con $12$ un numero assurdo, senza nessuna stagione. Nessun warning.

```c
#include <stdio.h>

enum mese {GENNAIO, FEBBRAIO, MARZO, APRILE, MAGGIO, GIUGNO,
           LUGLIO, AGOSTO, SETTEMBRE, OTTOBRE, NOVEMBRE, DICEMBRE};

int main(void) {
    int durata[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int numero;
    enum mese m;
    printf("Numero del mese (da 1 a 12): ");
    scanf("%d", &numero);
    m = numero;
    printf("Giorni: %d\n", durata[m]);
    switch (m) {
        case DICEMBRE:
        case GENNAIO:
        case FEBBRAIO:
            printf("Stagione: inverno\n");
            break;
        case MARZO:
        case APRILE:
        case MAGGIO:
            printf("Stagione: primavera\n");
            break;
        case GIUGNO:
        case LUGLIO:
        case AGOSTO:
            printf("Stagione: estate\n");
            break;
        case SETTEMBRE:
        case OTTOBRE:
        case NOVEMBRE:
            printf("Stagione: autunno\n");
            break;
    }
    return 0;
}
```

**Con gdb.** Con un breakpoint sulla riga della prima `printf` dopo la lettura, stampate `m` inserendo $3$ e poi $12$. Che cosa mostra gdb nel secondo caso, e perche' non compare un nome? Correggete il programma in due modi diversi: cambiando il valore iniziale dell'`enum`, oppure lasciandolo com'e' e cambiando il modo di calcolare `m`. Cosa bisogna sistemare, nei due casi, perche' anche `durata` resti corretto? Aggiungete infine una validazione con `do while`.

#### Macro e flag -E

**N12.** Trova l'errore. Il programma somma i quadrati da $1^2$ a $n^2$ e confronta il risultato con la formula $\frac{n(n+1)(2n+1)}{6}$: con $n = 10$ dovrebbe ottenere $385$, ma stampa $100$.

```c
#include <stdio.h>
#define QUADRATO(x) x * x

int main(void) {
    int n, k, somma = 0;
    printf("Inserisci n: ");
    scanf("%d", &n);
    for (k = 0; k < n; k++) {
        somma += QUADRATO(k + 1);
    }
    printf("1^2 + 2^2 + ... + %d^2 = %d\n", n, somma);
    printf("Formula n(n+1)(2n+1)/6 = %d\n", n * (n + 1) * (2 * n + 1) / 6);
    return 0;
}
```

1. **Con gdb.** Mettete un breakpoint sulla riga della somma, con `display k` e `display somma`, e andate avanti con `continue`. Che numeri assume `somma` alle fermate? Li avete gia' incontrati in E2: perche' compaiono qui? Provate anche `print QUADRATO(k + 1)`: cosa risponde gdb?
2. Generate il file preprocessato con `gcc -E` e cercate in fondo la riga della somma: che cosa e' diventata?
3. Mettete tra parentesi il parametro, `#define QUADRATO(x) (x) * (x)`: ora la somma e' giusta. Ma che cosa stampa `printf("%d\n", 100 / QUADRATO(5));`? Controllate con `-E` e scrivete la versione definitiva della macro.

**N13.** Trova l'errore. Il programma deve stampare il massimo dell'array, cioe' $11$, ma stampa $6$. Nessun warning.

```c
#include <stdio.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define N 8

int main(void) {
    int v[N] = {3, 9, 2, 7, 11, 4, 8, 6};
    int i = 0, massimo = v[0];
    while (i < N) {
        massimo = MAX(massimo, v[i++]);
    }
    printf("Il massimo e' %d\n", massimo);
    return 0;
}
```

1. **Con gdb.** Mettete un breakpoint sulla riga con `MAX` e usate `display i` e `display massimo`: quali valori di `i` vedete alle fermate? Quali elementi dell'array vengono saltati?
2. Guardate con `-E` come e' stata espansa la riga e spiegate il comportamento. Seguite a mano l'esecuzione e verificate che il risultato sia proprio $6$.
3. Correggete il programma. Che regola conviene seguire quando si passano argomenti a una macro?

**N14.** Una macro molto usata calcola il numero di elementi di un array: `sizeof(v)` sono i byte dell'intero array, `sizeof(v[0])` quelli di un elemento. Il programma la usa per calcolare il prodotto di Eulero $\prod_p \left(1 - \frac{1}{p^2}\right)$ sui primi dell'array, che si avvicina a $\frac{6}{\pi^2} \approx 0.607927$, il reciproco della somma di E13. Notate la dichiarazione `int primi[] = {...};`: quando si scrivono i valori iniziali, la dimensione si puo' omettere e la conta il compilatore.

```c
#include <stdio.h>
#define DIM(v) (sizeof(v) / sizeof((v)[0]))

int main(void) {
    int primi[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    double prodotto = 1;
    int i;
    for (i = 0; i < DIM(primi); i++) {
        prodotto *= 1 - 1.0 / (primi[i] * primi[i]);
    }
    printf("Primi usati: %d\n", (int) DIM(primi));
    printf("Prodotto di (1 - 1/p^2) = %f\n", prodotto);
    printf("6 / pi^2 = 0.607927...\n");
    return 0;
}
```

1. Compilate con i tre flag: quale warning compare, e su quale riga? Il risultato di `sizeof` e' un intero senza segno (rivedete F12): correggete il confronto con un cast.
2. Guardate con `-E` come diventa la condizione del `for`.
3. Aggiungete all'array tutti i primi fino a $97$: cosa dovete cambiare nel resto del programma? Di quanto si avvicina il prodotto a $\frac{6}{\pi^2}$?

**N15.** Ci sono tre modi per dare un nome alla dimensione di un array: una `#define`, una variabile `const` o una costante di un `enum` (anche senza nome).

```c
#include <stdio.h>
#define DIM_A 5

enum {DIM_C = 5};

int main(void) {
    const int DIM_B = 5;
    int a[DIM_A] = {0};
    int b[DIM_B] = {0};
    int c[DIM_C] = {0};
    printf("%d %d %d\n", a[0], b[0], c[0]);
    return 0;
}
```

1. Compilate: quale riga da' errore? Per il C, un array la cui dimensione e' una variabile, anche se `const`, ha *dimensione variabile* e non si puo' inizializzare con dei valori tra graffe (le versioni recenti di gcc accettano solo le graffe vuote `{}`). Correggete togliendo l'inizializzazione di `b` e assegnando `b[0] = 0;` prima della `printf`.
2. **Con gdb.** Fermatevi sulla `printf` e provate `print DIM_A`, `print DIM_B` e `print DIM_C`: quali nomi conosce gdb?
3. Con `-E`, quale dei tre nomi sparisce dal programma?
4. Riassumete in una tabella, per ciascuno dei tre modi: si puo' usare come dimensione di un array inizializzato con dei valori, come `{0}`? gdb lo conosce? Il preprocessore lo sostituisce? Quale scegliereste, e quando?

**N16.** Una macro per scambiare due variabili, da usare al posto delle tre righe di C13.

```c
#include <stdio.h>
#define SCAMBIA(x, y) { int t = x; x = y; y = t; }

int main(void) {
    int a, b;
    printf("Due numeri: ");
    scanf("%d %d", &a, &b);
    if (a > b)
        SCAMBIA(a, b);
    else
        printf("Gia' in ordine\n");
    printf("In ordine: %d %d\n", a, b);
    return 0;
}
```

1. Compilate: gcc segnala `'else' without a previous 'if'`. Guardate con `-E` la riga della macro espansa: da dove viene l'errore?
2. Il rimedio classico e' racchiudere il corpo della macro in un `do { ... } while (0)`: un ciclo che viene eseguito una volta sola e che, come ogni `do while`, va chiuso con il `;` scritto dopo la macro. Riscrivete la macro cosi', su piu' righe chiuse da `\`, con le parentesi attorno ai parametri e sempre con la variabile d'appoggio `t`, e verificate che il programma funzioni.
3. Usate `SCAMBIA` nell'ordinamento a bolle di F18, con l'array fissato `{5, 1, 4, 2, 8, 0}`. Contate gli scambi con una variabile.
4. **Con gdb.** Con un breakpoint sulla riga in cui usate la macro e `display v`, guardate l'array cambiare a ogni scambio.
5. Ora provate a scambiare due variabili che si chiamano `t` e `u`, con `int t = 3, u = 8;` e `SCAMBIA(t, u);`. Stampate `t` e `u` subito dopo: lo scambio e' avvenuto? Con `-E` capite perche' e correggete la macro.

**N17.** Dallo pseudocodice al C. Se un polinomio a coefficienti interi ha una radice intera $d$, allora $d$ divide il termine noto. L'algoritmo prova quindi solo i divisori del termine noto e si ferma quando ha trovato tante radici quanto e' il grado. Il polinomio e' $p(x) = x^3 - 2x^2 - 5x + 6$: scrivetelo nella macro `P(x)`, scrivete il valore assoluto nella macro `ABS(x)` con l'operatore `?:` e il grado in `#define GRADO 3`.

```text
INIZIO
    ASSEGNA a _noto il valore p(0)
    ASSEGNA a _radici il valore 0
    PER _d DA -|_noto| A |_noto|
        SE _d = 0 ALLORA
            PASSA AL GIRO SUCCESSIVO
        FINE
        SE il resto di _noto diviso _d e' diverso da 0 ALLORA
            PASSA AL GIRO SUCCESSIVO
        FINE
        SE p(_d) = 0 ALLORA
            VISUALIZZA "Radice intera:" e _d
            ASSEGNA a _radici il valore _radici + 1
            SE _radici = GRADO ALLORA
                ESCI DAL CICLO
            FINE
        FINE
    FINE
    VISUALIZZA _radici
FINE
```

```text
Radice intera: -2
Radice intera: 1
Radice intera: 3
Radici intere trovate: 3
```

1. Dimostrate che una radice intera di un polinomio a coefficienti interi divide il termine noto.
2. Scrivete l'intestazione del ciclo come `for (d = -ABS(noto); d <= ABS(noto); d++)` e guardate con `-E` come diventano `noto = P(0);` e questa intestazione. Quante volte viene calcolato `ABS(noto)` dall'inizio alla fine del ciclo, inizializzazione compresa?
3. Quali valori di $d$ vengono scartati dal secondo `continue`, e per quali viene calcolato `P(d)`? Contate i calcoli di `P(d)` con un contatore e tenete questa modifica.
4. **Con gdb.** Controllate quanto vale `d` dopo il ciclo: perche' proprio quel valore?
5. Cambiate polinomio: $x^4 - 5x^2 + 4$, con `GRADO` uguale a $4$. Quali radici trova il programma? Quante volte viene calcolato `P(d)`?

**N18.** Un codice ISBN-10 e' formato da dieci cifre $d_1 d_2 \dots d_{10}$, l'ultima delle quali puo' essere `X`, che vale $10$. Il codice e' valido se $10 d_1 + 9 d_2 + 8 d_3 + \dots + 1 \cdot d_{10}$ e' multiplo di $11$. Scrivete un programma che legge il codice un carattere alla volta con `scanf("%c", &c)` e accumula la somma pesata nella variabile `somma`: i trattini e gli spazi si saltano con `continue`, l'a capo chiude la lettura con `break`, una `X` e' accettata solo come decima cifra. Un altro carattere, o un numero di cifre diverso da dieci (contando la `X`), e' un errore: il programma stampa un messaggio e termina con `return 1`. Per riconoscere le cifre e calcolarne il valore usate due macro che lavorano sui codici ASCII:

```c
#define E_CIFRA(c) ((c) >= '0' && (c) <= '9')
#define VALORE(c) ((c) - '0')
```

```text
Codice ISBN-10: 0-306-40615-2
Codice valido (somma pesata 132 = 11 x 12)

Codice ISBN-10: 0-8044-2957-X
Codice valido (somma pesata 209 = 11 x 19)

Codice ISBN-10: 0-306-40651-2
Codice NON valido (somma pesata 136, resto 4)
```

1. **Con gdb.** Con un breakpoint sulla riga che aggiorna la somma pesata e `display c`, `display somma`, seguite il calcolo per `0-306-40615-2`. Perche' gdb mostra `c` come `51 '3'`?
2. Il terzo codice dell'esempio e' il primo con due cifre vicine scambiate (`15` e' diventato `51`). Dimostrate che scambiare due cifre adiacenti diverse rende sempre il codice non valido.
3. Guardate con `-E` come diventano le righe che usano `E_CIFRA` e `VALORE`.

#### Mettere insieme i pezzi

**N19.** Riprendiamo la congettura di Collatz (D43): tra i numeri di partenza da $1$ a $999$, quale produce la sequenza piu' lunga?

```c
#include <stdio.h>
#define LIMITE 1000

int main(void) {
    int partenza, x, passi, record = -1, campione = 0;
    for (partenza = 1; partenza < LIMITE; partenza++) {
        x = partenza;
        passi = 0;
        while (x != 1) {
            if (x % 2 == 0) {
                x /= 2;
            } else {
                x = 3 * x + 1;
            }
            passi++;
        }
        if (passi > record) {
            record = passi;
            campione = partenza;
        }
    }
    printf("Sotto %d la sequenza piu' lunga parte da %d: %d passi\n", LIMITE, campione, record);
    return 0;
}
```

1. Il programma stampa solo il risultato finale. Fategli stampare anche ogni nuovo record, con il numero di partenza e i passi, e tenete questa modifica: quali numeri stabiliscono un record? Quanti record vengono stampati, contando anche il primo (la partenza $1$, con $0$ passi)?
2. **Con gdb.** Partendo da $27$ servono $111$ passi. Qual e' il valore piu' alto raggiunto da quella sequenza, e dopo quanti passi? Usate un breakpoint sulla riga `if (x % 2 == 0)` con la condizione `if partenza == 27 && x > 9000`.
3. Alcuni record sono numeri pari. Dimostrate che, se $k$ fa $s$ passi, $2k$ ne fa $s + 1$. Poi spiegate perche', se $k$ e' un record e nessuna partenza tra $k$ e $2k$ lo supera, $2k$ stabilisce un nuovo record. Cercate nell'elenco del punto 1 un record $k$, con $2k < 1000$, per cui $2k$ non e' un record: che cosa e' successo?
4. Aggiungete all'inizio del ciclo esterno `if (partenza % 2 == 0) continue;`, per provare solo le partenze dispari: il risultato finale cambia? E il numero di record stampati?
5. Con un `break`, fate fermare la ricerca alla prima partenza che supera i $100$ passi: quale?

**N20.** **Sfida.** Il calendario. Il programma legge un anno tra $1900$ e $2100$ e un mese, e stampa il calendario di quel mese. Requisiti:

- `enum giorno` (da `LUNEDI` a `DOMENICA`) ed `enum mese` (da `GENNAIO = 1` a `DICEMBRE`);
- le macro `BISESTILE(a)` (rivedete D31) e `GIORNI_ANNO(a)`, che usa `BISESTILE` e l'operatore `?:`, e `#define` per il primo e l'ultimo anno accettati;
- la lettura in un `do while` che rifiuta valori fuori intervallo, con la `scanf` controllata come in M11;
- un array `durata[13]`, in cui `durata[0]` non si usa, cosi' che `durata[m]` sia la durata del mese `m`; febbraio ha $29$ giorni negli anni bisestili;
- il giorno della settimana del primo giorno del mese, ottenuto contando nella variabile `giorni` i giorni passati dal 1 gennaio 1900, che era un lunedi', e prendendone il resto della divisione per $7$, da salvare nella variabile `primo` di tipo `enum giorno`;
- il nome del mese stampato con uno `switch` sull'`enum mese`, senza `default`;
- la griglia stampata con `%3d`, che scrive un intero occupando sempre $3$ caratteri, a partire dal lunedi'.

```text
Anno (1900-2100) e mese (1-12): 2026 2
Febbraio 2026
 Lu Ma Me Gi Ve Sa Do
                    1
  2  3  4  5  6  7  8
  9 10 11 12 13 14 15
 16 17 18 19 20 21 22
 23 24 25 26 27 28
```

1. Guardate con `-E` come viene espansa la riga che usa `GIORNI_ANNO`: quante volte compare l'anno?
2. **Con gdb.** Con un breakpoint sulla riga che calcola `primo`, stampate `giorni` per gennaio 2000 e, dopo un `next`, `primo`: deve essere `SABATO`. Quanti giorni risultano per gennaio 2026, e quale giorno della settimana?
3. Togliete un mese dallo `switch`: cosa dice `-Wall`?


## Pacchetto O: La libreria standard

Fin dal primo programma avete usato una libreria: `stdio.h`, con `printf` e `scanf`. Una libreria e' codice gia' scritto, e collaudato da decenni, che si rende disponibile con `#include`; quella che accompagna ogni compilatore C si chiama *libreria standard*. Questo pacchetto e' una panoramica delle sue parti piu' usate. Non serve impararne a memoria le funzioni (per quello c'e' [cppreference](https://it.cppreference.com/c), che avete gia' incontrato): l'idea e' capire *perche'* conviene usarle invece di riscriverle. Le funzioni della libreria funzionano anche nei casi difficili, sono precise e veloci, e chi legge il vostro codice le riconosce subito. Qualche volta, come vedrete, bisogna comunque sapere che cosa fanno davvero.

Compilate sempre con `gcc -g -Wall -Wextra`. Come nei Pacchetti G e H, `time`, `-O2` e gprof accompagnano qualche esercizio, e gdb resta a disposizione.

### Le librerie piu' usate

| Libreria | A che cosa serve | Qualche funzione o costante | Dove l'avete incontrata |
| --- | --- | --- | --- |
| `stdio.h` | input e output | `printf`, `scanf` | dal Pacchetto B |
| `stdlib.h` | strumenti di uso generale | `rand`, `srand`, `abs`, `exit` | G2 |
| `math.h` | funzioni matematiche | `sqrt`, `pow`, `fabs`, `floor`, `round`, `sin`, `cos`, `atan2`, `M_PI` | nuova |
| `limits.h` | limiti dei tipi interi | `INT_MAX`, `LONG_MAX` | F2, M18 |
| `float.h` | limiti dei tipi reali | `DBL_EPSILON`, `DBL_MAX` | nuova |
| `ctype.h` | riconoscere e trasformare i caratteri | `isdigit`, `isalpha`, `toupper` | nuova |
| `time.h` | data, ora e tempo | `time`, `clock` | G2 |
| `assert.h` | controlli durante lo sviluppo | `assert` | M |

Manca `string.h`, per lavorare con i testi: la incontrerete quando studierete le stringhe.

### Due novita' tecniche

**Il flag `-lm`.** Le funzioni di `math.h` stanno in un file separato dal resto della libreria, e bisogna chiedere esplicitamente di aggiungerlo al programma con il flag `-lm`, scritto in fondo al comando:

```bash
gcc -g -Wall -Wextra -o radice radice.c -lm
```

**Il formattatore `%g`.** Stampa un `double` nella forma piu' compatta, passando alla notazione scientifica quando il numero e' molto grande o molto piccolo: `2.22045e-16` significa $2.22045 \cdot 10^{-16}$.

### Esercizi (O1-O10)

#### math.h

**O1.** In D45 avete calcolato la radice quadrata con il metodo di Erone. Scrivete un programma che legge un numero positivo `a` e ne calcola la radice in due modi: con il metodo di Erone, esattamente come in D45 (stessa condizione di arresto, ma usando `fabs` per il valore assoluto), e con la funzione `sqrt` di `math.h`. Il programma stampa entrambi i risultati con $17$ decimali e il numero di passi del metodo di Erone.

```text
Inserisci un numero positivo: 2
Erone (4 passi): 1.41421356237468987
sqrt:            1.41421356237309515
```

1. Compilate senza `-lm`: che cosa risponde gcc? In quale delle fasi di B10 nasce l'errore? (Alcune funzioni semplici, come `fabs`, gcc le traduce da solo e funzionano anche senza `-lm`: non fidatevi, e aggiungete sempre `-lm` quando usate `math.h`.)
2. Fino a quale cifra decimale i due risultati coincidono con $a = 2$? E con $a = 10$? Provate con $a = 0.01$: perche' qui il metodo di Erone sbaglia gia' alla settima cifra decimale? Suggerimento: rileggete la condizione di arresto, pensando a quanto vale $x^2$.
3. **Con time.** Scrivete un programma che somma le radici quadrate dei numeri interi da $1$ a $10000000$, in quest'ordine, e stampa la somma con `%.6f`, in due versioni: una con `sqrt`, che deve stampare `21081852648.716972`, e una che calcola ogni radice con il ciclo di Erone. Misurate i tempi delle due versioni.
4. **In piu'.** Togliete `-lm` e scrivete `sqrt(2.0)`, con un numero al posto di una variabile: ora il programma compila. Che cosa avra' fatto gcc? Ripensate a G8.

**O2.** Arrotondare un numero reale a un intero si puo' fare in molti modi, e per i numeri negativi i modi danno risultati diversi. Completate la tabella su carta, poi scrivete un programma che la stampa e controllate. `trunc` toglie la parte decimale, `floor` arrotonda all'intero inferiore, `ceil` all'intero superiore, `round` all'intero piu' vicino (e, a meta' strada, lontano dallo zero). Le funzioni restituiscono un `double`: stampatele con `%.0f`.

| `x` | `(int) x` | `trunc(x)` | `floor(x)` | `ceil(x)` | `round(x)` |
| --- | --- | --- | --- | --- | --- |
| $2.3$ |  |  |  |  |  |
| $2.5$ |  |  |  |  |  |
| $2.7$ |  |  |  |  |  |
| $-2.3$ |  |  |  |  |  |
| $-2.5$ |  |  |  |  |  |
| $-2.7$ |  |  |  |  |  |

1. Quali colonne coincidono sempre? Quali sono uguali per i numeri positivi, ma non per i negativi?
2. In C, `-7 / 2` vale $-3$: quale delle funzioni della tabella si comporta come la divisione tra interi? Quale funzione, applicata a `-7 / 2.0`, da' invece $-4$, cioe' il quoziente della divisione con resto che si usa in matematica?
3. Stampate $0.5$, $1.5$, $2.5$ e $3.5$ con `%.0f`: `printf` non arrotonda come `round`. Quale regola segue?
4. Rivedete M10: con l'importo $8.20$, la riga `centesimi = euro * 100;` produceva $819$ centesimi. Riscrivetela con `round` e spiegate perche' ora funziona.

**O3.** `pow(x, y)` calcola $x^y$ e restituisce un `double`. Il programma confronta le potenze di $3$ calcolate con un ciclo, in un `long`, con quelle calcolate da `pow`, e stampa le righe da $3^{30}$ in poi, segnalando quelle diverse.

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    long p;
    int k;
    p = 1;
    for (k = 0; k <= 39; k++) {
        if (p != (long) pow(3, k)) {
            printf("3^%d: ciclo %ld, pow %.0f  <-- diversi\n", k, p, pow(3, k));
        } else if (k >= 30) {
            printf("3^%d: ciclo %ld, pow %.0f\n", k, p, pow(3, k));
        }
        p = p * 3;
    }
    return 0;
}
```

Il cast `(long)` trasforma il risultato di `pow` in un intero, cosi' il confronto avviene tra due `long`.

1. Da quale esponente i due risultati sono diversi? Quale dei due e' giusto? Un `double` conserva le cifre del numero in $53$ cifre binarie (la costante `DBL_MANT_DIG` di `float.h` vale $53$): quanto vale $2^{53}$, e che cosa c'entra?
2. Aggiungete la riga `printf("%d\n", pow(2, 10));`: che cosa dice `-Wall`? Che cosa stampa? Correggete la riga in due modi diversi.
3. Se il ciclo e' piu' preciso, a che cosa serve `pow`? Provate `pow(2, 0.5)` e `pow(8, 1.0 / 3)`.
4. **Con time.** Riprendete la somma di E13, $\frac{1}{1^2} + \dots + \frac{1}{N^2}$, con $N = 100000000$ e la variabile `x` che vale `1.0 / k`. Calcolate ogni termine una volta con `x * x` e una volta con `pow(x, 2)`, compilando senza ottimizzazioni e con `-O2`. Completate la tabella: perche' con `-O2` le due versioni sono ugualmente veloci?

| | `x * x` | `pow(x, 2)` |
| --- | --- | --- |
| Senza ottimizzazioni |  |  |
| Con `-O2` |  |  |

#### float.h, stdlib.h, ctype.h e time.h

**O4.** L'*epsilon di macchina* e' la distanza tra $1$ e il piu' piccolo `double` maggiore di $1$: misura la precisione dei numeri reali del computer. Il programma lo trova provando le potenze di $2$: parte da $\varepsilon = 1$ e lo dimezza finche' $1 + \frac{\varepsilon}{2}$ e' ancora diverso da $1$. Poi lo confronta con la costante `DBL_EPSILON` di `float.h`.

```c
#include <stdio.h>
#include <float.h>

int main(void) {
    double eps;
    int dimezzamenti;
    eps = 1;
    dimezzamenti = 0;
    while (1 + eps / 2 > 1) {
        eps = eps / 2;
        dimezzamenti++;
    }
    printf("Epsilon calcolato: %g (dopo %d dimezzamenti)\n", eps, dimezzamenti);
    printf("DBL_EPSILON:       %g\n", DBL_EPSILON);
    return 0;
}
```

1. Quanti dimezzamenti servono? Che relazione c'e' con le $53$ cifre binarie di O3?
2. Ripetete il calcolo con una variabile `float epsf` e la condizione `(float) (1 + epsf / 2) > 1`, e confrontate con `FLT_EPSILON`. Che cosa c'entra con le circa $6$ cifre significative dei `float` e le circa $15$ dei `double` (tabella del Pacchetto F, e la costante `DBL_DIG`)?
3. Aggiungete al programma `double grande = DBL_MAX * 2;`, poi `double strano = grande - grande;`, e stampateli con `%f`: che cosa ottenete? Provate anche `sqrt(-1)` (serve `math.h`, e quindi `-lm`). Le funzioni `isinf` e `isnan` di `math.h` riconoscono questi valori: perche' servono, se basterebbe confrontare con `==`? Provate `strano == strano`.
4. In M8 due numeri reali erano considerati uguali se la loro differenza, in valore assoluto, era minore di `EPS`, che valeva $10^{-9}$. Con questa regola, $10^{-12}$ e $2 \cdot 10^{-12}$ sono uguali? E con la *tolleranza relativa* `fabs(a - b) <= 4 * DBL_EPSILON * fabs(b)`, che confronta la differenza con la grandezza dei numeri? Controllate che con la tolleranza relativa $0.1 + 0.2$ e $0.3$ risultino uguali.
5. **Con gdb.** Fermatevi dopo il calcolo di `strano` e provate `print DBL_EPSILON`: perche' gdb non lo conosce? (Rivedete E7.) Che cosa rispondono `print eps`, `print grande` e `print strano == strano`?

**O5.** Il metodo Monte Carlo stima $\pi$ con il caso: si scelgono punti a caso nel quadrato di lato $1$ e si conta quanti cadono dentro il quarto di cerchio di raggio $1$, cioe' hanno $x^2 + y^2 < 1$. Il rapporto tra i punti dentro e i punti totali si avvicina al rapporto tra le aree, $\frac{\pi}{4}$.

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    long n, i, dentro;
    double x, y, stima;
    srand(1);
    for (n = 1000; n <= 10000000; n *= 10) {
        dentro = 0;
        for (i = 0; i < n; i++) {
            x = rand() / (RAND_MAX + 1.0);
            y = rand() / (RAND_MAX + 1.0);
            if (x * x + y * y < 1) {
                dentro++;
            }
        }
        stima = 4.0 * dentro / n;
        printf("%9ld punti: pi circa %.6f, errore %.6f\n", n, stima, fabs(stima - M_PI));
    }
    return 0;
}
```

```text
     1000 punti: pi circa 3.132000, errore 0.009593
    10000 punti: pi circa 3.166400, errore 0.024807
   100000 punti: pi circa 3.138800, errore 0.002793
  1000000 punti: pi circa 3.141924, errore 0.000331
 10000000 punti: pi circa 3.140901, errore 0.000691
```

`M_PI` e' il valore di $\pi$ definito in `math.h`.

1. Perche' `rand() / (RAND_MAX + 1.0)` e' un numero reale tra $0$ (compreso) e $1$ (escluso)? Che cosa succederebbe scrivendo `rand() / (RAND_MAX + 1)`? Suggerimento: su Linux `RAND_MAX` e' uguale a `INT_MAX`.
2. Perche' $4 \cdot \frac{\text{dentro}}{n}$ si avvicina a $\pi$?
3. L'errore non diminuisce sempre: con $10000$ punti e' piu' grande che con $1000$. Perche' non e' strano? Provate con `srand(2)` e `srand(3)`. In media, quante volte bisogna aumentare i punti perche' l'errore diventi $10$ volte piu' piccolo? (Si dimostra che l'errore e' circa proporzionale a $\frac{1}{\sqrt{n}}$.)
4. **Con time.** Quanto impiega il programma? E' un buon modo per calcolare $\pi$?

**O6.** La libreria `ctype.h` contiene funzioni che riconoscono il tipo di un carattere: `isalpha` (lettera), `isupper` e `islower` (lettera maiuscola o minuscola), `isdigit` (cifra), `isspace` (spazio, tabulazione, a capo e simili), `ispunct` (punteggiatura). Restituiscono un valore diverso da $0$ (vero) oppure $0$ (falso). Ci sono anche `toupper` e `tolower`, che trasformano una lettera in maiuscola o in minuscola e lasciano invariati gli altri caratteri. Scrivete un programma che legge una frase un carattere alla volta con `scanf("%c", &c)`, fino all'a capo (come in N8), e la salva in un array `char testo[MAX]` (con `#define MAX 200`). Poi stampa quanti caratteri, lettere (e di queste quante maiuscole), cifre, spazi e segni di punteggiatura contiene, e la frase tutta in maiuscolo. Scrivete frasi senza lettere accentate: ciascuna di esse occupa piu' di un `char`, e per ora non le tratteremo.

```text
Scrivi una frase: Il 3 ottobre 2026, ore 14:30!
Caratteri: 29
Lettere: 12 (maiuscole: 1)
Cifre: 9
Spazi: 5
Punteggiatura: 3
In maiuscolo: IL 3 OTTOBRE 2026, ORE 14:30!
```

1. Come avreste scritto, senza `ctype.h`, il controllo "e' una lettera"? E la trasformazione in maiuscolo (F1)? Perche' le funzioni della libreria sono piu' comode e piu' sicure?
2. Riscrivete il programma di N18 (ISBN) sostituendo la macro `E_CIFRA` con `isdigit`. La macro `VALORE` serve ancora?
3. Riprendete il cifrario di Cesare di F8 e fate in modo che sposti sia le lettere minuscole sia le maiuscole, lasciandole tali, e copi invariati tutti gli altri caratteri. Usate `islower` e `isupper`.

**O7.** `time` misura l'intero programma, gprof dice quanto pesa ogni riga. Per misurare il tempo di una parte del programma, e stamparlo, c'e' la funzione `clock` di `time.h`: restituisce il tempo di processore usato fino a quel momento, cioe' il tempo `user` (piu' una piccola parte di `sys`), in unita' che diventano secondi dividendo per la costante `CLOCKS_PER_SEC`.

```c
clock_t inizio;          /* clock_t e' un tipo intero adatto a contenere i tempi */
double secondi;

inizio = clock();
/* ... la parte da misurare ... */
secondi = (double) (clock() - inizio) / CLOCKS_PER_SEC;
printf("Tempo: %.3f secondi\n", secondi);
```

Riprendete G10 e mettete le due ricerche nello stesso programma: prima generate le `Q` ricerche in un array `x`, poi le eseguite con la ricerca lineare e poi con quella binaria, misurando ciascuna fase con `clock`. Le due fasi devono trovare gli stessi numeri.

```text
Ricerca lineare: trovati 5087, 0.940 secondi
Ricerca binaria: trovati 5087, 0.002 secondi
```

1. **Con time.** Lanciate il programma con `time`: la somma dei tempi stampati e' vicina a `user`? E a `real`?
2. **Con gprof.** Il resoconto per righe da' la stessa indicazione di `clock`? Che cosa offre in piu' gprof, e che cosa `clock`?
3. `time(NULL)`, che avete usato in G2, restituisce i secondi trascorsi dal 1 gennaio 1970. Perche' non va bene per misurare queste due fasi?

**O8.** Due errori, entrambi progettuali, e uno solo lo segnala `-Wextra`. Il programma calcola media, deviazione standard e scarto massimo dalla media di cinque misure: deve stampare `Media: 0.600`, `Deviazione standard: 2.326` e `Scarto massimo dalla media: 3.800`, invece le ultime due righe sono `Deviazione standard: 1.000` e `Scarto massimo dalla media: 3.000`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 5

int main(void) {
    double x[N] = {4.4, 0.5, -2.7, 1.3, -0.5};
    double media, varianza, scarto, scarto_max;
    int i;
    media = 0;
    for (i = 0; i < N; i++) {
        media += x[i];
    }
    media /= N;
    varianza = 0;
    scarto_max = 0;
    for (i = 0; i < N; i++) {
        varianza += pow(x[i] - media, 2);
        scarto = abs(x[i] - media);
        if (scarto > scarto_max) {
            scarto_max = scarto;
        }
    }
    varianza /= N;
    printf("Media: %.3f\n", media);
    printf("Deviazione standard: %.3f\n", pow(varianza, 1 / 2));
    printf("Scarto massimo dalla media: %.3f\n", scarto_max);
    return 0;
}
```

**Con gdb.** Mettete un breakpoint sulla riga `scarto = abs(x[i] - media);`, e a ogni fermata date `print x[i] - media`, poi `next` e `print scarto`. Per l'altro errore, provate `print 1 / 2`. Correggete il programma: perche' `pow(varianza, 0.5)` funziona, e quale funzione di `math.h` e' ancora piu' chiara?

**O9.** Le coordinate polari di un punto $(x, y)$ sono la distanza $r$ dall'origine e l'angolo $\theta$ con il semiasse positivo delle $x$. La distanza e' $\sqrt{x^2 + y^2}$; per l'angolo, dato che $\tan \theta = \frac{y}{x}$, viene spontaneo usare `atan(y / x)`. La libreria offre pero' anche `atan2(y, x)`, che riceve separatamente le due coordinate. Scrivete un programma che legge $x$ e $y$ e stampa $r$ e l'angolo in gradi calcolato nei due modi (le funzioni restituiscono radianti: moltiplicate per `180 / M_PI`).

```text
Coordinate del punto: -1 1
r = 1.414214
Angolo con atan2: 135.000000 gradi
Angolo con atan:  -45.000000 gradi
```

1. Completate la tabella. In quali quadranti `atan(y / x)` sbaglia, e di quanto? (Ripensate a E4.)

| Punto | $(1, 1)$ | $(-1, 1)$ | $(-1, -1)$ | $(1, -1)$ | $(0, 2)$ | $(-2, 0)$ |
| --- | --- | --- | --- | --- | --- | --- |
| `atan2` |  |  |  |  |  |  |
| `atan` |  |  |  |  |  |  |

2. Con il punto $(0, 2)$, `y / x` e' una divisione per zero: perche' `atan` da' comunque il risultato giusto? (Rivedete E13 e O4.)
3. `atan2` restituisce angoli tra $-180$ e $180$ gradi. Modificate il programma perche' stampi l'angolo tra $0$ (compreso) e $360$ (escluso).
4. Per la distanza, `math.h` offre anche `hypot(x, y)`. Provate $x = y = 10^{200}$ con `sqrt(x * x + y * y)` e con `hypot(x, y)`: che cosa succede? (Rivedete O4.)

**O10.** **Sfida.** La "curva a campana" di Gauss descrive moltissimi fenomeni: le altezze delle persone, gli errori di misura, i voti di un esame molto numeroso. Il metodo di Box e Muller (1958) produce numeri casuali distribuiti secondo questa curva, con media $0$ e deviazione standard $1$, a partire da due numeri casuali $u_1$ e $u_2$ compresi tra $0$ e $1$:

$$z = \sqrt{-2 \ln u_1} \cdot \cos(2 \pi u_2)$$

Per questa curva vale la *regola del 68-95-99,7*: circa il $68.3\%$ dei numeri si trova entro una deviazione standard dalla media, il $95.4\%$ entro due e il $99.7\%$ entro tre. Requisiti:

- `N` numeri (con `#define N 100000`) in un array `double z[N]` dichiarato prima di `main` (H6), generati dopo `srand(1)`; $u_1$ e $u_2$ si calcolano entrambi, in quest'ordine, con `(rand() + 1.0) / (RAND_MAX + 1.0)`, che non vale mai $0$; il logaritmo naturale e' `log`;
- media e deviazione standard del campione, come in O8 ma senza errori;
- le percentuali di numeri che distano dalla media del campione al massimo $1$, $2$ e $3$ volte la deviazione standard del campione;
- un istogramma: $12$ classi di larghezza $0.5$, da $-3$ a $3$ (la classe di un numero e' `floor((z[i] + 3) / 0.5)`, e i numeri fuori da $[-3, 3)$ non si contano); ogni riga inizia con gli estremi della classe, stampati con `printf("%5.1f %5.1f |", ...)`, ed e' seguita da tanti asterischi quanti sono i numeri della classe diviso $400$, con la divisione tra interi.

```text
Media: -0.0033
Deviazione standard: 0.9998
Entro 1 deviazione standard: 68.08%
Entro 2 deviazioni standard: 95.46%
Entro 3 deviazioni standard: 99.72%
 -3.0  -2.5 |*
 -2.5  -2.0 |****
 -2.0  -1.5 |***********
 -1.5  -1.0 |***********************
 -1.0  -0.5 |*************************************
 -0.5   0.0 |************************************************
  0.0   0.5 |***********************************************
  0.5   1.0 |*************************************
  1.0   1.5 |***********************
  1.5   2.0 |**********
  2.0   2.5 |****
  2.5   3.0 |*
```

1. Perche' $u_1$ non deve mai valere $0$? Che cosa restituirebbe `log(0)`?
2. Le percentuali del campione sono vicine a quelle della regola? Provate con `N` uguale a $1000$ e a $1000000$.
3. Che cosa cambia se, al posto di `z[i]`, usate `10 * z[i] + 25`? Calcolate di nuovo media e deviazione standard: che cosa notate?


## Pacchetto P: struct, typedef e union

Fino a qui i dati sono stati variabili singole, oppure array di valori tutti dello stesso tipo. Molte cose, pero', sono fatte di pezzi diversi che vanno sempre insieme: un punto del piano e' due interi, una misura e' un'ora e un valore, una frazione e' un numeratore e un denominatore. Tenerli in variabili separate funziona finche' non si prova a passarli a una funzione, o a farseli restituire: li' si scopre che in C una funzione restituisce **un** valore, e che due numeri che devono tornare insieme non tornano affatto.

Le **strutture** risolvono proprio questo: raggruppano piu' valori, anche di tipo diverso, in una variabile sola, che si dichiara, si copia, si passa a una funzione e si fa restituire da una funzione esattamente come un `int`. Le **union** sono la loro sorella meno usata e piu' curiosa: tengono un valore per volta nello stesso spazio. Nel mezzo c'e' `typedef`, che serve a dare ai tipi un nome corto.

Gli esercizi di questo pacchetto rifanno in buona parte problemi che avete gia' risolto negli eserciziari precedenti: e' il modo piu' rapido per vedere che cosa si guadagna. Compilate sempre con `gcc -g -Wall -Wextra`; in P5 servira' anche `-lm`, per `math.h`, e in P20 il comando `time`. Come nei pacchetti precedenti, gdb vi accompagna quando serve a vedere cio' che l'output non mostra, e le domande che lo usano iniziano con **Con gdb.**: con le struct e' particolarmente utile, perche' gdb le stampa tutte insieme. Un'ultima avvertenza pratica: `sizeof` non restituisce un `int`, quindi per stamparlo con `%d` va scritto `(int) sizeof(...)`, come avete fatto in I7.

### Le strutture

```c
struct punto {
    int x;
    int y;
};                            /* attenzione al ; dopo la graffa chiusa */

struct punto p = {3, 4};      /* i valori nell'ordine in cui sono scritti i campi */
struct punto q;

q.x = -1;
q.y = 0;
printf("(%d, %d)\n", p.x, p.y);
scanf("%d", &q.x);            /* la & sta davanti al campo, non davanti a q */
```

- `struct punto { ... };` non dichiara una variabile: descrive un **tipo** nuovo. Va scritta prima delle funzioni che la usano, come i prototipi.
- Il nome del tipo e' `struct punto`, due parole: la parola `struct` fa parte del nome e non si puo' omettere. Per scriverne una sola c'e' `typedef`, qui sotto.
- Ogni campo, `p.x`, e' una variabile come tutte le altre: si legge, le si assegna, si passa a `printf` e a `scanf`.
- Si inizializza alla dichiarazione, `{3, 4}`, ma non dopo: `p = {3, 4};` non compila.
- **Si copia tutta insieme**: `q = p;` copia ogni campo. Con gli array questo non si puo' fare.
- **Non si confronta**: `p == q` non compila. Il confronto va scritto a mano, campo per campo (P2).

### typedef

```c
typedef struct {
    int x;
    int y;
} Punto;

Punto p = {3, 4};
```

`typedef` da' un nome nuovo a un tipo che esiste gia': da quel momento `Punto` vale esattamente quanto `struct punto`, e la parola `struct` sparisce dal resto del programma. Per convenzione il nome del tipo si scrive con l'iniziale maiuscola, cosi' si distingue a colpo d'occhio dalle variabili.

`typedef` funziona anche sui tipi di base (`typedef double Celsius;`) e sulle enumerazioni del Pacchetto N (`typedef enum {CUORI, QUADRI, FIORI, PICCHE} Seme;`). Attenzione pero': e' un soprannome, non un tipo nuovo, e il compilatore continua a vedere quello che c'e' sotto (P8).

Nei primi sei esercizi scriveremo `struct punto` per esteso, per prenderci la mano; dal P7 in poi useremo i `typedef`, tranne negli esercizi sulle union, dove tenere la parola `union` sotto gli occhi aiuta a ricordare di che cosa si sta parlando.

### Le struct e le funzioni

```c
int distanza2(struct punto a, struct punto b) {     /* riceve due copie */
    return (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y);
}

struct punto meta(struct punto a, struct punto b) { /* restituisce una struct */
    struct punto m;
    m.x = (a.x + b.x) / 2;
    m.y = (a.y + b.y) / 2;
    return m;
}
```

- Una struct passata a una funzione viene **copiata**, come un `int` e al contrario di un array (I7, I12): se la funzione la modifica, il chiamante non se ne accorge.
- Una funzione puo' **restituire** una struct, e questo e' il motivo principale per cui ci servono: e' il modo di far tornare indietro piu' valori insieme. `struct punto m = meta(a, b);` funziona come un qualsiasi assegnamento.
- Un **array di struct** si passa come un array qualunque, `struct punto v[]`, e come tutti gli array **non** viene copiato.

### Le union

```c
union numero {
    int i;
    double d;
};

union numero n;
n.i = 5;        /* adesso n contiene un int */
n.d = 2.5;      /* adesso contiene un double, e il 5 non c'e' piu' */
```

La sintassi e' identica a quella delle struct, punto compreso, ma il significato e' un altro: in una `struct` i campi stanno **uno accanto all'altro** e ci sono tutti insieme, in una `union` stanno **nello stesso posto** e ce n'e' uno solo per volta. Scrivere in un campo cancella gli altri.

Ne segue che una union occupa quanto il suo campo piu' grande, mentre una struct occupa almeno quanto la somma. Attenzione: come per le struct (P6), la dimensione viene poi arrotondata in su, perche' in un array anche l'elemento successivo cada a un indirizzo buono; una union che contiene un `double` occupa sempre un multiplo di $8$, anche quando il campo piu' grande e' piu' corto. E ne segue anche il rischio: leggere un campo diverso dall'ultimo scritto non e' un errore per il compilatore, ma il valore non significa niente. Ricordarsi quale campo e' valido tocca a chi scrive il programma, di solito con un `enum` accanto (P12).

### Esercizi (P1-P20)

#### Le prime struct

**P1.** Riprendete I19, i punti dentro un cerchio, e riscrivetelo con `struct punto {int x; int y;};` e la funzione `int distanza2(struct punto a, struct punto b)`. Il programma legge centro e raggio, poi `n` punti, e conta quanti stanno dentro o sul bordo; alla fine stampa anche il punto medio tra il primo e l'ultimo punto letto, calcolato da `struct punto meta(struct punto a, struct punto b)` con la divisione tra interi.

```text
Centro e raggio: 0 0 5
Quanti punti? 4
0 0
3 4
5 1
-2 -2
Dentro o sul bordo: 3
Punto medio tra il primo e l'ultimo: (-1, -1)
```

1. In I19 `distanza2` aveva quattro parametri, qui ne ha due. Elencate le variabili di tipo `struct punto` che servono nel `main` e dite a che cosa serve ciascuna: attenzione, per il punto medio bisogna ricordare anche il primo e l'ultimo punto letto.
2. Nella `scanf` si scrive `&p.x` e non `&p`. Rileggete la riga come la legge il compilatore: il punto si applica prima della `&`, quindi si sta passando l'indirizzo del campo. Che cosa succede se provate `scanf("%d %d", &p)`? gcc vi avverte (`expects argument of type 'int *', but argument 2 has type 'struct punto *'`) e il programma quasi sempre muore con `Segmentation fault`.
3. `meta` restituisce una struct, cioe' due numeri in una volta. Nei facili non si poteva fare: come avreste restituito due interi da una funzione, con quello che sapevate alla fine del Pacchetto J?
4. Spostate la dichiarazione `struct punto {...};` dentro `main`. gcc si arrabbia parecchio: un avviso `declared inside parameter list will not be visible outside of this definition or declaration` e, a seconda di dove ha guardato, un errore `parameter 1 ('a') has incomplete type` dove la funzione e' definita oppure `type of formal parameter 1 is incomplete` dove viene chiamata. Perche'? Dove va dichiarata una struct che serve anche alle funzioni?

**P2.** Copiare si', confrontare no.

```c
#include <stdio.h>

struct punto {
    int x;
    int y;
};

int main(void) {
    struct punto a = {3, 4};
    struct punto b = {-1, 0};
    struct punto t;
    printf("a = (%d, %d), b = (%d, %d)\n", a.x, a.y, b.x, b.y);
    t = a;
    a = b;
    b = t;
    printf("dopo lo scambio: a = (%d, %d), b = (%d, %d)\n", a.x, a.y, b.x, b.y);
    return 0;
}
```

```text
a = (3, 4), b = (-1, 0)
dopo lo scambio: a = (-1, 0), b = (3, 4)
```

1. Lo scambio e' quello di C13, in tre righe, ma qui ogni riga sposta due interi insieme. Provate a fare lo stesso con due array, `int v[2]` e `int w[2]`: la riga `t = v;` non compila, e gcc dice `assignment to expression with array type`. Scrivete quante righe servirebbero per scambiare due array di due elementi.
2. Aggiungete `if (a == b) { printf("uguali\n"); }`: gcc rifiuta con `invalid operands to binary ==`. Quindi il C copia volentieri una struct ma non la confronta.
3. Scrivete `int uguali(struct punto a, struct punto b)`, che restituisce $1$ se i due punti coincidono e $0$ altrimenti, e documentatela con Doxygen (I8). Provatela su due punti uguali e due diversi.
4. **Con gdb.** Mettete un breakpoint sulla riga `t = a;` e date `print a`: gdb risponde `$1 = {x = 3, y = 4}`, cioe' stampa la struct tutta insieme, esattamente come il C la copia. Provate anche `print sizeof(struct punto)` e `print a.x`.
5. **In piu'.** Perche' il C copia le struct ma non le confronta? Il motivo si capisce in P6: tra un campo e l'altro ci possono essere byte di riempimento, che la copia porta con se' ma che non contengono niente di significativo. Due struct con gli stessi campi potrebbero avere riempimenti diversi: un confronto byte per byte direbbe "diverse" anche quando i campi coincidono.

**P3.** Le frazioni sono l'esempio perfetto di due numeri che non hanno senso da soli. Scrivete `frazioni.c` con `struct frazione {int num; int den;};` e quattro funzioni:

- `int mcd(int a, int b)`, l'algoritmo di Euclide di I16;
- `struct frazione riduci(struct frazione f)`, che riduce ai minimi termini e porta il segno al numeratore;
- `struct frazione somma(struct frazione a, struct frazione b)`;
- `struct frazione prodotto(struct frazione a, struct frazione b)`.

Il programma legge due frazioni e stampa la prima ridotta, la somma e il prodotto, gia' ridotti.

```text
Prima frazione (num den): 84 126
Seconda frazione (num den): 5 9
84/126 ridotta = 2/3
Somma: 11/9
Prodotto: 10/27
```

1. **Il punto di tutto il pacchetto.** `somma` deve far tornare al `main` due numeri. Senza struct, con quello che sapevate alla fine dei facili, come ve la sareste cavata? Elencate i modi possibili e dite perche' nessuno e' comodo.
2. `riduci` va chiamata dentro `somma` e `prodotto`, oppure dal `main` subito dopo? Funzionano tutte e due: quello che non funziona e' non ridurre affatto, e si vede subito con $\frac{1}{2} + \frac{1}{2}$, che senza riduzione stampa `4/4` invece di `1/1`. Quale delle due scelte vi risparmia righe se domani aggiungete anche `differenza` e `quoziente`?
3. `mcd` puo' restituire un numero negativo: `mcd(-3, -6)` vale $-3$. Verificatelo, e sistemate `riduci` perche' funzioni anche con numeri negativi. Con $\frac{3}{-6}$ in ingresso deve stampare `-1/2`, non `1/-2`: serve una riga che, se il denominatore e' negativo, cambi segno a tutti e due.
4. Il denominatore zero non ha senso. Aggiungete `assert(f.den != 0);` come prima riga di `riduci` (Pacchetto M) e scrivetelo anche nella documentazione, in un `@pre`. Provate a dare $\frac{1}{0}$: che cosa succede, e in quale momento?

**P4.** Riprendete G1, le temperature di una giornata. Li' la temperatura massima e l'ora in cui era stata misurata erano due variabili separate, da aggiornare insieme a ogni giro e facili da scordare. Adesso sono una cosa sola: `struct misura {int ora; double valore;};`. Il programma legge $24$ valori in `struct misura temp[ORE]` (con `#define ORE 24`), riempiendo `ora` con l'indice, e usa tre funzioni: `struct misura massima(struct misura v[], int n)`, `struct misura minima(...)` e `double media(...)`.

```text
Massima: 19.5 alle ore 14
Minima: 7.5 alle ore 5
Media: 12.92
```

A differenza di G1, questa volta il programma non stampa nessuna richiesta: legge i $24$ numeri e basta. Usate il file `temperature.txt` di G1 e lanciate il programma con `./misure < temperature.txt`.

1. In G1 c'era il rischio di aggiornare la massima e dimenticare l'ora. Qui quel rischio non c'e' piu': guardate la riga che aggiorna il massimo dentro la funzione e dite perche'.
2. Con questi dati la massima, $19.5$, compare alle ore $14$ e alle ore $15$. Quale confronto dentro `massima` fa restituire la prima? E quale farebbe restituire l'ultima?
3. L'array di struct si passa come un array qualunque e **non** viene copiato. Verificatelo: fate in modo che `massima` scriva `v[0].valore = -99;` prima di restituire, e stampate `temp[0].valore` nel `main`. Guardate anche le righe `Minima` e `Media`, che diventano `-99.0 alle ore 0` e `8.40`: perche' cambiano anche loro? Che cosa vi dice, questo, sull'ordine in cui il `main` chiama le tre funzioni? Poi togliete quella riga.
4. Stampate `(int) sizeof(struct misura)`, che vale $16$, e `sizeof(temp)`, che vale $384$. I campi sono un `int` di $4$ byte e un `double` di $8$: $16$ non e' la loro somma. Il perche' e' in P6. Intanto contate gli elementi dell'array con la macro `DIM` di N14.

**P5.** Perimetro e area di un poligono, con una struct dentro un'altra.

```c
struct punto {
    int x;
    int y;
};

struct segmento {
    struct punto a;
    struct punto b;
};
```

Il programma legge `n` vertici (da $3$ a $20$, controllati con un `do while`) in un array `struct punto v[MAX]` (con `#define MAX 20`) e calcola il perimetro, sommando `double lunghezza(struct segmento s)` su tutti i lati, e l'area con la formula del laccio di scarpa: l'area vale la meta' del valore assoluto di $\sum_i (x_i y_{i+1} - x_{i+1} y_i)$, dove dopo l'ultimo vertice si torna al primo. Servono `sqrt` e `fabs` di `math.h` (O1 e O2), quindi compilate con `-lm`.

```text
Quanti vertici (da 3 a 20)? 3
0 0
3 0
3 4
Perimetro: 12.0000
Area: 6.0000
```

1. `s.a.x` ha due punti di seguito: scrivete che cosa indica ciascuno dei tre nomi, partendo da sinistra.
2. L'ultimo lato va dall'ultimo vertice al primo. Come si scrive l'indice del vertice successivo, in un solo pezzo, senza un `if`? (E' lo stesso trucco della rotazione di G4.)
3. Provate con il quadrato di vertici $(0,0)$, $(2,0)$, $(2,2)$, $(0,2)$: perimetro $8$ e area $4$. Poi inserite gli stessi vertici in ordine inverso: il risultato non cambia. Togliete `fabs` e riprovate: adesso l'area del secondo e' negativa. Che cosa distingue i due casi?
4. `lunghezza` riceve un `struct segmento`, cioe' quattro interi copiati a ogni chiamata: `sizeof(struct segmento)` vale $16$. Per un poligono di $20$ lati, quanti byte vengono copiati in tutto? Sarebbe stato piu' economico passare due `struct punto` separati? E perche' per l'array di vertici il problema non si pone?

**P6.** Una struct occupa piu' spazio della somma dei suoi campi. Il programma lo mostra su tre struct con gli stessi campi.

```c
#include <stdio.h>

struct a        { char c1; int n; };
struct compatta { char c1; char c2; int n; };
struct sparsa   { char c1; int n; char c2; };
```

```text
struct {char; int}        campi 5 byte, sizeof 8
struct {char; char; int}  campi 6 byte, sizeof 8
struct {char; int; char}  campi 6 byte, sizeof 12
```

Il motivo viene da come e' fatto il calcolatore: il processore legge la memoria a blocchi, e un `int` di $4$ byte si legge in un colpo solo se il suo indirizzo e' un multiplo di $4$. Per ottenerlo il compilatore infila dei byte di riempimento, che non contengono niente e servono solo a far cadere i campi al posto giusto. Alla fine aggiunge il riempimento necessario perche' anche l'elemento successivo di un array cada bene.

1. Scrivete il programma che stampa quelle tre righe, usando `sizeof` sui tipi e la somma dei `sizeof` dei singoli campi.
2. `compatta` e `sparsa` hanno gli stessi identici campi, in ordine diverso, e occupano $8$ e $12$ byte. Dove stanno i byte di riempimento nelle due? Disegnate le due disposizioni su carta, una casella per byte.
3. In un array di un milione di elementi, quanti megabyte si risparmiano usando `compatta` invece di `sparsa`? Qual e' la regola pratica che se ne ricava, per l'ordine in cui scrivere i campi?
4. In P4 avevate trovato `sizeof(struct misura)` uguale a $16$, con un `int` di $4$ byte e un `double` di $8$. Dove sono i $4$ byte di troppo? Provate a invertire i due campi, mettendo prima il `double`: la dimensione resta $16$. Questa volta il riempimento non sta in mezzo ma in fondo, e serve perche' in un array anche il secondo elemento debba partire a un indirizzo multiplo di $8$, come vuole il suo `double`.
5. **Attenzione.** Questi numeri dipendono dal computer e dal compilatore: su un PC normale, x86-64 con gcc, escono proprio cosi'. Su un'altra macchina potrebbero essere diversi, e nessuno di questi valori va mai dato per scontato in un programma.

#### typedef

**P7.** Riscrivete il programma di P1 usando `typedef`, in modo che la parola `struct` non compaia piu' da nessuna parte dopo la dichiarazione del tipo.

```c
typedef struct {
    int x;
    int y;
} Punto;

int distanza2(Punto a, Punto b);
Punto meta(Punto a, Punto b);
```

1. Contate quante volte la parola `struct` compariva nella versione di P1 e quante ne restano adesso.
2. C'e' una seconda forma, che tiene anche il nome della struttura:

```c
struct punto {
    int x;
    int y;
};
typedef struct punto Punto;
```

Le due forme fanno la stessa cosa, e da qui in avanti `Punto` e `struct punto` sono intercambiabili. Nella prima forma il nome `punto` non esiste proprio: la struttura e' *anonima* e si puo' chiamare soltanto `Punto`. Provate a scrivere `struct punto p;` dopo la prima forma: gcc risponde `storage size of 'p' isn't known`.

3. La convenzione dell'iniziale maiuscola (`Punto p;`) non e' una regola del linguaggio, ma e' seguita quasi ovunque. Che cosa vi fa capire, a colpo d'occhio, in una riga come `Punto meta(Punto a, Punto b)`?
4. `typedef` si usa anche sulle enumerazioni del Pacchetto N: scrivete `typedef enum {ROSSO, VERDE, BLU} Colore;` e usatela per un campo `colore` dentro `Punto`. Un `enum` occupa quanto un `int`, cioe' $4$ byte: `sizeof(Punto)` passa quindi da $8$ a $12$. Verificatelo.

**P8.** `typedef` da' un nome, non un tipo. Questo programma lo dimostra, ed e' la cosa piu' importante da sapere su `typedef`.

```c
#include <stdio.h>

typedef double Celsius;
typedef double Fahrenheit;

Fahrenheit in_fahrenheit(Celsius c) {
    return c * 9 / 5 + 32;
}

int main(void) {
    Celsius c = 20;
    Fahrenheit f;
    f = in_fahrenheit(c);
    printf("%.2f C = %.2f F\n", c, f);
    printf("Adesso sbagliamo: %.2f C = %.2f F\n", f, in_fahrenheit(f));
    return 0;
}
```

```text
20.00 C = 68.00 F
Adesso sbagliamo: 68.00 C = 154.40 F
```

1. L'ultima riga passa dei gradi Fahrenheit a una funzione che vuole gradi Celsius. gcc non dice una parola, nemmeno con `-Wall -Wextra`: perche'?
2. Se non fa controllare niente al compilatore, a che cosa serve allora `typedef` su un tipo di base? Pensate a chi legge il prototipo `Fahrenheit in_fahrenheit(Celsius c);` senza avere il corpo sotto gli occhi, e confrontatelo con `double converti(double x);`.
3. Per avere un controllo vero serve un tipo davvero diverso, e una struct con un campo solo lo e':

```c
typedef struct { double gradi; } Celsius;
typedef struct { double gradi; } Fahrenheit;
```

Riscrivete il programma cosi'. Adesso la riga sbagliata non compila: gcc risponde `incompatible type for argument 1 of 'in_fahrenheit'` e aggiunge `expected 'Celsius' but argument is of type 'Fahrenheit'`. Che cosa si e' pagato in cambio, in ogni riga che usa un valore?

4. **In piu'.** Con la versione a struct, provate anche `Celsius c; Fahrenheit f; c = f;`. Compila? E con la versione a `typedef double`?

**P9.** Un mazzo di carte mette insieme `typedef`, `enum` (Pacchetto N) e i numeri casuali con seme fisso (G2).

```c
#include <stdio.h>
#include <stdlib.h>
#define CARTE 52

typedef enum {CUORI, QUADRI, FIORI, PICCHE} Seme;

typedef struct {
    Seme seme;
    int valore;        /* da 1 a 13: 1 asso, 11 fante, 12 cavallo, 13 re */
} Carta;
```

Il programma costruisce il mazzo con due cicli annidati, quello esterno sui quattro semi e quello interno sui valori da $1$ a $13$, lo mescola con `srand(1)` e il metodo di Fisher e Yates (per `i` che va da `CARTE - 1` fino a $1$, si estrae `j = rand() % (i + 1)` e si scambiano `mazzo[i]` e `mazzo[j]`, con lo scambio in tre righe di P2), stampa le prime cinque carte con `void stampa_carta(Carta c)` e infine conta quante carte ci sono per ogni seme, in un array `int conta[4]`.

```text
Prime cinque carte:
9 di picche
6 di picche
8 di cuori
6 di quadri
7 di fiori
Carte per seme: 13 13 13 13
```

1. `stampa_carta` usa due `switch`: uno sul valore, per scrivere `Asso`, `Fante`, `Cavallo`, `Re` o il numero, e uno sul seme. Scrivete quello sul seme senza `default` e togliete poi il `case PICCHE`: `-Wall` risponde `enumeration value 'PICCHE' not handled in switch`. Perche' con un `#define` questo controllo non ci sarebbe?
2. Nell'array `conta` l'indice e' `mazzo[i].seme`, cioe' un `Seme` usato come intero. Funziona perche' un `enum` **e'** un intero: i quattro semi valgono $0$, $1$, $2$ e $3$. Che cosa succede, allora, se scrivete `c.seme = 7;`? Compila? Che cosa stampa lo `switch`, e che cosa succederebbe a `conta[7]`?
3. Lo scambio di due `Carta` si scrive in tre righe come in P2, non in sei: perche'?
4. **Con gdb.** Mettete `break stampa_carta`, lanciate il programma e date `print c`: gdb risponde `$1 = {seme = PICCHE, valore = 9}`. Due cose insieme: la struct viene stampata tutta, e il seme compare con il suo nome e non come $3$, perche' gli `enum` arrivano fino a gdb mentre i `#define` no (Pacchetto N).
5. Il controllo finale, $13$ carte per seme, e' una verifica che la mescolata non abbia perso o duplicato niente. Provate a sbagliare apposta la mescolata, scrivendo `j = rand() % CARTE` invece di `j = rand() % (i + 1)`: i conteggi restano $13$ lo stesso. Il controllo quindi non basta a dire che una mescolata e' giusta: che cosa controlla davvero?

#### union

**P10.** La prima union, messa accanto alla struct corrispondente.

```c
#include <stdio.h>

union numero {
    int i;
    double d;
};

struct coppia {
    int i;
    double d;
};

int main(void) {
    union numero n;
    struct coppia s;
    n.i = 5;
    printf("union:  dopo n.i = 5    n.i = %d\n", n.i);
    n.d = 2.5;
    printf("union:  dopo n.d = 2.5  n.d = %f\n", n.d);
    printf("union:                  n.i = %d\n", n.i);
    s.i = 5;
    s.d = 2.5;
    printf("struct: s.i = %d, s.d = %f\n", s.i, s.d);
    return 0;
}
```

```text
union:  dopo n.i = 5    n.i = 5
union:  dopo n.d = 2.5  n.d = 2.500000
union:                  n.i = 0
struct: s.i = 5, s.d = 2.500000
```

1. Che fine ha fatto il $5$ nella terza riga? Spiegate in una frase la differenza tra le prime tre righe e la quarta.
2. gcc non segnala niente. Confrontate con I15, dove a mentire era la documentazione: in quale dei due casi il compilatore *potrebbe* accorgersene, in linea di principio, e in quale no?
3. Provate ora il verso opposto: `n.d = 0;` e poi `n.i = 5;`, e stampate `n.d` con `%g`. Esce `2.47033e-323`, un numero piccolissimo. Non e' un errore del programma: `printf` sta leggendo come se fosse un `double` una sequenza di byte che e' stata scritta come un `int`.
4. Il $0$ della terza riga non e' casuale. Il `double` $2.5$ occupa $8$ byte, e l'`int` ne legge solo i primi $4$: in $2.5$ quei quattro byte valgono tutti zero. Provate con `n.d = 2.5000001`, che differisce da $2.5$ proprio in quei byte: `n.i` diventa $225179981$. (Questi due numeri dipendono dal modo in cui il computer scrive i `double` e dall'ordine in cui dispone i byte: il perche' e' in P14.)

**P11.** Quanto occupano. Scrivete `dimensioni.c` che dichiara

```c
union u  { int i; double d; char c; };
struct s { int i; double d; char c; };
```

e stampa la somma dei byte dei tre campi, `sizeof(union u)` e `sizeof(struct s)`.

```text
somma dei campi:          13 byte
union  {int;double;char}:  8 byte
struct {int;double;char}: 24 byte
```

1. La union occupa $8$ byte, meno della somma dei campi. Perche' $8$ e non $13$, e perche' proprio $8$?
2. La struct occupa $24$ byte, piu' della somma. Da dove vengono gli $11$ byte in piu'? (P6.)
3. In un array di un milione di elementi, quanti megabyte occupano l'una e l'altra?
4. Il risparmio e' reale solo a una condizione: quale? Scrivete in una riga in che situazione una union e' la scelta giusta, e in quale sarebbe un disastro.

**P12.** Ecco a che cosa serve davvero una union: tenere un valore che puo' essere di tipi diversi, con accanto un'etichetta che dice quale. E' la combinazione `enum` piu' `union`, e si chiama *record variante*.

```c
typedef enum {INTERO, REALE, CARATTERE} Tipo;

typedef struct {
    Tipo tipo;
    union {
        int i;
        double d;
        char c;
    } valore;
} Dato;
```

Il programma riempie un array `Dato v[4]` usando tre funzioni costruttrici, `Dato fai_intero(int i)`, `Dato fai_reale(double x)` e `Dato fai_carattere(char c)`, che restituiscono un `Dato` con etichetta e contenuto gia' d'accordo, e lo stampa con `void stampa(Dato d)`, che fa uno `switch` sull'etichetta.

```text
intero    42
reale     3.140000
carattere x
intero    -7
sizeof(Dato) = 16
```

1. `d.valore.i` ha due punti: il primo scende nella struct, il secondo nella union. Scrivete che cosa indica ciascuno dei tre nomi.
2. Togliete un `case` dallo `switch` di `stampa` e compilate: `-Wall` ve lo segnala come in P9. Perche' qui quel controllo e' particolarmente prezioso?
3. `sizeof(Dato)` vale $16$: da che cosa e' composto? Tenete conto che `Tipo` e' un intero di $4$ byte, che la union occupa $8$ (P11) e che vale quanto detto in P6.
4. Aggiungete un quarto tipo, `FRAZIONE`, che dentro la union contiene una `struct frazione` di P3. Una union puo' contenere una struct senza problemi. Quanto diventa `sizeof(Dato)`? Resta $16$: la frazione occupa $8$ byte, quanto il `double`, e la union non cresce. Provate invece con una struct di **tre** `int`, cioe' $12$ byte: adesso `sizeof(Dato)` diventa $24$. Perche' $24$ e non $20$? Rileggete l'ultima frase del riquadro sulle union.

**P13.** Il punto debole del record variante: niente obbliga l'etichetta a dire la verita'.

```c
Dato bugiardo = fai_reale(0.0);   /* etichetta REALE, contenuto 0.0 */
bugiardo.valore.i = 42;           /* adesso dentro c'e' un int, ma l'etichetta dice ancora REALE */
stampa(bugiardo);
```

```text
reale     0.000000
```

1. Il $42$ e' finito dentro la union, eppure la stampa non lo mostra e non mostra nemmeno qualcosa che gli somigli. Stampate lo stesso valore con `%g` invece di `%f`: esce `2.07508e-322`. Che cosa sta leggendo `printf`, e perche' il numero e' cosi' piccolo?
2. L'errore e' nato dall'aver scritto etichetta e contenuto in due momenti diversi. Le funzioni `fai_intero`, `fai_reale` e `fai_carattere` di P12 servono proprio a questo: con quelle, l'errore qui sopra si puo' ancora commettere, ma occorre farlo apposta. Riscrivete le tre righe usandole correttamente.
3. Aggiungete a `stampa` un `assert` che controlli che l'etichetta sia uno dei tre valori previsti. Che cosa **non** riesce a controllare, questo `assert`?
4. **Con gdb.** Mettete `break stampa`, lanciate il programma e, quando si ferma sul dato bugiardo, date `print d`. gdb risponde con una riga sola:

```text
$1 = {tipo = REALE, valore = {i = 42, d = 2.0750757125332355e-322, c = 42 '*'}}
```

e vi mostra i tre campi della union tutti insieme, cioe' i tre modi di leggere gli stessi otto byte. Quale dei tre e' quello giusto, e chi ve lo dice?
5. Nessun flag di gcc vi protegge da questo errore. Chi vi protegge, allora? Scrivete in due righe la regola di buona educazione che evita il problema: dove devono stare le righe che scrivono l'etichetta e quelle che scrivono il contenuto.

**P14.** Guardare un numero dall'interno. Una union con un `int` e un array di quattro `unsigned char` permette di vedere i singoli byte con cui l'`int` e' scritto in memoria. (`unsigned char` e' un `char` senza segno: invece di andare da $-128$ a $127$ va da $0$ a $255$, che e' proprio l'intervallo dei valori di un byte.)

```c
#include <stdio.h>

union vista {
    int i;
    unsigned char b[4];
};

void mostra(int n) {
    union vista v;
    int k;
    v.i = n;
    printf("%10d ->", n);
    for (k = 0; k < 4; k++) {
        printf(" %3d", v.b[k]);
    }
    printf("\n");
}
```

Il `main` stampa `sizeof(union vista)` e poi chiama `mostra` con $1$, $258$, $16909060$ e $-1$.

```text
sizeof(union vista) = 4
         1 ->   1   0   0   0
       258 ->   2   1   0   0
  16909060 ->   4   3   2   1
        -1 -> 255 255 255 255
```

1. $258 = 1 \cdot 256 + 2$. Nei byte compaiono infatti un $1$ e un $2$, ma nell'ordine opposto a quello in cui li scriveremmo: il byte meno significativo sta per primo. Questa disposizione si chiama *little-endian*.
2. $16909060$ in esadecimale si scrive `0x01020304`. Confrontate con la riga corrispondente: quale cifra esadecimale corrisponde a quale byte?
3. Perche' l'array e' di `unsigned char` e non di `char`? Provate a cambiarlo e guardate che cosa succede alla riga di $-1$.
4. L'ultima riga mostra come e' fatto $-1$: tutti i bit a uno. E' la rappresentazione in *complemento a due*, quella con cui il calcolatore scrive i numeri negativi. Quanto vale, con la stessa regola, il numero che ha i byte `255 255 255 127`?
5. **Attenzione.** L'ordine dei byte dipende dal processore. I PC x86-64 e i Mac con processore Apple sono little-endian e danno questo risultato; esistono macchine big-endian, dove $258$ darebbe `0 0 1 2`. Un programma che dipende da questo ordine non e' trasportabile.

#### Mettere insieme i pezzi

**P15.** Un registro di esami. Mette insieme `typedef`, `enum`, array di struct e funzioni che restituiscono struct.

```c
typedef enum {ANALISI, ALGEBRA, GEOMETRIA, FISICA} Corso;

typedef struct {
    int matricola;
    Corso corso;
    int voto;          /* da 18 a 30 */
    int lode;          /* 1 se con lode, 0 altrimenti */
} Esame;

Esame registro[] = {
    {1001, ANALISI,   28, 0},
    {1001, ALGEBRA,   30, 1},
    {1002, ANALISI,   24, 0},
    {1002, GEOMETRIA, 30, 0},
    {1003, FISICA,    18, 0},
    {1003, ANALISI,   27, 0},
    {1001, GEOMETRIA, 26, 0}
};
```

Scrivete le funzioni `void stampa(Esame e)`, che stampa un esame con uno `switch` sul corso, `double media(Esame v[], int n)`, `int conta_corso(Esame v[], int n, Corso c)`, `double media_corso(Esame v[], int n, Corso c)` e `Esame migliore(Esame v[], int n)`, che restituisce l'esame con il voto piu' alto; a parita' di voto vince quello con la lode, e a parita' di tutto il primo incontrato.

```text
Esami registrati: 7
Media: 26.14
Esami di Analisi: 3
Media di Analisi: 26.33
Migliore: matricola 1001, Algebra, 30 e lode
```

1. L'array e' dichiarato `Esame registro[] = {...};` senza dimensione, come in N14: la conta il compilatore. Ricavate `n` nel `main` con la macro `DIM` di N14.
2. `migliore` restituisce un `Esame` intero, non solo il voto. Che cosa riesce a stampare il `main` che non avrebbe potuto stampare se la funzione avesse restituito un `int`?
3. Aggiungete un corso all'`enum`, per esempio `PROBABILITA`, e non toccate lo `switch` di `stampa`: `-Wall` ve lo ricorda. Se invece i corsi fossero dei `#define`, chi se ne sarebbe accorto?
4. **In piu'.** Scrivete `int conta_studente(Esame v[], int n, int matricola)` e `double media_studente(...)`, e stampate la media della matricola $1001$. Poi provate a chiedere la media di una matricola che non esiste: che cosa succede, e come lo sistemate? (Un `assert` basta? E' il posto giusto?)

**P16.** I numeri complessi sono due `double` che vanno sempre insieme, e le operazioni su di loro restituiscono due numeri: e' il caso perfetto per una struct.

```c
typedef struct {
    double re;
    double im;
} Complesso;

Complesso somma(Complesso a, Complesso b);
Complesso prodotto(Complesso a, Complesso b);
double modulo2(Complesso z);
void stampa(Complesso z);
```

Il programma legge due numeri complessi (parte reale e immaginaria), stampa somma e prodotto, il modulo al quadrato del primo, e infine calcola $(1+i)^8$ con un ciclo che moltiplica otto volte.

```text
Primo numero (re im): 1 2
Secondo numero (re im): 3 -1
Somma: 4.00 + 1.00i
Prodotto: 5.00 + 5.00i
Modulo quadro del primo: 5.00
(1+i)^8 = 16.00 + 0.00i
```

1. `prodotto` calcola $ac - bd$ e $ad + bc$, cioe' quattro moltiplicazioni e due addizioni. Ne bastano tre, di moltiplicazioni: calcolate $t_1 = ac$, $t_2 = bd$ e $t_3 = (a+b)(c+d)$, e ricavate da questi tre numeri la parte reale e quella immaginaria del prodotto. (Verificate l'identita' a mano prima di scrivere il codice, poi controllate che il programma dia gli stessi risultati di prima.)
2. `stampa` deve scrivere `3.00 - 1.00i` e non `3.00 + -1.00i`. Scrivetela con un `if` sul segno della parte immaginaria, stampando in quel caso `-z.im`.
3. Il ciclo delle potenze e' `z = prodotto(z, uno_piu_i);`, dove `z` parte da $1 + 0i$. Il risultato di una funzione che restituisce una struct si assegna direttamente a una variabile: verificate a mano che $(1+i)^2 = 2i$ e $(1+i)^4 = -4$, e controllate che il programma dia $16$.
4. `modulo2` restituisce il quadrato del modulo, non il modulo: e' la stessa scelta di I19, e serve a evitare una radice quadrata. Quando serve il modulo vero c'e' `sqrt` di `math.h` (O1). In P20 vedrete un caso in cui il quadrato basta e avanza.

**P17.** Un polinomio e' un grado piu' un array di coefficienti. Metterli dentro una struct ha una conseguenza che vale la pena di vedere.

```c
#define GRADO_MAX 10

typedef struct {
    int grado;
    double c[GRADO_MAX + 1];    /* c[0] + c[1] x + c[2] x^2 + ... */
} Polinomio;
```

Scrivete `double valuta(Polinomio p, double x)` con il metodo di Horner (si parte da `r = 0` e, scendendo dal grado piu' alto al grado $0$, si fa `r = r * x + p.c[i]`), `Polinomio somma(Polinomio a, Polinomio b)` e `Polinomio derivata(Polinomio p)`. Il programma lavora su $p(x) = 2 - 3x + x^2$ e $q(x) = -1 + x$.

```text
p: grado 2, coefficienti 2.00 -3.00 1.00
q: grado 1, coefficienti -1.00 1.00
p(0) = 2.00, p(1) = 0.00, p(2) = 0.00, p(3) = 2.00
somma: grado 2, coefficienti 1.00 -2.00 1.00
derivata di p: grado 1, coefficienti -3.00 2.00
dopo r = p e r.c[0] = 100:  p.c[0] = 2.00, r.c[0] = 100.00
sizeof(Polinomio) = 96
```

1. **La riga importante e' la penultima.** `Polinomio r = p;` copia anche l'array `c`, tutti e undici i coefficienti. Un array nudo non si puo' copiare con `=` (lo avete visto in P2): messo dentro una struct, invece, si copia insieme a tutto il resto. Verificatelo modificando `r.c[0]` e stampando `p.c[0]`.
2. `sizeof(Polinomio)` vale $96$ byte, e ogni chiamata a `valuta` li copia tutti, anche se del polinomio di grado $2$ servono solo tre coefficienti. Quante volte viene copiata la struct nelle quattro chiamate della terza riga? E' un prezzo accettabile, qui?
3. Horner calcola $p(x)$ con $n$ moltiplicazioni e $n$ addizioni. Quante moltiplicazioni servirebbero calcolando ogni $c_i x^i$ separatamente, senza riusare le potenze gia' calcolate? Confrontate con il grado $10$.
4. $p(1) = 0$ e $p(2) = 0$: il polinomio e' $(x-1)(x-2)$. Verificatelo moltiplicando a mano.
5. **Con gdb.** Mettete `break valuta` e, alla prima fermata, date `print p`: gdb risponde

```text
$1 = {grado = 2, c = {2, -3, 1, 0, 0, 0, 0, 0, 0, 0, 0}}
```

cioe' stampa anche tutti e undici i coefficienti, compresi gli otto che non usate. E' la stessa cosa che viene copiata a ogni chiamata.
6. **In piu'.** La somma di due polinomi dello stesso grado puo' avere grado piu' basso: $x^2 + (5 - x^2) = 5$. La vostra `somma` deve accorgersene e correggere il campo `grado`, altrimenti il polinomio dice di avere grado $2$ con il coefficiente di $x^2$ uguale a zero. Aggiungete il ciclo che abbassa il grado finche' il coefficiente piu' alto e' zero, fermandosi comunque a grado $0$, e provate con quei due polinomi: deve stampare `grado 0, coefficienti 5.00`.

**P18.** Le date sono tre interi che da soli non significano niente.

```c
typedef struct {
    int g;
    int m;
    int a;
} Data;
```

Scrivete `int bisestile(int anno)`, `int giorni_del_mese(int mese, int anno)` (e' la funzione documentata in I1: adesso tocca a voi scriverla), `int giorno_dell_anno(Data d)`, `int confronta(Data a, Data b)` e `long giorni_totali(Data d)`, che conta i giorni dal $1$ gennaio dell'anno $1$. Il programma legge due date e dice quale viene prima e quanti giorni le separano.

```text
Prima data (g m a): 1 3 2024
Seconda data (g m a): 16 10 2026
Giorno dell'anno della prima: 61
La prima viene prima della seconda
Giorni di differenza: 959
```

1. `confronta` non restituisce $1$ o $0$ ma un numero **negativo** se la prima data viene prima, **zero** se coincidono e **positivo** se viene dopo: e' la convenzione dei confronti in C, e ritorna utile ogni volta che si vuole ordinare qualcosa. Perche' e' piu' informativa di una funzione che risponde solo si' o no? Scrivetela confrontando prima gli anni, poi i mesi, poi i giorni.
2. $61$ e' il giorno dell'anno del $1$ marzo $2024$: $31$ di gennaio piu' $29$ di febbraio piu' $1$. Controllate che il vostro programma risponda $60$ per il $1$ marzo $2025$, che non e' bisestile.
3. `giorni_totali` fa un ciclo su tutti gli anni dall'anno $1$: sono duemila giri per ogni chiamata. Funziona, ma e' uno spreco. Quante volte viene chiamata nel programma? Sapreste calcolare la differenza senza partire dall'anno $1$? (Suggerimento: contate gli anni interi tra le due date e trattate a parte il primo e l'ultimo.)
4. Aggiungete gli `assert` che controllano la validita' di una data: mese tra $1$ e $12$, giorno tra $1$ e `giorni_del_mese(d.m, d.a)`, anno positivo. Mettendoli dentro `giorno_dell_anno`, quali date finiscono per essere controllate? Guardate il vostro `giorni_totali`: chiama `giorno_dell_anno`? Se si', il controllo arriva a tutte e due le date; se avete contato i giorni in un altro modo, una delle due resta scoperta. Dove conviene allora mettere gli `assert`?
5. Il $1$ gennaio $2026$ e' un giovedi'. Sapendo questo, scrivete una funzione che dice il giorno della settimana di una data qualsiasi del $2026$, usando il resto della divisione per $7$. Verificate che il $16$ ottobre $2026$ sia un venerdi'.

**P19.** Quattro risultati in un colpo solo. In I10 servivano due funzioni e due passaggi sull'array per avere media e conteggio; qui una sola funzione restituisce quattro numeri.

```c
typedef struct {
    double media;
    double varianza;
    int minimo;
    int massimo;
} Statistiche;

Statistiche calcola(int v[], int n);
```

La varianza si calcola come media dei quadrati meno quadrato della media. Il programma legge $10$ numeri interi e stampa le quattro statistiche.

```text
Inserisci 10 numeri interi: 3 1 4 1 5 9 2 6 5 3
Media: 3.90
Varianza: 5.49
Minimo: 1
Massimo: 9
```

1. Quante volte `calcola` scorre l'array? Confrontate con I10, dove `media` e `conta_sopra` lo scorrevano una volta ciascuna.
2. L'array entra nella funzione senza essere copiato: di lui viaggia solo l'indicazione di dove si trova, che occupa $8$ byte (I7). La struct, invece, ne esce copiata, e `sizeof(Statistiche)` vale $24$. Quanti byte viaggiano allora in ciascuna direzione?
3. Provate ad aggiungere la mediana al risultato. Non ci riuscite in un solo passaggio: perche'? Che cosa servirebbe prima?
4. La formula "media dei quadrati meno quadrato della media" e' comoda ma fragile. Cambiate il programma perche' legga **tre** numeri e provate con $100000001$, $100000002$, $100000003$, la cui varianza vale esattamente $\frac{2}{3}$: la formula restituisce $0$. Attenzione a una trappola: la somma dei quadrati va accumulata scrivendo `somma2 += (double) v[i] * v[i];`, perche' senza la conversione la moltiplicazione avviene tra `int`, esce dall'intervallo e gcc non se ne accorge. Calcolatela allora come media di $(v_i - \text{media})^2$, in un secondo passaggio sull'array, e riprovate: adesso esce $0.6666666667$. Che cosa e' successo alla prima formula? (I due numeri che si sottraggono sono entrambi circa $10^{16}$ e differiscono per meno di un'unita': un `double` tiene circa $16$ cifre decimali, e la differenza si perde tutta.)

**P20.** **Sfida.** L'insieme di Mandelbrot e' l'insieme dei numeri complessi $c$ per cui la successione $z_0 = 0$, $z_{n+1} = z_n^2 + c$ resta limitata. Si dimostra che se un $z_n$ esce dal cerchio di raggio $2$, allora la successione diverge: basta quindi iterare un certo numero di volte e guardare se si e' usciti.

Scrivete `mandelbrot.c`, che riusa `Complesso`, `somma`, `prodotto` e `modulo2` di P16 e disegna l'insieme a schermo, un carattere per punto.

```c
#define LARGHEZZA 70
#define ALTEZZA 25
#define MAX_ITER 100
```

La funzione `int iterazioni(Complesso c)` parte da `z` uguale a $0 + 0i$ e fa un ciclo `for (k = 0; k < MAX_ITER; k++)`: a ogni giro esegue `z = somma(prodotto(z, z), c);` e subito dopo, se `modulo2(z) > 4`, restituisce `k`; se il ciclo finisce senza mai uscire, restituisce `MAX_ITER`. Scrivetela esattamente cosi': restituire `k + 1`, o controllare prima di aggiornare `z`, cambia qualche carattere del disegno.

Il `main` scorre le righe e le colonne: alla colonna `j` corrisponde la parte reale `-2.2 + 3.0 * j / (LARGHEZZA - 1)` e alla riga `i` la parte immaginaria `-1.2 + 2.4 * i / (ALTEZZA - 1)`. Si stampa `*` per i punti che non escono mai, e per gli altri il carattere `scala[k * 9 / MAX_ITER]`, dove

```c
char scala[] = " .:-=+*#%@";
```

e' solo un modo abbreviato di scrivere un array di dieci `char`: `scala[0]` e' uno spazio, `scala[1]` un punto, e cosi' via fino a `scala[9]`. (Le stringhe vere le vedrete piu' avanti.)

```text

                                              .
                                                  .
                                               .:.
                                             .*****
                                             .****:
                                      +*%*-***********.. :..
                                    ..********************:
                                   .:**********************  .
                       .%. .::    .*************************.
                       .********..+*************************.
                   ...:*************************************
     ****************************************************.
                   ...:*************************************
                       .********..+*************************.
                       .%. .::    .*************************.
                                   .:**********************  .
                                    ..********************:
                                      +*%*-***********.. :..
                                             .****:
                                             .*****
                                               .:.
                                                  .
                                              .
```

1. La riga chiave e' `z = somma(prodotto(z, z), c);`: una riga sola per $z^2 + c$, grazie alle funzioni di P16. Scrivetela senza quelle funzioni, con le parti reale e immaginaria separate: quante righe diventano?
2. Perche' si controlla `modulo2(z) > 4` invece di calcolare il modulo e confrontarlo con $2$? (E' la stessa ragione di I19 e di P16.)
3. La formula della parte reale manda `j = 0` in $-2.2$ e `j = LARGHEZZA - 1` in $0.8$. Verificatelo. Perche' si scrive `3.0` e non `3`? Provate a scrivere `3` e guardate che cosa succede al disegno.
4. La riga lunga al centro, all'altezza in cui la parte immaginaria vale esattamente zero, e' il segmento reale dell'insieme: si estende da $-2$ a $0.25$. Verificatelo con il disegno, contando le colonne.
5. L'ultimo carattere della scala, `@`, non viene mai stampato: `k * 9 / MAX_ITER` arriva al massimo a $8$, perche' i punti con `k` uguale a `MAX_ITER` prendono l'asterisco. Verificatelo, poi provate `scala[k % 10]` al posto di `scala[k * 9 / MAX_ITER]`: che cosa cambia nel disegno, e perche'?
6. **Con time.** Il disegno e' istantaneo: $70 \times 25$ punti sono troppo pochi per misurare qualcosa. Scrivete allora una versione senza stampa, che scorre una griglia di $2000 \times 2000$ punti nella stessa regione e conta quanti stanno dentro l'insieme: sono $858336$ su quattro milioni, e ci vogliono circa quattro secondi, compilando senza ottimizzazioni. Portate `MAX_ITER` a $1000$: i punti contati scendono a $838157$ e il tempo sale a una trentina di secondi. Riprovate le due misure aggiungendo `-O2` (G8): di quanto scendono? Perche' i punti diminuiscono? E dove si concentra tutto quel tempo, nei punti dentro l'insieme o in quelli fuori?


## Pacchetto Q: Operatori bit a bit e stringhe

Due argomenti che sembrano lontanissimi e che invece si incontrano di continuo. Il primo e' il modo di lavorare **direttamente sui bit** di un numero, cioe' sulla sua scrittura in base due: il C mette a disposizione sei operatori che agiscono su tutti i bit in una volta sola, e che il processore esegue in un colpo solo. Il secondo sono le **stringhe**, cioe' i testi, che in C non sono un tipo di dato a se' ma soltanto array di `char` con una convenzione.

Si incontrano perche' un testo e' fatto di caratteri, e un carattere occupa un byte, cioe' otto bit: letto come `unsigned char` e' un numero da $0$ a $255$ (il `char` semplice, con gcc su questi computer, ha segno e va da $-128$ a $127$; ci torneremo in Q6). ogni volta che si cifra, si comprime o si controlla un testo, si finisce per guardarlo come una sequenza di bit. Gli ultimi quattro esercizi del pacchetto fanno esattamente questo.

Compilate sempre con `gcc -g -Wall -Wextra`; in Q4 serve `time`, e in diversi esercizi serve `ctype.h`, che avete incontrato in O6.

### Gli operatori bit a bit

Sono sei, e lavorano sulla scrittura binaria dei numeri interi. Quattro sono logici e agiscono su ogni bit indipendentemente dagli altri; due spostano i bit.

| Operatore | Nome | Che cosa fa |
| --- | --- | --- |
| `a & b` | AND | il bit del risultato vale $1$ se **entrambi** valgono $1$ |
| `a \| b` | OR | il bit vale $1$ se **almeno uno** vale $1$ |
| `a ^ b` | XOR | il bit vale $1$ se i due sono **diversi** |
| `~a` | NOT | rovescia tutti i bit |
| `a << k` | spostamento a sinistra | sposta i bit di `k` posti a sinistra, riempiendo con zeri |
| `a >> k` | spostamento a destra | sposta i bit di `k` posti a destra |

Le tabelle di verita' sono quelle della logica, che gia' conoscete: la novita' e' che qui vengono applicate a trentadue coppie di bit in parallelo. Con $12 = 1100_2$ e $10 = 1010_2$:

```text
   1100   (12)        1100   (12)        1100   (12)
&  1010   (10)     |  1010   (10)     ^  1010   (10)
   ----               ----               ----
   1000   (8)         1110   (14)        0110   (6)
```

Gli spostamenti sono moltiplicazioni e divisioni per potenze di due: `a << k` vale $a \cdot 2^k$ e, **per `a` non negativo**, `a >> k` vale $a / 2^k$ con la divisione intera. `12 << 2` fa $48$ e `12 >> 2` fa $3$. (Per `a` negativo le due cose non coincidono: lo vedrete in Q3.)

**Usate `unsigned int` quando lavorate sui bit.** Nei tipi con segno il bit piu' a sinistra indica il segno, e allora: `~12` non vale un numero grande ma $-13$; lo spostamento a destra di un numero negativo e' definito dall'implementazione, e con gcc `-7 >> 1` vale $-4$ e non $-3$ come la divisione; lo spostamento a sinistra di un numero negativo e' addirittura comportamento indefinito. Con `unsigned` non ci sono sorprese. Il formattatore di `printf` per `unsigned int` e' `%u`.

### Maschere

Una *maschera* e' un numero scelto perche' ha $1$ esattamente nei bit che interessano. La maschera del solo bit numero `k` e' `1u << k`, e da sola basta per tutte e quattro le operazioni elementari su un singolo bit:

```c
x = x | (1u << k);     /* accende il bit k            */
x = x & ~(1u << k);    /* spegne  il bit k            */
x = x ^ (1u << k);     /* inverte il bit k            */
if ((x >> k) & 1u)     /* legge   il bit k            */
```

Da qui nasce l'idea che percorre meta' di questo pacchetto: **un intero senza segno e' un insieme**. Il bit `k` acceso significa "l'elemento `k` c'e'". Allora `|` e' l'unione, `&` e' l'intersezione, `^` e' la differenza simmetrica, e un `unsigned int` rappresenta un qualunque sottoinsieme di un insieme di trentadue elementi occupando quattro byte.

**Attenzione alla precedenza.** Gli operatori `&`, `^` e `|` hanno precedenza **piu' bassa** di `==` e `!=` (mentre `<<` e `>>` l'hanno piu' alta di tutti i confronti ma piu' bassa di `+` e `-`, quindi `x << 1 + 2` vale `x << 3`). La riga

```c
if (x & 1 == 0)        /* SBAGLIATO */
```

viene letta come `x & (1 == 0)`, cioe' `x & 0`, che e' sempre falso. Si scrive `if ((x & 1) == 0)`. Mettete sempre le parentesi: e' uno degli errori piu' difficili da vedere rileggendo.

### Le stringhe

In C una stringa non e' un tipo: e' un array di `char` in cui, dopo l'ultimo carattere utile, c'e' il carattere `'\0'`, che vale zero e si chiama *terminatore*. Tutto il resto segue da questa convenzione.

```c
char s[10] = "ciao";
```

dichiara dieci caratteri, di cui i primi cinque valgono `'c'`, `'i'`, `'a'`, `'o'`, `'\0'`; gli altri cinque esistono ma non contano. Da cui due conseguenze da tenere a mente sempre:

- **l'array deve essere piu' lungo del testo di almeno un carattere.** Per un testo di al piu' $20$ caratteri serve `char s[21]`;
- **nessuna funzione sa quanto e' lungo l'array**: sa solo dove si ferma il testo, perche' cerca lo zero. Se il terminatore manca, la funzione continua a leggere oltre la fine dell'array, e il programma fa cose arbitrarie.

Per scorrere una stringa si usa quindi il terminatore come condizione:

```c
for (i = 0; s[i] != '\0'; i++) { ... }
```

Per leggerla, `scanf("%s", s)` si ferma al primo spazio e non controlla la lunghezza dell'array; e' preferibile `fgets(s, L, stdin)`, che legge una riga intera, si ferma a `L - 1` caratteri e **tiene il carattere di a capo**, che quasi sempre va tolto:

```c
char riga[200];
if (fgets(riga, 200, stdin) != NULL) {
    int n = (int) strlen(riga);
    if (n > 0 && riga[n - 1] == '\n') {
        riga[n - 1] = '\0';
    }
}
```

Notate che nella `scanf` e nella `fgets` il nome dell'array si scrive **senza `&`**: come per gli array di I, il nome da solo basta.

### string.h

E' la libreria che mancava all'appello nella tabella di O. Le funzioni che userete qui sono cinque:

| Funzione | Che cosa fa | Attenzione |
| --- | --- | --- |
| `strlen(s)` | la lunghezza, terminatore escluso | la **conta** ogni volta, scorrendo: non e' gratis |
| `strcpy(d, s)` | copia `s` in `d` | non controlla che `d` sia abbastanza grande |
| `strcmp(a, b)` | $0$ se uguali, negativo se `a` viene prima | confronta i codici, non le lettere: `'Z'` viene prima di `'a'` |
| `strcat(d, s)` | attacca `s` in fondo a `d` | come `strcpy`, non controlla niente |
| `strncpy(d, s, n)` | copia al piu' `n` caratteri | se `s` e' lungo `n` o piu', **non** mette il terminatore |

`strlen` non restituisce un `int` ma un tipo senza segno, quindi per stamparlo con `%d` va scritto `(int) strlen(s)`, come per `sizeof`.

### Esercizi (Q1-Q10)

#### Gli operatori bit a bit

**Q1.** Guardare i bit. Scrivete un programma con un sottoprogramma `void stampa_binario(unsigned int x, int cifre)` che stampa gli ultimi `cifre` bit di `x`, dal piu' significativo al meno significativo, e un `main` che parte da `x = 0` e, mostrando `x` in binario e in decimale a ogni passo, accende il bit $3$, accende il bit $5$, inverte il bit $3$, accende il bit $1$ e spegne il bit $5$. Poi rilegge e stampa uno per uno i bit da $0$ a $3$ del risultato, e in fondo stampa `12 & 10`, `12 | 10`, `12 ^ 10`, `~12`, `12 << 2` e `12 >> 2`.

```text
partenza:        00000000  (0)
acceso il bit 3: 00001000  (8)
acceso il bit 5: 00101000  (40)
invertito bit 3: 00100000  (32)
acceso il bit 1: 00100010  (34)
spento il bit 5: 00000010  (2)
bit 0 = 0
bit 1 = 1
bit 2 = 0
bit 3 = 0

12 & 10 = 8
12 | 10 = 14
12 ^ 10 = 6
~12 = 4294967283
12 << 2 = 48,  12 >> 2 = 3
```

1. `stampa_binario` parte da `cifre - 1` e scende: perche' non si puo' partire da $0$ e salire? Che cosa stamperebbe?
2. Le due righe `acceso il bit 3` e `invertito bit 3` partono da situazioni diverse e il bit $3$ finisce in modo diverso. Che cosa succede se invece **accendete** un bit gia' acceso? E se lo **invertite** due volte? Aggiungete le due prove.
3. `~12` vale $4294967283$ e non $-13$: e' perche' la variabile e' `unsigned int`. Verificate che $4294967283 + 12 + 1 = 2^{32}$, e dite quanti bit a $1$ ha `~12`.
4. In F19 avete scritto un numero in una base qualsiasi dividendo per la base e tenendo i resti. Per la base $2$ c'e' questa scorciatoia. Riscrivete `stampa_binario` con il metodo di F19 e verificate che dia lo stesso risultato; poi dite quale delle due versioni e' piu' veloce e perche'.
5. **Trova l'errore.** Questo sottoprogramma dovrebbe dire se `x` e' pari, e invece risponde sempre "dispari":

```c
int e_pari(unsigned int x) {
    if (x & 1 == 0) {
        return 1;
    }
    return 0;
}
```

Spiegate come viene letta la condizione e correggetela. Perche' per il compilatore non e' un errore? Un avviso pero' c'e': compilate con `-Wall -Wextra` e riportatelo (e' `suggest parentheses around comparison in operand of '&'`, cioe' `-Wparentheses`).

**Q2.** Un intero e' un insieme. Con quattro elementi (`pane`, `latte`, `uova`, `sale`, in un array `char nomi[4][8]`) ci sono $16$ sottoinsiemi possibili, e ciascuno corrisponde a un numero da $0$ a $15$. Scrivete un programma che li elenca tutti, con un ciclo `for (s = 0; s < (1u << N); s++)`, stampando per ciascuno il numero, i quattro bit, gli elementi che contiene e la loro quantita', calcolata da `int quanti_bit(unsigned int x)`.

```text
sottoinsieme   elementi
 0  0000   { }   |S| = 0
 1  0001   { pane }   |S| = 1
 2  0010   { latte }   |S| = 1
 3  0011   { pane latte }   |S| = 2
...
15  1111   { pane latte uova sale }   |S| = 4

unione di {pane,uova} e {latte,uova}: 7
intersezione:                        4
differenza simmetrica:               3
```

1. Perche' il ciclo arriva a $2^N - 1$ e non a $N$? Quanti sottoinsiemi ha un insieme di $N$ elementi, e dove avete gia' incontrato questo numero? (Rileggete J10, la Torre di Hanoi: le mosse sono $2^n - 1$.)
2. `quanti_bit` si scrive con un `while (x)` che guarda `x & 1u` e poi fa `x >>= 1`. Quanti giri fa, al massimo, su un `unsigned int`? Scrivetelo e verificate che le quantita' stampate siano giuste.
3. Nella stampa dei bit si cicla da `N - 1` a $0$, nella stampa degli elementi da $0$ a `N - 1`. Perche' i due versi sono opposti? Che cosa succede se li uniformate?
4. Verificate a mano le tre righe finali: `{pane, uova}` e' il numero $5$, `{latte, uova}` e' il numero $6$. Calcolate $5 \mid 6$, $5 \mathbin{\&} 6$ e $5 \wedge 6$ in binario e controllate che corrispondano all'unione, all'intersezione e alla differenza simmetrica.
5. In N avete usato le `enum` per dare un nome ai valori. Dichiarate `enum spesa {PANE = 1, LATTE = 2, UOVA = 4, SALE = 8};` e riscrivete le tre righe finali usando i nomi. **In piu'.** Perche' in una `enum` di maschere i valori si scrivono come potenze di due, invece di lasciare che il compilatore conti $0, 1, 2, 3$?
6. Con `unsigned int` si arriva a insiemi di $32$ elementi. Quanti sottoinsiemi avrebbe un insieme di $32$ elementi? Se il programma ne stampasse uno al microsecondo, quanto tempo ci metterebbe?

**Q3.** Aritmetica con i bit. Tre fatti elementari: `x & 1u` dice se `x` e' dispari, `x >> 1` e' la meta', `x << 1` e' il doppio. Da soli bastano a riscrivere senza ricorsione l'esponenziazione veloce di J:

```c
long potenza_bit(long base, unsigned int e) {
    long r = 1;
    while (e) {
        if (e & 1u) {
            r *= base;
        }
        base *= base;
        e >>= 1;
    }
    return r;
}
```

Scrivete un programma che la confronta con la versione ricorsiva di J, in una tabella per $e$ da $0$ a $10$ con base $2$, e poi su $3^{13}$.

```text
  e   2^e (bit)   2^e (ric)
  0           1           1
  1           2           2
...
 10        1024        1024

3^13 = 1594323 (bit), 1594323 (ric)

7 << 1 = 14, 7 >> 1 = 3
-7 >> 1 = -4   (e -7/2 = -3)
5 & 1 = 1 (dispari), 8 & 1 = 0 (pari)
```

1. Seguite l'algoritmo a mano su $3^{13}$, scrivendo a ogni giro i valori di `e`, `base` e `r`. Quanti giri fa? Confrontate con $13$ in binario, che e' $1101$.
2. Perche' il ciclo calcola `base *= base` anche all'ultimo giro, quando il risultato non servira' piu'? E' uno spreco? Quanto grande puo' diventare `base` prima di traboccare?
3. Le due versioni fanno lo stesso numero di moltiplicazioni? Aggiungete un contatore a entrambe e verificate per $e$ da $1$ a $20$.
4. `-7 >> 1` vale $-4$ mentre `-7 / 2` vale $-3$: lo spostamento arrotonda verso il basso, la divisione verso lo zero. Scrivete che cosa succede ai bit di $-7$ e dite perche' questo e' un motivo in piu' per usare `unsigned` quando si lavora sui bit.
5. **In piu'.** `x & (x - 1)` spegne il bit acceso piu' a destra di `x`. Verificatelo su qualche numero, e usatelo per riscrivere `quanti_bit` di Q2 in modo che faccia tanti giri quanti sono i **bit accesi**, invece di tanti quanti sono i bit fino al piu' alto acceso. Contate i giri delle due versioni su `x = 1u`, su `x = 2147483648u` (un solo bit, ma il piu' alto) e su `x = 4294967295u`: su quali valori le due versioni pareggiano, e su quali la nuova vince?

#### Le stringhe

**Q4.** Il terminatore, `strlen`, e un errore da mezzo secondo. Scrivete un programma che dichiara `char s[MAX]` con `#define MAX 200001`, riempie le prime `MAX - 1` posizioni con le lettere `a`, `b`, ..., `z` ripetute, mette il terminatore in `s[MAX - 1]`, e poi conta quante volte compare la `a` in due modi: con `strlen` nella condizione del `for`, e con `strlen` calcolata una volta sola prima del ciclo.

```text
strlen(s) = 200000
strlen nella condizione: 0.403 s   (trovate 7693 'a')
strlen prima del ciclo:  0.000 s   (trovate 7693 'a')
```

1. Quante volte viene chiamata `strlen` nella prima versione? E quanti caratteri scorre ogni chiamata? Scrivete il numero totale di caratteri letti in funzione di `n` e dite qual e' la classe di complessita' delle due versioni.
2. E' esattamente l'errore che avete gia' incontrato in K12, dove al posto di `strlen` c'era una funzione che contava gli elementi fino a un valore sentinella. Rileggete quell'esercizio: che cosa hanno in comune il terminatore `'\0'` e la sentinella $-1$?
3. Sostituite il terminatore con una lettera (`s[MAX - 1] = 'x';`) ed eseguite. Che cosa stampa `strlen`? Il programma e' ancora corretto? Provate piu' volte: il risultato e' sempre lo stesso?
4. Verificate che `7693` sia il numero giusto: con $200000$ caratteri presi ciclicamente fra $26$, quante `a` ci si aspetta? Il conto torna?
5. **In piu'.** `strlen` restituisce un tipo senza segno. Scrivete `for (i = 0; i < strlen(s) - 1; i++)` su una stringa **vuota** e guardate che cosa succede: quanto vale `strlen(s) - 1` se `strlen(s)` vale $0$ e il tipo non ha segno?

**Q5.** Confrontare e copiare. Scrivete un programma che contiene `char v[6][20] = {"pera", "mela", "banana", "fico", "uva", "Mela"};`, stampa il risultato di cinque `strcmp` scelti da voi e poi ordina l'array con il selection sort di G16, usando `strcmp` per confrontare e `strcpy` per scambiare.

```text
strcmp("mela","pera")  = -1
strcmp("pera","mela")  = 1
strcmp("mela","mela")  = 0
strcmp("Mela","mela")  = -1
strcmp("mel","mela")   = -1

ordinate: Mela banana fico mela pera uva
```

Lo standard garantisce soltanto il **segno** del valore restituito da `strcmp`, non il valore: sulla vostra macchina al posto di $-1$ e $1$ potreste vedere $-3$ e $3$, o altri numeri. E' corretto lo stesso, e i confronti del tipo `strcmp(a, b) < 0` funzionano in ogni caso.

1. `"Mela"` finisce **prima** di `"banana"`. Non e' un errore: `strcmp` confronta i codici dei caratteri, e le maiuscole hanno codici piu' piccoli delle minuscole. Guardate la tabella ASCII e dite qual e' il codice di `'M'`, di `'b'` e di `'m'`.
2. Lo scambio di due stringhe richiede **tre** `strcpy` e una variabile di appoggio `char t[20]`, esattamente come lo scambio di due interi richiede tre assegnazioni. Perche' non si puo' scrivere `v[i] = v[pmin];`? Provate: gcc risponde `error: assignment to expression with array type`. Che cosa vi dice, quell'errore, su che cosa e' il nome di un array?
3. `strcmp("mel", "mela")` e' negativo: una stringa che e' l'inizio di un'altra viene prima. Spiegate perche', guardando che cosa trova `strcmp` nella quarta posizione delle due stringhe.
4. Per ordinare senza distinguere maiuscole e minuscole non si puo' usare `strcmp`. Scrivete `int confronta_minuscole(char a[], char b[])` che usa `tolower` di `ctype.h` carattere per carattere, e riordinate con quella. Dove finisce adesso `"Mela"`?
5. **Con gdb.** Mettete un punto di arresto dentro il ciclo esterno e stampate `v` a ogni giro: gdb mostra tutte e sei le stringhe. Verificate che dopo `k` giri le prime `k` siano quelle giuste e definitive.
6. **In piu'.** La dichiarazione e' `char v[6][20]`: ogni stringa occupa $20$ byte anche se ne usa $5$. Quanti byte occupa `v`? Quanti ne servirebbero davvero per queste sei parole? Perche' il C vi fa pagare lo spreco? (La risposta comoda arriva con i puntatori.)

**Q6.** Leggere e analizzare una riga. Scrivete un programma che legge una riga con `fgets`, toglie l'eventuale carattere di a capo, e stampa il numero di caratteri, di parole, di lettere e di cifre, e se la riga e' palindroma **considerando solo le lettere** e senza distinguere maiuscole e minuscole (quindi spazi, cifre e punteggiatura vengono saltati).

```text
$ echo "I topi non avevano nipoti" | ./analizza
riga: "I topi non avevano nipoti"
caratteri 25, parole 5, lettere 21, cifre 0
palindroma: si

$ echo "Anna 2025, anna!" | ./analizza
riga: "Anna 2025, anna!"
caratteri 16, parole 3, lettere 8, cifre 4
palindroma: si
```

Per contare le parole si tiene una variabile `dentro` che dice se si sta attraversando una parola: si incrementa il contatore solo quando si passa da fuori a dentro. Per il palindromo si usano due indici, uno dall'inizio e uno dalla fine, che saltano i caratteri non alfabetici e si avvicinano.

1. Perche' il controllo del palindromo non puo' essere semplicemente "confronta `riga[i]` con `riga[n - 1 - i]` per ogni `i`"? Provate questa versione sui due esempi e dite dove sbaglia.
2. Il secondo esempio risulta palindromo pur contenendo `2025`, perche' le cifre vengono saltate. Modificate il programma perche' le cifre contino come gli altri caratteri, e dite quale delle due versioni preferite e perche'. (Qui non c'e' una risposta sola: l'importante e' che il programma faccia una cosa sola e la dichiari nella documentazione.)
3. Che cosa succede se la riga e' piu' lunga di $199$ caratteri? Provate. Dove finisce il resto? E che cosa legge la `fgets` successiva?
4. Sostituite `fgets` con `scanf("%s", riga)` ed eseguite sui due esempi. Che cosa cambia, e perche'?
5. `isalpha` e compagne vogliono un argomento convertito a `unsigned char`: si scrive `isalpha((unsigned char) riga[i])`. Il motivo e' che `char`, con gcc su questi computer, e' con segno: il byte di una lettera accentata diventa un numero negativo, e lo standard dice che `isalpha` accetta solo i valori da $0$ a $255$ e `EOF`. Provate senza il cast su una riga con una lettera accentata: con la libreria di Linux non vedrete nessuna differenza, perche' la sua tabella copre anche gli indici negativi. Perche' allora il cast va messo lo stesso? (Pensate a che cosa succede su una libreria che la tabella negativa non ce l'ha.)
6. **In piu'.** Contate anche le vocali e stampate la parola piu' lunga. Per la seconda vi servono due indici e `strncpy`: attenzione al terminatore, che `strncpy` non mette se la parola e' lunga esattamente quanto il limite.

#### Mettere insieme i pezzi

**Q7.** Il cifrario XOR. Lo XOR ha una proprieta' che lo rende il cifrario piu' semplice che esista: applicarlo due volte con la stessa chiave riporta al punto di partenza, perche' $(a \wedge k) \wedge k = a$. Scrivete un programma con un sottoprogramma `void cifra(char s[], char chiave)` che fa `s[i] = s[i] ^ chiave` per ogni carattere, e un `main` che cifra un messaggio, lo stampa come sequenza di numeri, lo cifra di nuovo con la stessa chiave e verifica che sia tornato leggibile.

```text
in chiaro: Attacco all alba
cifrato  : 10 63 63 42 40 40 36 107 42 39 39 107 42 39 41 42
decifrato: Attacco all alba

'A' = 65, 'A' ^ 'K' = 10, ('A' ^ 'K') ^ 'K' = 65
```

1. Dimostrate la proprieta' $(a \wedge k) \wedge k = a$ guardando un singolo bit: fate la tabella dei quattro casi.
2. Il testo cifrato viene stampato come numeri e non con `%s`. Guardate la sequenza: c'e' un $10$. Che carattere e' il codice $10$? Che cosa succederebbe stampando il cifrato con `%s`? E se un carattere cifrato risultasse $0$?
3. Quest'ultima e' una domanda seria: se `s[i] == chiave`, il carattere cifrato e' `'\0'`, e la stringa si accorcia. Con la chiave `'K'`, quale lettera manda a zero il proprio carattere cifrato? Nel messaggio `"Attacco all alba"` non compare, ed e' per questo che li' la cifratura funziona; provate a cifrare `"OK"` e guardate che cosa resta.
4. Correggete il difetto cifrando un array di `unsigned char` di lunghezza nota invece di una stringa terminata. Che cosa dovete cambiare nelle firme dei sottoprogrammi?
5. Questo cifrario e' facilissimo da rompere: con una chiave di un solo carattere ci sono $256$ possibilita'. Scrivete il programma che le prova tutte su un messaggio cifrato e stampa i $256$ risultati: quanti sono leggibili?
6. **In piu'.** Con una chiave lunga quanto il messaggio, scelta a caso e usata una volta sola, lo stesso cifrario diventa **indecifrabile**, ed e' un risultato dimostrato. Modificate `cifra` perche' accetti una chiave che e' una stringa, usando `chiave[i % strlen(chiave)]`. Attenzione: cosi' scritto, `strlen` finisce dentro il ciclo. Rileggete Q4.

**Q8.** Il bit di parita'. I caratteri ASCII usano sette bit, quindi l'ottavo e' libero: si puo' usarlo per accorgersi degli errori di trasmissione. Si mette a $1$ se il numero di bit a $1$ del carattere e' dispari, in modo che il totale sia sempre pari; chi riceve ricalcola la parita' e, se non e' zero, sa che qualcosa si e' rovinato.

Scrivete un programma con `int parita(unsigned char c)`, che restituisce $0$ o $1$, e `unsigned char con_parita(unsigned char c)`, che accende il bit $7$ quando serve. Applicatelo a `"Ciao"`, mostrate la tabella, poi rovesciate un bit di un carattere e ricontrollate.

```text
car   ascii   bit      parita   con bit 7
 C      67   01000011     1       195
 i     105   01101001     0       105
 a      97   01100001     1       225
 o     111   01101111     0       111

controllo in ricezione:
  195 -> parita' totale 0  (deve essere 0)
  ...
dopo aver rovesciato un bit del secondo carattere:
  195 -> parita' totale 0
  109 -> parita' totale 1   ERRORE
```

1. Verificate a mano la prima riga: scrivete $67$ in binario, contate i bit a $1$, e controllate che $195$ sia $67$ con il bit $7$ acceso.
2. `con_parita` usa `0x80`, cioe' $128$, cioe' `1u << 7`. Scrivete i tre modi e dite quale preferite.
3. Il controllo funziona perche' la parita' di un carattere con il bit di parita' e' **sempre** zero. Spiegate perche', senza fare conti: che cosa fa il bit aggiunto al numero totale di bit a $1$?
4. Questo controllo rileva un bit sbagliato, ma non due. Rovesciate **due** bit dello stesso carattere e verificate che il controllo non se ne accorga. Quanti errori simultanei servono perche' il controllo fallisca? E con quale probabilita', se ogni bit si rovina indipendentemente?
5. Il bit di parita' dice che c'e' un errore ma non dove. Scrivete, per un messaggio di $n$ caratteri, un secondo controllo che sia lo XOR di tutti i caratteri: messo in fondo al messaggio, che cosa permette di fare in piu'? (Suggerimento: se sapete **quale** carattere e' andato perso, lo XOR di tutti gli altri ve lo restituisce.)
6. **In piu'.** La funzione `parita` fa fino a otto giri. Scrivetela con tre XOR e nessun ciclo, usando `c ^= c >> 4; c ^= c >> 2; c ^= c >> 1;` e poi leggendo il bit $0$. Verificate che dia gli stessi risultati per tutti i $256$ valori possibili.

**Q9.** La maschera dell'alfabeto. Ventisei lettere stanno comodamente nei trentadue bit di un `unsigned int`: il bit $0$ per la `a`, il bit $1$ per la `b`, e cosi' via. Con una sola variabile si risponde allora a diverse domande su un testo. Scrivete `unsigned int maschera(char s[])` che accende il bit di ogni lettera presente, ignorando maiuscole e caratteri non alfabetici, e usatela per stampare la maschera in binario, il numero di lettere diverse e se la frase e' un pangramma, cioe' contiene tutte e ventisei le lettere.

```text
Quel vituperabile xenofobo zelante assaggia il whisky ed esclama: alleluja!
  11111111111111111111111111  lettere diverse 26  pangramma si
Ciao mondo
  00000000000111000100001101  lettere diverse  7  pangramma no
abcdefghijklmnopqrstuvwxyz
  11111111111111111111111111  lettere diverse 26  pangramma si

maschera completa = 67108863 = 2^26 - 1 = 67108863

anagrammi?
  "roma" e "amor": maschere 151553 e 151553 -> forse
  "casa" e "caos": maschere 262149 e 278533 -> no
  "aab"  e "abb" : maschere 3 e 3 -> forse
```

1. Il test del pangramma e' `m == (1u << 26) - 1u`. Spiegate perche' quel numero ha esattamente ventisei bit accesi, e verificate che valga $67108863$.
2. Il numero di lettere diverse e' `quanti_bit(m)` di Q2. Quante operazioni costa, rispetto a contarle con un array di ventisei contatori? Quale delle due usereste se vi servisse anche **quante volte** compare ciascuna lettera?
3. Le ultime tre righe mostrano che la maschera **non** basta per gli anagrammi: `"aab"` e `"abb"` hanno la stessa maschera e non sono anagrammi. Dite esattamente che cosa dimostra l'uguaglianza delle maschere e che cosa no, e scrivete il controllo completo con i ventisei contatori.
4. La maschera e' pero' utilissima come **filtro veloce**: se le maschere sono diverse, le due parole non sono anagrammi, e la risposta costa un confronto fra due interi. Generate $2000$ parole casuali di lunghezza fra $3$ e $8$ (con `srand(1)` e `rand`, come in G2), calcolate una volta sola le $2000$ maschere e contate quante delle circa due milioni di coppie sopravvivono al filtro. Misurate il tempo con il filtro e senza, cioe' applicando a ogni coppia il controllo completo a ventisei contatori.
5. Scrivete, usando due maschere, un programma che dice quali lettere compaiono nella prima frase e non nella seconda. Quale operatore vi serve?
6. **In piu'.** Con un `unsigned long long`, che ha almeno sessantaquattro bit, si potrebbero distinguere maiuscole e minuscole usandone cinquantadue. Che cosa cambierebbe nella funzione `maschera`? E il pangramma, come si controllerebbe?

**Q10.** **Sfida.** Impacchettare. Un testo di sole lettere maiuscole e spazi usa ventisette simboli diversi, che stanno in cinque bit; eppure ogni carattere ne occupa otto. Si possono quindi memorizzare otto caratteri in cinque byte invece che in otto: a regime si risparmia il $37.5\%$.

Scrivete un programma che impacchetta una stringa di maiuscole e spazi a cinque bit per carattere, stampa i byte ottenuti in esadecimale e poi la ricostruisce, verificando con `strcmp` che sia identica all'originale.

```text
testo:     "MATEMATICA DISCRETA"  (19 caratteri, 19 byte)
impacchettato: 12 byte  -> 63% dell'originale
byte: 60 26 46 02 68 10 34 34 48 51 24 C0
ricostruito: "MATEMATICA DISCRETA"  -> identico
```

L'idea e' tenere un *accumulatore* `unsigned int acc` e un contatore `bit` di quanti bit utili contiene. Per ogni carattere si fa `acc = (acc << 5) | valore; bit += 5;` e, finche' `bit >= 8`, si estrae il byte piu' alto con `(acc >> (bit - 8)) & 0xFF` e si fa `bit -= 8`. Alla fine, se avanzano bit, si completa l'ultimo byte spostando a sinistra.

1. Verificate il conto: $19$ caratteri per $5$ bit fanno quanti bit? E quanti byte, arrotondando per eccesso? Il $12$ torna?
2. Scrivete la formula generale dei byte necessari per `n` caratteri, e verificate che per `n` multiplo di $8$ il risparmio sia esattamente $\frac{3}{8}$.
3. Controllate a mano il primo byte. `'M'` e' la tredicesima lettera, quindi vale $12$, cioe' `01100`; `'A'` vale $0$, cioe' `00000`. I primi otto bit sono allora `01100000`, cioe' `0x60` in esadecimale. Torna?
4. Lo spazio e' codificato come $26$. Che cosa succede se il testo contiene un carattere che non e' ne' una maiuscola ne' uno spazio? Aggiungete un controllo e decidete che cosa fare: rifiutare il testo, oppure sostituire il carattere. Motivate la scelta.
5. Il programma deve sapere `n` per ricostruire: i bit avanzati alla fine sono indistinguibili da altri caratteri. Toglietelo dalla ricostruzione e fatela andare avanti finche' ci sono bit. Con `"MATEMATICA DISCRETA"` non cambia niente, perche' $19 \cdot 5 = 95$ bit lasciano un solo bit di riempimento; con `"MATEMATICA"` invece $10 \cdot 5 = 50$ bit ne lasciano sei, e in fondo compare una `A` che non c'era. Per quali lunghezze succede? Come si risolve il problema in generale? (Due modi: memorizzare la lunghezza, oppure riservare un valore come terminatore. Quale dei due costa meno, qui?)
6. **In piu'.** In L19 avete visto che la codifica a sequenze puo' **allungare** il testo. Questo metodo invece non puo' mai allungarlo, e sui testi lunghi lo accorcia praticamente sempre dello stesso fattore, qualunque sia il testo (a meno dell'arrotondamento dell'ultimo byte). Qual e' la differenza fra i due? Che cosa sfrutta ciascuno dei due per risparmiare, e perche' solo uno dei due puo' fallire?
