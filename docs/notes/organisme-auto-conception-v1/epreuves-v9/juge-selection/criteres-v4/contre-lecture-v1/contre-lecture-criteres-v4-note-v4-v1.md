# Contre-lecture des critères de choix v4, de la note sur le juge v4 et des trois programmes — v1

- **Contre-lecteur, modèle O, neuf.** Je n'ai écrit ni le mandat du rédacteur, ni les critères, ni la note, ni les programmes, ni aucune carte, ni aucun rejeu (règle R2). Écrit le 2026-11-20 (`date -u` : 2026-11-20T02:04:14Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau hors `git fetch` et `git show` du dépôt. Rien n'est écrit dans le dépôt.
- **Mandat** : `JUGE/criteres-v4/mandat-contre-lecteur-criteres-v4-note-v4-v1.md`, sha256 `75e7da7ff7256e5a6427dd28aa2576403be708d7c393ca06fe6bb1534fcf050b`, égale à son compagnon. Point ajouté par la session en cours de travail, à la demande de la mère (R-4050) : les deux tests désignés d'avance à 0,025 ; il est traité au § 2. (JUGE = `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/`.)

## Verdict

**Conforme après corrections.** Huit corrections, au § 4, texte ancien et texte nouveau. Deux sont de fond. La première porte sur les deux tests à 0,025 : ils dépendent d'une valeur déjà vue et doivent sortir de la v4. La seconde porte sur le défaut de la décision 2 : son contenu change alors que son délai court. Les huit constats, les consignes et les recommandations de l'audit sont portés, chacun à sa place. Les v3 sont intactes. Les v4 sont, à l'octet près, la v3 plus les opérations déclarées. Les 134 essais passent chez moi. Aucune carte n'a été ouverte. Aucun outil ni classifieur n'a refusé.

## 1. Ce qui est vérifié et tient

**Empreintes** (`sha256sum -c` sur chaque compagnon, par `env -C` sur le dossier) : toutes égales.
- Pièces contre-lues : les critères v4 (`8e8c6194e3719afc01339a41071f1405d3765b33ddaa461d7834276da5d38582`), la note v4 (`4b2c5ad24351777764b695e65129b93295b3e0ae17d8db4e29977526264217c6`), l'assemblage (`258d5de7ae97152ef97acfd9a29b063119c5cdf61aca8e80e269643c775a4cf3`), le masque (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`), le lecteur par programme (`f656bd5260466b146103d3b7c29a4d5605c56d00d501f92e84686121dcce1319`) et le rapport (`5530e316b27ad49e732ff5e0ca9da3083d2aeb393f4a04ae8b7febc63c73bc7b`).
- Aussi : les trois essais, leurs trois sorties, la mesure du faux déclenchement et sa sortie, l'outil de construction, les deux fichiers d'opérations et `ecrire_compagnons_v1.py`.
- Pièces qui font foi : le mandat du rédacteur (`b7831779…`), la contre-lecture v3 (`cce1a8f4…`), l'audit (`ff814fc9…`), les critères v3 (`1ce41903…`), la note v3 (`de9d144d…`), la statistique de famille (`bb2fa4a8…`), son programme et sa contre-lecture.
- Recalculées : les consignes de la mère (`986e3a3c…`) et l'ordre de passage v3 (`b19f550b…`).
- Sur `origin/main` (après `fetch`) : la note de littérature (`bb54b685…`, égale). Copie de `registres/go.md` : `4ef8b490867bbda1e77defd47abdf967b28bd8fbe101a12a3068efb4faa38f51`. Elle diffère de la copie du rédacteur (`7fce4374…`) parce que `main` a avancé ; les lignes lues ne changent pas.

**V3 intactes, v4 rejouées à l'octet.** J'ai copié les deux v3, les deux fichiers d'opérations et `construire_par_lignes_v1.py` dans mon dossier, puis rejoué l'outil :
- les critères donnent `8e8c6194…` (27 opérations, 360 lignes) ;
- la note donne `4b2c5ad2…` (15 opérations, 373 lignes).

C'est égal aux pièces versées. L'outil vérifie l'empreinte de la source avant tout. Il refuse deux opérations sur une même ligne et refuse d'écraser. Il ne contrôle pas deux limites : une insertion placée à l'intérieur d'une plage remplacée, et l'ordre de deux insertions après une même ligne (elles s'appliqueraient en ordre inverse). Aucun des deux fichiers d'opérations n'a ce cas : sans effet ici.

