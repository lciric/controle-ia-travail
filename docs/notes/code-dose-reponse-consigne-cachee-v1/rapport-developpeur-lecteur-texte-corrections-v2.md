# Rapport du sous-agent développeur : corrections v2 du lecteur du texte

Pièce versée à l'identique du rapport rendu par le sous-agent (Opus 5.5), après la contre-lecture 1.

---

Les corrections CL-01 à CL-05 et CL-07 sont faites dans trois fichiers v2 neufs, tous scellés. La suite v2 passe en entier : 128 essais en 149 s, dont le mode réel de bout en bout par le lanceur. Chacun des quatre mutants du contre-lecteur fait maintenant échouer des essais, seul comme ensemble. La v1 (commit adb6c6b2) et le fabricant factice v1 ne sont pas touchés : leurs empreintes se vérifient. Rien n'est committé ni poussé.

## Fichiers écrits (neufs, avec leur `.sha256`)
| Fichier | Empreinte |
|---|---|
| `/home/user/controle-ia-travail/scripts/lecteur_texte_dose_reponse_v2.py` | `6cf3a1ac65ed2b656db32f2a19ae2bbb27635e176b8f95530223cb0316ee75d8` |
| `/home/user/controle-ia-travail/scripts/lancer_lecteur_texte_dose_reponse_v2.sh` | `0521f980f0e24ec88c07f79e67c4cf36ff2b63369d1f8e3b16eab30b991268d8` |
| `/home/user/controle-ia-travail/tests/test_lecteur_texte_dose_reponse_v2.py` | `2e8b7c46e245e0be432fa2866efeaa308049ca57381bf181028b16add0a5a16c` |

- Le lanceur v2 ne diffère du v1 que par le module joué.
- Le fabricant factice `scripts/fabrique_factice_lecteur_texte_dose_reponse_v1.py` reste tel quel ; la pièce v2 le cite dans `FICHIERS_ESSAIS`.
- La pièce et les essais portent en tête une note de version qui liste les changements et renvoie aux constats.
- Le calcul de T0.6 n'a pas changé : la garde d'identité avec la pièce de T0.6 reste et passe.

## Changement fait, par constat

**CL-01 (coût non fini)** — fonction `lire_mesures`, nouvelle fonction `_flottant_non_fini`.
- Un `cout` flottant non fini (`Infinity`, `-Infinity` ou `NaN` dans `mesures.jsonl`) est lu illisible et stocké `nan`, comme `null`.
- Tout autre type reste refusé : chaîne, booléen, liste, objet.
- Essais : un cas sain avec les trois valeurs écrites telles quelles dans le fichier (vérifiées lues `nan` et illisibles), et quatre artefacts : `"12"`, `True`, `[12.0]`, `{"v": 1}`.

**CL-02 (mode jouet sur un lancement réel)** — fonction `lire_lancement`.
- En mode jouet, un manifeste de lancement `decisif` vrai, ou dont `config.mode` vaut `"reel"`, est refusé.
- Essais : cas sain (lancement jouet) ; artefacts : lancement de forme réelle, refusé à la fois par `lire_lancement` et par `executer` sans rien écrire ; puis chacun des deux signes seul.

**CL-03 (`--registre`)** — fonction `executer`.
- En mode réel, `--registre` n'est permis qu'égal à `registres/scellements-v1.md`.
- Essais : un autre registre est refusé ; le registre par défaut passe cette garde et s'arrête ensuite sur la garde des fils de calcul.

**CL-04 (une garde, un cas sain, un artefact)** — essais neufs seulement :
- **Audit** : 14 cas paramétrés, bornes comprises.
  - Déclencheurs (1) et (2), et leurs cas contraires : témoin positif en échec, intensité 10 « non calculable ».
  - (4) : aire 0,99 déclenche, 0,9899 non.
  - (5) : plancher 0,61 déclenche, 0,60 non ; une base non calculable est ignorée.
  - (6) : écart +0,11 et baisse de l'honnête déclenchent, +0,09 non ; un écart sur un témoin est ignoré.
  - Échantillon par graine reproductible.
