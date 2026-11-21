# Rapport du concepteur des corrections — additif « matière première », devis de la lecture de fin, liste des lecteurs — v2

- Concepteur neuf, modèle F, effort élevé ; 2026-11-21, de 13:25Z à 14:15Z environ (`date -u` relevé à 13:33:02Z). Pièce de travail (classe C). Mandat : `mandat-concepteur-corrections-additif-matiere-premiere-v1.md` (`fcee0e856da002211fdff01d214aec505e93b00be045a85f654914e26ff63b62`).
- Processeur seul : aucun appel, aucune dépense, aucun commit, aucune écriture hors de mon dossier. Non ouverts : le registre servi de la matière, la branche `matiere-premiere/…`, toute branche de quarantaine, `archives-reponses-modeles/`, `/root/.claude/`.
- **Aucun refus de permission, de classifieur ni de garde.**
- **Écarts de procédure, dits.** (1) Une commande composée, une fois : le premier jeu du calcul a été lancé par un changement de dossier suivi du programme, en un seul appel ; les suivants sont des commandes simples à chemins complets. (2) Une tentative de `git show` sur un chemin que je supposais, pour l'additif 1 au complément v3 : refusée par git (« does not exist ») ; je n'ai pas cherché plus loin, faute de commande de liste permise ; le fichier vide laissé par la redirection a été retiré de mon dossier. (3) Les compagnons `.sha256` et la table d'empreintes sont écrits par un script de mon dossier (`sources/ecrire_empreintes.sh`, écrit par l'outil d'écriture, lancé en une commande), qui joue `sha256sum` depuis le dossier, fichier par fichier. Le sous-dossier `sources/` ne porte que mes extractions de `origin/main`, le second jeu du calcul et ce script : il n'est pas à verser.
- `origin/main` relu à `fed5dc2f4b10faef327ff1ca0071ea64c4b31db8`, après `git fetch origin main` (la contre-lecture avait relu à `fdbc8a73`).

## 1. Ce qui est rendu

| pièce | ce qu'elle est | change de la v1 ? |
|---|---|---|
| `additif-matiere-premiere-preenregistrement-court-v9-v2.md` | l'additif | oui |
| `annexe-objets-de-controle-lecture-de-fin-matiere-premiere-v1.md` | pièce neuve : la forme et les issues attendues des objets de contrôle, sorties de l'additif | neuve |
| `devis-lecture-de-fin-matiere-premiere-v2.md` | le devis | oui |
| `calcul_devis_lecture_de_fin_matiere_premiere_v2.py`, `entrees-devis-…-v2.json`, `calcul-devis-…-v2.json` | le calcul, joué deux fois, `cmp` muet ; aucun chiffre des trois cas ne change ; la règle de la borne de sortie s'ajoute | oui |
| `entrees-objet-faux-regle-v2.json` | objet de contrôle du programme, faux par construction | neuve |
| `liste-nominative-lecture-de-fin-matiere-premiere-v2.md` | la liste des lecteurs de la branche | oui |
| `texte-servi-aux-deux-juges-lecture-de-fin-v1.txt` | **inchangé, reste en v1** (`bbb50f64…`) ; non recopié dans mon dossier | non |
| `table-des-corrections-additif-matiere-premiere-v2.md` | le sort des quinze corrections | — |
| `differentiels-v1-v2/` | six différentiels unifiés, v1 vers v2 | — |
| `table-empreintes-corrections-additif-matiere-premiere-v2.txt`, un compagnon `.sha256` par fichier | empreintes | — |

**Compte des corrections** : quinze (treize de la contre-lecture, deux de la relecture « fuite de la vérité ») ; douze portées telles quelles, trois portées autrement (C1, C4, C11), aucune refusée.

## 2. Pièces lues

