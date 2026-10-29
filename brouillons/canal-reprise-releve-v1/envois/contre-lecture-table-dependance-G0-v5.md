# Contre-lecture (R2) de la table de dépendance « critères de G0 → travaux », v5

**Déclaration.** Je n'ai écrit ni la v5 ni son script, ni aucune version ou contre-lecture antérieure de cette lignée. Modèle : **Sonnet 5.5** (sous-agent neuf) :
même famille que les auteurs de la v3 et de la v4 et que le contre-lecteur de la v4, différent de l'auteur de la v5 (Opus 5.5) ; des erreurs corrélées avec la lignée
restent possibles. `date -u` : début 2026-10-29 22:57:49 UTC ; relevé avant l'écriture 23:05:00 UTC. Interdits tenus : rien lu sous `donnees/`, ni
`prereg/P3-consignes-v1.md`, ni `diag/*/traces` ; aucune branche, aucune commande git ; aucune dépense ; aucun fichier existant modifié ; rien scellé (ce rapport n'a
pas de compagnon `.sha256`) ; les dossiers `cl-table-v4*` n'ont pas été ouverts. Travail dans `…/scratchpad/cl-table-v5/`. Un fichier `.pyc` créé par mon premier
import du script dans `envois/__pycache__/` a été supprimé (le `.pyc` de la v4 y était déjà).
**Empreintes** (recalculées, compagnon = recalcul) : table v5 `cd05b2aecea05ec0395ecfba180cb4c08ecebcc10a26377a416653a6dc38f751` OK ; script
`e4d79bfbc71f0680ec9ad3003a4457cd2be274152e36e1c937936f370282bcbf` OK ; v4 `8226dd55…` OK ; grille `320af9b0…`, brief `9261932a…`, synthèse `527f5853…`, R-765/R-776
`f6e454f3…`, GO du jour `9c1c7bc2…`, `CLAUDE.md` `a2aabda8…` conformes à l'en-tête. `registres/decisions.md` a grandi depuis l'auteur (`ff34aaf4…`, jusqu'à R-518) :
mode `sources` « a bougé » (statut vivant, sans arrêt), `verifier` reste OK. Mes pièces : `alterations_v5.py` `4956c23b…`, `…_v5b.py` `aa23461c…`, `…_v5c.py`
`77524a87…`.
**Rejeu** : `verifier … SY` : OK 62 lignes dérivées, 51 lignes de travaux, 20 produits, clause identique à SY § 5 (code 0). `essais` avec dépôt et SY : 48
altérations sur 48, 15 refus de `feuille` sur 15, 5 refus du constat sur 5, **73 gardes exercées, 0 manquante** (code 0). `tester` sur le dépôt : présents P-T04,
P-T03, P-NM ; 17 absents. Tout reproduit.

## (a) CT4-01 à CT4-12 : traités comme déclaré ?
CT4-01 oui (§ 0 point par point ; 168 mots ; citation de R-765 entière, présente dans `R-765-R-776.md` ; les deux clauses gelées). CT4-02 **partiel** (CT5-02).
CT4-03 oui sur la forme (défaut inconditionnel), mais voir CT5-01 et CT5-04. CT4-04 oui sur la borne et la « levée », **partiel** sur les appuis (CT5-03). CT4-05 oui
(P-EA à trois producteurs, P-EAV neuf, W28/W29 sur P-EAV, listé au § 7 ; diff v4/v5 : seules W04, W05, W06, W21, W22, W24, W28, W29, W52 et P-EA, P-EAV, P-T04
changent, comme déclaré). CT4-06 oui (§ 9 (5), défaut = lettre de R-765). CT4-07 oui avec réserve (CT5-06). CT4-08 **partiel** (CT5-07). CT4-09 oui (§ 8 (16)).
CT4-10 oui (§ 7 « assouplis », § 8 (17), G l.234 vérifiée). CT4-11 oui : (a) clause, 168 mots, citation, dates dans l'ordre, motifs, empreinte du script gelés ; E28
à E38 rejouées ; (b) comptes de l'annexe (15 refus, 5 refus, 73 gardes) égaux à la sortie ; (c) T2 appelle `controle_ia.scellement.verifier` et exige la concordance
; (d) déclaration de tête exacte. CT4-12 oui sur la table `S:` (17 sources, `sources` code 0), **partiel** sur la durabilité (CT5-05).

## Constats
**CT5-01 — Défauts applicables sans le mot de Lazar sur des points qui touchent la porte. Gravité : à corriger (R-518).** R-518 tranche : pour la clause de repli, la
table de dépendance, la grille et D-G0, **aucun défaut ne s'applique**. La v5 (écrite avant R-518) garde la question ouverte (§ 9, ouverture : « si tu les tiens pour
des nœuds de porte… ») et ne vise que (1) à (3). Points où un « défaut » reste appliqué ou affiché : (i) § 9 (1) « Défaut sous 48 heures : (a) » ; (ii) § 9 (2) «
(b), sans condition » ; (iii) § 9 (3) « (3) » **et son application dans le code** (L11, `requis`, `bas` : le script calcule la bascule °) et dans les scénarios 9-10
; (iv) § 9 (4) D-G0-8 « (a) » **hors de l'avertissement** (R-518 nomme D-G0) et T3/T5 supposés « exiger » (§ 8 (9)) ; (v) § 9 (5) « (a) » **hors de l'avertissement**
(il touche le gel, le constat et le droit de devis, donc la lecture de la porte) ; (vi) § 0 (b) « [choix de Lazar, défaut : absent] » et la clause « appliquée » («
La table applique “absent” ») ; (vii) L8 « défaut = cette lettre », § 6.6 « défaut proposé », § 1 (CT4-02/03) « défaut inconditionnel » ; (viii) « le délai de 48
heures, si tu le retiens, court depuis la remise de la v5 ». À corriger : remplacer « défaut » par « recommandation » partout, étendre l'avertissement à (1) à (5),
citer R-518 et dire que la table ne se scelle que sur le mot de Lazar. Convention sans source touchant le constat : l'heure de `C_31` (§ 6.2) ; elle est dite
modifiable, rien d'autre à reprendre.
**CT5-02 — « La porte reste atteignable dans les deux cas » : exagéré. Gravité : à corriger (texte).** § 9 (3) (option 3) et § 1 (CT4-02) l'affirment. Rejeu de
`feuille` (A = 2,3,4,6,7,8, produits absents de `tester`) : sans plafond (`plaf=non`), 0 droit de devis ; W13 s'ouvre mais W14 (run de T0.6) n'a pas de devis ; P-V6‡
ne vient jamais ; W16, W19, W21 restent fermées. L11 ne retire que P-PIL de W21 : elle suffit seulement si P-V6, P-L7, P-B4 sont déjà présents (scénarios 9-10 : A =
6 seul). Autres cas où la porte n'est pas atteignable, par construction et sans que § 9 (3) le dise : plafond fixé mais épuisé avant le pilote (§ 6.5 (ii), « ne
change pas la clé ») ; critère C ou V sous le défaut (5)(a) ; G' non vide (§ 8 (2), voulu) ; table non scellée à V1 (CT5-04) ; V1 interrompu (§ 6.3, nœud). Corriger
l'avantage : « atteignable pour le critère 6 seul, quand 2, 3, 4 sont déjà établis » et lister les autres cas, ou le dire en tête du § 9.
**CT5-03 — D-TD-2 (a) : sans latitude pour l'essentiel, mais quatre points d'appui inexacts ou omis. Gravité : à corriger (texte).** La « levée de la cause » est
testable élément par élément (empreinte de la grille, `verifier-arbre`, lecteur neuf, fichier interdit) ; l'échéance, la reprise unique et l'issue « non franchie »
sont fixées : pas de latitude réelle. Mais : (1) (a) est un **état suspendu**, que SY § 2 pt 5 (3/3, « aucun état suspendu ») interdit ; la table cite ce point comme
appui du *bornage* sans dire que même borné il y déroge ; (2) la borne du report est le 31 janvier 2027 (R-452 « borne fixée », R-750, R-765 « au plus tard ») : (a)
ouvre une fenêtre de verdict jusqu'au 7 février ; seule la dérogation à G l.424 est dite ; (3) l'issue « lecture non rendue » à l'échéance recoupe G l.421-422 (heure
dépassée sans lecture : lue au premier moment possible, sans borne) : deux règles pour un même cas ; dire laquelle prime ; (4) « SY § 2 pt 2, modèles B et C, 3 sur 3
» : le 3/3 de pt 2 porte sur la première moitié ; « absence de verdict scellé vaut non franchie » cite T2-B l.193, cellule de l'équipe rouge qui « ne propose rien »
(SY l.21), et T3-C l.100.
**CT5-04 — Date de scellement : inconditionnelle, mais deux trous. Gravité : à signaler.** Le défaut (b) est bien sans condition, avec une borne haute fixe (« plus
tôt si prêts » ne joue que sur la date). (1) « Scellé avant V1 » n'est garanti que si V1 ne précède pas : la grille interdit toute lecture avant son propre
scellement (G l.96-98) et permet une lecture anticipée (G l.89-94), mais aucune règle équivalente ne lie V1 au scellement de la table ; à ajouter : « aucune lecture
V1 avant le scellement de la table et du script ». (2) Si le mot de Lazar manque au 15 novembre (R-518 : aucun défaut), rien n'est dit de l'effet sur V1 et sur la
clause (c) (« tâches de la table scellée » : sans table scellée, aucune ne continue).
**CT5-05 — Sources non durables et chaîne R13 incomplète. Gravité : à corriger avant scellement.** S:G, S:SY, S:R765, S:GO sont des chemins du bloc-notes de session
(`/tmp/claude-0/…`) : `sources`, `verifier … SY` et l'argument DEC échouent dans une autre session. R-765 n'existe que dans la copie de `main` ; DEC doit donc être
deux fichiers. La table v1 est une entrée de `verifier` et n'est pas dans le tableau `S:`. § 6.1 ne donne aucune ligne de commande (ordre des arguments, fichiers à
remettre au lecteur). Les copies (grille, synthèse, R-765/R-776, GO, table v1) doivent être versées au dépôt avec empreinte, et la chaîne écrite en commandes
complètes. Titre : « BROUILLON (non scellé) » alors que R-517 écrit « scellés à 22:57 » et qu'un compagnon existe : dire « empreinte compagnon posée (R6) ;
scellement de G0 à venir ».
**CT5-06 — Fermeture de W24 (question b) : tient, avec réserve. Gravité : remarque.** Chaîne relue : PC l.99 (couche 2 : « banque avec sabotage… ; première lecture
de H2 ») ✓ ; B l.218 (H2 lu par T1.2) ✓ ; SY l.84 (« banque de G1 », 1 400 USD) ✓ ; SY l.138 (critère 2, gelé : « banque de G1 ») ✓ ; SY l.140 (critère 4, gelé : «
banque ») ✓ ; DP l.143 (1 400 USD ↔ ≈ 18 650 épisodes de banque) ✓. La fermeture tient comme **gelé de SY** et par la clause (c) (« sans expérience décisive de G1 »)
; elle ne tient pas strictement comme d2 : la fabrication n'est pas la lecture de H2 (PC les met dans la même couche), et l'identité « banque de G1 » = « banque de
la couche 2 » repose sur le seul chiffre 1 400 USD, que SY l.174 donne pour rapporté et non vérifié. L'extension de d2 (« grandeur que l'expérience de G1 lit ») n'a
qu'une ligne qui en dépend, W24 : à dire. Sens resserrant, réserve déjà au § 8 (14). Pas de bloquant.
**CT5-07 — Borne des arêtes † (CT4-08) non appliquée à elle-même. Gravité : remarque.** Le § 2 écrit qu'une arête † vers P-T04 « ne se pose que » sur une ligne dont
la source dit qu'un modèle tourne par notre harnais ; § 8 (15) garde W14, W19, W33, W47 dont la source ne le dit pas (W33 : N-028 « sans nouvelle génération
d'épisodes »). Réécrire la règle en « se pose sauf… » ou retirer ; sens resserrant, aucun effet tant que P-T04 est présent.

