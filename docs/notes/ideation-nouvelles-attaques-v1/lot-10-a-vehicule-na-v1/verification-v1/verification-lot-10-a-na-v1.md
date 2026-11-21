# Vérification du lot 10 a du véhicule NA-1 (colonne « matière première » : chargement et garde) — v1

Vérificateur neuf (modèle S), hostile ; je n'ai écrit ni ce lot, ni les lots 1 à 5, ni la conception. Pièce de travail (classe C). 2026-11-21. Aucun appel à un fournisseur, aucune clé, aucune dépense, aucun commit ; rien écrit hors de mon dossier ; rien ouvert sous `additif-matiere-premiere-v1/`, `archives-reponses-modeles/`, `/root/.claude/`, aucune branche de quarantaine ou de matière première, aucune attache de dépôt. Aucun refus de permission, de classifieur ni de garde rencontré.

## Verdict : **Conforme** (avec cinq réserves de couverture des essais, aucune ne touche un artefact de la lettre ; § 4)

Les quatre questions posées :

| question | verdict | en une ligne |
|---|---|---|
| 1. un appel que la garde devait arrêter peut-il partir, ou un appel sain être arrêté ? | **tenu** | la garde mord à l'égalité de ligne entière sous huit formes et sous sept séparateurs de ligne ; un seul chemin la contourne, le câblage (un contexte du lot 4 muni du journal ordinaire), qui est hors du module : point pour la mère |
| 2. l'empreinte de l'additif lue ailleurs qu'au manifeste (E4) | **tenu** | les quatre artefacts d'E4 et six variantes refusent ; la configuration n'est jamais lue pour cette empreinte |
| 3. source des octets de l'identifiant de ligne fixée (E5) | **tenu** | aucune source dans le module, aucun défaut, deux fonctions d'essai différentes |
| 4. essais passés sans être mérités (mutations, témoins) | **tenu, avec réserves** | 460 et 52 sur 52 rejoués ; sur huit mutations à moi, huit prédictions tenues, dont quatre survivantes réelles aux essais du lot (réserves R1 à R4) |

## 1. Rejeu

