# Contre-lecture de l'addendum des témoins du juge et du budget de pensée de Carbon, version 2 (organisme d'idéation, organismes discrets)

Contre-lecteur neuf (R2), modèle Opus 5.5. Je n'ai écrit ni l'addendum (v1 ou v2), ni les témoins, ni leur script, ni le
script d'épreuve, ni ses essais, ni la première contre-lecture. 18 novembre 2026. Contre-lecture **courte**, limitée aux
parties changées, comme demandé.

Pièce lue : `addendum-temoins-et-carbon-v2.md` (`6bc16256…`, non scellé au moment de la lecture). Pièces d'appui, empreintes
vérifiées par leurs compagnons `.sha256` (toutes conformes) : `temoins-organisme-discrets-v4.json` (`af06e21a…`),
`ecrire_temoins_v4.py`, `-v1.json` (`1c6eef38…`), `question-v3.md`, `faits-v3.md`, `diagnostic-temoins-v2.md`,
`contre-lecture-addendum-temoins-v1.md`, `scripts/epreuve_temoins_seuls_v2.py` (`8f993ba2…`),
`tests/test_epreuve_temoins_seuls_v2.py` (`7383dbfc…`), `epreuve-lot-carbon-v1/` (cinq pièces), `epreuve-carbon-2048-v1/`
(deux pièces) ; journal de la relance, OD-015 à OD-023 ; orchestrateur épinglé (`a41b7b50`, arbre propre) :
`pole/ideation_v2.py`, `pole/adaptateurs.py`, `pole/relais_reel.py`, `pole/relais.py`, `demonstrations/ideation_v2.py`
l. 1185-1215 ; manifestes de pré-départ et de départ des courses (copies dans `runs/course-ideation-organismes-discrets-v8/`,
champs de commande, de budget et de versions seulement) ; journal du relais Claude des courses
(`/home/user/hors-depot/relais-organismes-discrets-v8/journal-relais-claude.jsonl`, usage et horaires seulement) et
journaux des relais Gemini d'épreuve.

**Ce qui n'a pas été ouvert.** Aucune fiche de proposeur, aucun `fiches-*.json`, aucun dossier `proposeurs/`, aucun
`consigne.md` ni `reponse.md` de juge des courses. Écarts de forme, déclarés : (1) `find … -name consigne.md` sous le
dossier de sortie des courses (noms de chemin seulement) pour donner un chemin à `--verifier-gabarit` ; (2)
`--verifier-gabarit` lancé sur la consigne du juge d'Astra et sur celle d'Argon (booléen seul affiché). Rien lancé de payant,
aucun relais lancé ; le compteur de dépense du relais a été exercé **en mémoire** (classe `Compteur`, sans serveur ni réseau).
Sorties de mes essais : bloc-notes de session (`/tmp/claude-0/…/scratchpad/cl2/`), hors du dépôt ; `runs/epreuve-temoins-seuls-v2/`
n'existe pas (vérifié avant et après).

## Verdict

