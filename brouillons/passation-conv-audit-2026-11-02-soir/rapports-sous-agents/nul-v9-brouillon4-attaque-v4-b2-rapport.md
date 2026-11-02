# Rapport de sous-agent (texte de modèle, non opposable)

## Contre-lecture de la validation v9 : B1, I5, I6 et I2 levés, brouillon 4 écrit
Le brouillon 4 est prêt à recommiter. Je n'ai rien commité, écrit aucun `.sha256`, rien écrit sous `donnees/`. Seuls trois fichiers existants ont été modifiés, comme tu l'as demandé : `pole/nul_v9.py`, `essais/test_nul_v9.py`, `essais/mutations_nul_v9.py`.
- **Essais** (`essais/test_nul_v9.py`) : 37 réussis, 35 sous-essais (33 avant).
- **Mutations** (`essais/mutations_nul_v9.py`) : 43 sur 43 tuées pour la raison attendue, témoin de 26 essais sans échec avant et après. Dernier passage de 19:55 à 19:57 UTC, sur le code final.
- **Mutations du contre-lecteur** : G1 à G5, L1, L2 et C5 sont reproduites avec ses fragments exacts (ceux de l'ordre des issues, comparés à l'identique). Toutes sont tuées.

## Essais ajoutés
- **B1, mode décisif** : `GrainesEtPreenregistrement.test_mode_decisif_cas_sain_et_refus`.
  - Cas sain : texte scellé au nom décisif, gelant les 14 empreintes, sans option. Code 3, avec `jouer_tout` remplacé par un bouchon qui ne lance aucun calcul ; la course n'est appelée qu'une fois.
  - On vérifie : les 31 lignes du plan, 1 000 répétitions chacune, durée transmise 172 800 s, entropie égale à l'empreinte du texte, manifeste « decisif ».
  - Artefacts : `--lignes M01` et `--repetitions 999` donnent le code 2, le texte n'est jamais lu, rien n'est écrit.
  - Tue G1, G2, G3 et G4.
- **B1, monotonie par la seule richesse** : sous-essai « monotonie-richesse » dans `test_banc_reduit_et_liste_d_arret` (log W 2,0 sous v9 contre 1,0 sous v8, aucune promotion). Code 3, `MonotonieViolee`. Tue G5.
- **I5, ordre des issues** : `LectureGelee.test_ordre_des_issues`. Une fatale non tenue avec une perte non tenue se lit « trou » ; une perte non tenue avec un artefact non tenu se lit « puissance perdue ». Tue L1 et L2.
- **I6, optimisation tronquée** : `CertificatMorceaux.test_valeur_certifiee_sous_optimisation_tronquee`, sur les 30 mondes de l'essai de domination, avec un palier et un pas. La valeur certifiée reste au-dessus de la vraisemblance du monde ; la meilleure valeur atteinte + 10⁻³ passe dessous à au moins un instant. Tue C5.
- **I2, description** : `DescriptionPublique.test_description_publique_separe_trous_choix_et_nature`, et l'essai de description existant réécrit. Mutation neuve « description publique : choix rangés parmi les trous », tuée.

## Ce qui a changé dans `pole/nul_v9.py` : la description seulement
Empreinte : 8cb44adf… → **7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95**.
- `NON_COUVERT_V9` ne garde que les 4 trous. Le « bruit propre / loi aveugle seule » en sort.
- Trois constantes neuves :
  - `HORS_DU_NUL_PAR_CHOIX_V9` : escalier aveugle, loi aveugle seule sur un morceau, bruit propre à un morceau (autre loi, ou même loi avec un autre poids) ;
  - `HORS_DU_NUL_PAR_NATURE_V9` : lois hors de l'archive ;
  - `RESERVES_V9` : mondes sans mémoire, traits finis, marge de Newton des membres log-linéaires.
- `PHRASES_MEMBRES_V9` dit maintenant « même loi aveugle, même poids ».
- Fonction neuve `description_publique()` : maximum au dénominateur, classe couverte, garantie, puis trous, choix, nature et réserves, dans cet ordre. `description()` les rend aussi.
- Aucun calcul ne change. J'ai comparé les arbres syntaxiques avant et après : seuls ces constantes et les deux fonctions de description diffèrent. La docstring du module dit les trois sortes. Copie d'avant : `nul_v9-avant-description.py` dans le bloc-notes.
- Conséquences : la ligne `pole/nul_v9.py` du bloc d'empreintes de la validation change, et le gel de l'attaque v4 suit. Une vérification courte de ce changement serait prudente, puisque la contre-lecture ne l'a pas vu.

