# Le pari apparié borné — conception v10 : fraîcheur par rapport à la course, une affirmation une fiche, plan des tranches scellé, journal tenu par le monde, lectures de la démonstration corrigées (contre-lecture de la v9)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), rédaction commencée après le relevé `date -u` de
01:26:56 UTC le 28 octobre. **Remplace la v9** (`aab37f63…`, gardée, R12) selon la contre-lecture de la v9 et du code
versions 26 et 27 (sous-agent neuf Opus 5.5, `contre-lecture-v9/rapport-contre-lecture-pari-signe-v9.md`, `b73789ca…`,
« à amender en v10, corrections locales » ; code « à corriger » ; K8-1 à K8-5 : K8-3 fermé, K8-1 et K8-2 à moitié, K8-4
**ouvert alors que la v9 l'annonçait codé** — erreur de la v9, dite ; K8-5 à moitié ; dix constats K9-1 à K9-10, tous
acceptés, traitement en § 1). Delta de la v9. Exploratoire (R-546) ; décisif dès qu'il sert G1. Code : v7, **version 28**
(`../orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v28.md`). **Cette v10 n'est pas encore contre-lue.**

## Verdict (ce que change la v10)

1. **La fraîcheur des unités est définie par rapport à toute la course, pas à la fiche (K9-1, touche la garantie).** Une
   unité n'est lue qu'**à la génération de sa première lecture par la course**, par quelque fiche que ce soit : une tranche
   se partage entre fiches **dans sa génération**, jamais ensuite. Mesuré par la contre-lecture, toutes gardes de la version
   27 passées : copie renommée d'une fiche, tranche lue une génération d'avance par la copie, puis déclaration « fiche non
   lancée » vraie → **0,087 puis 0,626** d'au moins une fausse promotion sur 10 puis 30 générations (contre 0,025 et 0,024
   en course honnête). Et : **toute décision de ne pas lire une partie** (déclaration « sans partie », fiche non lancée,
   abandon « avant partie ») **est prise avant toute issue de la génération, d'aucune fiche** — la preuve exige que chaque
   partie soit une e-valeur conditionnelle au passé de toute la course, et que la décision de ne pas lire soit prévisible.
   Code : registre `premiere_lecture` unité → génération dans `Course`, refus de toute unité lue à une génération antérieure.
2. **Une affirmation, une fiche — par la clé canonique (K9-3).** La clé de l'héritage ne contient plus de nom libre : les
   contrastes y sont dans leur **forme canonique** (cellules triées, coefficients et constante) ; renommer un contraste ne
   fait pas une autre affirmation ; deux contrastes de même forme dans une fiche sont refusés ; la mémoire (`Lignees`) refuse
   une seconde fiche pour la même clé **et** une seconde clé pour une même fiche (K9-2) ; la course reçoit la clé de chaque
   fiche à l'entrée et refuse une partie d'une autre clé (K9-2 : une fiche recevait une partie de développement, puis
   d'épreuve, puis à τ changé, toutes acceptées). **Dit (D-S25 bis (5), K9-3)** : la garantie de D-S25 bis est un taux **par
   fiche promue** ; le rembourrage d'une course par des vraies faciles abaisse la barre e-BH pour les fiches nulles (mesuré :
   au moins une nulle promue dans 0,01 / 0,10 / 0,735 / 1,0 des courses pour 6 / 30 / 200 / 1 000 vraies faciles par
   génération, le taux **par fiche** restant ≤ 0,0022) ; **ce qui sort du pôle se lit par e-Bonferroni** (D-S25 bis (6)),
   seule lecture insensible au rembourrage ; la mémoire qui refuse les redécouvertes est ce qui empêche les copies.
3. **Le plan des tranches est scellé avec l'engagement ; l'ordre d'une tranche est dérivé de l'empreinte de l'engagement et
   de la génération (K9-5).** Plus d'étiquette libre : essayer 100 ordres sous le nul faisait passer le franchissement du
   seuil de 0,03 à 0,535. Le plan (unités par génération) est dérivé de la banque (strates, identifiants), jamais des scores,
   et entre dans la clé ; `evaluer(monde, engagement, generation=g)` lit la tranche du plan dans l'ordre dérivé ; **une seule
   évaluation par fiche et par génération** (refusée sinon par le journal).
