# Nœuds ouverts au 18 novembre 2026, pour Lazar — version 1

Rassemblés par la session mère `session_01XJ6Mgr8BN6UanALsQatc5E` entre 01:19Z et 02:00Z, pour être lus d'un trait.
Chaque nœud suit le format du `CLAUDE.md` : décision en une phrase ; enjeu ; options avec avantage et inconvénient ;
recommandation et confiance ; défaut sous 48 heures quand il y en a un. **Rien de ce qui suit n'est engagé.**

Contexte commun : crédit du loueur de cartes à **zéro**, solde **−2,19 USD** ; mot de Lazar à 01:26Z, verbatim
« plus de credits vast avant 9h du matin ». L'autonomie renforcée de la mère a expiré. Aucune dépense engagée depuis
la reprise.

---

## A. Urgent — avant 9 heures, parce qu'une fenêtre se ferme

### A1. Dans quel ordre dépenser le crédit quand il revient

**Enjeu.** Quatre travaux attendent le même crédit, et l'un d'eux a une fenêtre qui se ferme aujourd'hui.

| travail | coût | contrainte de temps |
|---|---|---|
| reprise du témoin de Bailey (récupérer les journaux de son instance arrêtée) | ≈ 0,5 USD, ≈ 20 min | **la relance perd son objet après ≈ 13:00Z** |
| relance de la confirmation du témoin de Bailey | ≈ 34 USD (ligne GO-2026-11-17-07) | même fenêtre |
| course de l'étape B bis de l'épreuve des sondes | exige **20 USD de crédit** avant toute création (R-2975) | **verdict scellé dû le dimanche 22 novembre** |
| jeu de l'idée du poids du nul, relancé | ≈ 1 à 3,5 USD (ligne GO-2026-11-16-13) | aucune |

**Options.** (a) Reprise du témoin d'abord, puis l'étape B bis, le reste après. Avantage : la reprise est quasi gratuite,
rapide, et ses journaux sont périssables ; l'échéance du 22 est ensuite servie. Inconvénient : la relance du témoin
reste suspendue à A2. (b) L'étape B bis d'abord. Avantage : l'échéance dure du 22 est la seule déjà inscrite au
programme. Inconvénient : fait probablement perdre la fenêtre du témoin. (c) Tout, dans l'ordre d'arrivée du crédit.
Inconvénient : rien n'est arbitré, le risque se réalise au hasard.

**Recommandation : (a). Confiance 0,7.**

### A2. Le comptage des heures d'arrêt dans le texte scellé du témoin de Bailey

**Enjeu.** Le texte scellé compte la dépense de chaque instance à son taux réel **de sa création à sa destruction**,
sans distinguer la marche de l'arrêt (lu par la session, texte en main : `prereg/temoin-attaque-publiee-bailey-v1.md`,
`fb6c2f34…`, l. 252-254 ; le code suit le texte). Or une instance arrêtée **ne facture que son disque** : la mère a lu
les champs de facturation du loueur à 01:41Z — l'instance du témoin coûte **0,153 USD/h** réels (110 Go, concordance
exacte avec le coût de stockage déclaré), **pas 1,325 USD/h**. Le texte impute donc ≈ 8,7 fois le coût réel sur les
heures d'arrêt, et cela fait tomber le nombre de tours de la relance sous le seuil où elle serait retenue au verdict.
Conséquence : **un run de confirmation de 34 USD est perdu à cause d'une règle de prudence, pour un surcoût réel de
quelques dollars.** C'est un écart à un texte scellé : la décision appartient à Lazar, jamais au calcul.

**Options.** (a) Un addendum qui compte les heures d'arrêt au taux de stockage relevé chez le loueur, avec la preuve du
relevé. Avantage : la relance redevient pleinement valable, même vers midi ; la règle devient juste au lieu d'être
seulement sévère. Inconvénient : on modifie une règle de comptage **après avoir vu** qu'elle gêne — à écrire comme tel,
et à contre-lire durement (c'est exactement la forme d'un ajustement intéressé, même quand il est fondé). (b) Ne rien
changer. Avantage : aucune discussion sur la pureté du préenregistrement. Inconvénient : la relance est abandonnée pour
un artefact comptable. (c) L'addendum, plus celui déjà proposé par la session sur le plafond horaire (1,6 → 1,40 USD/h).

