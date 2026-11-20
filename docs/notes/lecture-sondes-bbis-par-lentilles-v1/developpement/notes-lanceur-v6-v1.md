# Notes du développeur — lanceur de la première passe, version 6 : interruptions pendant le traitement d'un arrêt cloisonné — v1

Pièce de travail (classe C) qui accompagne un instrument de classe B. Même développeur que pour la version 5 (sous-agent de la
session des lentilles, `session_01QPDgKhLLz1oJQwPBeB5aFs`, modèle servi Fable 5.2), même mandat
(`mandats/mandat-developpeur-lanceur-v5-messages-arret-v1.md`, `1ba9f15a…`), branche `claude/brave-galileo-jhp684`,
2026-11-20 (UTC). Suit `notes-lanceur-v5-v1.md` (`44895d08…`), qui reste valable pour tout ce que cette version ne change pas.

- Ce qui commande ce travail : la correction 1 de la contre-lecture du lanceur version 5,
  `contre-lectures/contre-lecture-lanceur-v5-messages-arret-v1.md`,
  `d821cf66698537c8649a3b55ffebdf13b321abfd066bbde1d9df1af6aa82be9b` (empreinte recalculée, égale ; lue en entier), et le
  message de la session des lentilles qui me la confie.
- **La seconde passe n'est pas touchée.** Aucune garde n'est ajoutée sur un `arret.json` déjà présent. Les mots fixes de la
  ligne affichée ne changent pas.

## 1. Ce qui change, en mots

`src/controle_ia/lentilles_sondes_bbis/lanceur_v6.py` est `lanceur_v5.py` (`599f4a19…`) plus une seule correction : **une
interruption du clavier qui tombe pendant le traitement d'un arrêt cloisonné n'en porte plus le message dans sa trace.**

Le mécanisme de la fuite : tant qu'un bloc `except` traite un arrêt, toute exception neuve levée dans ce bloc est enchaînée à
l'arrêt, et Python affiche les deux, message compris. La correction tient en trois endroits, ceux que nomme le contre-lecteur :

| où | version 5 | version 6 |
|---|---|---|
| `principal` | la ligne de l'arrêt était calculée et imprimée dans le bloc `except` | le bloc `except` ne fait que retenir l'arrêt dans une variable ; la ligne est calculée et imprimée après, quand aucun arrêt n'est plus « en cours » |
| `calculer` | le tri et le versement se faisaient à nu dans le bloc `except` | ils sont sous un `try` : toute exception qui en sort, interruption comprise, est relevée sans enchaînement (`from None`) |
| `verser_arret_cloisonne` | la première ligne était hors du `try` ; le traitement d'un fichier d'arrêt impossible à écrire avait son propre bloc, hors coupure | tout le corps, première ligne comprise, est sous un seul `try` extérieur, relevé sans enchaînement |

**Mots fixes de la ligne affichée** : inchangés, mot pour mot (un essai compare les quatre lignes à celles de la version 5).
Ils sont maintenant tenus par quatre constantes ; pour n'afficher que le nom de l'arrêt, une seule change :
`LIGNE_ARRET_CLOISONNE = "{nom}"` (un essai le montre). Le nœud reste chez Lazar ; je n'ai rien tranché.

Rien d'autre ne change : aucun autre module (`statistiques_v3.py` : `9a478aa8…`), aucune ligne de calcul, la sortie des autres
arrêts (égale à celle des versions 4 et 5, octet pour octet), `arret.json`, le code de retour, les noms d'arrêt
(`EgaliteDirectionLue`, `EgaliteNulleDecisive`).

**Différence entière** : outil `outils/fabrique-lanceur-v6-v1.py`, sept remplacements exacts, chacun trouvé une fois et une
seule (en-tête ; `MODULES` ; corps de `verser_arret_cloisonne` ; `ligne_d_arret_cloisonne` et ses constantes ; branche de
`calculer` ; deux dans `principal`).

## 2. Ce qui reste exposé, dit sans détour

