# Vérification du programme des deux essais d'admission du bras A — livraison 3 (fichiers `_v2`) — v1

- **Vérificateur** : Claude Opus 5.5, le contre-lecteur des livraisons 1 et 2, le 2026-11-21. N'a écrit ni le devis, ni le programme, ni ses essais.
- **Objet** : le commit `70715d3b0` et sa note `note-programme-essais-admission-bras-a-v2.md`. Les six fichiers `_v2` répondent « OK » à leur compagnon : chef d'essai (2 913 lignes), relais de Mistral, relais de Google, faux fournisseur, essais, gabarit de configuration `…-v2-gabarit.json`.
- **Essais** :
  - la commande imposée (`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 … tests/test_chef_essais_admission_bras_a_v2.py`), quatre fois : **152 passés à chaque fois** (72 à 73 s) ;
  - sous charge (huit boucles de calcul sur quatre cœurs, trois suites en parallèle), les essais sensibles au temps : **159 sur 159**, dont 75 rejeux de l'essai de la borne en octets (garde 19), qui échouait 2 fois sur 180 à la livraison 2 ;
  - quatre essais jetables neufs, hors du dépôt.
- **Interdits tenus** : aucun réseau hors de la boucle locale, aucune clé, `GO_ID` jamais fixé, aucun chemin interdit, rien écrit dans le dépôt hors ce rapport, rien scellé.

## Verdict

**Engageable sur le devis accepté (`421ee2e6…`), sous trois mineurs ; non engageable tel quel sur la décision de Lazar GO-2026-11-21-68 sans la livraison 4.** Toutes les corrections demandées sont fermées et éprouvées. Le neuf (verrou, coupure brutale, code 7 bloquant, code 8) ne fait partir aucun envoi en double dans les cas éprouvés. Je trouve deux blocages sans issue simple : le numéro de processus de l'amorce repris après un redémarrage (m-1), et une fausse alerte de clé qui ne se lève qu'en révoquant la clé (m-2). La livraison 3 ignore l'avenant 1, déjà committé : la recharge automatique gardée y est refusée par la garde 9 (section 5).

## 1. Ce qui devait être fermé

| point | fermé ? | appui |
|---|---|---|
| **V-1** commande `rapport` pendant une file | **oui** | mon essai, rejoué avec une amorce vivante : rien n'est écrit, `regles` refuse une file non close ; après l'événement « fin », `rapport` écrit et `regles` rend « tient » |
| **m-a** deux lancements simultanés | **oui** | verrou exclusif `flock`, gardes rejouées sous le verrou ; essai du dépôt, rejoué quatre fois sous charge ; réserve m-3 |
| **m-b** coupure de l'amont | **oui** | `SO_LINGER` à zéro avant la dernière fermeture, après une coupure (client parti ou délai) ; une fin déjà envoyée par `shutdown` est suivie d'une remise à zéro (Linux remet à zéro depuis `FIN_WAIT2` à la fermeture brutale) |
| **m-c** code 7 sans suite | **oui** | `garde_cle_vue` relit tous les dossiers du fournisseur avant tout départ ; essai du dépôt ; réserve m-2 |
| **m-10** essai manquant | **oui** | essai versé |
| **m-15** vérification du devis à `null` | **oui** | une configuration définitive exige la pièce, à son empreinte et à son compagnon |
| **Devise affichée** | **oui** | deux lignes obligatoires au constat ; en devise autre que USD, la conversion est exigée pour chaque montant de ce fournisseur ; en USD, elle est refusée |
| **Âge du taux** | **oui**, réserve m-4 | 24 heures au plus |
| **Marge de change** | **oui** dans le programme | paramètre exigé en configuration définitive ; une marge à 0 y passe (essai `test_v3_…`) : sa valeur doit venir d'un mot de Lazar cité par la configuration |

## 2. Le neuf : recherche d'un blocage sans issue ou d'un envoi en double

