# Contre-lecture — question de la course « nouvelles attaques », différentiel v4 → v5 (les deux couples de la note de périmètre v3) — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur la demande de la mère (message de mi-session), sous les interdits de mon mandat (`mandat-contre-lecteur-question-v4-v1.md`, `73aa9466…`). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Aucune recette, aucun nom ni énoncé de mode. J'ai contre-lu la v4 ; je n'ai écrit aucune version de la question, de la note de périmètre, de l'ordre de course, du préenregistrement court ni du devis.

## 0. Verdict

**Conforme, à sceller.** Aucune correction.

1. Le rejeu de l'outil sur la v4 scellée, avec le JSON, rend la v5 à l'octet (`cmp` muet ; `eaf5db8a…`).
2. Les deux couples sont mot pour mot ceux du § 2 de la note de périmètre v3 scellée. Mon programme trouve, une fois chacune, les chaînes exactes « Avant : « … » Après : « … » » de la note.
3. Rien d'autre que la tenue n'a changé :
   - les § 1, § 2, § 3, § 5, § 6 et § 7 sont égaux à l'octet à ceux de la v4 ;
   - le § 4 de la v5 est exactement le § 4 de la v4 auquel on applique les deux seuls couples (+444 octets) ;
   - l'en-tête porte les trois zones de tenue.
4. Mon relevé ne trouve aucune occurrence, ni des motifs du mandat ni des motifs complémentaires, dans les § 2 à § 7.
5. **L'écart de définition** (le couple 1 contre le § 1 de la note) va **sans suite pour la question**. Il va **au directeur pour la lecture**, par le préenregistrement court v7 (§ 4 ci-dessous).

## 1. Pièces et empreintes

`origin/main` après `fetch` : `6d97a4304`. Tirés par `git show origin/main:… > …` dans `v5/` :

| pièce | empreinte |
|---|---|
| question v4 scellée, `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v4.md` | `47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654` |
| note de périmètre v3 scellée, `prereg/ideation-nouvelles-attaques-v1/note-perimetre-modes-inedits-v3.md` | `dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580` |
| `registres/go.md` (lignes 573 à 577 lues : GO-2026-11-20-42, -44, -45, -46) | copie `v5/tire-de-main-go.md` |

Dossier `docs/notes/ideation-nouvelles-attaques-v1/question-v5/` (compagnon de la question vérifié « OK » ; toutes les valeurs recalculées sont égales à celles que donne la mère) :

| pièce | empreinte |
|---|---|
| `question-course-nouvelles-attaques-v5.md` | `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f` |
| `remplacements-question-v4-vers-v5-v2.json` | `00c87047e44358d6b9513283a780f23317340a7592920e60fa5fbd3c1ec315c6` |
| `differentiel-question-v4-v5-v1.diff` | `2bd5b5b7074c6abbf449a959da40cfa957ca3a06349e4b28750b683c11aa8fb6` |
| `releve_motifs_partie_servie_v1.py` ; `releve-motifs-question-v5-v1.txt` | `7024cd82…` ; `0e82beaf…` |
| `rapport-redacteur-question-v5-v1.md` | `96b87336f7ed8291020079c1670b2685f17952a22011d8aa3974bf55af10aa3d` |
| `mandat-redacteur-question-v5-v1.md` | `1fa844077ad6c250b04b9630d123be5340303dcc0a77432205cb46e8b9873396` |
| outil `scripts/remplacer_texte_exact_v1.py`, sur disque | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## 2. Contrôles

