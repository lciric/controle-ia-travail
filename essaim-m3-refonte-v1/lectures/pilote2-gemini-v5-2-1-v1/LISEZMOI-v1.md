# Lecture du second pilote descriptif (courses M et S, organisme v5.2.1 de Gemini) — pièces, v1

Lignée conv-audit, 25 octobre 2026, 15:47 UTC (heure lue sur `date -u`). Texte scellé lu :
`essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-2-v2.md` (T2,
`d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b`).

**Moment de lecture** (T2, plan § 3) : préenregistrement de l'étape 1 scellé (v9) ; inscription de la version 8 de la
confrontation, `essaim-m3-refonte-v1/prereg/brouillon-confrontation-essaims-v8.md`
(`e660cc4c01b9562746aa958307845857df0570d0a42eda2037ba6719f34e83ed`, branche `outils/confrontation-v8-travail`,
`59172f3`, poussée à 15:26 UTC). Aucune archive fermée n'a été ouverte avant.

## Pièces de ce dossier

| pièce | sha256 | ce que c'est |
|---|---|---|
| `lire_pilote_tableaux_v1.py` | `bf78c7ea19eef5f2ac17b99e8edf6993d9b1c35a12fc4837360a8ba05d81f70d` | lecteur : vérifie l'empreinte de `ferme.tar.gz`, ne lit dans l'archive que `juge/score.json`, `juge/score-final.json`, le rapport et le manifeste, écrit un tableau ; ne calcule aucune différence |
| `tableau-M-v1.md` | `322eb0e186acd6b6372ad18549f4021f1a962ac94b22ddee4bf5e366d33120f1` | course `pilote2-gemini-v5-2-1-maieutique-v1` ; `ferme.tar.gz` `a7bd419eb7e7d15c2edaf3985328b4847851c6f334f79369f29d84cb37dbe368` |
| `tableau-S-v1.md` | `8276db6aaa098973b7cc36b2c851b70784ed44dff8501c60e8603463318fb415` | course `pilote2-gemini-v5-2-1-structure-v1` ; `ferme.tar.gz` `323cb0ddf0bc98ff2851bafd39d3ea78bc371504f627044f7bb6691b90a81df6` |
| `audit-symetrie-v1/AUDIT-SYMETRIE-pilote2-v1.md` | `f732bfd857432086518357daae4bcd114c92f184a5cd987d0a738a7e6cfd9d36` | audit de symétrie (R4), sous-agent neuf lancé par conv-audit ; verdict « défaut établi » |
| `audit-symetrie-v1/EMPREINTES-v1.txt` | `3b285f6d7fa4f4739a448316b62cc4fc7590143456274333cf6dcf9cf9cef82f` | 69 pièces de l'audit ; 29 sont poussées ici (rapport, scripts, sorties) et se vérifient ; les 40 autres sont des fichiers extraits des deux `ferme.tar.gz` (`extrait-M/`, `extrait-S/`), non poussés, reconstituables depuis les archives des branches `pilotes/…` |

## Ce qui s'est passé à la lecture

1. Le critère gelé n° 1 de T2 s'est déclenché dans les deux courses (famille `controle-delegation`, g001 : M, `test` et
   `test_final` ; S, `test_final`). Audit de symétrie avant tout rapport, sans relance, par un sous-agent neuf.
2. **Verdict de l'audit : défaut établi, dans l'instrument** : les identifiants des tâches de la banque
   `confrontation-v1` (`f1387a20…`) donnent la vérité dans les deux familles et les trois parts (recoupé par conv-audit
   sur la banque scellée : train 80, test 60, test_final 60, sans exception) ; le noyau les sert aux organismes
   (`taches.masquer`), et l'entraînement avec ses vérités. La phrase de T2 « jamais une vérité de `test` ni de
   `test_final` n'est servie par le noyau » est fausse sur le fond. **Aucun effet trouvé sur M ni sur S** (aucun
   identifiant de `test` ou de `test_final` dans les 504 consignes envoyées aux modèles ; l'organisme ne se sert de
   l'identifiant que comme clé). Cause possible du déclenchement, non établie : les traces de cette famille ont été
   écrites par la même espèce que celle qui répond aux tâches (réserve déjà écrite dans `banque/LISEZMOI-v2.md`).
3. Le rapport de lecture complet de T2 (plan § 4 : appels, jetons, coûts, durées, moisson, clés, castes, mémoire,
   identité du code de g1, relance, éléments écartés, recouvrement du dépôt, les deux réponses telles quelles avec leur
   structure mécanique) suivra dans une version 2 de ce dossier ; les deux tableaux ci-dessus en sont la partie
   « scores ». Lectures interdites de T2 appliquées (aucun verbe de comparaison, aucun adjectif sur un score, aucune
   différence calculée).
