# Note de livraison 2 — programme des deux essais d'admission du bras A (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres) — v1

- **Rédacteur** : Claude Fable 5.2, même agent que la livraison 1, le 2026-11-21, sous le même mandat (`mandat-redacteur-fable-programme-essais-admission-v1.md`, `d3bc3628…`).
- **Point de départ** : livraison 1 (commit `16f948022`) ; contre-lecture `contre-lecture-programme-essais-admission-livraison1-v1.md`, lue en entier : « engageable après corrections », cinq corrections, quinze mineurs.
- **État** : **livraison 2 finie, 144 essais passent** (121 de la livraison 1, 23 neufs). Rien scellé, rien committé. Les fichiers sont modifiés en place, sur consigne : **les empreintes compagnons de la livraison 1 ne répondent plus** aux cinq fichiers changés ; la session les refait.
- **Interdits tenus** : aucun réseau hors de `127.0.0.1` ; aucun appel à un fournisseur ; aucune dépense ; aucune clé lue ni affichée ; `GO_ID` jamais fixé au poste ; le chef jamais lancé sur une vraie ligne. Aucun devis changé.

## 1. Corrections : défaut → changement → essai

Chaque essai nommé échoue sur le code de la livraison 1 et passe sur la livraison 2. Vérifié : les essais neufs ont été rejoués contre une copie du code de `16f948022`, hors du dépôt (21 échecs sur 23 ; les deux qui passent sont un cas sain de C-4 et l'essai de m-11, que la livraison 1 tenait déjà à un morceau près).

| | défaut | changement (chef, sauf mention) | essais (cas sain et artefact) |
|---|---|---|---|
| **C-1** | un relevé ou un rapport non rendu effaçait la mémoire d'une ligne : compte de trois appels et plafond remis à zéro, gardes 10 et 20 aveugles | **L'état d'une ligne se lit dans tous ses dossiers.** `lancements_de_verification` : dernier relevé, puis, pour tout dossier postérieur sans relevé, son journal — chaque « envoi » écrit, et chaque « départ » sans « envoi » tenu pour un envoi coupé, compté au régime prudent sur le délai total de la ligne (ce coût est écrit à l'événement « départ »). `lignes_jouees` fait de même pour les files : sans rapport rendu, le rapport est reconstitué du journal, et la pièce à citer est le journal. `faire_rapport` compte les départs sans réponse. Sur un refus de la garde 18, un **relevé réduit** est écrit et scellé (valeurs fixées par le programme seulement), ligne close, code 8. La commande `rapport` écrit et scelle un rapport qui manque. Un dossier avec des envois mais sans manifeste, ou un journal illisible, arrête tout : nœud de Lazar. | `test_c1_releve_non_rendu_le_compte_de_la_ligne_ne_repart_pas_de_zero` ; `test_c1_depart_sans_reponse_au_journal_vaut_un_envoi_coupe_compte_au_regime_prudent` ; `test_c1_file_sans_rapport_rendu_reconstituee_du_journal` ; `test_c1_refus_de_la_garde_18_un_releve_reduit_est_ecrit_quand_meme` |
| **C-2** | la garde 13 bloquait à jamais une file dont aucun envoi n'était parti | Une file est partie si un de ses dossiers porte un « départ » au journal, des octets envoyés à l'amont au journal du relais, ou un rapport (`dossier_parti`). Un dossier sans départ est gardé tel quel et cité au manifeste du lancement suivant (`dossiers_anterieurs_sans_depart`). Journal illisible : tenu pour parti. | `test_c2_une_file_dont_aucun_envoi_n_est_parti_peut_partir` (clé oubliée, puis départ sain, puis second départ refusé) ; `test_c2_dossier_parti_unites` ; `test_garde_13_une_file_ne_se_rejoue_pas` repris |
| **C-3** | une sonde illisible, ou coupée avant tout nom servi, était classée « autre nom servi » | « Autre nom » seulement sur une réponse reçue entière dont un nom est présent et différent, ou multiple. | `test_c3_sonde_illisible_ou_sans_nom_reste_indecidee_la_verification_reste_saine` (Google illisible, Google sans nom, Mistral coupée ; artefact : nom autre, non saine) |
| **C-4** | un appel de liste en panne de transport laissait partir l'appel payant | Sans réponse du fournisseur à la liste (origine autre que l'amont, ou incident), le lancement s'arrête « à refaire » : aucun appel payant, rien de compté. | `test_c4_liste_sans_reponse_du_fournisseur_aucun_appel_payant` (trois cas) ; `test_c4_sain_liste_rendue_par_le_fournisseur_meme_en_erreur_l_appel_part` |
| **C-5** | une réponse qui fait tomber le programme de forme arrêtait la file, et l'envoi payé manquait au rapport | L'événement « envoi » est écrit **avant** le jugement de forme ; la forme suit dans un événement « forme ». Toute panne du programme de forme vaut « non conforme », cause `panne_du_programme_de_forme:<type>`. | `test_c5_reponse_qui_fait_tomber_le_programme_de_forme_la_file_continue_l_envoi_est_compte` ; `test_c5_l_envoi_est_au_journal_avant_le_jugement_de_forme` |

