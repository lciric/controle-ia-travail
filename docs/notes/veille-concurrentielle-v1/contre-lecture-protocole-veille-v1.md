# Contre-lecture du protocole de veille concurrentielle v1 (règle R2)

- **Objet** : `docs/notes/veille-concurrentielle-v1/protocole-veille-concurrentielle-v1.md`, empreinte
  `37e335d61cdee751d9828cacb1f9f010c2dfe43c8ca027371515d4768080173f` (recalculée, égale au compagnon ; 797 lignes), ligne
  R-2569 de `registres/decisions.md` (l. 2528).
- **Contre-lecteur** : sous-agent neuf, Claude Fable 5.2 (autre modèle que le rédacteur, Claude Opus 5.5 ; même lignée, limite
  dite). Il n'a écrit ni le protocole, ni la synthèse de niveau 3, ni les décisions N-067 à N-070.
- **Écrit** le 13 novembre 2026, de 19:19 à 19:29 UTC (`date -u`).
- **Couples « texte actuel → texte corrigé »** : 25 ; chaque texte actuel est recopié du protocole et sa présence a été
  vérifiée par programme (25 sur 25, aux blancs et retours à la ligne près).
- **Moyens** : lecture de fichiers du dépôt seulement. Aucune requête réseau, aucune dépense, aucune écriture git, aucune
  valeur de clé lue.
- **Demande servie** (R-2562, R-2563) : coder chaque article rival sur les éléments de nos pièces libres, nommer par pièce
  l'équipe la mieux placée et sa date probable, mettre en face notre délai, classer par regret attendu, décider par pièce,
  valider par rétro-test au 1er octobre et par prédictions datées.

## Verdict

**Utilisable après corrections.** Le protocole est sérieux sur la forme (requêtes écrites, refus non contournés, gardes
nommées, seuils et conséquences écrits avant toute requête, limites déclarées). Mais **trois défauts bloquent la première
requête**, et tous trois touchent ce que la demande veut prouver :

1. le rétro-test, tel qu'écrit, **ne peut pas être joué sans choix faits à la main par quelqu'un qui connaît la réponse** :
   les signatures « d'origine » sont celles d'après les collisions, et leurs listes « cédé » citent les collisions mêmes ;
2. le vocabulaire des axes, envoyé à deux fournisseurs extérieurs et à un relais, **porte nos énoncés sous une forme
   découpée** ; l'arbitre n'a pas de famille fixée ; le protocole garde une exception écrite pour le collisionneur ;
3. le modèle d'équipe **sature** (toute équipe du corpus compte sur toute pièce, fenêtres de 26 et 13 semaines sur un corpus
   de quatre semaines), et le seul critère chiffré du rétro-test juge des **rangs** alors que les décisions consomment des
   **niveaux**.

Une v2 (R12) est nécessaire avant la phase 2. La liste d'arrêt du protocole le prévoit (« contre-lecture du protocole qui
demande une v2 »).

**Réponse courte aux huit points demandés**

| point | réponse |
|---|---|
| 1. Rétro-test réussi par construction ? | En partie oui (critère 1, première moitié ; critère 3), en partie **échec ou réussite au gré de l'opérateur** (B1). Garde-fous manquants : B1, M1 à M7. |
| 2. Seuils et conséquences écrits avant les données ? | Oui pour les seuils, mais l'auteur connaît la liste ; conséquences incomplètes et boucle de reprise jusqu'à réussite (M6) ; aucun critère de niveau (B3). |
| 3. Grille codable sans nos énoncés ? Collisions d'autre forme ? | Codable, oui. Le recouvrement par script n'est pas calculable tel qu'écrit et écarte les collisions de cadre différent sans jamais mesurer ce qu'il écarte (M10). |
| 4. Modèle d'équipe et regret | Saturation (B3) ; abandon favorisé par construction, sensibilité partielle (M11). |
| 5. Sources | Versions suivantes, catégories, pièces déjà nommées et non lues, sites des laboratoires absents (M8) ; règle des ancrages non mécanique (M9) ; refus traités sans contournement, mais règle d'arrêt contradictoire (M13). |
| 6. Confidentialité | Trois fuites possibles (B2). |
| 7. Devis | Arithmétique juste ; cinq postes absents (M12). |
| 8. Règles du dépôt | R1, R6, R9, R12 : écarts mineurs (m1 à m4) ; R3 touchée par M6. |

## Contrôles faits

| contrôle | résultat |
|---|---|
| Empreinte du protocole contre son compagnon | conforme (`37e335d6…`) |
| Les 22 fichiers de la section 0.3 contre leurs compagnons (16 premiers caractères) et contre `docs/sha256sums-lancement-v2.txt` | 22 sur 22 conformes |
| `registres/decisions.md`, R-2551 à R-2569 | présentes, l. 2510 à 2528 ; R-2562 et R-2563 aux l. 2521 et 2522, comme écrit ; « go les deux demandes » lu à R-2563 ; refus d'OpenReview et de GitHub (403) lus à R-2562 |
| Lignes citées du programme v2 (93, 98, 99, 103, 108, 111, 112, 178, 211) et de `anteriorite-v1.md` (233, 392) | 11 sur 11 conformes au contenu annoncé |
| Prix : `devis-mini-course-kimi-argon-nuit-v1.md` l. 62 et 63 ; `depense-et-incidents-v1.md` l. 48 ; `registres/depenses.md` l. 389 ; ligne GO-2026-11-12-04 de `registres/go.md` (l. 311) | conformes (Kimi 2 et 10 « vérifiés » ; Argon 10 et 50 « supposé » ; 9,54 USD ; 15 USD par tour) |
| Arithmétique des sections 11.2 et 11.3, refaite | conforme (0,0029 ; 0,0088 ; 0,106 ; 0,462 ; 0,12 ; 0,36 ; 15 à 87 ; 60 à 348) |
| Décomptes : 26 pièces vivantes, 33 d'origine, 10 touchées | conformes à l'addition du texte |
| Les quinze ancrages dans les deux documents de lancement | 14 présents dans l'état de l'art v1 ; POPPER absent des deux (déclaré) ; 2609.03035 cité cinq fois dans l'état de l'art v1, comme écrit |
| Identifiants des strates 1 et 2 dans la synthèse de niveau 3 (`e30a013d…`) | 15 sur 16 présents ; **2609.17560 absent** (0 occurrence), voir M2 |
| Dates de première version des strates 1 et 2 dans la synthèse | **aucune trouvée** à côté des identifiants, voir M2 |
| Table de `note-anteriorite-co-scientist-v1.md` | vingt lignes O1 à O20 (l. 257 à 276) ; la plage citée « l. 257 à 273 » s'arrête à O17 et n'atteint pas O19 (l. 275), voir M1 |
| Section 6 de la contre-lecture de la synthèse (`f1580ddc…`, l. 878 à 894) | quinze énoncés « à ne pas déclarer libres » ; neuf identifiants qu'elle demande de lire sont absents du protocole, voir M8 |

**Écarts du contre-lecteur lui-même (déclarés).** (a) Un `find docs -name 'note-anteriorite-co-scientist-v1.md'` a parcouru
l'arbre `docs/` ; le filtre ne portait que sur l'affichage ; aucun nom ni contenu d'un chemin interdit n'a été affiché ni
ouvert, mais la consigne « aucune recherche récursive qui traverse ces chemins » n'a pas été tenue pour cette commande.
(b) Pour vérifier le prix d'Argon, la ligne 389 de `registres/depenses.md` a été affichée : c'est une ligne de dépense de
l'essai de format de l'étiqueteur (prix et montants seuls), le même écart que celui du rédacteur (R-2569). (c) Les débuts
des lignes R-2552 à R-2566 ont été affichés pour la vérification demandée ; ils nomment des pièces de 7b par leur nom et leur
empreinte, sans contenu.