- **Rejeu.** L'outil a pour cible la copie de la v4 tirée de `main`, pour JSON celui du dossier, pour sortie `v5/question-v5-rejouee.md`. Il répond « FAIT : 5 remplacement(s) ; cible 47160d37… → … (eaf5db8a…) ». L'outil compte lui-même chaque ancien à une occurrence et chaque neuf à une de plus : le rejeu sans refus vaut ce compte. `cmp` avec la v5 rendue : muet.
- **Programme.** `controle_question_v5_v1.py` (bibliothèque standard, plus mon module de relevé de la v4, `releve_motifs_question_v4_v1.py`). Sortie : `sortie-controle-question-v5-v1.txt`.
  - Couples 1 et 2 : chaîne « Avant … Après … » présente 1 fois dans la note ; ancien 1 fois dans la v4 ; neuf 1 fois dans la v5 et 0 fois dans la v4.
  - § 4 : celui de la v4 auquel on applique les deux couples est égal à celui de la v5 (1 171 → 1 615 octets).
  - Sections : en-tête et § 4 différents ; § 1, 2, 3, 5, 6, 7 égaux à l'octet.
  - Relevé des motifs sur la v5 :
    - en-tête : 23 occurrences du mandat (`GO-20`, `docs/`, `prereg/`, `registres/`, quinze empreintes) ;
    - § 1 : 6 ;
    - **§ 2 à § 7 : 0 du mandat, 0 des motifs complémentaires.**
    
    Cela s'accorde avec le relevé du rédacteur (0 dans la zone).
- **Tenue.** Trois zones dans l'en-tête :
  - le titre ;
  - la phrase de la v4 sur le § 4 ;
  - la ligne de version de la v5 et le statut.
  
  La ligne de version cite exactement la cause et les sources, dit « deux phrases » (le compte est juste) et « cinq remplacements ».

## 3. L'en-tête « rendu juste » plutôt que retiré

