# Notes du développeur — lanceur de la première passe, version 7 : garde du fichier d'arrêt déjà présent — v1

Pièce de travail (classe C) qui accompagne un instrument de classe B. Même développeur que pour les versions 5 et 6
(sous-agent de la session des lentilles, `session_01QPDgKhLLz1oJQwPBeB5aFs`, modèle servi Fable 5.2), même mandat
(`mandats/mandat-developpeur-lanceur-v5-messages-arret-v1.md`, `1ba9f15a…`), branche `claude/brave-galileo-jhp684`,
2026-11-21 (UTC). Suit `notes-lanceur-v5-v1.md` (`44895d08…`) et `notes-lanceur-v6-v1.md` (`26e41a2d…`), qui restent valables
pour tout ce que cette version ne change pas.

- Mot qui fonde ce travail : GO-2026-11-21-06 (« go recos »), rapporté par la session des lentilles ; je n'ai ouvert aucun
  registre. Il tranche les deux nœuds de la contre-lecture `d821cf66…` : les mots fixes de la ligne affichée sont gardés tels
  quels ; une garde neuve refuse de partir si un `arret.json` existe déjà.
- Lu avant de commencer : `contre-lectures/verification-correction-lanceur-v6-v1.md` (`23f466a8…`, en entier).
- **La seconde passe n'est pas touchée.**

## 1. Ce qui change, en mots

`src/controle_ia/lentilles_sondes_bbis/lanceur_v7.py` est `lanceur_v6.py` (`e0517259…`) plus une seule garde.

**La garde** (`exiger_aucun_fichier_d_arret`) : au départ de la sous-commande `calcul`, si un fichier existe déjà au chemin où
l'arrêt de cette course serait écrit, `<sortie>/versement/<run>/calcul-interrompu/arret.json`, le lanceur s'arrête.

