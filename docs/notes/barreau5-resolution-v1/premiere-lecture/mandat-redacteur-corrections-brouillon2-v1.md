# Mandat du rédacteur Fable 5.2 des corrections du texte de la première lecture (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 15:30Z. Pièce de travail : elle dit quoi lire, quoi faire et quoi rendre, sans rien concevoir.

---

Tu es un rédacteur (Claude Fable 5.2) du programme de contrôle boîte blanche, dépôt `/home/user/controle-ia-travail`. Tu écris une pièce de conception décisive (classe A) : le brouillon 2 du texte neuf de la première lecture, « validité de l'adaptateur pour les sondes apprises sur la tâche ». Tu appliques pour cela la contre-lecture du brouillon 1. Un autre modèle (Claude Opus 5.5) vérifiera tes corrections. Français, mots en clair, identifiants en appui seulement. Aucune dépense, aucun lancement sur carte, aucun commit.

## Pièces
Vérifie d'abord chaque empreinte : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement verifier <fichier>`.
- **Brouillon 1 :** `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md` (c5cd9259…).
- **Contre-lecture par Opus 5.5 :** `docs/notes/barreau5-resolution-v1/premiere-lecture/contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md` (13bde378…), avec ses outils dans `contre-lecture-outils-v1/` (même dossier). Verdict : « scellable après ces corrections exactes », 3 bloquantes, 10 majeures, 16 mineures.
- **Autour, dans le même dossier :** `noeuds-restants-v1.md`, `devis-relecture-meme-chemin-v1-brouillon1.md`, `pieces/`.
- **Dans `registres/go.md` :** la ligne `GO-2026-11-19-62` et celles qui portent sur ce texte.
- Ce que le brouillon 1 cite peut s'ouvrir quand une correction l'exige.

## Travail
1. **Applique chaque correction de la contre-lecture.**
   - Quand elle donne un couple exact « avant → après », applique-le à la lettre.
   - Quand elle demande d'écrire quelque chose, écris-le toi-même, et dis-le dans la table : c'est de la conception.
   - Si tu juges une correction fausse, ne l'écarte pas en silence. Écris pourquoi dans la table ; laisse le texte tel quel, ou propose une autre rédaction marquée « à trancher par le vérificateur ».
2. **Ne change rien d'autre** que ce qu'une correction exige. Tout autre changement va dans la table, sous « hors correction », avec sa raison.
3. **Le devis :** si la contre-lecture demande de le reprendre, écris-en le brouillon 2.
4. **Les nœuds pour Lazar :** si une correction change un nœud ou en ajoute un, écris `noeuds-restants-v2.md`.

## Sorties (noms neufs, R12 ; chacune scellée par `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement sceller <fichier>` ; non commises)
- `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md`.
- `docs/notes/barreau5-resolution-v1/premiere-lecture/table-corrections-brouillon2-v1.md`. Une ligne par correction, avec :
  - son repère dans la contre-lecture ;
  - sa classe (bloquante, majeure, mineure) ;
  - son mode : « appliquée à la lettre », « écrite par le rédacteur » ou « non appliquée, raison » ;
  - où elle se trouve dans le brouillon 2.

  Puis la liste des changements « hors correction ».
- Seulement si nécessaire, dans le même dossier : `devis-relecture-meme-chemin-v1-brouillon2.md` et `noeuds-restants-v2.md`. Tout outil neuf prend un nom neuf.

Avant d'écrire un fichier, vérifie qu'il n'existe pas ; ne réécris jamais un fichier déjà scellé.

## Vérification qui suivra
Le contre-lecteur d'origine est resté sur un autre compte : il n'est pas joignable. Un agent Opus 5.5 neuf vérifiera tes corrections à partir de la table, de la contre-lecture et de la différence entre les deux brouillons. C'est un écart déclaré à la règle « vérification par le même contre-lecteur ». Écris la table pour qu'un lecteur neuf vérifie chaque ligne sans rien deviner.

## Interdits
- **N'ouvre jamais :**
  - un fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
  - `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059 ;
  - les notes « pour Lazar seul » ;
  - le fichier des scores par unité du bras A ;
  - les valeurs des deux booléens d'aiguillage du texte scellé de validité, où qu'elles soient écrites ;
  - rien sous `/root/.claude/`.
- **R1 :** n'ouvre aucun fichier des scores fermés que ce texte doit lire ; aucune lecture de résultat avant scellement.
- **Recherches :** pas de recherche plein texte sur tout le dépôt. Limite-toi aux dossiers nommés ici, en excluant les motifs interdits, par exemple `grep -r --exclude='*consigne-privee*' --exclude='*conception-ii-b*' --exclude-dir='ii-b-saboteur-budget-v1' …`. Si une recherche fait apparaître un fichier interdit, ne l'ouvre pas et signale-le.
- **Exécution :** ne lance pas la suite complète des essais. Aucune commande `rm` sur un chemin construit par variable.
- **État de l'art :** aucun chiffre sans page de PDF vérifiée (R7) ; aucune zone déclarée libre (R8).
- **Refus d'outil :** au premier refus, arrête-toi et dis-le, sans le contourner.
- **Écriture :** écris sur disque tôt et souvent, car la limite d'usage de Fable peut t'arrêter. Scelle chaque sortie quand elle est finie.

## Rends
1. La phrase exacte de ton invite système qui nomme le modèle qui te sert.
2. Les chemins et empreintes de tes sorties.
3. Dix lignes au plus :
   - les corrections appliquées, par classe et par mode ;
   - ce que tu as écrit toi-même ;
   - ce que tu n'as pas appliqué, et pourquoi ;
   - ce qui change au devis et aux nœuds.
4. La liste des fichiers et des dossiers que tu as ouverts, une ligne chacun (registre de « qui a lu quoi »).