## (e) Le script détecte-t-il des altérations nouvelles ?
J'ai fait 32 altérations propres effectives (hors les 48 de l'auteur ; une, sans effet, écartée) : **9 détectées, 23 non**. Détectées : « sert » de W21 (k:7), I→H de
W44 (par aud:neuves-ouvertes, par hasard), cellule k:2 modifiée, aud:L29 modifié, date 15→16 novembre, défaut (1) changé avec retrait de « 7 février » (par la liste
des dates seulement), jeton d2→préalable de W24 (aud:sources), clause appliquée (c), motif de chemin de P-C. **Non détectées** (rejouables avec mes trois scripts) :
en-tête (modèle déclaré) ; puce (c) du § 0 ; producteur de P-P4 changé de façon cohérente dans les deux tables ; heure du second verdict 23:59→12:00 (les dates sont
gelées, pas les heures) ; empreinte de S:B en `verifier` (le mode `sources` la détecte, hors de la chaîne 6.1) ; colonne « travail » de W52 et de W23 (« neuvième »→«
huitième », « seize »→« soixante ») ; prose du § 3 (« dernière version scellée »→« première ») ; montant d'un GO (11,8→118 USD) ; texte de L3, L8, L9 (le code
gouverne, le texte peut diverger) ; statut figé→vivant de S:B ; lignes relues de S:B ; **toutes les lettres de défaut du § 9** ((1) (a)→(b), (3) (3)→(1), (5)
(a)→(c), « sans condition »→« sous condition ») ; § 9 intro retirée ; § 6.4 ; § 6.5 (ii). Lecture : le script garde la structure, les clauses, les dates, les motifs
et les tables dérivées, pas les décisions ni la prose. Pour (c) cela compte : le défaut (1) n'est protégé que par la date « 7 février » ; les lettres des défauts, «
inconditionnel » et la lettre (3) ne le sont pas. À ajouter : empreinte du § 9 et des paragraphes L1-L11 (ou sentinelles par phrase), empreinte du tableau des GO,
heures dans le contrôle des dates. Gravité : à signaler (le scellement du fichier gèle ensuite tout ; le trou joue avant le scellement et à la v6 qui suivra les mots
de Lazar).