**Les huit constats de `cce1a8f4…`, chacun à sa place.**
- 1 (i) : deux gardes à statistique et seuil (critères § 5.3 ; code `gardes_coeur`). 1 (ii) : retour à Lazar avant adoption, dans les deux sens, « pas une condition de réussite » ; mais le titre de l'option (a) de la décision 1 dit le contraire (correction C3). 1 (iii) : réponse « ajoutable », trois régimes, posés comme option (décision 4).
- 2 : axe A « voisin » ; la définition scellée fait foi. Je l'ai vérifié sur la ligne 28 de l'ordre de passage v3 : elle exclut bien « un instrument qui mesure sans changer ce qui est promu ».
- 3 : commande `tiers`, par voie, par sous-strate et par espèce.
- 4 : les sept cas, que j'ai vérifiés dans le code un par un :
  - veto sur une carte visée, écartée ou rendue : « sans objet », suppléante suivante ;
  - permutation sur toutes les cartes lues ;
  - porteuse choisie au plancher, puis par les clés 1 à 7 sous la voie de chaque lecteur, puis par le numéro de la carte ;
  - clés 3 à 6 sur les seuls items gardés ;
  - A1 et A4 sous leurs deux formes ;
  - séparabilité en désaccord : notée et signalée ;
  - garde du tiers « chez l'un au moins ».
- 5 : kappa, et item « gardé sans accord au-delà du hasard ». 6 : clé 7 comptée à part.
- 7 : « 90 sur 94 » chez O ; « 28 sur 92, 62 à un point, 2 à deux » chez F. Le rédacteur corrige ici, à juste titre, le « toutes à un point » de la contre-lecture. Les totaux du tableau de l'audit, § 3, donnent bien 28, 62 et 2.
- 8 : huit confirmations, chacune avec son défaut. Il y en a deux de plus que les six de la v3 : les seuils des gardes, et les réglages du masque.

**Consignes et GO.**
- R-3876 : les neuf comptes du veto (code `resoudre_veto`) et le plafond commun au nombre visé.
- GO-2026-11-19-68 : deux et trois cartes, avec et sans plafond, rejouées à chaque sélection (code `comparaison_veto`). Le tableau de la note, § 5, est juste : 4 et 6 cartes ; 14 et 21 demandées, 9 entrent, 5 et 12 coupées.
- GO-2026-11-19-69 : le coût reste hors de toute note, de toute clé et de tout plancher (§ 0, § 7, § 10).
- « Question neuve ≠ zéro » : § 4.2.
- GO-2026-11-19-89, que le rédacteur n'a pas lue : rien de la v4 ne sert au proposeur un score ni un verdict de juge. Pas de contradiction.
- Recommandations de l'audit :
  - D inchangé depuis la v3 ;
  - limite et signal « 11 sur 16 contre 1 sur 46 » en tête, et imprimés par le programme ;
  - lecteur par programme ;
  - masque ;
  - veto filtré par famille et compté tel que déposé.

**Chiffres repris, vérifiés sur leur source.**
- De l'audit : 11 sur 16 contre 1 sur 46 ; 16 sur 35 contre 12 sur 57, p = 0,012 ; 6,00 contre 5,93, p = 0,57 ; 27 % de la variance et 23 points ; 0,024 contre 37 sur 94 ; 37 cartes de la famille sur 94.
- De la note de littérature, ligne 18 : de 17,5 % à 9,0 % de fuite, avec un juge changé.
- De la sortie de la mesure du faux déclenchement : 3 mondes sur 60.

**Tirages (R9).**
- `SeedSequence([int(h1,16), int(h2,16)])`, `spawn(4)`, puis `PCG64`, dans l'ordre du § 9 : voies, départage, lot, titulaires.
- Graines des gardes : la chaîne `gardes-par-espece-v4-v1`, puis un enfant par test, dans l'ordre écrit : item par item, lignées puis famille ; puis groupe par groupe, cinq objets par groupe.
- Graines de `tiers` : par l'empreinte de l'ordre.
- Le masque et le lecteur par programme ne tirent rien.

**N-058 et la parole de Lazar.** Partout, la règle, les lecteurs, le veto et les gardes proposent ; l'épreuve tranche. Le taux de réussite des veto ne choisit ni ne pondère personne (§ 8). Aucune garde ne corrige une liste. Seul écart de lettre : le titre de la décision 1, option (a) (C3).

