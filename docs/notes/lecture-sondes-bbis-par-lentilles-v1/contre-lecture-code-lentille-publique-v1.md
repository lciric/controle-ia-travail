# Contre-lecture du code de la lecture des sondes de l'étape B bis par la lentille publique — v1

Pièce de classe B (instrument). Contre-lecteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Opus 5.5
(le développeur était Fable 5.2), 2026-11-19. Objet : le paquet `src/controle_ia/lentilles_sondes_bbis/` et ses essais, au commit
`128810af` de la branche `claude/lentilles-bbis-developpeur-v1` (empreintes égales à `empreintes-code-v1.txt`, `6de20bce…`, vérifiées).
Texte qui gouverne : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`, vérifiée sur main).

**Conclusion : pas avant : (1) les corrections A à D ci-dessous (fiche du code, scellement antérieur au verdict, versement avant
nettoyage, cloisonnement de l'impression), plus un essai à artefact du libellé des pôles après repli, inscrits et revérifiés ; (2) la décision du directeur sur le biais de la valeur p de
concentration (fiche du point 5), et, si l'addendum est retenu, son code et sa revérification.**

Déclaration. Lu : les notes, la table des essais, les empreintes, les renvois et les outils du développeur ; le texte scellé en entier ;
les dix modules et les six fichiers d'essais ; du code voisin seulement la copie versée de `readout.py`, la tête du correctif (2) et, pour
le type de `pli_lu` et la forme de `enc.reglage`, des lignes de `t07bbis/validation_imbriquee_v1.py` et `commun_v1.py` (code, jamais une
sortie) ; la fiche `registres/code-mots-et-cout-bras-a/CODE-MOTS-ET-COUT-BRAS-A-v2.json` (forme, sur la demande de la mère). Jamais
ouverts : `docs/verdicts/`, `diag/`, `runs/`, `donnees/`, aucun verdict, aucune table, aucun résultat de l'étape B bis ni des lentilles,
aucun fichier « consigne-privee » ou « conception-ii-b ». L'extraction du commit dans mon bloc-notes contenait des dossiers interdits :
je ne les ai ni listés ni ouverts. Aucune dépense, aucune machine, aucun téléchargement. Un blocage d'outil (attente par « sleep »,
règle de l'outil et non refus de permission, ainsi jugé par la mère) : signalé, puis attente par notification.

## 1. Conformité au texte scellé

Les règles de « Code neuf », du plan et de la liste d'arrêt sont codées telles qu'écrites, aux exceptions suivantes. Vérifié en
particulier : liste blanche de E-2 et formes (a), (b), (c) ; décodage clé par clé de E-1 sans `direction*` ; empreintes des sondes ;
graines et clés ; deux nuls, repli par direction, témoins ; z, concentration, part, familles, jeton de début, pôles, comparaisons ;
libellés ; bornes de calibration (égales aux exemples du texte et au programme scellé des bornes : essai joué, 4 passés) ; déclencheurs
et audit ; phrase de tête **identique au texte** (comparée par programme) et phrases gelées recopiées mot pour mot ; garde de la fonction
de lecture et ses deux artefacts ; montage (clé, débogage, un octet, voisin, `readout.py` comparé avant les correctifs, poids en flux,
lentille, jetons gardés).

Écarts :
- **E1 (à corriger, correction B)** — Liste d'arrêt, ligne 1 : « `VERDICT-BBIS` déjà présente à l'inscription de
  `SCELLEMENT-LENTILLES-BBIS` : rien ne part » n'est pas codée (aucune comparaison d'heures, ligne `ABSENCE-VERDICT-LENTILLES-BBIS`
  non exigée). Elle est codable.
- **E2 (à corriger, correction A ; tranché par la mère)** — « code non cité par `CODE-LENTILLES-BBIS` : rien ne part » : le code ne
  vérifie que la présence de la ligne.
- **E3 (à corriger, correction C)** — Le nettoyage du point 10 efface le dossier de travail sans versement ; un arrêt pendant le calcul
  ne verse rien (« arrêt ; versement de ce qui existe », ligne de la durée de 8 h) ; une sortie placée dans le dossier de travail serait
  effacée.
- **E4 (petit)** — La ligne `ENTREES-LENTILLES-BBIS` proposée ne porte que E-2 ; le texte y veut aussi l'empreinte de E-1 et celle de
  l'extrait de la liste blanche (rendues à part par le lanceur : la mère les recopie, ou une fiche fermée les porte).
- **E5 (tautologies, sans effet)** — `exiger_pointeur("lentille publique", …)` compare entre elles des constantes du texte ; dans
  `ouvrir_entrees`, `ch["e2"] != course.chemin_e2` ne peut jamais être vrai (le chemin est reconstruit du même identifiant de course,
  déjà contrôlé par l'expression du chemin). À garder ou retirer, sans effet.
- **E6 (ordre)** — L'essai d'un octet des jeux de données du corpus vient après le clone du voisin (il en lit les provenances) : il reste
  avant tout flux long ; à déclarer.

Les treize précisions de lecture du développeur :

| n° | objet | jugement |
|---|---|---|
| 1 | forme des clés de graines, tirage `(M, largeur)`, signes par `integers`, colonnes sans remise | lecture fidèle |
| 2 | écart type de population, quantile par interpolation linéaire, rang empirique, part et familles des nuls sur leurs vingt premiers, « attendu », même norme, arrêt sur écart type nul | lectures fidèles ; « attendu » = moyenne des comptes nuls, conforme à l'esprit du texte |
| 3 | rang des pôles parmi les maxima nuls, p sur le maximum de \|cosinus\| | fidèle (le cosinus maximal des 28 672 pôles est le maximum de \|cosinus\|) |
| 4 | « concentrée » pour le déclencheur trop beau : un signe ou un vecteur suffit ; tout négatif : les deux lentilles | fidèle (A-1 dit « à un signe au moins ») |
| 5 | « au rang près » et tolérance 10⁻⁴ sur les jetons échangés ; garde aux trois couches | fidèle ; jouer les trois couches est un sur-ensemble permis |
| 6 | calibration hors bornes : aucun libellé pour la lecture, l'autre nul gardé ; pôles non touchés | lecture tenable ; « pôles non touchés » est un choix (la calibration éprouve les concentrations de la lentille, pas les cosinus) : à consigner par la mère, sans enjeu de verdict |
| 7 | `provenance` : `source_layers`, `d_model` présents et différents : arrêt ; liste d'entiers exigée | **plus sévère que le texte** ; ratifiable : voir ci-dessous |
| 8 | pôles « intermédiaires » : aucune phrase | fidèle (le texte ne gèle aucune phrase) ; voir point 6 |
| 9 | jetons communs de la phrase de comparaison : lentille publique, signe + | fidèle (la phrase porte un seul nombre ; les tables portent les quatre) |
| 10 | horloge tenue dans le dossier de travail, montage et calcul additionnés | fidèle |
| 11 | réglages par défaut du texte, non exposés en ligne de commande | fidèle |
| 12 | ne compare pas ses empreintes à la fiche `CODE-LENTILLES-BBIS` | **choix qui devait revenir à la mère** ; tranché par elle : correction A |
| 13 | dépôts et révisions du corpus lus dans les provenances du voisin corrigé | fidèle |

**Précision 7, ratification.** Je la juge **sans effet sur un verdict** : elle ne peut que produire un arrêt avant tout calcul (nœud),
jamais changer une table, un libellé ou une phrase. Seul coût possible : un arrêt à tort si le fichier réel range `source_layers` sous une
autre forme qu'une liste (un tenseur, par exemple) ; ce serait un nœud, pas un résultat. Ratifiable telle quelle.

## 2. Gardes et essais (R5)

Essais ciblés sur l'extraction du commit : `257 passed, 1 skipped in 114.90s` ; l'essai sauté (bornes comparées au programme scellé du
texte, cherché par git) passe une fois la pièce recopiée de main : **258 au total, comme annoncé**.

Essai des essais du contre-lecteur, distinct de celui du développeur (`mutations_v1.py`) : une garde retirée ou un seuil faussé à la fois.
Première série (57 altérations, quatre fichiers d'essais rapides) : **17 survivent** (quatre d'entre eux sont vus par les essais de procédure, voir plus bas). Seconde série (procédure) : voir la fin de cette
section. Survivants, classés :

- *Gardes réelles qu'aucun essai ne voit* (essais à ajouter ; ceux des quatre premières sont écrits dans la correction D) :
  `run_id` de E-2 ; `SCELLEMENT-LENTILLES-BBIS` qui doit citer ce texte ; `fichier_sondes.fichier` ; `cellule` et `pli_lu` ; forme de
  `…_b` (tableau d'un élément) ; longueur de l'essai d'un octet ; `git rev-parse HEAD` du voisin égal au commit ; tailles des tenseurs
  extraits dans `conclure` ; modèle et longueurs de `jetons-gardes.json` ; type de `W_U` dans `lire` ; seuil d'espace disque (`libre <
  minimum`).
- *Altérations équivalentes* (sans effet observable sur des scores continus) : `searchsorted` à droite au lieu de gauche (égalités) ;
  part avec `>=` au lieu de `>`.
- *Vues par les essais de procédure seulement* (rejouées avec eux, `mutations_survivants_v1.py`) : la phrase des pôles
  « intermédiaires », le seuil d'espace disque, la marque du dossier avant nettoyage, les clés permises d'une ligne de registre :
  quatre sur quatre vues. Le seuil d'espace disque sort donc de la liste ci-dessus.
- *Tautologique* : `ch["e2"] != course.chemin_e2` (E5) — sa survie est attendue.

Seconde série (dix altérations du lanceur, essais de procédure compris) : **6 survivent** :
- **le libellé des pôles après repli** : remplacer, dans `_etiqueter`, la valeur p du nul isotrope par direction par celle du nul
  partagé « remplacée » n'est vu par aucun essai (l'essai de repli ne contrôle pas le libellé des pôles) ; garde réelle, essai à
  ajouter avant inscription ;
- le contrôle d'espace disque à chaque direction (seul celui du départ est éprouvé) ;
- le refus d'un dossier de travail déjà existant au montage (R12) ; le refus de tables ou de manifeste déjà existants au calcul (R12) ;
- l'arrêt « montage absent » quand `etat-montage.json` manque (la marque suffit aux essais) ;
- la recherche de la clé dans les fichiers écrits **au montage** : l'essai sain vérifie l'absence de la clé, aucun artefact n'écrit la
  clé pendant le montage pour voir la garde tomber.
Essais à ajouter pour ces six (non écrits ici) ; aucun n'est un défaut de calcul, mais R5 demande l'artefact de chaque garde.

Les gardes des corrections A à D sont toutes vues : dix altérations, dix vues (`mutations_corrections_v1.py`).

## 3. Graines (R9)

Conformes : `SeedSequence(entropy=E, spawn_key=(entier des 8 premiers octets du SHA-256 de la clé,))`, `PCG64`, une clé par tâche, de la
forme du plan, point 3 ; chaque clé demandée est consignée. Réserve : les graines du montage (colonnes de la garde, permutation) ne sont
que dans le rapport du montage ; le manifeste du calcul devrait citer l'empreinte de ce rapport (ajout recommandé, non bloquant).

## 4. Cloisonnement

- **Lectures** : le code n'ouvre que E-1, E-2 et leurs compagnons (chemins permis seulement), et des registres seulement les clés
  nommées ; `VERDICT-BBIS` sans son chemin. Le clone partiel télécharge les arbres de la branche des données : des **noms** de fichiers,
  jamais un contenu (conforme au texte, à déclarer).
- **Impression avant l'étape du lecteur** : la ligne de commande du calcul imprime les noms des tableaux des morceaux, qui disent la
  couche, la famille (présence de `q`), les sondes en échec et l'existence d'un repli par direction : information que l'opérateur ne doit
  pas lire. Correction D.
- **Suppression avant versement** : oui (E3). Correction C, conforme à « récupérer ce qui est récupérable » : inventaire (chemin,
  taille, SHA-256) de tout le dossier de travail ; copie scellée de tout ce qui n'est pas sous licence ou corpus (journaux des scripts du
  voisin, jetons gardés, état du montage, horloge, marque) et du correctif réellement appliqué au voisin ; les poids, la lentille, le
  cache des téléchargements et le clone du voisin (où le corpus est écrit) sont inventoriés, jamais copiés (« Données gardées » : non
  versés pour licence) ; le versement est vérifié avant la suppression. À tout arrêt après le départ du calcul : le dossier de travail
  est versé de même, les tableaux déjà calculés sont écrits, fermés, scellés sous `versement/<run>/calcul-interrompu/`, marqués
  « interrompus, non lus », et rien n'est supprimé. Un dossier de sortie emboîté dans le dossier de travail (ou l'inverse) est refusé.

## 5. Le biais de la valeur p de concentration

**Banc refait par un programme à moi** (`banc_contre_lecteur_v1.py`, matrices aléatoires seulement, aucun code du paquet) : taille
réelle (89 498 jetons, largeur 4 096, M = 2 000), lecture t = RMSNorm(J u)·γ, ε = 10⁻⁶ ; **huit répétitions de 2 000 témoins** par
scénario, chacune avec son propre jeu de M directions nulles (le banc du développeur n'en tirait qu'un par nul : la part d'un seul jeu
varie déjà d'environ ± 0,5 point sous un nul exact, loi bêta de paramètres 100 et 1 901) ; comparaison **appariée** sur les mêmes nuls et
témoins entre la statistique du texte (u_j compris dans la moyenne et l'écart type) et la même sans u_j. Sept scénarios : W_U et γ
gaussiens ; W_U structuré (direction commune, normes de lignes log-normales, γ à huit coordonnées extrêmes) ; le même lu par une
matrice J anisotrope de rang fort 64 ; nul isotrope et nul des signes autour de deux vecteurs anisotropes. Sortie :
`sortie-banc-contre-lecteur-v1.txt` (`0101c9aa…`).

| part des témoins à p ≤ seuil | 0,05 | 0,01 | 0,000 999 5 (= p ≤ 0,001) |
|---|---|---|---|
| attendu sous un nul exact | 0,0500 | 0,0100 | 0,0010 |
| texte (u_j compris), moyenne des 7 scénarios | **0,0571** (0,0555 à 0,0585) | 0,0121 | 0,0013 |
| sans u_j, moyenne des 7 scénarios | 0,0513 | 0,0103 | 0,0010 |

- **Le biais est réel** : +0,7 point au seuil 0,05 (≈ × 1,14), ≈ × 1,2 au seuil 0,01, ≈ × 1,3 au seuil 0,001 (ce dernier sur peu
  d'événements). Il est stable d'un scénario à l'autre (structure de W_U, de γ, de J, forme du nul). Sans u_j, la part revient à la
  valeur nominale à l'erreur du banc près. Mécanisme : une direction nulle comprise dans sa propre moyenne et son propre écart type voit
  son z maximal rétréci (≈ z²/(2M) en valeur relative, z ≈ 4), alors que la direction lue ne l'est pas.
- **Portée du banc** : il mesure la valeur p de concentration seulement. La part au-dessus du nul compare aussi u_j à un quantile
  qui le comprend : même sens attendu, non mesuré ici. Les comptes de familles ne dépendent pas des statistiques du nul : non touchés.
- **Sens** : anti-conservateur : p un peu trop petits pour les directions réelles comme pour les témoins ; la lecture penche donc vers
  « se distingue du nul ». Au seuil du libellé « concentrée » (p ≤ 0,001 et ≤ 0,01), l'effet sur une lecture est faible (une direction
  nulle serait « concentrée » à ≈ 0,0013 au lieu de 0,0010) ; l'« attendu par le seul hasard » écrit à côté des comptes est sous-estimé
  d'environ un quart à un tiers.
- **Sortie des bornes de calibration** (`risque_calibration_v2.py`, calcul exact par lois bêta-binomiales, sortie
  `sortie-risque-calibration-v2.txt`) — probabilité qu'une calibration (couche, lentille, nul) sorte de ses bornes :

  | jeux de témoins | bornes | nul exact | sans u_j (0,0513) | texte (0,0571) | taux du développeur (0,0605) |
  |---|---|---|---|---|---|
  | isotrope, 1 000 | [23, 85] | 0,0002 | 0,0002 | 0,0018 | 0,0055 |
  | signes, 6 × 200 | [33, 92] | 0,0001 | 0,0002 | 0,0033 | 0,0132 |
  | signes, 13 × 200 | [89, 176] | 0,0002 | 0,0003 | 0,0137 | 0,0681 |
  | signes, 20 × 200 | [149, 256] | 0,0002 | 0,0004 | 0,0359 | 0,1790 |
  | signes, 40 × 200 | [326, 478] | 0,0002 | 0,0007 | **0,159** | 0,594 |

  Oui, il peut faire sortir la calibration de ses bornes : faiblement pour le nul isotrope, **sensiblement pour le nul des signes
  quand une couche porte beaucoup de vecteurs** (la mise en commun resserre les bornes autour de 5 % alors que le biais est
  systématique). Le nombre de vecteurs par couche n'est connu qu'après `VERDICT-BBIS` (jusqu'à 40 si toutes les sondes choisissent la
  même couche et la famille « attention »). Une sortie rend « non calculables » toutes les tables de cette couche, de cette lentille et
  de ce nul : on perd la lecture, à tort, sans fausse affirmation (la garde échoue du côté sûr). À taux réel plus fort que le banc, le
  risque monte vite (colonne de droite).

### Fiche de décision pour le directeur

**Décision** : garder le texte scellé tel quel en déclarant le biais, ou le corriger par un addendum scellé avant toute lecture d'une
sonde réelle.

**Enjeu** : la valeur p de concentration (et, par le même mécanisme appliqué au quantile 0,99, celle de la part au-dessus du nul ;
pas celle des familles, qui ne compte que les premiers jetons bruts de u_j) est un peu trop petite (≈ × 1,14 au
seuil 0,05, mesuré sur matrices aléatoires) ; la calibration du nul des signes peut alors sortir de ses bornes à tort et rendre une
couche entière « non calculable » (≈ 4 % à 20 vecteurs, ≈ 16 % à 40 vecteurs par couche, davantage si le taux réel dépasse celui du
banc). Aucune sonde réelle n'a été lue : corriger maintenant n'expose rien.

**Options**
1. **Garder le texte, déclarer le biais** (déclaration écrite avant la lecture, phrase ajoutée par le lecteur aux attendus par hasard).
   Avantage : aucun écart, aucun délai, aucun code neuf. Inconvénient : biais connu laissé dans la lecture ; risque non négligeable de
   perdre une couche entière par une calibration en échec à tort ; « négligeable », dans le texte, devient une affirmation fausse.
2. **Addendum : statistique des directions nulles calculée sans elles-mêmes** (pour C(u_j), moyenne et écart type des M − 1 autres,
   par formule exacte ; pour P(u_j), quantile 0,99 des M − 1 autres, tiré des statistiques d'ordre du jeton ; familles inchangées ;
   inchangé pour v et les témoins). Avantage : biais ramené au niveau nominal sur le banc (5,13 %) ;
   coût de calcul faible (une passe sur le tableau des scores nuls, plus un tri par jeton pour le quantile) ; quelques dizaines de
   lignes dans `statistiques_v1.resumer_nul` ;
   calibration et bornes inchangées. Inconvénient : écart à un texte scellé (addendum, contre-lecture, revérification du code) ; validité
   approchée, non exacte (v jugé contre M directions, u_j contre M − 1 : différence d'ordre 1/M²).
3. **Addendum : moyenne et écart type estimés sur un jeu séparé de M directions nulles** (graine propre), puis v et les u_j jugés avec
   ces mêmes valeurs. Avantage : validité exacte par échangeabilité. Inconvénient : M lectures de plus par nul (≈ +50 % de produits,
   ≈ +10 à 15 min au débit du banc, dans les 8 h) ; code un peu plus long ; même procédure d'écart que l'option 2.

**Recommandation** : **option 2**, par un addendum scellé avant toute lecture d'une sonde réelle, avec la même revérification du code
par ce contre-lecteur. Confiance : 0,7 (le biais et son sens sont sûrs ; sa taille réelle dépend des scores réels, que le banc
n'imite qu'en structure ; l'option 3 vaut si le directeur veut l'exactitude au prix d'un peu de calcul).
**Défaut sous 48 heures** : aucun défaut ne s'applique (écart à un texte scellé : nœud, on attend le mot du directeur) ; tant qu'il
manque, rien ne part.

## 6. Les trois autres points du développeur

- **Pôles « intermédiaires »** : juste ; le texte ne gèle aucune phrase. À ajouter : la sortie des phrases devrait le dire
  explicitement (« pôles intermédiaires : aucune phrase gelée ; valeurs en table ») pour qu'un lecteur ne prenne pas l'absence pour un
  oubli ; toute phrase du lecteur sur eux est « description libre, après lecture, non préenregistrée ».
- **Ligne `CODE-LENTILLES-BBIS`** : la forme est tranchée par la mère ; le code la vérifie désormais (correction A) : fiche citée par
  la ligne, d'empreinte égale à la ligne, de la forme des fiches `CODE-` (`commit`, `fichiers`, `essais`, `contre_lecture`), et
  empreinte de chacun des dix modules égale à celle de `fichiers` sous `src/controle_ia/lentilles_sondes_bbis/<module>.py` ; vérifiée au
  montage et au calcul avant toute requête ou ouverture ; citée dans le rapport du montage et dans le manifeste. Le commit de la fiche est
  rapporté, non exigé égal à `HEAD` (les lignes de registre ajoutées après la fiche changent `HEAD` sans changer le code).
- **Réseau réel non éprouvé** : juste. À ajouter : (i) le voisin lit le tokeniseur d'un dépôt à porte, **sans clé**, depuis le cache posé
  par notre code, alors que `05_act_corpus.py` tourne en ligne : la bibliothèque peut répondre « dépôt à porte » au lieu de lire le
  cache ; c'est après ≈ 12 Go de flux. Recommandation : jouer, juste après la pose du cache, un enfant hors ligne qui charge le tokeniseur
  et décode un jeton (arrêt tôt et bon marché) ; (ii) les clés de `J` (entiers) et les types de `provenance` sous `weights_only=True` ne
  sont éprouvés que sur jouet (un écart arrête : nœud) ; (iii) le retrait de la clé sur une redirection vers un autre hôte repose sur
  `requests` ; (iv) **disque** : ce conteneur n'avait que 4,4 Go libres au début de cette contre-lecture, sous les 6 Go exigés au départ
  du montage : l'opérateur vérifiera la place avant de lancer.

## 7. Corrections (texte avant et après)

(Aucune ligne de calcul n'est changée : A à D touchent les gardes, le versement et l'impression.)

Éprouvées sur une copie du paquet (aucun fichier du dépôt modifié) : essais ciblés et dix-sept essais neufs : **274 passed, 1 skipped**
(l'essai sauté demande le programme des bornes du texte, absent de la petite copie ; il passe sur l'extraction complète). Le diff complet,
avant et après, est en annexe (`contre-lecture-outils-v1/corrections-v1.diff`). Noms : la mère choisit entre correction en place avant
`CODE-LENTILLES-BBIS` (l'historique git garde l'état) et noms neufs (R12) ; le développeur l'a déjà posé.

**A. Fiche `CODE-LENTILLES-BBIS` vérifiée par le code** (`lanceur_v1.py`).
Avant (`monter`, et de même au début de `calculer`) :
```python
    r = ctx.reglages
    en.exiger_registre_propre(ctx.registre_propre)