Copie neuve de l'orchestrateur (`/home/user/orchestrateur-a41b7b50/`, lecture seule) vers `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-lot-10-a/copie-neuve/` ; application, dans l'ordre, des programmes des lots 2 v5, 3 v3, 4 v1, 5 v1, puis de `appliquer_paquet_vehicule_na_lot_10_a_v1.py --destination <copie> --lancer-essais` : quatre fichiers copiés, empreintes relues égales ; **460 passés** (rapport : 460). Le fichier d'essais du lot seul : 99 passés (rapport : 99). Mutations du lot, `mutations_na_lot10a_v1.py` sur la copie, journal `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-lot-10-a/journal-mutations-rejoue.json` : **52 tuées sur 52**, témoin non muté 0, témoin inerte survit (rapport : idem). Empreintes recalculées égales à la table : module `8ee98aa0…`, aides `57a0c49a…`, essais `10fc15ae…`, mutations `a4213dc9…`, rapport `dcbe5f8d…`, journaux, mesure, programme d'application ; mandat `9f9f20f9…`, erratum `61674e25…`, lancement `08a6bac6…`, consigne `d327b3fc…` (tirée de `origin/main` vers mon dossier, le chemin donné n'existe pas sur ce disque). Le compagnon de la table égale la table (`cb4366c1…`). Le fichier `table…txt` ne se liste pas lui-même : sans conséquence.

## 2. Lignes tenu / cassé (fichier : ligne ; preuve)

Module : `docs/notes/ideation-nouvelles-attaques-v1/lot-10-a-vehicule-na-v1/paquet/orchestrator/pole/matiere_premiere_na_v1.py` (MP).

| # | ce qui est visé | verdict | passage | preuve |
|---|---|---|---|---|
| 1 | garde par ligne entière, empreinte, jamais le nom court | tenu | MP:204-222, MP:150 | essais du lot (nom court, début, reformulation, ligne plus longue : passent ; sept formes ramenées : mordent) ; sonde V-A : ` `, ` `, `\x85`, `\x0b`, `\x0c`, `\x1c`, `\r` mordent (rang 2) ; relevé V-G : pleine largeur mord ; point final ajouté, numérotation, guillemets, NUL inséré, homoglyphe cyrillique ne mordent pas (la conception dit « la garde tient la copie, non le sens ») |
| 2 | tenue (ii), vrai noyau, aucun envoi, coût nul | tenu | MP:507-520 ; appel `appel_garde_na_v1.py`:361 | ArretColonneNA n'est pas rattrapé (:362-365 ne rattrape que motif, `JournalRefuse`, `OSError`), levé avant `ouvrir_vol` (:384) : aucun appel, aucun coût ; octets examinés = octets envoyés (`journal_na_v3.py`:257-259, :250) ; sortes `proposeur`, `sonde_refus` = les deux sortes de la lettre (`requete_na_v3.py`:77, 393, 402) |
| 3 | câblage : rien ne force le journal de la colonne | **point pour la mère** | `appel_garde_na_v1.py`:217-218 | sonde V-F : un contexte du lot 4 muni d'un `jn.JournalRequetes` ordinaire, état 1, requête de proposeur portant une ligne égale à une entrée : `issue_na == "ok"`, un envoi reçu. Le module n'y peut rien (il n'est pas dans le chemin) ; au lot 6 ou 8 de refuser un contexte dont le journal n'est pas `JournalRequetesColonneNA` quand l'état ≥ 1 |
| 4 | tenue (iii) et pièces fixes | tenu | MP:548-567, MP:453-466 | essais du lot ; mutations X-41 à X-44 tuées |
| 5 | état 0 : rien chargé ; état 1 : sixième ligne seule ; absente, double, autre libellé, empreinte fausse : départ refusé | tenu | MP:334-363, MP:469-486 | essais du lot ; X-16 à X-21 tuées. Réserve de lettre : le rang 6 n'est pas exigé (la ligne est prise à n'importe quel rang, MP:348) ; plus strict que la lettre sur les autres lignes qui nomment l'interrupteur (MP:349-351) |
| 6 | E4 : manifeste absent | tenu | MP:404-405 | essai du lot (`manifeste_absent`) ; X-27 tuée ; sonde V-C : chemin qui est un dossier, manifeste illisible : refusés |
| 7 | E4 : empreinte absente | tenu | MP:413-414 | essai du lot (`empreinte_absente`) ; X-28 tuée |
| 8 | E4 : empreinte fausse | tenu | MP:415-416 | essai du lot (`empreinte_fausse`) ; X-29 tuée ; sonde V-C : majuscules (égalité stricte) refusées ; ma mutation V2 (« empreinte non vide ») tuée |
| 9 | E4 : empreinte posée dans la configuration seulement | tenu | MP:420-439 (la configuration n'est lue que pour comparer l'état, MP:433) ; MP:400-417 | essai du lot (deux cas, dont conditions absentes d'empreinte épinglée) ; sonde V-C : configuration seule, `conditions_allumage=None` : refusé ; X-26 tuée. Nuance : l'empreinte **attendue** est un paramètre de `ConditionsAllumage` (MP:374), « épinglée par le lanceur » : si le lot 8 la lisait dans la configuration, le module ne le verrait pas. Point pour la mère (test du lot 8) |
| 10 | E5 : source des octets reçue par une fonction | tenu | MP:242-243 (paramètre sans défaut), MP:255-256, MP:298 | recherche dans le module de `to_bytes`, `random`, `urandom`, `getenv` : rien ; l'essai `test_aucune_source_fixee_par_le_module` ; ma mutation V6 (source fixée en repli) tuée |
| 11 | E5 : deux fonctions d'essai différentes | tenu | aides:77-84 ; essai du lot `test_deux_fonctions_differentes_memes_empreintes` | mêmes 35 empreintes, identifiants disjoints |
| 12 | faux refus | tenu pour l'essai, non établi pour le réel | MP:572-597 ; mesure `90c03891…` | 0 sur 3 247 lignes de 100 requêtes et 3 énoncés ; données factices, comme le rapport le dit |
| 13 | rapport et pièces | tenu | rapport § 7 | six rubriques présentes dans l'ordre ; « Mode d'échec affecté » et « Dérivation » portent « Sans objet : » ; objets de contrôle nommés ; premier pas non justifié désigné |

Rien n'est **cassé**.

## 3. Mutations à moi (prédiction écrite avant la passe, `mutations_verificateur.py`, journal `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-lot-10-a/journal-mutations-verificateur.json`)

Les sondes `test_verif_lot10a.py` (14 essais) passent sur la copie non mutée. Chaque mutation : un remplacement à texte exact dans le module, essais du lot (99) et sondes jouées à part.

| id | faute par construction | prédiction écrite d'avance | rendu |
|---|---|---|---|
| V0 | aucune (témoin) | 0 et 0 | 99 passés ; 14 passés : tenu |
| V1 | `splitlines()` remplacé par `split("\n")` (MP:218) : un énoncé séparé par un saut de ligne autre que `\n` échappe | lot : survit ; sondes : échouent | lot **survit** (99 passés) ; sondes 7 échecs : tenu |
| V2 | E4 : égalité à l'empreinte épinglée remplacée par « non vide » | lot : tuée ; sondes : échouent | lot 1 échec ; sondes 1 échec : tenu |
| V3 | E4 : contrôle « épinglée, hexadécimale » retiré | lot : survit ; sondes : échouent | lot **survit** ; sondes 2 échecs : tenu |
| V4 | tenue (ii) : 2000 premiers octets seuls examinés | lot : tuée | lot 7 échecs ; sondes 1 : tenu |
| V5 | environnement : fragment `COLONNE_MATIERE` retiré | lot : survit ; sondes : échouent | lot **survit** ; sondes 1 échec : tenu |
| V6 | E5 : source fixée en repli | lot : tuée | lot 1 échec : tenu |
| V7 | E4 : test d'existence du fichier retiré | survit (mutant équivalent : l'ouverture échoue, refus « illisible », toujours « (b) ») | survit : tenu, équivalent |
| V8 | tenue (iii) : passe sur le fichier entier retirée | lot : survit | lot **survit** : tenu |

Huit prédictions sur huit tenues. Les mutations du lot (X-01 à X-52) sont donc des juges qui tuent ce qu'elles visent, et les quatre survivantes ci-dessus sont des trous de couverture, non des fautes du module.

## 4. Réserves de couverture (pour le développeur, non bloquantes)

- **R1 (V1)** : aucun essai du lot ne met un énoncé après un séparateur de ligne autre que `\n`. La remarque 5 du rapport nomme `splitlines` ; son essai manque. Les sept cas de ma sonde V-A le comblent.
- **R2 (V3)** : l'artefact « empreinte épinglée absente ou non hexadécimale **avec** manifeste à empreinte nulle ou égale » n'est pas joué ; le code tient, l'essai du lot (`c2`) est tué aussi par l'égalité seule. Sondes V-B et V-B2.
- **R3 (V5)** : le fragment `COLONNE_MATIERE` seul n'est pas éprouvé (les deux noms d'essai portent `MATIERE_PREMIERE`). Sonde V-D.
- **R4 (V8)** : le passage sur le fichier entier du registre servi n'a pas d'essai propre (il sert un énoncé hors ligne de tentative).
- **R5** : la tenue (ii) n'est éprouvée qu'avec un énoncé planté en fin de synthèse ; V4 montre que la troncature est tuée, mais le milieu d'une requête n'est pas visé.