**Noms de lignées.** « Opus », « Fable », « Argon », « Carbon » et « Astra » sont des étiquettes de famille. Une recherche dans tout le dossier `criteres-v4/` ne trouve aucun identifiant de modèle véritable : aucun motif `claude-…`, aucun nom suivi d'un numéro de version.

**Choix motivés, au regard de R3.**
- *Veto filtré par famille* : motivé par un principe de récusation (le titulaire ne sauve pas sa famille). Le 4 sur 4 de l'audit n'en est que l'illustration ; aucun seuil n'est réglé sur lui. Son prix est dit : tant que les lecteurs sont seuls titulaires, aucune carte de leur famille n'entre par veto. Ce choix ne vise pas un signe. Il crée cependant un test vide par construction dans la garde 2 (C7).
- *Masque coupé à la médiane* : la médiane est un quantile des données à venir, et non une valeur observée ; la règle est définie par la longueur, non par l'espèce. Elle ne vise pas un signe. Mais elle peut retirer le canal qu'elle doit éprouver (C4).
- *Deux tests à 0,025* : non. Voir le § 2.

## 2. Les deux tests désignés d'avance à 0,025 (R-4050)

**(a) Le choix dépend-il de la valeur déjà vue ? Oui, de quatre façons.**
1. **Sa seule raison écrite est cette valeur.** Critères, § 5.3 : « le compte de l'audit sur le veto, p = 0,024 […], n'y passerait pas. Deux tests sont donc désignés d'avance ». La note, § 8, dit de même. La règle est justifiée par l'effet qu'elle aurait sur un résultat connu.
2. **Le seuil se place juste au-dessus de cette valeur, et c'est ce qui la fait passer.** J'ai fait un calcul exact, hypergéométrique, non stratifié, base 37 sur 94 (programme `outils/verif_contre_lecture_v1.py`, `5fda646d…` ; sortie `verif-contre-lecture-sortie-v1.txt`, `a1522f97…`). La configuration vue, quatre cartes sur quatre de la famille, donne p ≈ 0,022. Elle passe à 0,025. Elle ne passe pas sous Holm à douze tests, où la plus petite p doit être au plus 0,05/12 ≈ 0,0042.
   Pour la liste attendue par défaut (deux titulaires, trois cartes chacun, soit six cartes), 0,025 et Holm déclenchent sur les mêmes issues dans le sens « plus » : six sur six seulement (p ≈ 0,0029). Le gain du seuil neuf tient donc surtout à la configuration déjà vue.
3. **Le test désigné est celui où la valeur a été vue.** Un test choisi après avoir vu la quantité qu'il vise n'est pas « désigné d'avance ». Peu importe que 0,025 soit aussi 0,05/2 : le choix du test vient des données. Aucune désignation symétrique n'est faite pour les listes ni pour les sens où rien n'a été vu (règle R4).
4. **La valeur ne vient même pas de la même statistique.** Le 0,024 de l'audit est un binomial contre 37 sur 94, sur les 4 cartes d'espèce connue. La statistique scellée est une permutation stratifiée par voie, sur toutes les cartes déposées, couverture complète. « N'y passerait pas » est une analogie, non un calcul.

Le rejeu v4 aura d'autres lecteurs et d'autres listes, mais les 94 cartes et la famille seront les mêmes. La règle est réglée pour qu'une répétition du motif vu déclenche : c'est le risque que R1, R3 et R4 interdisent. Elle touche aussi la lecture d'une pièce scellée et contre-lue : c'est un écart à un préenregistrement scellé, donc un nœud qui demande le mot de Lazar. La mère a raison sur les deux points.

**(b) Options qui ne dépendent d'aucune valeur observée.**

1. **Garder la statistique scellée telle quelle** — ma recommandation, confiance 0,75.
   - Avantage : aucune pièce scellée n'est touchée, rien ne dépend d'une valeur vue, et Holm tient le taux de fausse alerte. La perte de puissance sur les listes courtes est une limite qui se déduit des seuls effectifs ; on l'écrit.
   - Inconvénient : la statistique reste presque aveugle au veto. Un écart de la taille de celui de la v2 ne déclencherait rien.
