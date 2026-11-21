# Note de livraison 5 — programme des deux essais d'admission du bras A, version 4

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Fable 5.2). Aucun réseau, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue.

## Journal
1. Lue : la contre-lecture de la livraison 4 (`contre-lecture-programme-essais-admission-livraison4-v1.md`), en entier.
2. Six fichiers `_v4` créés par copie des `_v3` scellés (commit `616fb1504`), références mises à jour par un programme qui nomme les six fichiers un à un. Les `_v3` ne sont pas touchés.
3. Codés dans le chef `_v4` : C-1 (somme retirée tant que le lien entre clé et projet est levé), C-2 (réflexion facturée confrontée à la borne), m-1 (recharges survenues recopiées et dites), m-3 (défauts de Google comptés à part), m-5 (taux borné par l'heure de chaque montant). Essais neufs écrits. Premier lancement : 186 passent, 1 échoue (empreintes des relais au gabarit, à régénérer) ; régénérées.
4. Campagne de mutations par outil (m-2), hors du dépôt : 91 mutants, 9 survivants au premier passage ; un essai d'artefacts ajouté ; second passage : 91 tués sur 91.
5. Trois lancements sur l'état livré : 188 essais passent, trois fois ; aucun relais laissé vivant ; les cinq fichiers `_v3` suivis sont inchangés (`git diff --quiet`).

## 1. Fichiers de la livraison 5 (noms neufs, R12)

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v4.py` | `2996abffbab3d0293a62f6097a017b3562ef3e742b294bef49c5402c610aad34` |
| `scripts/relais_google_essais_admission_v4.py` | `9a7763b9dc97fb7c5eee3569314b763ba8a577e32b4076356477557c54780aa7` |
| `scripts/relais_mistral_essais_admission_v4.py` | `6ea05f35c43f715ad51bf82c7570fab00b397fa9fd862b1d561d8b211ab96806` |
| `tests/faux_fournisseur_essais_admission_v4.py` | `78266a774bf5f7aa4f588bf4f06d6d8bf983b0dd589a2042f529b76dbf0b99d2` |
| `tests/test_chef_essais_admission_bras_a_v4.py` | `796e924a1dd58c2cccc80228eab3b65fb379d745951507e75c1515d24ac8470e` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v4-gabarit.json` | `63a53802bd86715a032c63bebbe7b55c8872f05e82b28333edc8ea6ba1cece48` |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` (inchangé, toujours employé) | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` |

Les deux relais et le faux fournisseur ne changent que de nom et de numéro de version. Le gabarit `_v4` ne change que par sa version et les empreintes des deux relais. Tout le reste de la note de livraison 4 (`note-programme-essais-admission-bras-a-v3.md`) vaut encore : gardes, formes des pièces de Lazar, lignes de calcul attendues, écarts.

## 2. Les deux corrections

| défaut | changement | essais (cas sain et artefact) |
|---|---|---|
| **C-1** — la plus grande des deux dépenses était retirée dès que « deux projets distincts » valait « oui », même quand le lien entre chaque clé et son projet était levé | la plus grande des deux n'est retirée que si « deux projets distincts » vaut « oui » **et** si les deux clés « clé du projet constaté » sont constatées (aucune levée) ; sinon la somme. Le contrôle du crédit dit la règle employée, `lien_cle_projet_constate` et `cles_du_lien_levees` ; le manifeste, le relevé et le rapport le recopient | `test_c1_l5_lien_cle_projet_leve_la_somme_est_retiree_meme_sous_deux_projets_distincts` (l'exemple de la contre-lecture : 5 et 5 dépensés, 25 vus ; lien constaté : part ; lien levé, ou une seule clé levée : ne part pas), `test_c1_l5_la_regle_employee_est_au_manifeste_et_au_releve`, `test_credit_avenant_4_4_cas_sain_…` (adapté) |
| **C-2** — la borne déclarée, ou le budget, n'était jamais confrontée à la réflexion facturée | à chaque réponse lisible de Google, `thoughtsTokenCount` est comparé à la borne (`borne_dementie`). Au-dessus : « borne de réflexion démentie ». Dans la file : défaut journalisé, la file s'arrête, l'envoi n'est ni jugé ni compté parmi les réponses. À la vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure, portée à la fiche, au relevé (`bornes_de_reflexion_dementies`) et au nœud de Lazar | `test_c2_l5_file_reflexion_facturee_au_dela_de_la_borne_defaut_journalise` (deux formes ; à la borne : réponse ; un jeton au-dessus : défaut), `test_c2_l5_verification_borne_dementie_non_saine_et_sonde_comme_mesure` (deux formes), `test_c2_l5_unites_borne_dementie` |

Lecture déclarée pour C-2 : la contre-lecture laissait à Lazar le choix, dans la file, entre l'arrêt et un simple constat ; **à défaut, j'ai pris l'arrêt**. Le relais de Google ne confronte pas la réflexion facturée : il ne lit pas les compteurs de la réponse ; ce contrôle vit dans le chef seul.