La correction ferme les fenêtres nommées. **Elle ne peut pas les fermer toutes** : tant que l'arrêt est une exception que
`calculer` relève vers `principal`, il reste des instants où il est « en cours » et où aucun code de ce lanceur ne peut couper
l'enchaînement d'une interruption qui tomberait exactement là :
- dans `principal`, l'instruction unique du bloc `except` (`arret = e`) ;
- dans `calculer`, l'entrée dans le `try` de la coupure, et les deux instructions qui le suivent (`if cloisonne:` puis `raise`) ;
- dans `verser_arret_cloisonne`, l'entrée dans le `try` extérieur ;
- et le temps où l'arrêt remonte de `statistiques_v3` jusqu'à `calculer`, par les fonctions du calcul, qui n'ont pas de bloc
  `except` (là, l'arrêt n'est pas « en cours » : une interruption ne s'y enchaîne pas ; je le note pour être complet).

Ce sont quelques instructions sans appel de fonction ; les fenêtres de la version 5 couvraient, elles, des appels entiers
(le versement, le calcul de la ligne, l'impression). Les essais injectent l'interruption dans les appels ; aucun essai ne peut
la poser sur ces instructions nues, et je ne prétends pas qu'elles soient couvertes. Les fermer demanderait une autre forme
(par exemple : ne plus relever l'arrêt comme une exception jusqu'à la ligne de commande, ou masquer le signal) : c'est un
changement plus large, que je ne fais pas sans mot.

Une interruption qui tombe pendant le versement laisse toujours, comme à la version 5, un versement incomplet et peut-être pas
d'`arret.json` : le message n'est alors écrit nulle part (nœud 2 de la contre-lecture, chez Lazar).

## 3. Essais

- **Fichier neuf** : `tests/test_lentilles_sondes_bbis_lanceur_v6_interruptions_v1.py`, 28 essais. Pour chaque point
  d'injection, les deux arrêts, un cas sain et un artefact (copie jetable, tenue en mémoire, qui remet à cet endroit la forme
  de la version 5 : la trace porte alors le message entier, et le contrôle du cas sain tombe) :

| interruption injectée | cas sain | artefact |
|---|---|---|
| dans `ligne_d_arret_cloisonne` | la trace ne porte que l'interruption | `principal` de la version 5 |
| dans `nom_d_arret_cloisonne`, à son appel de `calculer` | idem | enveloppe de la version 5 |
| dans `nom_d_arret_cloisonne`, à son appel de `principal` | idem | `principal` de la version 5 |
| dans le `print` de `principal` | idem | `principal` de la version 5 |
| entre le versement (fait, `arret.json` écrit) et le relevé, dans `calculer` | idem | enveloppe de la version 5 |
| sur la première ligne de `verser_arret_cloisonne` (appelée seule, sans la coupure de l'enveloppe, puis par la ligne de commande) | idem | première ligne remise avant le `try` |

  S'y ajoutent : les mots fixes et leurs constantes ; la sortie des autres arrêts égale à celle des versions 4 et 5 ; l'outil de
  fabrique rejoué (`lanceur_v6` et les huit copies à l'octet près) ; les lignes de `lanceur_v5` retirées, et l'égalité des
  tranches de calcul.
- **Essais repris**, par le même outil, sous des noms neufs qui visent `lanceur_v6` (deux remplacements de noms) :

| fichier d'origine | copie |
|---|---|
| `tests/lentilles_sondes_bbis_jouets_v5.py` | `tests/lentilles_sondes_bbis_jouets_v6.py` |
| `…_addendum_concentration_v3.py` | `…_addendum_concentration_v4.py` |
| `…_corrections_contre_lecture_v4.py` | `…_corrections_contre_lecture_v5.py` |
| `…_garde_egalite_v2.py` | `…_garde_egalite_v3.py` |
| `…_gardes_non_vues_v4.py` | `…_gardes_non_vues_v5.py` |
| `…_montage_v5.py` | `…_montage_v6.py` |
| `…_procedure_v5.py` | `…_procedure_v6.py` |
| `…_lanceur_v5_v1.py` | `…_lanceur_v6_v1.py` |

  **Seule la dernière copie change de contenu** (table `ACCORDS` de l'outil, six remplacements exacts, et une coupe) : ses
  copies jetables défont des lignes dont la forme a changé à la version 6 ; son artefact de l'interruption retire maintenant les
  deux coupures (celle du versement et celle de l'enveloppe) ; ses deux derniers essais (fabrique rejouée, lignes retirées de
  la version 4) sont retirés de la copie et repris, pour la version 6, dans le fichier neuf. Elle garde 41 essais sur 43.
- **Essais du paquet**, relancés une fois : **1 724 essais, tous verts** (`1724 passed in 981.93s`), dont 311 de plus qu'au rendu de la version 5 : 28 neufs, 41 et 242 repris (`sortie-essais-v6.txt`).
- **Essai des essais** (`outils/essai-des-essais-v5.py`, sortie `outils/sortie-essai-des-essais-v5.txt`) : un témoin sans
  altération, sain ; **dix-sept altérations de `lanceur_v6.py`, une à la fois, dix-sept vues** : les douze de la version 5,
  accordées à la forme de la version 6, et cinq qui défont les corrections de la version 6 (ligne de commande traitée dans le
  bloc `except` ; enveloppe sans coupure ; coupure de l'enveloppe sans `from None` ; première ligne du versement hors du bloc ;
  gabarit de la ligne changé).
- **Non lancée** : la suite complète du dépôt (mandat).

## 4. Ce qui reste ouvert

1. Les fenêtres du § 2 : quelques instructions nues, non fermées, non éprouvables.
2. Les deux nœuds de la contre-lecture, chez Lazar, non tranchés ici : les mots fixes de la ligne affichée (prêts à être
   réduits au nom par une constante) ; le message perdu quand `arret.json` ne peut pas être écrit (aucune garde ajoutée).
3. **Fiche du code et commande de l'opérateur** : la fiche doit porter les treize modules de `lanceur_v6.MODULES`
   (`empreintes-code-v6.txt`, treize premières lignes) ; la commande devient
   `python -m controle_ia.lentilles_sondes_bbis.lanceur_v6`. Avec la liste de la version 5, `lanceur_v6` refuse de partir.
4. `lanceur_v5.py` reste dans le dépôt, inchangé (R12) ; il n'est plus dans la liste des modules de la fiche.
5. Les réserves de `notes-lanceur-v5-v1.md`, § 5, points 3, 5 et 6, inchangées.

## 5. Ce que j'ai lu, expositions, refus d'outil

- **Lu en plus de la version 5** : le rendu du contre-lecteur `d821cf66…`, en entier ; mes propres fichiers.
- **`git pull`** : fait en nommant la branche ; il n'a affiché aucun autre nom de branche.
- **Vu par des noms seulement** : rien de neuf. `verifier-arbre` a été joué avec sa sortie comptée, sans afficher de chemin.
- **Jamais ouvert** : comme à la version 5 (aucun registre, aucune branche de données, de calcul ou de verdict, ni `diag/`,
  `runs/`, `donnees/`, `docs/verdicts/`, aucune table, aucun verdict, aucune clé).
- **Environnement** : celui de la version 5, dans le bloc-notes ; rien d'installé de plus. Aucune machine, aucune dépense.
- **Refus d'outil** : aucun.

## 6. Scellement et empreintes

Pièces scellées de ce dossier : `empreintes-code-v6.txt`, cette note, `sortie-essais-v6.txt`,
`outils/fabrique-lanceur-v6-v1.py`, `outils/essai-des-essais-v5.py`, `outils/sortie-essai-des-essais-v5.txt`. Comme aux versions
précédentes, aucun compagnon `.sha256` n'est posé à côté des fichiers de code et d'essais : `empreintes-code-v6.txt` les porte.