---

## Constats bloquants

### B1 — Rétro-test : les signatures « d'origine » sont celles d'après les collisions

**Fait.** La section 1.4 dit que le rétro-test emploie les énoncés d'avant les resserrements, puis renvoie aux signatures de
la section 1.3 pour toutes les pièces sauf cinq. Or les signatures de 1.3 portent les resserrements, et leurs listes
« cédé » citent les pièces de la liste de référence :
- A-H1 : « à fausses alarmes égales et à agrégation égale » (R-2567, du 13 novembre), ME1 et CA3 exigés, « cédé : le gain par
  étape sur sabotage étiquetable (2610.12445) » : la collision n° 1 de la strate 1 est cédée d'avance ;
- C-HC5 : « cédé : matrice entre juges, quorum avec moteur de règles (2610.29178) » : collision n° 5 ;
- B-H5 : « cédé : … (2604.13386 ; 2609.36490, p. 8) » : pièce n° 3 de la strate 2, que le critère 1 demande pourtant de juger
  « au moins occupe en partie » sur B-H5 ou C-HC4 ;
- A-H8 : « cédé : le socle » : c'est exactement ce que la strate 2 attribue à 2609.10739 (« A-H8 (socle) ») ;
- A-H2, A-H6, A-L, A-T, B-H3, B-H7, C-HC1, C-HC3, C-HC4, C-HC6 : aucune version d'origine écrite ; la section 3.3 ne compte
  un article que « sur un élément non cédé ».

**Conséquence.** Le juge du rétro-test doit ou bien appliquer « cédé » tel qu'écrit (les pièces n° 3 et 6 de la strate 2
échouent alors **par construction**, et le critère 1, qui en exige 5 sur 7, se joue sur une seule pièce de marge), ou bien
l'ignorer sur décision de l'opérateur, qui connaît la liste. Dans les deux cas le résultat ne dit rien du dispositif. La liste
« pièces d'origine touchées dans H » (A-H1, C-HC5…) contredit les signatures qui cèdent ces mêmes éléments.

```actuel
construction ce qui a été pris après le 1er octobre. Signatures identiques à la section 1.3, sauf :
```
```corrige
construction ce qui a été pris après le 1er octobre. **Les 33 signatures d'origine sont écrites en entier à l'annexe A**
(axes exigés, codes voisins, forme de résultat, liste « cédé au 31 août 2026 »), à partir des seuls documents de lancement
et des décisions datées d'avant le 1er octobre 2026 ; pour l'organisme, voir la section 8.3 bis. Une liste « cédé »
d'origine ne cite aucune pièce dont la première version est postérieure au 31 août 2026 (donc aucune pièce des strates 1
et 2) et aucun resserrement de R-2567 ni de N-067 à N-070. Le script refuse toute signature d'origine qui contient un
identifiant 2609.*, 2610.* ou 2611.* (garde testée sur un cas sain et sur un artefact, R5). L'annexe A est écrite par un
sous-agent qui n'a lu ni la section 8.3 ni la synthèse de niveau 3 ; s'il n'en existe pas, la limite est dite. Écarts
notables avec la section 1.3 :
```

### B2 — Confidentialité : nos énoncés partent, découpés, dans le vocabulaire des axes ; arbitre et collisionneur

**Fait 1 — le vocabulaire n'est pas neutre.** La section 4.2 remet aux lecteurs extérieurs « le vocabulaire fermé de la
section 1.1, recopié tel quel ». Plusieurs codes n'existent que parce qu'une de nos pièces existe, et la reprennent presque
mot pour mot :
- GA8 « nul formé des lois connues (archive, facteurs connus, englobement) » : c'est l'énoncé retenu de O4 (N-064, N-067), que
  R-2568 interdit de déclarer publiquement avant la lecture de SSRN 6569258 ;
- ME11 « adversaire adaptatif qui répartit un budget dans le temps ou entre agents, ou préserve les marginales » : le cœur de L
  et de T ;
- AC7 « statistique conjointe temps × agents » avec GA4 : le cœur du papier B ;
- ME1 « sabotage diffus : aucune action prise seule n'est étiquetable », OS2 « agent auteur d'un contenu destiné au moniteur »,
  ME5 avec sa liste « flatterie, autorité, approbations forgées, usurpation de style, ordres en bande », ME10, OS9 à OS11,
  ME9 : papiers A, C, H9 et organisme.
L'union des codes rend le plan du programme à qui la reçoit. Le destinataire est double pour le lecteur A (« par le relais
du dépôt » : le relais et le fournisseur du modèle).

**Fait 2 — l'arbitre.** Il est « un troisième modèle, distinct des deux lecteurs et du rédacteur », sans famille. Il tranche
« chaque désaccord sur un jugement par pièce » (section 4.5), et le jugement par pièce porte la signature, la forme et la
liste « cédé » de la pièce (section 4.3). Rien n'empêche de lire « troisième modèle » comme un modèle d'un troisième
fournisseur. De même, la section 4.4 fait refaire par l'arbitre les lectures d'un lecteur contaminé, et la section 7.3 nomme
« un juge » sans dire lequel.

**Fait 3 — le collisionneur.** Le point 7 de la section 10 garde une exception écrite, et la ligne 3 du devis enverrait
les cinq premières pièces à trois fournisseurs. R-2568 interdit la forme de O12 dans tout texte sortant et réserve O4.

**Autres sorties vérifiées, sans constat** : en-tête neutre, pas de `mailto`, journal « sans aucun secret », adresses
`github.com` non suivies, lecteurs sans nos pièces à l'étage 2, phrases « travaux futurs » (textes publics). **À noter** : la
sonde de connaissance envoie aux fournisseurs cinq identifiants de nos collisions (information publique, mais elle dit ce que
nous surveillons) ; les requêtes par auteur à Semantic Scholar disent quelles équipes nous suivons. Risque faible, à écrire.

```actuel
- **Aucun énoncé du programme n'est envoyé à un fournisseur extérieur** : A et B ne reçoivent que des textes publics et le
  vocabulaire neutre des axes ; le jugement par pièce, qui porte nos énoncés, reste chez les sous-agents de la session.
```
```corrige
- **Aucun énoncé du programme n'est envoyé à un fournisseur extérieur autre que celui de la session.** Le vocabulaire des
  axes est une forme découpée de nos énoncés : il ne sort pas en l'état. Deux voies, au choix de Lazar (section 13, point 1) :
  (i) **défaut** : codage par article fait par deux sous-agents Claude, rien ne sort ; (ii) lecteurs extérieurs, seulement si
  Lazar accorde par un mot exprès **le texte exact** des consignes sortantes, déposé et scellé dans
  `consignes/consigne-lecteurs-exterieurs-v1.md`, où chaque code propre au programme (GA8, ME1, ME5, ME10, ME11, AC7, OS2, OS9
  à OS11) est remplacé par un code générique tiré d'une taxonomie publiée et noyé parmi des codes leurres en nombre au moins
  égal. Le jugement par pièce, l'arbitrage et toute étape qui porte une signature, une forme de résultat ou une liste
  « cédé » restent chez les sous-agents Claude de la session. **Garde de sortie** : le script n'envoie à un hôte de modèle
  extérieur qu'un message formé d'une consigne dont l'empreinte figure dans une liste blanche scellée et d'un texte public
  archivé ; il refuse tout message qui contient une suite de huit mots d'un fichier de `docs/decisions/`, du programme ou de la
  section 1.3 (garde testée sur un cas sain et sur un artefact, R5). La sonde de connaissance envoie des identifiants publics
  de pièces surveillées : risque écrit, accepté ou non par le même mot de Lazar.
```
```actuel
- **Arbitre** : un troisième modèle, distinct des deux lecteurs et du rédacteur, pour chaque désaccord (section 4.5).
```
```corrige
- **Arbitre** : un sous-agent Claude de la session, d'un modèle distinct de ceux des deux juges et du rédacteur, pour chaque
  désaccord (section 4.5) ; jamais un modèle d'un fournisseur extérieur. Le « juge » de la section 7.3 est de même un
  sous-agent Claude.
```
```actuel
7. Aucun énoncé du programme envoyé à un fournisseur extérieur (section 4.4), sauf le collisionneur, s'il est accordé (section
   11, ligne 3).
```
```corrige
7. Aucun énoncé du programme envoyé à un fournisseur extérieur (section 4.4), sans exception dans ce protocole. Le
   collisionneur sort de ce protocole (ligne 3 du devis et point 4 de la section 13 retirés) : s'il est voulu, il fait l'objet
   d'un nœud à part, qui dit quels énoncés partent, chez qui, et sa compatibilité avec R-2568.
```

