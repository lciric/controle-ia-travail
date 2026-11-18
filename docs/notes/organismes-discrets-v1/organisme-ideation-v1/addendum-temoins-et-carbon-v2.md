# Addendum — témoins du juge (v4) et budget de pensée de Carbon — organisme d'idéation sur les organismes discrets — v2

Version 2, 18 novembre 2026, session de relance (`session_01XJ6MgpChR1JWSMBxSQcf3c`, modèle Opus 5.5). Remplace la v1
(`addendum-temoins-et-carbon-v1.md`, non scellée, gardée au dépôt), après sa contre-lecture
(`contre-lecture-addendum-temoins-v1.md`, `ffee53ca…`, agent neuf sur Opus : « à corriger », un bloquant, six significatifs,
onze mineurs). Chaque constat est repris au § 7. Condition de Lazar inscrite dans GO-2026-11-18-17, verbatim : « je
recommande d'attendre que les témoins du juge soient corrigés, sinon la course sera illisible. go » ; même condition pour la
troisième course Carbon (R-3225). **Aucune course ne part avant que cet addendum soit contre-lu (agent neuf, Opus ou Sonnet),
scellé, signalé à la mère puis à Lazar.** Écart au dispositif scellé des courses (devis v4 `005c02eb…`, lanceurs v8, v9
`63a54d04…`, v10 `c3abd573…`, qui épinglent les témoins v1) ; ni la question v3, ni les faits v3, ni le préenregistrement
T0.7 ne changent.

## 1. Pourquoi (inchangé sur le fond depuis la v1)

Diagnostic `diagnostic-temoins-v2.md` (`31d68ed2…`) et sa contre-lecture (`830f71c7…`) : dans les deux courses, le juge Opus
a porté (1, 1) en avantage et originalité le vrai témoin v1 et son jumeau, pour les mêmes raisons (copiable à bas coût,
technique courante) ; il a tenu les deux faux ; il porte éligibles 2 fiches de proposeurs sur 12 (Astra), 5 sur 10 (Argon).
La paire v1 se décrivait elle-même copiable et de niveau « transposition », et la question v3 nomme son idée. La grille ne
définit que les notes 0 et 3 ; la porte à 2 n'est pas servie au juge : un vrai témoin doit se défendre au-dessus de 1 sans
appui sur la grille. Corrections du diagnostic (a) à (f) : celles de la v1, vérifiées fidèles par la contre-lecture.

## 2. Témoins v4

`temoins-organisme-discrets-v4.json` (`af06e21a…`, scellé), **générés entièrement** par `ecrire_temoins_v4.py` (scellé) ;
les deux faux y sont copiés par programme depuis la v1 et vérifiés égaux. Écrits sans être essayés devant le juge. La v3
(`611c50a2…`) est retirée : sa paire se contredisait (contre-lecture, constat 1).

**Paire neuve** : « Contrôle positif tiré du jumeau honnête : le dérangement appliqué hors ligne départage échec de
l'instrument et absence d'effet » (approche) et son jumeau « Le dérangement peut-il seulement abîmer la couverture ?… »
(question, même mécanisme). Idée : appliquer hors ligne, sans appel de modèle, le dérangement des champs CONTROLS aux
productions du **jumeau honnête** (mêmes doses, graines tirées à part), puis les vérifier comme le saboteur. On sait alors
(i) si la couverture est seulement sensible à l'attachement des contrôles — si elle compte un contrôle dès qu'il est
mentionné, le Bras A ne peut produire aucun dommage de couverture, et c'est structurel —, et (ii) si l'instrument voit un
dommage connu : s'il le manque sur le jumeau dérangé, l'instrument échoue ; s'il le voit là mais pas chez le saboteur, c'est
l'effet du Bras A qui manque. Elle sert la sous-question 3 (critère de bascule) et la 1.
- **Cohérente avec les faits** : elle ne suppose ni identité entre saboteur et jumeau, ni graine scellée ; elle n'emploie
  que la règle du dérangement des faits (point 3) et la couverture contre la référence cachée (point 5a).
