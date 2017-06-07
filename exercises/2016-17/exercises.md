### Alcuni esercizi assegnati

Qui si raccolgono alcuni esercizi significativi assegnati durante il corso:

1.  Realizzare InsertionSort in modo ricorsivo
2.  Realizzare una funzione Dup(A,p,r) che verifica, in modo divide et impera, la presenza di duplicati nell'array A.
3.  Realizzare una funzione Sum(A,key) che dato un array A e un intero k verifica se key è esprimibile come la somma di due elementi di A ovvero se vi sono indici i e j tali che key = A[i] + A[j].
4.  Siano date n monete, delle quali una è falsa. Le monete sono identiche esteticamente, ma quella falsa pesa meno delle altre. Data una bilancia a due piatti e avendo a disposizione come operazioni solo la pesata di due sottoinsiemi (disgiunti) di monete, dare un algoritmo di complessità _O(log n)_ che determina qual è la moneta falsa. Mostrare che questa è la complessità del problema, ovvero che ogni algoritmo è _Ω(log n)_.
5.  Risolvere le seguenti ricorrenze:
    1.  T(n) = 2 · T(n/2) + log(n)
    2.  T(n) = 2 · T(n/2) + n²
    3.  T(n) = 2 · T(n/2) + n ·log(n)
    4.  T(n) = a · T(n-1) + b
6.  Realizzare una funzione Select(A, k) che restituisce l'elemento che occuperebbe la k-ma posizione nell'array A ordinato. Detta n la dimensione dell'array, trovare soluzioni:
    *   O(n log(n))
    *   O(n + k log(n))
    *   O(n log(k))Per gli ultimi due casi il suggerimento è quello di usare un MinHeap e un MaxHeap rispettivamente.
7.  Realizzare con approccio divide et impera una funzione Inv(A,p,r) che ritorna il numero di inversioni in A[p,r], ovvero il numero di coppie di indici i, j tali che i < j e A[i] > A[j]. [Suggerimento: Modificare il MergeSort]
8.  Realizzare una procedure per fondere due alberi binari, il primo completo, il secondo quasi completo, della stessa altezza, che soddisfano la proprietà di Max-Heap, mantenendo questa proprietà. Cercare una soluzione di costo O(log(n)) dove n è il numero di elementi totali dei due alberi.
9.  Fornire una implementazione dei max-heap come alberi realizzati mediante strutture a puntatori
10.  Dire se esiste un algoritmo di tempo lineare per elencare gli elementi di un max-heap in ordine descrescente. Descrivere l'algoritmo oppure motivare l'impossibilità di realizzarlo.
11.  Mostrare che la funzione di hash _h(k) =_ ⌊ _k mod m_⌋, quando _m= 2<sup>p</sup>-1_ e le chiavi _k_ consistono di _w_ parole di _p_ bit è invariante per permutazioni delle parole costituenti la chiave.
12.  Realizzare una implementazione degli alberi binari di ricerca nella quale il campo p (padre) è sostituito dal campo succ (successore).
13.  Dimostrare che un albero binario è un Albero Binario di Ricerca se e solo se una visita simmetrica visita i nodi in ordine di chiave crescente.
14.  Realizzare un algoritmo ricorsivo che verifica se un albero binario è completo e valutarne la complessità.
15.  Definire un algoritmo di programmazione dinamica che determina la triangolazione di peso minimo per un poligono convesso. Si assuma che il poligono sia dato tramite la sequenza, in senso orario, dei suoi vertici (q<sub>1</sub>, q<sub>2</sub>, ..., q<sub>n</sub>), che il peso di un triangolo T = q<sub>i</sub>q<sub>k</sub>q<sub>j</sub> sia dato da c(T) (costo di calcolo costante) e che il peso di una triangolazione sia la somma del peso dei triangoli che la compongono.q
16.  Definire un algoritmo di programmazione dinamica che date due sequenze X = x<sub>1</sub> ... x<sub>m</sub>, Y = y<sub>1</sub> ... y<sub>n</sub> determina una shortest common supersequece.
17.  Definire un algoritmo di programmazione dinamica che data una sequenza X = x<sub>1</sub> ... x<sub>m</sub> determina una sottostringa (sottosequenza formata da caratteri consecutivi) palindroma di lunghezza massima.

### Esercizi aggiuntivi (cartella extra)

1.  Scrivere un algoritmo per determinare un insieme minimo di monete, di tagli 5, 2 e 1, che totalizzi un dato resto r.
2.  Date n lezioni A<sub>1</sub>, ..., A<sub>n</sub>, ciascuna con il suo tempo di inizio s<sub>i</sub> e fine f<sub>i</sub> scrivere un algoritmo per allocare tutte le lezioni in un numero minimo di aule.
3.  Date n lezioni A<sub>1</sub>, ..., A<sub>n</sub>, ciascuna con il suo tempo di inizio s<sub>i</sub> e fine f<sub>i</sub> scrivere un algoritmo per allocare il massimo numero di lezioni in un numero prefissato m di aule.
4.  Implementare una coda FIFO con due pile, garantendo per le operazioni di inserimento ed estrazione costo ammortizzato O(1).
5.  Realizzare un contatore come array di bit A[0,k], con operazioni di incremento e reset, garantendo per le operazioni costo ammortizzato O(1).
6.  Risolvere le seguenti ricorrenze:
    *   T(n) = 4 · T(n/16) + √n
    *   T(n) = 4 · T(n/16) + n
    *   T(n) = 4 · T(n/16) + log(n)
    *   T(n) = T(n-1) + n<sup>2</sup>nei primi tre casi utilizzando il master theorem, nell'ultimo il metodo di sostituzione.
7.  Dato un insieme di file di dimensione f1, ..., fn e un disco di capacità d, realizzare un algoritmo greedy che massimizza il numero di file nel disco, dimostrandone la correttezza.
8.  Realizzare una generalizzazione del Mergesort nel quale l'array viene diviso in k parti invece che in 2\. Valutarne la complessità.
9.  Tradurre nel modo più diretto possibile la definizione dei numeri di Fibonacci (ovvero fib(0) = fib(1) =1, fib(n+2) = fib(n+1) + fib(n) in un algoritmo ricorsivo. Mostrare che la complessità è limitata inferiormente da α<sup>n</sup> per una opportuna costante α > 1 e fornire un algoritmo iterativo (stile programmazione dinamica, bottom up) di complessità lineare.
10.  Si consideri una variante degli alberi binari di ricerca nei quali ogni nodo x ha un attributo addizionale f che rappresenta il numero di foglie nel sottoalbero radicato in x. Definire una funzione Insert(T,z) che inserisce un nodo.
11.  Data una tabella hash con indirizzamento aperto, di dimensione m=7 operante con doppio hash basato sulle funzioni h1(k)= k mod m e h2(k) = 1 + k mod (m-1), descrivere cosa si ottiene inserendo i valori 10, 15, 22, 31, 43.