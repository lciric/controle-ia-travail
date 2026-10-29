# Contre-lecture (R2) de la table de dépendance « critères de G0 → travaux », v6 (version soumise à Lazar)

**Déclaration.** Je n'ai écrit ni la v6 ni son script, ni aucune version ou contre-lecture de cette lignée. Modèle : **Sonnet 5.5** (sous-agent neuf), même famille que
l'auteur de la v5 et que le contre-lecteur de la v5, différent de l'auteur de la v6 (Opus 5.5) ; des erreurs corrélées avec la lignée restent possibles. `date -u` : début
2026-10-29 23:33:17 UTC ; avant l'écriture 23:39:32 UTC. Interdits tenus : rien lu sous `donnees/`, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces` ; aucune branche, aucune
commande git ; aucune dépense ; aucun fichier existant modifié ; rien scellé (ce rapport n'a pas de compagnon `.sha256`) ; les dossiers `cl-table-v*` n'ont pas été ouverts.
Travail dans `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/cl-table-v6/` (mes pièces : `ctest.py`, `alt.py`, `alt2.py`) ; le script a été lancé
en `python3 -I` : aucun `__pycache__` créé dans le dépôt.
**Empreintes** (recalculées, compagnon = recalcul) : table v6 `8d0c72968c7e1b32c979a23dc7c21361add4735771ed35776bec754d1bc73e38` OK ; script
`0a0c19ed2448ace947259f850916747be9ed9c98d5003da9f5a12d59ede56435` OK ; table v1 `e2480618…`, v5 (lue pour le diff), cinq copies de `main` et mémo `9daeb52b…` conformes à
leurs compagnons ou à la table des sources.
**Rejeu** : `scellement verifier` table et script OK ; `verifier … SY` : OK 71 lignes dérivées, 51 lignes de travaux, 20 produits, clause identique à SY § 5 (code 0) ;
`sources` : seule S:D (vivante) a bougé ; `essais` avec dépôt et SY : E01-E48 48/48, CL01-CL32 32/32, N01-N09 9/9, 28 refus sur 28, constat 6 sur 6, **128 gardes, 0
manquante** (code 0) ; `feuille` sur la v6 telle quelle : refus « décisions en attente » (code 2). Diff v5/v6 : seule la ligne W24 change parmi les 71 lignes de travaux et de
produits (jeton `[GEL-SY]`), comme déclaré ; les règles L0, L8 à L14 sont les seules autres différences.

## (a) Le résumé d'une page : exact, complet, sans mot plus fort que la table ?
Exact sur l'essentiel : 51 travaux ; R-765 ; les huit décisions, recommandations et confiances égales au registre (§ 9) ; « aucune n'est présumée » et R-518 ; le script refuse
tant qu'une décision est « en attente » (vérifié). Défauts :
**CT6-01 — La conséquence du silence manque. Gravité : à corriger.** Le résumé dit que la table « ne s'applique pas » sans l'effet : si les huit mots manquent à la date de
D:2, la table n'est pas scellée, V1 est lu sans table et **aucune tâche ne continue** pendant le report (L0, § 6.1, § 6.7 (v)-(vi)). C'est ce qui engage Lazar. Manquent aussi
: la clause scellée de Lazar (N-027 bis) n'existe pas et, si elle diffère, la table est à refaire (§ 8 (1)) ; le résumé pose « reportée une fois » comme acquis alors que R-452
dit « forme de la clause à confirmer ».
**CT6-02 — D:1 (a) mal résumée. Gravité : à corriger.** « une reprise avant la borne, puis « non franchie » » se lit comme « non franchie » après la reprise ; le texte (§ 9)
dit : « non franchie » seulement **sans verdict scellé** le 31 janvier 23:59. « Reprise » heurte la clause (d) (« toute reprise exige une nouvelle version du programme ») :
dire « reprise de la lecture ». La lettre (a) désigne dans le mémo (G0-2, 0,6) la **suspension jusqu'à ton mot**, retirée par la v6 : sans le dire, Lazar, qui a lu le mémo,
peut croire retenir le même (a).
**CT6-03 — Format du dépôt. Gravité : à corriger.** Le § 9 est au format (décision, enjeu, options avec avantage et inconvénient, recommandation et confiance, « en attente »,
aucun défaut) pour D:0b à D:7. Le résumé n'a ni enjeu ni avantage/inconvénient et **ne renvoie pas au § 9** (aucun « § 9 » dans les lignes 3-15). D:2, D:4, D:6 sont des
énoncés, non des questions ; D:4 et D:6 citent « (a) » sans définir les lettres ; D:7 parle de « W19 et W33 » sans les nommer (run des bases de T0.8 ; nouveau run de P3b).
Recommandation de forme : ajouter « détail et options : § 9 » et nommer W19 et W33.
**CT6-04 — Mots plus forts que la table. Gravité : à corriger.** (i) « les critères 2, 3 et 4 … ne peuvent plus avancer » : la table dit que ce dont **le reste exige une
dépense** ne peut plus avancer (§ 6.7 (i)) ; au scénario 13, W13, W15, W18, W40 restent ouvertes. (ii) « Elle ne lit aucun résultat » : L2bis et ‡ lisent la **classe copiée**
(négatif, établi) d'un verdict ; la table dit seulement qu'elle ne lit rien de G1 ni du papier C (L10). (iii) « recommandation de conv-audit » pour les huit : le § 9 attribue
D:1, D:5, D:6, D:7 à l'auteur de la v6 « au nom de conv-audit, qui les confirme ou les corrige avant l'envoi » ; R-521 les liste, sans confirmation explicite. (iv) « pour le
reste, la clause du collisionneur » : (b) est ouvert, (c) sans plafond, (d) avec D:1 (§ 0 le dit, le résumé non). Même défaut dans le § 9 : la recommandation de D:3 écrit «
c'est le plafond … qui rend le critère 6 atteignable » ; il est nécessaire, non suffisant (P-V6 établi, P-L7, P-B4).
**CT6-05 — « Nécessaires aussi » incomplet. Gravité : à corriger.** Le § 9 (« Déjà ouverts ») ajoute le choix n° 4 (empreintes tenues hors dépôt, que la clause cite), le n° 6
(pilote ρ pendant le report) et « session facturée » (SUPPOSÉ) ; le mémo G0-6 donne n° 4 et pilote ρ. Le résumé ne cite que le plafond et G1-2. R-765 laisse « onze autres
choix » ouverts.
**CT6-06 — La phrase unique du résumé est refusée par le script. Gravité : à signaler.** « recommandations de la table v6, D:0b à D:7 » : inscrite telle quelle, elle est
refusée pour D:1 (l'identifiant « D:1 » n'y figure pas ; essai 10 de `ctest.py`) ; acceptée si les huit identifiants sont écrits. Dire « avec les huit identifiants écrits ».

## (b) CT5-01 à CT5-07 traités comme déclaré ?
CT5-01 **oui** : plus aucun défaut (recherche textuelle : « défaut » ne reste que dans la négation et le constat), R-518 cité, registre lu par le script, `feuille` et
`constat` refusent (essais). CT5-02 **oui** pour le texte, avec **CT6-08**. CT5-03 **oui** (D:1 réécrite, (c) marquée contraire à la synthèse, appuis corrigés : SY l. 21, l.
38, l. 72 vérifiées). CT5-04 **oui** (L0, § 6.1). CT5-05 **oui** (copies versées, `S:` sans chemin de bloc-notes, commandes complètes) ; titre : voir **CT6-09**. CT5-06
**oui** (`[GEL-SY]`, le diff le confirme). CT5-07 **oui** (borne réécrite ; W19 et W33 en D:7). Les trente-deux altérations de la contre-lecture de la v5 sont détectées
(rejeu).

## (c) Le script refuse-t-il toute feuille sans les huit décisions citant un mot de Lazar ?
Essais sur copies décidées scellées en bac à sable (`ctest.py`) : décision manquante (D:6) **refusée** ; citation d'une ligne sans « Lazar » **refusée** ; ligne inexistante
(R-9999) **refusée** ; ligne de Lazar d'une autre décision (R-765 pour D:3) **refusée** ; option non admise **refusée** ; « D:10 » pour D:1 **refusée** ; cas sain accepté.
**Mais le contrôle ne porte que sur la forme, et une fausse acceptation existe déjà.**
**CT6-07 — Gravité : à corriger avant le scellement de la v7.** R-521 (`registres/decisions.md` l. 735), relevé de session qui nomme D:0b à D:7 et contient « Lazar », **suffit
pour les huit** : citée « R-521 : option » dans les huit cellules, la feuille est produite (essai 6) ; de même une note de session « Lazar n'a pas encore répondu à D:3 »
(essai 8). R-521 écrit pourtant que le script refuse « tant que les huit décisions ne citent pas une ligne de mot de Lazar » : plus fort que le contrôle (§ 8 (19) l'avoue, le
résumé non). L'argument DEC est libre : un fichier jouet passe, et la sortie de `feuille` n'imprime ni les R-nnn cités ni l'empreinte de DEC. Corrections possibles : exiger
sur la ligne citée une marque de mot direct (« mot direct de Lazar » ou colonne de source « décision de Lazar » hors relevés), imprimer R-nnn et empreinte de chaque fichier de
DEC dans la feuille, que le lecteur R13 recopie.

## (d) Cas d'inatteignabilité (§ 6.7) : complets et justes ?
Justes pour (i) à (x). **CT6-08 — Incomplets. Gravité : à corriger (texte).** (1) (xi), sous D:3 (1) (et § 9 D:3 option 1) : n'énumère que plafond absent, plafond épuisé,
P-ARR absent ; W21 exige aussi P-V6 « établi », P-L7 et P-B4 sous **toutes** les options (la marque ° ne retire que P-PIL) : la comparaison de D:3 fait paraître (2) plus
étroite que (1), alors qu'elle l'est autant. (2) Un chemin « nommé par P-x » (P-6a-res, P-EP, P-LST, P-PIL) non écrit dans le préenregistrement scellé rend le produit absent à
jamais (R12 interdit de le réécrire) : W16, W17, W19, W48 ou W21 restent fermées ; cas non listé. Même effet si un verdict est déposé hors du motif de chemin, convention non
encore inscrite (§ 8 (6)). (3) Plafond fixé mais **insuffisant** ou nul (§ 8 (10) : « oui » sans devis possible) : (ii) ne parle que d'épuisement. (4) Un produit présent de
classe « autre » : W16, W19, W21 restent fermées jusqu'à version nouvelle (scénario 8) : à nommer dans la liste.

## (e) D:1 (a) conforme à la synthèse ?
Dans la lettre, oui : échéance fixe (24 janvier, 31 janvier 23:59), aucune suspension sans borne (SY l. 72), aucun troisième verdict (SY § 2 pt 2, pt 5), l'arrêt ne vaut rien
(G l. 424), l'heure butoir tranche, « absence de verdict scellé vaut non franchie » (SY l. 38). Réserves : la reprise unique n'est dans **aucune** cellule de SY (ajout de la
table, non marqué comme tel dans le § 9) ; entre l'arrêt et la reprise la porte est en attente d'au plus sept jours, ce que SY pt 5 interdit à un GO sans borne, non à une
fenêtre bornée : à dire ; le texte ne dit pas ce qui arrive si la lecture est ouverte **après** le 24 janvier mais rendue avant le 31 (la coupure du 24 a-t-elle un effet
propre ?) : à préciser. Voir CT6-02 pour le résumé.

## (f) Altérations de ton cru
J'ai fait **14** altérations (dont **6** dans le résumé : porte garantie atteignable, défaut de 48 heures, feuille malgré attente, « ne lit aucun résultat » inversé, confiance
de D:0b 0,7 → 0,9, « contraire à la synthèse » → « conforme »), dans le § 6.5 (GO couvrent le report), le § 6.7, § 9 (confiance de D:1, défaut ajouté à D:3, D:1 (c) « conforme
», D:7 0,55 → 0,85), le titre (« scellée »). **14 détectées sur 14**, mais par le seul filet (empreinte de section) ou l'empreinte du § 9 : **aucune garde ne lie le résumé au
registre** ; une dérive résumé/registre faite en v7, avec les constantes recalculées, ne serait vue que par la contre-lecture. À ajouter : garde « recommandation et confiance
du résumé = registre ».

