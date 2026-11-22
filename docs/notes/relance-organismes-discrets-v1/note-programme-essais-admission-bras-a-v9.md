# Note de livraison 10 — programme des deux essais d'admission du bras A, version 9

- État : LIVRÉE à la session le 22 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Opus 5.5), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`). Aucun réseau, aucun `git fetch`, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ni affichée, `GO_ID` jamais fixé.
- Deux décisions de la session mère sous GO-2026-11-21-69, venues de la vérification de la livraison 9 (`verification-programme-essais-admission-livraison9-v1.md`).

## Journal
1. Lue : la vérification de la livraison 9, par recherche de lignes (`outputTokenLimit`, exemption, échéance).
2. **Tentée et refusée par l'outil** : la lecture des dix premières lignes de `registres/go.md`, que le mandat permet. Je n'ai pas réessayé. La forme du registre est connue par la garde 8 elle-même (huit cellules ; `identifiant | accordé | type | périmètre | plafond | échéance | par | référence`).
3. Six fichiers `_v9` copiés des `_v8` scellés, noms changés par un programme qui les nomme un à un ; par `diff`, seuls les noms diffèrent. Outils de mutation en version 5 (`tests/mutations_essais_admission_v5/`). Les `_v8` et les outils version 4 ne sont pas touchés.
4. Deux essais hérités échouaient passé minuit (temps universel). Ils sont corrigés ; c'est un défaut des essais, non du chef (section 4).
5. Trois lancements : 240 essais passent, trois fois. Campagne de mutations : section 5.

## 1. `outputTokenLimit` absent : refus par prudence

**Aux vérifications de Google.** L'appel de liste, gratuit, rend la fiche du modèle. Si cette fiche est lisible, de code 200, porte l'identifiant figé, et n'a pas d'`outputTokenLimit` entier (`liste_sans_limite`), la vérification se ferme **avant tout appel payant**. Elle est classée à la **ligne 2** du classement (relue), close, nœud de Lazar, et rien n'est compté. Le motif exact (`MOTIF_LIMITE_ABSENTE`) :

> `outputTokenLimit` absent de la fiche du modèle rendue par l'appel de liste : refus par prudence (décision de la session mère, GO-2026-11-21-69 ; devis 4.4, ligne 2 relue) ; aucun appel payant ; nœud de Lazar

Une fiche illisible, d'un autre code ou d'un autre identifiant garde son classement d'avant (lignes 7 à 9 et suivantes du devis). Une limite présente et basse garde son motif de la livraison 9.

**À la file du juge.** La file ne fait pas d'appel de liste. La garde 10 exige donc, de **chacun des deux relevés** de vérification, que la dernière fiche lue (code 200, lisible) porte un `outputTokenLimit` entier au moins égal à `fournisseurs.google.sortie_max` (`limite_de_sortie_des_releves`). Sinon la file ne part pas, avant tout appel payant :
- limite absente, ou aucune fiche lisible : « garde 10 : relevé de GEMINI_API_KEY_2 : `outputTokenLimit` absent … ; la file ne part pas ; nœud de Lazar » ;
- limite sous la sortie maximale : « … `outputTokenLimit` (65535) sous la sortie maximale de la file (65536) : la file ne part pas ».

Les limites lues sont recopiées au contexte de la file, donc à son manifeste (`contexte.limites_de_sortie`) ; le rapport ne les reprend pas.

| essai | cas sain | artefact |
|---|---|---|
| `test_l10_artefact_output_token_limit_absent_refuse_avant_tout_appel_payant` | — | fiche sans limite : aucun appel payant, ligne 2, close, nœud, motif exact |
| `test_l10_sain_limite_presente_et_fiche_d_un_autre_code_garde_son_classement` | 65 536 rendu : les appels partent ; fiches 404, illisible, d'un autre identifiant : ancien classement | — |
| `test_l10_la_file_du_juge_exige_la_limite_des_deux_releves` | deux relevés à 65 536 ; la dernière fiche compte ; une fiche illisible est ignorée | limite absente, aucune fiche, fiche 404 seule, 65 535, dernière fiche sans limite |

Les relevés d'essai écrits par `Monde.releve` portent désormais une fiche à 65 536.

## 2. GO de l'exemption de la sonde, lu au registre

`exemption_de_la_sonde_go` n'est plus figé à `GO-2026-11-21-69` : la valeur est retirée des constantes de la section 9 (`AVENANT_2_FOURNISSEUR`).

**En configuration définitive**, toute ligne de Google refuse d'envoyer quoi que ce soit, avant tout envoi (`controler_go_de_l_exemption`, appelé par `gardes_avant_depart` juste après l'avenant 2), si la valeur ne remplit pas toutes ces conditions :
1. c'est un identifiant de GO (`GO-AAAA-MM-JJ-NN`) ;
2. le registre de la branche principale (`origin/main:registres/go.md`, lu par `git show` comme pour la garde 8) porte **une seule** ligne qui commence par lui, de huit cellules ;
3. son type est exactement `décision` ;
4. elle est accordée par `Lazar` ;
5. son échéance est lisible et **n'est pas passée au jour de l'envoi** (elle vaut encore le jour même) ;
6. son périmètre ou sa référence cite « exemption de la sonde » ;
7. aucune ligne `| révocation |` ne la cite.

**GO-2026-11-21-69** est admis sans la condition 6, puisque sa ligne accorde l'exemption sans la nommer, mais avec toutes les autres, échéance comprise. Il ne passe donc plus après le 22 novembre ; il ne passe pas non plus si sa ligne n'est pas de type `décision`, ce que je n'ai pas pu lire (journal, point 2).

Ce que la garde ne fait pas :
- **Configuration d'essai** : seule la forme de l'identifiant est contrôlée, comme avant.
- **Passage à blanc** (`a-blanc`) : la garde n'est pas jouée, comme la garde 8, puisque le registre n'est pas lu à blanc.

La ligne lue (identifiant, échéance, empreinte de la ligne) est recopiée au manifeste (`go_de_l_exemption`).

**Forme de la ligne de prolongation** acceptée (exemple éprouvé) :

```
| GO-AAAA-MM-JJ-NN | 2026-11-22 | décision | prolonge l'exemption de la sonde de borne des vérifications de Google (avenant 2, section 6) | — | 2026-11-30 | Lazar | avenant 2, section 6 |
```

| essai | cas sain | artefact |
|---|---|---|
| `test_l10_sain_le_go_de_l_exemption_lu_au_registre` | ligne de décision ; prolongation jusqu'au 30, admise le 30 ; GO-69 sans la citation le 22 ; Mistral et l'essai sans objet ; la ligne entière part | GO-69 le 23 : échu |
| `test_l10_artefact_le_go_de_l_exemption_absent_echu_ou_d_une_autre_forme` | — | absent ; deux fois ; type `calcul` ; échu ; échéance illisible ; sans la citation ; autre que Lazar ; sept cellules ; révoqué ; identifiant mal formé ; registre non lu ; la ligne entière refusée |

## 3. Configuration définitive de Google, à jour, champ par champ

À tirer du gabarit `_v9` sous un nom neuf, scellée. Les empreintes `""` sont à remplir par la session. Valeurs exigées par le chef v9 en définitive : section 9 de l'avenant 2 (`controler_avenant_2`) et ce qui précède.

**Premier niveau** (champs à changer par rapport au gabarit) :

```json
{
 "version": "configuration-essais-admission-bras-a-v9-google-AAAA-MM-JJ-v1",
 "etat": "definitive",
 "marge_de_change": 0.05,
 "marge_de_change_go": "GO-2026-11-21-68",
 "age_max_du_fixage_heures": 96,
 "recharge_comptee": false,
 "regime_file_google": "prudent",
 "temperature_retiree_d_avance": false,
 "constat": {"chemin": "docs/notes/relance-organismes-discrets-v1/constat-comptes-google-bras-a-AAAA-MM-JJ-vN.md", "sha256": ""},
 "constat_second": {"chemin": null, "sha256": null},
 "regles": {"chemin": "<fichier des règles scellé, non gabarit>", "sha256": "", "lignes_du_texte": [521, 529],
            "gabarit": "docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md"},
 "essai_local": null
}
```

- `avenant_2` est déjà au gabarit (`9d4b8a08…`), comme `devis`, `verification_du_devis` et `avenant` : on les garde.
- `temperature_retiree_d_avance` n'est pas lu par Google ; `false` est inscrit pour que la même configuration reste admise ailleurs.
- `constat` peut aussi être le constat complet ; ou bien la pièce de Mistral sous `constat` et celle de Google sous `constat_second`. La forme de la pièce de Google seul est à la note de la livraison 9, section 3.
- `age_max_du_fixage_heures` : 96 est proposé ; c'est à décider. Avec le fixage du vendredi 20, une pièce ne sert plus après le 2026-11-24 à 00:00Z.

**`fournisseurs.google`** (seuls les champs à changer) :

```json
{
 "sortie_max": 65536,
 "reflexion": {"forme": "niveau", "borne_declaree": 49536},
 "exemption_de_la_sonde": true,
 "exemption_de_la_sonde_go": "<GO de type « décision », au registre, non échu, qui cite « exemption de la sonde »>",
 "jetons_par_mot": "<à inscrire par le lecteur habilité>",
 "credit_min_avant_verification_usd": 28.28,
 "credit_min_avant_file_usd": 23.59,
 "credit_a_avoir_usd": 32.97
}
```

`consignes.appariement.limite_de_mots` et `consignes.couverture.limite_de_mots` sont à inscrire par le lecteur habilité, avec la contrainte : limite × jetons par mot ≤ 16 000. Le reste de `fournisseurs.google` comme au gabarit (modèle, prix, orthographes `XHIGH` puis `xhigh`, `marge_de_texte_jetons` 16 000, `sortie_max_sonde` 256, relais `_v9`, variables de clé).

**Les trois lignes de Google, sous `lignes`** (seuls les champs à changer ou à remplir) :

```json
{
 "verification-google-cle-1": {
  "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 3.0, "plafond_registre": "3,00 USD", "exces_possible_d_un_envoi_usd": 1.69,
  "delais": {"silence_s": 900, "total_s": 900, "relais_silence_s": 890, "relais_total_s": 890},
  "reserve_sortie_jetons": null, "lectures_console": [], "levees_cle": []
 },
 "verification-google-cle-2": {
  "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 3.0, "plafond_registre": "3,00 USD", "exces_possible_d_un_envoi_usd": 1.69,
  "delais": {"silence_s": 900, "total_s": 900, "relais_silence_s": 890, "relais_total_s": 890},
  "reserve_sortie_jetons": null, "lectures_console": [], "levees_cle": []
 },
 "file-neon": {
  "go": "GO-AAAA-MM-JJ-NN", "plafond_usd": 16.5, "plafond_registre": "16,50 USD", "exces_possible_d_un_envoi_usd": 7.09,
  "delais": {"silence_s": 2700, "total_s": 2700, "relais_silence_s": 2690, "relais_total_s": 2690},
  "reserve_sortie_jetons": null, "lectures_console": [], "levees_cle": [],
  "releves_verification": {"GEMINI_API_KEY": {"chemin": "runs/verification-cle-google-1-bras-a-v1/<dossier>/releve-verification-v1.json", "sha256": ""},
                           "GEMINI_API_KEY_2": {"chemin": "runs/verification-cle-google-2-bras-a-v1/<dossier>/releve-verification-v1.json", "sha256": ""}},
  "inscrit": {"nom_servi": "<nom servi des deux relevés>", "hote": "generativelanguage.googleapis.com", "orthographe_niveau": "<orthographe des deux relevés>"},
  "mot_de_lazar_sonde": null
 }
}
```

- Le reste des lignes comme au gabarit : numéros au devis, marques du périmètre, hôte, dossiers, appels et envois, entrées et partage de la file, `envois_max_par_relais`.
- `mot_de_lazar_sonde` : `null` si les deux sondes disent « comprise » ; sinon la pièce du mot, avec le crédit vu de chaque projet, et la file part de toute façon au régime prudent.
- Chaque relevé doit porter une fiche à `outputTokenLimit` ≥ 65 536 (section 1).

**Au registre**, pour chaque ligne de Google : la ligne courte de la note de la livraison 9, section 4, avec son plafond à la lettre et l'empreinte de l'avenant 2. Il faut en plus la ligne de **décision** qui accorde ou prolonge l'exemption (section 2), sous l'identifiant inscrit à `exemption_de_la_sonde_go`.

## 4. Deux essais hérités corrigés (sensibles à minuit)

- `test_ma_l7_un_constat_vieux_d_un_mois_est_refuse` comparait la date du fixage à celle du montant, alors que le fixage est daté du jour de l'heure du taux, dix minutes plus tard. Il échouait quand ces dix minutes passaient minuit. Il compare maintenant au jour de l'heure du taux.
- `test_age_du_fixage_l6_le_dernier_fixage_publie_admis_dans_sa_borne` lisait le constat à l'heure du module d'essai. Depuis la livraison 8, l'âge du fixage se compte aussi depuis l'envoi, et le cas sain de trois jours dépassait 96 heures passé minuit. L'envoi est maintenant fixé à dix minutes après la pièce.

Ces deux corrections ne touchent aucun contrôle du chef.

## 5. Campagne de mutations, version 5

Commande : `env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 .venv/bin/python -I tests/mutations_essais_admission_v5/campagne_mutations_v5.py toutes [SORTIE.json]`.

Six campagnes : celles de la version 4, et `livraison10`, qui mute `liste_sans_limite`, `limite_de_sortie_des_releves` et `controler_go_de_l_exemption`.
- Premier passage de `livraison10` : 51 tués sur 52. Le survivant ignorait une fiche illisible après une fiche saine ; il est tué par un cas sain ajouté.
- Passage final : section 7.

## 6. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v9.py`