La note, § 2, dit que l'en-tête de la v5 « retire » la phrase « le § 4 […] est égal à l'octet à celui de la v3 ». Le rédacteur l'a rendue juste : « était dans la v4 égal à l'octet à celui de la v3 (il ne l'est plus dans la v5 : voir la ligne de version qui suit) ».

**Jugement : sans suite, conforme. Confiance 0,75.**
- Le but de la note est atteint : la v5 ne porte plus d'affirmation fausse sur son § 4.
- La forme retenue garde un fait vrai de la v4 et la provenance, ce que le retrait effaçait.
- La phrase n'est pas servie.
- Le rédacteur déclare l'écart de lettre (son écart 3), et son mandat permettait l'un ou l'autre.
- La mère peut le noter au scellement en une ligne.

## 4. Les remarques du rapport

| remarque | issue | recommandation | confiance |
|---|---|---|---|
| **Écart de définition** : le couple 1 définit le mode par ce qu'il met en défaut seul, la visée tenue par la case ; le § 1 de la note le définit par la visée et par ce qu'il met en défaut ; le § 2 de la question dit « classe de mécanisme » | **sans suite pour la question ; au directeur, par la mère, pour la lecture** (préenregistrement court v7) | Corriger le couple 1 romprait le « mot pour mot » que portent GO-2026-11-20-46, point 1 (b), et la note scellée : ce serait un écart neuf. Le texte servi n'est pas incohérent. La note, § 1, dit elle-même que, dans la course, « la case fixe déjà la menace et ce que le moniteur suppose » ; le couple 1 tient la visée au grain de la case (« qui reste dans la menace du programme que nomme ta case ») ; le couple 2 laisse nommer une visée plus fine (« par ce qu'elle vise »). La lecture adoptée par GO-2026-11-20-46, point 9 (b), une définition qui vit à côté des autres, les autres étant des cas où la visée est fixée, va dans le même sens. **Le vrai écart est dans la lecture.** La règle d'antériorité (question, § 2 ; ordre de course, § 9) juge par classe de mécanisme, c'est-à-dire par ce que l'idée met en défaut, alors que l'épreuve 4 de la note juge par le couple (visée, supposition mise en défaut). Deux fiches d'une même case qui ne diffèrent que par une visée plus fine sont « la même classe » pour la première, et deux modes pour la seconde. Que l'épreuve 4 entre ou non au plan d'analyse est un écart au préenregistrement court, que la note signale déjà (§ 2, dernier alinéa) : à trancher au v7, avant son scellement. | 0,7 |
| Part « hors case » | à la mère, pour le v7 et le contrôle de la v5 | Rien à corriger dans la question. Les seuils d'audit restent gelés ; le déplacement possible est à dire comme réserve de lecture. | 0,7 |
| Garde du coffre | à la mère, idem | Même réponse. | 0,7 |
| Nombre de fiches, réponse vide motivée | **à la mère, pour le v7** | Nommer, avant la course, une classe de compte pour une réponse vide ou un refus motivé par « ne la propose pas », distincte du refus d'un classifieur de sûreté (arrêt n° 1). Sinon, une réponse vide n'a pas de classe. | 0,6 |
| Variante déclarée (« par sa seule réalisation ») | au directeur, avec l'écart de définition | Même nœud : ce que la lecture fait de cet aveu dépend de l'entrée ou non des quatre épreuves au plan d'analyse. | 0,65 |
| Empreinte scellée seulement au v7 | sans suite (juste) | — | 0,9 |
| Arrêt n° 14 et racine gardée (`0x2cf2aae0…`, GO-2026-11-20-42, point 2) | sans suite (juste) | — | 0,9 |
| Sondes de refus sur la v5 ; pire de la sonde de l'espèce 6 recalculé | à la mère | Le risque est déjà porté au directeur (note, § 5, point 2) et accepté avec les recommandations. Le recalcul est à faire avant la sonde. | 0,8 |
| Témoins plantés | **à la mère** | Ajouter un témoin « variante d'une famille connue », au texte inerte, dont la bonne issue est connue d'avance. La v5 demande de ne pas en proposer : c'est la seule manière d'éprouver ce que le portier et les lecteurs en font. | 0,6 |
| Partie servie dérivée de la v5 | sans suite (juste) | GO-2026-11-20-46 suit la recommandation du point 2 de la note : la dérivation part de la v5 scellée, et le relevé se refait sur le fichier dérivé. | 0,85 |
| Devis non recalculé | à la mère | — | 0,8 |
| « Pièces sœurs » (devis v2) laissé tel quel | sans suite | C'est hors de « rien d'autre que les deux couples » ; le v7 porte le devis en vigueur. | 0,8 |
| Outil absent de `origin/main` (écart 1 du rédacteur) | à la mère | L'empreinte sur disque est celle que citent les textes scellés. Verser l'outil sur `main`, puisque des pièces scellées le citent. | 0,7 |
| Premier essai écarté, gardé (écart 2) | sans suite | Conforme à la règle de récupération. | 0,9 |

## 5. Observations sans correction

1. La ligne de version dit « le procédé n'est demandé qu'ensuite, pour les seuls modes jugés inédits, ailleurs que dans cette question ». La lettre de GO-2026-11-20-46 dit « puis le procédé est permis » ; la recommandation qu'il accepte (note, § 8, point 1) dit « le procédé se demande ensuite […] dans le bras d'attaque ». La paraphrase suit la recommandation acceptée. La phrase n'est pas servie : sans suite.
2. GO-2026-11-20-46, points 3, 5 et 6 (portier, relecture, quarantaine) touchent l'ordre de course et le préenregistrement court, non le texte de la question : sous « (b) d'abord », la garde du § 3 (niveau de l'idée, scellement au coffre du concret) reste vraie pour la v5.

## 6. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-question-v4/`. Chaque fichier a son compagnon `.sha256`.

- `contre-lecture-question-v5-v1.md` (cette pièce) ;
- `controle_question_v5_v1.py` ; `sortie-controle-question-v5-v1.txt` ;
- dans `v5/` : `question-v5-rejouee.md` (avec le compagnon, le journal et le compagnon du journal écrits par l'outil) ; `tire-de-main-question-v4.md` ; `tire-de-main-note-perimetre-v3.md` ; `tire-de-main-go.md`.

— contre-lecteur neuf, modèle O