### B3 — Modèle d'équipe : saturation, fenêtres impossibles, niveaux jamais jugés

**Fait 1 — plancher.** `g(T,p) = 0,25 + 1,5 × c(T,p)` donne un taux non nul à toute équipe sur toute pièce, et
`P_p(w)` somme « Σ_T » sans dire sur quelles équipes. Ordre de grandeur, avec les formules du protocole : une équipe de trois
articles par an dont un passe le préfiltre a `λ = 4/104`, `π = 2/5`, `g = 0,25`, `r` entre 0,5 et 1, soit 0,0019 à 0,0038 par
semaine ; avec 150 équipes au corpus de l'étage 2 (100 à 600 articles prévus), le taux de fond vaut 0,3 à 0,6 par semaine et
`P_p(H)` vaut 0,84 à 0,97 **pour toute pièce**, avant même la première équipe positionnée. Les unités ne se répondent pas :
`λ × π` compte des articles du domaine, la « sortie » est un article qui occupe au moins en partie un élément non cédé d'une
pièce précise.

**Fait 2 — fenêtres.** `h_nouv` compte « les 26 semaines avant t0 » et la base de volume de la section 8.5 « les 13 semaines
avant t0 », mais la collecte par listes commence le 1er septembre : au rétro-test, 4,3 semaines sont observées. Diviser par 26
sous-estime le terme par six ; « équipe sans article antérieur dans le corpus » est vrai de presque tout le monde quand le
corpus a un mois. La base de volume du critère 2 (« articles de septembre ») et celle de la section 8.5 (« 13 semaines ») ne
sont pas la même.

**Fait 3 — rangs contre niveaux.** Le critère 2 est une aire sous la courbe, insensible à toute transformation monotone ; le
score de Brier est « rapporté, sans seuil ». Or la section 7 tire `T_r` de `P_p` : elle consomme les niveaux. Un modèle saturé
passe le critère 2 et rend partout « le rival sort avant nous ». Et la section 0.1, point 5, interdit ensuite tout réglage.

```actuel
- **Proximité** `g(T,p) = 0,25 + 1,5 × c(T,p)` (a priori).
```
```corrige
- **Proximité** `g(T,p) = 1,5 × c(T,p)` (a priori). Une équipe sans position sur la pièce (`c = 0`) n'entre pas dans la somme
  des équipes nommées : `Σ_T` porte sur les seules équipes avec `c(T,p) > 0` ; les autres sont portées par le terme de fond.
```
```actuel
- **Équipe nouvelle** (non nommée) : pour chaque famille F de pièces (A, B, C, organisme), `h_nouv(p) = (k_F + 0,5) / (26 × |F|)`,
```
```corrige
- **Terme de fond** (équipes non positionnées et équipes nouvelles, non nommées) : pour chaque famille F de pièces (A, B, C,
  organisme), `h_nouv(p) = (k_F + 0,5) / (S × |F|)`, où S est le nombre de semaines **réellement collectées** par les listes
  avant t0 (du 1er septembre à t0 ; 4,3 au rétro-test), et où « 26 semaines » se lit partout « S semaines », base de volume de
  la section 8.5 comprise ;
```
```actuel
**Réussite = 1 et 2 et 3.** Rapportés en plus, sans seuil : score de Brier et score de Brier relatif à la fréquence observée sur
```
```corrige
4. **Niveau** : la moyenne des `P_p(H)` sur les pièces jugées est comprise entre la moitié et le double de la fréquence
   observée des pièces touchées, et le score de Brier est inférieur à celui de la fréquence observée constante.
**Réussite = 1 et 2 et 3 et 4.** Si 4 seul échoue : un seul facteur d'échelle κ, commun à tous les taux, est ajusté sur le
rétro-test pour égaler la moyenne des `P_p(H)` à la fréquence observée ; il est déclaré comme réglé sur le test, et seules
les prédictions datées de la section 9 jugent alors les niveaux. Rapportés en plus, sans seuil : score de Brier relatif à la
fréquence observée sur
```

---

## Constats majeurs

### M1 — Douze pièces de l'organisme, nées après t0 et choisies sans règle, portent presque la moitié du rétro-test

**Fait.** L'organisme n'existait pas au lancement (section 2.3 du protocole) ; N-064 est du 9 novembre. Ses douze pièces
« d'origine » sont donc postérieures de cinq semaines à t0, et écrites au voisinage de ce qui venait d'être trouvé. Elles
portent 4 des 10 pièces touchées (O2, O3, O12, rôle 1), 5 des 9 collisions (n° 4, 6, 7, 8, 9) et 4 des 7 pièces de la strate 2
(n° 1, 4, 5, 7). Le protocole ne met à part que l'ancrage POPPER, et calcule le seuil sans l'organisme « pour information ».
De plus, la table source compte vingt lignes (O1 à O20, l. 257 à 276) ; douze sont prises, huit écartées (O5, O6, O7, O13 à
O16, O18, O20) sans règle, alors que la contre-lecture de la synthèse (B2) dit O20 occupée comme méthode et O5, O6, O15 non
réexaminées. La plage citée (l. 257 à 273) n'atteint pas O19.