4. **Le journal des parties est tenu par celui qui calcule, pas par celui qu'il contrôle (K9-6).** `evaluer` journalise
   lui-même chaque partie (fiche, génération, empreinte des unités, clé) ; la course reçoit le journal et **refuse à la
   lecture** une déclaration « sans partie » contredite, et à l'ajout une partie absente du journal, d'une autre empreinte
   d'unités, ou une seconde évaluation. Une déclaration « sans partie » pour une fiche gelée, arrêtée, promue ou qui a sa
   partie est refusée (K9-10 c).
5. **La version de l'e-processus est dans la clé — codée cette fois (K8-4, K9-4)** : champ `e_processus` (règle de
   combinaison sur Λ, règle d'arrêt, module, version 28) ; essai « règle changée ⇒ clé changée ». La v9 disait « version
   26 » au verdict et « version 27 » au § 3 : les deux étaient faux ; **c'est la version 28**.
6. **Identifiants d'unités stables (K9-2)** : (identité de la banque, partie, unité), l'identité étant déclarée par la
   banque (`identite`) et indépendante de sa version — une banque grandie d'une unité garde ses unités physiques (la
   version 27 les rendait toutes « fraîches » : 40 unités relues acceptées) ; l'empreinte de la banque reste au manifeste.
7. **Lectures de la démonstration corrigées (K9-7, K9-8, K9-10 e).** (a) « Signe connu par construction » était **faux
   conditionnellement aux seuils scellés** — là où la garantie porte : deux cellules de même loi ont des seuils scellés
   différents (jumeaux : 4,1 points de rappel d'écart en moyenne, jusqu'à 14) ; la vérité de L1 est désormais l'**espérance
   conditionnelle aux seuils scellés** (calculée analytiquement dans la banque synthétique) ; le témoin « faux nul » est un
   **contrôle 12** (« calibrage insuffisant » s'il est promu), pas une violation ; en courses répétées, l'ancienne L1 se
   lisait « rompue » dans 13,5 % et 34 % des cas sans aucune fausse promotion au sens conditionnel. (b) « G1 promue en
   génération 3 » était une promotion **par la lecture e-BH de la course du pôle**, pas la lecture de G1 (une fois, hors de la
   suite, N-050) : la fiche s'appelle « forme-G1 », sa **sortie par e-Bonferroni** est rapportée à côté (sous cette règle elle
   ne sortait que dans 16 % des courses), les richesses par comparateur sont **descriptives** ; « comparateur le plus
   faible » retiré (bruit : 0,1368 contre 0,1367). (c) Les « forces » des témoins sont des **décalages de loi** (0,5 ≈ 14
   points de rappel au seuil τ = 0,05), pas des points de rappel.
8. **Garde par comparateur (K9-9, K9-10 a)** : l'intersection-union de G1 porte **une garde par comparateur** (le minimum
   sur toutes) ; le § 6 cite une table à alertes indépendantes alors que le blanc contre la cascade **sur les mêmes sondes**
   est concordant : le devis de la couche 2 se chiffre en (écart, **discordance**, taille du calibrage C), mesurés par la
   lecture pilote, avec le contrôle 12 à la taille de calibrage de G1 ; les composantes rapportées de G1 sont descriptives.

## 1. Corrections, section par section de la v9

### D-S25 bis (5) (K9-1, K9-3, K9-5)
Remplacer « toute intersection avec les unités déjà lues par la fiche est refusée » par : « toute unité **déjà lue par la
course à une génération antérieure** est refusée à toute fiche (une tranche se partage dans sa génération) ; la fiche ne
relit jamais une unité ; **le plan des tranches** (unités par génération) est scellé avec l'engagement et dérivé de la
banque, jamais des scores ; l'ordre d'une tranche dérive de l'empreinte de l'engagement et de la génération ; une seule
évaluation par fiche et par génération ; **toute décision de ne pas lire** (déclaration, fiche non lancée, abandon « avant
partie ») **est prise avant toute issue de la génération, d'aucune fiche** ». Ajouter : « la garantie est un taux par
**fiche** promue ; une affirmation (clé canonique) n'est portée que par une fiche ; ce qui sort du pôle se lit par
e-Bonferroni (D-S25 bis (6)) ».