2. **Une règle neuve, dans une pièce neuve**, par exemple `statistique-famille-rejeu-v4-v1.md`. Elle serait motivée par les seuls effectifs, écrite sans référence à aucune valeur observée, contre-lue, scellée avant toute lecture v4, et soumise au mot de Lazar. Deux formes possibles : une correction pour tests discrets, qui ne compte dans Holm que les tests capables de conclure (méthode de Tarone, connue, non vérifiée sur source ici, règle R7) ; ou une hiérarchie fixée par un principe et non par une valeur, par exemple l'assemblage avant les lectures seules.
   - Avantage : plus de puissance, sans désigner un test d'après les données.
   - Inconvénient : une pièce, une contre-lecture et un mot de Lazar de plus, et du délai. Le rédacteur de cette pièce a vu le 0,024 ; il doit le déclarer et ne pas s'en servir.
3. **Lecture descriptive seulement.** La p brute ≤ 0,05 de chaque liste est déjà « signalée comme indice, sans autre effet » par la pièce scellée (§ 5, point 4) ; la proposition la recopie en tête.
   - Avantage : rien à changer, c'est la lettre scellée.
   - Inconvénient : un indice ne renvoie pas à Lazar avant adoption.

Les options 1 et 3 se combinent sans rien écrire de neuf. L'option 2 est à poser à Lazar par la mère, avant toute lecture v4, s'il veut plus de puissance.

**(c) Ce que la v4 doit dire, en texte exact** : correction C1 au § 4. Elle retire les deux tests, écrit la limite sans chiffre vu, et refait le taux de faux déclenchement : 0,05 × 3 + 0,05, soit une fois sur cinq au plus.

## 3. Programmes, essais et réserve de la graine 8 (R4, R5)

**Essais lancés par moi**, sur mes copies, par `python3 -B -m pytest -q -p no:cacheprovider CHEMIN` (Python 3.13.18) :
- assemblage : **81 passés, 0 échoué** (43,9 s) ;
- masque : **27 passés** ;
- lecteur par programme : **26 passés**.

C'est égal aux sorties versées.

**Gardes d'entrée** (manifeste, lecture, empreintes, écrasement, numpy) : chacune a son cas sain et son artefact. Le refus se fait par le code 2, sans rien écrire. Le filtre du veto sans table d'espèces est refusé, jamais laissé sans filtre. Une carte notée sans espèce est refusée. Je n'ai trouvé aucun repli silencieux qui compte, sauf deux valeurs résiduelles du lecteur par programme (C5).

Petite remarque, sans correction : si les deux lecteurs étaient de deux familles, `gardes` sauterait le niveau « famille » sans l'écrire. Ce n'est pas le cas sous la v4.

**La graine 8.** J'ai rejoué les mondes sans effet planté, à 400 et à 2 000 permutations (sortie `a1522f97…`) :
- graine 7 : se déclenche (item A2, niveau des lignées) ;
- graine 11 : se déclenche à 400 permutations, plus à 2 000 ;
- graine 8 : silencieuse.

Mon jugement :
- **Au regard de R5**, un « cas sain » choisi parce qu'il ne déclenche pas ne prouve qu'une chose : qu'il existe un monde nul où rien ne sonne. Tout test à seuil inférieur à 1 en a. Ce n'est pas l'épreuve de la garde sur une entrée saine. Le vrai cas sain du programme est l'essai de taux : 30 mondes fixés d'avance (graines 100 à 129), au plus 8 déclenchements. Je n'ai pas trouvé de raison de croire cette borne fixée après coup.
- **Au regard de R4**, un résultat propre obtenu en choisissant la graine est « trop beau » par construction. La réserve est donc juste, et honnêtement déclarée. L'essai doit cependant être requalifié, et un cas sain par construction ajouté : un monde où chaque lignée reçoit, dans chaque voie, les mêmes réponses. La part de variance entre groupes y est nulle et T = 0, donc aucune garde ne peut sonner, quelle que soit la graine (C6).
- **Artefacts** : ceux de la garde 1 sont joués sur la graine 7, qui sonne déjà par hasard. Leur assertion « retour à Lazar » est donc vide. Leurs assertions sur l'item planté (B3, S3) restent informatives : dans le monde 7 non retouché, seul A2 est nommé. C'est à écrire dans l'essai (C6).

