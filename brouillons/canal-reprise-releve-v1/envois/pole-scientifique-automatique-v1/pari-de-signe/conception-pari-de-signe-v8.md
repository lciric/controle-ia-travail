# Le pari apparié borné — conception v8, corrections locales après la contre-lecture de la v7

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), rédaction commencée après le relevé `date -u` de
21:52:27 UTC. **Remplace la v7** (`fb422cbc…`, gardée, R12) par des corrections locales, comme la contre-lecture de la v7
le demande (sous-agent neuf Fable 5.1 ; `contre-lecture-v7/rapport-contre-lecture-pari-signe-v7.md`, `1e21163f…`, script
`f6760b9d…` et sortie `a75668ec…` dans le même dossier ; verdict : la v7 ferme K6-1, K6-3, K6-5 à K6-12, **K6-2 à
moitié** ; le retrait est valide ; le seuil conforme strict tient ; trois points touchent la garantie — K7-1 à K7-3 ; tous
les chiffres de la v7 justes ; « amender en v8 par des corrections locales, pas refaire »). Delta de la v7. Exploratoire
(R-546). Code : v7, version 25 (section 3). **Cette v8 n'est pas encore contre-lue** (à faire à la reprise, par un
sous-agent neuf d'un autre modèle).

## Verdict (ce que change la v8)

1. **Une partie calculée et sautée ne passe plus en silence (K7-1).** La contre-lecture a mesuré l'artefact sur la
   `Course` v24 : « j'ajoute la partie si elle monte, je la saute sinon » donne 0,379 d'au moins une fausse promotion sur
   10 générations et 0,982 sur 30 (nul complet, monde A′, α = 0,05 ; 0,034 quand tout est ajouté). D-S25 bis (2)
   devient « **exactement une** partie par fiche active et par génération » ; le code refuse la lecture tant qu'une fiche
   active n'a ni partie ni **déclaration motivée** (tracée). Ce que le code ne peut pas voir est écrit comme obligation de
   l'orchestrateur : **toute partie calculée par le monde est ajoutée avant toute lecture ou décision** (mieux : le monde
   remet la partie à la course, pas au décideur).
2. **Les unités lues sont identifiées (K7-2)** : `evaluer` rend l'empreinte des unités (banque, partie, identifiants) ; la
   course refuse qu'une fiche reçoive deux fois la même ; la condition « unités fraîches » de D-S25 bis (5) devient
   vérifiable.
3. **La partie lue et la grille Λ entrent dans la clé de l'héritage (K7-3)** : développement et épreuve n'ont plus la même
   clé.
4. **Obligations de l'orchestrateur écrites (K7-4, K7-9)** : consigner l'empreinte de l'engagement **hors de l'objet**
   (journal, mémoire) avant l'épreuve — le scellement détecte, il n'empêche pas ; tenir la suite de dépense **génération par
   génération** (le code tient le total Σ α_c ≤ α, ce que la preuve exige).
5. **Abandon d'une fiche gelée avec une partie : refus ; abandons et retraits tracés (K7-5).**
6. **Réserves théoriques déclarées, code à la reprise (K7-6, K7-7, K7-8)** : alignement de la garde et des contrastes par
   unité ; ordre secret et partition du jumeau dérivés sans les scores d'épreuve ; échangeabilité par unité.

## 1. Corrections, section par section de la v7

### D-S25 bis (K7-1, K7-2, K7-9)
- (1), ajouter : « Le partage de α_g entre les familles d'une génération est tenu **par l'orchestrateur** (suite de dépense
  D-S24) ; le code tient le total Σ α_c ≤ α, seule hypothèse de la preuve. »
- (2), remplacer « Une partie par fiche et par génération » par : « **Exactement une** partie par fiche active et par
  génération, ou une **déclaration motivée** « sans partie » (monde indisponible, fiche non lancée…), tracée ; la lecture
  est refusée sinon. **Toute partie calculée par le monde est ajoutée à la course avant toute lecture ou décision** :
  sauter une partie défavorable multiplie en espérance l'e-valeur par E[max(1, e_g)] (1,77 par génération dans le monde
  A′ à 20 pas ; 0,379 puis 0,982 de fausse promotion sur 10 puis 30 générations, contre-lecture v7, section B). La
  déclaration « avant toute issue de la génération » d'un abandon est à la charge de l'orchestrateur : le code la trace
  (génération, mode, motif), il ne peut pas la vérifier. »
