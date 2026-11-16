# Contre-lecture, tour 2, de l'addendum de relance de l'idée 1.1 (brouillon 2) — v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-1-v1-brouillon2.md`
  (`566304ede89c8aab86682bd9a7602e20b307e97fadce2071ea46ffed87a3ee4a`, égale à son compagnon ; `scellement verifier` : OK ; 844 lignes).
- **Lecteur** : modèle C, lecteur neuf (R2) ; je n'ai écrit ni la pièce, ni le rapport du tour 1, ni [T], ni [AE], ni le code, ni l'étape 0.
  Rédacteur de la pièce et des corrections : modèle A (selon la consigne du tour).
- **Dates (UTC, `date -u`)** : 2026-11-16, de 20:37Z à 20:39Z. Dépôt : `main`, tête `a6bc9938`.
- **Fait** : `diff` brouillon 1 / brouillon 2 ; relecture du rapport du tour 1 (empreinte `aaacb415…` vérifiée, égale) ; lecture du programme
  d'application `appliquer-corrections-…-brouillon2.py` (compagnon : OK) ; contrôle des renvois de code de c-1 et c-3 ; rejeu du programme de l'annexe A.
- **Non fait** : aucun fichier du run invalide ouvert ; rien écrit dans la copie ; ni jeu, ni `pytest`, ni réseau, ni clone ; aucun `env`.
- **Verdict : « corrections »** — 0 majeure, 1 mineure (un couple exigé, d-1), plus deux remarques facultatives. La conception n'est pas en cause.

## 1. Les quatre corrections du tour 1 et le différentiel

`diff` entre brouillon 1 et brouillon 2 : six zones seulement, rien d'autre.

- **c-1** (4.2, dernier alinéa) : appliqué mot pour mot ; renvoi vérifié, `rec["temps_s"]` est à `banc_idee_1_1_v2.py` l. 694.
- **c-2** (§ 3, dernière puce) : appliqué mot pour mot.
- **c-3** (4.2, première puce) : appliqué, à un renvoi près : « [T] l. 492 » devient « [T] l. 492-493 ». Écart déclaré dans § 7 et **justifié** :
  dans [T], « essai » est en fin de l. 492 et `(98, r)` est l. 493 ; `cle=(98, r)` est bien à `etape0_idee_1_1_v5.py` l. 174 ; les prolongements
  `0` et `1` sont bien aux l. 481 et 636 du banc. Accepté.
- **c-4** (4.10, lieu (ii)) : appliqué mot pour mot ; D5 = GO-2026-11-16-07 (`registres/go.md` l. 348) : exact.
- **Reste du différentiel** : l'en-tête (nouvelle puce « Version : brouillon 2 », ligne « Statut et lieu » passée à « brouillon 2 ») et la
  section 7, remplacée par le traitement du tour 1. Rien d'autre, comme le dit l'en-tête. Le programme d'application tire les couples du rapport
  et refuse le chevauchement et la ré-écriture ; zéro ligne au format du lanceur et zéro ligne commençant par 64 caractères hexadécimaux (mon recompte :
  0 et 0). Le § 7 rapporte fidèlement le rapport du tour 1 (0 majeure, 4 mineures, 4 facultatives ; heures ; empreintes).
- **Rien d'autre à signaler** dans les passages touchés ; les corrections n'ont dérangé aucun autre passage.

## 2. Vérifications refaites

- **Programme et sortie de l'annexe A** : extraits de la pièce, empreintes `b9664f76…` et `f457df14…` égales à celles déclarées. Rejeu de 20:38:02Z à
  20:38:05Z (`python3 -I -B`, code de sortie 0, sortie d'erreur vide) : sortie identique à la recopie, aux trois seules lignes d'heure près (début, fin,
  `/proc/uptime`). Les chiffres de l'état du run invalide (234 fichiers, compagnons, absence de `sortie.json` et `arret.json`, listes d'empreintes, 46 sur 46) sont donc
  inchangés.
