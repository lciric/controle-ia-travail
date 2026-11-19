# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 7 — note du rédacteur — v1

**En bref.** La version 7 porte les trois défauts à corriger et les huit mineurs de la vérification du code de la version 6, et s'accorde au brouillon 25, qui fait foi. La garde statique n'entre plus dans aucun chemin cloisonné, par défaut et sans moyen de l'y faire entrer. La liste des refus d'une livraison suit celle du texte, ligne par ligne. Une ligne de GO n'ouvre qu'une livraison refaite, liée par un acte de reprise scellé. Le registre des accords n'est lu que s'il porte l'empreinte que la configuration scellée attend. Aucun fichier des versions 4 à 6 n'est modifié. Les cinq choix qui attendent Lazar restent obligatoires, sans valeur par défaut ; aucune issue n'est choisie.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : brouillon 25 (`ab5fc58e…`) et sa note (`3732b6b4…`) ; vérification du code de la version 6 (`4a6e1b41…`) et ses essais d'attaque ; avis du rédacteur du texte (`24f4f9b3…`).
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni de modèle ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun sous-agent. Deux incidents sont déclarés en partie 8.
- **Heure** : 2026-11-19, 17:50Z.

## 1. Fichiers

Sous `src/controle_ia/organismes_discrets/`, chacun avec son compagnon :

| fichier | empreinte | ce qui change depuis la version 6 |
|---|---|---|
| `cloisonnement_bras_a_v7.py` | `b13c99d4fe62fd03470233892efc1969b189d08108262676e0f775065e36c5d1` | élagage par défaut, avant tout parcours ; liens non suivis ; deux formes de noms recollés de plus |
| `arrets_bras_a_v7.py` | `c14dbc88ef90af8ada7a04c6b8f2e55b6ec4542da70e86a14d788b864bf7803d` | six désignations de liste et quatre natures de défaut |
| `configuration_bras_a_v7.py` | `d49d32f60b0248c743fe555cc4f89f5ae81be81c81fda3ea2845654470fd7b09` | nom du fichier fixé ; deux chaînes pour le fichier des scores par unité ; pièces attendues |
| `graines_bras_a_v7.py` | `2930e02e228ae465115c798bc07b8e3c456374f0e93c44839feb52b3867cb5dc` | registre lu sous empreinte attendue ; révocation ; formes de refus entières |
| `analyse_bras_a_v7.py` | `38b0191f2d6853589677c1eb42033eea598ffb6e5c5e44f1a1b4810b7fce15b1` | liste fermée des refus ; acte de reprise ; fichier d'arrêt à cinq champs ; constats rejoués |
| `verdicts_bras_a_v7.py` | `54ebfc8ef959f191c2fe12e4a399d43ac686a39edcc299b9e697cdfa493a6dc8` | `issues` lit le dossier des arrêts et le fichier de l'étape (m) |
| `permutation_etiquettes_bras_a_v7.py` | `b074eb4d69d2728244dc39073f363c957be56797d41251bb00864171faae3820` | imports de la version 7, rien d'autre |
| `mesures_bras_a_v7.py` | `7314b6e61b96ea3a236d578759c03a995fe98a09022f7960b7f920609d4421db` | imports de la version 7, rien d'autre |

Sous `tests/` : `aide_bras_a_v7.py` (`f4c91d8c…`), `test_analyse_bras_a_v7.py` (`d8886a75…`), `test_verdicts_bras_a_v7.py` (`dd3f05e6…`), `test_graines_bras_a_v7.py` (`e16ccad9…`), `test_cloisonnement_bras_a_v7.py` (`a9789d3a…`), `test_permutation_etiquettes_bras_a_v7.py` (`d5f4c976…`), `test_mesures_bras_a_v7.py` (`2bb899e6…`).

**Restent et sont importés tels quels** : `reponses_lecteurs_v5.py`, `instrument_appariement_v4.py`, `epreuves_couverture_bras_a_v3.py`, `fabrication_v3.py`, `graines_bras_a_v4.py`. La chaîne de la version 7 n'importe aucun module des versions 5 et 6 (essai).

## 2. Essais

Commande :

```
PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v7.py tests/test_verdicts_bras_a_v7.py tests/test_graines_bras_a_v7.py tests/test_permutation_etiquettes_bras_a_v7.py tests/test_mesures_bras_a_v7.py tests/test_cloisonnement_bras_a_v7.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
```