- **Plis** (`plis_imposes`) : plis égaux acceptés ; une tâche basculée et une autre graine refusées.
- **Plis mêlés et centres** : `noter_indices` refuse le pli d'apprentissage en lecture et le permet hors lecture ; `exiger_centres` sain et artefact ; modèle à empreinte de centres fausse refusé.
- **Branche « fichier réel » de `exiger_premiere_execution`** : fichier réel d'autres entrées refusé en mode réel et accepté en mode jouet ; fichier jouet accepté ; doses jugées réelles refusées.
- **Tirages dégénérés de `rappel_episode`** : cas sain (0 tirage dégénéré) ; artefact où les positifs ne sont que dans une tâche, rendu « non calculable » avec le motif.

**CL-05 (`valider_doses`)**
- Nouvelle fonction `attendu_doses` : elle reconstruit tous les champs du fichier (d) depuis la ligne de la lecture du coût, les doses établies, les états, les qualificatifs et les motifs de l'audit. Champs reconstruits : ligne K, doses jugées, phrase gelée, phrase, suite, motif, témoin positif, qualificatifs, réserves R-K1 à R-K6, lecture prudente, option, doses admissibles.
- `valider_doses(doc, sources=None)` compare le document à cette reconstruction, champ à champ ; il vérifie aussi la cohérence des prédictions K-P1, K-P2 et K-P4 avec les états.
- `executer` valide deux fois : contre les sources écrites (issue, lecture du coût, audit), puis contre le document lui-même.
- Le fichier (d) porte deux clés de plus pour permettre la reconstruction : `etats_temoins` et `audit_motifs`. **C'est un changement de format à connaître du sous-agent R13.**
- Essais :
  - 6 cas sains : KA-4, avec audit, KA-2, KA-3, ligne C5, K1 ;
  - 20 falsifications refusées une à une, dont celles du contre-lecteur (phrase, suite, témoin positif, qualificatifs, R-K2 cachée, phrase gelée, doses jugées, KA-3) ; aucun motif de refus ne porte de valeur ;
  - 5 écarts aux sources refusés : états, établies, ligne, audit, qualificatifs.

**CL-07 (clone superficiel)** — fonction `controler_code`.
- Quand le commit cité est absent et que `git rev-parse --is-shallow-repository` vaut `true`, le refus ajoute « clone superficiel : `git fetch --unshallow` ».
- Essai sur un vrai clone `--depth 1` ; contre-cas : un commit inventé dans un clone complet donne un refus sans cette mention.

**CL-06** : aucun changement de code, comme demandé.

## Essais
`tests/test_lecteur_texte_dose_reponse_v2.py` : **128 essais, 149 s, tous verts.** Ce sont les 75 de la v1 adaptés à la v2, plus 53 essais neufs.

## Les quatre mutants du contre-lecteur
Ils sont appliqués à une copie de la v2 dans le bloc-notes : `mutants_v2.py`, copie `mut2/`, journal `mutants-v2.log`. Chaque passe joue 127 essais, sans le mode réel de bout en bout.

| Mutants appliqués | Essais en échec | Essais en cause |
|---|---|---|
| Les quatre ensemble | 35 | ceux des quatre lignes suivantes |
| Audit neutralisé seul | 8 | déclencheurs (1), (2), (4), (5), (6) de l'audit, échantillon par graine |
| Branche « fichier réel » retirée seule | 1 | `test_cl04_seconde_execution_branche_fichier_reel` |
| `valider_doses` vidé seul | 25 | toutes les falsifications et tous les écarts aux sources |
| Garde des plis désactivée seule | 1 | `test_cl04_garde_des_plis` |

## Déclaration de cloisonnement
- Je n'ai ouvert aucune donnée d'organisme : rien sous `diag/`, `runs/` ni `donnees/` du dépôt, aucun score, verdict ni sortie de course.
- Je n'ai ouvert aucune pièce privée (ni la pièce jointe des consignes privées, ni `prereg/P3-consignes-v1.md`), ni `registres/etat.md`, ni aucune passation.
- J'ai lu le rapport de contre-lecture versé, et dans le bloc-notes du contre-lecteur `exp2.py`, `exp3.py`, le différentiel de `mut/` et la fin de `mutA.log` : ce sont des données factices.
- Je n'ai créé aucune instance, rien dépensé, lancé aucune génération de modèle ; je n'ai rien committé ni poussé.