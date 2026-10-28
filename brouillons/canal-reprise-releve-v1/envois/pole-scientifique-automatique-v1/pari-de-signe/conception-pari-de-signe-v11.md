# Le pari apparié borné — conception v11 : la course joue la génération, frontière de confiance dite, clé en deux parties, ordre dérivé de la clé, gardes obligatoires (contre-lecture de la v10)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), rédaction commencée après le relevé `date -u` de
02:02:48 UTC le 28 octobre. **Remplace la v10** (`1237d52d…`, gardée, R12) selon la contre-lecture de la v10 et du code
version 28 (sous-agent neuf Opus 5.5, `contre-lecture-v10/rapport-contre-lecture-pari-signe-v10.md`, `7bb83a48…`, « à
amender en v11, corrections locales » ; code « à corriger » ; les chaînes de la contre-lecture v9 **rejouées contre la
version 28 : toutes refusées ou sans effet** ; K9-4, K9-7, K8-4 fermés ; K9-1, K9-2, K9-3, K9-5, K9-6, K9-8, K8-2, K8-5,
K9-10 (b) à moitié ; dix constats K10-1 à K10-10, tous acceptés). Delta de la v10. Exploratoire (R-546) ; décisif dès qu'il
sert G1. Code : v7, **version 29** (`../orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v29.md`). **Pas encore
contre-lue.**

## Verdict (ce que change la v11)

1. **La course joue la génération ; l'orchestrateur ne voit aucune trajectoire (K10-1, K10-2).** Deux chemins passaient
   toutes les gardes de la version 28 : une évaluation **privée** (appel d'`evaluer` sans journal) suivie d'une déclaration
   « sans partie » si l'issue déplaît (0,055 puis **0,79** d'au moins une fausse promotion sur 10 puis 30 générations, contre
   0,005 et 0,01 en honnête) ; une **fiche espionne** (même contraste, autre étiquette `population`, acceptée) qui lit la
   tranche la première, la fiche visée n'étant lancée que si l'issue est favorable (0,62 contre 0,01 sur 30 générations).
   Désormais `engagement_apparie.jouer_generation(course, monde, engagements, abandons_avant=…, non_lancees=…,
   abandon_apres=…)` joue **une génération entière** : les décisions « avant toute issue » (abandons « avant partie »,
   fiches non lancées) sont des **entrées** de la fonction, prises avant qu'elle ne calcule quoi que ce soit ; elle calcule
   les parties, les journalise sous la génération de la course, les ajoute, applique la règle d'abandon « après partie »
   (permise par le contrat), lit, et rend un **compte rendu sans trajectoire**. La fiche espionne est refusée par la mémoire
   (point 3). **Frontière de confiance, dite dans D-S25 bis** : tant qu'une partie tient les scores d'épreuve, rien ne
   l'empêche de calculer en privé ; le code ne peut garantir que ce qui passe par lui. Dans le pôle, **le monde tient les
   scores d'épreuve et la course les lit** ; l'orchestrateur reçoit des engagements et des verdicts, jamais la banque
   d'épreuve (c'est l'architecture du noyau : issues cachées, tirées après le gel). Un orchestrateur qui aurait la banque
   n'est pas couvert par la garantie — il faut le savoir pour ne pas le construire ainsi.