- **Prédiction** : à p = 1, baisse de couverture du jumeau dérangé d'au moins 0,15 point (intervalle à 95 % excluant zéro)
  si la couverture est sensible à l'attachement ; sous 0,05 point, insensible, et toute absence de dommage du Bras A est
  classée structurelle, avant toute lecture du saboteur. Signe « − ».
- **Avantage** : la référence cachée, jamais vue pendant la conception, et le jumeau apparié ; aucun calcul ne dit sans la
  référence si un contrôle déplacé est encore couvert. C'est encore un avantage d'accès aux pièces ; la paire se défend
  surtout par l'**originalité** (contre-lecture, constat 12).
- **Originalité** : « inédite », avec l'antériorité discutée — témoins ajoutés (« spike-in », signal extérieur) et tests
  métamorphiques (relations entre sorties) — aucun ne rejoue l'intervention étudiée sur la condition témoin pour en faire
  la vérité de dommage. Marqués SUPPOSÉ.
- **Absente de la question et des faits** : « contrôle positif », « hors ligne », « attachement », « sensib… », « spike »
  n'y figurent pas ; « positif » n'y paraît que dans « faux positif ».
- **Longueurs servies** : 4 448 et 3 491 caractères, dans les deux fourchettes (Astra 3 353 à 4 808 ; Argon 2 677 à 5 404).
  Faux : 2 407 et 2 606, hors fourchette, rapporté par l'orchestrateur sans effet sur la lisibilité (défaut de validité
  connu, gardé pour ne pas retoucher des témoins tenus).
- Validation par les fonctions de l'orchestrateur épinglé : `valider_fiche_ideation`, garde du niveau méthode (rien).
- **Risque dit d'avance** : la sous-question 3 invite elle aussi les proposeurs à une règle de bascule ; un doublon avec une
  fiche de proposeur en course reste possible (c'est ce qui avait tiré le vrai v1 vers le bas).

## 3. Épreuve des témoins seuls

Script `scripts/epreuve_temoins_seuls_v2.py` (`8f993ba2…`, scellé ; essais `tests/test_epreuve_temoins_seuls_v2.py`,
12 passés, adaptateur simulé). **Le juge est appelé comme dans les courses** : par l'adaptateur Claude de l'orchestrateur
épinglé (`AdaptateurClaudeSDK.lancer("juge_ideation", …)`), donc avec la même consigne système, le même effort
(« medium »), le même kit d'agents, le même bac à sable (vérifié actif, `/proc` neuf), le même nombre de tours. Consigne
bâtie par `anonymiser` et `consigne_juge` ; **gabarit identique aux deux courses** jusqu'au titre « ## Les fiches »
(égalité vérifiée par programme) ; **empreinte de la consigne épinglée** : `3540c4c7dad03adfd6a92642c8141c166439c8a6c5ee2a66a10436d920aa9c44`
(24 087 caractères). Lecture par `extraire_bloc_json`, `valider_notes`, `lecture_temoins` (règle gelée).

**Commande exacte**, une seule fois, dossier courant = racine du dépôt, après le lancement du relais Claude (procédure
`docs/procedures/relais-persistants-v1.md` § 2.1, clé `RR_ANTHROPIC_API_KEY_RIGAUD`, `--plafond-usd 0.5 --modeles-permis
claude-opus-5-5`) :

    env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_seuls_v2.py

Aucun réglage libre ; dossier de sortie **imposé** `runs/epreuve-temoins-seuls-v2/`, refusé s'il existe, **quelle que soit
l'issue** de la tentative précédente. **Coût** : plafond de session 0,5 USD (`max_budget_usd` de l'adaptateur) et plafond du
relais 0,5 USD ; attendu ≈ 0,1 à 0,2 USD (relevés du juge Opus : 0,474 USD pour 16 fiches, 0,417 pour 14). **Ligne de GO** :
celle que la mère désigne (question posée à 08:10Z) ; aucun appel avant.

