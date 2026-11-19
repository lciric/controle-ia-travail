# Vérification du brouillon 25 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 24. Je juge ; je ne corrige rien.
- **Texte vérifié** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md`, `ab5fc58ee698…`. Note : `3732b6b42e8b…`. Les deux compagnons sont vérifiés.
- **Pièces lues** :
  - l'avis du rédacteur sur les défauts du code de la version 6 (`24f4f9b3…`) ;
  - la vérification du code de la version 6 (`4a6e1b41…`), ses parties C-1, C-2, C-3, M et 7 ;
  - le relevé des défauts trouvés en écrivant la version 7 (`defauts-du-texte-trouves-en-codant-v7.md`).
  - Aucun code ouvert.
- **Méthode** : différence phrase par phrase entre les brouillons 24 et 25, faite par programme. J'ai lu les 23 blocs touchés et leur contexte.

## Verdict : **engageable après corrections**

- **Aucune règle de jugement n'est changée.** Par programme :
  - la section 12, la section 7.5, la ligne A17, toute la table A (7.2), les tables B et C (7.3 et 7.4), et 7.6 à 7.8 sont identiques au brouillon 24 ;
  - les fiches parties (9 à 12) restent mot pour mot dans le texte.
- Ce que le brouillon 25 ajoute est de trois sortes :
  - des gardes de forme ;
  - des fichiers nommés ;
  - des précisions de procédure, sur une reprise et sur le statut d'un fichier scellé.
- **Une chose doit pourtant partir à Lazar, comme information et non comme fiche, avant qu'il réponde à la fiche 12** (C-1). Depuis l'envoi de cette fiche, la liste des causes de refus d'une livraison est écrite et fermée, et elle compte des causes de plus. Sous l'option (a), chacune fait tomber l'issue du résultat principal.
- Restent :
  - une tolérance du contrôle des valeurs p plus large que ce qu'elle doit tolérer (C-2) ;
  - une règle de dossier contredite par la routine du dépôt (C-3) ;
  - une série de précisions venues du relevé de la version 7 (C-4).
- **Aucune fiche neuve n'est nécessaire.**

## 1. Les changements, regardés un à un

| changement | règle de jugement ? | avis |
|---|---|---|
| **Liste des refus déclarée fermée**, avec cinq contrôles neufs : valeur p contre ses comptes ; lecture hors de sa place ; nombre impossible ; borne sans quantile ; borne remplie au cas E | **non** : ce sont des gardes de forme ; aucun état, seuil ni issue ne change ; ce que vaut un refus reste la seule question du point 21 | La fermeture de la liste est un progrès : avant, le code refusait pour des causes que le texte ne disait pas, ce que la vérification du code avait relevé. Mais sous l'option (a) de la fiche 12, chaque cause peut ôter son issue au désappariement, et Lazar répond sur une fiche partie quand la liste était plus courte et non écrite : **information à joindre (C-1)**. Les artefacts et les cas sains sont écrits en 8.4 (R5). |
| **Liste fermée des refus du fichier des scores par unité** ; valeurs de `dose` et de `condition` lues dans la configuration ; `tache`, `episode` et `pas` non contrôlés | non | Bon : les formes devinées sont retirées du code. Quelques natures et cas sont à préciser (C-4). |
| **Tolérance d'un demi-pas de la grille** pour la valeur p contre ses comptes ; la valeur rendue est prise telle quelle | **non par rapport au brouillon 24**, qui n'exigeait aucun accord entre la valeur p et ses comptes ; c'est une garde de plus | Elle est trop large pour sa raison d'être. Dans la marge qu'elle tolère, une valeur rendue, prise telle quelle, peut franchir un niveau de Holm que la formule ne franchit pas : **C-2**. |
| **« Une ligne de GO n'ouvre qu'une livraison refaite »**, sans plafond | non : c'est la règle écrite, « aucune livraison n'est refaite sans un mot de Lazar », appliquée à chaque livraison ; le texte le dit expressément | Juste. C'est la seconde des deux lectures que proposait la vérification du code (C-2) ; Lazar garde la main à chaque livraison. Un écart entre 6.9 et 8.4 est à corriger (C-4). |
| **Acte de reprise**, scellé avant la lecture d'une livraison refaite | non : c'est une procédure qui lie une ligne à une livraison | Juste. Il fait paraître un cas, la panne entre l'acte et la fin de la lecture, que le texte doit dire (C-4, point A.1). |
| **Statut du fichier de l'étape (m)** après un arrêt à l'étape (n), une valeur par rédaction de la fiche 12 | non : l'issue de chaque rédaction ne change pas | Le statut sous (a), « rapporté tel quel, non opposable », est la lettre de A17 et de 7.5. Sous (c), « inchangé, opposable », c'est l'option elle-même. Sous (b), « non opposable : discrétion non lue », le contenu est rapporté sous cette marque : c'est **une lecture du mot « retirée » de la fiche 12**, que l'avis proposait de joindre à la fiche. À dire à Lazar (C-1). Elle est sans risque de retouche : la livraison refaite exige le même calcul et les mêmes graines, donc une table C identique. |
| **Fichiers nommés** (configuration, constats de l'étape (m), fichier d'arrêt, acte de reprise) | non | Juste. La configuration est contredite par le code, qui a trois parties, et une configuration par livraison manque (C-4). |
| **Dossier « que rien ne parcourt »** pour le fichier des scores par unité | non | La règle, telle qu'écrite, est violée par la routine du dépôt : **C-3**. |
| **Section 10** : « restent prononcés », « reste prononcée » | non | Ma remarque M-1 du brouillon 24 est tenue. |
| **Trace d'appel** : l'enchaînement ne tire de l'exception que son constat | non | Juste ; c'est un cloisonnement. |

## 2. Défauts à corriger

**C-1. Une information pour Lazar, avant sa réponse à la fiche 12.**
- **Endroit** : 6.9, « Liste fermée » et « Cinq écarts de structure de plus » ; « Statut du fichier scellé de l'étape (m) ».
- **Pourquoi** :
  - La fiche 12 dit seulement que « le texte fait contrôler la forme de ces nombres par des gardes ». Depuis son envoi, la liste est écrite et fermée. Elle porte cinq causes de plus pour les lectures, et une liste neuve pour le fichier des scores par unité.
  - Sous l'option (a), chacune de ces causes rend le désappariement « non prononcé ». La vérification du code l'avait relevé : « la réponse de Lazar à la fiche 12 porterait sur un ensemble de causes plus large que celui qu'il lit ».
  - Le texte lit aussi « retirée » (option (b)) comme « conservée, citée et rapportée telle quelle sous la marque « non opposable » ».
  - Ni l'une ni l'autre ne change les options. Lazar doit pourtant les avoir sous les yeux.
- **Ce qui le réglerait** : un message à Lazar, à joindre aux fiches parties, sans nouvelle question. Il pourrait dire :
  > Depuis l'envoi de la fiche 12, la liste de ce qui fait refuser une livraison du côté habilité est écrite au texte et fermée : rien d'autre ne la fait refuser. Elle compte, en plus des fautes de forme déjà dites, cinq contrôles : une valeur p qui ne répond pas à ses comptes ; une lecture rangée hors de sa place ; un nombre impossible (une aire hors de 0 à 1, une valeur p nulle ou au-dessus de 1) ; une borne sans son quantile ; une borne rendue là où aucun tirage n'est possible. S'y ajoute une liste pour le fichier des rangs. Sous l'option (a) de la fiche 12, chacune ôte son issue au résultat principal ; sous (b) et (c), seule la discrétion est touchée. Par ailleurs, sous l'option (b), « retirée » veut dire que la table de discrétion déjà scellée reste conservée et citée, rapportée telle quelle sous la marque « non opposable », sans être un résultat. Rien n'est supprimé.
- Les deux remarques de la note, partie 5 (couple des fiches 11 et 12 ; règle de reprise fixée d'avance), partent avec ce message.

**C-2. La tolérance du demi-pas est plus large que l'arrondi qu'elle doit tolérer.**
- **Endroit** : 6.9, écart de structure (i) : « d'un demi-pas de sa grille ou plus, soit de 1 ÷ (2 × 2 001) … ; en deçà, la valeur rendue … est prise telle quelle, jamais recomposée ; il tolère un arrondi à quatre décimales ou plus ».
- **Pourquoi** :
  - Un arrondi à quatre décimales écarte d'au plus 0,00005. Le demi-pas de la valeur p haute vaut 1 ÷ 4 002, environ 0,00025, cinq fois plus.
  - Exemple, calculé : avec 6 aires au moins égales, la formule donne 7 ÷ 2 001 ≈ 0,003498. C'est au-dessus du premier niveau de Holm, 0,05 ÷ 15 ≈ 0,003333. Une valeur rendue de 0,0033 est à moins d'un demi-pas, donc acceptée, et prise telle quelle : elle passe ce niveau.
  - La tolérance laisse donc une valeur rendue, qui ne vient d'aucun arrondi déclaré, décider d'un « repère » contraire à la formule. La valeur p basse a le même écart, face au seuil de 0,05 de la condition (a).
  - Ce n'est pas un recul par rapport au brouillon 24, qui ne contrôlait rien. C'est donc à corriger, sans bloquer.
- **Ce qui le réglerait**, l'une ou l'autre :
  - (i) une tolérance égale à la moitié de la dernière décimale que le module déclare rendre (demande 13 de 13.1), plafonnée au demi-pas, et inscrite dans la configuration scellée avant la réception ;
  - (ii) garder le demi-pas, mais tenir pour écart de structure toute valeur rendue qui tombe, par rapport au niveau de Holm qui s'applique à elle ou au seuil de 0,05 de la condition (a), de l'autre côté que la valeur de la formule.
- Je préfère (i). Ce sont des gardes, à éprouver en 8.4. Aucune fiche.

**C-3. Le « dossier que rien ne parcourt » est parcouru par la routine du dépôt.**
- **Endroit** : conventions, ligne 172 : « aucun programme ne lit « tous les fichiers » de ce dossier ni d'un dossier qui le contient » ; 13.2, ligne 1296.
- **Pourquoi** :
  - La routine de reprise de chaque session (R14 ; `python -m controle_ia.scellement verifier-arbre .`) parcourt tout le dépôt. Elle lit, pour en prendre l'empreinte, tout fichier qui a un compagnon, donc ce fichier scellé.
  - Git en fait autant à chaque versement, et le texte exige de « récupérer ce qui est récupérable » (8.5).
  - La règle, à la lettre, est donc violée chaque jour, ou bien le fichier doit vivre hors du dépôt, ce que le texte ne dit pas.
- **Ce qui le réglerait** : borner la règle au contenu. « Aucun programme n'en lit le contenu, hors le programme de l'aire conditionnelle par son chemin exact ; les outils de scellement et de version n'en prennent que l'empreinte et ne l'affichent pas ». Ou bien dire où le fichier vit, s'il vit hors du dépôt.

**C-4. Les précisions venues du relevé de la version 7 du code.** Aucune ne change une règle de jugement, et aucune ne demande de fiche. Le détail point par point est en partie 3.

## 3. Le relevé de la version 7 : précision au texte, fiche, ou rien

| point du relevé | ce qu'il faut | ce qu'il faudrait écrire |
|---|---|---|
| **A.1 Panne entre l'acte de reprise et la fin de la lecture** | **précision au texte** | « Lue une fois, sans relecture » vise la retouche. Une lecture interrompue avant tout résultat écrit (aucun état, aucun fichier de l'étape (m) scellé, aucun résultat ouvert) n'est pas une lecture. Elle se rejoue à l'identique, sous le même acte, avec les mêmes pièces et la même configuration ; le rejeu est consigné et rapporté. Dès qu'un résultat est écrit, c'est une relecture, refusée. C'est la règle de 8.6 pour un transport interrompu, appliquée à l'analyse, qui est déterministe ; elle met la livraison refaite au même régime que la première, que rien n'empêche de rejouer après une panne. Si le rédacteur préfère la lecture stricte (la discrétion reste « non lue » après une panne), c'est l'issue d'un cas : il faudrait alors une fiche. Je ne la recommande pas. |
| **A.2 Révocation de la ligne de GO après la lecture** | **précision d'une phrase** | « La lecture se fait sous la ligne valide au moment où l'acte de reprise est scellé. Une révocation postérieure est consignée et rapportée ; toute suite est un nœud de Lazar. » Lazar garde la main, rien n'est décidé à sa place : pas de fiche. |
| **B.3 Configuration en trois parties** (`pieces_attendues` : empreinte du registre des accords, empreinte du module) | **précision au texte** | « Deux parties et elles seules » devient trois, et la troisième est nommée. Attention à l'empreinte du registre : le registre change à chaque ligne neuve. Il faut dire de quel état du registre elle est l'empreinte (celui qui porte la ligne qui ouvre la livraison) et comment l'instance, qui est sans réseau, le reçoit. |
| **B.4 Une configuration par livraison** | **précision au texte** | Une livraison refaite a sa configuration, scellée et inscrite avant sa réception, avec l'empreinte du module corrigé. Son nom (ou son dossier) la distingue de la première, qui n'est jamais réécrite (R12). |
| **B.5 Noms des deux chaînes de plus** | **précision au texte** | `doses_du_fichier_des_scores`, `condition_de_l_honnete_du_fichier_des_scores`, ou d'autres noms, mais écrits. |
| **B.6 6.9 et 8.4 ne disent pas la même chose de la ligne de GO** | **précision au texte** | Aligner 6.9 sur 8.4 : la ligne doit citer le module corrigé que la configuration de la livraison refaite inscrit. Dire si l'empreinte du rapport de contre-lecture est seulement exigée ou aussi vérifiée, et contre quoi. |
| **B.7 Empreinte entière ou abrégée** | **précision au texte** | Une empreinte entière de 64 signes. Le registre abrège d'habitude : la ligne d'une reprise doit faire exception, et il faut le dire à la session qui inscrit. |
| **B.8 Quel fichier d'arrêt** | **précision au texte** | La ligne cite un seul fichier d'arrêt, dont la livraison n'a pas encore d'acte de reprise. |
| **B.9 Le rapport compte les livraisons lues** | **précision au texte** | La première livraison ne laisse aucune trace dans le dossier des arrêts. Le compte se fait sur les constats de l'étape (m), un par livraison lue, et sur les actes. |
| **B.10 Trois défauts sans nature écrite** (dix bons champs hors d'ordre ; un champ de plus et un de moins ensemble ; une clé en double à l'intérieur d'un champ non contrôlé) | **précision au texte** | Ajouter à la liste fermée des natures « champs hors d'ordre » et « champs remplacés » (un de plus et un de moins). Pour une clé JSON en double n'importe où dans la pièce, écrire qu'elle rend la pièce **illisible**, et l'ajouter à la liste fermée des écarts, avec son artefact. Sinon le code refuse pour une cause que la liste fermée ne nomme pas, ce qui est exactement le défaut que le brouillon 25 corrige. |
| **B.11 `lectures` : liste ou table** | **rien pour l'instant** | Attend la réponse du développeur habilité (demande 14). |
| **B.12 Nom et compagnon du fichier des scores : refus sans événement** | **précision au texte** | Ils sont dans la liste fermée : ce sont des refus de l'étape (n), qui lèvent l'événement d'arrêt comme les autres, avec un fichier d'arrêt. Ou bien il faut les retirer de la liste et dire qu'ils sont une garde ordinaire. Le choix entre les deux ne change aucune issue au-delà du point 21. |
| **B.13 `scores_par_unite.fichier` non lu** | **précision au texte** | Dire qu'il n'est pas lu, comme `forme`, puisque le nom est contrôlé sur le fichier lui-même. |
| **B.14 Fichier vide annoncé tel** | **précision au texte** | Il est lu ; chaque aire conditionnelle est « non calculable », avec son motif, sans arrêt. C'est cohérent avec la règle déjà écrite pour un pli sans ligne retenue. |
| **B.15 « `cle` vide »** | **précision au texte** | Dire ce qui est vide (`null`, texte vide, liste ou objet vide) et qu'une clé qui n'est pas un texte est admise. |
| **B.16 Jointure impossible par `tache` et `episode`** | **précision au texte** | Aire conditionnelle « non calculable », avec ce motif, sans arrêt. C'est une grandeur rapportée sans verdict, comme les autres. |
| **B.17 Le dossier des arrêts est listé par le programme** | **précision au texte** | Le fichier des scores par unité ne se range ni dans le dossier des arrêts ni sous lui (lié à C-3). |
| **B.18 Les constats n'ont pas les deux réglages de la table A** | **précision au texte** | Ajouter deux champs (« révision refusée », « tâches gardées lues »), ou dire qu'ils sont dans le journal relu. Sinon, la relecture des constats ne voit pas un premier échec dont la révision a été refusée. |
| **B.19 Chemins cloisonnés de la garde statique** | **rien au texte** ; à la session principale | Demande 17 de la note. |
| **C.20 Tolérance tirée du texte, non de la configuration** | **rien** pour la source de la grille (le texte fixe 2 000 permutations, déjà exigées des réglages) | Mais la largeur de la tolérance est à revoir : C-2. |

## 4. Mineurs

- **M-1. Sous la rédaction (a) de la fiche 12, ce que rétablit une reprise réussie n'est pas écrit.** Sous la ligne A17, rien n'est prononcé, et la « reprise par nœud » est permise. Une livraison refaite lue avec succès rend-elle les issues de 7.5 prononçables ? Ce point date du brouillon 23 ; il ne demande rien avant le mot de Lazar. Si Lazar retient l'option (a), la ligne qui se reporte au scellement (case « nœuds » de 13.1) doit le dire.
- **M-2. Les refus qui ne sont pas des refus d'une livraison** n'ont pas d'issue écrite : constats de l'étape (m) absents ou faux, ligne de GO ou acte de reprise en défaut, nom ou compagnon du fichier des scores tant que B.12 n'est pas tranché. Une phrase suffit : ce ne sont pas des arrêts de la lecture de la discrétion ; ils bloquent le programme jusqu'à correction de la pièce en cause, sans lecture ni issue, et ils sont consignés.
- **M-3.** Le rédacteur a ouvert, pour la première fois, du code de la relance (les seuls noms de fichiers et de champs) et le déclare. Ce n'est l'interne d'aucun moniteur. Rien à reprocher : c'est à consigner.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 24 intacts | `b076e3f9…`, `8d834631…`, `ade786eb…`, `ed7823af…`, `12609c04…` : compagnons vérifiés |
| brouillon 25 et note | `ab5fc58e…`, `3732b6b4…` : compagnons vérifiés |
| **section 12** | **identique au brouillon 24** ; les points 17 à 21 sont donc ceux des fiches parties, et les fiches 9 à 12 sont mot pour mot dans le texte |
| **7.5 et ligne A17** | **identiques au brouillon 24** |
| tables A, B et C ; 7.6 à 7.8 | identiques au brouillon 24 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 24 : 1 121 sur 1 121 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1271, 1272, 1274, 1275, 1277, 1282, 1283, 1284), toutes en 13.1 |
| table d'en-tête, six lignes neuves | empreintes égales (brouillon 24, sa note, vérification du brouillon 24, relevé de la version 6, avis, vérification du code de la version 6). **Aucune empreinte de fichier cloisonné prise.** |

## 6. Ce que je n'ai pas regardé

- Le texte en entier, hors des blocs touchés et de leur contexte, et des sections dont j'ai vérifié par programme qu'elles n'ont pas bougé.
- Le code des versions 6 et 7 et leurs notes. Ce que je dis du code vient des trois pièces lues.
- Les quatorze lignes héritées de la table d'en-tête.

## 7. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md` : par différence, et les blocs touchés.
- Les brouillons 20 et 24, par programme.
- La note du brouillon 25.
- `docs/notes/relance-organismes-discrets-v1/avis-redacteur-defauts-code-v6-v1.md`.
- `docs/notes/relance-organismes-discrets-v1/verification-corrections-code-v6-bras-a-v1.md` : en-tête, C-1 à C-3, partie 3 et partie 7.
- `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v7.md`.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Rien d'autre : aucun fichier de code ni aucune note du code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
