Echipa Python

Obiective:

    Aplicarea protocolului HTTP în transmisiuni de date;
    Elaborarea modulului reverse proxy;
       - Implementarea mecanismului de caching,
       - Implementarea mecanismului de load-balancing,
       - Elaborarea sincronizării datelor (distribuirea în date) între nodurile data-warehouse (utilizînd un (S)DBMS existent).


Implementarea unui web-proxy : balansarea interogarilor client intre noduri, numite dara warehouse , un nod ce ia date din baza de date, le serializeaza si le returneaza, similar nod informational, cum stocam date ? Avem 2 noduri, care cumva sincronizeaza datele intre ele, prin 2 metode, un nod specializat ce sincronizeaza datele, sau folosim o baza de date, baza de date o folosim ca sa sincronizam datele prin ea, fara tranzactii, cum populam datele ? ele apar de undeva, le introducem manual, generam random, etc.

Membrii :
Suicimezov Georgeta; 
Gherman Olga; 
Filipesco Radu; 
Turcan Dorin-Teodor;