## 5. Écarts du rapport (§ 5), lesquels sont des points pour la mère

| remarque du rapport | point pour la mère ? | pourquoi |
|---|---|---|
| 1. lieu de la tenue (ii) : journal dérivé et non surcharge | **oui** | écart de lettre (« dans la surcharge d'`appel`, au pas 3 ») ; il tient, mais voir ligne 3 du § 2 : rien ne force le câblage ; le refus est compté dans `comptes_colonne`, non dans `na_comptes` du lot 4 |
| 2. portier et juges non gardés en tenue (ii) | **oui** | conforme à la lettre (« proposeur et sonde ») ; un énoncé recopié dans une fiche passerait ; décision de la mère |
| 3. forme du registre réel inconnue | **oui** | à fixer par qui peut l'ouvrir ; ne se voit qu'à l'essai à blanc |
| 4. défauts du n° 19 seuls au chargement | non | lecture littérale ; listes de marques brouillon du lot 5 |
| 5. forme comparée : bords retirés, `splitlines` | non (mais R1) | précision, non écart |
| 6. identifiant de ligne : six octets, dix-huit lettres | non | encodage posé au lot 10 a par la conception (§ « Où l'encodage est posé ») ; la fonction peut lire l'entrée : c'est le choix de qui la donne |
| 7. libellé d'essai de la sixième ligne | **oui** | libellé fixe à l'additif du véhicule ; contrôle v5 point 4 ; rang 6 non exigé ; toute autre ligne nommant l'interrupteur refuse : les cinq lignes fixes de la pièce réelle ne doivent pas le nommer |
| 8. état 0 « mot de la mère » pris de la sixième ligne | **oui** | à confirmer ; la pièce étant scellée (n° 14), l'état 0 n'est atteignable que par elle |
| 9. environnement et configuration | non | tenu ; le contrôle ne vaut que si le lanceur passe l'environnement réel, `environ={}` l'efface |
| 10. formes d'essai de la règle d'allumage | **oui** | (a), (c), (d), (e) sont des vérifications de forme d'essai (présence de chaînes, un booléen) ; à fixer au lot 10 b et à l'additif ; l'empreinte attendue de l'additif doit être épinglée en code par le lot 8 |
| 11. faux refus mesuré sur factice | oui (déjà dit) | le taux réel est à l'essai à blanc du lot 9 |
| 12. commandes de liste hors du dossier du lot et des lots 1 à 5 | **oui** | écart au mandat (interdit de liste), dit au rapport et attribué à la coordination ; je ne peux pas le vérifier |
| (§ 2) base v68 non ouverte | **oui, mineur** | « mutations à la manière de la v68 » prises du programme du lot 5 qui la suit ; non vérifié contre la base |

## 6. Relevé de méthode

**Chaîne de raisonnement.**
1. Mandat (`9f9f20f9…`) et erratum (`61674e25…`, E4, E5) lus en entier ; la note de lancement (`08a6bac6…`) fixe la racine ; la conception v5 (`1b7f6822…`), § 2.14, lignes 442 à 495, donne la lettre de la garde, des trois tenues et de la règle d'allumage.
2. Application sur copie neuve des lots 2 v5 à 5 v1 puis du lot 10 a : 460 passés (calcul rejoué, § 1).
3. Les 99 essais du lot seuls : 99 passés ; les 52 mutations du lot rejouées : 52 tuées, témoin non muté 0, témoin inerte survit (journal du rejeu).
4. Lecture du module en entier (MP:1-616). E5 : paramètre requis, aucune source, essais à deux fonctions (§ 2, lignes 10 et 11). E4 : manifeste lu à MP:400-417 ; l'empreinte attendue vient de `ConditionsAllumage`, jamais de la configuration (MP:433 ne lit que l'état).
5. Chemin de la garde en course : surcharge d'`appel` à `appel_garde_na_v1.py`:361 ; rattrape seulement `ArretMotifInterdit`, `JournalRefuse`, `OSError` ; l'arrêt de la colonne passe, avant le noyau (:384) ; octets examinés = octets journalisés = octets envoyés (`journal_na_v3.py`:250-259, `appel_garde_na_v1.py`:376).
6. Sondes à moi sur le vrai code (14 passés) : séparateurs de ligne, quatre artefacts E4 et variantes, environnement, câblage, formes de normalisation (relevé).
7. Huit mutations à moi, prédictions écrites avant la passe, huit tenues (§ 3).
8. Câblage (V-F) : le contexte du lot 4 n'exige qu'un `jn.JournalRequetes` (`appel_garde_na_v1.py`:217-218) ; donc la tenue (ii) dépend du lot 6 ou 8 : déclaré point pour la mère, non défaut du module.
9. Supposé : que la racine `/home/user/orchestrateur-a41b7b50/` est bien la base `a41b7b50…` ; je ne l'ai pas contrôlée contre le clone (les empreintes des dépendances du manifeste sont, elles, vérifiées par le programme d'application avant toute copie).

