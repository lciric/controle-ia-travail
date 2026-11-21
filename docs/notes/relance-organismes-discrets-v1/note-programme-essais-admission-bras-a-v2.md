# Note de livraison 3 — programme des deux essais d'admission du bras A, version 2 (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres)

- **Rédacteur** : Claude Fable 5.2, même agent que les livraisons 1 et 2, le 2026-11-21, sous le même mandat (`mandat-redacteur-fable-programme-essais-admission-v1.md`, `d3bc3628…`).
- **Point de départ** : mon travail de la livraison 2, et sa vérification `verification-corrections-programme-essais-admission-livraison2-v1.md`, lue en entier : « engageable après corrections », une correction neuve (V-1), trois mineurs neufs (m-a, m-b, m-c), l'essai de m-10 à verser, m-15 à fermer, trois exigences sur la conversion des euros, un essai instable.
- **État** : **livraison 3 finie, sous des noms neufs (`_v2`), 152 essais passent**, trois lancements de suite. Rien scellé, rien committé.
- **Interdits tenus** : aucun réseau hors de `127.0.0.1`, aucun appel à un fournisseur, aucune dépense, aucune clé lue ni affichée, `GO_ID` jamais fixé au poste, le chef jamais lancé sur une vraie ligne. Aucun devis changé.

## 1. Noms neufs, et fichiers `_v1` rendus à leur état scellé (R12)

| fichier neuf | parti de |
|---|---|
| `scripts/chef_essais_admission_bras_a_v2.py` | le chef de la livraison 2 |
| `scripts/relais_mistral_essais_admission_v2.py`, `scripts/relais_google_essais_admission_v2.py` | les relais de la livraison 2 |
| `tests/faux_fournisseur_essais_admission_v2.py` | le faux fournisseur, inchangé depuis la livraison 1, plus un mandataire qui ferme sans répondre |
| `tests/test_chef_essais_admission_bras_a_v2.py` | les essais de la livraison 2 |
| `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v2-gabarit.json` | le gabarit de la livraison 2 |

- Références internes mises à jour : imports des essais, noms et versions des relais, chemins et empreintes des relais au gabarit, commandes de l'en-tête du chef. Le gabarit des règles n'a pas changé : il reste `regles-admission-bras-a-v1-gabarit.md`. Le lanceur reste `scripts/lancer_relais_local_v1.py`. Les noms des pièces produites ne changent pas (`releve-verification-v1.json`, dossiers sous `runs/…-bras-a-v1/`).
- Les cinq fichiers `_v1` modifiés à la livraison 2 ont été rendus par `git checkout 16f948022 -- <fichier>` ; chacun répond « OK » à `sha256sum -c` sur son compagnon (le faux fournisseur `_v1`, jamais modifié, aussi). `git status` ne montre plus aucun fichier suivi modifié.
- **Conséquence, à dire** : la livraison 2 n'a jamais été committée ; son seul exemplaire était l'arbre de travail, et je n'en ai pas gardé de copie avant de continuer dans les fichiers `_v2`. **Je n'ai donc pas pu rejouer les essais neufs contre le code de la livraison 2.** La colonne « échoue sur la livraison 2 » ci-dessous est tenue par construction, dite cas par cas.

## 2. Corrections : défaut → changement → essai

