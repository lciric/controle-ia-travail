# Vérification des corrections — brouillon 7 de l'additif 1 à la lecture des sondes du barreau 8 (règle R2)

## Verdict

**SCELLABLE EN L'ÉTAT (APRÈS REMPLISSAGE DES SEPT MARQUEURS PAR LA MÈRE)**

- **Horodatage (temps universel coordonné, commande `date -u`)** : `2026-11-23T21:11:23Z`
- **Pièces vérifiées** :
  - brouillon 7 : [`lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-additif-b8/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md) (185 969 octets, SHA-256 `ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`) ;
  - script de correction : [`corrections-brouillon6-vers-brouillon7-v1.py`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-additif-b8/corrections-brouillon6-vers-brouillon7-v1.py) (32 004 octets, SHA-256 `a7af0989f331b547d67ff1e5b3cd14cef23b0e638ceb09cd2dd8c989e7d9160e`).
- **Vérificateur** : même contre-lecteur R2 (`289f9a3a862f39f87ccb565b8aa65125`), modèle Gemini 4 Carbon en effort élevé, mandaté sous `GO-2026-11-23-16`, `GO-2026-11-23-32` et `GO-2026-11-23-33`.

---

## Contrôles exécutés

1. **Rejeu reproductible du script (`EXACT_REPLAY`)** :
   - L'exécution de [`corrections-brouillon6-vers-brouillon7-v1.py`](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/redaction-additif-b8/corrections-brouillon6-vers-brouillon7-v1.py) sur le brouillon 6 (`bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e`) reproduit exactement le brouillon 7 octet pour octet (`ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`).
   - L'inspection complète du différentiel unifié entre le brouillon 6 et le brouillon 7 confirme qu'aucun passage hors du traitement des remarques `M-1` à `M-3`, `m-1` à `m-5` et de la provenance du brouillon 7 n'a été altéré : toutes les règles de report (`RP-1` à `RP-14`), les sondes, les planchers, les seuils, les états, la table des issues, l'audit et la frontière `NL-3` restent intacts.

2. **Traitement des remarques majeures et mineures** :
   - **`M-1` (clés de graines dans `LD-0` point `(g)`, `LD-1`, `LD-2`, `LD-4`)** : **CORRIGÉ**. `LD-0` point `(g)` (ligne 457) définit désormais sans doublon toutes les clés, dont `additif-1/episode/difference/<statistique>/<base>/<sonde>/<jeu>`, `additif-1/reference/<statistique>/<terme>/<surveillant>/<sonde>/<jeu>` (`<terme>` = `surveillant` ou `sonde`) et `additif-1/reference/difference/<statistique>/<surveillant>/<sonde>/<jeu>`. Le tirage exact d'intervalle de rappel et des parts d'alertes sous `<c>-contre-<h>`, `<c>-contre-<j>` et `<j>-contre-<h>` est précisé dans `LD-0` point `(j)` (ligne 460), `LD-1` (ligne 462), `LD-2` (ligne 471) et `LD-4` (ligne 481).
   - **`M-2` (cas limites du rappel à 1 % de fausses alertes et actions communes de `h` dans `LD-4`)** : **CORRIGÉ**. `LD-0` point `(j)` précise le tri décroissant avec répétitions comptées à l'indice 0-basé `k = floor(n / 100)` (`scores_tries[k]`) et renvoie explicitement `n = 0` hors de `τ` à la ligne 27 de la liste d'arrêt (« échec »). `LD-4` (ligne 481) définit explicitement l'ensemble de référence de `h` pour les trois jeux (y compris `<c>-contre-<j>`) comme les actions de `h` ayant au moins un jeton noté et un score fini du surveillant `b`, et la ligne 27 de la liste d'arrêt (ligne 589) est complétée en conséquence.
   - **`M-3` (alignement de provenance et d'agent)** : **CORRIGÉ**. L'en-tête (lignes 5 et 9), la section des changements (lignes 25-39), la table des expositions (lignes 514-515), la déclaration de la chaîne (ligne 548) et l'entrée « Contre-lecture 2 (finale, texte rempli) » (ligne 599) reflètent exactement la chaîne réelle (`289f9a3a862f39f87ccb565b8aa65125` comme contre-lecteur R2 puis vérificateur sous `GO-2026-11-23-16`, `-32` et `-33` ; `a99cfcf7527baf9160bb77d7cb2dca01` comme rédacteur du brouillon 7 sous `GO-2026-11-23-33`).
   - **`m-1` à `m-5`** : **TOUS CORRIGÉS**. L'empreinte historique de `CLAUDE.md` (ligne 16), le renvoi caduc à `NL-7` (ligne 547), le temps de l'inventaire des brouillons 1 à 4 (ligne 521), le développement des sigles techniques dans la prose (en-tête, `D-6`, `D-15`, fiche des champs, `RP-7`, `LD-4`, « Ce qu'il doit éprouver en premier ») et la formulation stricte des trois lieux modifiables au scellement (ligne 121, ligne 18 de la liste d'arrêt ligne 580, et ligne 599) sont tous conformes.

3. **Compatibilité mécanique avec [`src/controle_ia/prereg.py`](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/prereg.py) et [`src/controle_ia/manifeste.py`](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/manifeste.py)** :
   - **Validateur [`problemes`](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/prereg.py#L37-L60)** : sur le brouillon 7 tel quel, retourne uniquement `['section vide ou à remplir : Contre-lecture']` ; exactement **7 marqueurs `À REMPLIR`** demeurent aux emplacements prévus (lignes 153 à 158 pour `AD-1` à `AD-6`, ligne 599 pour `Contre-lecture 2`). En simulant leur remplissage avec les deux empreintes exigées dans `Contre-lecture 2`, `problemes` retourne `[]`.
   - **Générateur de graines [`graines`](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/manifeste.py#L37-L48)** : éprouvé avec l'entropie `F-3` du texte scellé sur un jeu complet de 270 clés distinctes suivant le schéma de `LD-0` point `(g)` (aucun doublon, 270 séquences dérivées sans erreur).

4. **Intégrité du dépôt** : aucune modification ni opération `git checkout` / `commit` / `push` effectuée dans `/home/antigravity/lciric/controle-ia-travail`.

---

## Ligne pour « qui a lu quoi » (mise à jour de vérification)
- **Agent** : même contre-lecteur R2 (`289f9a3a862f39f87ccb565b8aa65125`), Gemini 4 Carbon en effort élevé, mandaté sous `GO-2026-11-23-16`, `GO-2026-11-23-32` et `GO-2026-11-23-33`.
- **Pièces lues en plus lors de cette passe de vérification** : `corrections-brouillon6-vers-brouillon7-v1.py` (`a7af0989f331b547d67ff1e5b3cd14cef23b0e638ceb09cd2dd8c989e7d9160e`) et `lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`).
- **Expositions** : aucune pièce interdite ouverte.
- **Rôles exclus** : lecteur, juge du verdict et auditeur de la lecture des sondes du barreau 8.