**Recommandation : (a), avec contre-lecture par un agent neuf d'un autre modèle, et mention écrite que la règle est
corrigée après constat. Confiance 0,6** — la correction est fondée, mais sa forme doit être irréprochable.

### A3. Le devis de la tranche de l'ajustement de nos lentilles dépasse son plafond

**Enjeu.** Relevé de prix du 2026-11-18T01:39:39Z : **aucune carte au prix exigé de 3,00 USD/h** ; les offres du filtre
complet sont vers 4,23 USD/h stockage compris, soit un **pire cas vers 109,6 USD contre un plafond de 88 USD**.

**Options.** (a) Relever le plafond. (b) Garder 88 USD en réduisant explicitement le périmètre, **en disant quelle
question on renonce à trancher**. (c) Attendre un prix plus bas, au risque que la fenêtre du travail se referme.
(d) Renoncer à la tranche.

**Recommandation : la session de la lecture par lentille neuronale la donnera avec sa version corrigée** ; la mère ne
tranche pas à sa place. Consigne déjà donnée : ne rien ajuster pour faire entrer le pire cas sous le plafond.

---

## B. Décisions de fond, sans urgence d'horloge

### B1. Le jeu de l'idée du poids du nul, arrêté à 385 tranches sur 600

**Enjeu.** Sa machine s'est arrêtée avec la fin du crédit, à 385 tranches sur 600, sans sortie ni fichier d'arrêt.
L'addendum en vigueur **interdit la reprise d'un jeu interrompu** : relance seulement sous un addendum neuf. La machine
n'est **pas détruite** : ses tranches sont sur son disque et elle ne coûte que 0,0026 USD/h, soit six centimes par jour.

**Options.** (a) Addendum de relance neuf, contre-lu et scellé, et le jeu repart de zéro quand le crédit revient.
(b) Le jeu passe après l'étape B bis, dont l'échéance est dure. (c) Détruire la machine et abandonner les 385 tranches.

**Recommandation : (b). Confiance 0,7.** Dans tous les cas, ne pas détruire la machine avant décision : elle ne coûte rien.

### B2. Lequel des deux préenregistrements des organismes discrets fait foi

**Enjeu.** Deux textes ont été scellés le 17 novembre pour la **même** expérience : `prereg/T0.7-organismes-discrets-v-a-v1.md`
(`06ab6a2f…`, inscrit au registre des scellements) et `prereg/organismes-discrets-va-v1.md` (`37d1e1b6…`, inscrit en
R-3097). Deux empreintes opposables pour une seule expérience rendent n'importe quel verdict attaquable.

**Options.** (a) Celui du registre des scellements fait foi, l'autre est déclaré surnuméraire et archivé. (b) Celui de
R-3097, dont les en-têtes passent le validateur du gabarit. (c) Un troisième texte unique, les deux archivés.

**Recommandation : (b), confiance 0,6**, sous réserve de ce que l'audit en cours établira sur leur différence de fond.
Dans tous les cas, la version écartée est archivée sans modification (R12) et une ligne de registre dit laquelle fait foi.

### B3. Renouveler ou non l'autonomie de la mère

Sans mot de Lazar, la mère reste en hiérarchie ordinaire : elle écrit, fait contre-lire, ne dépense ni ne franchit rien.

### B4. Garder le mode d'orchestration étendu (« ultracode ») pour la session mère

**Enjeu.** Ce mode fait orchestrer des équipes de sous-agents sans regarder le coût en jetons. Il sert bien les règles du
programme, qui exigent déjà un contre-lecteur neuf partout (R2), un verdict par un tiers neuf (R13) et un audit de
symétrie (R4). Mais **deux mères se sont déjà arrêtées en pleine course pour quota épuisé** (14 et 15 novembre) : si le
quota tombe cette semaine, la mère s'arrête avant le verdict du 22.

**Recommandation : le garder, en l'employant pour les audits, contre-lectures et cribles, et non pour la coordination
ni l'écriture des registres. Confiance 0,7. Défaut sous 48 heures : gardé avec cette discipline.**

---

## C. Gestes qui n'appartiennent qu'à Lazar (contact externe, clés, accès)

### C1. Dépôt chez le tiers des pièces du témoin de Bailey