Trois lancements avant la campagne : `240 passed in 102.09s`, `240 passed in 101.01s`, `240 passed in 107.71s` ; trois de plus sur l'état livré, section 7. La suite entière n'a pas été lancée (mandat).

## 7. Empreintes et sorties finales

La note n'est pas empreintée ici : la session la scelle. Fichier des règles inchangé (`4e99bade…`).

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v9.py` | `2be9c9463bbda8d52857c7e288490f69ab793971506a2271f402ab96e183caf4` |
| `scripts/relais_google_essais_admission_v9.py` | `55f9b14d7043016c14cfa8ad5df6c78c5ba69f2f0d5367f2faaab052acb1ee7c` |
| `scripts/relais_mistral_essais_admission_v9.py` | `dc3c053d04df5225eb6c183032a534bebe0b1617f4caa97b5c13be5109b9cd54` |
| `tests/faux_fournisseur_essais_admission_v9.py` | `c643559231a4f52ab64c0fffe2c880e6c25b4cd19e22ed34b6a520b8da2c799d` |
| `tests/test_chef_essais_admission_bras_a_v9.py` | `2318f878db360a65875b86e60e591c982dcd2209e2d287394762c77da145cf8c` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v9-gabarit.json` | `390f5aa580c64b726e74b0fa1c072a40beafd9c0e06d1cc424fae686a91feb18` |
| `tests/mutations_essais_admission_v5/campagne_mutations_v5.py` | `6696c484d6ccd9f79d51b6c1ac282d433e26e3959009ef1f0d87005abaab3c9a` |
| `tests/mutations_essais_admission_v5/greffe_mutant_v5.py` | `c064531b97041a3a0790aac774f2e99ca86c9c351972f98c53fae700138c400e` |