```actuel
Ce choix est fait après coup : au rétro-test,
les résultats de l'organisme sont rapportés à part, et le seuil (section 8.4) est aussi calculé sans eux, pour information.
```
```corrige
Ce choix est fait après coup, comme les pièces de l'organisme elles-mêmes (N-064, 9 novembre 2026). **Le rétro-test se
juge donc sans l'organisme** : 21 pièces d'origine (papiers A, B, C), 6 touchées (A-H1, A-H8, B-POP, B-ST, B-H3, C-HC5),
4 collisions de la strate 1 (n° 1, 2, 3, 5), 3 pièces de la strate 2 (n° 2, 3, 6) ; les seuils de la section 8.4 s'écrivent
sur ces dénominateurs. Les résultats avec l'organisme (toutes les lignes O1 à O20 de la table, l. 257 à 276, et le rôle 1,
sans tri) sont rapportés à part, pour information.
```
Avec ces dénominateurs et la règle de proportion de M2 (arrondi à l'entier supérieur), les critères 1 et 3 deviennent : « les
3 pièces de la strate 2 retenues et jugées au moins "occupe en partie" » ; « au moins 2 des 4 collisions ». La puissance est faible (voir M3) ; il faut l'écrire plutôt que la
masquer par des pièces nées après coup.

### M2 — La liste de référence n'est pas figée, et ses « non touchées » sont des « non trouvées »

**Fait.** (a) Quatre lignes de la strate 1 et cinq de la strate 2 portent « à relever » pour la date ou l'équipe ; si une
première version tombe hors de sa strate, les dénominateurs 7, 9 et 10 changent et les seuils « 6 sur 7 », « 3 sur 9 » ne
sont plus définis. (b) Aucune date de première version n'est dans la synthèse à côté de son identifiant : les dates écrites
(« 8 oct. », « 7 nov. »…) n'ont ni chemin ni empreinte (R6). (c) 2609.17560 n'apparaît pas dans la synthèse ; la règle
d'entrée (« tirée de la synthèse et de R-2551 à R-2553 ») n'est donc pas celle qui a servi. (d) Les 23 pièces « non touchées »
le sont au sens « non trouvé dans les pièces lues » (R8) : R-2567 dit que rien n'a été cherché du 10 au 13 novembre et que les
travaux qui citent trois ancrages n'ont jamais été cherchés ; la synthèse elle-même est « utilisable après corrections, pour
une partie des énoncés seulement », sans version corrigée. Or H court jusqu'au 13 novembre.

```actuel
donnent comme occupant, au moins en partie, un élément d'une pièce d'origine **que rien de daté d'avant le 1er octobre
n'occupait déjà**. Date = première version (ce qui a été ajouté par une version suivante n'est pas daté ; limite dite).
```
```corrige
donnent comme occupant, au moins en partie, un élément d'une pièce d'origine **que rien de daté d'avant le 1er octobre
n'occupait déjà**. Date = première version (ce qui a été ajouté par une version suivante n'est pas daté ; limite dite).
**Les dates et équipes des tableaux sont des pistes** : la première requête de la phase 2 les relève par `id_list`, un
sous-agent neuf complète les tableaux et les scelle (`retro-test/liste-reference-datee-v1.md`) avant la collecte. Règle
écrite d'avance : une pièce dont la première version est antérieure au 1er septembre passe en strate 2b ; antérieure au
1er octobre, en strate 2 ; postérieure au 9 novembre, hors liste. **H = du 1er octobre au 9 novembre 2026**, dernier jour
cherché (R-2567). Tout seuil s'applique alors en proportion, arrondie à l'entier supérieur (détection : 6/7 et 5/7 ;
équipes : 1/3). **Seconde lecture, obligatoire** : après la veille vivante, les articles du 1er octobre au 9 novembre
qu'elle juge au moins « occupe en partie » sont rejugés contre les pièces d'origine ; les critères 2 à 4 sont recalculés
avec ces issues complétées ; si le verdict change, c'est la seconde lecture qui commande les sections 7 et 9, et le
rapport donne les deux.
```

### M3 — Critère 2 : il peut être passé par un modèle pire que la base triviale, sans mesure d'incertitude

**Fait.** « Au moins 0,70 et pas inférieure de plus de 0,05 à la base de volume » : un modèle qui fait moins bien que le
simple décompte d'articles réussit. Sous le hasard, l'écart type de l'aire vaut environ 0,11 pour 10 touchées sur 33 et 0,14
pour 6 sur 21 (formule de Mann-Whitney, sans ex æquo) : 0,70 est atteint par chance environ une fois sur 28, puis une fois sur
12 ; et les pièces ne sont pas indépendantes (un seul article, 2611.10620, en touche quatre).

```actuel
   **au moins 0,70**, et n'est pas inférieure de plus de 0,05 à celle de la **base de volume** (nombre d'articles de septembre
   comptés sur la pièce).
```
```corrige
   **au moins 0,70**, avec sa valeur de permutation (10 000 permutations des issues par blocs d'article : les pièces touchées
   par un même article sont permutées ensemble ; graine de la section 7.4) inférieure à 0,10. L'aire de la **base de volume**
   (nombre d'articles de septembre comptés sur la pièce) est rendue à côté, avec l'intervalle de l'écart par rééchantillonnage
   des pièces. **Si le modèle ne dépasse pas la base de volume, c'est la base de volume qui sert aux décisions** (le plus
   simple l'emporte), et le rapport dit que le modèle d'équipe n'apporte rien de mesuré.
```

### M4 — Critère 3 : vrai presque par construction

**Fait.** (a) La règle d'équipe (dernier auteur commun, ou deux auteurs, ou indice de Jaccard d'au moins 1/3, puis
composantes reliées) chaîne les laboratoires qui échangent leurs auteurs en une seule équipe géante ; « une équipe qui
partage au moins un auteur » avec la collision est alors presque sûre d'être dans les trois premières. (b) Les ancrages ont
été choisis par quelqu'un qui connaît la liste (M9), et plusieurs sont des équipes de la strate 1. (c) Aucune base de
comparaison : trois équipes prises par simple volume feraient-elles aussi bien ?

```actuel
3. **Annonce par équipe** : pour **au moins 3** des 9 collisions de la strate 1, une équipe qui partage au moins un auteur avec
   l'article figure parmi les **trois premières** équipes (probabilité sur H) de l'une des pièces qu'il touche.
```
```corrige
3. **Annonce par équipe** : pour **au moins le tiers** des collisions de la strate 1 jugées, une équipe qui partage au moins un
   auteur avec l'article figure parmi les **trois premières** équipes (probabilité sur H) de l'une des pièces qu'il touche,
   **et** ce nombre dépasse celui de la base « trois équipes de plus grand volume » (`λ × π` seul), **sans** le flux des
   citations. Une équipe de plus de quinze auteurs distincts est scindée par dernier auteur ; la taille de chaque équipe
   citée est rendue. Le nombre attendu sous tirage au hasard de trois équipes du corpus (1 000 tirages, graine de la
   section 7.4) est rendu à côté.
```

### M5 — Rappel du préfiltre et du tri : mesuré seulement contre ce que l'auteur connaissait déjà

**Fait.** Les listes L1 à L3 sont écrites le 13 novembre par un rédacteur qui a lu la synthèse ; plusieurs termes nomment des
objets apparus après le lancement (tout le vocabulaire de l'organisme : `AI scientist`, `hypothesis generation`,
`hypothesis validation`, `Goodhart`, `falsification` ; celui de H9 : `delegation chain`, `constraint drift`, `handoff*`) ou des
bancs précis (`NARCBench`). Le jeu de témoins (ancrages et pièces de la synthèse) et la strate 2 viennent tous de la même
recherche, faite avec le même regard : le rétro-test mesure « retrouve-t-on ce que nous avions trouvé », pas « trouve-t-on ce
qui existe ». La première moitié du critère 1 (« présentes dans le corpus après dédoublonnage ») est acquise pour tout article
d'une des six catégories : elle ne juge que le choix des catégories. Un contrôle des termes contre les deux documents de
lancement n'est pas concluant (documents en français, termes en anglais) ; il ne peut pas servir de garde.

