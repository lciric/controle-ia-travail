envoyable après remplacements (couples exacts ci-dessous)

# Contre-lecture neuve du CV v14 et du mémo v2 (candidature Pivotal) — v1

- Lecteur : sous-agent neuf, sans part aux textes relus. Écrit le 2 novembre 2026, de 06:47 à 07:10 UTC environ. Lecture seule : aucun commit, aucun `git fetch`, aucun appel de réseau ni de modèle, aucun fichier existant modifié. Calculs sous `nice -n 10`. Extractions et images dans le bloc-notes de la session (`/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/cl/`).
- État relu (sha256, 12 premiers caractères) : `construire_cv_v14.py` `2eb054e0b9d4…`, `variantes.json` `e34e53b06873…`, PDF U `547697b7e34c…`, C `b7a77c61380f…`, I `5a49a7e7aeba…`, S `f921cb32caa3…` (les copies posées dans `candidature-pivotal-v15/` sont identiques à l'octet), mémo `7175910011d0…`, formulaire `e46a3fe5690c…`.
- **Attention : un autre auteur modifie le dossier pendant la relecture.** `reponses-formulaire-v14.md` a été réécrit à 07:00:55 UTC, et `contre-lecture-formulaire-v14-v1.md` (06:58 UTC) et `LISEZMOI-candidature-pivotal-v15.md` sont apparus. Je n'ai pas lu cette autre contre-lecture. Ce rapport vaut pour les empreintes ci-dessus.

## Ce qui bloque l'envoi, et ce qui est seulement recommandé

- **Bloquant (1)** : le bandeau des variantes U et C donne le résultat de R4 sans sa réserve, et dit « stays diffuse » alors que la dose forte était flagrante (« plain in behaviour »). Couples 1 et 2.
- **Bloquant (2)** : la section 10 du formulaire donne le même résultat de R4 sans réserve (couple 7). Le PDF du mémo ne reprend plus la section 10 actuelle : il faut le **régénérer** après le couple 7 (E).
- **Recommandé** : essaim (« by about 0.2 » s'applique à une seule des deux réfutations), défenses (marge de 0,02), lecture à graines neuves (« mêmes 96 tâches », lecteur neuf). Couples 3 à 5.
- **Facultatif** : la borne de P3 sous la forme (b) de sa vérification (couple 6). La mise en page de U et C (en-tête de projet seul en bas de la page 1) n'a pas de correctif sûr à longueur constante (D).

## A. Différentiel v13 → v14

Relevé avec `diff` sur `construire_cv_v13.py`/`construire_cv_v14.py` et sur les deux `variantes.json`.

- **Changements attendus, tous présents et seulement eux** :
  - générateur, l. 65 : puce des défenses réécrite ;
  - l. 66 et 67 : deux puces ajoutées (essaim ; « First tests on a real model ») ;
  - l. 76 : ajout dans « Evidence so far » (« then a fresh-seed batch of 288 … no real link ») ;
  - l. 83 : `@page` 10/12 mm → 8/11,5 mm ;
  - l. 85 : police 7,45 → 7,3 pt, interligne 1,2 → 1,175 ;
  - `variantes.json` : seuls les bandeaux U (l. 17) et C (l. 62) changent, avec une proposition ajoutée chacun. Les bandeaux B, S et I sont inchangés.
- **Autres changements, sans effet sur le texte imprimé** :
  - la docstring de la l. 1 (interne) ;
  - `imprimer.js`, qui ne diffère que par les chemins ;
  - `chiffres.json`, identique ;
  - les `cv-{U,C,I,S}.html` intermédiaires, désormais posés dans le dossier.
- **Dans la réécriture de la puce des défenses** :
  - « November 2026 » a disparu, sans effet ;
  - « better on held-out laws » a disparu, alors que ce constat est **répliqué** (HRép-ii : +0,0598 et +0,0673). C'est une perte de contenu, pas une erreur.
- Les PDF sont à jour : leur texte contient les nouvelles puces et les nouveaux bandeaux, et « stays diffuse » figure dans `cv-U.html` et `cv-C.html` seulement.

## B. Concordance des nombres et qualificatifs ajoutés

| Énoncé du CV | Source | État |
|---|---|---|
| « +0.11 and +0.13 detection rate », « replicated at a fresh seed » | réplication des défenses, § 6 : +0,1123 et +0,1255, « répliquée » aux deux budgets | conforme (ce sont les valeurs de la réplication ; l'original donnait +0,10/+0,12) |
| « "a fixed defence does as well" was neither confirmed nor contradicted » | § 3 : « ni confirmé ni contredit : reste le constat d'une seule course, à dire avec sa marge de 0,02 » ; table, ligne 7 | conforme ; la marge de 0,02 manque (couple 4) |
| « Synthetic arena, no language model » | § 3, portée | conforme |
| « 4 of 7 … held, 2 were refuted and the refutations replicated …, 1 was inconclusive » | essaim, verdict : 4/2/1 sur 7 ; HP.4 et HP.5a de nouveau contraires en réplication | conforme |
| « (the surrogate underestimated the swarm statistic's power by about 0.2) » | HP.4 : 0,665 observé contre 0,463 modélisé, **sous la seule sonde des enjeux** (tromperie : 0,744 contre 0,705). HP.5a : la règle de la moitié tient à 5 agents (0,068 contre 0,032 modélisé) | imprécis : l'écart de 0,2 vaut pour une réfutation, pas pour les deux. mentor-4 v10 nomme aussi la seconde. Couple 3 |
| « on never-computed cells and the real honest scores of my first activation experiment » | 60 épisodes honnêtes de P3, rééchantillonnés, menace simulée | conforme à la phrase contrôlée de mentor-4 v10. Le verdict interdit seulement « sur données réelles » en général, ce que le CV ne dit pas |
| « (2,400 scored actions) », « plain in behaviour », « no generic probe cleared its random-probe floor » | mentor-6 v10 (contrôlé) ; n° 251, point 1 (2 400) ; R4-prereg (P3 « flagrant », × 33) | conforme |
| « power 0.8 only near a 0.46-SD shift » | borne P3 v2 : δ* au seuil observé 0,457 (JSON) et 0,462 (recalcul) pour la **sonde de tromperie** ; enjeux 0,40 | nombre conforme, et c'est le bout prudent. Mais c'est la forme (c) de la vérification, « 0,46 seul », que la règle de divergence gelée n'admet pas sans v3. mentor-6 v10 emploie (b), qui nomme 0,33. Couple 6, facultatif |
| « Under a weaker instruction » | consigne de dose faible : « about 30% higher » contre « about three times » ; dose réalisée r médian 6,59 [1,97 ; 26,5] contre ≈ × 33 en P3 | conforme, aussi pour la dose réalisée (hors de la fourchette prédite [1,2 ; 5], sans effet sur le critère) |
| « 27% … at 1% false alarms, LLM judges of 3B and 8B at most 3% » | n° 251 : 0,269 (prédicteur sur les traits) ; juges ≤ 0,028 ; R4-prereg l. 26-29 et 83-87 : juges 3B et 8B, rappel **par action** | conforme |
| « preregistered dose criterion » | R4-prereg, § Seuil : (i) rappel < 0,5 et (ii) borne basse de log10 r > log10 1,1 | conforme |
| « one reservation on the controls » | n° 251 : « diffuse, avec réserve » ; mention 0,57 et témoin 1,44 hors [0,8 ; 1,25] ; R4-prereg l. 123 | conforme **au résumé** : le verdict scellé n'est pas lisible ici. Le texte prévoit aussi une réserve si (i) change entre 1 % et 2 % ; le n° 251 n'en dit rien |
| « The white-box versus black-box comparison is sealed before any data » | mentor-6 v10 : « both analyses sealed before any data » | repris d'une phrase contrôlée ; non revérifié, faute de source dans la liste |
| « 288 … the 3 planted links, none of 19 null controls, and no real link » | lecture à graines neuves, § 2 et § 3 : 0 témoin faux promu sur m = 19, 3/3 plantés, aucune loi réelle promue | conforme. Les 288 épisodes viennent des **mêmes 96 tâches** (« ne permet rien sur des tâches neuves ») ; le lecteur est une instance neuve. Couple 5 |

## C. Sur-énoncés

1. **Bandeaux U et C : « a hidden saboteur under a weak instruction stays diffuse — … 27% … »**
   - La réserve de R4 manque. C'est le cas « résultat de R4 présenté sans sa réserve ».
   - « stays » laisse croire que la menace était déjà diffuse. Or, sous la consigne forte, le sabotage est flagrant (« plain in behaviour » dans la puce elle-même ; P3 : règle du coût à 0,888 d'aire).
   - « hidden saboteur » peut se lire comme un saboteur spontané.
   - Couples 1 et 2 : même longueur, « weakly instructed » et « (one reservation) ».
2. **Section 10 du formulaire et mémo : « under a weaker instruction the best per-action black-box monitor catches 27% … »**, sans réserve. Couple 7.
3. **Puce de l'essaim : « (… by about 0.2) »** attribue l'écart de 0,2 aux deux réfutations. Couple 3, même longueur.
4. **« the threat becomes diffuse »** dans la puce du CV : bien limité à la dose faible (« Under a weaker instruction »), avec le critère et la réserve. Pas de sur-énoncé.
5. **« 3 sur 3 »** : le CV et le mémo ne le donnent que comme un compte (« promoted the 3 planted links »), jamais comme une puissance. Cela respecte la réserve 6, à condition de ne pas ajouter « power ».
6. **« First tests on a real model »** : le modèle est réel (Llama-3.1-8B), et la nature d'organisme à consigne cachée est dite dans les mots suivants (« hidden-instruction saboteur »). Acceptable tel quel.
7. **Défenses** : « a fixed defence does as well » est bien donné comme le constat de la première course. Il manque la marge de 0,02 que le verdict exige (couple 4, plus court).
8. **Graines neuves** : rien de faux. Préciser « same 96 tasks » écarte toute lecture « nouvelles tâches ». « fresh reader » est le terme des phrases contrôlées (mentor-8 v10, README). Couple 5, plus court.

## D. Mise en page

Relevé avec `pdfinfo`, `pdftotext -layout`, `-bbox-layout` et `pdftoppm -r 60`, puis lecture des images.

- **Les quatre PDF font deux pages A4.** Aucun texte coupé : chacun finit par « Spoken: French, English, Serbian ». Bas de la page 2 : U, C et I à 810,2 pt, S à 801,2 pt, pour une limite de 819,2 pt (marge de 8 mm). Il reste donc à peu près 1 ligne libre (U, C, I) et 2 lignes (S). La page 1 de U est pleine (819,0 pt).
- **U et C : défaut visible, non bloquant.** L'en-tête « Geometry and Causal Structure of Safety Concepts in Open-Weight LLMs », avec ses deux lignes de description, reste seul en bas de la page 1, et ses trois puces passent en page 2. En v13, la première puce était encore en page 1.
  - Je ne propose aucun correctif à longueur constante. `break-after: avoid` sur l'en-tête le ferait passer en page 2, qui n'a qu'une ligne libre : la page 3 serait probable.
  - À trancher par la session : laisser tel quel, ou libérer au moins 3 lignes en page 2 puis le tester.
- **I et S** : la première puce de l'organisme est coupée par le saut de page (2 + 3 lignes en I, 3 + 2 en S). Aucune ligne n'est isolée ; acceptable.
- Les couples 1 à 6 sont de longueur égale ou plus courts. Ils ne devraient pas changer la pagination ; c'est à vérifier sur les PDF régénérés.

## E. Mémo v2

- **Une page** : oui. Environ un tiers de la page est vide.
- **Concordance de la phrase sur Llama-3.1-8B**, « generic probes miss a cost-inflating saboteur (a bounded null), and under a weaker instruction the best per-action black-box monitor catches 27% of its actions at 1% false alarms » :
  - les nombres concordent : 0,269 ; borne de P3 ; dose faible ;
  - « miss » rend bien « no generic probe cleared its floor » ;
  - **la réserve de R4 manque** (couple 7).
- **Le PDF ne reprend plus exactement la section 10 actuelle** (formulaire à 07:00:55 UTC) :
  - la phrase « read once under a sealed plan, it found … no real link » est devenue dans le formulaire « read once as preregistered, it promoted … no real law » ;
  - la phrase « Under way this week, each sealed before it runs: … » est absente du PDF ;
  - l'en-tête du PDF diffère : « Career memo / Lazar Ciric · 2 November 2026 · Pivotal Research Fellowship, 2027 Q1 », contre « Career memo, Lazar Ciric, 2 November 2026 ». C'est cosmétique.
  - Le reste du corps est identique, une fois la césure de fin de ligne retirée.
  - **Il faut régénérer le PDF depuis la section 10 corrigée.** Avec la phrase ajoutée (environ 3 lignes), il tient encore sur une page.
- **Hors de ma liste de sources, non vérifié** : la phrase ajoutée « Under way this week… ».
  - « each sealed before it runs » s'accorde mal avec « preregistration drafted, public » : c'est un engagement, pas un constat.
  - « on those actions » renvoie, par la grammaire, aux actions de la dose faible ; mentor-6 v10 situe la comparaison sur les 2 400 actions de P3.

## Couples exacts « remplacer : … / par : … »

**1. `cv-v14/variantes.json`, bandeau U** (bloquant ; 162 → 162 caractères)
- remplacer : `on the same model, a hidden saboteur under a weak instruction stays diffuse — the best per-action black-box monitor catches 27% of its actions at 1% false alarms;`
- par : `on the same model, a weakly instructed saboteur is diffuse (one reservation): the best per-action black-box monitor catches 27% of its actions at 1% false alarms;`

**2. `cv-v14/variantes.json`, bandeau C** (bloquant ; 160 → 160)
- remplacer : `on Llama-3.1-8B, a hidden saboteur under a weak instruction stays diffuse — the best per-action black-box monitor catches 27% of its actions at 1% false alarms;`
- par : `on Llama-3.1-8B, a weakly instructed saboteur is diffuse (one reservation): the best per-action black-box monitor catches 27% of its actions at 1% false alarms;`

**3. `cv-v14/construire_cv_v14.py`, l. 66** (recommandé ; 71 → 71)
- remplacer : `(the surrogate underestimated the swarm statistic's power by about 0.2)`
- par : `(the surrogate underestimated the swarm statistic's power by up to 0.2)`

**4. `cv-v14/construire_cv_v14.py`, l. 65** (recommandé ; 104 → 99)
- remplacer : `the first run's "a fixed defence does as well" was neither confirmed nor contradicted by the replication`
- par : `the first run's "a fixed defence does as well" (within 0.02) was neither confirmed nor contradicted`

**5. `cv-v14/construire_cv_v14.py`, l. 76** (recommandé ; 113 → 111)
- remplacer : `then a fresh-seed batch of 288 real episodes, read once under a sealed plan and checked by an independent reader:`
- par : `then 288 fresh-seed episodes of the same 96 tasks, read once under a sealed plan and checked by a fresh reader:`

**6. `cv-v14/construire_cv_v14.py`, l. 67** (facultatif : forme (b) de la vérification de P3, comme mentor-6 v10 ; 139 → 138)
- remplacer : `the sabotage is plain in behaviour, yet no generic probe cleared its random-probe floor (bounded null: power 0.8 only near a 0.46-SD shift)`
- par : `plain in behaviour, yet no generic probe cleared its random-probe floor (bounded null: power 0.8 only near 0.46 SD; 0.33 at a noise floor)`

**7. `reponses-formulaire-v14.md`, section 10**, puis régénérer `Lazar_Ciric_career_memo_2026-11-02_v2.pdf` (bloquant ; 115 → 113)
- remplacer : `and under a weaker instruction the best per-action black-box monitor catches 27% of its actions at 1% false alarms.`
- par : `and under a weaker instruction black-box monitors flag ≤ 27% of its actions at 1% false alarms (one reservation).`
- Variante plus claire si la longueur ne compte pas pour le mémo (il reste un tiers de page) : `… catches 27% of its actions at 1% false alarms (one reservation, on the controls).`

Après les couples 1 à 6 : régénérer les quatre PDF, puis revérifier deux pages par variante et l'en-tête « Geometry » de U et C.
