# Rapport du préparateur — course de l'atelier d'idées sur la question « Regard ou raisons » — v1

Préparateur neuf, sous-agent de la session mère, 14 novembre 2026, de 09:18 à 09:49 UTC (heures relevées par `date -u`).
Demande : registre, R-2679 (point 3), R-2680 ; modèle suivi au plus près : la préparation « conception propre »
(`docs/notes/organisme-conception-propre-v1/`). **Aucune course, aucun appel de modèle, aucun appel réseau, aucune dépense ;
aucune valeur de clé lue ; rien commité, rien poussé ; `.claude/` lu, non modifié ; clone de l'orchestrateur lu, resté
propre** (fichiers ignorés compris, vérifié après chaque passage). Aucun refus de permission, de classifieur ou de crochet.
Non ouverts : `bilan-mere-v1.md`, le dossier `collisionneur-v1/` apparu pendant la préparation, les fiches et le dossier
de run de la course précédente, ses dossiers `lecture-*`.

Dans ce texte, « modèle A » et « modèle B » sont les deux modèles de Claude de la course (proposeurs ; le juge de
l'organisme est du modèle A), comme dans les pièces de la course précédente.

## Verdict

**Préparation rendue ; la course peut partir après deux gestes** : la contre-lecture du lanceur par un autre modèle, que
R-2682 exige (le différentiel fait 252 lignes, dont 69 lignes de code), et la lecture par la mère de la question servie.
**Pire cas 17 USD** (21 pour la course précédente), **attendu ≈ 5,5 USD** ; la ligne **GO-2026-11-14-01** (25 USD), inscrite
par la mère pendant la préparation, est trouvée seule par le lanceur. Essais : **151 passés** ; banc : **61 mutants tués
sur 61**.

## 1. Pièces (toutes scellées ; empreintes SHA-256)

Dossier : `docs/notes/regard-ou-raisons-confondants-v1/organisme-v1/`, sauf mention.

| Pièce | Empreinte |
|---|---|
| `question-organisme-regard-ou-raisons-v1.md` (servie ; épinglée dans le lanceur) | `2c19b11c8b50be23e3d784612914253f9b46c4c6162c03561887079e32a6544d` |
| `../faits-v1.md` (servis tels quels, par leur chemin ; non copiés, non modifiés) | `8708619040b1483a97d33bd5dc3576d083656a3a7c29a8b273b0944e964e6642` |
| `temoins-organisme-regard-ou-raisons-v1.json` (juge de l'organisme seul ; épinglé) | `b585464363989d02da36b804bd2fe2bd7254a76c463fc08d19c13e75d68c876f` |
| `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` | `3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f` |
| `tests/test_lancer_course_ideation_regard_ou_raisons_v1.py` | `509fc85d05faadefbd3137457065bc288e9f240cebce1504a28a03f3e85d0bd8` |
| `differentiel-lanceur-conception-propre-v1-vers-regard-ou-raisons-v1.diff` | `411b7dd2e9052fc42d8619ccd0e747351884ad83b51c6c93e94102aa91285e46` |
| `differentiel-essais-conception-propre-v2-vers-regard-ou-raisons-v1.diff` | `2ccc7c6f4537607802d199a8e7b3d702a5dbbd8b16ca61ca533f4c600ff8bedb` |
| `devis-v1.md` | `1d9628bc42dbf261d83f15788171a7a2e1b4c85d6468f7032ab9aae77f6c9c6b` |
| `outils/mutations_lanceur_regard_ou_raisons_v1.py` ; son résultat `outils/resultat-mutations-lanceur-regard-ou-raisons-v1.json` | `2974ad06…` ; `204f8ded9e25c2be81fcdb5d34cbd56b42b86ce94b5c4757e3228bc96a516b91` |
| `outils/resultat-essais-lanceur-regard-ou-raisons-v1.txt` | `d7546da19f978278bd7d88db71851fa32947a68b920db260b372c1075e489a27` |
| `outils/valider_pieces_v1.py` ; son résultat `outils/resultat-valider-pieces-v1.txt` | `d69a4aa7…` ; `8ce6207e…` |
| `outils/mesure-consignes-sans-appel-v1.json` ; `outils/gardes-de-taille-et-de-somme-v1.json` | `d9e31d6b…` ; `411131f5…` |

Rien de la course précédente n'est modifié (lanceur toujours à `709cf1c7…`, compagnon vérifié).

## 2. Ce qui est servi, et à qui

- **La question de l'organisme**, aux proposeurs et au juge. Le fond de `question-v1.md` (`f0481482…`) y est recopié
  **octet pour octet** : le bloc entre guillemets, 2 418 caractères, vérifié par programme (`outils/valider_pieces_v1.py`,
  et un essai du lanceur). Autour de ce bloc, j'ai ajouté de la forme seulement :
  - quatre leviers, une étiquette par fiche : `levier:phenomene` (famille a), `levier:instrument` (famille b),
    `levier:mesure` (famille c), `levier:papier` (Partie B) ; trois étiquettes facultatives (`signature-positive`,
    `duel-decisif`, `episodes-deja-joues`) ;
  - la répartition des cinq points de la « forme de la réponse » dans le gabarit de fiche de l'orchestrateur : une fiche de
    la Partie A porte une seule explication rivale ; une fiche de la Partie B porte une forme de papier entière, en six
    conseils au plus, deux fiches de ce genre au plus par passe ; une fiche au moins dit la signature positive de
    « raisons », une au moins porte le duel décisif ; les points (1) et (5) vont dans les champs `perte_traduction` et
    `cosmetique_si` ;
  - quatre bornes tirées de la question et du filtre des faits (rien au-delà du mesuré, adaptateurs publiés d'abord, aucun
    texte de scénario ni phrase à servir à un modèle, une fiche propose et ne décide rien) ;
  - une **contrainte d'écriture** (nœud N2) : le filtre lexical de l'orchestrateur met en quarantaine toute fiche qui
    contient certains mots ou formes, dont la famille d'« exfiltrer », que les faits emploient pour décrire un scénario ;
  - la manière dont les fiches seront lues : bilan scellé avant toute lecture, croisé ensuite par un lecteur neuf, notes du
    juge de l'organisme jamais employées.
- **Les faits** : `faits-v1.md` lui-même, aux proposeurs et au juge (le code sert la même pièce aux deux). Rien de plus.
- **Les témoins** : au juge de l'organisme seul (§ 3).
- **Rien d'autre** : aucun bilan d'une autre source, aucun matériau de notre part. Un essai vérifie qu'aucune pièce
  épinglée ne porte « bilan » dans son chemin.

## 3. Pièces témoins exigées par le lanceur : lesquelles, et pourquoi

Le code de l'orchestrateur refuse une course sans témoins et impose **quatre classes** (`charger_temoins` : vrai, jumeau,
faux de falsifiabilité, faux d'antériorité) ; le lanceur passe donc un fichier de quatre fiches, servi au seul juge de
l'organisme. Je n'en ai écrit aucune autre.

Différence voulue avec la course précédente : **aucune de ces quatre fiches ne contient d'affirmation fausse**. La
fiche « faux de falsifiabilité » est une remarque vague qui dit elle-même n'avoir ni facteur, ni seuil. La fiche « faux
d'antériorité » rejoue un constat que les faits attribuent au travail [9], et se déclare « occupée » en le citant (les
témoins précédents de cette classe se disaient « inédits »). Le vrai et son jumeau portent une même idée de mon cru
(parenté de surface entre démonstrations d'entraînement et scénarios), écrite sans avoir lu aucun bilan. Les quatre
passent le validateur réel de l'orchestrateur et ne déclenchent pas son filtre lexical
(`outils/resultat-valider-pieces-v1.txt`).

## 4. Ce que je retire de la conception précédente, et pourquoi

Il n'y a ici ni lecteur de la règle, ni classement par la règle : le croisement avec les quatre autres sources se fait
après, par un lecteur neuf (R-2682). Je retire donc tout ce qui servait cette règle.

| Élément de `conception-course-v1.md` (course précédente) | Ici |
|---|---|
| § 3 : attestation de lecture avant l'envoi à un lecteur externe | Retirée : aucun envoi à un lecteur payant sous cette ligne. Le manifeste de fin désigne à la place le bilan de l'organisme (copie scellée des fiches validées). |
| § 4 : règle de sélection (admissibilité, lecteur d'une autre famille, huit points prouvés par citation, classement, témoin à score permuté) | Retirée entière. |
| § 5 : vingt témoins (conceptions publiées réécrites, fausses fiches, idées tirées au hasard) | Seize retirés : ils étalonnaient le lecteur de la règle. Restent les quatre que le code exige. |
| § 6 et § 7 : conditions de lisibilité, test unique, échecs E2 à E5 | Retirés. Reste E1 : aucune fiche validée, une relance au plus. |
| Catalogue de conceptions publiées, consigne du lecteur, outil du lecteur, programme de classement | Sans objet. |
| **Réserve du lecteur, 4 USD, dans la garde de cumul** | **Retirée** : le pire cas passe de 21 à 17 USD. |
| § 9 : essai des idées désignées sur des mondes jamais vus | Sans objet. |
| § 1 et § 2 : orchestrateur épinglé, proposeurs, parts, juge exigé par le code, aucun bras, lancement détaché, relevé et copies scellés, relance unique, environnement par liste de noms, fiches validées seules lues | **Gardés à l'identique.** |

Ce que le retrait laisse ouvert : la méthode du croisement des cinq bilans n'est écrite nulle part dans ces pièces
(nœud N6).

## 5. Le lanceur dérivé

`scripts/lancer_course_ideation_regard_ou_raisons_v1.py`, dérivé par remplacements exacts du lanceur « conception propre »
v1 (`709cf1c7…`), contre-lu « autorisable » (R-2623) et joué (R-2628). Hors de l'en-tête, le différentiel touche 69 lignes.

**Gardé à l'identique** : la garde de soi (options `-I -B`, commande d'origine exacte, argument unique `1`, dossier
courant, interpréteur, fichier non lien et d'empreinte égale à son compagnon, avant le verrou) ; tout ce qui peut échouer
avant le détachement, aucune commande git après ; relevé de dépense et copies scellées dans le dépôt à la clôture ; une
seule relance au total, seulement après une course finie proprement, sans fiche, à relevé lisible ; environnement par liste
de noms ; verrou ; orchestrateur épinglé (arbre `ee84d6ec…` et neuf empreintes) ; mêmes proposeurs, même juge, mêmes
plafonds de session, même enveloppe et même commande d'Argon ; aucun bras ; gardes de somme, de taille et de drapeaux.

**Changé** :

1. Pièces, noms de dossiers, de runs et de verrou (aucun mélange possible avec la course précédente), graine 2026111402.
2. Ligne de GO cherchée par son contenu : périmètre contenant « organisme d'idéation » **et** « regard ou raisons »
   (casse et apostrophe indifférentes), type calcul, Lazar, période, non révoquée, **une seule**, plafond ≥ 17 USD.
3. Garde de cumul sans réserve du lecteur : dépense relevée + 14,9 ≤ min(17, plafond de la ligne). Pire cas et borne du
   lanceur à 17 USD.
4. Manifeste de fin : le bloc qui préparait l'attestation devient `bilan_de_l_organisme` (chemin et empreinte de la copie
   scellée des fiches validées).
5. Conseil d'arrêt imprimé : `kill -INT` d'abord, `kill -TERM` seulement si la course ne finit pas (condition C1 de la
   contre-lecture précédente). Le relais des signaux par PID n'est pas touché.

**Non corrigé, repris tel quel de la contre-lecture précédente** (`cd482ebe…` au registre) : les relevés ne protègent que
commités et poussés (A2) ; un départ au code 5 suivi de la perte du dossier hors dépôt passe pour « rien lancé » (m1) ;
une clôture interrompue ne se reprend pas seule (m2) ; fenêtre d'orphelin de quelques instructions (m7) ; la garde de soi
ne vaut que contre l'accident (m8). D'où les conditions d'emploi du § 8.

## 6. Essais et mutations

- **Essais** : `tests/test_lancer_course_ideation_regard_ou_raisons_v1.py`, dérivés des essais v2 du lanceur précédent
  (73 fonctions, 131 cas), portés à 86 fonctions et **151 cas**. Joués quatre fois, 151 passés chaque fois : à 09:31 et
  09:35 UTC sur la copie de base du banc, à 09:33 UTC dans le dépôt, puis à 09:43 UTC dans le dépôt, **151 passés en
  60 secondes** (`outils/resultat-essais-lanceur-regard-ou-raisons-v1.txt`). Deux d'entre eux jouent, sans appel, l'orchestrateur réel
  (liste blanche et mesure sur les vraies pièces ; analyseur d'arguments). Aucun dossier de production créé.
- **Essais neufs** : les trois gardes que la contre-lecture précédente avait trouvées sans essai qui les isole (sortie
  sans manifeste de fin, pièces hors liste blanche, bac à sable inactif) ; ses deux mutations « équivalentes », rendues
  décidables ; l'arrêt propre par SIGINT relayé ; la fidélité de la question au fond ; les quatre classes de témoins ; les
  noms propres à cette course ; un essai du registre réel des GO qui tient avant comme après l'inscription de la ligne.
- **Banc** : `outils/mutations_lanceur_regard_ou_raisons_v1.py`, de 09:34 à 09:43 UTC : base 151 passés, **61 mutants
  tués sur 61**, aucun survivant. Trois séries : les 25 du préparateur précédent (un adapté) ; les **28 de la
  contre-lecture précédente**, réécrites d'après sa description, dont ses 5 survivantes, tuées ici par les essais neufs ; 8
  sur ce que ce lanceur change. J'ai relu, pour chaque mutant, l'essai qui le tue : chacun vise bien la garde mutée.

## 7. Devis (`devis-v1.md`)

| | Attendu | Pire cas |
|---|---|---|
| Relais Claude (plafond 10) | ≈ 3,5 USD | 10,0 pour une course ; 10,4 relance comprise |
| Relais Gemini v2 (8 appels) | ≈ 2,0 USD | 4,9 pour une course ; 6,6 relance comprise |
| **Total** | **≈ 5,5 USD (4 à 8)** | **14,9 pour une course ; 17,0 relance comprise** |

Rappel : la course précédente a coûté 5,53 USD pour un pire cas de 21. Les plafonds de session ne sont pas abaissés, et le
devis dit pourquoi (§ 5 du devis) ; les tailles mesurées sans appel tiennent toutes les gardes, avec une marge de 112 048
caractères sur la garde de course.

## 8. Commandes exactes, et ce qu'il faut à la session qui lancera

Préalables, dans l'ordre :

1. Contre-lecture du lanceur par un autre modèle (R-2682) : le différentiel, les essais neufs, la question servie.
2. `bwrap` et `socat` présents (vrai à 09:18 UTC) ; clone `/home/user/lciric/ideation-organism` à l'arbre `ee84d6ec…`,
   propre (vrai à 09:44 UTC) ; ports 8787 et 8788 libres (vrai à 09:47 UTC, lu dans `/proc/net/tcp` ; le port 8789
   est tenu par un autre processus, que je n'ai pas cherché à identifier).
3. Empreinte du lanceur, à comparer à `3b2dcb11…` :
   `cd /home/user/controle-ia-travail/scripts && sha256sum -c lancer_course_ideation_regard_ou_raisons_v1.py.sha256`
4. Relais lancés et vérifiés avant la commande, comme pour la course précédente (registre, R-2624, première ligne de ce
   numéro) : relais Claude du clone, clé lue par son nom par le relais seul, port 8787, `--plafond-usd 10`, modèles permis
   limités aux deux de `PROPOSEURS` ; relais Gemini v2 (`2b0043bc…`), port 8788, `--max-appels 8`. Ne pas relancer le
   relais Claude entre une course et sa relance.
5. Commande exacte écrite au registre avant le lancement (compensation de l'absence du crochet, R-2611 et R-2682).

**Lancement**, au premier plan (ni `&` ni `nohup`), depuis la racine du dépôt :

    cd /home/user/controle-ia-travail
    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_regard_ou_raisons_v1.py 1

Code 0 et « lancée, détachée » : la course tourne sous son superviseur, dont le PID est imprimé. Commiter et pousser le
dossier `runs/course-ideation-regard-ou-raisons-v1/<identifiant>/` aussitôt.

**Compte rendu et clôture** : la même commande, exactement. Code 3 tant que la course tourne ; code 0 et « clôture » une
fois le superviseur mort (une seule invocation de clôture) ; code 4 si un orchestrateur orphelin vit ; code 2 pour tout
refus. Après la clôture : commiter et pousser le dossier de run, consigner la dépense relevée dans
`registres/depenses.md`, arrêter les relais par PID.

**Arrêt en cours de route** : `kill -INT <PID du superviseur>`, attendre la fin, puis la commande de clôture ;
`kill -TERM <PID du superviseur>` seulement si elle ne finit pas. Si le lancement rend le code 5 ou une trace : clôturer
dans le même conteneur, sinon nœud, aucune relance.

**Après la clôture** : le bilan de l'organisme est `copies/sortie--fiches-validees.json` dans le dossier de run, scellé
par le lanceur. Les copies des notes du juge, de la lecture de la course et du manifeste de fin de l'orchestrateur restent
fermées au lecteur du croisement : la question servie le promet aux proposeurs.

## 9. Ligne de GO

**Déjà inscrite** par la mère pendant la préparation : GO-2026-11-14-01, calcul, 25 USD, échéance 30 novembre, Lazar
(R-2682). Le lanceur la trouve, seule, et se borne lui-même à 17 USD (vérifié à 09:35 UTC sur le registre réel, sans rien
lancer). Ses conditions : rendu du préparateur (ce rapport), contre-lecture du lanceur par un autre modèle, pire cas
≤ 25 USD (17).

Le texte que j'aurais proposé, pour mémoire seulement, puisqu'une ligne ne se réécrit pas : « Course de l'organisme
d'idéation (atelier d'idées, N-065 rôle 2) sur la question « Regard ou raisons » (explications rivales autres que le
regard, forme du papier ; R-2679, R-2680) : une génération, une seule relance au total, lanceur
`scripts/lancer_course_ideation_regard_ou_raisons_v1.py` (`3b2dcb11…`) lancé seulement après sa contre-lecture par un autre
modèle, bac à sable actif ; relais par leurs clés nommées, plafonds du devis (`1d9628bc…`) ; aucun lecteur payant ni
classement par règle sous cette ligne ; bilan scellé avant toute lecture ; arrêt par identifiant (R10) », 17 USD,
échéance 30 novembre 2026.

À garder en tête : toute autre ligne principale dont le périmètre contiendrait les deux expressions « organisme
d'idéation » et « Regard ou raisons » ferait refuser le lanceur (deux lignes : sens fermé).

## 10. Nœuds pour la mère

- **N1 — fiches en quarantaine.** Enjeu : le filtre est lexical et écrit pour d'autres questions ; sur celle-ci, des
  fiches honnêtes peuvent y tomber. Options : (a) le lecteur du croisement lit aussi `fiches-en-quarantaine.json`, marquées
  comme telles, après lecture par la mère ; (b) fiches validées seules. **Recommandation (a)**, confiance 0,6 ; défaut
  sous 48 heures : (b), le plus fermé.
- **N2 — contrainte d'écriture dans la question.** Elle dit aux proposeurs quels mots et formes le filtre met à part.
  Options : (a) la garder ; (b) question v2 sans elle (lanceur v2, R12). Sans elle, toute fiche qui nomme le premier
  scénario par le mot des faits part en quarantaine. **Recommandation (a)**, confiance 0,7 ; défaut : (a).
- **N3 — répartition demandée aux proposeurs** (deux fiches de forme de papier au plus par passe ; une fiche au moins sur
  la signature positive ; une au moins sur le duel décisif). C'est de la forme ajoutée par moi, non du fond.
  **Recommandation : garder**, confiance 0,6 ; défaut : garder.
- **N4 — borne du lanceur à 17 USD sous une ligne à 25.** Une relance après une première tentative de plus de 2,1 USD
  serait refusée, alors que la ligne la couvrirait. La lever demande un lanceur v2. **Recommandation : garder 17**,
  confiance 0,7 ; défaut : garder.
- **N5 — la question servie part chez deux fournisseurs.** R-2682 (point 3) accepte l'envoi de la question et des faits ;
  ma mise en fiches est un texte neuf autour du même fond. À lire par la mère avant le lancement.
- **N6 — méthode du croisement.** Comment le lecteur neuf juge et retient des propositions venues de cinq sources n'est
  pas écrit ici (hors mandat). À écrire et sceller avant l'ouverture du premier bilan.

## 11. Réserves

- **Erratum sur une pièce scellée.** Le champ `auteur_tiers` du fichier de témoins dit que le préparateur est « du modèle
  d'un proposeur et du juge ». C'est inexact : je suis de la lignée du modèle B (un proposeur), dans une version voisine ;
  le juge est du modèle A. Ce champ n'est ni lu ni servi par l'orchestrateur (seule la liste `temoins` l'est). Je ne
  réécris pas une pièce scellée et épinglée (R12) : l'erreur est dite ici.
- Des témoins honnêtes éprouvent moins le juge de l'organisme que des témoins qui se disent inédits. Sans effet sur la
  course : ses notes ne servent pas.
- L'attendu vient d'une seule course ; sa répartition entre relais est estimée (ventilation précédente non lue).
- Les deux différentiels, les essais et le lanceur gardent, comme code, les identifiants de modèles que l'orchestrateur
  exige ; le manifeste de pré-départ en portera aussi (déjà noté pour la course précédente, R-2625). Les pièces de texte
  neuves n'en portent aucun (question, témoins, devis vérifiés par programme ; ce rapport vérifié à la main).
- Le fichier d'essais ajoute environ une minute à la routine `python -m pytest -q`. Si la règle « aucun commit sous
  `tests/` avant S7 » (R-2614) tient encore, il attend ; la mère le sait.
- Les heures de rédaction sont des intervalles bornés par des relevés `date -u`, non des instants.