**Lecteur par programme.** Sur des phrases inventées (programme `outils/verif_lecteur_v1.py`, `9d4736a2…` ; sortie `verif-lecteur-sortie-v1.txt`, `e2a532ae…`) :
- « ne pas adopter », « ne pas retenir le module » et « garder la base » donnent chacune **D = 2** : le terme du « oui » est trouvé à l'intérieur de la négation ;
- une carte sans aucun terme reçoit D = 0 et la voie N, non « indécidable ».

Le témoin de D, qui est le canal de l'audit, se trompe donc dans le sens de 2 (C5).

**Garde 2 et filtre du veto.** Sous le filtre « famille », la présence de la famille des lecteurs parmi les cartes entrées par veto est nulle par construction. Le test lit alors le filtre, non les lecteurs, et il alourdit Holm (C7).

## 4. Corrections

Elles sont à appliquer par un rédacteur de modèle F. « Critères » = `criteres-choix-cartes-v9-v4.md` ; « note » = `note-conception-juge-selection-cartes-ecartees-v4.md`. Les numéros de ligne sont ceux des pièces versées. Comme pour la v4, la v5 se construit par un fichier d'opérations : les v4 ne sont pas encore scellées, mais elles sont versées.

**C1 — moyen — retirer les deux tests à 0,025 (§ 2).**
- Critères, ligne 176. Ancien, de « **Un point est ajouté ici, par cette pièce neuve et sans la réécrire** » jusqu'à la fin de la ligne (« …lu sur la sortie du programme scellé. »). Nouveau : « Elle s'applique telle quelle au rejeu des critères v4 : sa « note » est la note fine de l'assemblage (`cartes[].note`), et sa liste « veto » est `listes.veto_depose_titulaires`, avant tout retrait. **Limite, déduite des seuls effectifs et dite d'avance** : avec la correction de Holm, une liste courte — celles du veto — ne peut y porter un « signal présent » que si elle est presque entière d'un côté. Cette limite n'est pas corrigée ici : changer la lecture d'une pièce scellée demande une pièce neuve et le mot de Lazar, et aucune règle de lecture ne se règle d'après une valeur déjà vue (règles R1, R3, R4). La p brute de chaque liste reste rapportée « comme indice, sans autre effet », comme le prévoit la pièce scellée (§ 5, point 4). »
- Critères, ligne 177. Ancien : « Un item nommé, un écart fort, un « signal présent » de la statistique scellée ou un déclenchement des deux tests désignés : ». Nouveau : « Un item nommé, un écart fort ou un « signal présent » de la statistique scellée : ».
- Critères, ligne 178. Ancien : « Trois familles de tests à 0,05 (deux niveaux de la garde 1, la garde 2), la statistique scellée à 0,05 et deux tests désignés à 0,025 chacun : par la borne de la somme, une fois sur quatre au plus quand il n'y a aucun effet. » Nouveau : « Trois familles de tests à 0,05 (deux niveaux de la garde 1, la garde 2) et la statistique scellée à 0,05 : par la borne de la somme, une fois sur cinq au plus quand il n'y a aucun effet. »
- Critères, ligne 306. Ancien : « 7. les seuils des gardes par espèce (0,05 après correction de Holm ; trois cartes au moins ; dix mille permutations) et les deux tests désignés d'avance à 0,025 ; ». Nouveau : « 7. les seuils des gardes par espèce (0,05 après correction de Holm ; trois cartes au moins ; dix mille permutations) ; ».
- Critères, ligne 320. Ancien : « les trois choix de la statistique de famille confirmés, deux tests désignés d'avance ajoutés (A4). » Nouveau : « les trois choix de la statistique de famille confirmés, sa limite sur les listes courtes écrite, aucun test ajouté (A4). »
- Note, ligne 240. Ancien : « statistique de famille scellée, trois choix confirmés ; deux tests désignés d'avance ajoutés | ». Nouveau : « statistique de famille scellée, trois choix confirmés ; sa limite sur les listes courtes écrite, aucun test ajouté | ».
- Note, ligne 252. Ancien : la ligne entière, qui commence par « - **Ajout** : ». Nouveau : « - **Limite, non corrigée ici** : la correction de Holm rend la statistique presque aveugle aux listes courtes, qui sont celles du veto ; cela se déduit des seuls effectifs. Je n'ajoute aucun test : une règle de lecture réglée d'après une valeur déjà vue reviendrait à viser un signe (règles R1, R3, R4), et changer la lecture d'une pièce scellée demande ton mot. Si tu veux plus de puissance, la mère peut te poser une pièce neuve, fixée d'après les seuls effectifs et scellée avant toute lecture v4. »
- Note, ligne 271. Ancien : « les gardes se déclenchent à tort une fois sur quatre au plus quand il n'y a rien. » Nouveau : « les gardes se déclenchent à tort une fois sur cinq au plus quand il n'y a rien. »
- Note, ligne 350. Ancien : « 7. Les seuils des gardes par espèce : 0,05 après correction de Holm, trois cartes au moins, dix mille permutations ; deux tests désignés d'avance à 0,025. » Nouveau : « 7. Les seuils des gardes par espèce : 0,05 après correction de Holm, trois cartes au moins, dix mille permutations. »