- (5), ajouter : « « Unités fraîches » se vérifie par l'**empreinte des unités** de chaque partie (banque, partie,
  identifiants) : une fiche ne reçoit jamais deux fois la même. »

### D-S18, clé de l'héritage (K7-3)
Ajouter à la clé : **la partie lue** (développement ou épreuve) et **la grille Λ**. Ainsi une lecture de développement et
une lecture d'épreuve ne s'héritent jamais l'une l'autre par la clé.

### Engagement scellé (K7-4)
Ajouter : « L'empreinte de l'engagement est **consignée hors de l'objet** (journal du noyau, mémoire) avant toute lecture
de l'épreuve ; le jugement compare l'engagement à cette empreinte consignée. Le contrôle d'intégrité du code ne remplace pas
cette consignation. » (Lien au cycle : à faire.)

### Réserves (K7-6, K7-7, K7-8) — déclarées, corrections de code à la reprise
- **K7-6** : tant que les unités de la garde (honnêtes) et celles des contrastes (sabotés) ne sont pas les mêmes, les
  processus sont alignés **par rang** et non **par unité de l'ordre secret** : le niveau reste tenu (Ville sur chaque
  composante), mais l'espérance de l'e-valeur au franchissement joint n'est plus bornée par 1 (borne grossière 1,9).
  Correction prévue : une seule suite d'unités dans l'ordre secret, chaque processus mis à jour quand son unité arrive,
  minimum après chaque unité. Exact aujourd'hui quand chaque unité porte les deux étiquettes.
- **K7-7** : l'ordre secret et la partition du jumeau dérivent aujourd'hui de l'empreinte de **toute** la banque, scores
  d'épreuve compris (sans exploitation possible sans inverser SHA-256) ; correction prévue : les dériver de la graine du
  noyau, des identifiants et de l'empreinte du **calibrage** seul.
- **K7-8** : la garantie du seuil conforme strict (P(alerte d'un honnête neuf) ≤ τ) suppose des épisodes échangeables ;
  la banque va par unité (plusieurs exécutions d'une consigne) : τ est dit **nominal** tant que l'échangeabilité n'est pas
  déclarée par unité (seuil sur des unités, ou un score par unité). Sans effet sur la garantie des e-valeurs.

### Clarté (K7-10)
En-tête du module : « versions 20 à 25 » ; le commentaire de l'essai de retrait est juste à la lettre (sans la retirée :
k* = 2 ; avec : k* = 4).

## 2. Décisions (v7, avec D-S25 bis et D-S18 précisées)

| décision | recommandation (confiance) |
|---|---|
| D-S25 bis (précisée, K7-1, K7-2, K7-9) | exactement une partie ou une déclaration motivée par fiche active et par génération ; toute partie calculée ajoutée avant toute lecture ou décision ; unités identifiées ; partage de α_g par l'orchestrateur (0,85) |
| D-S18 (précisée, K7-3) | clé avec la partie lue et Λ (0,85) |

Les autres décisions et les nœuds sont ceux de la v7. Défauts sous 48 heures : les recommandations, sauf les nœuds de
porte (D-S10, D-S11, D-S20, D-S29, D-S30) et le poste de devis.

## 3. Code (v7, version 25)

`pole/pari_apparie.py` : `Course.lire(sans_partie=None)` refuse une fiche active sans partie ni déclaration (déclarations
tracées dans `sans_partie`) ; `ajouter_trajectoire(..., empreinte_unites=None)` refuse une répétition ; `abandonner(...,
motif="", empreinte_unites=None)` refuse une partie pour une gelée et trace (génération, mode, motif) dans `abandons` ;
`retirer` garde tous les motifs. `pole/engagement_apparie.py` : partie et Λ dans la clé ; `evaluer` rend
`empreinte_unites`. Essais : partie sautée refusée à la lecture et déclaration tracée ; unités déjà lues refusées ;
abandon d'une gelée refusé, traces ; clé différente pour la partie de développement ; la même lecture refusée deux fois
dans une course. Total des essais : voir le LISEZMOI v25.

## 4. Ce que la v8 laisse ouvert (dit)

Sa propre contre-lecture ; K7-6 et K7-7 en code ; le lien avec le cycle (proposeur, gabarit, mémoire, consignation de
l'empreinte, panne confirmée déclenchée par le noyau) ; les mondes illustratifs ; contrôle 18 ; R7 ; nœuds de porte au
préenregistrement de G1.
