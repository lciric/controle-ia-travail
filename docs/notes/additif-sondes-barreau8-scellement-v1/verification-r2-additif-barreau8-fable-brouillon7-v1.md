# Vérification R2 finale — Brouillon 7 de Fable de l'additif 1 aux sondes du barreau 8 (v1)

- **Rôle** : contre-lecteur neuf indépendant (règle R2, sous `GO-2026-11-23-33` et `GO-2026-11-23-36`, conversation `1d691bacd476e88383a7f68e53c90b67`).
- **Date et heure (UTC)** : `2026-11-24T03:53:14Z` (`date -u`).
- **Branche et commit inspectés (sans checkout ni modification du dépôt)** : `origin/prep/additif-sondes-barreau8-scellement-v1`, commit `7cdedeca00be0533991891f8f48fe4b7c91bb325`.
- **État du dépôt principal** : inchangé (`git status --porcelain` vide) ; répertoire temporaire `/tmp/verif-additif-b8-fable` détruit après rejeu (`PYTHONDONTWRITEBYTECODE=1`).

---

## Verdict

**`SCELLABLE EN L'ÉTAT APRÈS REMPLISSAGE DES MARQUEURS PAR LA MÈRE`**

Pièce vérifiée : `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (623 lignes, 190 354 octets, SHA-256 `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`).

---

## 1. Empreintes SHA-256 recalculées et vérification des compagnons

Les **3 fichiers compagnons `.sha256`** du commit `7cdedeca00be0533991891f8f48fe4b7c91bb325` sont **3/3 conformes**.

| pièce (dans `7cdedeca0`) | SHA-256 recalculé | taille / lignes | compagnon `.sha256` |
|---|---|---|---|
| `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` | `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b` | 190 354 o / 623 l. | conforme |
| `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md` | `f9379270cddf80f25eb35f3079e03f0b423a6932e53075f0f592de53de857714` | 49 803 o / 271 l. | conforme |
| `docs/notes/additif-sondes-barreau8-scellement-v1/corrections-brouillon6-vers-brouillon7-v1.py` | `3b46c67a7fa6b839e66a3d2f8b96faa580de09cc42e9dde6091ea4a7e8bca2b3` | 38 694 o / 219 l. | conforme |
| `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon6.md` (entrée) | `bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e` | 171 566 o / 586 l. | vérifié |
| `src/controle_ia/prereg.py` (identique sur `HEAD` et sur la branche) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` | 3 086 o / 76 l. | — |
| `docs/decisions/decision-N-053-v1.md` (cité remarque 19) | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | vérifié | — |

---

## 2. Rejeu par programme (`brouillon 6 -> brouillon 7`)

Exécuté dans `/tmp/verif-additif-b8-fable` (puis détruit) avec `PYTHONDONTWRITEBYTECODE=1` :

- Commande rejouée : `corrections-brouillon6-vers-brouillon7-v1.py` (`3b46c67a…`) sur `brouillon6.md` (`bf107842…`).
- Sortie standard : `écrit /tmp/verif-additif-b8-fable/b7_rejoue.md 180614 caractères ; marqueurs restants : 7`.
- **Identité stricte octet pour octet** avec le brouillon 7 du commit `7cdedeca0` :
  - `b7.md` (`7cdedeca0`) : `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`
  - `b7_rejoue.md` : `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`
  - Égalité binaire : **`True`**.

---

## 3. Contrôle exhaustif des 22 remarques d'Opus (`f9379270…`)

Les **22 remarques** (1 bloquante, 12 à corriger, 9 mineures) ont été vérifiées **directement dans le texte cible** du brouillon 7 (pas seulement dans la table récapitulative de tête) : **22/22 traitées et conformes**, avec contrôle négatif des motifs résiduels (0 occurrence résiduelle hors tables historiques des brouillons précédents).

