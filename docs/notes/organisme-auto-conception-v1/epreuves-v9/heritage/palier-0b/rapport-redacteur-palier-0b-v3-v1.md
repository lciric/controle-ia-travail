# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 3 (erratum) — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Rendu le 2026-11-19 vers 22:04Z (`date -u`), le texte ayant été produit à 22:03Z.
- Mandat : `mandat-redacteur-preenregistrement-palier-0b-v3-v1.md` (`084207ec830f3b438f54633882611fada4ea7301411ae8dc5be60eb58a281de8`), empreinte vérifiée avant de commencer. Empreintes vérifiées sur disque : version 2 `0a80a1adac833a3858754855f09bc420e569f2aeeb8c62e7cb0630bd4677becf`, vérification `9d18eab3f578258d04f1295e54a9ddc35261e7e66114ba56d0248f9f0b4eafef`, contre-lecture `127aa59f…`, rapport de la version 2 `9839b15d…`, queue `90ea7fda…`, différentiel v1 → v2 `20e4011e…`, calcul de la version 2 `470f3385…` et sa sortie `b97ed1f1…` ; tous les compagnons `.sha256` du dossier `palier-0b/` sont égaux. Ligne `GO-2026-11-19-81` lue sur `main` au commit `d4449d3273f3820b71e78e9e9adc44674f6ea31b` (`registres/go.md`, `78efe8782883f4de91fa6d06d84d1b93498f8bb3ee5a70e111ffc2d9cd8c1275`).
- Sur processeur seul : aucun tirage, aucun appel à un fournisseur de modèles, aucune dépense, aucun commit, aucune poussée, aucune écriture dans le dépôt ; réseau : un seul `git fetch` de `main`. **Aucun refus d'outil.** Rien de lu ni de touché sous `archives-reponses-modeles/`.

## 1. Fichiers rendus (bloc-notes, dossier `redacteur-palier-0b-v3/`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v3.md` | `a4535a67e99cd0babfb580a731868c0670ffab55be803b8aa7979f3ded84ebc6` |
| `differentiel-preenregistrement-palier-0b-v2-v3.diff` (15 lignes de la version 2 changées, 2 blocs ajoutés) | `42253287e96320681fa4ed89e56898b2ddd42f7a336c08ce3e28b30c09baf4b4` |
| `appliquer_corrections_palier_0b_v3.py` (16 remplacements exacts sur la version 2, chacun trouvé une seule fois, puis ajout d'une section à l'annexe E ; arguments : version 2, cible, heure de fin `22:03Z`) | `438a2a0c45ecb0789d3c983ff51dc08b601183ba3603e67f2cd6cf16136a10ad` |
| `rapport-redacteur-palier-0b-v3-v1.md` | à calculer par qui le verse |

La version 2 est intacte (R12). La version 3 passe le validateur du gabarit à la même remarque près que la version 2, voulue : la section « Contre-lecture » n'a pas encore ses deux empreintes.

## 2. Les quatre corrections

| n° | où, dans la version 3 | comment |
|---|---|---|
| 1 — engagement seul aux paliers payants | B4, point (iv) ; réserve 16 ; valeurs gelées, ligne « ce que l'expérimentateur reçoit du champ `tentative` » | mots de la vérification (§ 6) ; « ligne `GO-…` à inscrire » devient « ligne `GO-2026-11-19-81` » |
| 2 — seuil de « beaucoup plus de sources » | réserve 14 ; valeurs gelées, ligne du seuil | mots de la vérification : proposition du rédacteur, accordée par Lazar, option (a), ligne `GO-2026-11-19-81` ; chiffres du seuil inchangés |
| 3 — paires sur les lois distinctes | B7, ligne du lecteur réglé pour l'héritage ; « Le repli du point 7 » | mots de la vérification |
| 4 — écart-type entre jumelles des proposeurs sans réglage | B7, « Réglage par programme » ; table des critères, C1 (« sur 72 cases ») | phrase de la vérification reprise à l'octet ; voir les écarts ci-dessous |

Sort des quatre corrections : annexe E, section « Erratum de la version 3 ».

**Calcul.** Aucune correction ne touche un calcul : le calcul de la version 2 n'est ni changé ni rejoué, aucun calcul neuf n'est écrit. Le « 72 cases » est déjà dans la sortie de la version 2.

## 3. Écarts et choix à relire

1. **Place de la phrase de la correction 4.** La vérification dit « Après « Pour chaque proposeur réglable, chaque dose et chaque taille réduite visée, », ajouter avant le paragraphe » : pris à la lettre, cela coupe une phrase en deux. Je l'ai placée après la fin de cette phrase (« … celle du contraste de la tenue pour τ. »), dans le même paragraphe.
2. **Une phrase de plus à la correction 4**, hors du texte exact du § 6 : « Cet écart-type sert au rapport d'écarts-types de la famille A (M9), à M8 en taille réduite et à M14. » Le mandat nomme ces usages ; les mots sont ceux de la vérification. À rayer si le contre-lecteur la juge de trop. M9 n'est pas changée.
3. **Changements hors des quatre corrections, de tenue du texte seulement** : en-tête (titre « v3 », phrase de version, heure, mandat de la version 3 et ligne `GO-2026-11-19-81`, vérification citée) ; section « Contre-lecture » (vérification inscrite, relecture de l'erratum dite à faire, fichiers à donner). Sans eux la version 3 se dirait version 2 et dirait non faite une vérification faite.
4. **Le titre de l'annexe E** reste « Différentiel de la version 1 à la version 2 » ; la section de l'erratum y est ajoutée à la fin, comme le mandat le demande.
5. `main` a avancé pendant le travail (de `d4449d327` à `6874e0d4d`) ; la ligne est citée au commit que donne le mandat.

## 4. Reste à faire, hors de mon mandat

Relecture du seul erratum par le même contre-lecteur ; versement avec compagnons `.sha256` ; erratum du commit du code avant tout scellement.