| pièce | empreinte | lecture |
|---|---|---|
| mandat des corrections ; mandat d'origine | `fcee0e85…` ; `fadb3ab51cc232939baa208e6bbff6fec31f0913ecaf9a6a7f4bde17f35c17a8` | en entier |
| les huit pièces de la v1 | celles de la table de la contre-lecture, recalculées, égales | en entier |
| contre-lecture ; relecture « fuite de la vérité » ; `entrees-objet-faux.json` | `54df8945…` ; `c04e65e8…` ; `75e68a21cab8b64ec316eae3fae39444cffa843384ae620b5a2bc850f05476d0` | en entier |
| V9 (`origin/main`, `fed5dc2f`) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | l. 296 à 335 et 366 à 396 |
| additif 1 à la V9 | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` | en entier |
| complément de valeurs, lot 1, v3 | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` | § 0, § 1 (début), § 3 (Minuit, Luc, lignes à part) |
| devis v11 de la course | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | par recherche : 450, 456, Minuit |
| `registres/go.md` à `fed5dc2f` | `c454dea5da77654680913b0bf7c3499837879e9ed5d9857261fe8dd385fc65c8` | GO-2026-11-21-18 à -55 |
| conception du véhicule v5 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` | § 2.14, § 2.15, § 5.2, § 6.2 (lignes de la colonne) |

**Non lus, et cela pèse** : l'additif 1 au complément v3 (`ce76e0d6…`, chemin non donné) ; l'additif du véhicule ; la pièce de relevés ; la note d'arbitrage et le devis v6 (repris de la v1 et de la contre-lecture, qui les ont contrôlés) ; la liste des motifs de la garde ; la liste nominative de la course elle-même.

## 3. Points délicats pour la mère

Aucun n'est tranché dans les pièces v2 : le texte prend l'option qui ne s'écarte pas du scellé, ou laisse le point ouvert et le dit. Aucun défaut : chacun touche un texte scellé, une règle de la mère ou une dépense.

**PD1 — Tirer l'ordre des lignes, ou non.** *Décision* : demander ou non à Lazar des clés de tirage neuves pour l'ordre des lignes servies aux lecteurs et aux juges. *Enjeu* : la V9 dit « Aucune autre méthode de tirage n'est permise » (l. 311) ; la clé n° 30 a demandé un accord (GO-2026-11-20-65). *Options* : (a) aucun tirage, ordre des identifiants — c'est la v2 ; avantage : aucun écart ; inconvénient : le même ordre pour tous, un effet de rang n'est pas brouillé, et une ligne de contrôle tombe où son identifiant la met. (b) Cinq clés neuves, accordées par Lazar dans sa ligne d'allumage ; avantage : ordre brouillé, différent par appel ; inconvénient : un écart de plus à la V9, et une version neuve de l'additif. *Recommandation* : (a), confiance 0,7 ; les avis des juges sont « pour information », et les lecteurs étiquettent ligne à ligne.

**PD2 — Jouer la garde de motifs sur les réponses brutes avant le mot de Lazar, ou non.** *Décision* : faire ou non lire la branche par un programme avant l'état 2, pour dire à Lazar combien de requêtes partiraient. *Enjeu* : la conception v5 (§ 2.15) et la liste des lecteurs disent que rien ne s'ouvre avant l'état 2 ; la garde écrit « le texte trouvé » à son journal (V9, l. 387). *Options* : (a) à l'état 2 seulement, premier pas de la lecture — c'est la v2 ; avantage : la règle d'ouverture tient ; inconvénient : la ligne de 16 USD peut n'acheter aucun avis, et Lazar donne son mot sans le savoir. (b) Avant le mot, par exception écrite, aux quatre conditions de la contre-lecture (programme seul, rôle inscrit autre que la mère, ligne au journal, sortie réduite, texte trouvé écrit nulle part) ; avantage : Lazar sait ce qu'il achète ; inconvénient : une exception à la règle d'ouverture, et l'arrêt n° 16 à surcharger. *Recommandation* : (a), confiance 0,75 ; au pire, 16 USD réservés ne sont pas dépensés.

**PD3 — Le sort d'une ligne de la matière classée « recette ».** *Décision* : suivre la lettre de la V9 (« « recette », au coffre », l. 328) ou porter la ligne à Lazar sans coffre, comme l'écrivait la v1. *Enjeu* : la matière est attestée « aucune recette » ; le coffre est celui de la course. *Options* : (a) la lettre, et un signalement à Lazar en plus — c'est la v2 ; avantage : aucun écart ; inconvénient : une ligne qui n'est pas une fiche entre au coffre de la course, hors de ses mesures. (b) À Lazar seul, sans coffre ; avantage : le coffre ne reçoit que des fiches ; inconvénient : écart à la l. 328, à déclarer. *Recommandation* : (a), confiance 0,6.

**PD4 — Les deux juges à la liste nominative de la course, ou une liste propre à la branche.** *Décision* : inscrire ou non les lignes de la lecture de fin comme entrées de plus de la liste de la course. *Enjeu* : cette liste a été bornée à quatre puis à cinq noms par deux accords de Lazar. *Options* : (a) une liste propre à la branche, liée à celle de la course par les mêmes identifiants de session — c'est la v2 ; avantage : la liste de la course n'est pas touchée, et les juges n'y gagnent aucun accès ; inconvénient : deux listes à tenir. (b) Des entrées de plus, numérotées à la suite ; avantage : une seule liste ; inconvénient : demande le mot de Lazar, comme la cinquième entrée. *Recommandation* : (a), confiance 0,65.

**PD5 — La composition citée, et les numéros d'arrêt.** *Décision* : confirmer que l'additif cite la bonne composition et la bonne suite d'arrêts. *Enjeu* : la V9 dit six espèces ; l'additif 1 scellé dit cinq, 27 arrêts ; l'additif du véhicule, que je n'ai pas lu, en numérote d'autres. *Options* : (a) cinq espèces, « arrêts n° 1 à n° 27 et ceux que l'additif du véhicule numérote » — c'est la v2 ; (b) une formule qui ne cite aucun nombre. *Recommandation* : (a), confiance 0,8 ; la mère donne les numéros des arrêts A, D et E avant le scellement.

**PD6 — Le reste de Minuit.** *Décision* : rien à trancher dans le texte ; à constater. *Enjeu* : le juge de l'espèce 3 se paie sur Minuit (conception v5, § 2.14) ; la part de Minuit a reçu un second rôle, puis est diminuée de la reprise de deux autres courses (GO-2026-11-21-28 et -30) ; d'autres appels lui sont accordés (GO-2026-11-21-39 et -52). Le reste au jour de la lecture peut être sous 8,00 USD. *Options* : (a) laisser l'arrêt C refuser — c'est la v2 ; la lecture se fait alors sans ce juge ; (b) une recharge, ou un autre routage : dépense ou écart à la conception, donc mot de Lazar. *Recommandation* : (a), confiance 0,7. **Je n'ai pas relu l'additif 1 au complément v3** : ses chiffres (131,66 et 24,90 USD) sont cités d'après la contre-lecture.

**PD7 — La mère a-t-elle lu une réponse brute ?** *Décision* : la mère le dit, par oui ou par non, avant le scellement. *Enjeu* : GO-2026-11-21-20 dit « avant toute lecture par la mère », ce qui n'exclut pas une lecture ensuite ; la liste écrit « la mère ne lit jamais ». *Options* : (a) non : la liste vaut ; (b) oui : inscription sous « ont lu avant la liste », arrêt n° 17, nœud de Lazar. *Recommandation* : aucune ; c'est un fait à dire.

**PD8 — L'annexe des objets de contrôle : son lieu, et qui écrit ses textes.** *Décision* : où verser l'annexe et ses textes pour que les deux lecteurs ne les ouvrent pas ; et qui écrit les textes inertes. *Enjeu* : sur `main` ou dans la quarantaine de la course, les lecteurs peuvent la lire ; la v1 faisait écrire les textes par la mère, alors que les épreuves sont conçues par un concepteur. *Options* : (a) une branche à part, non liée à `main`, lue par le programme de fin et par Lazar, son empreinte seule sur `main` ; textes écrits par un concepteur neuf, contre-lus, scellés par la mère ; inconvénient : une branche de plus à tenir. (b) Sur `main`, avec un interdit au mandat des lecteurs ; avantage : simple ; inconvénient : un interdit ne ferme rien. *Recommandation* : (a), confiance 0,6. Dans l'attente, **ne pas verser l'annexe dans un dossier que les lecteurs ouvrent**.

**PD9 — La source des octets de l'identifiant de ligne.** *Décision* : comment le lot 10 a construit l'identifiant de ligne. *Enjeu* : s'il se tire, c'est une méthode de tirage de plus (V9, l. 311) ; s'il se calcule sur l'énoncé, un lecteur peut le recalculer et voir quelle ligne ne vient pas du registre. *Options* : (a) le rang de la ligne dans le registre servi, réencodé ; pour une ligne de contrôle, un rang pris à la suite ; inconvénient : un identifiant élevé trahit une ligne ajoutée. (b) L'empreinte de l'énoncé, tronquée et réencodée ; inconvénient : recalculable. *Recommandation* : aucune ferme ; je n'ai pas lu le lot 10 a. L'additif pose la contrainte (§ 10, valeur 10).

**PD10 — La borne de sortie et la règle permanente de GO-2026-11-21-47.** *Décision* : vérifier si le relais du juge de l'espèce 1 sert le modèle que cette règle nomme. *Enjeu* : elle veut un plafond de sortie large, « au moins 16 000 jetons de texte après la réflexion » ; la borne d'ici est de 16 000 jetons au plus, réflexion comprise. *Options* : (a) garder la borne ; le juge peut rendre des appels « illisibles », comptés ; (b) relever la borne et le plafond pour ce relais : version neuve et montant neuf. *Recommandation* : la mère constate d'abord ; si c'est ce modèle, (b), confiance 0,55.

**PD11 — Où se déclare l'extension de l'arrêt n° 12 à la ligne à part.** *Décision* : par cet additif, ou par la pièce de relevés. *Enjeu* : l'additif 1 a fait déclarer au complément de valeurs les extensions de l'arrêt n° 12 à d'autres clés (son § 7) ; la conception v5 (§ 2.14) dit que sa première clause lit le plafond de la ligne. *Options* : (a) par cet additif (§ 9, arrêt C) — c'est la v2 ; (b) par une ligne de la pièce de relevés, l'additif y renvoyant. *Recommandation* : (a), confiance 0,6.

## 4. Décisions ouvertes

Elles reprennent D1 à D8 du rapport de la v1 (`b507e48c…`), complétées (C4), et en ajoutent cinq. Défaut sous 48 heures : la recommandation, sauf là où c'est dit.

| n° | décision | enjeu | options (avantage ; inconvénient) | recommandation | défaut |
|---|---|---|---|---|---|
| D1 | allumer la lecture de fin après la clôture (Lazar) | sans elle, la matière reste gardée et jamais lue | (a) allumer, 16,00 USD au plus : la comparaison existe, gelée d'avance ; deux lecteurs écartés pour de bon des moniteurs. (b) Ne pas allumer : rien ne sort de la branche ; la matière n'est éprouvée que plus tard | (a), 0,65 | aucun : dépense |
| D2 | ce que rendent les juges | la conception dit « classement » | (a) trois étiquettes par ligne : appels indépendants, contrôles nets ; ce n'est pas un classement. (b) Un classement en un appel : la lettre ; un appel illisible ne laisse rien, un rang invite à comparer. (c) Ne pas jouer les juges : zéro dollar ; écart à « les juges de fin sont quatre » | (a), 0,6 | (a) |
| D3 | épinglage au manifeste de la lecture de fin, sous l'arrêt n° 14 étendu ; l'épreuve du lot 10 a (conception v5, § 6.2 : « sans additif épinglé ») y lit l'empreinte | l'épingler dans la configuration de la course la changerait après son scellement | (a) manifeste propre : la course n'est pas touchée ; un manifeste de plus. (b) Dans la configuration, si la course n'est pas partie : une seule configuration ; le départ attend l'additif | (a), 0,7 | (a) |
| D4 | lecteurs d'avant la liste : inscrits sous « ont lu avant la liste », avec l'exclusion ; la mère dit si elle a lu (PD7) | sinon une session qui a lu peut écrire un mandat de moniteur sans que rien le dise | (a) les inscrire : l'exclusion est vérifiable ; des noms de plus. (b) Constater seulement : plus léger ; rien ne se vérifie | (a), 0,75 | aucun : touche la quarantaine, Lazar |
| D5 | étiquettes par identifiant, des lecteurs et des juges : en quarantaine, à Lazar et au programme ; à la mère des comptes | « cette visée est sans antériorité trouvée » sert qui conçoit des moniteurs | (a) comme écrit : rien d'utile à un moniteur ne passe par la mère ; Lazar doit lire en quarantaine. (b) À la mère aussi : un seul régime ; la mère écrit des mandats de moniteurs | (a), 0,7 | (a) |
| D6 | mise en case de chaque ligne par chaque lecteur | sans elle, moins de requêtes que pour une fiche, ce qui pousse vers « aucune antériorité trouvée » | (a) la garder : même effort ; un jugement de plus, non contrôlé. (b) L'ôter, et écrire la réserve : plus simple ; effort inégal | (a), 0,6 | (a) |
| D7 | garde de motifs : voir PD2 | — | — | — | aucun |
| D8 | tarifs et tailles relevés avant la demande | condition de l'arrêt A, non une option | — | — | — |
| D9 | bornes : 120 000 octets ; 16 000 jetons ; règle de la borne de sortie ; plancher de 2 000 jetons | ce sont elles qui font le plafond de 16 USD | (a) comme écrit : plafond ferme à tout tarif ; un juge cher ne part pas. (b) Bornes fixées après le relevé des tailles : mieux ajustées ; l'additif attend le relevé, ou change après scellement. (c) Plancher plus haut ou plus bas : valeur du concepteur, sans mesure | (a), 0,6 | aucun : dépense |
| D10 | objets de contrôle de fin dans une annexe à part (PD8) | des contrôles que le contrôlé connaît n'éprouvent rien | (a) annexe à part : la fuite par le mandat est fermée ; une pièce et un lieu de plus. (b) Aucun contrôle des lecteurs, et le dire : simple ; rien n'éprouve leur soin | (a), 0,7 | (a) |
| D11 | recoupement : deux lecteurs, un identifiant commun, sinon « non tranché » | la conception dit « une étiquette fermée d'un lecteur » | (a) deux lecteurs : un désaccord ne fait pas un recoupement ; plus de « non tranché ». (b) Un seul : la lettre ; aucun contrôle | (a), 0,65 | (a) |
| D12 | un appel par réponse brute, plutôt qu'un seul pour les trois | forme des appels des juges | (a) un par réponse : un refus n'emporte qu'un texte, la requête tient sous sa borne ; six appels au lieu de deux. (b) Un seul : moins d'appels ; une requête trois fois plus longue, et un refus emporte tout | (a), 0,7 | (a) |
| D13 | unité : la ligne du registre servi | « chaque visée » n'est pas défini ailleurs | (a) la ligne : comptable par programme ; dépend du champ « visée ou défense ». (b) Un découpage par les lecteurs : plus fin ; non rejouable | (a), 0,75 | (a) |

## 5. Relevé de méthode

**Chaîne de raisonnement.** Elle est écrite à l'additif (§ 11, quatorze pas), au devis (§ 6, neuf pas), à la liste (cinq pas), à l'annexe (quatre pas) et à la table des corrections (quatre pas) ; ce rapport n'y ajoute que deux pas. 1. Les pièces v2 forment une chaîne : l'additif cite le texte servi par son empreinte (`bbb50f64…`) et la sortie du calcul par la sienne (`941c18a3…`) ; le devis cite le programme, les entrées et la sortie par leurs empreintes ; vérifiable par `sha256sum -c` sur les compagnons. 2. Chaque point délicat du § 3 renvoie à la lettre qu'un autre choix toucherait (V9, l. 311, 328, 387, relues ; additif 1, § 2 et § 7, relus ; conception v5, § 2.14 et § 2.15, relus ; GO cités, relus).

**Objets de contrôle.** Ceux de l'annexe (non joués, aucun appel n'étant permis) et du calcul (huit scénarios et un fichier d'entrées faux, joués, conformes). Faux par construction : la ligne étrangère, le tarif hors repère, la requête d'un octet hors borne, les tarifs qui mettent la borne sous son plancher, l'attendu faux. Vrais par construction : la ligne « redite », le pire égal au plafond, les trois tarifs où l'appel part.

**Premier pas non justifié.** À l'additif, le pas 12 (le champ « visée ou défense ») ; au devis, le pas 7 (un jeton par octet au pire) ; à la liste, le pas 5 (les lecteurs d'avant) ; à la table, le pas 3 (l'additif 1 au complément, non relu).

**Mode d'échec affecté.** Sans objet : je suis concepteur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.** Trois, notées à l'additif (§ 11) : le reste de Minuit depuis GO-2026-11-21-28 et -30 ; la règle de plafond de sortie de GO-2026-11-21-47 ; GO-2026-11-21-21, qui dit GO-2026-11-21-19 « sans matière rédigée », ce qui répond à la trouvaille de côté de la contre-lecture. Aucune n'est poursuivie.

**Évaluateur et conseil.** Le contre-lecteur O, à la vérification des corrections, sur la table et les différentiels. Par où ce lot pourrait être reçu sans le mériter : une correction dite « portée » et mal portée ; un point délicat rangé à tort parmi les choix sans écart (PD5, PD11) ; les chiffres de Minuit, que je n'ai pas tous relus. Conseil à la mère : lire d'abord PD7 et PD8, qui conditionnent le scellement ; puis PD6 et PD10, qui conditionnent la demande à Lazar.

— concepteur neuf des corrections, modèle F