```actuel
  avant toute lecture de l'étage 1 ; il est rapporté comme écart. Les pièces de septembre de la liste de référence
  (section 8.3, strate 2) n'y entrent jamais : elles jugent le rétro-test.
```
```corrige
  avant toute lecture de l'étage 1 ; il est rapporté comme écart. Les pièces de septembre de la liste de référence
  (section 8.3, strate 2) n'y entrent jamais : elles jugent le rétro-test.
- **Échantillon aveugle des écartés** (mesure du rappel hors de toute liste connue) : 300 articles de septembre tirés au
  hasard (graine de la section 7.4) parmi ceux que le préfiltre écarte passent l'étage 1 mêlés au lot, sans marque. Rendu :
  part retenue par au moins un lecteur, avec son intervalle ; les retenus vont à l'étage 2. **Au-delà de 2 % de retenus
  jugés au moins « voisin » à l'étage 2, le préfiltre est dit insuffisant** et la conséquence « 1 échoue » de la section 8.5
  s'applique.
- **Attribution** : pour chaque pièce de la strate 2 passée, le rapport nomme les termes qui l'ont fait passer ; le critère 1
  est rendu une seconde fois sans L3 et sans les termes propres à l'organisme et à H9.
- **Strate 3, mécanique** (liste que nous n'avons pas faite) : après le scellement des prédictions, le sous-agent neuf de la
  section 8.2 relève dans les bibliographies des PDF de la strate 1 tous les identifiants d'arXiv de 2609 ; rendu : part de
  ces articles présente après préfiltre, après l'étage 1, après l'étage 2.
```
Et, pour que la première moitié du critère 1 juge quelque chose :
```actuel
1. **Détection** : parmi les 7 pièces de la strate 2, **au moins 6** présentes dans le corpus du rétro-test après dédoublonnage,
```
```corrige
1. **Détection** : parmi les pièces de la strate 2, **au moins 6 sur 7 (en proportion)** présentes dans le corpus du rétro-test
   **après le préfiltre lexical et retenues à l'étage 1**,
```

### M6 — Conséquences d'un échec : reprise jusqu'à réussite, cas manquants, audit asymétrique

**Fait.** (a) « 1 échoue » : v2 puis nouveau rétro-test au 15 octobre sur une sous-liste de la même strate 1, après correction
éclairée par l'échec ; aucune liste de détection n'est définie pour ce second test, aucun nombre de reprises n'est borné :
c'est une course vers un signe positif (R3). (b) Rien n'est écrit pour « 2 et 3 échouent ensemble », ni pour une base de
volume elle-même sans pouvoir. (c) « Trop beau » exige l'aire d'au moins 0,95 **et** 9 sur 9 : l'un sans l'autre passe sans
audit ; et aucun audit n'est prévu pour un résultat trop net dans l'autre sens (R4, symétrie).

```actuel
- **1 échoue** : le corpus ou le tri ne voient pas ce qui existe ; arrêt de la veille vivante ; correction par une v2, puis
  nouveau rétro-test avec t0 = 15 octobre 2026 et la sous-liste de la strate 1 postérieure à cette date (fuite résiduelle dite).
```
```corrige
- **1 échoue** : le corpus ou le tri ne voient pas ce qui existe ; arrêt de la veille vivante ; nœud porté à Lazar. Une v2
  peut corriger, mais **aucun second rétro-test ne vaut validation** : ses pièces de référence ont servi à corriger. La veille
  vivante corrigée est alors rendue comme **description** (qui a publié quoi, page citée), sans probabilité ni classement par
  regret, et seules les prédictions datées (section 9) la valident, huit semaines plus tard.
- **2 et 3 échouent, ou la base de volume a elle-même une aire inférieure à 0,60** : aucun classement par regret ; rendu
  descriptif par pièce ; décisions laissées à Lazar sur les faits, sans chiffre de probabilité.
```
```actuel
- **Trop beau (R4)** : aire ≥ 0,95 et 9 sur 9 en 3 déclenchent un audit de fuite (dates, sonde de connaissance, gestes de
  l'opérateur) avant toute acceptation.
```
```corrige
- **Trop net, dans un sens ou dans l'autre (R4)** : aire ≥ 0,95, **ou** toutes les collisions annoncées en 3, **ou** aire
  ≤ 0,30, **ou** aucune pièce de la strate 2 retrouvée : chacun déclenche le même audit (dates, versions des résumés, sonde
  de connaissance, gestes de l'opérateur, accès des juges aux fichiers du dépôt) avant toute acceptation ou tout rejet.
```

### M7 — Fuites d'information que la garde de date ne voit pas

**Fait.** (a) L'interface d'arXiv rend le titre, le résumé et le champ `comment` de la **dernière** version ; un article de
septembre révisé en octobre entre au rétro-test avec son texte d'octobre, et la garde, qui ne lit que `published`, ne le voit
pas. Seul le PDF est fixé à la version d'avant t0 (section 2.8). (b) « NeurIPS : ce qui était public au 30 septembre » ne se
reconstruit pas par une requête d'aujourd'hui. (c) Semantic Scholar rend aujourd'hui des citations qu'il n'avait pas indexées
le 1er octobre : le flux des citations est plus complet au rétro-test qu'il ne le sera en veille vivante pour les dernières
semaines. (d) Les juges par pièce et l'arbitre sont des sous-agents de la session : rien ne leur interdit d'ouvrir la
synthèse ou le registre, qui donnent la liste. (e) La sonde de connaissance interroge par identifiant (un modèle ne
retient guère un numéro) et ne porte que sur les lecteurs A et B.

```actuel
1. Garde de date dans le script : tout élément de date postérieure au 30 septembre fait **échouer** la construction du corpus du
   rétro-test (pas de filtrage silencieux) ; testée sur un corpus sain et sur un corpus piégé (R5).
```
```corrige
1. Garde de date dans le script : tout élément de date postérieure au 30 septembre fait **échouer** la construction du corpus du
   rétro-test (pas de filtrage silencieux) ; testée sur un corpus sain et sur un corpus piégé (R5). **Elle porte aussi sur le
   champ `updated`** : pour tout article révisé après le 30 septembre, le titre et le résumé sont pris sur la page
   `arxiv.org/abs/<identifiant>v<K>` de la dernière version antérieure au 1er octobre, et le champ `comment` est vidé. Le flux
   NeurIPS n'entre pas au rétro-test. Le retard d'indexation de Semantic Scholar est dit comme limite du résultat « avec
   citations ».
1 bis. Les juges par pièce, l'arbitre et le sous-agent de comparaison travaillent **sans outil de lecture du dépôt** : ils ne
   reçoivent que leur consigne, la pièce et le texte masqué. La date de fin de connaissance déclarée de chaque modèle employé
   est consignée ; un modèle dont elle est postérieure au 30 septembre 2026 ne lit pas le rétro-test. La sonde de connaissance
   se fait par titre, et porte aussi sur les juges.
```

### M8 — Sources : versions suivantes, catégories, pièces déjà nommées et non lues, sites des laboratoires