```
Après :
```python
    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, en.exiger_registre_propre(ctx.registre_propre)["CODE-LENTILLES-BBIS"])
```
avec la fonction neuve `exiger_fiche_code(racine_depot, ligne_code)` : fiche absente ou d'une empreinte autre que la ligne → `Refus` ;
fiche sans `commit`, `fichiers` (dictionnaire), `essais` (dictionnaire), `contre_lecture.chemin` et `contre_lecture.sha256` → `Refus` ;
pour chacun des dix modules, `fichiers["src/controle_ia/lentilles_sondes_bbis/<module>.py"]` différent du SHA-256 du fichier exécuté →
`Refus` ; rend `{fiche, sha256, commit_de_la_fiche}`, écrit sous `code.fiche_code` du rapport du montage et `fiche_code` du manifeste.
Essais : fiche saine ; absente ; altérée d'un octet ; un module d'une autre empreinte ; un module absent ; forme sans `contre_lecture` ;
montage sans fiche : refus avant toute requête et sans dossier de travail. Les jouets écrivent une fiche de cette forme
(`ecrire_fiche_code`).

**B. Scellement antérieur au verdict** (`entrees_v1.py`).
Avant : `exiger_scores_et_verdict` rend l'heure de la **dernière** ligne `VERDICT-BBIS` ; aucune comparaison d'heures.
Après : elle rend l'heure de la **première** (`min`) ; fonction neuve `exiger_scellement_avant_verdict(registre_propre, course)` :
`ABSENCE-VERDICT-LENTILLES-BBIS` ou `SCELLEMENT-LENTILLES-BBIS` absente → `Refus` ; la plus tardive des deux non strictement antérieure à
la première `VERDICT-BBIS` → `Refus` (« texte exposé ; rien ne part ; nœud ») ; appelée dans `ouvrir_entrees` et `recuperer_entrees`
juste après `exiger_scores_et_verdict`. Jouets : `VERDICT-BBIS` à `HEURE_VERDICT`, une heure après les lignes du registre propre.
Essais : cas sain ; verdict antérieur ; relevé d'absence manquant.

**C. Versement avant toute suppression, et à l'arrêt** (`lanceur_v1.py`).
Avant :
```python
def nettoyer(travail: Path) -> None:
    travail = Path(travail)
    if not (travail / MARQUE).is_file():
        raise Arret(...)
    shutil.rmtree(travail)