## 2. Les quinze mineurs

| | traité ? | ce qui est fait, ou pourquoi non | essai |
|---|---|---|---|
| m-1 | corrigé | un 502 d'origine `mandataire` sans la signature est une connexion coupée : ligne 6 à la vérification, reprise unique dans une file, compté à sa réserve ; il vaut « envoi coupé » (lecture de la console due) | `test_m1_refus_du_mandataire_sans_sa_signature_est_une_panne_ligne_6` |
| m-2 | corrigé | garde 8 : colonne « accordé par » égale à `Lazar` ; date d'accord lisible, au plus tard ce jour | `test_m2_et_m15_…` |
| m-3 | corrigé | `src/controle_ia/__init__.py` ajouté aux pièces du programme de forme, au gabarit | `test_gabarit_complet_et_refuse_par_le_chef` |
| m-4 | corrigé, parade appliquée | les deux relais cherchent la **valeur exacte** de leur clé dans tout corps reçu de l'amont (liste, erreurs, réponse, flux, même à cheval sur deux morceaux) et dans les deux en-têtes relayés, la masquent, et écrivent le booléen `cle_vue_dans_la_reponse` ; le chef rend le code 7. La valeur n'est ni affichée ni écrite ; le chef ne la connaît pas | `test_m4_le_relais_cherche_la_valeur_exacte_de_sa_cle_…` ; `test_m4_relais_de_mistral_la_cle_est_masquee_dans_le_flux` |
| m-5 | corrigé | garde 18 : une fenêtre ne compte que si elle porte au moins huit lettres ou chiffres | `test_m5_m6_m7_m12_unites` |
| m-6 | corrigé | champ `detail_de_l_incident` à chaque envoi (« flux de code 200 fini sans son marqueur de fin », motif du relais…) | le même |
| m-7 | corrigé | le schéma de l'adresse du dépôt distant n'est plus un terme interdit | le même |
| m-8 | corrigé | sortie d'erreur de l'ouvrier gardée (`ouvrier-sortie-erreur.txt`) ; code 9 pour une panne, avec le type et les lieux du code, sans le message | `test_m8_panne_de_l_ouvrier_code_9_trace_sans_message` ; fichier gardé : essais de bout en bout |
| m-9 | corrigé | une seule commande dans l'en-tête (`.venv/bin/python -I -B`) ; `interpreteur` au manifeste | sans essai propre |
| m-10 | corrigé | le relais de Google rend l'appel à son compte sur une connexion non établie hors signature | **sans essai** : je n'ai pas de moyen simple de produire cette panne sur la boucle locale |
| m-11 | corrigé | relais de Mistral : délai total tenu par une minuterie qui coupe l'amont | `test_m11_le_delai_total_du_relais_de_mistral_est_tenu_par_une_minuterie` |
| m-12 | corrigé | formes `sk-…` bornées par un début de mot | `test_m5_m6_m7_m12_unites` |
| m-13 | corrigé | commande `a-blanc LIGNE CONFIGURATION EMPREINTE` : gardes 9, 10, 12, 13, 14, 15, 17, 20, puis 3 et 6, sans `GO_ID`, sans rien lancer ni écrire | `test_m13_commande_a_blanc_sans_ligne_de_calcul` |
| m-14 | corrigé | l'amorce traite le raccrochage du terminal comme un arrêt propre, sauf s'il est déjà ignoré (`nohup`) ; l'en-tête dit de lancer sous `nohup` ou un multiplexeur | **sans essai** |
| m-15 | corrigé, à juger | le gabarit inscrit la pièce de la vérification du devis (`0bec479f…`) ; la garde 8 exige que la ligne de calcul cite son empreinte, au périmètre ou à la référence. Mettre la clé à `null` lève l'exigence | `test_m2_et_m15_…` |

