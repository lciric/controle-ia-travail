# Rapport du développeur — lanceur v11d de la course d'affinage des idées des mentors

Pièce de classe B, écrite hors ligne : aucun appel de modèle, aucune valeur de clé lue, rien de poussé. La v11d corrige la
régression R1 relevée par la vérification des corrections du v11c (`course-v11/contre-lecture-lanceur-v11c-verification-v1.md`,
`525dc158…`). Elle ajoute aussi deux demandes du rédacteur du texte, relayées par la mère. Les fichiers v11, v11b et v11c restent
intacts (R12). Pour tout le reste, le rapport v11c (`rapport-developpeur-lanceur-v11c.md`, `a56faf45…`) vaut.

## 1. Fichiers neufs

| fichier | rôle |
|---|---|
| `scripts/lancer_course_affinage_mentors_v11d.py` | lanceur v11d, produit à partir du v11c (`fe7358b9…`) par trois remplacements exacts : version, ligne de LUC de l'essai à blanc, épingle de la configuration v11d |
| `tests/test_lancer_course_affinage_mentors_v11d.py` | essais v11c (`88a61acd…`) adaptés, plus les essais propres à v11d |
| `course-v11/configuration-course-affinage-mentors-v11d.json` | configuration v11c (`7615a31c…`) : notes de la commande v2, plafond inerte retiré |
| `course-v11/releve-credits-gabarit-course-affinage-v11d.json` | gabarit du relevé des crédits, avec la ligne de LUC sous sa forme admise |
| `course-v11/rapport-developpeur-lanceur-v11d.md` | ce rapport |

## 2. Corrections et ajouts

| point | correction | essai (cas sain ; artefact) |
|---|---|---|
| R1 : essai à blanc refusé | `reglages_a_blanc` écrit pour LUC `{"solde_non_lu": true, "reference": "GO-2026-11-22-124", "source": "essai à blanc"}` | `test_v11d_releve_de_l_essai_a_blanc_passe_verifier_credits` ; `test_v11d_essai_a_blanc_de_bout_en_bout_moteur_simule_rend_0` (moteur simulé, rend 0) ; `test_v11d_artefact_ligne_de_luc_de_l_essai_a_blanc_v11c_refusee` ; `test_v11d_mutation_essai_a_blanc_avec_la_ligne_v11c_refuse` (mutant : code 2) |
| (a) configuration v11d | notes `changements_v11.carbon` et `.argon` qui citent `commande_gemini_flux_v2.py` ; **`relais_persistants_v4.plafond_relais_claude_usd` retiré** (ni le lanceur ni l'orchestrateur ne le lisent ; le bloc `relais_persistants_v4` est exclu de la configuration servie à l'orchestrateur) ; une note `note_v11d` le dit dans le bloc | `test_v11d_configuration_notes_et_plafond_inerte_retire` |
| (b) gabarit du relevé des crédits | `releve-credits-gabarit-course-affinage-v11d.json` : LUC (`solde_non_lu`, `reference`, `source`) ; `GEMINI_API_KEY` et `OPENAI_API_KEY_2` en « non lisible » sous la dispense de la mère (R-3237), ou lisibles (`credit_usd`, `reste_usd`, `source`) ; `releve_utc` à remplir | `test_v11d_gabarit_du_releve_des_credits_rempli_passe_verifier_credits` ; `test_v11d_gabarit_non_rempli_refuse` |

**Gabarit du relevé des prix Claude** : je n'en écris pas. Le lanceur lit le relevé des prix du jour (`RELEVE_PRIX`, en moteur
réel), jamais un gabarit.

**Essai de bout en bout de l'essai à blanc** : il joue `reglages_a_blanc` sur un dépôt d'essai. Ce dépôt contient les pièces
épinglées, la garde Google de `origin/main` et un préenregistrement d'essai scellé, car l'empreinte du préenregistrement v11
n'est pas encore posée. L'essai joue aussi le faux orchestrateur des essais, parce que l'orchestrateur épinglé n'est pas sur
cette machine. Il ne joue donc pas l'orchestrateur réel en moteur simulé : à refaire sur la machine de départ, par la commande
`--a-blanc` de l'en-tête.

## 3. Essais (fichier du lanceur seulement)

| fichier | compte |
|---|---|
| `tests/test_lancer_course_affinage_mentors_v11d.py` | 330 réussis, 4 sautés (essais hérités qui cherchent l'orchestrateur aux emplacements fixes, absents ici), 0 échec |
