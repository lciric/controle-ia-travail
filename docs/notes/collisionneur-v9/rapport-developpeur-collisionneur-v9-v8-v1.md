# Rapport du développeur : collisionneur v9 version 8, v1

21 novembre 2026, vers 18:45Z (`date -u`). Développeur : Claude Opus 5.5 (`claude-opus-5-5`). Pièces d'instrument (classe B), à vérifier par un autre modèle. Mots de Lazar : GO-2026-11-21-63, GO-2026-11-21-69 et GO-2026-11-21-71. La mère a donné son ordre, puis deux ajouts en cours de travail :
- l'ajout 1 : « corrige et vérifie tous les réglages, plafond, troncation, limite de mots, réflexion, avant d'envoyer un modèle Gemini » ;
- l'ajout 2 : l'audit des réglages de Google, `docs/notes/audit-reglages-google-v1/audit-reglages-google-v1.md` (`09825b5b…`, sceau tenu), et son contre-audit, `contre-audit-reglages-google-v1.md` (`7dfe8ab2…`), lus en entier.

Ce que je n'ai pas fait :
- aucun envoi à un fournisseur, aucun comptage, aucune dépense ;
- aucune clé lue ni écrite : essais sous `env -u OPENAI_API_KEY -u GEMINI_API_KEY`, clés factices des doublures ;
- aucun commit.

Sur la branche des versements `origin/runs/collisionneurs-reprise-minuit-v1` (761c2c5a), j'ai lu cinq `journal.jsonl` par `git show` : statuts, usages, coûts, lignes. Je n'ai lu aucune réponse de modèle. J'ai lu deux pages publiques de Google, sans clé (section 2.2).

## Verdict

**La version 8 est écrite, et la garde des réglages de Google vit maintenant dans un module commun, `src/controle_ia/garde_google_v1.py`, avec ses essais dans `tests/test_garde_google_v1.py`.** La v8 l'appelle avant tout envoi à Google (flux et lot) et l'applique à toute réponse. Toutes les remarques de la contre-lecture de Fable sont portées, de même que les deux ajouts de la mère et les six points de l'audit sur le collisionneur.

- **Essais : 346 passés et 1 sauté pour la v8** ; le sauté est la copie du run « dopamine », non désignée, comme en v7. **42 passés pour la garde.** Les copies des quatre dossiers à reprendre ont tourné.
- **Mutations : 39**, faites sur la v8 et sur la garde. Section 7 ; le témoin sans mutation passe.
- **Pourquoi Argon ne réfléchissait pas.** La v7 n'envoyait que `thinkingBudget`, déprécié chez Gemini 4, et Argon recevait 8 192. La v8 envoie `thinkingLevel` au plus haut niveau documenté : « high » pour Argon et Carbon, « xhigh » pour Neon. Elle n'envoie plus de budget, sauf repli déclaré : si Google refuse le niveau, elle renvoie une fois au budget prévu, journalisé et affiché. Une réponse sans pensée, ou dont le compte de pensées manque, est un défaut (code 10), jamais une réponse.
- **Plafonds ramenés aux limites versées.** En lot (appel non diffusé), Argon et Carbon sont bornés à 32 768, d'après la liste versée, lignes 594 et 612. Carbon, dont la provision est de 49 152, est donc refusé en lot par la règle des 16 000 jetons de texte, et rien ne part. En flux, Carbon garde 65 536 : c'est au-delà de la liste versée (réserve 6.3).
- **Points à trancher par la mère (section 6)** :
  - SAFETY et RECITATION ne sont pas relancés ;
  - le réglage corrigé de l'unique relance est un niveau plus bas ;
  - le plafond de Carbon en flux ;
  - la lecture « niveau ou budget » de la règle.

## 1. Pièces lues

| pièce | empreinte |
|---|---|
| `collisionneur_v9_v7.py` (base) | `319a7b66…` (sceau tenu) |
| `test_collisionneur_v9_v7.py` | `7afaa354…` (sceau tenu) |
| `rapport-developpeur-collisionneur-v9-v7-v1.md` | `c0550182…` (sceau tenu) |
| `contre-lecture-collisionneur-v9-v7-fable-v1.md`, lue en entier | `f6342515…` (sceau tenu) |
| `reflexion-relance-collisionneurs-opus-max-v1.md` | sceau tenu |
| `docs/notes/audit-reglages-google-v1/audit-reglages-google-v1.md` | `09825b5b…` (sceau tenu) |
| `docs/notes/audit-reglages-google-v1/contre-audit-reglages-google-v1.md` | `7dfe8ab2…` |
| liste des modèles versée `liste-modeles-gemini-20261121T134904Z.json`, lignes 585 à 655 | `eeec19e8…` |
| page du modèle Neon versée, lignes 50 à 55 et 150 à 155 | `2eadc192…` |
| pages « Gemini thinking » (Interactions) et « Long decode », copies de Fable dans le bloc-notes | `a964d5cf…`, `a2317437…` (égales aux siennes) |
| `appel_modeles_externes_v3.py` et `appel-argon-v1.json` (métadonnées seules), `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/` | `8aee878d…`, `99539ec5…` |

## 2. Remarque → correction

