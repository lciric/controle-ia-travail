# Vérification des corrections du devis du service de la question v8 au collisionneur — v1

> Même contre-lecteur que `contre-lecture-devis-v8-v1.md` (230c7b4e…) : Claude Opus 5.5, sous-agent, qui n'a écrit ni le devis, ni la version servie, ni son programme. 23 novembre 2026. Dépôt au commit f0212d7d4.
>
> Pièces lues :
> - `devis-service-collisionneur-modes-v8-v2.md` (51142200…, non scellé, sans `.sha256` : normal avant le scellement) ;
> - `version-servie/` : six pièces, sceaux vérifiés ;
> - `calculs-v3/` : sceaux vérifiés, sauf l'artefact volontaire `d-sceau-faux` (N-3).
>
> Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre ». Aucun envoi, aucune dépense, aucun commit. Rejeux dans le bloc-notes de la session.

## Verdict

**Bon après deux corrections légères, sur la seule décision 1.** Les défauts D-1 à D-10 sont corrigés, sauf D-7, en partie. D-1 (en partie) et D-5 étaient mes erreurs, que la v2 relève à juste titre. Le programme de la version servie est solide : je l'ai rejoué, il redonne le texte servi au même octet (b69f6b6d…). Les calculs v3 se rejouent à l'identique. Deux points à corriger :
- l'option (b) de la décision 1 ne se fait pas avec « le même programme » ;
- le chemin `donnees/` reste un chemin interne au sens de la condition de GO-2026-11-21-08.

## 1. Défauts de la contre-lecture, un par un

| défaut | sort | constat |
|---|---|---|
| D-1, haut | **corrigé** | Le haut de 15,52 se rejoue : 10,46 + 2,41 + 2,66. La pointe de 19,99 aussi : 12,58 dépensés avant la réponse d'Astra, plus sa marge de 7,42. Le plafond est porté à 26 : il tolère deux coupures de Carbon de plus, et une troisième demanderait 28,12. **Mon ≈ 18 comptait deux fois** : l'espérance d'une cellule coupée puis relancée vaut s + p × w, et la relance réussie est la cellule elle-même. L'arbitrage de `--sortie-max` est dit : 4 USD de plafond. |
| D-2, mécanique au plafond | **corrigé** | La ligne scellée est la borne effective ; `--plafond-usd 26` est redonné à chaque commande. Une reprise demande ligne et plafond sur un même GO. Une cellule refusée au plafond est un « jamais parti » et devient un nœud, avec `devis-reprise`. La sous-commande `etage3` et l'option `--sortie` existent bien dans la révision 8m (l. 3319-3351). |
| D-3, version servie vérifiable | **corrigé**, une réserve (N-1, N-2) | Programme de classe B, liste fermée, reconstruction, zone, différentiel borné : voir § 2. Les restes « -136 » et « -139 » sont pris par l'identifiant élargi. Le transfert de la porte (v5 vers v6) est mis dans la décision 1. |
| D-4, option manquante | **corrigé** | « Fable seul » ajouté à l'option (b), chiffré : 10,56 / 15,45 / 26. La perte sans Fable et le coût de l'attente sont écrits, ainsi que la règle « Qui conçoit ». |
| D-5, relances dans l'attendu | **justifié, j'en conviens** | E = (1 − p) s + p (w + s) = s + p w : mon défaut était faux. |
| D-6, session d'Opus perdue | **corrigé** | § 7.5. |
| D-7, § 13 et compagnons | **en partie** | Le § 14 est à jour et liste tous les fichiers ; `calculs-v3/` a ses compagnons. Mais `calculs/` n'en a toujours aucun : 0 `.sha256` (R6), renvoyé « au prochain versement ». À faire avant la remise à Lazar. |
| D-8, provenance « v8d » | **corrigé** | « désigné par le mandat de la mère ». |
| D-9, réglages | **corrigé** | L'écart du dernier recours, R-4664, est cité (`registres/decisions.md` l. 4803, vérifié) ; la réserve sur le raisonnement d'Astra est au § 13. |
| D-10, forme | **corrigé** | Trois options par décision. L'option (b) de la décision 2 porte deux variantes, mais les deux sont chiffrées et départagées : acceptable. Les noms sont en clair d'abord. |

Ma contre-lecture situait le commit à la ligne 154 de la v8 : c'est la ligne 155 (ligne 153 du texte depuis le titre). La v2 a raison.

## 2. Contre-lecture du programme `produire_version_servie_v1.py` (dad030a2…)

**Rejeu.** La v8 (047eeddf…) n'est pas sur une branche que je peux lire sans risque. J'ai donc reconstruit une v8 témoin : une tête factice qui porte la phrase prescrite, une ligne vide, puis `calculs/servi/question-v8-depuis-le-titre.md` (38a1a8e9…). J'ai lancé une copie du programme dont seule l'empreinte attendue de la v8 change (la même substitution est faite dans une copie scellée de la liste), avec les moteurs révision 8d (b7803838…) et révision 8m (420394f9…).
- Résultat : code 0, tous les contrôles tenus.
- Version servie produite : **b69f6b6d…, identique à celle versée**.
- Le différentiel ne diffère du différentiel versé que par la ligne de tête, ce qui est attendu.