**Objets de contrôle.**
- Garde de la colonne. Vrai par construction (la conclusion « mord » est vraie) : ligne égale à l'énoncé 11 sous sept séparateurs ; attendu : mord ; rendu : mord. Faux par construction (« ne mord pas » est vrai) : nom court, début d'énoncé, reformulation, ligne plus longue ; attendu : passe ; rendu : passe (essais du lot). Mutation V1 : attendu et obtenu, les essais du lot ne la voient pas, mes sondes oui.
- Quatre artefacts d'E4. Objet où « état 2 autorisé » est faux : manifeste absent, empreinte absente, empreinte fausse, empreinte en configuration seule ; attendu : refus ; rendu : refus, plus variantes (dossier, illisible, majuscules, aucune condition). Objet où c'est vrai : manifeste sain à l'empreinte épinglée, toutes conditions ; attendu : état 2 ; rendu : état 2.
- E5. Faux par construction (source fixée) : mutation V6, attendu : mort ; rendu : tuée. Vrai : deux fonctions différentes, attendu : mêmes empreintes, identifiants disjoints ; rendu : conforme.
- Juge des mutations. Témoin non muté (0) et inerte (survit) du lot, reproduits ; mes huit mutations avec prédiction : huit tenues, dont quatre survivantes réelles ; un mutant équivalent (V7) nommé comme tel.
- Câblage. Objet où la tenue est contournée : contexte au journal ordinaire ; attendu : la ligne part ; rendu : elle part (constat, pas défaut du module).