### 2.1 Contre-lecture de Fable

| remarque | correction dans la v8 | essais |
|---|---|---|
| **C-1** : un relevé refusé abandonne un lot payé | `relever_lot` rend un relevé coupé **ou** refusé comme « manqué » ; `appeler_gemini_lot` suit le lot jusqu'au délai, puis l'annule. Le texte de Fable est porté sur le fond, et la boucle est réécrite autour de `relever_lot` | `test_c1_lot_sain_releve_refuse_puis_abouti_un_seul_lot` (texte de Fable) ; `test_c1_lot_artefact_releve_refuse_jusqu_au_delai_annule_compte_au_pire` (texte de Fable, plus le dernier relevé de la remarque 4) ; cas « relevé refusé » retiré de `test_v7_lot_artefacts_comptes_au_pire` |
| **C-2** : une réponse illisible est jetée | Partie de Fable : le relevé brut d'un lot échoué, d'un lot à forme inconnue ou d'une réponse en erreur va, masqué, dans `essais/…reponse.md`, scellé, jamais dans une cellule. Ordre de la mère (« jamais jetée »), au-delà du texte de Fable : sont aussi gardés le corps illisible de la création d'un lot, le relevé illisible au délai, la ligne illisible d'un flux (Google et Anthropic), le corps illisible de Kimi, le corps de la création chez OpenAI (illisible, ou lisible sans identifiant) et le dernier relevé illisible d'OpenAI. Outils : `charger_json`, `CorpsIllisible`, `avec_brut`, `BALISE_BRUT` | `test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule` (texte de Fable, trois cas) ; `test_c2_lot_corps_illisible_garde_masque` (deux cas) ; `test_c2_ligne_de_flux_illisible_gardee_dans_l_essai` (Carbon, Fable) ; `test_c2_kimi_corps_illisible_garde` ; `test_c2_temoin_charger_json_lisible` |
| **C-3** : le coût zéro d'un refus de crédit n'est pas établi | **Décision de la mère** (« établi, sinon compté au pire »), qui remplace la C-3 de Fable (l'usage annoncé, compté au prix réel). Le refus reste reconnu, il est nommé au journal (`refus_de_credit: true`), l'usage annoncé par `message_start` est gardé, et l'envoi est interrompu, compté au pire (code 5) | `test_v7_refus_de_credit_echec_cout_zero` (réécrit) ; `test_c3_refus_de_credit_compte_au_pire_jamais_zero` ; les quatre artefacts de la v7 |
| Remarque 1 : essai témoin du repli sur la provision | Essai de Fable, accordé à la v8 : une ligne écrite comme sous la v6 reste en défaut sous le réglage de la v6, mais plus sous celui de la v8, dont le réglage a changé | `test_cl_v7_reglage_en_defaut_essai_d_avant_le_v7_sans_budget_au_journal` |
| Remarque 2 : texte d'aide de `--rejuger-essai` | « refusé, rien n'est écrit pour la cellule ; la déclaration de reprise du script, elle, reste au journal » | `test_r2_texte_d_aide_du_rejugement` |
| Remarque 3 : `verifier` et l'empreinte du rejugement | La comparaison existait déjà, mais aucun essai ne la prouvait : essai ajouté | `test_r3_verifier_compare_l_empreinte_du_rejugement_a_l_essai` |
| Remarque 4 : lot orphelin et dernier relevé | Chaque lot porte un nom propre, `collisionneur-<cellule>-essai<N>`. Un dernier relevé précède l'annulation : un lot fini entre-temps est lu, ni annulé ni perdu | `test_v7_lot_sain_apres_coupure` ; `test_r4_lot_fini_au_dernier_releve_lu_et_jamais_annule` ; `test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire` |
| Remarques 5 à 7 | Remarque 5 : pour information. Remarque 6 (prix de Fable) : non changé, à décider à part. Remarque 7 : reste ouverte (section 8) | — |
| Plafond de l'appel non diffusé de Carbon | Ajout 1 : « aligné sur le flux (65 536) ». **Remplacé par l'ajout 2** : plafonds du lot ramenés à la limite versée, 32 768. Carbon est alors refusé en lot avant tout envoi (code 1, motif `REGLE_TEXTE_MIN`) ; Argon passe en lot à 32 768 | `test_v8_lot_plafond_aligne_sur_le_flux` (Argon 32 768 ; Carbon refusé, rien d'envoyé ni de compté) ; `test_a2_copie_anteriorite_repli_lot_refuse_pour_carbon` |

### 2.2 Réflexion des espèces de Google

Sources :
1. Page publique « Gemini thinking », variante `generateContent`. Adresse lue : `https://ai.google.dev/gemini-api/docs/thinking.md.txt?generate-content=true`, qui renvoie vers `https://aistudio.google.com/docs/thinking.md?generate-content=true`. Lue le 21 novembre 2026 à 17:42:41Z (`date -u`). Empreinte `fe0b8d8820b2ab7b8079bf1477e7871f850f6f5450f92f6b844866cade105892`. **Non versée** : c'est une provenance par transcription (R7). Copie : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/pages/thinking-generate-content.md.txt`.
   - Ligne 591 : `thinkingLevel` est « required for Gemini 4 ». Carbon et Argon admettent low, medium (le défaut) et high ; Neon admet low, medium, high (le défaut) et xhigh.
   - Ligne 939 : `thinkingBudget` est « deprecated ». Envoyé seul, il est ramené au niveau le plus proche ; envoyé avec un niveau, il donne une erreur 400.
   - Ligne 750 : corps REST `"thinkingConfig": {"thinkingLevel": "xhigh"}`.
   - Ligne 931 : un appel REST non diffusé de Carbon ou d'Argon rend au plus 32 768 jetons ; un appel en flux, au plus 65 536.
2. Référence de `generateContent`. Adresse lue : `https://ai.google.dev/api/generate-content.md.txt`, qui renvoie vers `https://aistudio.google.com/api-reference/generate-content.md`. Lue le 21 novembre 2026 à 17:42:04Z. Empreinte `829dabb8cb4b90bcbff71c53197ba8d834fc5dfb136294eaa9a1364a1b39a215`. **Non versée.** Lignes 2830 à 2849 : `thinkingConfig.thinkingLevel`, valeurs LOW, MEDIUM, HIGH, XHIGH. Copie : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/pages/generate-content.md.txt`.
3. **Pièces versées.** La page du modèle Neon (`2eadc192…`), ligne 153 : « Supported (low, medium, high, xhigh) ». Les journaux d'appels du dépôt montrent `"thinkingLevel": "high"` accepté (code 200) par `streamGenerateContent` pour Argon (06:28Z) et pour Carbon (06:29Z) le 21 novembre (`appel-argon-v1.json`, `99539ec5…` ; `appel-carbon-v1.json`). Comme le dit l'audit (section 2), le nom du champ et le niveau le plus haut d'Argon et de Carbon ne sont établis par **aucune page versée** : les pages 1 et 2 sont à verser par la mère.

| espèce | champ envoyé | niveau envoyé | repli déclaré, si le niveau est refusé | limite de sortie, flux / non diffusé |
|---|---|---|---|---|
| Argon | `generationConfig.thinkingConfig.thinkingLevel` | `high` | `thinkingBudget` 16 384 (SUPPOSÉ) | 32 768 / 32 768 (liste versée, ligne 594) |
| Carbon | idem | `high` | `thinkingBudget` 32 768 (accepté le 20 novembre) | **65 536** (page non versée, ligne 931 ; journaux versés) / 32 768 (liste versée, ligne 612) |
| Neon | idem | `xhigh` (**jamais envoyé** par le dépôt) | `thinkingBudget` 32 768 | 65 536 / 65 536 (liste versée, ligne 648 ; page versée, ligne 53) |

### 2.3 Garde commune des réglages de Google (ajouts 1 et 2), table à part

Le module `src/controle_ia/garde_google_v1.py` est sans état et sans réseau, sur la bibliothèque standard seule. Ses sources sont citées dans son en-tête. Il réunit les tables et trois fonctions :
- tables : `NIVEAUX_REFLEXION`, `NIVEAU_MAX_REFLEXION`, `LIMITES_SORTIE` (par espèce et par mode), `BUDGETS_REPLI`, `REFUS_GOOGLE` ;
- `verifier_reglages_google(espece, corps, provision, mots=None, mode="flux", niveau_attendu=None, budget_attendu=None)`, appelée avant l'envoi ; elle rend la liste des problèmes, et une liste vide permet l'envoi ;
- `defaut_reponse_google(fin, texte, pensees, blocage=None)`, appelée après la réponse ; elle rend `None` ou le nom du défaut ;
- `niveau_refuse(message)`.

La v8 l'importe (`garde_google`) et en reprend les noms. Chaque essai de Google porte au journal l'empreinte du module (`sha256_garde_google`). Un essai prouve que la v8 appelle bien la garde commune et pas une copie (`test_a2_le_script_appelle_la_garde_commune`).

| point | où dans la v8 | comportement | essais | mutations |
|---|---|---|---|---|
| (1) réglage explicite, au plus haut niveau | `executer_cellule` appelle la garde **avant le comptage**, sur les deux réglages prévus, puis **sur le corps même de chaque essai**. Elle est rappelée dans `appeler_gemini` et `appeler_gemini_lot` | niveau absent, non admis ou différent de l'attendu ; `thinkingBudget` présent avec un niveau ; `includeThoughts` non vrai. Le refus se fait avant l'envoi (motifs `REGLAGES_GOOGLE` et `REGLAGE_REFLEXION`, code 1) : rien ne part | `tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant` (onze cas) ; `test_v8_garde_reglages_un_essai_par_reglage_manquant` (huit cas) ; `test_v8_espece_de_google_sans_reglage_ne_part_jamais` (trois espèces) ; `test_v8_chaque_espece_de_google_part_au_niveau_le_plus_haut_journalise` | 8, 9, 10, 12, 29, 30, 31 |
| (1) repli déclaré au budget (ajout 2) | `executer_cellule`, juste après un `ECHEC` dont le message (HTTP 400) nomme le niveau (`niveau_refuse`) | un seul repli, au budget prévu (`BUDGETS_REPLI`), avec la ligne `repli_reflexion_declare` au journal, le champ `repli_reflexion` sur l'essai et le message « REPLI DÉCLARÉ » à l'écran. Le corps du repli est contrôlé par la garde (`budget_attendu`) : budget positif, au plus la provision, sans niveau. L'unique relance d'un repli part à la moitié du budget, journalisée | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` ; `test_a2_repli_temoins_autre_refus_et_une_seule_fois` ; `test_a2_repli_relance_corrigee_a_la_moitie_du_budget` ; `test_a2_garde_du_repli_au_budget` ; `tests/…::test_repli_declare_au_budget`, `::test_niveau_refuse` ; `test_a2_garde_par_essai_controle_le_corps_du_repli` | 12, 21, 22, 32, 40 |
| (1, retour) zéro pensée, ou pensées absentes = défaut | `juger` renvoie `SANS_PENSEES` (via `defaut_reponse_google`) ; `usage_gemini` lit un `thoughtsTokenCount` absent comme absent (`reflexion: None`, `pensees_absentes: true`), jamais comme zéro accepté | **code 10** (`CODE_PENSEES`) : coût réel compté, aucune cellule, aucune relance ; jamais renvoyée au même réglage. Au rejugement, au moins un jeton de pensée est exigé. `etat.md` signale les cellules déjà écrites sans pensées | `test_v8_reponse_sans_pensees_defaut_code_10_jamais_une_cellule` ; `…_en_lot_aussi` ; `test_a2_pensees_absentes_jamais_lues_comme_zero_accepte` ; `test_v8_rejugement_refuse_une_reponse_sans_pensees` ; `test_v8_etat_signale_les_cellules_de_google_sans_pensees` | 13, 14, 24, 39 |
| (2) plafond ≥ réflexion + 16 000, et au plus la limite versée | garde : `maxOutputTokens − provision ≥ 16 000`, `maxOutputTokens ≤ LIMITES_SORTIE[espèce][mode]`, provision positive ; `REGLE_TEXTE_MIN` étendue à Argon (32 768 − 16 384 = 16 384) ; en lot, plafonds ramenés à la limite non diffusée | Carbon est refusé en lot ; une réflexion nulle est refusée | `tests/…::test_limites_versees_par_mode`, `::test_limites_egales_a_la_liste_versee` (lit la liste versée), `::test_provision_nulle_ou_negative_refusee` ; `test_v5_regle_plafond_large_sain_et_bord` ; `test_v5_regle_plafond_large_temoin_argon_non_soumis` ; `test_v8_lot_plafond_aligne_sur_le_flux` | 19, 20, 33, 34, 35, 36 |
| (3) limite de mots : ⌈mots × 1,6⌉ < plafond de texte | garde, avec `mots = TOURS[tour]["mots"]` : 4 000 mots au plus, soit 6 400 jetons, sous 16 384 | refus avant le comptage | `tests/…::test_limite_de_mots_bord` ; `test_v8_garde_reglages_limite_de_mots_refuse_avant_l_envoi` (rien n'est compté ni envoyé) ; `test_v8_garde_reglages_mots_des_tours_compatibles` | 11, 37 |
| (4) motif de fin : MAX_TOKENS, SAFETY, RECITATION ou réponse vide = défaut | `defaut_reponse_google`, un essai par motif (seize cas). MAX_TOKENS, avec ou sans texte, et réponse vide : **une seule relance au réglage corrigé** (`NIVEAU_CORRIGE` : de « xhigh » à « high », de « high » à « medium » ; au repli, la moitié du budget), journalisée (`correction_reflexion`). Une reprise après un premier défaut part directement au réglage corrigé. Une relance corrigée en défaut n'est plus renvoyée. SAFETY et RECITATION sont un défaut, jamais une cellule, **sans relance** (section 6.1) | — | `tests/…::test_un_essai_par_motif_de_fin` ; `test_v8_defaut_de_reponse_un_essai_par_motif_de_fin` ; `test_v8_relance_unique_au_reglage_corrige_journalisee` ; `test_v8_relance_corrigee_en_defaut_jamais_renvoyee` ; `test_v8_reprise_apres_un_premier_defaut_part_au_reglage_corrige` ; `test_v8_refus_safety_recitation_jamais_une_reponse_ni_relance` ; `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage` (Argon, Carbon, Neon) | 15, 16, 17, 18, 38 |
| (6, audit) `annuler_lot` avale un échec | `annuler_lot` rend « annulation demandée » ou « annulation demandée, en échec (…) : lot peut-être encore en cours, à relever à la main », écrit dans l'échec de l'essai | — | `test_a2_echec_d_annulation_du_lot_dit_jamais_avale` | 23 |

## 3. Commandes exactes de reprise (GO-2026-11-21-69)

Les valeurs de Lazar sont des **arguments**, jamais écrites dans le code : ligne de reprise de 30 USD pour les mathématiques, de 17 USD pour la dérive v2. La v7 ne savait pas relever une ligne : un run garde sa ligne, et `--ligne-usd 30` est refusé sur un run ouvert à 28.

La v8 ajoute donc `--ligne-reprise-usd MONTANT --go-ligne GO`, qui ouvre une ligne neuve depuis la dépense du moment.
- Le journal la consigne : `ligne_reprise`, `go`, `depense_avant`, `ligne_precedente`.
- Elle remplace la ligne d'avant pour la garde par envoi (`ligne_courante`).
- Elle est idempotente par son GO : la même commande relancée n'ouvre rien, et le même GO avec un autre montant est refusé (code 1).

Lecture retenue : 17 et 30 sont le **reste** accordé à la reprise. Ils sont juste au-dessus des devis pessimistes de la v7 (15,73 et 28,45), et une ligne de 17 USD au total est impossible pour la dérive v2, déjà à 24. Le plafond `--plafond-usd` reste contrôlé à part, sur la dépense totale. Je le pose à la dépense totale plus la ligne de reprise, arrondie au dixième au-dessus, pour que la ligne soit la borne qui joue.

| dossier | dépense totale au journal versé | ligne du run | reste |
|---|---|---|---|
| percée | 10,2723 | 28 | 17,73 |
| dérive v2 | 9,8421 | 24 | **ligne de reprise de 17** (plafond 26,9) |
| antériorité | 14,7244 | 28 | 13,28 |
| mathématiques | 6,2326 | 28 | **ligne de reprise de 30** (plafond 36,3) |

Pour chaque dossier `D`, avant et après la reprise, avec `S=docs/notes/collisionneur-v9/collisionneur_v9_v8.py`, sur `PYTHONPATH=src` (sinon le script prend la garde dans le `src` du dépôt qui le porte) :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier $S src/controle_ia/garde_google_v1.py
PYTHONPATH=src .venv/bin/python -B $S verifier $D
```

Avant de lancer : l'ancienne session est arrêtée et versée (jamais deux écrivains sur un journal), et l'essai réel par modèle de la mère est fait (section 6.4).

```
# percée
PYTHONPATH=src .venv/bin/python -B $S devis-reprise runs/collisionneur-percee-controle-securite-v1-20261121-114810 --ligne-usd 28
GO_ID=GO-2026-11-21-39 PYTHONPATH=src .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie runs/collisionneur-percee-controle-securite-v1-20261121-114810 --plafond-usd 27.5 --ligne-usd 28 --reprise --rejuger-essai E3-T2-critique-croisee-E:1 2>&1 | tee -a runs/collisionneur-percee-controle-securite-v1-20261121-114810/journal-reprise-v8.txt

# dérive v2 (ligne de reprise de 17 USD, GO-2026-11-21-69)
PYTHONPATH=src .venv/bin/python -B $S devis-reprise runs/collisionneur-derive-de-regime-v2-20261121-131044 --ligne-reprise-usd 17
GO_ID=GO-2026-11-21-26 PYTHONPATH=src .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie runs/collisionneur-derive-de-regime-v2-20261121-131044 --plafond-usd 26.9 --ligne-usd 24 --ligne-reprise-usd 17 --go-ligne GO-2026-11-21-69 --reprise --rejuger-essai E3-T2-critique-croisee-E:1 2>&1 | tee -a runs/collisionneur-derive-de-regime-v2-20261121-131044/journal-reprise-v8.txt

# mathématiques (ligne de reprise de 30 USD, GO-2026-11-21-69)
PYTHONPATH=src .venv/bin/python -B $S devis-reprise runs/collisionneur-methodes-maths-v1-20261121-093850 --ligne-reprise-usd 30
GO_ID=GO-2026-11-21-23 PYTHONPATH=src .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie runs/collisionneur-methodes-maths-v1-20261121-093850 --plafond-usd 36.3 --ligne-usd 28 --ligne-reprise-usd 30 --go-ligne GO-2026-11-21-69 --reprise 2>&1 | tee -a runs/collisionneur-methodes-maths-v1-20261121-093850/journal-reprise-v8.txt

# antériorité : troisième envoi en flux, SANS --repli-lot (Fable, section 5.4 ; sous la v8, Carbon est de toute façon refusé en lot)
PYTHONPATH=src .venv/bin/python -B $S devis-reprise runs/collisionneur-anteriorite-pilier-v1-20261121-131029 --ligne-usd 28
GO_ID=GO-2026-11-21-39 PYTHONPATH=src .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie runs/collisionneur-anteriorite-pilier-v1-20261121-131029 --plafond-usd 26.4 --ligne-usd 28 --reprise 2>&1 | tee -a runs/collisionneur-anteriorite-pilier-v1-20261121-131029/journal-reprise-v8.txt

# fusionnée (nom complet …-20261121-153256 à reporter par la mère, section 4), quatre espèces
GO_ID=GO-2026-11-21-52 PYTHONPATH=src .venv/bin/python -B $S etage3 --fable --opus --argon --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie runs/<dossier fusionné …-20261121-153256> --plafond-usd 28 --ligne-usd 28 --reprise --rejuger-essai E3-T2-critique-croisee-D:1 2>&1 | tee -a runs/<dossier fusionné …-20261121-153256>/journal-reprise-v8.txt
```

Les clés et les GO viennent de la réflexion d'Opus (section 7) et de la contre-lecture de Fable (section 10). `devis-reprise` est une indication, jamais une condition.

J'ai fait tourner les quatre commandes sur des copies fabriquées depuis les journaux versés, avec de faux fournisseurs (`test_v8_copie_des_dossiers_commandes_de_reprise`) :
- toutes finissent au code 0, et `verifier` tient avant et après, avec 15 cellules ;
- les envois sont de 5, 5, 10 et 1 cellules (percée, dérive v2, mathématiques, antériorité) ;
- chaque envoi à Google porte `thinkingLevel: "high"` et aucun budget ;
- la même commande relancée n'envoie rien.

La commande de la v7 pour l'antériorité, avec `--repli-lot`, est refusée par la v8 au code 1, sans rien envoyer ni compter (`test_a2_copie_anteriorite_repli_lot_refuse_pour_carbon`).

## 4. Réserve par dossier : cellules d'Argon écrites sans réflexion (non rejouées)

Ces cellules ont été écrites par la v3 sous `thinkingBudget` seul, avec 0 jeton de pensées au journal versé. Elles ne sont pas rejouées. La v8 les signale dans `etat.md` (« Réserve (v9-v8) : cellules de Google écrites sur une réponse sans aucun jeton de pensée ») ; `verifier` ne les refuse pas. Dans un même dossier, le réglage d'Argon change donc entre les tours ; la note de reprise doit le dire.

| dossier | cellules d'Argon déjà écrites, 0 jeton de pensées | cellules d'Argon que la reprise enverra au niveau « high » |
|---|---|---|
| percée (…-114810) | E3-T1-conception-C, E3-T2-critique-croisee-C | E3-T3-reponse-C |
| dérive v2 (…-131044) | E3-T1-conception-C, E3-T2-critique-croisee-C | E3-T3-reponse-C |
| antériorité (…-131029) | E3-T1-conception-C, E3-T2-critique-croisee-C, E3-T3-reponse-C (les trois) | aucune |
| mathématiques (…-093850) | E3-T1-conception-C | E3-T2-critique-croisee-C, E3-T3-reponse-C |
| but (…-152615), fini | E3-T1-conception-C, E3-T2-critique-croisee-C, E3-T3-reponse-C | aucune |
| fusionnée (…-153256) | **non lu** : son nom complet n'est écrit ni dans le dossier du collisionneur ni dans les registres, et la recherche dans les journaux versés ne l'a pas trouvé. La mère le lit avant la reprise | à lire |

Carbon a réfléchi dans toutes ses cellules, de 21 534 à 44 101 jetons de pensées, sous le budget seul, donc au niveau que Google en déduisait. Ses cellules à venir partiront au niveau « high » : ce changement de réglage entre les tours est à déclarer de la même façon.

## 5. Essais

L'environnement est le `.venv` du dépôt, avec `PYTHONPATH=src`, sans aucune clé, et un `--basetemp` neuf dans mon bloc-notes.

| suite | résultat |
|---|---|
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8.py` | **346 passés, 1 sauté** |
| `tests/test_garde_google_v1.py` | **42 passés** |

La partie reprise de la v7 est adaptée là où la v8 change, avec la marque « v9-v8 ». Les adaptations portent sur :
- le niveau au lieu du budget ;
- la relance au réglage corrigé (deux envois avant le code 9) ;
- Argon sous la règle du plafond large ;
- la version ;
- la C-3 de la mère ;
- le cas « relevé refusé » retiré ;
- le dernier relevé avant l'annulation ;
- les essais du lot faits chez Argon, puisque Carbon y est refusé ;
- l'antériorité de la v7 reprise sans lot.

La section v8 compte 43 fonctions d'essai neuves (190 en tout, contre 147 en v7). Deux décorateurs de la v7, restés en double par mon outil de remplacement, ont été retirés.

## 6. Points à trancher par la mère

1. **SAFETY et RECITATION ne sont pas relancés.** La mère demande « relance une seule fois avec réglage corrigé ». Mais aucun réglage ne corrige ces refus, et le protocole du script dit « refus : enregistré tel quel, définitif dans le run, jamais reformulé ». Ces refus restent un défaut, jamais une cellule. Divergence non résolue ; une relance serait un changement d'une ligne, à essayer de nouveau.
2. **Le réglage corrigé est un niveau plus bas, au même plafond** (`NIVEAU_CORRIGE`), ou la moitié du budget en cas de repli. C'est la seule façon de libérer du texte sous la limite (page Interactions `a964d5cf…`, ligne 911 : « lower thinking_level »). En contrepartie, la relance ne réfléchit plus « jusqu'au bout » ; c'est un écart à « niveau le plus haut admis », relevé aussi par le contre-audit (section 4.2). L'autre choix possible : aucune relance, arrêt au premier défaut.
3. **Carbon en flux reste à 65 536, au-delà de la limite versée de 32 768** (liste versée, ligne 612). Ce plafond s'appuie sur la page non versée (`fe0b8d88…`, ligne 931 : 65 536 en flux, 32 768 en appel non diffusé) et sur les journaux versés : run « percée », sortie facturée 55 125 en flux. Ramener Carbon à 32 768 en flux empêcherait toute cellule de Carbon sous la règle des 16 000 avec la provision de 49 152. Je ne l'ai pas fait sans le mot de la mère. Argon reste à 32 768 en flux, comme la liste versée.
4. **Essai réel par modèle, sous le contrôle de la mère, avant toute reprise.** Si Argon au niveau « high » rend encore 0 jeton de pensées, chaque cellule d'Argon arrêtera son dossier au code 10. `xhigh` n'a jamais été envoyé à Neon. Le repli au budget d'Argon (16 384) est SUPPOSÉ.
5. **« Niveau le plus haut admis ou budget prévu »** (contre-audit, section 6). Chez Gemini 4, d'après la page non versée, un budget seul est ramené à un niveau. La v8 n'admet un budget qu'en repli déclaré, après un refus du niveau ; le refus de zéro pensée reste la protection. À trancher par Lazar.
6. **Un niveau sans budget ne borne plus la réflexion en jetons.** Seul `maxOutputTokens` la borne, et la provision n'est plus qu'un pire cas compté. La garde V-1 tient. La règle « réflexion bornée à part » est à relire (Fable, section 3.2 ; contre-audit, section 4.2).

## 7. Mutations

Chaque mutation est faite sur une copie dans mon bloc-notes : v8 et garde copiées, `PYTHONPATH` pointé sur la garde de la copie, les deux suites entières, arrêt au premier échec. Le témoin sans mutation passe : 384 passés, puis 385 après l'ajout d'un essai, avec 3 sautés et 1 désélectionné. L'essai désélectionné est `test_v5_prix_de_neon_egal_a_la_page_versee` : il lit la page versée par un chemin relatif au script, introuvable depuis une copie, et ne porte sur aucune ligne mutée. Outil : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/outils/mutations_v8_b.py` ; sortie : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/mutations-v8-b.txt`.

| n° | pièce mutée | mutation | premier essai en échec | prise |
|---|---|---|---|---|
| 2 | v8 | C-1 : un relevé refusé abandonne le lot | `test_v7_lot_sain_apres_coupure` | oui |
| 3 | v8 | remarque 4 : aucun dernier relevé avant l'annulation | `test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire` | oui |
| 4 | v8 | C-2 : relevé d'un lot échoué jeté | `test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule[lot` | oui |
| 5 | v8 | C-2 : ligne de flux illisible jetée | `test_c2_ligne_de_flux_illisible_gardee_dans_l_essai[carbon]` | oui |
| 6 | v8 | C-2 : corps illisible de Kimi jeté | `test_c2_kimi_corps_illisible_garde` | oui |
| 7 | v8 | C-3 : refus de crédit à coût zéro (comme la v9-v7) | `test_v7_refus_de_credit_echec_cout_zero` | oui |
| 8 | v8 | réflexion : budget envoyé au lieu du niveau | `test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision` | oui |
| 9 | v8 | réflexion : niveau le plus haut non exigé à la composition | `test_v7_budget_hors_borne_refuse_a_la_composition[niveau_reflexion-medium-niveau]` | oui |
| 10 | v8 | réflexion : Neon au niveau « high » | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 11 | v8 | garde (3) : limite de mots non passée à la garde avant l'envoi | `test_v8_garde_reglages_limite_de_mots_refuse_avant_l_envoi` | oui |
| 12 | v8 | garde : appelée sans le corps de l'essai (aucune garde par essai) | `test_a2_garde_par_essai_controle_le_corps_du_repli` | oui |
| 13 | v8 | (1, retour) : réponse sans pensées admise | `test_v8_reponse_sans_pensees_defaut_code_10_jamais_une_cellule` | oui |
| 14 | v8 | (1, retour) : pensées absentes lues comme zéro | `test_a2_pensees_absentes_jamais_lues_comme_zero_accepte` | oui |
| 15 | v8 | (4) : relance au même niveau, non corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 16 | v8 | (4) : reprise après un premier défaut au plus haut niveau | `test_v8_reprise_apres_un_premier_defaut_part_au_reglage_corrige` | oui |
| 17 | v8 | (4) : relance corrigée en défaut renvoyée par une commande suivante | `test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage` | oui |
| 18 | v8 | (4) : MAX_TOKENS sans texte arrête sans relance corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 19 | v8 | (2) : Argon retiré de la règle du plafond large | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[argon]` | oui |
| 20 | v8 | lot : plafonds non ramenés à la limite versée | `test_v8_lot_plafond_aligne_sur_le_flux` | oui |
| 21 | v8 | ajout 2 : aucun repli au budget si le niveau est refusé | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 22 | v8 | ajout 2 : repli silencieux (non journalisé) | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 23 | v8 | ajout 2 : échec d'annulation d'un lot avalé | `test_a2_echec_d_annulation_du_lot_dit_jamais_avale` | oui |
| 24 | v8 | rejugement : pensées non exigées | `test_v8_rejugement_refuse_une_reponse_sans_pensees` | oui |
| 25 | v8 | remarque 3 : empreinte du rejugement non comparée | `test_r3_verifier_compare_l_empreinte_du_rejugement_a_l_essai` | oui |
| 26 | v8 | remarque 4 : nom de lot générique | `test_v7_lot_sain_apres_coupure` | oui |
| 27 | v8 | ligne de reprise : une ligne neuve à chaque relance | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 28 | v8 | ligne de reprise : ignorée par la garde par envoi | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 29 | garde | garde (1) : thinkingLevel absent non relevé | `test_un_essai_par_reglage_manquant[niveau` | oui |
| 30 | garde | garde (1) : thinkingBudget présent avec un niveau non relevé | `test_un_essai_par_reglage_manquant[budget` | oui |
| 31 | garde | garde (1) : includeThoughts non contrôlé | `test_un_essai_par_reglage_manquant[pensées` | oui |
| 32 | garde | garde (1) : repli au budget, budget différent du prévu admis | `test_repli_declare_au_budget` | oui |
| 33 | garde | garde (1) : réflexion nulle (provision 0) admise | `test_provision_nulle_ou_negative_refusee` | oui |
| 34 | garde | garde (2) : texte sous 16 000 non relevé | `test_un_essai_par_reglage_manquant[texte` | oui |
| 35 | garde | garde (2) : limite versée non contrôlée | `test_un_essai_par_reglage_manquant[plafond` | oui |
| 36 | garde | garde (2) : limite non diffusée de Carbon à 65 536 | `test_limites_versees_par_mode` | oui |
| 37 | garde | garde (3) : limite de mots non contrôlée | `test_limite_de_mots_bord` | oui |
| 38 | garde | motif de fin : RECITATION lu comme une réponse | `test_un_essai_par_motif_de_fin[RECITATION-Texte-100-None-RECITATION]` | oui |
| 39 | garde | motif de fin : zéro pensée admis | `test_un_essai_par_motif_de_fin[STOP-Réponse.-0-None-SANS_PENSEES]` | oui |
| 40 | garde | repli : tout refus vaut refus du niveau | `test_niveau_refuse` | oui |

**39 mutations sur 39 prises** (les numéros vont de 2 à 40 ; le 1 est le témoin). La mutation 12 (garde par essai retirée) n'était pas prise au premier passage, parce que la garde faite avant le comptage couvre déjà les deux réglages prévus. J'ai ajouté `test_a2_garde_par_essai_controle_le_corps_du_repli` : le corps du repli au budget n'est vu que par la garde de chaque essai. Je l'ai rejouée ensuite (prise), avec le témoin rejoué (385 passés). Les autres mutations ont tourné avant l'ajout de cet essai, qui ne peut qu'en prendre davantage.

## 8. Restent ouverts

- La reprise d'un lot nommé au journal avant d'en créer un autre (remarque 4, conception à part).
- Les longues sorties au-delà de 65 536.
- Le délai du lot : un lot vise 24 heures, et le script l'annule au délai de l'espèce.
- La création non idempotente d'un lot.
- Le rapport de 1,6 jeton par mot n'est pas mesuré.
- Les deux pages de Google lues ce jour ne sont pas versées (R7) : copies dans mon bloc-notes (section 2.2), à verser par la mère.
- La garde n'est branchée que dans la v8. Les autres programmes relevés par l'audit et le contre-audit ne la portent pas encore (`envoi_v1.py`, consultation v6, commandes v3d et v3e, relais v4 qui bloque `thinkingLevel`, lanceurs).
- Le collisionneur v7, la v8 et ses essais sont cachés par `.git/info/exclude` (contre-audit, section 2) : ils ne seront pas poussés tant que la mère ne les verse pas. Le module et ses essais le sont aussi : `git check-ignore -v` les rattache à `.git/info/exclude`, lignes 94 et 95, et la v8 à la ligne 80.
- Je n'ai pas écrit de note de reprise déclarant les changements de réglage entre les tours : c'est à la session de reprise de l'écrire.

## 9. Écarts aux règles du mandat

- J'ai lancé une fois, par erreur, une commande de liste (`ls`) sur mon bloc-notes, hors de `docs/notes/collisionneur-v9/`. Je n'en ai rien tiré.
- Hors du dossier, je n'ai fait que :
  - ouvrir des pièces par leur chemin complet ;
  - vérifier des noms par `test -e` (le module et ses essais neufs, le contre-audit sous le nom deviné) ;
  - faire des recherches ciblées : `grep` sur `docs/notes` et `tests`, `git grep` sur les journaux de la branche des versements pour trouver le nom du dossier fusionné, sans résultat.
- Je n'ai rencontré aucun refus d'outil.

## Pièces écrites

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8.py` | `b85690310f5c4832a540bebe1156eb64caf98702cb0ed3d771933e1efac35d72` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8.py` | `4b0f4ab5a5248b9e56764d283015ed15aad8c3513d607fde2bbb098caa957153` |
| `src/controle_ia/garde_google_v1.py` | `04d233bd66c3fdbf80dbd04562e2405498614b39a82d12f82409ad150751d732` |
| `tests/test_garde_google_v1.py` | `ad022e3a9632c2704e2d76ab3be3995a0cd7d17e4254d862b1ba8b2824c81913` |

Chaque fichier porte son compagnon `.sha256`, fait par `sha256sum F > F.sha256` dans son dossier. Ce rapport aussi.