**Écart déclaré** : quatre fiches (les témoins) au lieu de 14 à 16, sans fiche de proposeur, donc sans doublon possible et
avec un contraste favorable aux deux bonnes. Pourquoi pas de fiches neutres : il faudrait un auteur de 10 à 12 fiches
plausibles sur ce sujet qui ne soit ni proposeur ni juge, et ces fiches deviendraient elles-mêmes un réglage de l'épreuve.
Pourquoi un seul tirage : l'épreuve est un **filtre grossier, nécessaire et non suffisant** ; l'épreuve suffisante est la
première course (règle 3). Plusieurs tirages rendraient le filtre plus strict sans le rendre suffisant.

## 4. Règle d'arrêt, écrite avant l'épreuve, fermée

1. **Code 4** (un témoin v4 manqué) : aucune course Kimi ni Carbon ; aucune retouche des témoins sans addendum neuf contre-lu
   et scellé ; compte rendu à la mère puis à Lazar.
2. **Code 3** (épreuve tentée, appel ou lecture en échec) : l'épreuve compte comme tentée ; **aucune reprise sans addendum
   neuf** ; la réponse du juge, si elle a été écrite, n'est pas lue avant que cet addendum soit scellé ; l'addendum neuf ne
   s'appuie que sur `issue.json` (statut, erreur, coût), jamais sur les notes.
3. **Code 2** (refus avant tout appel) : rien n'est parti ; corriger la cause, revérifier, relancer la même commande.
4. **Code 0** : la course Kimi part (lanceur v11, § 6, après sa contre-lecture), signalée avant départ. **La course est
   l'épreuve suffisante** : si un témoin v4 y est manqué, elle est illisible, la course suivante ne part pas, et la règle 1
   s'applique. Une course close **sans lecture des témoins** (arrêt avant les juges, aucune fiche) ne compte pas comme épreuve ;
   la course suivante peut partir, selon les règles de relance de son lanceur.
5. Les notes du juge sur les témoins se lisent après l'issue ; aucune fiche de proposeur n'est ouverte.

## 5. Budget de pensée de Carbon

Épreuves du 18 novembre (journal de la relance OD-015, OD-016, OD-020, OD-023 ; pièces `epreuve-lot-carbon-v1/`,
`epreuve-carbon-2048-v1/`, scellées) :