**C2 — moyen — délai des décisions déjà posées.** Le défaut de la décision 2 posé le 19 vers 14:41Z portait sur la (a) de la v3 : trois puis deux cartes, lecteurs titulaires, retrait par lignée, sans plafond. La v4 garde « Défaut : (a), pour le rejeu seulement » et la même échéance. Or sa (a) ajoute le plafond au nombre visé et le retrait par famille. Un défaut que Lazar n'a jamais vu prendrait ainsi effet sur un délai ouvert pour un autre. De même, la décision 1 porte désormais sur les critères v4 et sur la condition « dans chaque voie ». Les défauts des décisions 1 et 3 restent compatibles (rejeu seul, sans adoption ; « non »). Seule la décision 2 change de contenu. Note, ligne 262. Ancien : « Je les reprends ici avec ce que la v4 y change. Les décisions 4 et 5 sont neuves : leur délai court du moment où la mère te les pose. » Nouveau : « Je les reprends ici avec ce que la v4 y change. **Ce qui échoit le 21 vers 14:41Z, ce sont les défauts tels qu'ils ont été posés le 19** : le rejeu seul, sans adoption ; le veto à trois puis deux cartes, tenu par les deux lecteurs, retrait par lignée, pour le rejeu seulement ; la lignée reconnue non déclarée. Ce que la v4 change dans une option — décision 1 : critères v4 et huit items « dans chaque voie » ; décision 2 : plafond au nombre visé et retrait par famille — est une option neuve, dont le délai court du moment où la mère te la pose ; d'ici là, le manifeste porte la valeur du défaut du 19 (`filtre_veto` « lignee », `plafond_veto` null). Les décisions 4 et 5 sont neuves : leur délai court du moment où la mère te les pose. »

**C3 — mineur — titre de la décision 1, option (a)** (constat 1 (ii) ; N-058). Note, ligne 271. Ancien : « **(a) Rejeu d'abord, sans dépense ; adoption seulement s'il range et si aucune garde ne se déclenche.** ». Nouveau : « **(a) Rejeu d'abord, sans dépense ; adoption seulement s'il range ; retour vers toi avant toute adoption si une garde se déclenche.** ».

**C4 — moyen — la coupe du masque peut retirer le canal de D (R4).**
- Critères, ligne 39. Après « Le gain du masque est à mesurer, non à supposer (§ 12). », ajouter : « **Il peut toucher le canal même qu'il doit éprouver** : la coupe retire la fin des champs longs, dont celle du champ « ce qui la réfuterait », où s'écrit souvent l'issue « non » que lit D. Or ce champ est plus long, en moyenne, dans les cartes de la famille des lecteurs (audit `ff814fc9…`, § 6). Un écart par famille qui baisse sous le masque ne se lit donc pas comme une préférence retirée tant que la commande `gardes` n'a pas rapporté, par espèce et pour la famille des lecteurs, la part des cartes dont le D du lecteur par programme baisse entre la forme non masquée et la forme masquée. »
- Programme : `gardes` reçoit les deux sorties du lecteur par programme (masquée et non masquée) et rapporte ce compte. Essais : un cas sain (aucune baisse) et un artefact (baisse plantée dans une seule lignée).
- Note, ligne 329. Après « où une règle de lecture peut se trouver. », ajouter : « Le champ « ce qui la réfuterait », qui porte D, est plus long dans les cartes de la famille des lecteurs : la coupe peut effacer le signal par perte de contenu plutôt que par masque du style. ». Et ajouter l'option : « - **(d) Masque complet, sauf le champ « ce qui la réfuterait », gardé entier.** Avantage : D se lit sur le champ entier ; la longueur des autres champs est effacée. Inconvénient : la longueur de ce champ reste visible, et elle suit un peu la famille ; le programme doit accepter, par champ, un plafond « mediane » ou « aucun ». »