| exigence | jugement |
|---|---|
| Liste fermée | **tenue**. Elle est scellée, et chaque ancien apparaît une seule fois, à la ligne dite. Le programme exige que la liste soit **exactement** ce que dérive la garde, élargie au jeton entier entre accents graves ou à l'identifiant d'accord avec sa suite. Les 16 moteurs doivent trouver les mêmes occurrences. |
| Reconstruction exacte | **tenue**. Remettre les anciens redonne la v8 depuis son titre au caractère près, et la mention est absente de la v8. |
| Différentiel borné | **tenu**. Zone de lignes 77, 78 et 155 à 179. Hors zone, le reste est identique par empreinte (4d5d1563…). Seules diffèrent les 20 lignes porteuses, chacune redonnée par ses seules paires. Les repères sont identiques, aucun reste ne subsiste. Le différentiel unifié se limite à la tête et à ces lignes. La garde est repassée sur les invites du tour de conception. |
| Artefacts (R5) | **tenus en partie**. Six artefacts sont refusés au code 2 sans écriture : paire manquante, paire en trop, identifiant non élargi, sceau faux, v8 altérée, écrasement. Le cas sain est le lancement réel. Voir N-4 pour les contrôles jamais mis en échec. |

## 3. Le commit (v8 l. 155) et le chemin `donnees/` (v8 l. 169)

- **Le commit** (`2cd13d45…`) : c'est l'empreinte d'un état d'un dépôt privé. Il n'identifie rien au-dehors et n'est pas un chemin. Le garder est défendable, et la recommandation (a) aussi.
- **Le chemin `donnees/t05-pilote-v1/taches-pilote-60-v1.json`** : c'est un chemin interne du dépôt, de même nature que les 18 retirés. La garde ne le prend que parce que son expression régulière ne connaît pas le préfixe `donnees/`.
  - Or la condition de GO-2026-11-21-08 est écrite en clair : « aucun chemin interne, aucun nom ». La garde n'est que son instrument.
  - Le garder est donc un petit écart à cette condition. Le devis le présente comme « ce que la garde ne demande pas ». **Il faut le dire comme un écart**, ou le retirer.
  - Ma recommandation : le retirer. Le commit peut suivre, par cohérence, sans enjeu.

## 4. Défauts nouveaux

### N-1 (moyenne) — l'option (b) de la décision 1 est mal décrite

L'option dit : « même programme, deux paires de plus, environ une demi-heure ». Le programme refuse par construction toute paire que la garde ne dérive pas, et l'essai d'artefact « paire en trop » le prouve : c'est justement la paire du commit, refusée au code 2.
- Retirer le commit ou `donnees/` demande donc un programme v2, avec une seconde liste fermée et nommée des retraits hors garde, contrôlée elle aussi.
- C'est une pièce de classe B, à contre-lire, et une porte v6 qui vise une autre empreinte.
- **Correction** : récrire l'avantage et l'inconvénient de (b) dans ce sens ; recompter le délai (environ une à deux heures).

### N-2 (moyenne) — `donnees/` face à GO-2026-11-21-08

Voir § 3. **Correction** :
- dans la décision 1, nommer le maintien de `donnees/` comme un écart à la condition « aucun chemin interne » ;
- revoir la recommandation (ma préférence : (b) réécrite selon N-1) ;
- signaler à part le trou de la garde des moteurs (préfixe `donnees/` absent), à corriger dans une révision future, hors de ce devis.

### N-3 (mineure) — un faux sceau sous un nom ordinaire

`calculs-v3/essais-artefacts-produire-version-servie-v1/d-sceau-faux.json.sha256` porte volontairement des zéros. `sha256sum -c *.sha256` échoue donc dans ce dossier. `verifier-arbre`, rejoué, rend « arbre intact », mais le premier lecteur qui vérifie à la main croira à une altération.
**Correction** : renommer le faux sceau (par exemple `d-sceau-faux.json.sceau-faux-essai`), le programme d'essai étant adapté, ou le dire dans un compagnon lisible.

### N-4 (mineure) — couverture des artefacts et moteurs non fixés

Trois contrôles ne sont jamais mis en échec :
- les restes (contrôle 5e) : l'essai « identifiant non élargi » s'arrête avant, sur l'unicité ;
- la ligne changée hors des paires et le différentiel (5c et 5g) ;
- une garde différente entre deux moteurs.

Les empreintes des moteurs viennent de la ligne de commande et non du programme : le compte rendu les consigne, mais rien ne les fixe. Une structure de liste malformée (TypeError) sort en trace, et non en arrêt nommé.
**Correction** : à reporter en errata de classe B ; rien ne change le texte servi.

### N-5 (mineure) — lisibilité de la mention

Les faits 16 et 17 se lisent désormais « [source 21, ligne de [renvoi interne retiré]] ». Le sens tient, la forme est lourde. C'est sans conséquence pour le service ; à noter pour une version servie suivante.

## 5. Rejeux faits

| rejeu | résultat |
|---|---|
| Programme de la version servie, sur la v8 témoin, moteurs 8d et 8m | code 0 ; texte servi b69f6b6d… identique ; garde à zéro sur le texte et sur les cinq invites du tour de conception (69 908 caractères) |
| `calcul_devis_v8_v3.py`, sur le moteur 8m, le texte servi et `calculs/releve-journaux-v2.json`, dans un dossier neuf | sortie et totaux identiques au versé : attendu 10,58, haut 15,52, pire 40,19 et 99,03, pointe 19,99 ; il n'écrit que dans son dossier de sortie |
| Sceaux de `version-servie/` et de `calculs-v3/` | tous tenus, sauf le faux sceau volontaire (N-3) |
| `verifier-arbre` sur le dossier du service | « arbre intact » |
