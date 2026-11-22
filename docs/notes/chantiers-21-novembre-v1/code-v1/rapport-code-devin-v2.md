# Rapport de code — les épreuves du devin, version 2 (mondes simulés)

- Classe B (instrument). Développeur : Opus 5.5. La version 2 porte les corrections de la contre-lecture, sans rien concevoir.
- Contre-lecture : `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-devin-opus-v1.md` (40866478…, vérifiée), verdict « conforme après corrections ».
- Spécification, qui fait foi : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v3-consolidee.md` (e45bb770…).
- La version 1 (`src/controle_ia/devin_v1/`, ses essais, son script, son rapport) n'est pas touchée. Aucun commit.

## Fichiers neufs

- Paquet `src/controle_ia/devin_v2/` : mêmes onze modules que la version 1, corrigés.
- Essais `tests/test_devin_v2_{graines,vue,tirage,monde_plante,predicteurs,statistique,puissance,borne_haute,admission,lien_epreuve_11}.py`, plus `tests/test_devin_v2_admission_garde_c14.py`, écrit après le jeu des mutations (voir plus bas).
- Script `scripts/devin_v2_simulations_longues.py`.
- Mutations : `docs/notes/chantiers-21-novembre-v1/code-v1/mutations-devin-v2/mutations_devin_v2.py` et sa sortie `resultats-mutations-devin-v2.txt`.
- Ce rapport.

Chaque fichier a son compagnon `.sha256`.

## Essais

- **Scellement avant la première exécution.** Les dix fichiers d'essais ont été scellés avant tout lancement ; seule la compilation avait été vérifiée. Le fichier complémentaire de la garde C14 a été scellé, lui aussi, avant son premier lancement.
- **Résultat.** `PYTHONPATH=src python -m pytest -q tests/test_devin_v2_*.py` : **97 passés en 41 s** au premier lancement, puis 97 passés au second. Il faut y ajouter 1 passé pour le fichier complémentaire. Aucun fichier scellé n'a été corrigé après coup.
- **Racines.** Aucune racine n'est tirée de l'entropie du système dans un essai. Les courses reçoivent `source_racines`, des racines fixes dérivées de la constante du fichier par `SeedSequence`. Deux essais câblent le chemin par défaut en remplaçant la source du système par une source fixe :
  - `admission` : `tirer_racine` est remplacé ; 13 racines sont tirées, l'origine est « source d'entropie du système » ;
  - `graines` : `os.urandom` est remplacé par des octets fixes.
- **Reproductibilité.** Les essais sont déterministes : deux passes donnent le même résultat, et un essai rejoue une course à l'identique (M, p, témoins).

## Mutations (jouées sur une copie, depuis la racine de la copie)

La copie a son propre `pyproject.toml`, un `conftest.py` vide, et `PYTHONPATH` pointé sur la copie. Le script imprime le module chargé : c'est celui de la copie. Une mutation est appliquée à la fois, puis on rejoue le fichier d'essais de la pièce.

- **Ensemble joué.** Les 32 mutations de la contre-lecture, portées sur la version 2 (M20, M21 et M22 dédoublées), plus 4 mutations des gardes neuves (M33 à M36).
- **Les neuf survivantes de la version 1 sont toutes tuées** :

| Mutation | Constat | Essai qui la tue |
|---|---|---|
| M13 orientation toujours positive | C7 | `test_orientation_negative` |
| M15 Z sans centrage par π | C8 | `test_forme_de_z_et_rejeu_avec_pi_etoile` (Z calculé à la main) |
| M17 Z* avec π observé | C8 | même essai (M_nul contre Z* recalculé avec π*) |
| M20 témoin factice ignoré (règle a, emploi b) | C1, C6 | `test_regle_du_test_de_mort_4`, `test_course_emploie_la_regle_du_test_de_mort_4` |
| M21 racine en clair non cherchée (épreuve a, apprentissage b) | C9 | `test_racine_en_clair_dans_une_vue_refusee[epreuve]`, `[apprentissage]` |
| M24 rejet de l'épreuve à part versé dans le rejet | C10 | `test_vue_elargie_sans_preuve_epreuve_a_part` |
| M28 source « factice » admise | C11 | `test_aucun_repli_entrees_invalides` (`match="ne touche rien"`) |
| M29 garde à canaris sautée dans l'admission | C5 | `test_admission_refuse_un_extracteur_qui_fuit` |
| M30 racine de rejeu de la lecture égale admise | C13 | `test_lecture_substituee_service_et_equilibre` |

- **M22, racines d'épreuve tirées avant le scellement (C14)** : la version a (lignes déplacées) et la version b (garde muette) sont tuées.
  - La version c (appel de la garde retiré) **survivait** au premier jeu : l'ordre des lignes est juste, et l'absence de l'appel ne se voit pas.
  - J'ai écrit et scellé avant son lancement `tests/test_devin_v2_admission_garde_c14.py`, qui espionne l'appel. M22c est tuée au second jeu.
- **M33 à M36** (B < 999 admis, racine du monde hors de la source, taux du service à 0,5, empreinte sans le code) : tuées.
- Contrôle sans mutation : passe. Le détail est dans `resultats-mutations-devin-v2.txt`.

## Sort de chaque constat de la contre-lecture

| Constat | Sort | Ce qui est fait |
|---|---|---|
| C1 témoin factice inopérant à B < 999 | corrigé | `exiger_b_temoin_factice` refuse quand 1/(B + 1) > 0,001 (« B ≥ 999 exigé ») ; règle extraite en `declenchement_mort_4` ; essais à B = 999 ; refus essayé à B = 199 et 998 ; script : défaut 9 999, refus à 199 constaté |
| C2 racine du monde non consignée | corrigé | Avec `source_racines`, la racine du monde vient de la source (« …:monde »), dans `jouer_course` et `admettre`. Le verdict porte `empreinte_racine_monde` et, après la fin, `racine_monde` en clair. Le script dérive tout de sa racine et prend `--racine` pour rejouer (rejeu constaté identique sur deux sorties) |
| C3 racines révélées non consignées | corrigé | Le verdict porte `racines_revelees`, `racines_rejeu`, `graine_predicteurs` et `racine_canaris` ; ces champs sont exigés par `valider_verdict` ; un essai vérifie les empreintes |
| C4 essais d'admission au hasard | corrigé | `source_essai` sur toutes les courses. Le chemin par défaut est essayé avec une source remplacée, sans entropie du système (écart à la lettre de la correction proposée, qui gardait une course au hasard : la consigne de la mère l'interdit) |
| C5 = C12 garde à canaris non essayée | corrigé | `test_admission_refuse_un_extracteur_qui_fuit` |
| C6 essai du témoin qui recopiait la règle | corrigé | Remplacé par `test_regle_du_test_de_mort_4` |
| C7 orientation négative | corrigé | `test_orientation_negative` |
| C8 forme de Z et Z* avec π* | corrigé | `test_forme_de_z_et_rejeu_avec_pi_etoile` |
| C9 racine en clair dans le pli d'apprentissage | corrigé | Recherche ajoutée sur les vues du pli d'apprentissage, et essais pour les deux plis |
| C10 épreuve à part qui ne suspend rien seule | corrigé | Assertions `rejet is (p ≤ α)`, absence de rejet et garanties suspendues vides |
| C11 motif « factice » trop large | corrigé | `match="ne touche rien"` |
| C13 racine de rejeu de la lecture égale | corrigé | Assertion ajoutée |
| C14 ordre des racines d'épreuve | corrigé | Horloge logique (`graines.prochain_ordre`), rang de chaque `RacineScellee` et de chaque scellement de `Famille` ; la garde `exiger_epreuve_apres_scellement` est appelée avant le jeu du pli d'épreuve ; un essai direct et un essai d'appel |
| C15 taille au régime de service | corrigé | τ = part des lectures de témoins au-dessus du seuil ; essai à τ = 0,1 |
| C16 empreinte sans le code | corrigé | sha256 du fichier `monde_plante.py` dans l'empreinte ; essai par copie modifiée |
| C17 puissance du témoin non dite | corrigé | Champ exigé `puissance_temoin` : « non vérifiée par le code : à déclarer dans le préenregistrement… » |
| C18 nom d'essai trompeur | corrigé | `test_lecture_canal_ouvert_rejette` |
| C19 aucun artefact de cible A2 | **renvoyé au concepteur** | Inchangé. La cible A2 n'est éprouvée que sous le nul |

## Points renvoyés au concepteur (non tranchés)

1. **Artefact « ordre »** (point 6 du rapport v1). Le code garde le décalage de `rang_max`, hors du support. La contre-lecture recommande de le garder et de l'écrire dans un erratum.
2. **Vue de la cible A1** (point 3). Le code garde l'épisode visible entier, durée du dernier pas comprise. La spécification se contredit entre « avant chaque action » (section 1) et l'artefact d'horodatage du dernier pas (section 4).
3. **Cas hors table de l'épreuve 11** (point 19). Bras fermé, devin au hasard, courbe qui ne monte pas : toujours refusé, non lu.
4. **Critère « croît avec λ »** (point 20). `verifier_attendu_monde_plante` exige toujours une croissance stricte sur une seule réalisation. L'essai rapide joue les doses {0 ; 0,3 ; 1}, et le script les quatre doses.
5. **Artefact de cible A2** (C19).
6. Note au concepteur, acceptée par la contre-lecture : **J = 12 au lieu de 15** (point 10), et la question de compléter la douzaine de traits sur harnais réel.

Les autres points ouverts du rapport v1 sont acceptés par la contre-lecture et restent tels quels.

## Ce qui n'est pas écrit

Rien de neuf par rapport à la version 1 : étages 2 et 3, harnais réel, inventaire, couplage des états internes, cycle de réparation, devin des corrections, manifeste R9 par course. Les simulations longues ne sont pas jouées au budget de la spécification ; seul le montage du script et son rejeu ont été vérifiés, en petit.
