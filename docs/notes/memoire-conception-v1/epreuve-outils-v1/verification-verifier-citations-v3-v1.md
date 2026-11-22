# Vérification des corrections — verifier_citations_v3.py

- Pièces vérifiées, au commit 060a92a4 :
  - `docs/notes/memoire-conception-v1/epreuve-outils-v1/verifier_citations_v3.py` (93741405…) ;
  - `test_verifier_citations_v3.py` (4fd007c1…).
- Les deux empreintes sont conformes à leurs compagnons.
- Vérification par le même contre-lecteur, en lecture seule. J'ai lu tout l'écart entre la v2 et la v3.
- Je n'ai ouvert aucun fichier de la banque ; elle est retirée de l'arbre que j'ai listé.

## Verdict

**Conforme.** Les points 11 à 14 corrigent les deux défauts moyens et les trois défauts faibles de la v2. Je ne trouve ni défaut nouveau ni régression.

## Points de la v2, un par un

1. **Dossier exclu en dernier segment — corrigé.**
   - Sont refusés : le dossier de la banque (avec ou sans barre finale, et en chemin absolu), `docs/decisions/quarantaine` et `…/archives-reponses-modeles`.
   - Déclarer le dossier de la banque comme ouvert fait tomber la porte 1 (code 4).
   - Aucun fichier autorisé de l'arbre ne porte exactement un nom de dossier exclu : rien n'est refusé à tort.
2. **Dossier cité comme un fichier — corrigé.** `git cat-file -t` doit valoir `blob`. Citer `epreuve-outils-v1/` est refusé.
3. **Étoile qui traverse les dossiers — corrigé.** `demande-x/reponse-carbon.md` et `question-neutre-x/sous/reponse.md` sont refusés.
   - Aucun sous-dossier n'existe sous `copies-sans-nom-v1/` au commit : la règle du même nombre de « / » ne refuse rien d'autorisé.
4. **Compagnons des demandes — corrigé.** `demande-33-….md.sha256` est accepté.
5. **Identifiant — corrigé.** Un `id` en liste donne « ligne illisible » (code 1) ; le script ne tombe plus.

## Absence de régression

- Les 59 essais du dépôt passent.
- Toutes mes mutations de la v1 et de la v2 donnent le résultat attendu.
- **Arbre entier du commit :**
  - aucun des 96 fichiers hors de la sous-liste n'est accepté ;
  - les 8 fichiers autorisés passent ;
  - sous les préfixes autorisés, il ne reste que des refus voulus : la programmation de poids, la demande 24, « SEQUESTRE », un « compte-rendu ».
- **Porte 2 :** empreinte bruitée refusée, 64 signes faux refusés, passage banal refusé, passage coupé au milieu d'un mot refusé.
- **Porte 1 :**
  - champs absents : les deux portes tombent ;
  - chemin absolu dans le dépôt : accepté ;
  - autre racine : refusée.
- **Commit :** `main`, un SHA abrégé et un SHA inexistant sont refusés.
- **Fichier de réponses :** un identifiant répété et un fichier vide sont refusés.
- **Accents :** retirés avant les règles de nom.

## Remarques, sans défaut

- Un lien symbolique suivi par git est un objet de type `blob`. `git show` en rend la cible, c'est-à-dire un chemin, et jamais le contenu du fichier visé. C'est sans fuite.
- Choix déclarés et acceptables :
  - « transcription » est exclu comme sous-chaîne ;
  - la défense et les chiffres cloisonnés restent jugés par l'examinateur ;
  - l'ancêtre du commit (`main` ou `claude/bibliothecaire-v1`) n'est pas contrôlé.

## Fichiers

- Mutations :
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_regles_v3.py`
  - `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_v3_neuves.py`
- Arbre listé : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/arbre3.txt`