- **Code 8** (rapport que l'amorce n'a pas écrit) : sain. Avec V-1, seule une main étrangère peut écrire ce rapport pendant la file. `regles` confronte ensuite le rapport scellé au journal (six compteurs) : un rapport étranger mais juste sert quand même, ce qui n'est pas un blocage.
- **m-1, blocage** (`file_close`, `:2861-2868`), éprouvé par `test_v2_pid_reutilise_la_file_ne_se_ferme_jamais`. L'amorce meurt sans écrire « fin » (machine relancée). Son numéro de processus est ensuite repris par un autre processus vivant, ce qui est probable dans un conteneur, où les numéros recommencent bas. `file_close` reste faux : ni `rapport` ni `regles` ne concluent, tant que ce processus vit. **Exiger** : consigner au manifeste l'heure de démarrage du processus (`/proc/<pid>/stat`, champ 22) et l'identifiant de démarrage de la machine (`/proc/sys/kernel/random/boot_id`). La file est close si l'un diffère.
- **m-2, blocage coûteux** (`:819-840`) : une forme de clé trouvée par la relecture de fin de ligne ne se lève qu'avec « clé révoquée et remplacée : oui ». La relecture couvre aussi les réponses brutes gardées. Une réponse de modèle qui porterait par hasard une chaîne `AIza…` ou `Bearer …` force donc la révocation d'une clé saine, puis un constat neuf. **Ajouter** une seconde forme de levée : « faux positif : la chaîne n'est pas la clé », admise seulement si le relais n'a pas vu la valeur exacte (`cle_vue_dans_la_reponse` faux) pour ce dossier.
- **m-3, envoi en double possible** (`:2730`) : le verrou est tenu par l'amorce seule. L'ouvrier (sans `pass_fds`) et le relais (session neuve) ne le tiennent pas. Si l'amorce est tuée net, l'ouvrier orphelin continue d'envoyer par son relais, pendant que le verrou est rendu et qu'un lancement neuf de la même ligne de vérification lit un journal encore en cours d'écriture. Pour une file, la garde 13 arrête ce lancement neuf ; pour une vérification, non. **Exiger** : passer le descripteur du verrou à l'ouvrier (`pass_fds`), pour que le verrou vive tant que vit l'un des deux, et poser un verrou par fournisseur plutôt que par ligne. Aujourd'hui, une seconde vérification de Google peut tourner pendant la file Neon, sur le même solde, sans que la garde 10 le voie.
- **Coupure brutale** : rien d'autre à redire. La voie réelle, chiffrée, reste non éprouvée ; `SO_LINGER` s'applique à la prise brute, donc aussi sous chiffrement.

## 3. L'essai de la garde 19 sous charge

75 rejeux de l'essai de la borne en octets et 8 de la fermeture pendant un silence, dans les conditions où la livraison 2 échouait : **aucun échec**. L'essai attend les deux événements, la ligne `client_ferme` du journal du relais puis la fermeture vue par le faux fournisseur, et la remise à zéro est immédiate. L'essai du délai total du relais de Mistral (m-11), celui du délai global et celui du verrou passent aussi sous charge. L'instabilité est close.

## 4. L'âge du taux, compté depuis l'heure de la pièce

**Acceptable sur le fond** : on convertit le montant vu à l'heure où il a été vu ; c'est donc l'heure de la lecture qui compte, non celle du lancement. L'âge du solde lui-même, que rien ne borne, est une autre question, que tient déjà le contrôle par la dépense comptée (garde 10). **Une gêne pratique (m-4)**, éprouvée par `test_v4_…` : un taux relevé **après** l'heure de la lecture est refusé, même cinq minutes après. Or la session relève d'ordinaire le taux une fois que Lazar lui a dit le montant. **Admettre** un taux pris jusqu'à 6 heures après l'heure de la pièce, en plus des 24 heures avant.

## 5. Ce qui gênera la livraison 4 (GO-2026-11-21-68 : file du juge coupée entre deux clés Google, recharge automatique gardée, sans plafond mensuel, constat ligne par ligne abandonné)

