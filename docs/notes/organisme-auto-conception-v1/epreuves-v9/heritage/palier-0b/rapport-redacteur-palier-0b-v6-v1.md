# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 6 (erratum) — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-19, de 23:54Z à 23:58Z environ (`date -u`) ; le texte a été produit à 23:56:31Z (journal de l'outil).
- Mandat : `mandat-redacteur-preenregistrement-palier-0b-v6-v1.md` (`e37176c7d94d513108505e69fc80ea16e83970e84b256cacfd794885cc493fca`, commit `7b16f957a34e52e6eda59603611db926dbdd3195`), empreinte vérifiée avant de commencer. Empreintes vérifiées sur disque avant d'être citées : version 5 `6230d6c3…`, relecture de la version 5 `8faf3940…` (commit `a7772202…`), outil de remplacement `391db990…`.
- Sur processeur seul : aucun tirage, aucun lancement du code versé, aucun appel à un fournisseur de modèles, aucune dépense, aucun commit, aucune poussée, aucune écriture dans le dépôt, aucun réseau. **Aucun refus d'outil.** Rien de lu ni de touché sous `archives-reponses-modeles/`. Aucun bloc en ligne passé à un interpréteur ; programmes lancés, par leur chemin : `scripts/verifier_environnement_agent_v1.py` (Python 3.13.18) et l'outil de remplacement.

## 1. Fichiers rendus (bloc-notes, dossier `redacteur-palier-0b-v6/`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v6.md` (181 077 octets) | `4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029` |
| `differentiel-preenregistrement-palier-0b-v5-v6.diff` (`diff -u` ; 10 lignes de la version 5 changées, 14 lignes côté version 6) | `67ce17ebbf070166ff25e149c1540a80b2716b580ca0880095114be5ac15a6a4` |
| `remplacements-preenregistrement-palier-0b-v5-v6.json` (13 remplacements exacts) | `a32c2ed7822171740244685d0af4918f843ad4afdf99375fef9316b4ef8ce2d8` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v6.md.journal-remplacements-v1.json` (journal de l'outil) | `93c126b36aee21e82a46ca8a934a60d8b607c737603d8392eac03e7e247aa2dd` |
| compagnons `.sha256` de la version 6 et du journal | écrits par l'outil |
| `rapport-redacteur-palier-0b-v6-v1.md` | à calculer par qui le verse |

La version 5 est intacte (R12 ; empreinte relue après l'opération). L'outil a tout appliqué au premier appel, sans refus ni avertissement ; chaque texte ancien trouvé une seule fois.

## 2. Les sept remplacements de la relecture (§ 4), à la lettre

| n° | passage | ligne de la version 5 |
|---|---|---|
| 1 | S8 (i) : « dans chacune des deux strates, monde source et mondes cibles » | 146 |
| 2 | garde 23, artefact : lois vraies « du monde source » | 293 |
| 3 | B2, couche statistique : fréquence d'une loi vraie selon la strate de son monde | 174 |
| 4 | hypothèse de travail (iii) : lois vraies selon leur monde | 44 |
| 5 | B1, « Comment l'audit le contrôle », (ii) : arrêt sur la forme, rapport sur le contenu | 166 |
| 6 | « Ce qui est rapporté » : quinze exactitudes | 322 |
| 7 | réserve 7 : « Versions 4 et 5 », huit fréquences | 446 |

Les textes anciens et neufs sont copiés du § 4 de la relecture, lu dans le fichier.

## 3. La tenue (six remplacements)

Titre (v6) ; statut (version 6, erratum, remplace la version 5) ; heure ; ligne « Mandat de la version 6 » ajoutée ; ligne « relecture courte de la version 5 » ajoutée aux documents qui font foi ; un alinéa à la fin de l'annexe G, qui inscrit les sept remplacements.

## 4. Écarts et points à relire

1. **Heure du mandat.** Le mandat se dit donné « le 2026-11-20 vers 00:05Z » ; son commit est de 23:54:14Z le 19, et l'horloge de la machine disait 23:54Z à mon début. Je n'ai pas repris cette heure dans la version 6.
2. **Lignes d'accord non relues.** Les lignes `GO-2026-11-19-84` et `-93` sont citées d'après le mandat ; je ne les ai pas relues sur `main`. La version 6 le dit.
3. **Tenue bornée à la lettre du mandat.** La ligne du commit du code, l'étape 1 de l'ordre des opérations et la section « Contre-lecture » disent encore « cette version 5 » et sa relecture courte « à faire ». Je ne les ai pas touchées ; l'alinéa de l'annexe G le signale. La mère peut vouloir un mot de plus avant le scellement.
4. **Le compte de la relecture.** Son verdict dit « trois ferment la question, quatre alignent » ; son § 4 en donne quatre pour la question (n° 1 à 4) et trois d'alignement (n° 5 à 7). L'alinéa de l'annexe G suit le § 4 et ne reprend pas ce compte. Sans effet sur les sept textes.
5. **Annexe G : un alinéa, non une ligne de table.** Le titre de l'annexe (« Erratum de la version 5 ») n'est pas changé.
6. **L'heure écrite dans la version 6** est « vers 23:57Z » ; l'outil a écrit à 23:56:31Z.
7. **Non faits** : le validateur du gabarit n'a pas été relancé ; les listes « Ne pas écrire » n'ont pas été revérifiées par programme. Mes ajouts ne portent aucun identifiant de modèle.

## 5. Reste à faire, hors de mon mandat

Verser les fichiers et ce rapport ; coup d'œil du même contre-lecteur sur le différentiel v5 → v6 ; puis mandat du développeur neuf.