**C5 — mineur — lecteur par programme.**
- Programme : chercher les termes du « oui » dans le texte d'où les termes du « non » ont été retirés. Essais : « ne pas adopter », « ne pas retenir le module » et « garder la base » rendent D = 1, en artefact.
- Critères, ligne 43. Ancien : « Il rend « indécidable » plutôt qu'une valeur par défaut. » Nouveau : « Il rend « indécidable » quand le champ est vide ou quand deux voies font jeu égal ; faute de tout terme, il rend la voie N et D = 0, valeurs résiduelles de la règle, et le dit carte par carte (termes trouvés : aucun). »

**C6 — mineur — essais des gardes (R4, R5).**
- Ajouter `test_gardes_cas_sain_par_construction`, sur le monde équilibré du § 3 : aucune garde ne sonne, à deux graines au moins.
- Dans `test_gardes_cas_sain_rien_ne_se_declenche`, remplacer le commentaire par : « graine 8 choisie après coup parce qu'elle ne déclenche pas : sans valeur de preuve ; le cas sain est l'essai par construction et l'essai de taux ».
- Dans les trois artefacts de la garde 1 sur la graine 7, ajouter l'assertion que l'item planté n'est pas nommé sans le plant, et dire en commentaire que le « retour à Lazar » y est déjà vrai par hasard (item A2).
- Relancer les essais et verser la sortie neuve.

**C7 — mineur — garde 2 sous filtre du veto.** Critères, ligne 175. Après « et sous le plancher (statistique : nombre observé moins nombre attendu par voie) », ajouter : « ; sous un filtre du veto, la présence d'un groupe que le filtre retire est nulle par construction parmi les cartes entrées par veto : ce test est « sans objet par construction », hors de la correction, et la garde lit à sa place le veto tel que déposé par les titulaires ». Programme et essais : même changement.

**C8 — mineur — doublon entre la décision 5 et la confirmation 8.**
- Critères, ligne 307. Ancien : « 8. le masque de style : plafond de chaque champ à la médiane de ses longueurs ; phrase récitée retirée à partir d'un cinquième des cartes. » Nouveau : « 8. si la décision 5 garde le masque : phrase récitée retirée à partir d'un cinquième des cartes (la coupe est la décision 5). »
- Note, ligne 351. Ancien : « 8. Les réglages du masque : coupe à la médiane ; phrase récitée retirée à partir d'un cinquième des cartes. » Nouveau : « 8. Si la décision 5 garde le masque : phrase récitée retirée à partir d'un cinquième des cartes (la coupe est la décision 5). »

## 5. Ce que j'ai lu, et ce que je n'ai pas fait

- **Lu en entier** : le mandat ; les critères v4 ; les opérations de la note (le reste de la note v4 est la v3 à l'octet) ; la note v3, § 1 à § 10 ; le rapport ; la contre-lecture v3 ; l'audit ; la statistique de famille ; les consignes de la mère ; les trois programmes et l'outil de construction ; des essais de l'assemblage, la fabrique des mondes et les gardes par espèce.
- **Lu en partie** : la ligne 28 de l'ordre de passage v3 ; la ligne 18 de la note de littérature ; dans `go.md`, les lignes GO-2026-11-19-60, -63, -67, -68, -69, -73 et -89 (les autres lignes de -55 à -74 n'ont pas été ouvertes une à une) ; des essais du masque et du lecteur, les noms seulement.
- **Non lus** : le programme de la statistique et sa contre-lecture, dont j'ai seulement vérifié l'empreinte ; la fiche de la mère du 19 vers 14:41Z, que je n'ai pas trouvée. Le contenu des défauts du 19 est pris du mandat du rédacteur et de la note v3.
- **Jamais touché** : aucune carte, aucun fichier de cartes ni de sélections, le champ `meta`, rien sous `archives-reponses-modeles/`, aucun fichier ni aucune branche interdits.
- **Incident** : une commande `cut` sur ma copie de `go.md` a rendu une sortie trop longue. L'outil l'a rangée de lui-même dans un fichier sous `/root/.claude/`. Je ne l'ai pas ouvert.
- **Aucun refus** d'outil ni de classifieur. Aucun heredoc, aucun code passé en ligne : chaque programme est un fichier lancé par son chemin.

*contre-lecteur, modèle O*