| question | réponse |
|---|---|
| quand | première instruction de `calculer`, avant l'enveloppe : avant la lecture de la fiche du code et de tout registre, avant toute requête, tout chargement, tout calcul, et avant `etat["parti"]` |
| ce qui compte comme « existe » | un fichier, même vide, ou un lien symbolique, même cassé (l'écriture « sans écraser » de `arret.json` échouerait dans les deux cas) |
| ce qui est écrit ou supprimé | rien : le disque est égal avant et après, octet pour octet (essai) |
| le message | `ARRÊT : un fichier d'arrêt existe déjà pour cette course (<chemin>) : rien ne part ; rien n'est écrit, rien n'est supprimé`, code de retour 3 |
| sa sorte | un arrêt ordinaire (`Arret`), non cloisonné : son message ne porte que le chemin et sort comme celui des autres arrêts |

Pourquoi ce chemin : sans la garde, un second arrêt dans le même dossier de sortie ne pouvait pas écrire son message (R12 : on
n'écrase pas), et un arrêt cloisonné ne le sort nulle part ailleurs. Avec elle, ce second arrêt n'a pas lieu.

Le chemin gardé est le même pour un arrêt cloisonné et pour un arrêt ordinaire versé après le départ : la relance est refusée
dans les deux cas (essais). Un `arret.json` d'une autre course (autre identifiant) dans le même dossier de sortie ne gêne pas.

**Rien d'autre ne change** : les mots fixes de la ligne affichée (gardés tels quels, mot de Lazar), les noms d'arrêt
(`EgaliteDirectionLue`, `EgaliteNulleDecisive`), les coupures de la version 6, `arret.json`, aucun autre module
(`statistiques_v3.py` : `9a478aa8…`), aucune ligne de calcul. Sans fichier d'arrêt présent, les sorties sont celles de
`lanceur_v6`, octet pour octet (essai).

**Différence entière** : outil `outils/fabrique-lanceur-v7-v1.py`, quatre remplacements exacts, chacun trouvé une fois et une
seule (en-tête ; `MODULES` ; les deux fonctions de la garde, posées avant `calculer` ; son appel et une phrase de la docstring
de `calculer`). Deux lignes de `lanceur_v6` sont retirées (la ligne des modules, la fin de cette docstring) ; quatorze lignes
de code sont ajoutées hors de l'en-tête.

**La défense du versement reste** : si un `arret.json` apparaissait après la garde (entre le départ et l'arrêt), la ligne de
commande dirait toujours « fichier d'arrêt non écrit », sans un mot du message. Aucun chemin ordinaire n'y mène plus.

## 2. Nœuds : chemins voisins que je n'ai pas gardés

Le message qui me confie ce travail demande de ne pas ajouter d'autre chemin moi-même. Voici ceux que j'ai vus ; **aucun n'est
gardé par `lanceur_v7`**.

1. **Le dossier `calcul-interrompu` présent sans `arret.json`**, ou portant déjà des archives `lectures-interrompues-non-lues-NNN.npz`
   (cas : une interruption pendant un versement d'avant). Le calcul part. S'il s'arrête, l'écriture des archives échoue (R12) :
   pour un arrêt cloisonné, `arret.json` est quand même écrit, avec le message entier et la raison de l'échec, et la ligne dit
   « versement à l'arrêt en échec » ; les tableaux de cette seconde course ne sont pas versés. Le message n'est pas perdu.
2. **Le dossier `<sortie>/versement/<run>/travail-arret` présent** (versement du dossier de travail d'un arrêt d'avant, sans
   `arret.json`) : même effet que le point 1, par l'inventaire du travail.
3. **La sous-commande `montage`** : elle ne lève aucun arrêt cloisonné et n'écrit pas d'`arret.json` ; elle refuse déjà de
   partir si le dossier de travail existe. Je ne vois pas de message à y perdre. Une garde y serait une règle de conduite
   (ne pas remonter sous un identifiant de course déjà arrêté), non une protection du message.
4. **Un `arret.json` apparu après la garde** (autre processus sur le même dossier de sortie) : défense du § 1, sans garde.
5. **Après un refus de la garde, que fait l'opérateur ?** Le message dit ce qui est, non quoi faire. Relancer demande un
   identifiant de course neuf ou un dossier de sortie neuf ; or le montage est lié à l'identifiant (le rapport du montage est
   cherché sous `diag/<run>/`). La consigne à l'opérateur n'est pas de mon ressort ; je la signale.

Recommandation, si elle est utile : ne rien garder de plus pour les points 1 à 4 (aucun message n'y est perdu) ; écrire la
consigne du point 5 dans le mandat de l'opérateur. Confiance bonne pour 1 à 3, moyenne pour 5 (je ne connais pas ce mandat).

## 3. Fenêtres résiduelles de la version 6 : précision du contre-lecteur

`notes-lanceur-v6-v1.md`, § 2, déclarait quelques instructions nues, hors coupure, où une interruption du clavier resterait
enchaînée à l'arrêt en cours. Le contre-lecteur précise (`23f466a8…`, § 4, point 4), et je reprends sa précision telle quelle,
sans l'avoir établie moi-même : **sur CPython 3.13, une interruption n'est pas délivrée dans ces fenêtres.** CPython ne lève
une interruption du clavier qu'à l'entrée d'une fonction, sur un saut arrière ou à la fin d'un appel ; une interruption qui
arrive pendant ces instructions attend donc le point suivant, qui est couvert. Réserve du contre-lecteur : cela tient au
fonctionnement de CPython, non à une garantie du langage, et cède sous un traceur actif (`sys.settrace`), que l'opérateur
n'emploie pas. Les essais du paquet tournent sous Python 3.13.18. La version 7 n'ajoute aucune fenêtre : la garde est levée
hors de tout bloc `except`.

## 4. Essais

- **Fichier neuf** : `tests/test_lentilles_sondes_bbis_lanceur_v7_garde_arret_present_v1.py`, 19 essais.

| garde éprouvée | cas sain | artefact |
|---|---|---|
| sans `arret.json`, le calcul part | dossier de sortie absent, vide, dossier `calcul-interrompu` sans `arret.json`, `arret.json` d'une autre course | — |
| avec `arret.json`, refus avant toute requête, sans rien écrire ni supprimer | fichier plein, fichier vide, lien cassé ; la fiche du code, les registres, les entrées et les écritures sont piégés : aucun appel ; disque égal avant et après | copie jetable sans l'appel de la garde : le calcul part, le contrôle du refus tombe |
| relance après un premier arrêt cloisonné, même dossier de sortie | les deux arrêts : la seconde course refuse, le premier `arret.json` et le versement restent tels quels, aucun mot du premier message ne sort | copie jetable sans la garde : la seconde course repart, « fichier d'arrêt non écrit », le contrôle tombe |
| la même relance, calcul entier sur le monde miniature | première course arrêtée par une égalité d'une direction lue (déclarée par la garde d'égalité elle-même) ; seconde course refusée avant toute lecture | (les deux copies ci-dessus) |

  S'y ajoutent : le chemin gardé égal au chemin où l'enveloppe écrit ; le refus vu par l'appelant Python (un `Arret`
  ordinaire) ; la relance après un arrêt ordinaire ; les sorties égales à celles de `lanceur_v6` sans fichier d'arrêt ; l'outil
  de fabrique rejoué à l'octet près ; les lignes retirées et ajoutées.
- **Essais repris**, par le même outil, sous des noms neufs qui visent `lanceur_v7` : neuf fichiers.

| fichier d'origine | copie |
|---|---|
| `tests/lentilles_sondes_bbis_jouets_v6.py` | `tests/lentilles_sondes_bbis_jouets_v7.py` |
| `…_addendum_concentration_v4.py` | `…_addendum_concentration_v5.py` |
| `…_corrections_contre_lecture_v5.py` | `…_corrections_contre_lecture_v6.py` |
| `…_garde_egalite_v3.py` | `…_garde_egalite_v4.py` |
| `…_gardes_non_vues_v5.py` | `…_gardes_non_vues_v6.py` |
| `…_montage_v6.py` | `…_montage_v7.py` |
| `…_procedure_v6.py` | `…_procedure_v7.py` |
| `…_lanceur_v6_v1.py` | `…_lanceur_v7_v1.py` |
| `…_lanceur_v6_interruptions_v1.py` | `…_lanceur_v7_interruptions_v1.py` |

  **Deux copies changent de contenu**, et l'outil le porte en clair :
  - `…_lanceur_v7_v1.py` : un essai accordé, `test_echec_du_versement_reel_second_arret_dans_le_meme_dossier_de_sortie`. Il
    relançait le calcul sur un `arret.json` déjà présent, ce que la garde refuse désormais. Sa copie met la garde de côté pour
    garder l'épreuve de la défense du versement (§ 1) ; la relance elle-même est éprouvée dans le fichier neuf.
  - `…_lanceur_v7_interruptions_v1.py` : ses deux derniers essais (fabrique rejouée, lignes retirées de la version 5) sont
    retirés et repris, pour la version 7, dans le fichier neuf. Elle garde 26 essais sur 28. Sa constante `OUTIL`, qui nomme
    encore l'outil de la version 6, n'y sert plus à rien : je la laisse, la copie étant mécanique.
- **Essais du paquet**, relancés une fois : **2 052 essais, tous verts** (`2052 passed in 878.30s`), dont 328 de plus qu'au rendu de la version 6 : 19 neufs, et 309 repris (41, 26 et 242) (`sortie-essais-v7.txt`).
- **Essai des essais** (`outils/essai-des-essais-v6.py`, sortie `outils/sortie-essai-des-essais-v6.txt`) : un témoin sans
  altération, sain ; **vingt-deux altérations de `lanceur_v7.py`, une à la fois, vingt-deux vues** : les dix-sept de la version
  6, et cinq qui touchent la garde (non appelée ; autre chemin ; lien cassé non vu ; fichier supprimé au lieu du refus ; garde
  appelée après le calcul).
- **Non lancée** : la suite complète du dépôt (mandat).

## 5. Ce qui reste ouvert

1. Les nœuds du § 2.
2. **Fiche du code et commande de l'opérateur** : la fiche doit porter les treize modules de `lanceur_v7.MODULES`
   (`empreintes-code-v7.txt`, treize premières lignes) ; la commande devient
   `python -m controle_ia.lentilles_sondes_bbis.lanceur_v7`. Avec la liste de la version 6, `lanceur_v7` refuse de partir.
3. `lanceur_v4.py`, `lanceur_v5.py` et `lanceur_v6.py` restent dans le dépôt, inchangés (R12) ; les essais leur comparent la sortie.
4. Les réserves de `notes-lanceur-v5-v1.md`, § 5, points 3, 5 et 6, inchangées (champs ajoutés à `arret.json` ; arrêt visible
   en entier pour un appelant Python ; ce que les jouets ne prouvent pas).

## 6. Ce que j'ai lu, expositions, refus d'outil

- **Lu en plus** : la vérification `23f466a8…`, en entier ; mes propres fichiers.
- **`git pull`** : fait en nommant la branche ; il n'a affiché aucun autre nom de branche. Tête : `06d199ca`.
- **Vu par des noms seulement** : rien de neuf. `verifier-arbre` a été joué avec sa sortie comptée, sans afficher de chemin.
- **Jamais ouvert** : aucun registre, aucune branche de données, de calcul ou de verdict, ni `diag/`, `runs/`, `donnees/`,
  `docs/verdicts/`, aucune table, aucun verdict, aucune clé.
- **Environnement** : celui de la version 5, dans le bloc-notes ; rien d'installé de plus. Aucune machine, aucune dépense.
- **Refus d'outil** : aucun.

## 7. Scellement et empreintes

Pièces scellées de ce dossier : `empreintes-code-v7.txt`, cette note, `sortie-essais-v7.txt`,
`outils/fabrique-lanceur-v7-v1.py`, `outils/essai-des-essais-v6.py`, `outils/sortie-essai-des-essais-v6.txt`. Comme aux versions
précédentes, aucun compagnon `.sha256` n'est posé à côté des fichiers de code et d'essais : `empreintes-code-v7.txt` les porte.
