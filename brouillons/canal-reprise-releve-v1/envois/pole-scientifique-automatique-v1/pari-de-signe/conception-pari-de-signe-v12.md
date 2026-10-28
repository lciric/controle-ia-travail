# Le pari apparié borné — conception v12 : le côté de confiance nommé en entier, deux passes dans la génération, journal qui fixe trajectoire et clé, phrases de la v11 corrigées (contre-lecture de la v11)

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), rédaction commencée après le relevé `date -u` de
02:33:55 UTC le 28 octobre. **Remplace la v11** (`8307a6ac…`, gardée, R12) selon la contre-lecture de la v11 et du code
version 29 (sous-agent neuf Opus 5.5, `contre-lecture-v11/rapport-contre-lecture-pari-signe-v11.md`, `ee82b1ee…`, « à amender
en v12 : phrases et frontière, pas tout refaire » ; code « à corriger » ; K10-8, K10-9, K8-5 fermés ; K10-7 fermé avec un
résidu ; K10-1 à K10-6 et K10-10 à moitié ; sept constats K11-1 à K11-7, tous acceptés). Delta de la v11. Exploratoire
(R-546). Code : v7, **version 30** (`../orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v30.md`). **Pas encore contre-lue ;
la contre-lecture de la v12 et de la version 30 est la première tâche de la reprise sur ce sujet.**

## Verdict (ce que change la v12)

1. **Le côté de confiance est nommé en entier (K11-2)** : la banque d'épreuve, **le monde et sa graine**, **la course et son
   journal**, **la construction des engagements** (`construire` lit les seuils de calibrage et le plan) sont du côté de
   confiance ; l'orchestrateur du pôle n'y est pas — il reçoit des engagements construits, des comptes rendus et des verdicts.
   La garantie de D-S25 bis vaut **sous cette séparation** ; un orchestrateur qui tiendrait le monde ou la course est hors
   garantie, et le code ne peut l'en empêcher (il peut seulement refuser ce qui passe par lui). Ce que la v11 disait de la
   banque seule était juste et incomplet.
2. **Deux passes dans la génération (K11-1)** : `jouer_generation` calcule, journalise et ajoute **toutes** les parties
   **avant** d'appliquer la règle d'abandon « après partie » — la règle ne voit aucune issue avant que toutes soient
   fixées, et ne peut plus interrompre la génération entre deux fiches (l'espionne corrélée à τ = 0,051 passait par là :
   0,55 contre 0,04). Une exception au milieu est **tracée** au journal (« génération interrompue ») et la reprise ne
   recalcule aucune partie journalisée (K11-4) ; une partie journalisée mais non ajoutée après interruption rend la fiche
   irrécupérable sans sa trajectoire : retrait (D-S26 bis), dit.
3. **Le journal fixe la trajectoire et la clé (K11-3)** : il enregistre l'**empreinte de la trajectoire** ; la course refuse une
   trajectoire fabriquée, une clé déclarée différente de celle du journal, un abandon « avant partie » dont la partie est au
   journal, une **fiche fantôme** au journal (inconnue de la course), une entrée d'une génération à venir ; à la lecture,
   **toute unité journalisée dans la génération est enregistrée comme lue**, ajoutée ou non ; `evaluer` sans journal est
   refusé hors `essai=True`.
4. **Phrases de la v11 corrigées (K11-5)** : « plus d'étiquette libre » → « l'ordre dérive de la clé, de la génération et de
   la graine scellée du monde ; `population` est une étiquette **déclarée** de la clé de lecture, scellée avec
   l'engagement » ; « fiche espionne refusée par la mémoire » → « refusée quand elle porte la **même affirmation** ; une
   espionne **corrélée** (autre τ, mêmes seuils) n'est pas la même affirmation : c'est la **frontière** et les deux passes qui
   la bloquent, pas la mémoire » ; « génération fournie par la course » → « dans `jouer_generation` ; hors d'elle, à la
   lecture, le journal est confronté » ; « gardes obligatoires » → « présence exigée, authenticité non vérifiable par le
   code (un faux journal est du côté de confiance) » ; K7-7 **fermé pour l'ordre** (l'ordre ne dépend plus d'aucun score) ;
   l'artefact 5 commenté juste cette fois.
5. **Population et identité (K11-6)** : `population` n'est plus dans l'affirmation (voulu : la même affirmation sur deux
   viviers est une seule affirmation) ; une banque sans `identite` déclarée prend son empreinte et le code le **dit** au
   manifeste de l'engagement ; comment une fiche continue sur le vivier de la génération suivante : par le **plan des
   tranches** scellé (une tranche par génération), sinon elle est « sans partie » déclarée.
6. **Mineurs (K11-7)** : docstrings mises à la version 30 ; la version de l'e-processus reste écrite à la main (dit :
   c'est une constante du module, changée avec lui) ; essais ajoutés pour `abandon_apres` en deux passes et pour une
   exception au milieu.

## 1. Corrections, section par section de la v11

**D-S25 bis (2)** : ajouter le côté de confiance nommé en entier (point 1) et les deux passes (point 2). **D-S25 bis (5)** :
ajouter « toute unité journalisée dans la génération est lue par la course » et « le journal fixe la trajectoire et la clé ».
**D-S26 bis** : « une fiche dont une partie est journalisée mais non ajoutée après une interruption est retirée ».

## 2. Décisions

| décision | état |
|---|---|
| D-S25 bis (2), (5) (côté de confiance nommé ; deux passes ; journal qui fixe trajectoire et clé ; unités journalisées lues) | proposée (0,85) |
| D-S26 bis (retrait après interruption) | proposée (0,85) |
| D-S8 (garde par comparateur, coût au devis) | **à confirmer par Lazar** avec son coût (inchangé depuis la v11) |

## 3. Code (v7, version 30)

`pole/pari_apparie.py` : `_empreinte_trajectoire` ; `ajouter_trajectoire` compare trajectoire et clé au journal ; `abandonner`
refuse « avant partie » si la partie est au journal ; `lire` refuse fiches fantômes et générations à venir, enregistre les
unités journalisées comme lues. `pole/engagement_apparie.py` : `evaluer(..., essai=False)` exige un journal ; le journal
enregistre l'empreinte de la trajectoire ; `interrompre`, `interruptions` ; `jouer_generation` en deux passes, reprise sans
recalcul. **Essais : voir le LISEZMOI v30.**

## 4. Ce que la v12 laisse ouvert (dit)

Sa contre-lecture (première tâche de la reprise) ; K7-6 ; l'authenticité du journal et de la course (côté de confiance, hors
code) ; le lien au cycle (`pole/cycle.py` n'appelle pas encore `jouer_generation`) ; le dimensionnement de G1 (b) avec ses
gardes (écart, discordance, C, coût des gardes).