**Fait.** (a) **Versions.** La collecte se fait par date de première version. Le dépôt connaît pourtant plusieurs cas où
c'est une version suivante qui porte la collision : 2609.03035 v2 (contre-lecture des décisions, 68-1 et 69-1), et les
« versions postérieures de NARCBench, MasDrift, Sun » écartées en section 8.3. Un article d'avant septembre révisé en
novembre n'entre jamais au corpus vivant. (b) **Catégories.** Six catégories ; manquent celles où vivent les formes voisines
de nos pièces théoriques et de l'organisme : statistique mathématique et méthodologie (tests séquentiels sur plusieurs flux
dépendants : cœur de L, T et de la statistique conjointe), génie logiciel (pipelines de code à plusieurs rôles), théorie des
jeux, informatique et société, interaction humain-machine, économétrie et finance (le « nul des lois connues » : SSRN 6569258
est justement hors d'arXiv). (c) **Pièces nommées et non lues.** La contre-lecture de la synthèse (section 6, l. 880 à 893)
nomme ce qu'il faut lire pour lever chaque réserve ; les semences forcées n'en reprennent qu'une partie. Absentes :
1906.08938, 2605.16140, math/0410072 (L : « la collision la plus probable ») ; 2310.01153, 2102.00630, 1906.09256 (T) ;
2603.04069, 2609.19101 (Tr) ; 2610.27577 (H8) ; 2610.37849 (HC2b) ; 2110.00115, 2103.08402, 2610.07627, 2610.00314 (O4) ;
2605.26047 (H6). (d) **Voisins connus d'avant septembre** (strate 2b : MIRAGE, SafeDream, MasDrift, PACE…) : ils n'entrent
au corpus vivant que s'ils citent un ancrage ; « l'équipe la mieux placée » est alors calculée sans les occupants connus.
(e) **Hors d'arXiv** : les équipes que le programme nomme lui-même pour la bascule publient aussi sur leurs sites (institut
britannique de sécurité de l'intelligence artificielle, FAR.AI, Redwood Research, Apollo Research, METR, laboratoires) ; aucun
de ces hôtes n'est permis ni proposé à Lazar. Les ateliers de NeurIPS 2026 passent par OpenReview, refusé.

```actuel
6. **Dates** : toute date d'article est celle de sa **première version** (champ `published` de l'interface d'arXiv), en UTC.
   Les versions suivantes sont datées à part (champ `updated`, page `arxiv.org/abs/<identifiant>`).
```
```corrige
6. **Dates** : toute date d'article est celle de sa **première version** (champ `published` de l'interface d'arXiv), en UTC.
   Les versions suivantes sont datées à part (champ `updated`, page `arxiv.org/abs/<identifiant>`). **En veille vivante,
   les versions suivantes sont collectées** : mêmes requêtes que la section 2.1 avec `lastUpdatedDate` à la place de
   `submittedDate`, du 1er octobre à la date de lancement ; un article d'avant septembre ainsi révisé passe le préfiltre
   et l'étage 1 comme les autres, et son étage 2 lit la dernière version en disant ce que la révision ajoute.
```
```actuel
Pour chaque catégorie `C` ∈ {cs.LG, cs.AI, cs.CL, cs.CR, cs.MA, stat.ML} et chaque tranche de dix jours
```
```corrige
Pour chaque catégorie `C` ∈ {cs.LG, cs.AI, cs.CL, cs.CR, cs.MA, stat.ML, stat.ME, math.ST, cs.SE, cs.GT, cs.CY, cs.HC,
econ.EM, q-fin.ST} (les huit dernières : métadonnées et préfiltre gratuits, décompte rendu à part) et chaque tranche de dix jours
```
```actuel
2607.06807, 2510.04303 (B-ST) ; 2602.01425 (A-H8) ; 2607.05545, 2605.03255 (C-HC1) (synthèse § 9, point 7). **Elles n'entrent
jamais dans le rétro-test.**
```
```corrige
2607.06807, 2510.04303 (B-ST) ; 2602.01425 (A-H8) ; 2607.05545, 2605.03255 (C-HC1) (synthèse § 9, point 7) ; **toutes les
pièces que la section 6 de la contre-lecture de la synthèse (`f1580ddc…`, l. 880 à 893) demande de lire** : 1906.08938,
2605.16140, math/0410072 (A-L) ; 2310.01153, 2102.00630, 1906.09256 (A-T) ; 2605.26047 (A-H6) ; 2603.04069, 2609.19101
(A-Tr) ; 2610.27577 (A-H8) ; 2610.37849 (C-HC2b) ; 2110.00115, 2103.08402, 2610.07627, 2610.00314 (O-O4) ; les six pièces
du lot 4-B (O-R1). **Occupants connus** : toute pièce d'arXiv citée par la synthèse de niveau 3 entre à l'étage 2 du corpus
vivant, marquée « connue », pour que l'équipe la mieux placée soit calculée avec elle. **Elles n'entrent
jamais dans le rétro-test.**
```
Et à la section 13, point 2, une option de plus pour Lazar : la liste des hôtes des sites d'équipes (à nommer un par un), ou
un export à la main ; à défaut, la limite « équipes qui publient hors d'arXiv : non vues » est écrite dans chaque rendu.

### M9 — Les quinze ancrages : règle non mécanique, justifications tirées de faits d'après t0

**Fait.** La règle (« la plus proche de l'énoncé, puis la plus citée, puis celle dont les citants n'ont jamais été cherchés »)
ne se rejoue pas : « la plus proche » est un jugement. Les justifications du tableau citent des faits postérieurs à t0 :
n° 9, « 2611.04556 s'en dit la suite » (la collision n° 4 de la strate 1 sert à choisir l'ancrage) ; n° 5, « contre-lecture
N-067 à N-070 » (13 novembre) ; n° 1 à 3, « citants jamais cherchés (R-2567) ». Les deux documents de lancement citent
60 identifiants d'arXiv distincts, dont 25 au moins deux fois ; cinq des huit « écartés pour pièce déjà couverte » y sont cités
plus souvent (trois fois : 2506.10805, 2605.31593, 2607.02514, 2606.07054, 2601.20022) que trois ancrages retenus (une fois :
2512.07810, 2608.02698, 2603.12277). L'exclusion « citants attendus très nombreux, non comptés » n'a pas de seuil.

```actuel
**Limite déclarée (R4)** : le rédacteur connaît la liste de référence ; la règle de choix est écrite pour la tenir à distance,
et le rétro-test rapporte ses résultats **avec et sans** ce flux (section 8.5).
```
```corrige
**Limite déclarée (R4)** : le rédacteur connaît la liste de référence, et trois justifications du tableau s'appuient sur des
faits d'après le 1er octobre (n° 5, n° 9, et « citants jamais cherchés »). **Les seuils du rétro-test se jugent donc sans ce
flux** ; le résultat avec ce flux est rapporté à côté. **Jeu de contrôle mécanique**, sans choix : tous les identifiants
d'arXiv cités au moins deux fois par les deux documents de lancement, de première version au plus tard le 30 septembre 2026,
et dont `citationCount`, relevé par la première requête, ne dépasse pas 500 ; le résultat « avec citations » est rendu pour
les quinze ancrages et pour ce jeu. La veille vivante emploie l'union des deux.
```

### M10 — Recouvrement par script : non calculable tel qu'écrit, et aveugle aux collisions d'autre forme

