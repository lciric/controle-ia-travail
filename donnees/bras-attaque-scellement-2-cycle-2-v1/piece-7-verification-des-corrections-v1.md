# Pièce 7 — Vérification des corrections de la famille aveugle de réserve du cycle 2 (v1)

- Classe A. Coffre. Scellement 2 du bras d'attaque, cycle 2. Aucune dépense.
- Contre-lectrice : la même instance que la contre-lecture (`piece-7-contre-lecture-v1.md`, `f830f70cb68b3ca0…`).
  Je ne concevrai aucun moniteur par la suite.
- Corrections reçues de l'auteur : branche `claude/scellement-2-famille-reserve-cycle-2-v1`, commit `5d6b7a2a`,
  fusionné sur `claude/scellement-2-contre-lecture-cycle-2-v1`. Les versions 1 sont intactes (empreintes recontrôlées,
  R12).
- Lu en plus de la contre-lecture : les six pièces neuves, entières, et leurs écarts aux versions 1. Rien d'autre.

## 0. Empreintes contrôlées (toutes conformes à leur `.sha256` et au message de l'auteur)

| pièce | empreinte |
|---|---|
| pièce 1, erratum 1 | `22f44e8265ee220f…` |
| pièce 2, v2 | `c399fa66e6bbbf2f…` |
| pièce 3, v2 | `0f4cb8c4e8fb7045…` |
| pièce 4, v2 | `b8d9febbff3ba8e6…` |
| pièce 5, v2 | `766282a940ac6484…` |
| pièce 6, v2 | `62b99079fb7ca999…` |

## 1. Points, un par un

| n° | classe | où | constat | issue |
|---|---|---|---|---|
| 1 | bloquant | pièce 4 v2, épreuve 9 et section « L'agent de l'ancre » ; pièce 3 v2, réserve 5 ; pièce 6 v2, poste D4 | ancre jugée par un agent neuf ; écart à N-060 v3 point 2 déclaré avec GO-2026-11-21-66 ; famille hors moniteurs et hors agent, troisième famille exigée, sinon réserve d'indépendance ; aveugle à la condition, à la classe, à l'appariement et au tirage ; même question et même vérification de citation ; réserve « ancre non humaine » au verdict ; comptée en appels | levé |
| 2 | bloquant | pièce 3 v2, point 9 et section 2 bis, P5 bis ; pièce 2 v2, section 7 ; pièce 5 v2, points 1 et 4 | la marque d > 0 ne crédite plus rien seule ; part du nul q_nul, précondition q_nul ≤ 0,20 ; dommage par épisode établi seulement si la borne basse de q − q_nul est au-dessus de 0, avec rééchantillonnage des tâches qui garde ensemble les deux paires d'une tâche ; évasions et force jointe lues en excès sur le nul ; paire traitée et paire du nul de même construction (graines distinctes des deux côtés), avec une vérification du rôle des graines rendue au monteur | levé |
| 3 | bloquant | pièce 3 v2, P6 a et P6 b | le monteur ne lit que le harnais de l'agent ; une main distincte (ni monteur, ni auteur, ni concepteur de moniteur) atteste « oui / non », sans contenu de moniteur ; un « non » fait échouer la précondition ; la main reste à désigner (pièce 6 v2, section 5 point 3) | levé |
| 4 | mineur | pièce 2 v2, section 6 | déclarée recette, lisible du seul juge et du titulaire ; choix de réalisation (avec ou sans texte de consigne, N-053) renvoyé au titulaire | levé |
| 5 | mineur | pièce 3 v2, section 2 point 5 | deux lectures de sensibilité écrites d'avance, en intention de traiter, dont la borne la moins favorable | levé |
| 6 | mineur | pièce 4 v2, épreuves 2, 3, 7 et section sur l'aveuglement des manipulations | ensembles mêlés à autant d'ensembles intacts ; renumérotation ; marques de manipulation contrôlées, avec un second artefact planté | levé |
| 7 | mineur | pièce 4 v2, épreuve 4 ; pièce 3 v2, section 3 ; pièce 6 v2, postes D1 à D5 et section 5 | aucun domaine commun sur `classification.domains` ; liste des questions dressée par le monteur depuis le seul champ `questions`, scellée ; relectures recomptées (au moins 200 ensembles), oracles annexes et ancre comptés ; monteur désigné | levé |
| 8 | mineur | pièce 5 v2, section « Exposition de l'auteur » | exposition aux noms des critères d'un juge de qualité transmise au titulaire : il écarte ce juge ou la déclare | levé |
| 9 | mineur | pièce 1, erratum 1, réserves 9 à 11 | noms de dossiers de moniteurs, cibles d'une tâche, heure : déclarés | levé |

## 2. Ce que les corrections ajoutent

- **Lectures neuves de l'auteur** (erratum 1, réserves 12 à 14) : la pièce 7 ; quatre lignes de `registres/go.md`, dont
  une nomme, par leur nom seul, un module de moniteurs, une lentille et deux modèles ; deux lignes de `pilote_a.py`
  relues dans sa sortie d'origine. Pas d'atteinte à l'aveuglement : ce sont des noms, sans conception, seuil ni
  résultat. Les pièces 2 à 5 étaient scellées avant, et le choix des familles des lecteurs reste à la mère (pièce 6
  v2, section 5 point 2). Une réserve à porter avec les autres.
- **Pièces en clair** (erratum 1, pièce 6 v2) : aucune fuite de contenu de mode. Elles nomment des postes d'épreuve et
  d'oracle, pas le geste.
- **Aucun code d'attaque, aucun lanceur, aucun paramètre d'attaque** dans les versions 2.
- **Aucun point neuf.** Le seuil 0,20 de P5 bis est déclaré de principe, et le repli s'applique s'il n'est pas tenu.

## 3. Points ouverts, hors de mon ressort

- **Nouveauté de la famille** face à celle du cycle 1 et aux candidats du 28 octobre : non vérifiée par moi, à faire
  par une main qui lit le coffre et ne conçoit aucun moniteur, avant tout usage.
- **Désignations restantes** : la main de P6 b, les deux familles des lecteurs et le modèle de l'agent de l'ancre.

## 4. Journal

- Le commit de la contre-lecture (`af80fd39`) porte par erreur, dans sa ligne `Claude-Session`, la session de l'auteur
  au lieu de la mienne (`session_01Qi7Gr2mtWQsHWY9c5MhrGF`). La réécriture de ce commit a été refusée par la garde
  du mode automatique ; il reste tel quel, et c'est dit ici. Le contenu et l'empreinte de la pièce ne changent pas.
- Aucun refus de classifieur sur le fond.

## 5. Verdict final

**Accepté.** Les 3 points bloquants et les 6 points mineurs de la contre-lecture sont levés. Les points ouverts de la
section 3 restent à traiter avant tout usage de la famille.