...
    if nettoyage:
        nettoyer(ctx.travail)
```
Après :
```python
NON_COPIES = ("tenseurs", "lentille", "hf", "lentille-publique.pt", "voisin")   # licence ou corpus : inventoriés, jamais copiés

def verser_travail(travail, sortie, run, moment) -> dict:   # inventaire (chemin, taille, SHA-256) de tout fichier ; copie scellée
    ...                                                    # hors NON_COPIES ; `git diff` du voisin ; inventaire fermé et scellé
                                                           # sous <sortie>/versement/<run>/travail-<moment>/
def nettoyer(travail, sortie, run) -> dict:
    if not (travail / MARQUE).is_file():
        raise Arret(...)
    versement = verser_travail(travail, sortie, run, "fin")
    verifier(Path(sortie) / versement["chemin"])
    shutil.rmtree(travail)
    return versement
...
    versement = nettoyer(ctx.travail, ctx.sortie, ctx.run) if nettoyage else None
```
`calculer` devient une enveloppe de `_calculer` : à tout `Arret` levé après le départ du calcul (dossier monté reconnu), les tableaux
déjà calculés sont écrits par `ecrire_morceaux` sous `versement/<run>/calcul-interrompu/lectures-interrompues-non-lues-NNN.npz`
(fermés, scellés), `arret.json` (motif, morceaux, versement du travail à l'arrêt) est fermé et scellé, rien n'est supprimé, puis
l'arrêt est relevé tel quel ; un refus avant le départ (registres, verdict, dossier non monté) ne verse rien. Dans
`Contexte.__post_init__` : dossier de sortie égal au dossier de travail, dedans ou le contenant → `Arret` (« emboîtés »).
Essais : nettoyage qui verse (fichier copié, versement vérifié, dossier supprimé) ; calcul complet qui verse (jetons gardés copiés,
tenseurs inventoriés et non copiés, aucune occurrence de la clé dans les sorties) ; arrêt d'espace disque en cours de calcul (versement
scellé, morceaux interrompus scellés, rien de supprimé) ; refus avant le départ (rien de versé) ; trois emboîtements refusés.

**D. Cloisonnement de l'impression, et essais des gardes non vues** (`lanceur_v1.py`, essais).
Avant (`principal`) : le rendu du calcul est imprimé entier, noms des tableaux compris.
Après :
```python
            if a.commande == "calcul":   # cloisonnement : l'opérateur ne voit que fichiers et empreintes, jamais les noms des tableaux
                rendu["morceaux"] = [{"fichier": m["fichier"], "sha256": m["sha256"]} for m in rendu["morceaux"]]