| | défaut | changement | essais (cas sain et artefact) | échoue sur la livraison 2 ? |
|---|---|---|---|---|
| **V-1** | `rapport`, lancée pendant une file, figeait un rapport partiel ; l'amorce ne le refaisait pas ; `regles` rendait « ne tient pas » | `rapport` recalcule toujours du journal et n'écrit que si aucun rapport n'existe **et** que la file est close (`file_close` : événement « fin » de l'amorce, ou amorce plus en vie ; sans identifiant de processus au manifeste : non close). `regles` refuse une file non close, et refuse un rapport scellé qui ne répond plus au journal. L'amorce qui trouve un rapport qu'elle n'a pas écrit s'arrête : code 8 | `test_v1_la_commande_rapport_lancee_pendant_la_file_ne_fige_rien` ; `test_v1_l_amorce_ne_garde_pas_en_silence_un_rapport_qu_elle_n_a_pas_ecrit` | oui : la livraison 2 écrivait le rapport partiel, et son amorce sortait avec le code 0 |
| **m-a** | deux lancements simultanés passaient tous deux la garde 13 | verrou exclusif de la ligne (`<dossier>/<ligne>.verrou`, tenu par l'amorce, lâché par le système si elle meurt) ; les gardes sont rejouées sous le verrou | `test_ma_deux_lancements_simultanes_le_second_ne_part_pas` | oui : sans verrou, le premier lancement de l'essai partait (code 0 au lieu de 2) |
| **m-b** | la coupure de l'amont dépendait d'un délai de TCP | les deux relais posent `SO_LINGER` à zéro sur la prise de l'amont avant de fermer une connexion coupée (client parti, délai) : remise à zéro immédiate | `test_garde_19_artefact_file_coupee_a_sa_borne` (repris, point 6) ; `test_garde_19_la_fermeture_du_client_ferme_l_amont_meme_en_silence` | non mesurable ici : c'est une question de délai sous charge |
| **m-c** | un code 7 (clé vue) ne retenait aucune ligne suivante | `alertes_de_cle` relit, pour chaque dossier des lignes du fournisseur, le journal du relais (clé exacte vue) et le journal de l'amorce (forme de clé trouvée). `garde_cle_vue` (garde 7), avant tout départ : sans la pièce scellée de Lazar inscrite à `levees_cle`, la ligne ne part pas. La trace est aussi au relevé et au rapport (`cle_vue_dans_une_reponse`) | `test_mc_une_cle_vue_bloque_toute_ligne_suivante_du_fournisseur_jusqu_a_la_piece_de_lazar` | oui : la garde n'existait pas |
| **m-10** | essai manquant | essai du contre-lecteur versé : un mandataire qui ferme la demande de tunnel sans répondre | `test_m10_connexion_non_etablie_hors_signature_l_appel_est_rendu_au_compte_du_relais` | non : la correction était faite à la livraison 2 ; seul l'essai manquait |
| **m-15** | une configuration définitive pouvait mettre la vérification du devis à `null` | `controler_verification_du_devis` : en configuration définitive, la pièce est inscrite, présente à son empreinte et à son compagnon ; `null` n'est admis que d'une configuration d'essai | `test_m15_configuration_definitive_la_verification_du_devis_et_la_marge_de_change_sont_exigees` | oui : la fonction n'existait pas |
| **Euros** | conversion facultative ; âge du taux libre ; aucune marge | section 3 | `test_devise_affichee_obligatoire_taux_de_moins_de_24_heures_et_marge_de_change` ; `test_devise_mot_sur_la_sonde_et_console_la_conversion_est_exigee_et_le_taux_date` | oui : un solde en euros transcrit sans conversion passait ; un taux de 2019 passait |
| **Essai instable** | la garde 19 pariait sur 5 secondes | section 4 | — | — |

## 3. Euros

Le tableau du constat ne change pas : treize clés, un nombre en USD (devis, section 9). Hors du tableau :

- **Deux lignes obligatoires au constat**, quelle que soit la devise : `- devise affichée par la console de Google : XXX` et `- devise affichée par la console de Mistral : XXX` (trois lettres majuscules). Absente ou illisible : rien ne part.
- **Devise autre que USD** : la ligne de conversion est **exigée** pour chaque montant de ce fournisseur — crédit du constat, crédit vu du mot sur la sonde, solde et dépense vus de la lecture de la console. Forme inchangée : `- conversion de <clé> : MONTANT DEVISE ; taux TAUX USD par DEVISE ; source : … ; heure du taux (UTC) : AAAA-MM-JJTHH:MMZ`. La devise de la ligne doit être celle du constat.
- **Devise USD** : une ligne de conversion est refusée, comme incohérente.
- **Âge du taux** : au constat, 24 heures au plus avant le premier envoi de la ligne, jamais après. Au mot sur la sonde et à la lecture de la console, 24 heures au plus avant l'heure que porte la pièce : **lecture de ma part**, suivant le contre-lecteur ; la consigne ne parlait que du constat.
- **Marge de change** : paramètre `marge_de_change` de la configuration, une fraction. **Nulle au gabarit : aucune valeur n'est choisie.** Une configuration définitive qui ne l'inscrit pas ne part pas. Un crédit ou un solde vaut montant × taux × (1 − marge), au centime inférieur ; une dépense vue vaut montant × taux × (1 + marge), au centime supérieur. Toute conversion sans marge inscrite est refusée. Le contre-lecteur propose 2 % : à décider par Lazar.
- **Ce qui en découle, à dire à Lazar** : un constat en euros vieillit en 24 heures ; une ligne lancée le lendemain demande un taux relevé de nouveau, donc un constat neuf. La marge joue sur le seuil : à 2 %, il faut voir à la console un peu plus que le seuil divisé par le taux.

## 4. L'essai de la garde 19

L'essai attend maintenant les deux événements eux-mêmes, sans parier sur une durée : d'abord la ligne `client_ferme` du journal du relais, puis la fermeture vue par le faux fournisseur (délai de garde de 30 secondes, qui ne sert qu'en cas de défaut). Il éprouve la même chose qu'avant, et un peu plus : exactement une fermeture vue, un seul appel reçu. Avec `SO_LINGER` à zéro, la remise à zéro est immédiate.

Élargis de même : la fermeture en silence (elle lit le motif et la durée que le relais écrit lui-même, non l'horloge de l'essai) ; le délai total du relais de Mistral (fenêtre d'une seconde, contre un délai du client de 10 secondes). Je n'ai pas chargé la machine pour mesurer : la stabilité sous charge reste à constater par le contre-lecteur.

## 5. Écarts et lectures neuves, à juger

1. **Verrou de ligne** : un fichier `<ligne>.verrou` vit sous le dossier de la ligne dans `runs/…` ; il n'est jamais supprimé. Il est créé une fois les gardes passées.
2. **`regles` confronte le rapport au journal** : six compteurs. La garde 12 dit que le programme des règles « ne lit que le rapport » ; il lit ici aussi le journal, pour refuser un rapport figé. Aucune réponse n'est lue.
3. **Alerte de clé** : elle retient aussi un lancement refait sous la même ligne de calcul. La pièce de Lazar porte `- dossier de l'alerte : NOM` et `- clé révoquée et remplacée : oui`.
4. **Âge du taux** aux pièces autres que le constat : point 3.
5. Les écarts des livraisons 1 et 2 tiennent toujours (notes précédentes).

## 6. Reste ouvert

1. Vérification de cette livraison par le contre-lecteur ; rejeu sous charge de l'essai de la garde 19.
2. Les essais neufs n'ont pas été rejoués contre la livraison 2 (section 1).
3. La voie réelle des relais reste non éprouvée, `SO_LINGER` sous chiffrement compris.
4. m-14 (raccrochage du terminal) reste sans essai, accepté par le contre-lecteur.
5. Cas rare, à dire à Lazar avec les lignes de calcul : liste saine, puis connexion non établie au premier appel payant ; l'appel est compté sur sa durée et ferme la ligne.
6. La valeur de la marge de change : nœud de Lazar.

## 7. Commande d'essai et sa sortie

```
env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v2.py
```

Trois lancements de suite, après la dernière retouche :

```
152 passed in 73.69s (0:01:13)
152 passed in 72.53s (0:01:12)
152 passed in 72.30s (0:01:12)
```

**Un échec vu en route, corrigé** : sur huit lancements faits avant ces trois, deux ont échoué (une fois quatre essais, une fois un). Cause : des essais de bout en bout prenaient « le premier élément » du dossier d'une ligne, et tombaient parfois sur le fichier de verrou neuf. C'était un défaut des essais, non du programme ; ils ne lisent plus que les dossiers. Aucun relais resté vivant.

## 8. Empreintes sha256

| fichier | lignes | sha256 |
|---|---|---|
| `scripts/chef_essais_admission_bras_a_v2.py` | 2 913 | `9315f769462bad16114855fbdeefe6afe5750b53cb258a52eec74a31ad5c2c48` |
| `scripts/relais_mistral_essais_admission_v2.py` | 605 | `9a2bd10645149f4b33d883cacafd0561414a4e636f0a36e28eaca6728e0a0b0f` |
| `scripts/relais_google_essais_admission_v2.py` | 442 | `ec945644f78382c4f490855372e2c64881050e0ff73de146fc65d65b56d75e90` |
| `tests/faux_fournisseur_essais_admission_v2.py` | 324 | `75f709368c6256098bfed3c037582dd991b9b68754f968b778995ae38040e03f` |
| `tests/test_chef_essais_admission_bras_a_v2.py` | 2 618 | `bb82d43fd613b68d2719f6a33e7ef7d7f952e1cf1ff89b254aed370c58294318` |
| `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v2-gabarit.json` | — | `8936681b26debcb764450b147e8506d36e90c745d8d55d73757a71f91572d970` |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` | 23 | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` (inchangé, scellé) |

## 9. Chemins ouverts, déclarés

- Ouverts par moi : la vérification de la livraison 2, en entier ; les fichiers que j'écris. Rien d'autre de neuf.
- `git checkout 16f948022 --` sur cinq fichiers, et `sha256sum -c` sur six compagnons.
- Lus par le programme pendant les essais, comme avant : le lot des entrées nommé par le devis, les consignes et les règles du préenregistrement par empreinte, les modules du programme de forme ; la vérification du devis, empreintée.
- Aucun chemin interdit ouvert, listé ni empreinté.