**Fait.** (a) Les signatures de la section 1.3 sont de la prose : « TA3 **et** TA1 ou TA2, comparés », « même AC des deux
côtés », « panel de moniteurs à sondes » (B-H5 : aucun code d'objet), « régimes d'accès comparés » ; l'axe d'échelle (« modèle
ouvert lu ≥ 7 milliards ») n'a pas de règle « présent, voisin, absent » ; les codes « voisins » ne sont listés que pour deux
pièces. Le script ne peut pas calculer `c` sans qu'on écrive les signatures en table, donc sans choix après scellement.
(b) Le nombre d'axes exigés va de deux (B-H7 : « ME11 adaptatif · CA1 » ; O-O8) à sept (A-H1) : pour B-H7, tout article de
contrôle codé CA1 passe au jugement ; pour A-H1, il faut quatre axes. (c) **Collisions d'autre forme** : un théorème de
statistique sur plusieurs flux dépendants, sans agent, obtient deux axes sur six pour B-ST et n'est jamais jugé ; un article
qui fait la mesure de A-H2 sur un banc d'outils (CA2) ou dans un vocabulaire de détection de fraude perd les axes d'objet, de
menace et de cadre. Le protocole ne mesure nulle part ce que le seuil `c ≥ 0,5` écarte.

```actuel
Un couple (article, pièce) passe au **jugement par pièce** (section 4.3) dès que `c ≥ 0,5` selon le codage de **l'un ou l'autre**
lecteur.
```
```corrige
Un couple (article, pièce) passe au **jugement par pièce** (section 4.3) dès que `c ≥ 0,5` selon le codage de **l'un ou l'autre**
lecteur, **ou** dès que le code discriminant de la pièce (le code en gras de sa signature ; un par pièce, fixé à l'annexe B)
est présent chez l'un des lecteurs, quel que soit `c`. Les signatures sont données à l'annexe B sous forme de table (pièce ;
axe ; codes exigés ; codes voisins ; règle de l'axe d'échelle), seule lue par le script ; une pièce a au moins trois axes
exigés. **Mesure de ce que le script écarte** : 60 articles de l'étage 2 tirés au hasard (graine de la section 7.4) parmi
ceux qui n'ont aucun couple retenu sont jugés contre **toutes** les pièces de leur famille la plus proche ; rendu : part
jugée au moins « voisin », au moins « occupe en partie » ; au-delà de 5 % d'« occupe en partie », le seuil descend à
`c ≥ 0,34` par addendum scellé, rapporté comme écart. Chaque lecteur rend en outre une phrase libre « contribution
principale » par article, que le juge de l'échantillon reçoit.
```

### M11 — Regret : l'abandon est favorisé par construction ; ce qui est arbitraire n'est pas tout perturbé

**Fait.** (a) `U(abandonner) = W × ρ` avec `ρ = ΣV / ΣW` : la capacité rendue est convertie en valeur au taux moyen, **sans
risque de rival**, alors que « tenir » vaut `V × [1(T_n < T_r) + s × …] ≤ V`. Pour toute pièce de rapport `V / W` égal ou
inférieur à la moyenne, l'abandon l'emporte quel que soit le rival ; le classement est donc mené par W, et la veille n'y pèse
qu'à la marge. Même biais pour le sommeil (`8 × (W / T_n) × ρ`). (b) Les W ne s'additionnent pas : une même mesure (porte G1)
sert plusieurs pièces ; abandonner une pièce ne rend pas W. (c) Rien ne dit que la capacité rendue est absorbable (portes,
GO, voie de calcul). (d) Le coût `0,4 × W × ρ` de l'accélération, le plancher 0,1 et le 0,5 de `s`, les 8 semaines du sommeil,
le 0,2 des versions, le terme de fond et la loi exponentielle (taux constant, sans échéances de conférence) sont a priori et
**hors** des perturbations de la section 7.5. (e) Minimiser `R(d)` revient à maximiser l'utilité attendue (le terme
`E[max]` ne dépend pas de d) : à dire, pour ne pas prêter au « regret » plus qu'il n'apporte. (f) Le glissement repose sur
un point censuré (porte G0 encore ouverte) ; moins de cinq jalons est le cas probable.

```actuel
- **abandonner** : `U = W × ρ` (toute la capacité restante rendue ; la pièce est citée chez le rival).
Où **W** = semaines de travail restantes de la pièce (plan, section 6) ; **ρ = Σ V / Σ W** sur toutes les pièces (valeur moyenne
d'une semaine de capacité) ;
```
```corrige
- **abandonner** : `U = W_p × ρ` (la capacité **propre** rendue ; la pièce est citée chez le rival).
Où **W** = semaines de travail restantes de la pièce (plan, section 6) et **W_p** = la part de W qui ne sert aucune autre
pièce gardée (une étape commune à plusieurs pièces n'est rendue que si toutes sont abandonnées) ; **ρ = Σ V × q / Σ W** sur
toutes les pièces, avec `q = E[1(T_n < T_r) + s × 1(T_n ≥ T_r)]` sous « tenir » (valeur moyenne d'une semaine de capacité,
**au même risque de rival que la pièce jugée**) ; dans les formules du sommeil et de l'accélération, W se lit W_p ;
```
```actuel
[0,75 ; 1,5] ; chaque multiplicateur de la section 5.3 × uniforme sur [0,5 ; 2]. Une décision est **stable** si elle reste la
même dans au moins 80 % des perturbations, sinon **fragile** ;
```
```corrige
[0,75 ; 1,5] ; chaque multiplicateur de la section 5.3 × uniforme sur [0,5 ; 2] ; le terme de fond × uniforme sur
[0,5 ; 2] ; le 0,5 de `s` uniforme sur [0,25 ; 0,75] et son plancher sur [0 ; 0,3] ; le coût de l'accélération uniforme sur
[0,2 ; 0,8] × W_p × ρ ; la durée du sommeil uniforme sur [4 ; 13] semaines ; la loi du temps de sortie tirée entre
exponentielle et Weibull de forme 1,5. Une décision est **stable** si elle reste la
même dans au moins 80 % des perturbations, sinon **fragile** ; **une décision fragile est rendue « tenir »**, avec la
décision calculée à côté ; avec moins de cinq jalons de glissement, toute décision autre que « tenir » est dite fragile ;
```

### M12 — Devis : cinq postes absents

**Fait.** L'arithmétique est juste. Manquent : (a) **les jetons de raisonnement**, facturés en sortie par ces fournisseurs
(précédent du dépôt : `depense-et-incidents-v1.md`, l. 46, « sortie comptée réflexion comprise ») ; 60 jetons de sortie par
article à l'étage 1 et 1 200 à l'étage 2 les ignorent ; (b) **le protocole s'applique deux fois** (rétro-test, puis veille
vivante) : le devis ne dit pas si les volumes couvrent les deux, ni si le codage de septembre est réemployé (les versions
lues diffèrent, section 2.8) ; (c) témoins des lecteurs (40 articles, second essai compris), échantillons de contrôle,
reprises sur erreur de format ; (d) **la capacité de la session** : avec 100 à 600 articles à l'étage 2, deux juges et un
arbitre lisant chacun un texte de 30 000 jetons par couple retenu, l'ordre de grandeur est de dizaines à centaines de
millions de jetons de sous-agents Claude ; le devis dit seulement « aucun appel facturé par clé » ; (e) aucun plafond global
écrit en USD, seulement des plafonds par ligne après décompte ; l'hypothèse de 1 500 à 8 000 articles après préfiltre paraît
basse pour une règle « L1 et L2 » où L1 contient `representation*`, `detection`, `classifier*`, `activation*`, `sequential` et
L2 `agent*`, `language model*`, `LLM*` (hypothèse du contre-lecteur, à trancher par le décompte gratuit).

```actuel
Devis **ferme en deux temps**, chacun après le décompte gratuit qui le précède : (a) après le préfiltre, ligne de l'étage 1 au
plafond `N1 × 0,0088 × 1,2` ; (b) après l'étage 1, ligne de l'étage 2 au plafond `N2 × 0,462 × 1,2 + 0,36`.
```
```corrige
Devis **ferme en deux temps**, chacun après le décompte gratuit qui le précède, **séparément pour le rétro-test et pour la
veille vivante** : (a) après le préfiltre, ligne de l'étage 1 au plafond `N1 × 0,0088 × 1,2` ; (b) après l'étage 1, ligne de
l'étage 2 au plafond `N2 × 0,462 × 1,2 + 0,36`. N1 et N2 comptent les témoins, les échantillons de contrôle et un second
essai. Les prix par unité sont **vérifiés sur les dix premiers appels payés** de chaque lecteur, raisonnement compris tel que
facturé ; si le coût mesuré dépasse le coût par unité
du pire cas, arrêt et nouveau devis. **Plafond global** : 350 USD pour l'ensemble des lignes 1 et 2, les deux passes
comprises ; au-delà, nœud. **Capacité de session** : le devis (b) donne le nombre de couples (article, pièce) à juger et
le nombre de jetons de sous-agents attendu ; au-delà de 3 000 couples, les couples sont jugés par ordre de `c` décroissant
et la coupure est rapportée.
```