- Campagne entière, version 5, six campagnes : **572 tués sur 573**. Le survivant est un mutant de la garde 8 (date d'accord égale au jour même, `>` changé en `>=`), qui n'était tué, à la livraison 9, que parce que les essais tournaient le 21 novembre, date d'accord du registre d'essai. Un cas sain explicite est ajouté (`test_m2_l9_…` : ligne accordée le jour même). La campagne `livraison9`, rejouée ensuite : **120 tués sur 120**. Les autres campagnes ne lisent pas ce cas.
- Trois lancements de la commande d'essai sur l'état livré, après ce cas : `240 passed in 100.33s`, `240 passed in 101.53s`, `240 passed in 99.98s`.
- Aucun relais laissé vivant ; les `_v8` et les outils version 4 sont inchangés.

## 8. Reste ouvert

- Le type de la ligne de GO-2026-11-21-69 au registre est inconnu de moi : s'il n'est pas `décision`, il faut une ligne de décision neuve, ce que la mère prévoit de toute façon pour aller jusqu'au 30 novembre.
- `jetons_par_mot` et les limites de mots, par le lecteur habilité.
- `age_max_du_fixage_heures`.
- Rien n'a été joué sur un vrai fournisseur.

## 9. Chemins ouverts, déclarés

- **Lus** : la vérification de la livraison 9 (recherche de lignes) ; les `_v8` et `_v9` (par `diff` et par recherche de lignes) ; les outils de mutation version 4.
- **Tenté** : `registres/go.md`, dix premières lignes, refusé par l'outil, rien lu.
- **Écrits** : les six `_v9`, les deux outils version 5 et cette note.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucun `sed`, aucune substitution hors de mes fichiers, nommés un à un.
