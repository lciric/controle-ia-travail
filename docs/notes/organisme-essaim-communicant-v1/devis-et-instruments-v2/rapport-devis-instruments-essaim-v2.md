# Rapport — devis et instruments de l'essaim — v2, et devis à coût réduit

- Sous-agent (Claude Opus 5.5), 22 novembre 2026. Commande de la mère de 06:26Z, complétée par le mot du directeur GO-2026-11-22-26.
- **Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit.** La v1 est intacte. Chaque fichier de ce dossier a son compagnon `.sha256`.
- Pièces lues en plus de la v1 :
  - contre-lecture de la v1 et sa table `tables/pire-alternatif-v1.txt` ;
  - `calcul-devis-course-auto-conception-v1.py` (`8bd1e48a…`, l. 40) ;
  - `monde_riche_v4.py` (`4b165847…`, fonction `course`) ;
  - `relecture_fable_api_v3.py` (`95bea064…`, lignes du cache) ;
  - `devis-course-affinage-mentors-v5.md` (`52147009…`, marge et ligne de l'aiguilleur) ;
  - `devis_multi_generations_v2.py` (`710954c7…`), relu par programme.

## 1. Corrections

| défaut | ce qui change | fichier |
|---|---|---|
| D1 : bornes au pire 1,50 et 0,80 USD | bornes lues dans la pièce et utilisées : 1,60 (première espèce Claude) ; 0,90 (Kimi) ; 3,50 (10 / 50) ; formule de la pièce sinon (Fable 2,80 ; Argon et Carbon 2,90). Le contrôle porte désormais sur les **nombres** lus, éprouvé sur 5 artefacts | `calcul_devis_essaim_v2.py`, `epreuves_devis_v2.py`, `devis-essaim-communicant-v2.md` |
| D2 : un pire qui n'en était pas un | plafonds de session (3,00 et 0,25) ; messages au plafond du proposeur (supposé) ; tests des fausses et des copies (8) ; aiguillage des objets de contrôle ; relances (10 %) ; surcroît d'entrée du bras (a) (supposé) ; C.8 à 105 %. Estimation et pire côte à côte. Pire toutes espèces au haut : **290 228 USD** (v1 : 159 588) | idem |
| D3 : nombres sans pièce | provenance de chaque nombre (chemin, empreinte, ligne) ; plafond de l'aiguilleur à l. 40 de `8bd1e48a…` ; dénominateur 4 × 6 lu dans `monde_riche_v4.course` ; « 319 » remplacé par une valeur arrondie (instruments : 956 à 3 490 USD) ; les nombres restants sans pièce sont rangés sous `supposes` | idem |
| D4 : versions et candidats | numpy **2.4.6** (lu dans la sortie), Python 3.13.18 ; candidats 226, 225, 224 ; essai 1 déclaré non rejouable (script écrasé, R12), noms neufs désormais | `bases-sans-modele-v2.md` |
| D5 : définitions fixées après un essai | couverture « par cartes vraies » et témoin relâché déclarés **à préenregistrer** ; l'échec du monde 0 (E3) reste visible | `bases-sans-modele-v2.md` |
| oracle : nom de verdict non listé | `promu`, `rang` et `log_w` dans l'arbre **passent la v1** (code 0). La v2 n'admet que les clés de la grammaire et refuse tout champ inconnu (code 3) | `oracle_toutes_cartes_v67_v2.py`, `epreuves_oracle_v67_v2.py`, `oracle-toutes-cartes-v67-v2.md` |
| pilote | P-std : 12 mondes neufs, (a) et (c), Kimi, 3 générations, sans tests de mort ni aiguilleur ; test exact par inversion de signe contre B3 ; puissance 0,80 à 0,94 à δ = 0,15 ; **57 à 102 USD estimés, 204 USD au pire** ; règle d'arrêt du programme écrite | `pilote-instrument-essaim-v1.md`, `calcul_pilote_essaim_v1.py`, `calcul-pilote-essaim-v1.json` |
| coût réduit | leviers (a) à (e) chiffrés un à un et combinés ; le pilote d'abord donne ×23 à ×49 à espèce égale ; combinaison recommandée = le pilote ci-dessus | `devis-cout-reduit-essaim-v1.md`, `calcul_devis_cout_reduit_v1.py`, `calcul-devis-cout-reduit-v1.json` |

## 2. Épreuves

| épreuve | attendu | rendu | fichier |
|---|---|---|---|
| devis : pièce saine | passe | passe | `epreuves-devis-v2.json` |
| devis : 5 artefacts sur la pièce des tests (borne, vérificateur, fausses, tour central, tours au pire) | refus | refus ×5 | idem |
| devis : plafond de l'aiguilleur 0,25 → 0,30 ; 6 → 5 cartes | refus | refus ×2 | idem |
| devis : bornes au pire par test | 1,60 / 0,90 / 3,50 / 3,50 / 2,80 / 2,90 / 2,90 | identiques | idem |
| devis : totaux de la section D | 0 écart | 0 écart | `calcul-devis-essaim-v2.json` |
| oracle v2 : vrai, faux, malformé ; invariance ; canari ; mutation | tenues | tenues | `epreuves-oracle-v67-v2/epreuves-oracle-v67-v2.json` |
| oracle v1 : `promu`, `rang`, `log_w` dans l'arbre | constat | **passent** (code 0) | idem |
| oracle v2 : mêmes champs | refus 3 | refus 3 ×3 | idem |
| oracle : `log_w_max` (nom listé), v1 et v2 | refus 3 | refus 3 | idem |
| oracle v2 : source réelle | calcul | refus 2, absente | idem |
| pilote : sortie des bases v1 lue à son empreinte | conforme | conforme (`4dcdeacf…`) | `calcul-pilote-essaim-v1.json` |

## 3. Écarts et réserves

- Les nombres sans pièce sont marqués partout :
  - débit, utilisation et mise en route de la carte ;
  - remise par lots ;
  - part mise en cache ;
  - taux d'échantillonnage des tests ;
  - facteur de sortie courte ;
  - surcroît d'entrée du bras (a) ;
  - plafond des messages.
- Aucun modèle ouvert n'est nommé par une pièce lue : le choix revient au directeur.
- **Point à trancher avant le préenregistrement du pilote** : l'équité d'information entre B3 (2 000 instances brutes) et des proposeurs servis par une case d'environ 9 000 jetons (pilote, § 6, réserve 1).
- Aucun refus de permission, de classifieur ou de garde n'a été rencontré.