### M13 — Règle d'arrêt contre essais vers des hôtes non vérifiés

**Fait.** R-2562 a vérifié arXiv, Semantic Scholar, OpenAlex, LessWrong et Alignment Forum. `neurips.cc` et `huggingface.co`
ne l'ont pas été ; le protocole y prévoit « un essai ». Or la section 2.0, point 5, dit qu'un refus du mandataire « arrête la
requête », et la liste d'arrêt de la section 12 dit qu'on s'arrête sur tout « refus d'un contrôle de permissions ou d'un
classifieur ». Un 403 attendu sur un hôte d'essai arrête-t-il la requête ou la phase ? Une garde d'arrêt ambiguë n'est pas
testable (R5), et sonder un hôte dont on attend le refus n'est pas dans l'esprit de « aucun contournement ».

```actuel
5. **Refus** : un refus du mandataire réseau (403) ou d'un contrôle de permissions ou d'un classifieur arrête la requête ;
   il est consigné **tel quel** et rapporté à la mère ; aucune reformulation ni aucun contournement.
```
```corrige
5. **Refus** : un refus du mandataire réseau (403) sur un hôte de la liste arrête **ce flux** : il est consigné **tel quel**,
   rapporté à la mère, le flux est dit « non observé », les autres flux continuent. Un refus d'un contrôle de permissions ou
   d'un classifieur arrête **la phase** (liste d'arrêt, section 12). Aucune reformulation ni aucun contournement. Les hôtes
   non vérifiés par R-2562 (`neurips.cc`, `huggingface.co`) ne reçoivent leur unique essai qu'après un mot de la mère qui
   l'autorise ; à défaut, ces deux flux sont « non observés ».
```

---

## Constats mineurs

- **m1 (R1).** Le protocole a les seuils, le plan, les critères et la liste d'arrêt du gabarit
  (`prereg/gabarit-preregistrement-v1.md`), mais ni « hypothèse » ni « prédiction chiffrée et signe » : il ne dit pas ce
  qu'il attend du rétro-test. À ajouter en tête de la section 8 : l'hypothèse (« la chaîne retrouve les pièces de septembre
  et range les pièces touchées au-dessus des autres »), et la prédiction chiffrée du rédacteur pour chaque critère, avant
  toute requête.
- **m2 (R6).** La section 0.3 omet trois fichiers employés : `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md`
  (section 1.4), `registres/go.md` (section 11.1), `CLAUDE.md` (section 6). Les lignes de registres vivants sont citées par
  numéro seul : y joindre les premiers mots de la ligne, un registre vivant bouge.
- **m3 (R9).** `spawn` dépend de l'ordre d'appel : fixer une table (usage, pièce) → rang, écrite dans le protocole. Restent
  sans graine ni règle : le choix des cinq identifiants de la sonde, des 20 témoins positifs, des dix PDF du test du masque,
  l'ordre des articles dans les lots de 25. Température des lecteurs à fixer et à consigner ; un second passage d'un lecteur
  sur le même lot ne remplace jamais le premier.
- **m4 (R12).** La section 12 nomme la contre-lecture `contre-lecture-protocole-veille-concurrentielle-v1.md` ; la mère a
  demandé `contre-lecture-protocole-veille-v1.md` (nom du présent fichier). Aucun zip versionné des livrables n'est prévu.
- **m5.** Section 2.1, variante de moissonnage : l'adresse `export.arxiv.org/oai2` est, de mémoire du contre-lecteur, remplacée
  par un autre hôte (`oaipmh.arxiv.org`), qui n'est pas dans la liste permise ; non vérifié (aucune requête). De plus `from` et
  `until` y filtrent la date de modification, pas la date de dépôt. Prévoir que la variante peut être refusée, et la dire
  « non disponible » plutôt que de suivre une redirection vers un hôte non permis.
- **m6.** Section 2.1 : l'arrêt « jusqu'à une page de moins de 500 entrées » coupe en silence sur une page vide passagère ;
  comparer au total annoncé par l'interface (`totalResults`) et réessayer une fois.
- **m7.** Section 5.3, part du sujet : la requête par auteur ne demande pas `abstract` ; le préfiltre « sur titre et résumé »
  ne peut pas s'y appliquer. Ajouter `abstract` aux champs, ou dire « sur titre seul ».
- **m8.** Section 2.6 : `venue=NeurIPS` peut ne rien rendre (nom long attendu) ; écrire les deux formes dans la même requête
  prévue, ou accepter « zéro » comme refus consigné.
- **m9.** Section 2.0, point 4 : pas de cadence pour LessWrong, Alignment Forum, Hugging Face, `neurips.cc`, ni pour les PDF ;
  écrire une requête toutes les 3 secondes partout, et prendre les PDF sur `export.arxiv.org`.
- **m10.** Section 4.5 : le kappa de Cohen par code s'effondre pour un code rare ; rendre aussi l'accord positif. Témoins
  négatifs : aucun seuil ; un lecteur qui retient tout passe. Ajouter : au plus 5 négatifs retenus sur 20.
- **m11.** Section 4.2 : « une page pour chaque code » suppose que le texte envoyé garde ses marques de page après masque et
  troncature ; l'écrire et le tester avec le masque.
- **m12.** Section 8.4 : « avec et sans billets » alors que les billets de la strate 1 sont « comptés seulement dans le score
  avec billets » sans y être listés ; les lister ou les retirer.
- **m13.** Section 13, point 1 : « comme le veut N-053 » ; N-053 parle du juge d'une autre lignée pour le dispositif de
  mesure, pas d'une veille ; écrire « par analogie avec ».
- **m14.** Section 6 : le délai ignore le temps de décision de Lazar (GO, portes) ; l'ajouter comme étape typée.

---

## Ce qui tient

- Les empreintes, les lignes de registre et les lignes de documents citées sont exactes (tableau des contrôles).
- Aucun contournement d'OpenReview ni de GitHub ; options portées à Lazar ; cadence et en-tête neutres ; journal des requêtes.
- La distinction entre énoncés courants et énoncés d'origine est la bonne idée ; elle est seulement inachevée (B1).
- La strate 2 hors des témoins du préfiltre, les prédictions scellées avant comparaison, la comparaison par un sous-agent
  neuf, la règle « aucun paramètre réglé après lecture » et les limites déclarées (auteur qui connaît la liste) sont des
  gardes réelles.
- Les prédictions datées à 56 jours (section 9) sont la seule validation hors échantillon du dispositif : après les
  corrections ci-dessus, c'est sur elles que la confiance doit reposer, et le rétro-test doit être présenté comme un contrôle
  de plomberie plus que comme une preuve.

## Pour Lazar, en une ligne chacun

1. Lecteurs du codage : tant que le vocabulaire sortant n'est pas accordé mot pour mot, le défaut sans dépense (deux
   sous-agents Claude) est aussi le seul qui tient la confidentialité (B2).
2. Le rétro-test, corrigé, sera jugé sur 21 pièces, 4 collisions et 3 pièces de septembre : il sera honnête et peu puissant.
3. Le collisionneur sort de ce protocole.