**296 essais passent** : 256 de la version 7 (analyse 53, verdicts 27, graines 104, garde statique 54, permutation 9, mesures 9), 36 des réponses des lecteurs, 4 des épreuves de couverture. Toutes les données sont fabriquées dans l'essai. La suite entière n'a pas été lancée.

## 3. C-3 — la garde statique n'entre plus dans les chemins cloisonnés

- **Ce qui est cloisonné, par défaut** :
  - tout dossier nommé `t07…`, `bases` ou `sondes`, à toute profondeur ;
  - tout dossier ou fichier dont le nom porte `mots_et_cout_`, `autres_moniteurs_v` ou `bras_a_v2_habilite` ;
  - tout dossier ou fichier qui porte une marque de T0.8 (`t08`, `t0.8`, `t0_8`, `t0-8`) ;
  - `prereg/T0.6-organismes-v0-v1.md`, et, sous `docs/notes/bras-a-moniteurs-v1/`, les notices, les contre-lectures du code et les vérifications des lots.
- **Comment** : le nom d'une entrée est jugé avant qu'elle soit listée ou ouverte. L'appelant peut ajouter des chemins, jamais en retirer : l'argument `exclus` n'existe plus. Un dossier de départ cloisonné est refusé. Aucun lien symbolique n'est suivi.
- **Rien n'est tu** : `chemins_elagues` rend les noms de ce que la garde n'a pas regardé. Sur le dépôt : quatre dossiers et dix-huit fichiers.
- **Plus large que les préfixes de la vérification** : « tout nom qui porte `mots_et_cout_` » couvre aussi sept fichiers de `scripts/` que la version 6 lisait (bancs, essais et lanceurs de la base « mots et coût »). Dans le doute, la garde n'entre pas. Liste à confirmer.
- **Essai sur un faux dépôt** : dix-huit programmes plantés sous des chemins cloisonnés, huit sous des noms voisins. Un crochet d'audit de Python note chaque fichier ouvert et chaque dossier listé : aucun n'est sous un chemin cloisonné ; les huit voisins sont lus et refusés.
- **Essai sur le vrai dépôt, avec les valeurs par défaut** : le même crochet refuserait toute ouverture d'un chemin cloisonné avant qu'elle ait lieu. Aucune n'est tentée ; aucune violation.

## 4. Le registre des accords — une solution sans réseau

- **Le défaut** : la branche porte un `registres/go.md` en retard sur la branche principale. Une ligne de GO, ou une révocation, peut y manquer.
- **La solution** : la configuration scellée porte l'empreinte du registre de la branche principale au moment où elle est scellée (`pieces_attendues.sha256_du_registre_des_accords`). Le code lit toujours `registres/go.md` du dépôt, et seulement s'il porte cette empreinte.
- **Sinon** : il s'arrête, et dit les deux empreintes et ce qu'il faut faire. Il ne lit jamais un registre périmé, ni en avance, sans le dire.
- **Sans réseau** : le code compare deux empreintes. Qui scelle la configuration sait où est la branche principale ; le code n'a pas à le savoir.
- **`null`** : aucun registre n'est lu sous cette configuration. C'est le cas d'une première livraison, qui ne demande aucune ligne.
- **Conséquence** : une reprise demande une configuration neuve, scellée après la ligne de GO. C'est aussi le moment où le module corrigé peut changer ses chaînes.
- **Après la lecture** : le registre reçoit d'autres lignes, et son empreinte change. La garde de sortie ne le relit donc pas : elle relit l'acte de reprise scellé.
- **En plus** : une ligne de type « révocation » qui nomme le GO le fait refuser.

## 5. Vérification du code de la version 6, point par point

| point | porté | comment |
|---|---|---|
| C-1 valeurs p | oui | écart d'un demi-pas de la grille ou plus : refus ; en deçà, valeur prise telle quelle |
| C-1 formes devinées | oui | `dose` et `condition` lus dans la configuration ; étendues de `episode` et de `pas` retirées |
| C-2 reprise | oui | acte de reprise scellé avant la lecture ; une ligne déjà portée par un acte n'ouvre rien ; aucun plafond |
| C-3 élagage | oui | partie 3 |
| M-1 constats | oui | journal relu par la table A ; trois empreintes comparées |
| M-2 `issues` | oui | l'arrêt se lit dans le dossier ; la table C dans le fichier de l'étape (m) |
| M-3 mot de refus | oui | formes entières ; une ligne qui nomme « la livraison refusée » est admise |
| M-4 fichier d'arrêt | oui | cinq champs ; l'événement qui remonte est refait de son seul constat |
| M-5 ligne de reprise | oui, autrement | la garde de sortie relit l'acte scellé, non le registre |
| M-6 module corrigé | oui, plus large | empreinte du module toujours exigée dans la configuration |
| M-7 contenus tels quels | **écart** | le texte dit « tels qu'ils sont rendus » ; la liste des refus est fermée |
| M-8 garde statique | en partie | `join` d'une compréhension, chaîne de variables, `_generateur` : refusés ; deux limites restent |

