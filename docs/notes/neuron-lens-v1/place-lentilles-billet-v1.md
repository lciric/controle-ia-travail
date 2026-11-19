# Place des lentilles dans le billet « Linear probes on an instructed saboteur » — proposition en une page — v1

Session des lentilles, 2026-11-19 (vers 09:50 UTC, `date -u` en pied). Demande de la mère après le dégel (GO-2026-11-19-28 : « degele les
lentilles quand meme, elles pourraient entrer dans le billet »). Billet : `docs/notes/billet-nul-avec-controle-positif-v1/billet-premiere-version-en-v2.md`
(branche principale) ; règle de Lazar R-2716 (2) : l'étape B bis n'y entre que si son verdict est scellé au plus tard le dimanche 22 novembre.
**Proposition seulement** : rien n'entre dans le billet sans nœud de Lazar ; rien n'est dépensé sans ligne de calcul.

## Ce que les lentilles peuvent y apporter, en quatre pièces

| | ce que ça montrerait au lecteur du billet | données | coût, délai | préenregistrement neuf ? | lecture d'un résultat non scellé ? |
|---|---|---|---|---|---|
| **1. Paragraphe de méthode : nos lentilles sur le même modèle** | qu'une lentille ajustée par nous sur Llama 3.1 8B Instruct refait une partie de la lecture publiée : elle devance la lentille des logits dans la première moitié du réseau (écart minimal 0,287 pour 0,20 exigé) et lit côté entrée (0,817 pour 0,60) ; mais sa stabilité entre moitiés du corpus et la lecture contre pilotage manquent de peu à quelques couches → verdict « partiel » ; c'est la limite d'outil que le billet doit dire avant toute lecture de sonde par lentille | **déjà versées et scellées** : `lecture-b-beta/verdict-b-beta-v1.md` (`3a9b947e…`), accepté par Lazar (`accord-lazar-verdict-b-beta-v1.md`, `8469add5…`) ; pièces de course `diag/20261118-164930-neuron-lens-b-beta/` | 0 USD ; rédaction, < 1 h | **non** | **non** (verdict scellé et accepté) |
| **2. Lecture des directions des sondes de l'étape B bis par la lentille publique** | vers quels jetons de sortie poussent les directions des sondes apprises sur la tâche et des lecteurs honnêtes (couches 7, 15, 23), contre deux nuls calibrés ; descriptif : peut ajouter un soupçon sur une sonde (par exemple une direction qui pousse vers des mots de coût ou de forme), jamais la blanchir | sondes de l'étape B bis (`donnees/t07-etape-b-bis-v2`, E-1 et E-2), ouvertes par programme seulement **après** le verdict de l'étape B bis — scellé le 19 vers 01:01Z (`1561399a…`, état de la mère) ; lentille publique `neuronpedia/jacobian-lens` téléchargée | 0 USD (processeur d'une session neuve) ; ≈ 1 jour de code par un développeur neuf (module `lentilles_sondes_bbis`, essais R5, contre-lecture) puis 1 à 2 h de calcul (pire 6 h) et une lecture ; **faisable avant le 22 si le chantier s'ouvre aujourd'hui** | **non** : texte déjà scellé (`prereg/lecture-sondes-bbis-par-lentilles-v1.md`, `ca5066d7…`) ; manquent les lignes GO, CODE, MONTAGE, ENTRÉES du registre propre | **non** : l'opérateur ne lit que codes d'arrêt et empreintes ; le lecteur neuf lit les tables fermées après `VERDICT-BBIS` scellé |
| **3. La même lecture avec nos lentilles R (et S côté entrée)** | si la lecture des sondes tient d'une lentille à l'autre (publique contre la nôtre) — la robustesse que le texte scellé déclare non mesurée (nœud N10, « Frontière ») ; S ajouterait quels jetons d'entrée activent la direction | lentilles à **réajuster** (elles n'existent plus) ; mêmes sondes | réajustement : devis v2 (`devis-reajustement/devis-reajustement-lentilles-b-beta-v2.md`, `49dcbc93…`) ≈ 28,5 à 31,6 USD attendus (plafond 54 ou 62), ≈ 12 à 13 h de machine, plus ≈ 1 jour de préparation (code de copie, commande v9, critère d'identité, contre-lectures) ; puis la lecture au processeur | **oui** : version neuve du texte de lecture (lentilles ajoutées, critère d'identité), contre-lue ; et le critère d'identité scellé | **non** si l'ordre est tenu ; la seconde mesure de la variante B passe par un lecteur neuf |
| **4. Lecture par lentille des sondes du saboteur à budget ou du barreau 8** | même question sur les sondes de l'entretien | sondes de ces courses, quand leurs verdicts seront scellés | 0 USD avec la lentille publique ; délai lié à ces courses | **oui** (texte neuf par chaîne) | non, après leurs verdicts |

## Recommandation
- **Pièce 1 maintenant**, comme limite d'outil dans « Limits » ou « What comes next » (quelques phrases ; chiffres repris du verdict
  scellé, chemin et empreinte au registre des affirmations du billet). Confiance 0,7.
- **Pièce 2 en priorité** pour la section ETAPE_B_BIS : c'est la seule lecture par lentille déjà préenregistrée, gratuite et faisable avant
  le 22 ; elle demande à la mère d'ouvrir aujourd'hui la session neuve du développeur (et ensuite celle de l'opérateur), et la clé
  Hugging Face gardée dans la configuration de son environnement (N8). Confiance 0,6 sur le délai.
- **Pièce 3 après le billet**, ou dans le billet seulement si le devis est choisi aujourd'hui et que la pièce 2 est finie : le chemin
  critique (réajustement 13 h + préparation + texte neuf + lecture) passe le 22 au mieux de justesse. Confiance 0,7 que la pièce 3 ne tient
  pas avant le 22.
- **Pièce 4** : hors billet ; à proposer après les verdicts de l'entretien.

## Ce que cela n'affirme pas
Une lentille lit ce qu'une direction **pousse en moyenne** sur la sortie, pas ce qu'une sonde « détecte » dans un épisode (texte gelé de la
tranche). Aucune pièce ci-dessus n'explique le nul de P3 ni ne valide une sonde ; le verdict « partiel » limite la confiance dans toute
lecture par **nos** lentilles aux couches où la stabilité tient.

Écrit le 2026-11-19T09:41:04Z (`date -u`).