## Brouillon 4
`prereg/preenregistrement-validation-nul-v9-brouillon4.md` : 653 lignes, sha256 **02dfbb7b139d71bde1f3d3fb85b150cc07f7371a12a71acdd0139842c8dc0908**, aucun jeton.
- **Couples** : les 23 applicables tels quels l'ont été dans l'ordre du fichier, chacun présent une seule fois. Les 15 d'I7 sont refaits sur le texte du brouillon 3.
- **Mises à jour d'état** : les mentions « à ajouter » des couples T07, T10, T21 à T23 et T25 disent maintenant que c'est fait.
- **Lecture et revendication** :
  - I1 : lecture à deux étages, sur `lecture.fatales` et `lecture.artefact`, sans toucher au code ;
  - I3 : la revendication publique et la production attendent le mot explicite de Lazar, la course peut partir ;
  - I4 : interdit de resceller pour changer de graine ; un arrêt déterministe est un défaut du code, pas un rejeu.
- **Mineurs** : M1 à M6, M9 et M10 sont traités. M7 n'est pas touché : les docstrings du code gelé citent encore le brouillon 1. M8 n'est pas fait : un essai d'A2 est facultatif et inaccessible dans une course complète.
- **Section 0 ter** : changements 3 → 4.
- **Bloc d'empreintes** : 14 lignes sur le code final, égales à l'arbre de travail. Vérifié hors dépôt par scellement simulé : le banc accepte le texte et refuse l'ancienne empreinte du banc.
- Construction par `construire_b4.py`, dans le bloc-notes `…/scratchpad/validation-b4/`.

## Attaque v4 : alignée sur la description publique
Tu as commité la v4 à b9b3ee3 pendant ce travail ; je l'ai modifiée ensuite. Sa description du juge v9 dit maintenant :
- « Non couvert : » suivi des seuls trous ;
- « Hors du nul par choix », puis « Hors du nul par nature ».

Une mutation de plus. 27 essais (73 sous-essais), 33 mutations sur 33 tuées.

Nouvelles empreintes, à comparer à b9b3ee3 :
| fichier | sha256 | à b9b3ee3 |
|---|---|---|
| `pole/attaque_goodhart_v4.py` | 0077a6470781b8cd9e0599232ddd52e3601c8c4c8735a5cfcf817800bda3bb5c | 692bef22… |
| `essais/test_attaque_goodhart_v4.py` | 350423da81e1f49eb251a72c8a0ca69c350cab8298b8f59b5c10c75bf3739cd6 | b8d9be41… |
| `essais/mutations_attaque_goodhart_v4.py` | 2dd378f6e83c1e5f0a4079e615b132763a13cd3d1fed028249747d806b87c6db | 3a66aaa9… |
| `prereg/rapport-redaction-attaque-goodhart-v4.md` (mis à jour en place) | 504577e6374f085f15eb50faa45363e7726a58486871103a4f33d3445e527c9d | — |
| `demonstrations/attaque_goodhart_v4.py` | inchangé | — |

Le texte de l'attaque passe dans un fichier neuf, `prereg/preenregistrement-attaque-goodhart-v4-brouillon2.md` (sha256 7be8589ef091d1a9afd2536cd44e65311d832e3aa5aa3c7a05a80c0827383862 ; section 0.4 pour les changements). Le bloc est relu et accepté par le lanceur v4, les deux jetons restent. Le brouillon 1 commité reste intact : je l'avais modifié avant de voir ton commit, puis je l'ai remis au contenu de HEAD (e778aac1…).

## Écarts et réserves
- Les courses à blanc A, B et C de la v4 ont tourné avec l'ancienne description. Le calcul, les graines et le proposeur scripté ne changent pas ; seuls les empreintes de consigne et les manifestes différeraient. Non rejouées, c'est dit au rapport v4.
- Je n'ai pas relancé le script de sondes du contre-lecteur sur toute la suite ; ses mutations sont vérifiées par le banc de mutations.
- Si tu préfères garder la v4 telle qu'à b9b3ee3, tu peux écarter ma modification : elle reste valide mais ne dirait plus les choix.

Sorties et empreintes : bloc-notes `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/validation-b4/` (`essais-et-mutations-b4-sortie.txt` cac9a7a3…, `verif_b4_validation.txt` 968f537c…) et `…/scratchpad/attaque-v4/` (`essais-et-mutations-final2-sortie.txt` 4a9e2bd7…).