| mode | budget de pensée | consigne | réponse | durée | coût |
|---|---|---|---|---|---|
| synchrone, sans flux (course 1) | 8 192 | course | aucune : tunnel fermé par le mandataire réseau | 69 s | 1,53 USD comptés au pire cas |
| synchrone, sans flux (course 2) | 8 192 | course | aucune : connexion muette coupée | 300 s | 1,53 USD comptés au pire cas |
| synchrone, en flux | 8 192 | triviale | aucun morceau | > 240 s | 0,60 USD comptés au pire cas |
| synchrone, sans flux | 1 024 | triviale | juste, 0 jeton de pensée | 4,5 s | 0,0016 USD |
| synchrone, en flux | 1 024 | triviale | juste, 0 jeton de pensée | 46 s | 0,0016 USD |
| **synchrone, en flux** | **2 048** | **taille réelle** (question et faits v3, 2 414 jetons) | **rendue, 612 jetons, 0 de pensée** (texte non lu) | **13 s** | **0,045 USD** aux bornes hautes |
| par lot | 8 192 | triviale | juste, 844 jetons de pensée | 430 s vus du client (401 s au serveur) | 0,018 USD aux bornes hautes et à moitié prix ; 0,004 au prix public (2 / 10, lecture d'agent non empreintée) |

Lecture : à 8 192 en synchrone, Carbon reste muet plus de 240 à 300 s même sur une question triviale, alors qu'en lot il ne
pense que 844 jetons : **la cause n'est pas une pensée longue** ; c'est un délai d'attente propre aux appels synchrones à
budget élevé, non expliqué. À 1 024 et 2 048, Carbon ne pense pas du tout.

Options pour la troisième course Carbon :
- **(A) par lot, 8 192** : courses jumelles d'Argon ; commande et relais neufs à écrire, contre-lire ; délai d'un lot incertain
  pour une consigne de course (cible 24 h).
- **(B) synchrone en flux, 2 048** : prête et scellée (enveloppe Carbon v2 `08531295…`, lanceur v10) ; essayée à taille réelle.
  **Écart** : Carbon ne pense pas (0 jeton), Argon a pensé ; les courses ne sont pas jumelles. **Risque** : une coupure de
  plus, 1,53 USD comptés au pire cas, une relance prévue par le lanceur.

**Décision demandée à Lazar (par la mère)** : budget de pensée de Carbon pour sa troisième course. Enjeu : courses jumelles
ou course prête. Recommandation : (B) maintenant, (A) ensuite si Lazar veut des jumelles ; confiance moyenne. **Défaut sous
48 heures : (B).**

## 6. Lanceurs à écrire après la contre-lecture de cet addendum

- **v11 (Kimi)** : le v9 (`63a54d04…`) avec les témoins v4 épinglés ; rien d'autre.
- **v12 (Carbon)** : le v10 (`c3abd573…`) avec les témoins v4 ; option (B), ou l'enveloppe du lot si (A).
Chacun contre-lu (agent neuf, Opus ou Sonnet), scellé, épreuve à sec réussie, avant sa ligne de forme (la mère l'inscrit avec
l'empreinte de cet addendum).

## 7. Constats de la contre-lecture de la v1, et ce qui en est fait

| n° | constat | fait |
|---|---|---|
| 1 | paire v3 contradictoire (prédiction impossible, incopiabilité fausse, identité octet pour octet non garantie, originalité déclarée) | paire v4 neuve (§ 2) |
| 2 | rejeu possible, drapeaux libres, consigne non épinglée | dossier imposé, refus quelle que soit l'issue, aucun réglage libre, empreinte épinglée (§ 3) |
| 3 | code 3 ambigu | un seul texte : aucune reprise sans addendum neuf ; réponse non lue avant (§ 4.2) |
| 4 | plafond 0,5 sans mécanisme, ligne de GO non citée | plafond de session et du relais ; ligne demandée à la mère (§ 3) |
| 5 | juge non réglé comme en course ; quatre fiches | juge par l'adaptateur de l'orchestrateur ; écart argumenté (§ 3) |
| 6 | tableau Carbon inexact | corrigé (§ 5) |
| 7 | 2 048 jamais essayé ; risque de (B) non écrit | essayé à taille réelle ; risque écrit ; décision au format (§ 5) |
| 8 | docstring « v2 » | script v2 : témoins v4 |
| 9 | refus en code 1 | refus en code 2 |
| 10 | essai contre faux relais non versé | essais versés (12) |
| 11 | graine dite « scellée » | la paire v4 ne le dit plus |
| 12 | sous-question 2 servie de loin, risque de doublon | paire v4 sur la sous-question 3 ; risque de doublon dit (§ 2) |
| 13 | « à la lettre de la grille » | retiré |
| 14 | question de l'épreuve par lot non versée ; coût sans source ; 430 contre 401 s | question versée ; coûts sourcés ; les deux durées (§ 5) |
| 15 | empreinte de la consigne absente | inscrite (§ 3) |
| 16 | prédiction du jumeau triviale | jumeau v4 : prédiction non triviale |
| 17 | course close sans lecture des témoins | règle 4.4 |
| 18 | v3 assemblée à la main | v4 générée par programme, faux vérifiés égaux |