**À corriger.** Les corrections de la v1 sont faites pour l'essentiel et vérifiées sur pièce (§ 7 ligne par ligne,
ci-dessous) ; les témoins v4 passent la validation complète du code épinglé ; le juge est bien appelé par l'adaptateur des
courses ; le tableau de Carbon est juste. Mais **la commande exacte, telle qu'écrite, a toutes les chances de consumer
l'unique tentative sur un refus du relais** (constat 1, bloquant) : chaque session du kit envoie deux requêtes simultanées,
et un relais à 0,5 USD avec la réserve par défaut de 0,4 USD par appel refuse la seconde. Viennent ensuite trois défauts du
script qui se corrigent sans dépense (coût jamais relevé, refus avant envoi classés en tentative, essais qui masquent l'un et
l'autre), et un jugement franc sur le vrai témoin v4 : un juge correct peut encore le noter 1 et 1, pour des raisons
proches de celles qui ont fait tomber la v1 ; l'addendum doit le dire.

## Vérifications faites

| point | résultat |
|---|---|
| Témoins v4 contre le code épinglé (`python3 -I -B`, `sys.path.insert(0, ORCH)`, aucun fichier de l'orchestrateur modifié) | `valider_fiche_ideation` : les quatre passent ; `signaux_niveau_methode(vue_servie(·))` : vide pour les quatre ; `charger_temoins` avec une liste blanche à l'empreinte `af06e21a…` : passe, quatre classes ; `jumeau_de` = nom du vrai |
| Génération | `ecrire_temoins_v4.py` rejoué sur la v1 : sortie identique octet pour octet à `temoins-organisme-discrets-v4.json` ; les deux faux égaux à ceux de la v1 (égalité d'objets JSON) |
| Longueurs servies (`texte_plat(vue_servie)`) | vrai 4 448, jumeau 3 491, faux 2 407 et 2 606 : conformes à l'addendum l. 49-51 |
| Termes de l'idée dans la question v3 et les faits v3 | « hors ligne », « attach », « sensib », « insensib », « spike », « témoin », « injecti », « simul », « à vide », « structurel », « connu », « calibr » : 0 ; « positif » : seulement dans « faux positif » (question l. 7) et dans « dispositif » ; « dérang » : faits l. 8 (la règle du Bras A) ; « étalonnage » : faits l. 17 (concordance des lecteurs, sans rapport) ; « plancher » : question l. 9 et faits l. 21 (critère d'échec de l'instrument, autre que celui du témoin). Conforme à l. 47-48, avec la réserve du constat 5 sur le fond |
| Épreuve à sec, commande exacte (`env -i … --a-sec --dossier <neuf>`) | code 0 ; consigne de 24 087 caractères, empreinte `3540c4c7…` = `CONSIGNE_ATTENDUE` = addendum l. 63 |
| Gabarit (`--verifier-gabarit`) | égal à la consigne du juge d'Astra et à celle d'Argon (code 0 les deux fois) |
| Essais | 12 passés (`.venv`, `PYTHONPATH=src`) |
| Environnement de la commande exacte | `/usr/local/bin/python3` 3.13 ; `claude_agent_sdk` 0.2.172 importable (même version que les quatre manifestes de départ), outil en ligne de commande embarqué présent ; `bwrap` et `socat` trouvés ; `etat_bac_a_sable_detaille()` : actif, `/proc` neuf monté (le script tourne sous root : la condition CL31-15 est tenue) ; `noms_de_cle_presents(os.environ)` : vide. L'environnement suffit au kit et au bac à sable |
| Appel du juge contre la course | même rôle `juge_ideation`, donc même consigne système (`CONSIGNES_SYSTEME`), même effort « medium », `tools=[]`, `MAX_TOURS_IDEATION` = 2, même délai de session (3 600 s, défaut ; les manifestes de départ disent 3 600), même bac à sable. Écarts restants, sans effet sur la façon de noter : plafond de session 0,5 au lieu de 2,0 (`--budget juge_ideation|claude-opus-5-5=2.0` au pré-départ d'Argon) ; pas de `lire_etat_relais` (pas de coût lu au relais) ; liste d'interdits de lecture différente (le juge n'a aucun outil) |
| Codes de sortie contre la règle d'arrêt | 0 / 4 / 3 / 2 conformes au § 4 pour les cas prévus ; deux écarts (constats 3 et 9) |
| Tableau de Carbon | lignes conformes au journal et aux pièces (détail au constat 7) ; « réponse juste » vérifiée (1 013, somme 5 : 1 009 a une somme de 10) ; 400,7 s entre création et fin du lot ; prix des bornes hautes 8,3 / 41,5 (enveloppe `appel-carbon-v2.sh`) : 2 414 × 8,3 + 612 × 41,5 = 0,0454 USD, et (82 × 8,3 + 863 × 41,5) / 2 = 0,018 USD ; 0 jeton de pensée à 1 024 et à 2 048 confirmé aux journaux des relais Gemini d'épreuve |

## § 7 de l'addendum, ligne par ligne

| n° | dit fait | sur pièce |
|---|---|---|
| 1 | paire v4 neuve | **fait** ; la paire ne se contredit plus ; jugement de fond au constat 5 |
| 2 | dossier imposé, refus quelle que soit l'issue, aucun réglage libre, empreinte épinglée | **fait** (script l. 37, 139-142, 161-166) ; reste un rejeu possible depuis une autre copie du dépôt (constat 10) |
| 3 | code 3 : un seul texte | **fait** (script l. 21-22, addendum § 4.2) ; mais le code 3 couvre aussi des refus avant envoi (constat 3) |
| 4 | plafond de session et du relais ; ligne de GO demandée | mécanisme **présent**, mais réglage du relais **faux** (constat 1) ; ligne de GO toujours non citée (constat 11) |
| 5 | juge par l'adaptateur ; écart argumenté | **fait** (vérifié ci-dessus) |
| 6 | tableau corrigé | **fait** |
| 7 | 2 048 essayé, risque écrit, décision au format | **fait** ; « taille réelle » vaut pour l'entrée seulement (constat 7) |
| 8 | docstring | **fait** |
| 9 | refus en code 2 | **fait** pour les refus du script ; pas pour ceux de l'adaptateur (constat 3) |
| 10 | essais versés (12) | **fait** ; le faux adaptateur ne rend pas la forme réelle du résultat (constat 4) |
| 11 | graine | **fait** (« tirée à part ») |
| 12 | sous-question 3, risque de doublon dit | **fait** |
| 13 | « à la lettre de la grille » retiré | **fait** (ne reste qu'au tableau du § 7) |
| 14 | question versée, coûts sourcés, deux durées | **fait** ; une ambiguïté de prix (constat 12) |
| 15 | empreinte de la consigne | **fait** |
| 16 | jumeau à prédiction non triviale | **fait** au sens de la v1 ; voir constat 8 |
| 17 | règle 4.4 | **fait** |
| 18 | v4 générée par programme | **fait** (régénérée identique) |

## Constats

### Bloquant

1. **Le relais réglé comme dit refuse l'appel du juge : l'unique tentative serait perdue en code 3** (addendum l. 66-68 et
   l. 72-74 ; script l. 24-25 ; `pole/relais_reel.py` l. 140-160 et l. 245-250 ; procédure
   `docs/procedures/relais-persistants-v1.md` l. 44-45). Le relais **réserve** 0,4 USD par appel avant de l'envoyer (défaut
   `RESERVE_PAR_APPEL_DEFAUT`) et refuse (402) tout appel tel que dépense + engagé + réserve dépasse le plafond. Or chaque
   session du kit envoie **deux requêtes presque simultanées** au modèle : au journal du relais Claude des courses, la
   session du juge d'Astra part à 1794983504,225 (entrée 32 069 jetons, sortie 31 : appel annexe) puis à 1794983504,256
   (appel principal : 31 459 jetons écrits en cache, 9 415 en sortie) ; le juge d'Argon de même (…097,582 puis …097,612) ;
   les deux proposeurs Opus de même ; l'annexe part la première, de 25 à 30 ms, et dure environ 2 s. Les relevés cités par
   l'addendum (0,474 et 0,417 USD) sont précisément la somme des deux appels de chaque session. Avec `--plafond-usd 0.5` et
   la réserve par défaut : annexe réservée (0,4), appel principal 0 + 0,4 + 0,4 = 0,8 > 0,5 → **402**. Vérifié en mémoire
   sur la classe `Compteur` du code épinglé : deuxième `reserver()` simultané refusé ; accepté seulement après le règlement
   de l'annexe, ou avec une réserve de 0,2. Le kit ne fait pas de reprise connue sur un 402 : la session finit en erreur,
   le script sort en code 3, et la règle 4.2 interdit toute reprise sans addendum neuf. **À faire** : lancer le relais de
   l'épreuve avec `--reserve-par-appel 0.2` (deux réserves tiennent dans 0,5 ; dépassement possible du plafond borné par la
   garantie du relais, quelques centimes au pire), l'écrire dans la commande du § 3 et dans le docstring du script ; et
   ajouter au script, **avant** la création du dossier imposé, une lecture gratuite de `GET /relais/etat` qui refuse en
   code 2 si le relais ne répond pas, si `plafond_usd` ≠ 0,5, si `reserve_par_appel_usd` > 0,25, si `modeles_permis` ≠
   `["claude-opus-5-5"]`, ou si `depense_usd` ou `appels` ≠ 0 (relais neuf, dédié à l'épreuve). Un essai le couvrant.

### Significatifs

2. **Le coût de l'appel n'est jamais relevé** (script l. 108 et l. 182). Le script lit `r.cout` ; le résultat réel de
   l'adaptateur (`pole/adaptateurs.py` l. 146-164) porte `cout_declare_usd` et `cout_inconnu`, pas `cout`. `issue.json`
   aura donc toujours `"cout_usd": null`, alors que la règle 4.2 fonde l'addendum suivant sur « `issue.json` (statut,
   erreur, coût) » et que la dépense doit être consignée. La course, elle, compte `max(cout_declare_usd, écart lu au
   relais)`. **À faire** : lire `cout_declare_usd` et `cout_inconnu`, et l'état du relais avant et après (la lecture du
   constat 1 le permet), écrire les trois dans `issue.json`.

3. **Des refus avant tout envoi sortent en code 3 et brûlent la tentative** (script l. 101-107, l. 167-177 ;
   `pole/adaptateurs.py` l. 418-426, l. 353-358). Le script crée le dossier imposé (l. 173), puis appelle
   `adaptateur.lancer`, où l'adaptateur refuse **avant tout envoi** si un nom de clé est dans l'environnement
   (`CleDansEnvironnement`), si le modèle n'est pas permis, ou si le kit n'est pas installé ; s'y ajoute le relais absent
   (connexion refusée, rien de facturé). Ces cas sont pris par `except Exception` et rendus en **code 3** (« tentée »), et
   le dossier existe : aucune reprise sans addendum neuf, alors que rien n'est parti. La commande `env -i` rend le premier
   cas improbable, pas les autres. **À faire** : exécuter avant la création du dossier les mêmes contrôles
   (`noms_de_cle_presents(os.environ)`, `verifier_modele_reel(MODELE)`, `importer_sdk()`, lecture du relais du constat 1)
   et les refuser en code 2.

4. **Les essais masquent les constats 2 et 3** (`tests/test_epreuve_temoins_seuls_v2.py` l. 42-44). Le faux adaptateur
   rend un `SimpleNamespace` avec `cout` et `texte`, champs que le résultat réel n'a pas ; aucun essai ne construit un
   `Resultat` réel, ni ne simule un refus de l'adaptateur avant envoi. **À faire** : rendre `pole.adaptateurs.Resultat`
   dans le faux (avec `cout_declare_usd`, `texte_final`, `texte_brut`), et ajouter les essais « clé dans l'environnement »,
   « relais absent ou mal réglé » → code 2, dossier non créé.

5. **Le vrai témoin v4 et son jumeau peuvent encore, légitimement, être notés 1 et 1** (`temoins-organisme-discrets-v4.json`
   l. 9-52 et 54-91 ; addendum l. 41-46 ; `diagnostic-temoins-v2.md` l. 43-48 et l. 85-88). Réponse franche à la question
   posée : **oui**, et le risque d'un code 4 est élevé, comparable à celui de la v1. La porte n'exige qu'une note 2 sur
   l'un des deux critères (`PORTE_ELIGIBILITE` = 2 sur `max(avantage, originalité)`), mais aucun des deux n'est solide :
   - **Avantage** : l'addendum le concède (l. 42-43). La fiche le décrit comme l'accès aux pièces du banc (jumeau apparié,
     référence cachée) et le dit elle-même fabriqué « sans aucun appel de modèle », coût « bas » (l. 46) ; c'est la forme
     exacte de la justification qui a mis 1 à la v1 (« les données … sont propres au programme, mais … se reproduit à faible
     coût »). Et la première lecture (la couverture est-elle sensible à l'attachement ?) se tranche en partie en lisant la
     définition de la couverture : une permutation conserve l'ensemble des contrôles mentionnés (faits l. 8 et l. 15), si
     bien qu'une couverture comptée par mention est invariante par construction, sans référence ni calcul. L'argument
     « aucun calcul ne remplace la référence » (l. 34-35) ne vaut que pour l'ampleur.
   - **Originalité** : le titre nomme une notion de manuel (« contrôle positif ») tout en se déclarant « inédite ». Les
     voisins les plus proches ne sont pas discutés : analyse de mutation et injection de fautes (appliquer à un objet sain
     la classe de défaut étudiée pour mesurer si l'instrument la voit ; DeMillo, Lipton et Sayward, 1978, SUPPOSÉ), tests à
     réponse connue, et, en contrôle de l'intelligence artificielle, la validation des moniteurs sur des sabotages plantés
     par programme. Le juge a déjà noté le jumeau v1 « contrôle par remplacement aléatoire, diagnostic courant ». La
     distinction revendiquée (« rejouer l'intervention étudiée sur la condition témoin ») est étroite.
   - **Proximité des faits** : les faits définissent le jumeau honnête comme la dose 0 du **même** dérangement, tiré par
     graine (l. 8). Un juge peut lire « jumeau dérangé hors ligne » comme une dose du Bras A lui-même, ou comme la
     vérification évidente du protocole ; la fiche ne dit pas en quoi le saboteur diffère d'un jumeau dérangé (elle le
     suppose en l. 18 : « s'il le voit là mais pas chez le saboteur »).
   Ce n'est pas bloquant : l'épreuve est faite pour attraper ce cas à 0,1 à 0,2 USD, avant toute course. Mais l'addendum
   doit **écrire** que l'échec est probable et ce qu'il coûte (un cycle), discuter l'analyse de mutation et l'injection de
   fautes dans l'antériorité des deux fiches, et dire, dans les deux fiches, ce qui distingue le saboteur d'un jumeau
   dérangé au vu des faits. Si l'épreuve passe, le témoin reste à la limite : une réussite dira la pente de ce juge, pas
   que le témoin a un verdict « connu ».

6. **Un arrêt brutal pendant l'appel n'est ni écrit ni classé** (script l. 101-107, l. 177-183 ; addendum § 4). Une interruption (`KeyboardInterrupt`, `asyncio.CancelledError`,
   `SystemExit`) pendant l'appel n'est pas une `Exception` : elle sort du script avec un code 1 ou 130, sans `issue.json`,
   dossier créé, appel peut-être facturé. Le docstring de `juger` (« Aucune exception ne sort ») est faux pour ce cas, et
   la règle d'arrêt ne dit rien d'un code autre que 0, 2, 3, 4. **À faire** : `except BaseException` qui écrit `issue.json`
   (code 3) puis relève l'interruption ; une ligne au § 4 : « tout autre code vaut 3 ».

7. **« Essayée à taille réelle » vaut pour l'entrée seulement** (addendum l. 109 et l. 119-121 ;
   `epreuve-carbon-2048-v1/ligne-de-la-commande-sans-texte.json`). L'épreuve à 2 048 a envoyé la question et les faits v3
   (2 414 jetons ; la consigne d'un proposeur de course en fait davantage, 11 085 caractères selon la première
   contre-lecture), avec une sortie **bornée à 2 048 jetons** (`max_sortie_jetons`), dont 612 rendus ; une course demande
   six fiches de 3 à 5 000 caractères, soit plusieurs milliers de jetons de sortie. Le flux a tenu (26 morceaux, silence
   maximal 0,6 s), ce qui est l'essentiel contre la coupure à 300 s, mais une génération dix fois plus longue n'a pas été
   essayée. Par ailleurs cette épreuve (07:20Z) n'a pas d'entrée au journal de la relance (qui s'arrête à OD-023), alors
   que le § 5 renvoie au journal. **À faire** : écrire « entrée de taille proche de la course, sortie bornée à 2 048 » dans
   le tableau et dans (B) ; journaliser l'épreuve (heure, coût, signalement).

### Mineurs

8. Prédiction des deux fiches (v4 l. 21-26, l. 65-69) : c'est surtout une règle de classement à deux branches dont la
   fiche ne dit pas laquelle elle attend ; seules une baisse intermédiaire (0,05 à 0,15 point) ou une réponse non
   monotone à la dose la contrediraient, et la zone 0,05 à 0,15 n'est pas classée. Possible, peu exposée ; sans effet sur
   `temoins_ok` (pas de `note_max`).
9. Le vrai porte sur « les quatre doses non nulles » (v4 l. 20, l. 43), le jumeau sur « p = 1/2, 3/4 et 1 » et « trois
   doses » (l. 64, l. 83) : petite incohérence d'une paire censée être la même idée.
10. Rejeu : `SORTIE` est dérivé de l'emplacement du script (l. 35-37) ; lancé depuis une autre copie du dépôt, il écrit
    ailleurs et passe. La barrière reste une règle ; le dire (« seul le dossier du dépôt de travail compte ; il est commité
    dès la sortie ») ou s'appuyer sur la lecture du relais neuf du constat 1 (`appels` = 0).
11. Ligne de GO toujours non citée (addendum l. 74-75 : « celle que la mère désigne ») ; la commande ne porte pas
    `GO_ID`. Acceptable tant qu'aucun appel ne part avant, mais l'addendum scellé doit la nommer, ou être suivi d'une
    ligne qui la nomme avec son empreinte.
12. Lot de Carbon (addendum l. 110) : « 0,004 au prix public (2 / 10) » est le prix public **à moitié prix** (lot) ; au prix
    public plein, 0,009 USD. Écrire « 0,004 au prix public du lot (moitié de 2 / 10) ».
13. Le script écrit `reponse-du-juge.md` à partir de `texte_brut`, non caviardé (l. 123, l. 180), là où la course écrit le
    texte caviardé ; et il écrit la clé d'anonymisation avant l'appel (l. 176), là où la course ne l'écrit qu'après le
    dernier juge (CL31-17). Sans effet ici (le juge n'a aucun outil), mais à aligner ou à dire.
14. `r.texte` (l. 117, l. 123) n'existe pas sur le résultat réel : une réponse vide sort en code 3 avec un message
    « AttributeError » trompeur. Utiliser `texte_a_analyser(r)` de l'orchestrateur, comme la course.
15. Décision Carbon (§ 5) : au format du dépôt (décision, enjeu, deux options avec avantage et inconvénient,
    recommandation, confiance, défaut). Rien à redire sur le fond ; (B) dit bien que Carbon n'y pense pas du tout, ce qui
    en fait une autre condition qu'une « pensée réduite ».

## Ce qui tient

- Les témoins v4 sont générés par programme, reproductibles, valides pour l'orchestrateur épinglé (validation, garde du
  niveau méthode, chargement complet) ; les faux sont ceux de la v1 ; la paire est un vrai jumeau (même mécanisme, même
  métrique, mêmes seuils ; approche et question) ; elle ne se contredit plus, n'emploie que la règle du dérangement et la
  couverture contre la référence cachée, et ne suppose ni identité octet pour octet ni graine scellée ; son idée n'est pas
  nommée dans la question v3 ni dans les faits v3.
- Le script appelle le juge par l'adaptateur Claude des courses, avec la même consigne système, le même effort, aucun
  outil, le même nombre de tours, le même délai et le même bac à sable ; la consigne est épinglée et son gabarit égal à
  celui des deux courses ; il n'écrit que dans son dossier imposé (ou un dossier neuf en mode à sec), ne lit aucune fiche,
  refuse un second passage quelle que soit l'issue ; l'environnement de la commande exacte suffit au kit et au bac à sable.
- La règle d'arrêt est fermée et cohérente avec les codes ; le tableau de Carbon est juste et sourcé ; la décision est au
  format.

## Pour que l'addendum soit autorisable

Réserve par appel du relais fixée (0,2) et état du relais contrôlé avant le dossier (1) ; coût relevé (2) ; refus avant
envoi en code 2 (3) ; essais sur la forme réelle du résultat (4) ; risque du vrai témoin écrit, antériorité complétée,
distinction saboteur et jumeau dérangé dite (5) ; arrêt brutal classé (6) ; portée de l'épreuve à 2 048 écrite et
journalisée (7). Les mineurs peuvent suivre. Puis contre-lecture courte des seules parties changées (script et ses essais,
§ 2 à § 5).
