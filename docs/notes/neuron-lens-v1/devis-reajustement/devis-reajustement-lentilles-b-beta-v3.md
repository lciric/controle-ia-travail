# Devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), pour les ranger et les faire entrer dans le programme — v3

- Auteur : session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`), branche `claude/brave-galileo-jhp684`, 2026-11-19 ; écrit entre
  08:12 et 08:30 UTC (`date -u`). La v1 (`devis-reajustement-lentilles-b-beta-v1.md`, `1bf439ac…`) reste archivée sans modification.
- **v3** = v2 (`devis-reajustement-lentilles-b-beta-v2.md`, `49dcbc93…`, archivée sans modification) qui intègre l'erratum
  (`erratum-devis-reajustement-v2-v1.md`, `c7915a23…`, retiré du circuit : pas d'erratum sur une pièce de classe A, décision de la mère)
  et la correction D7 de la vérification du critère v2 (`verification-critere-identite-reajustement-v2-v1.md`, `8a6045bb…`), plus la fin
  de course demandée par la réserve N-2 (`3cc64c86…`). **Le § 4 est remplacé par le critère d'identité v3**
  (`critere-identite-reajustement-lentilles-v3.md`), qui prime. Rien d'autre ne change (chiffres, plafonds, préalables). Écrit le
  2026-11-19 vers 10:40 UTC.
- v2 = v1 corrigée selon sa contre-lecture (`contre-lecture-devis-reajustement-lentilles-b-beta-v1.md`, `e58dc66c…`, lecteur neuf d'un
  autre modèle : **non employable**, 1 bloquante, 6 majeures, 11 mineures). Traitement de chaque remarque au § 9.
- Origine : mots de Lazar du 2026-11-19 (« je vais faire entrer maintenant ces lentilles dans le programme », « a, prépare le devis du
  réajustement ») ; décision posée : `decision-entree-lentilles-programme-v1.md` (`6aaf54e7…`).
- Statut : **devis, aucune dépense engagée**. Rien ne part sans ligne de GO de calcul neuve (nœud de Lazar), les préalables du § 5 et la
  vérification de la différence v1→v2 (R2).

## 1. Pourquoi
Les deux lentilles ajustées par la tranche close (course `20261118-164930-neuron-lens-b-beta`, verdict « partiel » accepté,
`lecture-b-beta/accord-lazar-verdict-b-beta-v1.md`, `8469add5…`) **n'existent plus** : la décision de lancement (GO-2026-11-18-02, lieu
L1) les laissait sur la machine louée, détruite le 2026-11-19 à 05:45:00Z. Il reste leurs empreintes et des empreintes numériques de leur
contenu, versées (`inventaire-sorties-courses-lentilles-v1.md`, `9f95da40…`) :

| pièce (dans `diag/20261118-164930-neuron-lens-b-beta/`) | ce qu'elle porte pour comparer |
|---|---|
| `b-beta-ajustement-R.json` | fichier d'ajustement de R `r-llama-3.1-8b-instruct-L32-dclm-T128.pt` : empreinte `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`, 8 455 720 309 octets ; différences entre moitiés non arrondies par couche et cible (`diffs_float64`), `n_docs`, longueurs ; `rows_sha256` `a6afd972…` |
| `b-beta-ajustement-S.json` | fichier d'ajustement de S : `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`, 8 589 938 049 octets ; mêmes champs |
| `b-beta-export.json` | **trois exports de R** (entier, moitié paire, moitié impaire) : une empreinte par fichier exporté (noms portant un identifiant de génération propre à chaque export) et deux empreintes par couche des matrices des moitiés (`matrices_moities`, 31 couches) ; aucune taille |
| code de course | dépôt réduit, commit `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` ; code voisin au commit `849bfe16…` |

**Ce qui est établi sur les octets** (lu sans dépense) :
- Le fichier d'ajustement ne contient que `meta` (lentille, modèle, couches, corpus, règles, `rows_sha256`, nombre de documents, longueur,
  `dim_batch`, cibles, part, type numérique : aucune heure, aucun chemin, aucun nom de machine), `state` (sommes et nombre de documents)
  et `next_doc` (code voisin `scripts/02_fit.py`, l. 140-147 et 161-166, au commit `849bfe16`).
- `torch.save` du même dictionnaire, au même nom de fichier, écrit les mêmes octets (essai local du 2026-11-19, torch 2.14.1 : deux
  écritures à 1,5 s d'écart, empreintes égales).
- **Non établi** : que la carte rende les mêmes sommes en virgule flottante d'une machine à l'autre (ordre des réductions), et qu'une
  reprise sur sauvegarde ne change rien (aucune reprise n'est prévue ; une reprise est notée et fait tomber au palier 2 du § 4).
- L'identifiant de génération des fichiers exportés ne vient pas du code voisin (aucune occurrence) mais de la bibliothèque des lentilles
  qu'il appelle : tenu pour différent à chaque export ; les exports se comparent **par couche et par contenu**, jamais par nom.

## 2. Deux variantes
**Variante A — ajustement seul, puis rangement.** Montage ; ajustement de R ; export ; copie de R ; ajustement de S ; copie de S ;
comparaison selon le critère d'identité v3 ; destruction. Aucune mesure refaite. **Au palier 2, la lentille rangée par la variante A n'a
aucune mesure propre** : le verdict du 18 ne se transporte pas (critère v3, § 4).

**Variante B — la course rejouée, plus le rangement.** La commande de la tranche (v8) rejouée entière, avec les changements du § 5,
point 5, et les copies ; les mesures B-1 à B-7 sont refaites sur une autre machine. **Ce qu'elle ajoute à A** : non pas l'identité des
lentilles (les paliers 1 et 2 sont communs ; **seul le palier 1 établit l'identité**), mais une **seconde mesure** sur un autre exemplaire du même modèle de carte (même code, même
corpus, mêmes graines : seule la machine change), utile parce que deux verdicts du 18 tiennent à une marge de l'ordre de l'effet du
matériel (lecture contre pilotage : 55 pôles sur 64 à la couche 8 pour 58 exigés ; deux codes : 20 couches sur 28 pour 21 exigées ;
`lecture-b-beta/verdict-b-beta-v1.md`, `3a9b947e…`, « Verdict, en mots simples »). Son statut est fixé par le § 4, palier 3, et exige un
texte scellé avant la création (§ 5, point 6). **Au palier 2, seule la variante B donne à la lentille rangée des mesures propres.**

## 3. Durées et coût
Durées **mesurées** sur H100 SXM le 18-19 novembre (pièces ci-dessus et `controles-b-beta-v1.log`) : montage jusqu'au début de
l'ajustement de R 1 h 14 (16:48:55 → 18:03:15 ; dont installation ≈ 59 min pour une borne de 3 600 s : le lanceur v4 la porte à
7 200 s, § 5) ; ajustement de R 18 414 s ; export 78 s ; ajustement de S 18 065 s ; suite de la course 1 h 19 (04:12:35 → 05:31:55) ;
fin de course jusqu'à la destruction 0,2 h (12,72 h de course, 12,93 h de location). Volume à copier : ≈ 17 Go de fichiers d'ajustement
et ≈ 13 Gio d'exports (commande v8, l. 288, estimé), soit **≈ 31 Go** ; à 200 Mbit/s (débit montant exigé) ≈ 0,35 h ; le débit en
écriture de la plateforme de modèles n'est pas mesuré (pire cas pris à 100 Mbit/s).

| bloc | attendu | pire cas | source du pire cas |
|---|---|---|---|
| montage | 1,25 h | 2,5 h | deux fois le mesuré (borne d'installation relevée à 7 200 s) |
| ajustements R et S, export | 10,16 h | 13,1 h | pire cas du devis v12 (6,56 h par lentille) |
| suite de la course (variante B) | 1,3 h | 2,6 h | deux fois le mesuré |
| copies (≈ 31 Go) | 0,35 h | 0,69 h | 100 Mbit/s |
| vérification à l'arrivée, préavis, destruction | 0,25 h | 0,25 h | mesuré 0,2 h le 19, plus la relecture au lieu |
| **variante A** | **12,0 h** | **16,5 h** | |
| **variante B** | **13,3 h** | **19,1 h** | |

**Prix** : relevé `releve-prix-vast-h100-20261119T080302Z-v1.tsv` (`90395583…`, 08:03:02 UTC) : une seule offre vérifiée sous 4 USD/h au
filtre complet, Japon, offre 59816165, **2,3713 USD/h avec 200 Go**, trafic sortant et entrant **0**, débit montant 1 744 Mbit/s,
fiabilité 0,9917 ; la suivante à 4,0990 (États-Unis). Le relevé est refait dans l'heure qui précède la création, avec les colonnes des deux
options ci-dessous (ses colonnes actuelles sont celles de la v8).

**Trafic** : réservé à **2,3 USD** de frais fixes (≈ 25 Go entrants et ≈ 31 Go sortants à 0,04 USD/Go, plafond de trafic du filtre) ;
nul à l'offre du relevé.

| | attendu à 2,37 | pire cas à 2,37 | pire cas au prix exigé de 2,62 | avec frais fixes |
|---|---|---|---|---|
| variante A | ≈ 28,5 USD | ≈ 39,2 USD | ≈ 43,3 USD | ≈ 45,6 USD |
| variante B | ≈ 31,6 USD | ≈ 45,4 USD | ≈ 50,1 USD | ≈ 52,4 USD |

**Plafonds proposés** (formules de la v8 : compte rendu 60 %, arrêt dur 90 %, minuterie = (arrêt dur − frais fixes) / prix lu ; la garde
compte au plus grand du prix déclaré, 2,62, et du prix lu ; marge d'au moins 5 % entre le pire cas avec frais et l'arrêt dur) :
- **variante A : plafond 54 USD** ; arrêt dur 48,6 ; minuterie (48,6 − 2,3) / 2,62 = **17,7 h** pour un pire cas de 16,5 h ; prix minimal
  de la règle du refus (48,6 − 2,3) / 36 = 1,29 USD/h ; compte rendu 32,4 USD, atteint vers 11,5 h, **donc en course normale** (avant les
  12,0 h attendues) : il est attendu et ne signale rien à lui seul ;
- **variante B : plafond 62 USD** ; arrêt dur 55,8 ; minuterie (55,8 − 2,3) / 2,62 = **20,4 h** pour un pire cas de 19,1 h ; prix minimal
  1,49 USD/h ; compte rendu 37,2 USD vers 13,3 h, **attendu en course normale**.
La garde arrête à ces durées quel que soit le prix lu ; la minuterie, plus longue au prix lu (19,5 h et 22,6 h à 2,37), est le filet.

**Risques** : le mesuré de l'ajustement (5,12 h) vaut 78 % du pire cas par lentille et a dépassé le haut de l'attendu du devis v12 ; une
machine plus lente arrête la course au banc du montage (seuil de 23,6 s par document) : perte faible, aucune reprise sans devis neuf.
**Perte de la machine** : arrêt, aucune reprise sans devis neuf ; avec les copies faites au fil de l'eau (§ 5, point 3), une perte après
la copie de R ne coûte que S.

## 4. Critère d'identité, et statut de la seconde mesure — remplacé par le critère v3
Le texte de la v2 (paliers, tolérance de 10⁻⁶, mention « lentille équivalente, octets différents ») est **remplacé** par
`critere-identite-reajustement-lentilles-v3.md`, à sceller avant toute création. En bref : **seul le palier 1 (octets identiques)
établit l'identité** ; au palier 2 (« différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non
comparables »), l'identité n'est pas établie et le verdict du 18 ne se transporte pas ; « différente » ou « non comparable » : rangée,
marquée, aucune lecture sans nœud de Lazar. Le statut de la seconde mesure (variante B) reste celui de la v2 : le verdict scellé et
accepté du 18 reste celui de la tranche ; la seconde course est lue par un lecteur neuf sur un plan scellé et rapportée à côté ; tout
désaccord est un nœud de Lazar.

## 5. Préalables, tous sans dépense (rien ne part sans eux)
1. **Ligne de GO de calcul neuve** (type « calcul »), nommée par la mère sur le mot de Lazar : variante, prix exigé, plafond, échéance.
2. **Nœud de l'entrée des lentilles dans le programme** inscrit par la mère (pièces : `decision-entree-lentilles-programme-v1.md`).
3. **Lieu de rangement** choisi par Lazar (§ 6) et prêt. Avec L2 : copie de R dès son export, de S dès la fin de son ajustement (la clé
   est de toute façon sur la machine : la copier au fil de l'eau ne l'expose pas plus longtemps et borne la perte) ; empreintes calculées
   sur la machine avant envoi. **Fin de course** (réserve N-2) : copie ; **première relecture** des empreintes au lieu de rangement par la
   session, clé de la machine encore valide (une copie fausse peut encore être refaite) ; **destruction de la machine sans attendre
   Lazar** ; puis révocation de la clé par Lazar et **seconde relecture** de la même révision ; par les empreintes que la plateforme rend pour ses gros fichiers (sans retéléchargement), avec la clé gardée de la session
   (lecture seule) ; si la plateforme ne rend pas d'empreinte : téléchargement par la session (≈ 31 Go : disque et temps à dire avant).
4. **Clé** : la clé actuelle reste gardée (mot de Lazar) et **n'est pas passée** à la machine ; une **clé neuve à droits restreints** (lecture
   du modèle à accès contrôlé ; écriture sur le seul dépôt de rangement) est créée par Lazar, passée à la création, révoquée par Lazar après
   la copie. Risque déclaré : exposée dès la création, elle permet d'écraser le dépôt ; parade : chaque copie vérifiée par empreinte à
   l'arrivée, révision du dépôt notée à chaque copie.
5. **Code et commande** (à écrire, essayer sur cas sain et artefact, contre-lire) : lanceur et amorce v4 = v3 avec (a) le GO attendu
   nouveau, (b) la branche de résultats `calcul/neuron-lens-reajustement-v1`, (c) **la clé gardée sur la machine toute la course** au lieu
   d'être retirée après le téléchargement (changement des gardes de secrets : le balayage des secrets avant chaque poussée, toutes les dix
   minutes, est refait et ses 14 formes rejouées à blanc avec cette clé présente), (d) les deux étapes de copie avec vérification, (e) la
   borne d'installation portée à 7 200 s, (f) pour la variante A, arrêt après la copie de S ; commande v9 ; essai à blanc refait.
6. **Textes scellés et contre-lus** : le critère du § 4 ; pour la variante B, le **statut de la seconde mesure** (§ 4, palier 3) et le
   plan de sa lecture par un lecteur neuf.
7. **Crédit du loueur** : **9,05 USD** au relevé de la session (`releve-credit-20261119T081130Z-v1.txt`, 08:11:29 UTC, crédit seul).
   La recharge automatique (5 USD sous 5 USD) est celle sur laquelle Lazar a levé la condition de crédit de la v8 (R-3319) ; elle a tenu le
   18 et le 19. **Proposition, un seul montant** : recharger **au moins le plafond retenu** (54 ou 62 USD) avant la création, en plus des
   autres lignes ouvertes ce jour-là sur le même compte (à chiffrer par la mère le jour du GO), et garder la garde de la v8 (crédit < 1 USD
   → arrêt). Budget journalier de 100 euros (mot de Lazar relayé par la mère, devis v12, § 2, point 8) : la dépense attendue (≈ 29 à 32 USD)
   y tient seule ; avec les autres courses du jour, à vérifier par la mère.
8. **Plateforme de modèles** : coût et quota du stockage privé, débit en écriture, et licence du modèle pour des poids dérivés rangés en
   privé, relevés avant le GO.
9. **Leçon du 19 novembre** : un redémarrage du conteneur de la session tue la minuterie et la garde ; la veille les réarme sur l'échéance
   absolue. Si la session est absente à la fin, la machine attend facturée la relecture et la révocation : la garde (plafond) et la
   minuterie restent le filet ; la mère détruit par identifiant si la session ne répond plus.

## 6. Lieu de rangement (choix de Lazar)
≈ 31 Go (fichiers d'ajustement ≈ 17 Go, exports ≈ 13 Gio) ; au-delà de la limite de l'hébergeur de code (100 Mo par fichier).
- **L2 — dépôt privé de modèles chez la plateforme de modèles** (Hugging Face), créé par Lazar sous son compte ; copie par la machine,
  relecture par la session (§ 5, point 3). Coût et quota : à relever (§ 5, point 8).
- **L3 — une machine de Lazar** : la machine louée pousse vers elle (un accès de sa machine sur la machine louée). « Lazar tire depuis la
  machine louée » supposerait un accès entrant, alors que la commande est sans ssh : écarté sauf changement de commande.

## 7. Décisions demandées à Lazar (par la mère)
**Décision 1 — variante.** Enjeu : ranger des lentilles ; on ne saura si ce sont celles qui ont été jugées qu'au palier 1 ; en option,
remesurer. **Conséquence pour le choix : au palier 2, la lentille rangée par la variante A n'a aucune mesure propre ; seule la variante B
lui en donne.**
Options : **A** (≈ 28,5 USD attendus, plafond 54 ; identité établie au seul palier 1 ; au palier 2, ni identité, ni mesure propre) ; **B** (≈ 31,6 USD attendus, plafond 62 ; mêmes
paliers, plus une seconde mesure des marges minces, lue par un lecteur neuf, sans effet sur le verdict accepté). **Recommandation : B,
confiance 0,6** : ≈ 3 USD et ≈ 1,3 h de plus pour savoir si les deux verdicts à marge mince tiennent sur une autre machine avant d'appuyer
une expérience du programme sur ces lentilles ; A suffit si l'on ne veut que les poids. Défaut sous 48 heures : rien ne part.

**Décision 2 — prix exigé et plafond.** Recommandation : prix exigé 2,62 USD/h ; plafond 62 USD (B) ou 54 (A). Défaut : rien ne part.

**Décision 3 — lieu de rangement et clé.** Recommandation : L2 sous le compte de Lazar ; clé neuve à droits restreints, révoquée après la
copie ; la clé gardée reste hors de la machine. Confiance 0,6 (L3 évite toute clé d'écriture sur la machine mais demande un accès de la
machine de Lazar). Défaut : rien ne part.

**Décision 4 — statut de la seconde mesure** (variante B) : le verdict du 18 reste ; la seconde course est rapportée à côté ; tout
désaccord est un nœud de Lazar (§ 4, palier 3). Recommandation : accepter cette règle. Défaut : rien ne part en variante B.

**Décision 5 — recharge** d'au moins le plafond retenu avant la création (crédit 9,05 USD à 08:11Z).

## 8. Ce que ce devis ne fait pas
Il ne décide pas de l'usage des lentilles dans le programme : chaque expérience qui s'en servira le dira dans son préenregistrement (R1) ;
toute modification d'un texte déjà scellé (par exemple la lecture des sondes de l'étape B bis, qui ne lit aujourd'hui que la lentille
publique) passe par une version nouvelle, contre-lue, et un mot de Lazar.

## 9. Traitement de la contre-lecture de la v1
| remarque | traitement |
|---|---|
| B-1 plafonds sous le pire cas | acceptée : frais fixes 2,3 USD ; copie de ≈ 31 Go au pire 0,69 h ; fin 0,25 h ; plafonds 54 et 62, marge ≥ 5 % (§ 3) |
| M-1 comparaison possible en variante A | acceptée : paliers 1 et 2 communs aux deux variantes ; l'argument de B redit (§ 2, § 4, § 7) |
| M-2 seuil de 0,03 | acceptée : retiré ; tolérance numérique du palier 2 déclarée conventionnelle ; comparaison des mesures sans critère, forme de la garde (j) (§ 4) |
| M-3 seconde mesure sans statut | acceptée : palier 3, préalable 6, décision 4 ; « indépendante » retiré ; chiffres des marges avec chemin et empreinte (§ 2) |
| M-4 clé d'écriture | acceptée : changement du lanceur dit (§ 5, point 5 c) ; copies au fil de l'eau ; relecture après révocation ; L3 « tirer » écarté (§ 6) |
| M-5 égalité d'octets | acceptée : contenu du fichier lu dans le code voisin, essai local de `torch.save`, identifiant de génération, trois exports (§ 1) |
| M-6 crédit | acceptée : relevé de la session versé ; un seul montant ; recharge automatique et garde dites (§ 5, point 7) |
| m-1 prix minimal | accepté : écrit (§ 3) ; colonnes du relevé refaites avant la création |
| m-2 compte rendu en course normale | accepté : dit (§ 3) |
| m-3 arrêt réel par la garde | accepté : dit (§ 3) |
| m-4 marge de l'ajustement | accepté : risque écrit (§ 3) |
| m-5 borne d'installation | accepté : portée à 7 200 s (§ 3, § 5) |
| m-6 disque | accepté en partie : 200 Go gardés (≈ 17 Go d'ajustement, ≈ 13 Gio d'exports, poids ≈ 16 Go, sauvegardes en place) ; la copie lit les fichiers sans les dupliquer : exigé du code de copie (§ 5, point 5 d) |
| m-7 plateforme et licence | accepté : préalable 8 |
| m-8 durée de fin | accepté : 0,25 h comptée |
| m-9 détails | acceptés : fin 05:31:55Z ; heure d'écriture relevée ; 932 documents sans effet |
| m-10 session absente à la fin | accepté : § 5, point 9 |
| m-11 cas mixte | accepté : chaque lentille jugée séparément (§ 4) |