```
Essais neufs des gardes réelles non vues : `run_id`, `fichier_sondes.fichier`, `cellule`, `pli_lu`, scellement qui ne cite pas ce
texte. À ajouter de même (non écrits ici) : forme de `…_b`, longueur de l'essai d'un octet, commit du voisin, tailles des tenseurs
extraits, `jetons-gardes.json` mal formé, `W_U` d'une autre précision, et les six gardes de la seconde série, dont **le libellé des
pôles après repli**, seul essai manquant que je tiens pour bloquant (il garde une valeur qui entre dans une phrase gelée).

Tout est dans `test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py` (dix-sept essais) ; l'essai existant
`test_nettoyage_refuse_un_dossier_sans_la_marque` est adapté à la signature neuve de `nettoyer` et vérifie le versement.

## 8. Pièces du contre-lecteur

Sous `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-outils-v1/`, chacune scellée : `banc_contre_lecteur_v1.py` et sa
sortie ; `risque_calibration_v1.py`, `risque_calibration_v2.py` et leurs sorties ; `mutations_v1.py`, `mutations_survivants_v1.py`,
`mutations_corrections_v1.py` et leurs sorties ; `sortie-essais-corriges-v1.txt` ;
`corrections-v1.diff`. Aucune n'emploie une donnée, un poids, une sonde ni une lentille réelle.