## (f) Taillage sur l'état (R4)
Règles façonnées sur le 29 octobre : la marque ° (seul cas P-PIL, pilote du 29 octobre) et L11 ; W52 (neuve, R-511, R-513) ; l'extension de d2 pour W24. Tous trois
déclarés (A6, § 7, § 8 (14)). Contrefactuel recompté par le script : aud:L29 = 16 lignes ; retrait : 3 scénarios sur 50 diffèrent, 1 ligne (W21), 0 classe ; la règle
est locale. Diff v4/v5 : aucun assouplissement ou resserrement non listé (W12, P-EAV, L11 sont au § 7). Asymétrie à nommer : sur silence, deux défauts penchent du
côté qui garde la porte ouverte ((b) « absent » ; L11 : ne pas fixer de plafond relâche W21), alors que (5)(a) et D-TD-2 (a) ferment ; L11 « récompense » l'absence
de plafond (SY l.82, attaque « inaction récompensée »). La décision revient à Lazar (CT5-01) ; la table devrait écrire cette asymétrie. Les 10 lignes I du 29 octobre
restent ouvertes par défaut ; l'aveugle de la v4 les confirme (62 % de concordance, 84 % hors †) ; je n'ai pas refait de classement.

## (g) Applicable mécaniquement par le lecteur R13 ?
Oui une fois les décisions prises et CT5-05 corrigé : `tester`, `feuille` (qui rappelle `verifier`), `constat` sont déterministes, leurs refus sont testés, la sortie
se copie. Restes : (1) les chemins « nommé par P-x » (P-6a-res, P-EP, P-LST, P-PIL) sont passés à `tester` à la main (`P-PIL=chemin`) à partir de la ligne `produit
P-y : chemin` du préenregistrement scellé : une lecture d'un texte, non mécanique ; (2) T3 et T5 supposent D-G0-8 (a) et des préenregistrements de T0.6 à T0.8 qui
n'existent pas encore ; (3) « fixe le plafond » (oui/non) ne prévoit ni plafond séquencé par critère (SY choix n° 5) ni montant nul ; (4) « engage une dépense
facturée » (définition d'une étape) laisse un jugement à la session, la liste fermée limite le risque ; (5) « dans le même commit » et la coupure M-0.6 ne sont pas
testés (dit au § 8 (19)).

## Conclusion
**Scellable après corrections de texte (CT5-01 à CT5-05, puis CT5-06 et 07), et seulement après les décisions de Lazar : aucun défaut ne s'applique à la porte
(R-518) ; aucun bloquant de fond ; les douze constats de la v4 sont traités, quatre en partie.**