Six pièces, **empreintes vérifiées par la mère sur la branche** `claude/compassionate-meitner-d4ryyk` (sommet `46d6f187`),
et non recopiées d'une déclaration. Cinq sur six sont conformes à leur compagnon ; **la sixième (le code de lecture) n'a
pas de compagnon**, écart à R6 à faire corriger par la session avant le dépôt.

| pièce | empreinte vérifiée |
|---|---|
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-3-code-v16-message-erreur-nouvelle-serie.md` | `4b1f33bf4102b4a6dcc0873d41682ebbe00220c5a678c9eacaa4e69ea2624b58` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-troisieme-serie.md` | `89d2f6470a30276197a7ca986355e8026bb7ed6a5e2be43a068166acdcd5bbf3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-code-v20.md` | `eb97994a1ebcd0f3dfa3b413187a0b4dc213ef62ad1e516fc4b8814eb8ab357d` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-6-credit-recharge-auto.md` | `982bfbcbb7ed5634b0f297514133999d4141de53ed458c41e0c95d6f8281d49d` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` | `554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e` |
| `src/controle_ia/temoin_bailey/lecture_scellee_v3.py` | `a367853b4aadbf20482001ad086c67fdaa5b6e80bc45ac4a15f01d9211800dcb` (compagnon absent) |

Les addenda 1 et 2 sont **déjà déposés** : vérifié par la mère (file F-002 du 10 novembre ; manifeste v5 déposé le
11 novembre à 23:13:50Z, projet privé `dr57c`, R-2397).

### C2. Révocation du jeton de la plateforme de modèles

Recommandée par la session de la lecture par lentille neuronale : il a été passé à **six machines louées**. Sans lien
avec les deux clés du témoin de Bailey, qui, elles, **ne doivent pas être retirées avant la clôture du témoin** (clé de
déploiement `diag-temoin-bailey-depot-20261115`, clé d'accès distant 1864483 du loueur).

### C3. Lieu de rangement des lentilles

Trois possibilités — aucun rangement, stockage d'objets privé, ou la machine de Lazar — et le choix **conditionne la
commande** de la tranche d'ajustement. Il appartient à Lazar.

### C4. Une session neuve pour le compte de l'organisme d'idéation

Sa garde de calcul **ne se charge pas** : les réglages sont lus à l'ouverture de la session, depuis le dossier
d'ouverture, et elle s'est ouverte sur le dépôt public. Le script lui-même est sain (éprouvé sur quatre cas par elle, et
indépendamment par la mère). **Seul remède : rouvrir la session sur le dépôt de travail.** En attendant, interdiction de
toute commande payante, appliquée.

### C5. Lettre de modèle de la session hôte du compte 3

Elle se déclare de la même lettre que l'ancien hôte et demande que Lazar le confirme ; la ligne 190 de la liste
« qui a lu quoi » le porte comme non confirmé.

---

## D. Pour information — ce qui n'attend rien de Lazar

- **Reprise faite** (R-3103) : empreintes de lancement conformes ; arbre d'empreintes à 100 écarts, **aucune empreinte
  fausse** ; aucune machine de cette lignée en marche ; garde de calcul de la mère active et éprouvée sur un cas sain et
  deux artefacts.
- **Cinq sessions sœurs reprises et encadrées** (R-3105 à R-3110) ; identité de la mère confirmée par Lazar à 01:40:39Z.
- **Quatre déclarations spontanées de lecture large**, toutes sans effet sur un résultat : aucune issue, aucun score
  ouverts. Cause commune : aucune porte d'entrée pour une session rouverte sur un compte neuf. Remède écrit et scellé :
  `docs/procedures/orientation-sessions-v1.md` (R-3111).
- **Version 5 de la liste « qui a lu quoi »** écrite, scellée, attestée conforme, **pas encore en vigueur** : contre-lecture
  par un agent neuf en cours, et quatre corrections déjà demandées par l'hôte du compte 3 ; une version 6 les intégrera
  d'un seul tenant.
- **En vol, sans dépense** : audit de reprise en six dimensions, chacune contre-lue ; suite d'essais complète ; lecture
  sur documents d'origine pour le juge au nul formé des lois connues ; version 7 du devis de la tranche d'ajustement.