**M-5, pourquoi autrement.** Relire la ligne au registre ferait échouer la garde dès qu'une ligne sans rapport y entre. L'acte est écrit par le programme après la lecture de la ligne, et scellé. La garde refuse un résultat qui dit une autre reprise que l'acte, ou une reprise sans acte.

**M-8, ce qui reste.** Un programme qui liste un dossier sans écrire l'extension n'est ni refusé ni signalé ; un nom lu dans la pièce n'est pas vu. Le texte porte maintenant la règle du dossier.

## 6. Brouillon 25, partie 3 de sa note

| points | état |
|---|---|
| 1 à 6, liste fermée | portés ; deux fouilles au hasard : tout refus est l'événement nommé, sous une garde de 8.4 |
| 7 à 9, fichier des scores par unité | portés ; `scores_par_unite.forme` et `.fichier` non lus |
| 10 à 13, livraison refaite | portés ; `compte_des_livraisons` pour le rapport |
| 14 à 17, fichier d'arrêt | portés ; statut lu du choix nommé |
| 18 à 20, autres fichiers | portés, à un écart près : la configuration a une troisième partie |
| 21, dossier | porté ; le fichier est refusé s'il est rangé dans le dossier des arrêts |

## 7. Ce qui reste à faire

1. **Le texte** : les vingt points du relevé `defauts-du-texte-trouves-en-codant-v7.md`. Deux touchent la conséquence d'une règle.
2. **La session principale** : confirmer la liste des chemins cloisonnés ; dire si `lectures` est une liste ou une table ; donner l'arrondi des valeurs p.
3. **L'enchaînement de l'analyse**, non écrit : il nomme le dossier des arrêts, remet `listages_a_relire` et `chemins_elagues` à son contre-lecteur, et ne tire d'une exception que `constat()`.
4. **L'épreuve de forme** du module réel, avant toute dépense.

## 8. Réserves

1. **Un fichier parasite créé puis retiré dans `prereg/`.** Une commande de lecture mal écrite a créé un fichier de quatre octets, au nom fait d'une ligne du brouillon. Je l'ai supprimé. Aucun fichier existant n'a été touché ; `git status` ne montre aucun changement suivi.
2. **Des compagnons refaits.** J'ai scellé, puis corrigé sept de mes fichiers de la version 7, en supprimant leur compagnon pour le refaire. Ces compagnons étaient les miens, non committés.
3. **Le demi-pas de la grille** suppose des valeurs p rendues à quatre décimales au moins.
4. **La troisième partie de la configuration** est de moi ; le texte dit deux.
5. **L'acte de reprise scelle contre la mégarde, non contre la fraude** : qui écrit un acte à la main et le scelle passe la garde de sortie.
6. **Les deux formes de `lectures`** sont lues faute de savoir laquelle le module rend.
7. **Le crochet d'audit des essais** ne se retire pas d'un processus ; il dort hors des essais qui l'allument.

## 9. Fichiers ouverts pour la version 7

- La vérification du code de la version 6, en entier ; ses pièces : quatre programmes d'attaque et leurs sorties, et la sortie seule de `attaques_regle_v6`.
- L'avis du rédacteur du texte, en entier ; la note du brouillon 25, en entier.
- Le brouillon 25 : les seules lignes qui diffèrent du brouillon 24 ; le brouillon 24, pour la comparaison et deux recherches.
- Mes fichiers de la version 6, sous `src/` et `tests/`.
- `registres/go.md` : l'en-tête et ses trois premières lignes, pour la forme d'une ligne.
- Des listes de noms seuls : `src/controle_ia/`, `scripts/`, `prereg/`.
- Par programme (la garde statique) : le code de `src/` et de `scripts/`, hors des chemins cloisonnés ; il n'en sort que des noms et des comptes.