Complément de C-4 **non retenu** : compter à sa réserve, et non à sa durée, un envoi dont le relais dit zéro octet envoyé. Ce serait un écart au devis (4.4 : seule la signature est exemptée). C-4 ferme déjà le cas du premier contact.

## 3. Solde de Google affiché en euros

**Tenable sans changer le devis.** Le devis veut, au tableau du constat, « un nombre » en USD, « net de toute conversion de monnaie » (section 9 ; 6.5). Le tableau ne change donc pas : la valeur inscrite reste un nombre en USD. La pièce porte en plus, **hors du tableau**, une ligne que le programme lit :

`- conversion de google_credit_utilisable_usd : 21,50 EUR ; taux 1,0700 USD par EUR ; source : … ; heure du taux (UTC) : AAAA-MM-JJTHH:MMZ`

Le programme refait le produit en décimal exact et refuse tout arrondi favorable : un crédit ou un solde ne dépasse pas le produit arrondi au centime **inférieur** ; une dépense vue n'est pas sous le produit arrondi au centime **supérieur**. Il exige une devise autre que USD, la même des deux côtés, un taux non nul, une source, et une heure du taux en temps universel, antérieure à l'envoi. La valeur en USD est ensuite comparée au seuil, comme avant. Mêmes lignes pour le mot sur la sonde (`conversion du crédit prépayé vu`) et la lecture de la console (`conversion du solde prépayé vu`, `conversion de la dépense vue`). Sans ligne de conversion, la valeur est tenue pour vue en USD.

Essais : `test_devise_constat_en_euros_converti_sans_arrondi_favorable` ; `test_devise_mot_sur_la_sonde_et_lecture_de_la_console`.

**Ce que le programme ne tient pas, à dire à Lazar** :
- il ne sait pas dans quelle devise la console affiche : il ne peut pas **exiger** la ligne de conversion ; c'est à la pièce de la porter ;
- le taux est une parole datée, non une mesure ; rien ne borne son âge, et le devis ne prévoit aucune marge de change. Un solde vu juste au seuil peut passer dessous si le cours bouge avant la file. Le devis charge 23,00 USD pour un seuil de 19,76 : cette marge couvre un écart de prix, non de change.

## 4. Écarts au devis et lectures neuves

Aucun critère, seuil, plafond ni délai du devis n'est changé. Sont neufs, à juger :

1. **C-4, plus prudent que le devis**, qui se tait : pas d'appel payant après une liste sans réponse du fournisseur.
2. **C-3, sonde mesurable mais sans nom servi** : « indécidée », non « comprise » (rien ne dit que le modèle demandé a répondu). La vérification reste saine ; c'est un nœud de Lazar de plus, non une file perdue.
3. **C-5** : une panne du programme de forme vaut « non conforme ». Le modèle peut donc ne pas tenir sur une réponse que le programme ne sait pas lire ; la cause est au rapport.
4. **C-1, départ sans réponse** : compté 200 jetons par seconde sur le délai total de la ligne, faute de durée connue. Chez Google, cela passe le plafond de la vérification : la ligne s'arrête, lecture de la console due.
5. **C-1, garde 20 sur une pièce reconstituée** : la lecture de la console cite l'empreinte du journal du dossier, faute de pièce finale.
6. **m-1** : le refus du mandataire sans signature vaut maintenant « envoi coupé », donc lecture de la console.
7. **m-15** : la ligne de calcul doit citer l'empreinte de la vérification du devis ; le devis (section 11) ne l'exige pas. Levé en mettant la clé à `null`.
8. **Fichiers modifiés en place**, sur consigne ; R12 voudrait un nom neuf.

