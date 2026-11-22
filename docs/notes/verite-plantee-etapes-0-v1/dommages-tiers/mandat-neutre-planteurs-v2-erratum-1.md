# Erratum 1 du mandat neutre des tiers planteurs de l'étape 2 (v2)

- **Date** : 21 novembre 2026, vers 21:10 UTC (`date -u` : Sat Nov 21 21:10:09 UTC 2026), arbre de travail à `3118c8a2`, branche `prep/verite-plantee-etapes-0-v1`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf en effort maximal, sur le mandat de la mère sous `GO-2026-11-21-84` (mot de Lazar vers 20:35Z : « Opus 5.5, en effort maximal, écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues. + appels api claude fable 5.2 puis sceller »). Je n'ai rien conçu de neuf : quand un point demandait un choix que les pièces ne tranchent pas, je l'ai écrit en nœud ouvert.
- **Pièce corrigée** : `docs/notes/verite-plantee-etapes-0-v1/dommages-tiers/mandat-neutre-planteurs-v2.md` (`cb7ba44824517b50e823150385cbfabb2c9a475dca759e8d942b6b292bc07b9b`), gardée intacte (R12). Cet erratum prime aux lieux qu'il nomme ; ailleurs, la pièce se lit telle quelle, avec les errata 1 des autres pièces du dossier là où elle les cite.
- **Remarques portées** : `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` (`8d1ee3a4b31cf7a7762e6f7cf618a9e71927e23c14a0d2026bc8fcc6455dfc61`), lue en entier ; ici : V-4, V-2 (D-5 appliquée sous GO-2026-11-21-69) et V-3 (nœud N-14). Pour V-2, la lecture de la mère, appliquée telle quelle : `docs/notes/verite-plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md` (`dc9e757b1aa4cbd716d0a4bce3639e21f4866ac926623cdfdb97489298c43f7a`). Pour N-14, la garde commune `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91`, sur `main`, en vérification ; citée, non modifiée).
- **Chiffres** : aucun nombre neuf ni changé dans cette pièce.
- **Statut** : non scellé ; à relire par Claude Fable 5.2, appelé par l'API, puis scellement (`GO-2026-11-21-84`). Ni commit, ni appel payant ; aucun compagnon `.sha256` écrit par moi, puisque le scellement vient après la relecture.
- **Cloisonnement** : celui de l'erratum 1 du brouillon v2 du préenregistrement (même auteur, même session).
- **Forme** : chaque point donne son lieu, la remarque qu'il porte, l'ancien texte, copié de la pièce et présent une seule fois quand le point s'applique, et le nouveau texte ; un ajout cite le texte qu'il suit ou qu'il précède, qui ne change pas. Les points s'appliquent dans l'ordre ; appliqués ensemble à une copie, ils passent tous (vérifié par programme dans mon bloc-notes ; la copie n'est pas versée). Les tables d'historique de la pièce (« Remarque de la contre-lecture → correction portée » et ses pareilles) disent ce que la v2 a porté ; elles ne sont pas réécrites.

Les parties A et A bis, servies au planteur, ne changent pas : aucun point de cet erratum ne les touche, et la relecture de cloisonnement de la partie B reste due avant tout envoi.

## Les points

### M-1 — En-tête, « Rien n'est lancé »

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> **Rien n'est lancé** : l'étape 2 attend la décision sur qui plante et de quelles lignées (D-5 de la note source), un devis par ligne et un mot de Lazar.

**Nouveau texte** :

> **Rien n'est lancé** : l'étape 2 attend un devis par ligne et un mot de Lazar. La décision D-5, option (a) avec (c) écrit d'avance comme repli, est appliquée sous `GO-2026-11-21-69` (lecture de la mère, `docs/notes/verite-plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md`, `dc9e757b1aa4cbd7…`, point 2) : deux modèles de deux lignées hors de celles des lecteurs, sessions isolées, plants en quarantaine ; les lignées elles-mêmes se fixent dans l'additif de l'étape 2. L'emploi de modèles extérieurs passe par la règle des appels aux modèles de Google (`CLAUDE.md` ; nœud N-14 du préenregistrement ; partie B, point 11 bis) et par la garde de motifs vide avant tout envoi (partie B, point 2).

### M-2 — Partie B, point 3 bis

Remarque portée : V-4.

*Ajout, après le texte cité, qui ne change pas ; à la suite, dans le même paragraphe.*

**Texte cité (inchangé)** :

> La relectrice vérifie ces quatre égalités sans lire les plans, et rejette l'envoi si une liste est vide ou si les deux longueurs diffèrent.

**Texte ajouté** :

> **La taille grande se définit par la liste servie** : l'écart touche le passage désigné et la moitié au moins des passages de la liste servie (partie A, « Le sens des tailles »). Ramener la liste au plus petit des deux nombres de passages repérés peut faire tomber, du côté de la référence, la part touchée sous « la moitié au moins des contrôles » : **les valideurs vérifient donc la dose contre la grille** (préenregistrement, « Plan d'analyse », la grille : grossier, la moitié au moins des contrôles) ; **sinon, la taille grande est « sans objet » pour ce plan**, des deux côtés, comme au dernier point de « Ce que ce mandat laisse ouvert ». Comment ce « sans objet », constaté après l'écriture, se compte (dans la part rejetée, par motif, ou hors des plants prévus) n'est écrit dans aucune pièce : nœud ouvert, avec le mandat des valideurs, qui n'est pas écrit.

### M-3 — Partie B, « Sur la session », après le point 11

Remarque portée : V-2, V-3 (N-14).

*Ajout, après le texte cité, qui ne change pas ; à la ligne.*

**Texte cité (inchangé)** :

> 11. Chaque rédacteur travaille dans une session neuve, isolée, sans outil de lecture du dépôt ; sa session est close avant la première lecture de l'oracle ; rien ne lui revient.

**Texte ajouté** :

> 11 bis. **Si un rédacteur est un modèle de Google**, chaque envoi passe d'abord la garde commune des appels aux modèles de Google, `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée, non modifiée) : un envoi qu'elle refuse ne part pas ; une réponse à zéro jeton de pensée, au motif de fin « MAX_TOKENS », « SAFETY » ou « RECITATION », ou au texte vide est un défaut journalisé, jamais une réponse (`CLAUDE.md`, « Appels aux modèles de Google », `GO-2026-11-21-71` ; nœud N-14 du préenregistrement).

## Remarque par remarque

| Remarque | Ce qui est porté ici | Points |
|---|---|---|
| V-2 | D-5 (a), avec (c) écrit d'avance comme repli, appliquée sous GO-2026-11-21-69 ; l'étape 2 attend un devis par ligne et un mot de Lazar | M-1 |
| V-3 (N-14) | un rédacteur qui serait un modèle de Google passe par la garde commune ; la garde de motifs reste due (point 2) | M-1, M-3 |
| V-4 | taille grande définie par la liste servie ; dose vérifiée par les valideurs contre la grille ; sinon « sans objet » pour ce plan ; le compte de ce « sans objet » laissé en nœud ouvert | M-2 |