1. **L'avenant 1 n'est pas intégré.** Il a été committé avant la livraison 3 (`9dee27629`, « recharge gardée, deux clés »), et le programme ne cite que le devis `421ee2e6…`. La clé `google_recharge_automatique` n'admet que `désactivée` ou `non proposée` : avec la recharge gardée, la garde 9 refuse **toute** ligne, Mistral comprise, puisque le constat est lu en entier.
2. **Une clé par fournisseur** : `fournisseurs.google.variable_cle` vaut le seul `GEMINI_API_KEY`. Le relais, le lanceur (`!GEMINI_API_KEY`), l'état initial du relais et le manifeste n'en connaissent qu'une. `GEMINI_API_KEY_2` n'est nommée nulle part : il faut une clé par ligne.
3. **Une seule file Neon, en dur** : les constantes `LIGNES` (cinq lignes), `ENTREES_NEON` (huit entrées, un seul ordre), `CRITERES["file-neon"]` (huit lectures, huit conformes) et `ROLES`. La garde 17, la garde 13 (une file, un dossier), le rapport et `appliquer_regles` travaillent par dossier. Couper la file en deux demande deux lignes de file, et un verdict « huit sur huit » réuni sur deux rapports, qui n'existe pas aujourd'hui.
4. **Une seule vérification de Google** (`verification-google`) : il en faut une par clé. Le relevé, la garde 10 (`releve_verification`, `inscrit`) et la garde 15 supposent une vérification par fournisseur.
5. **Tout est compté par fournisseur, non par clé ni par projet** : `lignes_jouees`, la garde 20 (lecture de la console), la garde 10 (crédit du constat moins dépense comptée, sur `google_credit_utilisable_usd`, une seule valeur) et les alertes de clé (m-c, qui bloquent les deux clés). Avec deux projets ou deux comptes de facturation, il faut un crédit, une dépense comptée et une console par clé.
6. **Constat ligne par ligne abandonné** : la garde 9 lit un constat à treize clés pour chaque ligne et exige une conversion datée de 24 heures au plus avant **le lancement** (lecture retenue à la livraison 3, à ma demande). Avec un constat unique, cette règle oblige à refaire le constat chaque jour. Il faudra dater le taux depuis la transcription du constat, ou sortir le crédit du constat.
7. **Recharge automatique sans plafond mensuel** : le raisonnement du devis où « le solde prépayé borne la perte » (6.4) tombe. Les seuils de 19,76 et de 16,08 USD (garde 9, garde 10, garde 20) ne bornent plus rien et ne font plus que retarder. Seuls restent le compteur et la lecture de la console : à réécrire avec l'avenant 2, non à garder par inertie.

## 6. Ce que j'ai ouvert

- La note de livraison 3, en entier.
- Le chef `_v2`, aux sections : conversion et constat (lignes 440 à 632), gardes 20, 7 et 8 (lignes 751 à 860), crédit vu de la garde 10 (lignes 925 à 950), règles (lignes 2365 à 2396), amorce, verrou et fin (lignes 2637 à 2700 et 2760 à 2800), `file_close` et `rapport` (lignes 2861 à 2884), plus un index des fonctions et des recherches de lignes.
- Les deux relais `_v2` : la coupure brutale et les séquences de fermeture.
- Dans les essais `_v2` : le banc (`jouer`), les essais V-1 et l'index des noms.
- Le gabarit `_v2`, lignes 100 à 112, et des recherches de lignes.
- `git log` et `git status` (un fichier non suivi, l'avenant 1 en `-v2`, non ouvert) ; empreintes par `sha256sum -c`.
- Lus par programme pendant les essais, comme avant : le lot des entrées nommé par le devis, les consignes et les règles du préenregistrement par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
- Bloc-notes, hors du dépôt : `essais_jetables_l3/test_livraison3_jetable.py` et `test_charge_v2_jetable.py`, avec leurs sorties.