## (g) Taillage sur l'état (R4)
Diff v5/v6 : aucune cellule « produits », « fournit », « sert », « classe » ne change (vérifié) ; W24 passe de d2 à `[GEL-SY]`, sens resserrant, réserve du chiffre 1 400 USD
déclarée (§ 8 (14)). L11 n'est plus qu'une option non recommandée : le taillage sur le pilote du 29 octobre recule. Les scénarios prennent pour hypothèse les recommandations
(déclaré, non lu par `feuille`). Le sens (ouvre/ferme) des recommandations est au § 7 mais **absent du résumé** ; § 7 range D:5 (c) parmi celles qui « gardent la porte ouverte
» alors qu'elle gèle un « invalide » : à nuancer. À signaler (CT6-10).

## Autres
**CT6-09 — Énoncés de scellement périmés. Gravité : à signaler.** Le titre, la déclaration (« aucun compagnon `.sha256` ») et l'annexe (« refus : table non scellée (T2
compagnon absent) ») sont faux à la remise : les compagnons existent (posés vers 23:33 UTC) et R-521 écrit « scellés à 23:33 UTC » ; le refus réel est « décisions en attente
». Toute retouche étant une version nouvelle (R12), dire à Lazar, dans le message d'envoi, que ces trois énoncés sont périmés, ou publier une v7 de texte (alors ses mots
iraient en v8, le résumé écrit « v7 »).
**CT6-10 — Résumé : sens des recommandations.** Voir (g).

## Conclusion
**Prête après corrections** : logique et script sains (rejeu complet, refus testés), mais le résumé que Lazar lira doit être corrigé (CT6-01 à 05), le contrôle du mot de Lazar
durci avant la v7 (CT6-07), la liste d'inatteignabilité complétée (CT6-08).