- **Hygiène** : aucun identifiant de modèle (recherche de claude, opus, sonnet, fable, haiku, gpt : rien) ; lettres A et C seulement ; aucune ligne au format du lanceur.
- Les points 1 à 6 du tour 1 (cause, preuves, mêmes tirages, conditions, consigne de tâche, deux lieux sous c-4) restent conformes ; c-1, c-2, c-3 comblent les précisions demandées.

## 3. Correction exigée (mineure)

**d-1 — En-tête, nouvelle puce « Version » : la lettre et le statut du rédacteur des corrections ne sont pas ceux du tour.** La puce dit « rédacteur neuf, lettre C … qui
n'a écrit ni le brouillon 1 ». Or, d'après la consigne du tour 2, les corrections ont été faites par le modèle A, qui a écrit le brouillon 1 : « lettre C » est fausse, et « neuf »
et « n'a écrit ni le brouillon 1 » aussi. La lettre C est celle du lecteur du tour 1 ; la confusion mêle une lettre de rédacteur et une de lecteur. À corriger (l'« ancien » figure une
fois ; vérifié par `grep -cF` : 1) :

- ancien : `  rédacteur neuf, lettre C, sous-agent de la session mère, qui n'a écrit ni le brouillon 1, ni son rapport de`
- nouveau : `  rédacteur, lettre A (le modèle du brouillon 1), sous-agent de la session mère, qui n'a écrit ni son rapport de`

Si la mère sait que les corrections ont en fait été appliquées par un rédacteur de lettre C, la phrase tient et il n'y a rien à changer : à confirmer par la mère. Le
programme d'application (`appliquer-corrections-…-brouillon2.py`, scellé) porte le même texte dans `EN_TETE_N` : une correction de la pièce par un brouillon 3 le rendrait
incohérent avec lui, ce qu'il faut ou bien signaler dans la pièce, ou bien corriger par un programme neuf (R12).

## 4. Remarques facultatives (la pièce peut être scellée sans, si d-1 est réglé)

- **g-1** : après la correction, « ce brouillon » (§ 3, « Par le rédacteur de ce brouillon », § 8) désigne le brouillon 1 ; le § 8 le dit déjà (« reste celle du rédacteur du brouillon 1 »).
  À nettoyer à la recopie sous `prereg/`.
- **g-2** : les remarques f-1 à f-4 du tour 1 restent non appliquées ; choix déclaré et recevable.

## 5. Points pour la mère

1. **Lettre du rédacteur des corrections (d-1)** : à confirmer ou à corriger avant la recopie sous `prereg/`.
2. **Écart à un texte scellé (lieu (ii))** : une machine louée est un écart à [T] l. 629 et 660 ; D7 est à demander à Lazar en toutes lettres avec la question de R-3010. Sans son mot, aucune machine
   louée ne part (c-4, appliquée). Le lieu (i) n'en demande aucun.
3. **`--reprendre` reste accepté par le code** dans la copie du run invalide ; seule la règle écrite l'interdit : l'opérateur ne le passe jamais.
4. **Risque du lieu (i)** : une reprise imposée malgré une tâche active a déjà eu lieu (20:11Z) ; 15,7 heures de jeu s'y exposent de nouveau. Égalité au bit près non garantie sur un autre processeur (limite déclarée, sans effet sur la validité).
5. **À la recopie** : recompter les lignes au format du lanceur (attendu 0) et recalculer les empreintes du § 8 ; compléter la section de contre-lecture avec ce tour (modèle C, verdict « corrections », 0 majeure, 1 mineure).

## 6. Incidents et gestes de ma main

Aucun incident. Gestes : `diff`, `sha256sum`, `scellement verifier` de la pièce, `sha256sum -c` du programme d'application, `grep`/`sed` de lecture sur la pièce, [T], le code et `go.md`, extraction et rejeu du programme de
l'annexe A dans le bloc-notes de la session. Aucun fichier existant modifié, aucun commit ; rien d'autre écrit que ce rapport et le bloc-notes.
