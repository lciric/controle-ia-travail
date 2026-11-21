# Manifeste du lancement de l'essai court de mesure du palier 0b — v1

Session du compte organisme (session fille), 2026-11-21. Décision de la mère R-4605 (option (b)), mot de la mère de 16:15Z ; ordre de Lazar « 2 puis 3 » (GO-2026-11-21-66). Processeur du conteneur, aucune dépense, aucune machine louée.

- **Racine** : `/home/user/palier-0b-racine`, arbre de travail détaché du dépôt à `d7f949acd9ac92e998e57663d2cc741de93f18c3`, sans modification ; programme `lancer_etapes_3_5_6_v2.py` à l'empreinte `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`.
- **Pièces employées**, copiées dans le dossier de tenue `/home/user/journaux-palier-0b-essai-court-v1/` : `lancer-essai-court-v2.sh` (`4c96c703…`), `demarrer-essai-court-v2.sh` (`2ec06e95…`), `gardien-essai-court-v3.py` (`d8fd650b…`), `demarrer-gardien-essai-court-v3.sh` (`97586b7b…`). Chaîne : auteur v1, contre-lecture (À corriger), erratum 1, auteur v2, vérification (À corriger), erratum 2, gardien v3, vérification (Conforme, réserve sur l'orphelin lent qui écrit moins d'une fois par seconde).
- **Vérification à blanc** à 17:31:30Z : départ permis, code 0. Elle a écrit `code-de-sortie.txt` (« 0 ») dans le dossier de tenue, ce qui aurait refusé le vrai départ (code 4) : renommé `code-de-sortie-verification-a-blanc.txt`, sans suppression.
- **Commande** : celle du complément 1 v3, à l'octet, sauf le dossier des sorties : `/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1`.
- **Départ** : 2026-11-21T17:31:41.98Z ; processus 14722, groupe 14722, heure de départ 683679 tops ; démarrage de la machine `3006ce58-85f4-41fc-9405-8895082f1d03`.
- **Gardien** : processus 14816, prise de garde 17:31:47Z, identité confirmée. Seuils : place libre 8 000 000 000 octets ; arrêt de mesure à n = 13 dossiers de source de l'étape 4, ou 2 700 s d'étape 4 ; intervalle 60 s ; arrêt forcé après 60 s. Place libre au départ : 38 363 934 720 octets.
- **Journaux** : `journal-essai-court.txt` (lanceur), `journal-de-tenue-essai-court.txt` (gardien) ; mesure attendue dans `mesure-essai-court.txt`, arrêt dans `arret-gardien.txt`.