Les écarts de la livraison 1 (note 1, section 3) tiennent toujours.

## 5. Reste ouvert

1. Contre-lecture de cette livraison, ou vérification des corrections par le même contre-lecteur (devis, 12.11).
2. La voie réelle des relais (chiffrement vers l'amont, tunnel) reste non éprouvée ; C-4 fait de l'appel de liste son premier essai, gratuit.
3. m-10 et m-14 sont sans essai.
4. Le masque de la clé retient la fin d'un morceau seulement si elle peut être un début de clé : sans effet attendu sur les délais de silence.
5. Durée de la suite d'essais : 67 secondes. Mêmes essais sensibles au temps qu'à la livraison 1.

## 6. Commande d'essai et sa sortie

```
env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v1.py
```

```
........................................................................ [ 50%]
........................................................................ [100%]
144 passed in 67.53s (0:01:07)
```

Trois lancements entiers de suite, 144 à chaque fois. Aucun relais resté vivant.

## 7. Empreintes sha256

| fichier | lignes | sha256 |
|---|---|---|
| `scripts/chef_essais_admission_bras_a_v1.py` | 2 750 | `02d5a2889d19ed9b4ae0c9f4b26a455090f5408c5dc6da60a853bb0162e58592` |
| `scripts/relais_mistral_essais_admission_v1.py` | 593 | `e29299833759e99717a7dc5f60d393b282699718650fac10dc90c57ca232850f` |
| `scripts/relais_google_essais_admission_v1.py` | 430 | `e75b429615998848a6968f8138fe9d9154218b67e824116f09cfd0b726ed6106` |
| `tests/faux_fournisseur_essais_admission_v1.py` | 321 | `311f9a89d1e96fb4504590e5c100a138c77e89ac9997e95dc0bd2b15014306fe` (inchangé) |
| `tests/test_chef_essais_admission_bras_a_v1.py` | 2 324 | `9652ff7666e7fb5314f033b57c7dd9a9b9148f7e873c37c7492e38aca7c27e1c` |
| `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v1-gabarit.json` | 481 | `77b3be1965e121df69c69f2d6104fcb8a2f778204275bb4e6a06b4ebfb958c1f` |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` | 23 | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` (inchangé) |

## 8. Chemins ouverts, déclarés

- Ouverts par moi : la contre-lecture, en entier ; les fichiers que je modifie. Rien d'autre de neuf.
- Empreintés par programme, non ouverts : `src/controle_ia/__init__.py` (m-3) ; la vérification du devis (m-15), déjà lue à la livraison 1.
- Lu par `git show`, pour l'épreuve « échoue sur la livraison 1 » : les trois programmes au commit `16f948022`, copiés dans mon bloc-notes, hors du dépôt, avec une copie des essais.
- Lus par le programme pendant les essais, comme à la livraison 1 : le lot des entrées nommé par le devis, les blocs de consigne et les règles du préenregistrement par empreinte, les modules du programme de forme.
- Une sortie de commande trop longue (un extrait du chef, par erreur de ma part) a été gardée d'office par le harnais hors du dépôt, sous `/root/.claude/projects/…/tool-results/`.
- Aucun chemin interdit ouvert, listé ni empreinté.

## 9. Journal (au fil de l'eau)

1. Contre-lecture lue. Plan : C-1 par reconstitution depuis le journal de chaque dossier (aucune impasse), relevé réduit sur refus de la garde 18 ; C-2 : une file est partie à son premier « départ » ; C-3 ; C-4 ; C-5 ; mineurs ; conversion de devise par lignes hors tableau.
2. Code écrit (chef et deux relais) pour C-1 à C-5, les mineurs 1 à 15 sauf ceux déclarés, et la conversion de devise ; gabarit complété (pièce de la vérification du devis, `src/controle_ia/__init__.py`, empreintes des relais). Les 121 essais de la livraison 1 repassent, sauf celui de la garde 13, à reprendre selon C-2. Restent : les essais neufs.
3. Essais neufs écrits (23) ; une lecture ajoutée en route (sonde mesurable sans nom servi : « indécidée »). 144 essais passent, trois lancements de suite. Essais neufs rejoués contre le code de la livraison 1 : 21 échouent, comme attendu. Note achevée.
