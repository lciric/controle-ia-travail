# Contre-lecture, tour 3, du brouillon 3 du second addendum de B bis (contrôle carte-processeur v4)

- **Lecteur** : contre-lecteur neuf (R2), lettre de modèle C ; n'a écrit aucune pièce ; lecteur déclaré de T0.7 (exclu des lecteurs de P3-bis).
- **Date (UTC, `date -u`)** : de 2026-11-17T02:09Z à 2026-11-17T02:39Z (`date -u`, la seconde au scellement).
- **Pièce lue** : `brouillon-second-addendum-bbis-v3.md` (brouillon 3, non scellé), `2e2c1e075ee6f8ee5e3b04c372e6250dcdd1ac55111b4153d44b06fcd9878c8c`, compagnon vérifié conforme. Brouillon 2 (`ab66d5fa…`) : empreinte recalculée égale à celle que le brouillon 3 déclare. Rapport du tour 2 : `f4843729…` recalculée égale.

## 1. Verdict

**Scellable.** La seule correction exigée au tour 2 (m1) est appliquée, au caractère ; le différentiel contre le brouillon 2 ne contient rien d'autre que l'en-tête et la section 11 ; contrôle mécanique, essais rejoués par moi : conformes. Aucune correction exigée. Des remarques facultatives sont dites telles au § 5.

## 2. Correction du tour 2 appliquée fidèlement

m1 : « ancien » `(lettre de modèle C ; n'a écrit ni le brouillon 1` → « nouveau » `(lettre de modèle A ; n'a écrit ni le brouillon 1`. Le `diff` brouillon 2 / brouillon 3 montre ce remplacement et seulement lui sur la ligne « Brouillon 2 » (un seul caractère change). Appliqué.

## 3. Différentiel (diff)

Quatre blocs seulement : (a) titre (« brouillon 2 » → « brouillon 3 ») ; (b) lignes 7 à 11 : m1, nouvelle ligne « Brouillon 3 », statut réécrit pour dire tour 1 appliqué au brouillon 2 et tour 2 appliqué au brouillon 3 ; (c) intertitre du tour 1 et note « Texte du brouillon 2, gardé tel quel » ajoutés avant le texte inchangé du tour 1 ; (d) section « Tour 2 » ajoutée à la fin. Aucune ligne entre le titre du § 0 et celui de la section 11 ne change : ni fragment SA, ni chiffre, ni seuil, ni budget, ni hypothèse, ni issue. Vérifié par `diff` direct.

Vérifications des déclarations du tour 2 ajouté : empreinte du brouillon 2 (complète) exacte ; empreinte du rapport du tour 2 exacte ; verdict du rapport résumé exactement (corrections, une seule exigée, m1, aucun majeur) ; réponses R1, R2 et points pour la mère décrits comme non appliqués : conformes au rapport du tour 2. La phrase « le rapport laissait le point à trancher par la mère » est exacte (§ 4, m1 du rapport).

## 4. Revérifications

- **Contrôle mécanique** : rejoué par moi depuis le dossier du bloc-notes (git archive de `af0adb14` plus `code/`, interpréteur du dépôt) sur une copie du brouillon 3 : 25 fragments SA, chacun « ancien » unique, « nouveau » présent, R-PILE et point (7) égaux aux chaînes de `lecture_v3` ; CONFORME, code 0. Sortie identique, ligne à ligne, à `pieces/sortie-controle-fragments-second-addendum-v3.txt` (hors ligne d'en-tête de la date). Textes en vigueur `texte-en-vigueur-apres-second-addendum-v3.md` et `premier-addendum-lu-avec-le-second-v3.md` : reproduits octet pour octet (`cmp`). Les « anciens » de SA-1 à SA-25 se vérifient donc contre le texte scellé (T `0ae6210f…`) et le premier addendum (`f00eda8a…`).
- **Code v4** : les neuf fichiers de `code/` ne sont pas touchés depuis le tour 2 (aucun plus récent que le rapport du tour 2 ; compagnons `.sha256` tous conformes). Diff de `validation_imbriquee_v4` contre la v3 relu : contrôle à 3 époques pour les deux familles, déterminisme à 300 époques sur la carte, information à 300 époques de la linéaire écrite sans décider, `version_controle` « v4 » ; la mesure de dispersion est de l'information seulement, erreur d'exécution = « non faite ». Conforme au texte ; relu en diff, non ligne à ligne en entier (le tour 2 l'avait rejoué ; le code est à contre-lire à part, condition de GO-2026-11-16-11).
- **Essais rejoués** : `tests/test_t07bbis_second_addendum_v1.py` et `tests/test_t07bbis_controle_v3.py`, sur processeur, 4 fils, copie du bloc-notes : **51 passés en 17 min** (le rédacteur : 51 en 10 min 57 s). Couvrent le cas sain (dont anisotrope divergent à 300 époques passant en v4), l'artefact d'erreur de chaîne arrêté dès 3 époques, le non-déterminisme, les sondes en échec, l'horizon hors bornes, R-PILE, la seconde ligne `CODE-BBIS`, la mesure de dispersion.
- **Interdits** : aucun identifiant de modèle dans le brouillon 3 (recherche faite) ; aucun score ni donnée de 7a ou 7b lus ; rien lu sous `diag/`, `runs/`, `donnees/`.

## 5. Remarques facultatives (aucune correction exigée)

- **F1** : les pièces v1 de contrôle et de texte en vigueur nommées au § 0 et au § 9 restent celles du brouillon 1 ; le brouillon 3 le dit en section 11 et le contrôle v3 existe en copie. Acceptable tel quel.
- **F2** : la ligne « Brouillon 3 » dit « n'a écrit aucun des brouillons 1 et 2 » alors que les trois rédacteurs sont de la même lettre de modèle (A) ; la phrase parle de l'instance, non du modèle : exacte.
- **F3** : mes essais ont pris 17 min contre 11 min : sans importance, mais le coût processeur de la suite sur l'instance n'est pas à compter pour le feu.

## 6. Points pour la session mère

1. Rien n'est exigé : sceller sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md` avec compagnon, ligne `ADDENDUM-ECART-2-BBIS`, **avant** la seconde ligne `CODE-BBIS` (geste de la mère, aucun code ne le vérifie).
2. Restent dus avant le feu : contre-lecture du code v4 ligne à ligne (non faite ici), versement du code, recompte de `MIN_ESSAIS` (148 = 115 + 33, zéro marge, l'essai F saute sur l'instance), branche `donnees/t07-etape-b-bis-v2` à vérifier absente, pilote 595 ou 580, liste des témoins de destruction.
3. Entropie reprise et répétition à blanc : décisions de la mère, hors texte, comme au tour 2.
4. Incident de ma main : un premier lancement de la suite, borné à 580 s, a été coupé (7 essais) ; je l'ai relancé en entier ; sans effet sur le dossier. Aucun fichier du dossier modifié ; rapport seul écrit.