| # | gravité | objet de la remarque d'Opus (`f9379270…`) | vérification dans `brouillon7.md` | statut |
|---|---|---|---|---|
| 1 | **bloquante** | Rappel de la cascade nul par construction à T=64, E=1, A=10 | « Seuil au plafond (déclaré) » ajouté en LD-2 (`non définis : seuil au plafond`, aire gardée), B8-A2, NL-9 et essais de « Codes » | **Traité** |
| 2 | à corriger | « À taux égal » : `(k+1)/(n+1)`, ex aequo, citation P-066 | Source P-066 précisée, limites `(k+1)/(n+1)` et ex aequo récrites, part d'alertes réalisée de `h` avec `n` et `k` exigée pour chaque lecteur, NL-9 complété | **Traité** |
| 3 | à corriger | LD-0 (b) : jeu sous S1/S3/S4/L5, capture d'exception | Jouées uniquement hors S1, S3, S4, L5 (jouées sous S2, S5) ; exception capturée et écrite « échec » sans arrêter l'étape (h) ; deux essais ajoutés dans « Codes » | **Traité** |
| 4 | à corriger | Règle R4 dans le bloc descriptif et déclenchement audit | Point `(k)` ajouté à LD-0 (marquage « trop propre : réserve (règle R4) » sans effet, sort du bloc sous AU-a, auditeur ne lit pas le bloc) ; ligne audit précisée (déclencheurs d1 à d4 seuls) | **Traité** |
| 5 | à corriger | Liste fermée des passages touchés incomplète | Quatre lignes ajoutées avant `tout le reste` (« Ce que l'on perd… » / plan / conformité ; « Hypothèse » ; marquage / « Autres combinaisons » ; conditions des rôles) | **Traité** |
| 6 | à corriger | Contradiction NL-11 sur `GO-2026-11-18-55` / `R-3435` | Les deux lectures sont posées dans NL-11 et « Activité interne » ; la session mère tranche d'après `R-3435` | **Traité** |
| 7 | à corriger | Quatre phrases héritées d'avant le scellement après la course | Toutes quatre récrites (L179, L541, L558, NL-7 caduc remplacé par NL-0) | **Traité** |
| 8 | à corriger | Exposition par erreur non datée et absente de NL-6 | Datée (`2026-11-23` à `18:17Z`, avant les changements 8 à 13 du brouillon 6) ; NL-6, NL-0 et « Rien n'a été réglé » complétés | **Traité** |
| 9 | à corriger | Provenance des demandes (brouillons 5–7) hors bornes dures | Borne dure `(b4)` ajoutée partout (« quatre bornes dures », `(b1) à (b4)` dans AD-3, forme AD-3, NL-0, liste d'arrêt ligne 19) ; 0 occurrence résiduelle hors tables historiques L62/L79 | **Traité** |
| 10 | à corriger | « Première sortie » : tous lancements de l'étalonnage compris | Ajouté dans « Quand l'additif doit être scellé », forme AD-3 (`nombre de lancements de l'étalonnage`) et réserve dans « Rien n'a été réglé » | **Traité** |
| 11 | à corriger | D-6 : comparaison par sections ambiguë en multi-pièces | Découpe de section, condition « identique » sur toutes les pièces et format `<rang>:<numéro>` du champ `lieu` fixés | **Traité** |
| 12 | à corriger | « Ce que tout lecteur apprend » incomplet | Trois faits structurels ajoutés en L540 (ordre en trois pièces, aucune activité interne enregistrée, heures des sorties et fin) | **Traité** |
| 13 | à corriger | Course figée dès sa fin et non dès le scellement | Remplacé par « après la fin de la course lue » en `(c4)` et en liste d'arrêt ligne 29 | **Traité** |
| 14 | mineure | D-15 : clause « aucun chiffre » excluait `commit_lancement` | `commit_lancement` ajouté à la liste des exceptions | **Traité** |
| 15 | mineure | AD-3 : heure du scellement impossible dans le texte haché | Remplacé dans la forme AD-3 par `attestation écrite à : <heure, date -u>` + renvoi à la ligne `SCELLEMENT-ADDITIF-1-SONDES-IIB` | **Traité** |
| 16 | mineure | Cinq points laissés au code (LD-0 e, f, g ; LD-1) | Méthode des quantiles (`intervalle_blocs`) et multiplicité (e, LD-1), plancher pour les aires seulement (f), clés `<jeu>` de rappel, parts d'alertes ponctuelles et clés LD-4 (g) fixés | **Traité** |
| 17 | mineure | LD-4 : contrôle à l'ouverture incomplet | Empreinte au mandat du lecteur, `scores.sha256`, `joue_par`, `numpy.load(..., allow_pickle=False)` et ordre du tableau `surveillants` ajoutés | **Traité** |
| 18 | mineure | Deux formulations contre LD-0 (LD-5 et B8-A1) | Table « par mode » dans `descriptif_additif_1` recopiée par le juge ; « supérieure à 0,5 » et « supérieur à la part d'alertes » | **Traité** |
| 19 | mineure | Provenance de l'en-tête (`deecb4c7`, `18:18Z`, `GO-17`, `N-053`, datation b1) | Tous cinq portés et vérifiés contre `git show` (`f74a6829…` à `18:18:16Z`, `bc271120…`, `c947f5c3…`, `ce2e1a03…`, `decision-N-053-v1.md` `2204256d…`) | **Traité** |
| 20 | mineure | Lieux non nommés dans les deux tables de changements | Ajoutés dans les tables b4→b5 et b5→b6 (`NL-1`, « Ce que chaque côté fournit », « Plan d'analyse » point 8, « Passages touchés », « Où chaque point ») | **Traité** |
| 21 | mineure | NO-1 / RP-7 : condition de retour de Fable remplie à la lettre | Reconnu explicitement dans la déclaration de RP-7 avec motif de maintien de l'option (a) (défauts systématiques) | **Traité** |
| 22 | mineure | D-6 : syntaxe de la clé `ordre` | Récrite proprement à quatre clés (`chemin`, `sha256`, `scelle`, `pieces`) | **Traité** |

---

## 4. Validation `src/controle_ia/prereg.py` et liste exacte des marqueurs à remplir par la mère

### Résultat du validateur `src/controle_ia/prereg.py` (`3b2e3ee5…`)

- Toutes les **8 sections exigées** par `prereg.SECTIONS` (`Hypothèse`, `Prédiction chiffrée et signe attendu`, `Métrique`, `Seuil`, `Plan d'analyse`, `Critères de lecture gelés`, `Liste d'arrêt`, `Contre-lecture`) sont présentes et non vides.
- **0 marqueur de gabarit `<<...>>`** (`prereg.GABARIT`) dans tout le fichier.
- Sur le brouillon 7 brut : `prereg.problemes(...)` renvoie uniquement `['section vide ou à remplir : Contre-lecture']` (et signale les 6 marqueurs `AD-1..AD-6` hors sections dès que `Contre-lecture` est remplie sans eux).
- **Simulation de remplissage** (copie temporaire dans `/tmp/verif-additif-b8-fable`, sans toucher le dépôt) : en remplaçant uniquement les **7 occurrences de `À REMPLIR`** (`AD-1` à `AD-6` et `Contre-lecture 2` avec deux empreintes SHA-256 à 64 caractères hexadécimaux), `prereg.problemes(...)` retourne **`[]`** (0 problème — conforme à `R1`/`R2`).

### Liste exacte des lignes à remplir / compléter par la session mère avant scellement

**A. Les 7 occurrences uniques du marqueur `À REMPLIR` (seuls marqueurs d'attente du fichier) :**

1. **Ligne 172 — Champ `AD-1`** : accord de Lazar sur l'écart et sur les options des nœuds `NL-0` à `NL-6`, `NL-9` et `NL-11` (identifiant de la ligne du registre des accords + option choisie par nœud).
2. **Ligne 173 — Champ `AD-2`** : table des expositions du côté des moniteurs complétée + attestation qu'aucun agent nommé dans cette table ne figure parmi les exclus de l'ordre neuf.
3. **Ligne 174 — Champ `AD-3`** : attestation de la session mère avec heure (`date -u`), à rédiger **selon la forme exacte de la ligne 568** (« Forme du champ AD-3 » : `première sortie de l'étalonnage : <heure> (tous lancements compris ; nombre de lancements de l'étalonnage : <nombre>) ; première sortie de la course : <heure> ; fin de la course : <heure> ; attestation écrite à : <heure, date -u> ; lectures du dommage et de la diffusion jouées avant le scellement : <oui ou non> ; bornes (b1), (b2), (b3) et (b4) tenues : oui ; source de (b1) : <registre « qui a lu quoi », chemin et empreinte> ; Lazar avait-il vu une sortie avant ses mots : <oui ou non>`). *(Note mineure : le libellé descriptif de la colonne centrale de la ligne 174 mentionne encore « et du scellement », mais la forme normative de la ligne 568 précise bien que l'heure du scellement n'y figure pas et relève de la ligne `SCELLEMENT-ADDITIF-1-SONDES-IIB`.)*
4. **Ligne 175 — Champ `AD-4`** : réponse à la question `E-1` connue au scellement (`oui`, `non` ou `inconnue`), avec chemin et empreinte de la pièce d'attestation de l'ordre si elle existe.
5. **Ligne 176 — Champ `AD-5`** : renvoi vers la section « Contre-lecture » remplie (`À REMPLIR (dans la section)` à remplacer par l'état rempli).
6. **Ligne 177 — Champ `AD-6`** : identifiant de la ligne de calcul du registre des accords sous laquelle la course lue a été lancée.
7. **Ligne 619 — Section « Contre-lecture », entrée `Contre-lecture 2 (finale, texte rempli)`** : remplacer `À REMPLIR` par l'identifiant du contre-lecteur, les empreintes SHA-256 à 64 caractères du brouillon 6 relu (`bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e`), du rapport de contre-lecture 2 (`f9379270cddf80f25eb35f3079e03f0b423a6932e53075f0f592de53de857714`), du brouillon 7 vérifié (`eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`) et du présent rapport de vérification finale (plus mention explicite si la vérification des corrections est portée par ce contre-lecteur neuf indépendant sous `GO-2026-11-23-33` plutôt que par l'agent Opus du brouillon 6).

**B. Ligne de la table des expositions autorisée par la règle du scellement (ligne 136) au titre de `AD-2` :**

- **Ligne 536** (et ajout éventuel de la ligne du présent contre-lecteur neuf dans le tableau des lignes 528–537) : `| conductrice du côté des moniteurs ; développeurs de la passe, de la lecture et du programme de report ; contre-lecteurs des codes ; session mère | complété par la session mère (AD-2) | complété (AD-2) | complété (AD-2) |`.

---

## 5. Vérification mécanique de `manifeste.graines` sur toutes les clés

Testée par programme via `.venv/bin/python3` (`numpy 2.4.6`, `PYTHONDONTWRITEBYTECODE=1`) sur `src/controle_ia/manifeste.py` avec l'entropie racine `F-3 = 149333987590752343984325077404464904184` du texte scellé `prereg/lecture-sondes-barreau8-v1.md` (ligne 76) :

- **Toutes les familles de clés couvertes** :
  - Texte scellé + RP-9 : `puissance`, `repetabilite-passe`, `injection-adaptateurs`, `intervalle/<sonde>/<jeu>`, `jumeau/<sonde>/<jeu>`, `dose/<sonde>` (pour 1 couple) / `dose/<sonde>/<haute>-moins-<basse>` (pour ≥ 2 couples), `placebo/<sonde>/<jeu>`, `diagnostic-moyenne/<sonde>/<jeu>`, `descriptif/<sonde>/<jeu>`, `sain/<sonde>`, `artefact/<sonde>`, `alignement/<sonde>`, `sain-2/<sonde>`, `artefact-2/<sonde>`, `alignement-2/<sonde>`.
  - Additif 1 (LD-0, point (g)) :
    - `additif-1/jumeau-honnete/<aire|rappel>/<sonde>/<jeu>`
    - `additif-1/episode/<maximum|dernier-etat|cascade>/<aire|rappel>/<sonde>/<jeu>`
    - `additif-1/episode/difference/<dernier-etat|cascade>/<sonde>/<jeu>`
    - `additif-1/reference/<aire|rappel>/<surveillant>/<sonde>/<jeu>`
- **Résultats du test exhaustif** :
  - **Configuration version 6 (`m = 2`, `H, B50, B100, TJ100`, 3 sondes c15 + 6 sondes descriptives c7/c23 + 2 surveillants)** : `99` clés scellées + `162` clés additif 1 = **`261` clés** — **0 doublon**, **0 collision de `spawn_key` (`cle_de_tache`)**, **0 collision d'`etat_controle`**, **100 % d'invariance** des 99 graines du texte scellé, **100 % de reconstruction déterministe** via `manifeste.generateur(...)`.
  - **Configuration généralisée (`m = 3`, `H, B25, B50, B100, TJ100`, 3 couples de doses)** : `135` clés scellées + `222` clés additif 1 = **`357` clés** — **0 doublon**, **0 collision de `spawn_key`**, **0 collision d'`etat_controle`**, **100 % d'invariance** des 135 graines scellées, **100 % de reconstruction déterministe**.
  - **Test négatif** : `manifeste.graines` lève bien `GardeArret` dès qu'une clé est dupliquée.

---

## Ligne « qui a lu quoi »

- **Agent** : sous-agent contre-lecteur neuf indépendant `1d691bacd476e88383a7f68e53c90b67` (`2026-11-24T03:53:14Z`, sous `GO-2026-11-23-33` et `GO-2026-11-23-36`).
- **Lu pour cette vérification** : par `git show` sur `origin/prep/additif-sondes-barreau8-scellement-v1` (`7cdedeca0`) : `docs/notes/additif-sondes-barreau8-scellement-v1/contre-lecture-additif-1-brouillon6-opus-v1.md`, `docs/notes/additif-sondes-barreau8-scellement-v1/corrections-brouillon6-vers-brouillon7-v1.py`, `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon6.md`, `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`, et leurs compagnons `.sha256` ; lignes relatives aux graines et à F-3 de `prereg/lecture-sondes-barreau8-v1.md` ; `src/controle_ia/prereg.py` ; `src/controle_ia/manifeste.py` ; empreinte seule de `docs/decisions/decision-N-053-v1.md` ; métadonnées de commits `ce2e1a03…`, `f74a6829…`, `bc271120…`, `c947f5c3…`.
- **Non ouvert** : aucun fichier sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, ni aucune consigne privée, conception ou ordre de la course du saboteur, ni `registres/etat.md`. Aucun résultat lu.
