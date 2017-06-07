#include<iostream>
using namespace std;

int rest(int r, int * p){								//restituisce il numero minimo di monete necessarie per rendere il resto r 
														//usando l'array p, array che contiene il taglio delle monete disponibili ordinate
														//in modo decrescente. Usiamo una strategia Top-down
	if(r==0)											//Per restituire un resto pari a 0 €,..
		return 0;										//...occorrono zero monete, caso base
	
	if(r-p[0] >=0){										//Se il resto rimanente (togliendo dall'originale r, la moneta del taglio più grande) è >=0 
		cout << "Moneta usata "  << p[0] << endl;		//stampiamo il taglio della moneta
		return 1 + rest(r - p[0], p);					//aggiungiamo 1 alle monete usate ed eseguiamo la funzione usando lo stesso array e scalando 
	}													//il valore della moneta usata dal resto
		
	else {												//altrimenti, la moneta che stiamo usando non è più adatta e 
		cout << "Cambio moneta " << endl;				//la cambiamo con quella di valore appena inferiore
		return rest(r,p+1);								//per fare ciò reinvochiamo la funzione usando la posizione successiva dell'array
	}
}	

main() {
		int coins [] = { 5, 2, 1 };						//contiene le monete ordinate in modo decrescente per taglio 
		int amount = 48;								//il resto originale da ritornare
		int cont = rest(amount, coins);					//un contatore piuttosto inutile per salvare il valore della funzione
		cout << "Il numero minimo di monete richieste per restituire il resto "
				<< amount << " e': " << cont;			//stampiamo quello che cerchiamo
}