Conséquence de C-1 à dire à Lazar : avec le constat tel que GO-2026-11-21-68 le permet (les deux clés du lien levées), la somme est toujours retirée. Après deux vérifications, chaque projet doit donc porter le seuil plus la somme des deux dépenses.

## 3. Les sept mineurs

| mineur | traité comment | essai |
|---|---|---|
| m-1 recharges survenues ignorées | lues (nombre et montant), refusées si incohérentes, recopiées au manifeste, au relevé et au rapport (`lectures_de_la_console`, `recharges_survenues_a_dire_a_lazar`), écrites au texte du rapport et sur la sortie d'erreur de l'amorce (« À DIRE À LAZAR ») quand le nombre dépasse zéro | `test_m1_l5_les_recharges_survenues_sont_recopiees_et_dites_a_lazar` |
| m-2 mutations par outil | campagne faite, section 4 | `test_m2_l5_artefacts_ajoutes_par_la_campagne_de_mutations` |
| m-3 défauts comptés parmi les réponses | `reponses_de_code_200` les excluait déjà en livraison 4 ; le rapport porte en plus `nombre_de_defauts_google` et `codes_200_recus` (ce que le fournisseur a rendu, défauts compris), une ligne de son texte, et une cause dans les règles. Les compteurs `refus` et `fins_par_sortie_maximale` gardent le compte du devis (ses règles 2 et 3) : un même envoi peut donc figurer à la fois comme défaut et comme refus — lecture à juger | `test_m3_l5_le_rapport_compte_les_defauts_de_google_a_part` |
| m-4 sonde sous la forme « budget » | **non codé, à dire** : le corps de la sonde porte alors le budget de la file avec un plafond de 256 jetons ; rien ne dit que le service l'admet ; un refus classerait l'issue à la ligne 12. À joindre à la décision de Lazar sur la forme | — |
| m-5 heure de référence du taux | le taux est au plus 24 heures avant le montant le plus tardif et au plus 6 heures après le montant le plus ancien ; seules les clés de crédit bornent | `test_m5_l5_le_taux_est_borne_par_l_heure_de_chaque_montant` |
| m-6 seuil de Mistral et lignes de Google | **non changé, à dire** : le crédit de Mistral sous 8,23 dollars arrête aussi une ligne de Google, parce que le constat est une seule pièce. Sans risque de dépense | — |
| m-7 deux fichiers hors périmètre modifiés par mon `sed` | **non touchés, sur consigne** : `scripts/epreuve_temoins_seuls_v3.py` et `scripts/lancer_course_affinage_mentors_v3.py` restent modifiés (`git status` : ` M`) ; à rendre par `git checkout`, sur décision de Lazar | — |

## 4. Campagne de mutations (m-2)

- Outil : deux fichiers hors du dépôt, `/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/mut/campagne.py` et `/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/mut/greffe_mutant.py`. Ce répertoire peut être effacé : si la campagne doit être rejouable, la session les verse au dépôt sous un nom versionné. Aucun fichier du dépôt n'est modifié par la campagne : le mutant remplace la fonction en mémoire, dans le processus d'essai.
- Mutations : chaque comparaison retournée, chaque « et » échangé avec « ou », chaque « non » retiré, chaque constante entière augmentée de un, chaque arrêt retiré, chaque retour remplacé par rien.
- Cibles : dans le chef, `garde_google_avant_envoi` (26 mutants), `defaut_de_reponse_google` (13), `borne_dementie` (6), `reglage_de_reflexion` (11), `controler_la_configuration_de_google` (17) ; dans le relais de Google, `defaut_du_corps` (18).
- Essais joués contre chaque mutant : ceux de la règle de Google, de C-2, de m-3, du gabarit et des corps.
- Premier passage : 82 tués, 9 survivants (corps sans plafond de sortie, au chef et au relais ; motif de fin absent ; réflexion ou plafond nuls). Second passage, après l'essai d'artefacts ajouté : **91 tués sur 91**.
- Limite : une seule mutation à la fois ; les fonctions qui appellent ces gardes ne sont pas mutées.

## 5. Reste ouvert

- Les deux décisions de Lazar sur la règle de Google (plafond et réflexion ; exemption de la sonde), les limites de mots, m-4, m-6, m-7.
- Le choix de C-2 dans la file (arrêt, pris par défaut).
- Rien n'a été joué sur un vrai fournisseur.

## 6. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v4.py`

Trois lancements : `188 passed in 92.99s`, `188 passed in 95.87s`, `188 passed in 96.93s`. La suite entière du dépôt n'a pas été lancée (mandat).

## 7. Chemins ouverts, déclarés

- Lue : la contre-lecture de la livraison 4. Écrits : les six fichiers `_v4` et cette note. Rien d'autre de neuf.
- Lus par le programme pendant les essais, comme avant : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté. Aucune substitution hors de mes six fichiers, nommés un à un.