### D-S25 bis (2) (K9-6, K9-10 c)
« Le monde journalise toute partie calculée » devient « **la fonction qui calcule la partie journalise** (fiche, génération,
empreinte des unités, clé) ; la course **reçoit le journal** et refuse : une déclaration contredite, une partie absente du
journal ou d'une autre empreinte, une seconde évaluation, une déclaration pour une fiche gelée, arrêtée, promue ou qui a sa
partie ».

### D-S18 (K8-4, K9-4, K9-3)
La clé contient : contrastes en **forme canonique** (sans nom), comparateurs par forme, pondération et m_max, partie, Λ,
**version de l'e-processus**, τ, strate, seuils, population = **identité** de la banque, gardes (liste triée), **plan des
tranches**. Le budget d'entrée et les noms restent hors de la clé (dans l'engagement).

### D-S8 et § 6 (K9-9, K9-10 a)
Ajouter : « une garde par comparateur ; les composantes de l'intersection-union rapportées sont descriptives (la course ne
garde que le minimum) ». § 6 : « la table du pari v2 § 6 suppose des alertes indépendantes ; pour blanc contre blanc sur les
mêmes sondes, la variance par unité suit (discordance − écart²)/m ; le devis se chiffre en (écart, discordance, C) par la
lecture pilote ; le bruit de seuil des jumeaux (≈ 4 points ici) est du même ordre que l'écart attendu : contrôle 12 à la
taille de calibrage de G1 ».

### Démonstration (K9-7, K9-8, K9-10 d, e, f)
L1 sur l'espérance conditionnelle ; contrôle 12 ; « forme-G1 » et e-Bonferroni ; décalages de loi ; essai `test_nul_repete`
corrigé (Bonferroni ⊂ e-BH) ; le nul × 200 ne porte que sur le nul complet : le cas mêlé (vraies et nulles) est celui où e-BH
est le moins prudent — rapporté par la contre-lecture (0 fausse promotion conditionnelle sur 250 courses mêlées, taux de
fausses découvertes 0,011 et 0,021 au sens de la population).

## 2. Décisions

| décision | état |
|---|---|
| D-S25 bis (5) (fraîcheur par rapport à la course ; décision de non-lecture prévisible ; une affirmation, une fiche ; plan scellé) | proposée (0,85 — la contre-lecture donnait 0,6 à la v9 « tant que K9-1 n'est pas écrit ») |
| D-S25 bis (2) (journal tenu par qui calcule, course qui confronte) | proposée (0,85) |
| D-S18 (clé canonique, e-processus, plan, identité) | proposée (0,85) ; **codée** en version 28 |
| D-S8 (garde par comparateur ; composantes descriptives) | précision de la décision de Lazar (nœud 1 = b), à confirmer d'un mot |
| nœud 2, D-S29, D-S30 | inchangés (lus, non confirmés) |

## 3. Code (v7, version 28)

`pole/pari_apparie.py` : `E_PROCESSUS` ; `evaluer` à plusieurs gardes ; `Course(alpha, journal=…)`, `premiere_lecture`,
`entrer(..., cles=…)`, `ajouter_trajectoire(..., empreinte_cle=…, empreinte_unites=…)`, `lire` qui confronte au journal et
refuse les déclarations indues. `pole/engagement_apparie.py` : `canonique`, `construire(..., plan_tranches=…)` (gardes en
liste, clé canonique, `e_processus`, population = identité), `evaluer(monde, engagement, generation=…, fiche=…, journal=…)`,
`Lignees` (une fiche, une clé ; journal sans doublon). `pole/monde_banque_scores.py` : `identite`. Démonstration et essais
refaits (cinq artefacts : relecture, tranche antérieure par une autre fiche, « sans partie » mensonger, relance sous un autre
nom, partie d'une autre clé). **Essais : voir le LISEZMOI v28.**

## 4. Ce que la v10 laisse ouvert (dit)

Sa contre-lecture ; K7-6, K7-7 (alignement par unité des gardes et des contrastes ; ordre sans les scores d'épreuve : le plan
scellé y répond en partie) ; la mesure de (écart, discordance, C) pour le devis de G1 (b) ; le lien au cycle ; la
« faisabilité » n'est pas l'objet de ce document.