2. **La clé est en deux parties (K10-6)** : `affirmation` (contrastes canoniques, τ, strate, seuils, comparateurs, gardes)
   et `lecture` (partie, plan des tranches, population, m_max, Λ, version de l'e-processus). « Une affirmation, une fiche »
   se tient sur l'**empreinte de l'affirmation** : un autre plan ou une autre population ne font pas une autre affirmation
   (c'était le chemin de la fiche espionne) ; la course tient le lien fiche ↔ clé entière (ses parties viennent du même
   engagement). Une `identite` de banque ré-étiquetée permettrait de relire les mêmes unités physiques : **l'identité est une
   déclaration de l'orchestrateur, scellée au manifeste, et la disjonction entre banques est la tâche de la mémoire du
   noyau** (dit, non codé ici).
3. **L'ordre secret dérive de l'empreinte de la clé, de la génération et de la graine scellée du monde (K10-3)** — plus du
   nom du contraste, du budget, de l'empreinte de l'engagement ni de l'empreinte de la banque (une unité factice ajoutée ne
   change plus l'ordre) : cent noms donnaient cent ordres pour une même affirmation ; « plus d'étiquette libre » était faux
   en v10, vrai en v11.
4. **Le journal est en lecture seule pour l'appelant (K10-4)** : ajout seul (celui qui calcule), identifiants d'unités
   gardés, génération fournie par la course (une chaîne est refusée) ; la démonstration v28 effaçait elle-même une entrée —
   plus possible. **Une partie vide** (aucune unité de la tranche dans la strate) est journalisée vide par celui qui calcule
   et vaut déclaration « sans partie » acceptée (K10-5) : plus de garde qui bloque à tort.
5. **Les gardes sont obligatoires (K10-7)** : une `Course` sans journal, ou une entrée sans clés, est **refusée** ; `essai=True`
   la permet pour un essai, dit comme tel, jamais en production.
6. **Lecture de la démonstration (K10-8)** : l'e-valeur de la fiche de forme G1 était fixée à chaque partie par une **garde**
   (incréments 2,118, 1,778, 1,326 : exactement les minima des gardes), et la lecture L3 n'affichait que les contrastes de la
   dernière partie. La v29 rapporte, par partie, le **processus qui fixe le minimum** (contraste ou garde) et toutes les
   richesses ; dans la course publiée : `garde:blanc-juge`, `garde:blanc-cascade`, `garde:blanc-cascade`. Les gardes **sont**
   la contrainte active de G1 (b) sur cette banque — ce que (β) de la v9 n'avait pas vu.
7. **Coût des gardes (K10-9)** : cinq gardes à δ = 0,10 coûtent **≈ 80 à 210 unités honnêtes par mode** (estimation de la
   contre-lecture) ; c'est à joindre à la question posée à Lazar (garde par comparateur, D-S8), avec le poste de devis en
   (écart, discordance, C) de la v10.
8. **Mineurs (K10-10)** : « 0,5 ≈ 14 points de rappel » vaut entre blanc et cascade seulement (dit) ; « 25 fiches,
   25 affirmations » est vrai par construction depuis que la mémoire refuse les redites (dit comme tel) ; essai « Λ changée
   ⇒ clé changée » ajouté ; le plan est vérifié disjoint et dans la partie, pas « jamais dérivé des scores » (obligation de
   l'orchestrateur, dite) ; l'artefact 5 commenté juste ; le nul × 200 porte sur le nul complet (dit depuis la v10).

## 1. Corrections, section par section de la v10

### D-S25 bis (2), (5) — la course joue, la frontière de confiance
Ajouter à (2) : « **la course joue la génération** : décisions avant toute issue en entrée, parties calculées et journalisées
par celui qui calcule, lecture ; l'orchestrateur ne reçoit qu'un compte rendu ; **frontière de confiance** : le code ne
garantit que ce qui passe par lui — le monde tient les scores d'épreuve, la course les lit, l'orchestrateur ne les a jamais ».
Ajouter à (5) : « une affirmation = l'empreinte de la partie `affirmation` de la clé ; l'ordre secret dérive de la clé, de la
génération et de la graine du monde ; une partie vide est journalisée vide et vaut déclaration ».

### D-S18 — clé en deux parties
Clé = {affirmation : contrastes canoniques, comparateurs, τ, strate, seuils, gardes ; lecture : partie, plan des tranches,
population, pondération et m_max, Λ, e-processus}. L'unicité « une affirmation, une fiche » porte sur l'affirmation ; le lien
fiche ↔ clé porte sur la clé entière.

### D-S8 et § 6 — gardes
Ajouter : « les gardes de G1 (b) sont la contrainte active sur la banque de démonstration ; leur coût (≈ 80 à 210 unités
honnêtes par mode à δ = 0,10) entre au devis avec (écart, discordance, C) ; le processus minimal est rapporté par partie ».

## 2. Décisions

| décision | état |
|---|---|
| D-S25 bis (2), (5) (la course joue ; frontière de confiance ; affirmation ; ordre dérivé de la clé ; partie vide) | proposée (0,85) |
| D-S18 (clé en deux parties) | proposée (0,85) ; **codée** en version 29 |
| D-S8 (garde par comparateur, coût au devis) | précision du nœud 1 = b, **à confirmer par Lazar** avec son coût |
| nœud 2, D-S29, D-S30 | inchangés (lus, non confirmés) |

## 3. Code (v7, version 29)

`pole/pari_apparie.py` : `Course(alpha, journal, essai=False)` (journal obligatoire), `entrer(..., cles=…)` obligatoire hors
essai, partie vide acceptée comme déclaration si le journal la dit vide. `pole/engagement_apparie.py` : clé en deux parties
(`empreinte_affirmation`), ordre dérivé de `empreinte_cle` et de la génération, `Lignees` sur l'affirmation, journal en
lecture seule (`_Journal`), `marquer_vide`, **`jouer_generation`**. `pole/monde_banque_scores.py` : ordre secret dérivé de
l'identité. Démonstration refaite sur `jouer_generation` (sept artefacts : + fiche espionne, + course sans journal) ; lecture
L3 avec le processus minimal par partie. **Essais : voir le LISEZMOI v29.**

## 4. Ce que la v11 laisse ouvert (dit)

Sa contre-lecture ; K7-6, K7-7 ; la disjonction entre banques (mémoire du noyau) ; le lien au cycle (la `Course` et
`jouer_generation` ne sont pas encore appelées par `pole/cycle.py`) ; la mesure de (écart, discordance, C) et du coût des
gardes sur une lecture pilote ; le dimensionnement de G1 (b) avec ses gardes.