**Premier pas non justifié.** Le pas 9 : que la copie en lecture seule est bien la base `a41b7b50…` ; le justifierait un `git rev-parse` sur le clone, que je n'ai pas lancé hors de mon périmètre ; les empreintes des dépendances du manifeste, vérifiées par le programme d'application, couvrent les fichiers lus, non le reste de l'arbre.

**Mode d'échec affecté.** Réponse, ligne par ligne : (1) garde : tenue, hors câblage ; (2) E4 : tenu, quatre artefacts et variantes ; (3) E5 : tenu ; (4) essais mérités : tenu, quatre trous de couverture (R1 à R4), aucun sur un artefact de la lettre. Pas visés : MP:204-222, MP:400-439, MP:242-256 et MP:298, MP:507-520. Preuves : § 1 à § 3.

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur de code, non agent de re-dérivation.

**Trouvaille de côté.**
- La garde ne voit ni l'homoglyphe cyrillique, ni le NUL inséré, ni le point final ajouté (relevé V-G) : conforme à « la garde tient la copie, non le sens », à dire au rapport de la course.
- `environ={}` passé au lieu de l'environnement réel désarme le refus par variable d'environnement : le lot 8 doit passer `os.environ`.
- La consigne commune n'est pas sur le disque de ce conteneur (`docs/procedures/` absent de la branche extraite) ; elle est sur `origin/main`, à l'empreinte attendue.

**Évaluateur et conseil.** Ce qui juge ma pièce : mes 14 sondes et mes huit mutations, écrites par moi, hors du dossier du lot ; témoin non muté (0 échec) et prédictions écrites avant la passe. Par où ma pièce pourrait paraître juste sans l'être : mes sondes lisent les mêmes aides factices que le lot (registre, pièce de relevés, conditions) ; un registre réel de forme autre, ou une pièce de relevés réelle qui nomme l'interrupteur ailleurs, ne se verraient qu'à l'essai à blanc du lot 9. Je n'ai pas vérifié la base v68 ni les pièces réelles ; le verdict « Conforme » ne vaut que pour le module sur données factices.
