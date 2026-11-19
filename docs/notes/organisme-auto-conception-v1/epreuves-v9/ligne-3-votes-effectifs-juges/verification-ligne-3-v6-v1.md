# Vérification — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 6 du préenregistrement et du devis, sur les différentiels v4 → v5 et v5 → v6 — v1

- **Vérificateur** : agent neuf du « modèle O ». Je n'ai écrit aucune des pièces lues (versions 1 à 6, calculs, rapports des rédacteurs, vérifications antérieures, compte rendu arrêté) (règle R2).
- **Heure** (`date -u`) : 2026-11-19T22:23:33Z (relevée en cours de travail). Processeur seul ; aucun appel de modèle, aucune dépense, aucun tirage du banc, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main` et des `git show`.
- **Branche** `lot/compte-organisme-v1`, tête `991e4229233e864def74b525b09d28685c331bb7` (commit d'une autre ligne, après celui de la version 6, `12535e609…`) ; le dossier de la ligne 3 est inchangé entre ces deux commits (`git diff --stat` vide).
- **Aucune commande sur un chemin sous `archives-reponses-modeles/`** : ni ouverture, ni empreinte, ni liste, ni taille, ni test d'existence. Aucune carte ouverte. L'empreinte `ba65c411…` du fichier des cartes n'est donc **pas** vérifiée par moi : elle est reprise des versions 1 à 5. Aucun outil n'a refusé.

## 1. Empreintes (recalculées sur disque ; les 33 compagnons du dossier rendent « OK »)

| pièce | empreinte |
|---|---|
| préenregistrement v6 | `b040d24cbef61a2a61ca724b097e6857d3465bba4d21f16d2cffc0241220ab94` |
| devis v6 | `34e87d90f8f3060f7eecd0abdce84721078cea6a97247f909e4cb4d0f2a6c26a` |
| rapport du rédacteur v6 | `bca6c1c1a216e86695f5a730b86b326546bd9879123f654254492dd73d14d03e` |
| référence : préenregistrement v5 / v4 | `915fbe4b7ab17d83b9d39b92f21fd4cf4d52394d974b8b5b9c6e9e589d2fed12` / `26bb22145e8d90dc0d38382361e50fe6d59b3a7cd82d56d25dafeb10fe97cd84` |
| référence : devis v5 / v4 | `43bcb1c887de4f8e683510ceac5871ff4c07464f6dfe396480937567b8761c4f` / `0051297ab2bb2fc6552d5354d06d4301ff082570f6b81cdcbd7ac7224f4f95fe` |
| référence : vérification v4 | `597b97bb1ac78f97b570fb5ded3cd2d71c8f222e165a029d7380e8d5d89b37a8` |
| référence : compte rendu arrêté v5 | `9031205f353a970036f87bf41531899d223c154b9edc33219bd04e9938498fb5` |
| mandats v5 / v6 | `a5864b782ff9ac0079f06012e8b207d04f5c605479f198d6fbc63800e37053eb` / `dae0606be4002f6173b3dd2755a58c0b38ff4a719e3b6669e45459c3abfb48b8` |
| rapport du rédacteur v5 | `c03a952eaefe61420948bfcc86b4c79c85bad50c45e12ea07a4869eb47aab83e` |
| `calcul_predictions_ligne_3_v2.py` / sortie | `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` / `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724` |
| `calcul_predictions_ligne_3_v1.py` / sortie | `282b5d518685059371e160c74e0e1a05b1f22593a20275924712320509216434` / `d0ea89843d450f9bbe983726e0cbccc9f5bf359cef50d54aab5571a4e7af9faf` |
| `calcul_devis_ligne_3_v3.py` / sortie | `9364867e7a21d28e2b30f3f73d3f0a6604cecfa3eee5efb46eb2331ba3dcbaf8` / `1a13fe2756a5587398e122c17700fab6472350d6c38975d58c1c3cf337ad6cf6` |

## 2. Registre sur main (contrôle laissé par le vérificateur arrêté)

- `git fetch origin main` fait ; tête de main à mon heure : `79da594ce55fb0f9941be082b02f3a7c01136838` (plus récente que celle du rédacteur, `5ee19a44…`).
- `registres/go.md` : au commit `2ec5da6c…` → `5750c7fabeb66968e340f8dcc6aeec5ffe1a676a5415d7f726b3fb4b99fefe32` (**juste**) ; au commit `d4449d327…` → `78efe8782883f4de91fa6d06d84d1b93498f8bb3ee5a70e111ffc2d9cd8c1275` (juste) ; à `5ee19a44…` et à la tête `79da594c…` → `1570ae2b65621e490b1a07dae69b9829320896410944b24c67bba9e1c20c5faa` (même fichier ; juste).
- Comparaison par programme, ligne par ligne : **GO-2026-11-19-55 à -77 égales à l'octet aux trois commits** (`2ec5da6c`, `d4449d327`, tête) ; -78 à -82 égales entre `d4449d327` et la tête ; -83 neuve à la tête (absente des deux autres).
- **GO-77** : texte conforme à ce que portent les versions 5 et 6 (décision 1 (a), décision 2 (a), mot du 16:18:19Z). **GO-81** : « reprise du travail neuf du compte de l'organisme », mot du 21:47:18Z ; ses cinq recommandations visent la ligne 1 et le palier 0b, non la ligne 3, ce que la version 6 dit exactement. C'est bien le mot de reprise qu'attendait le mandat v6.
- GO-83 (neuve, 22:00Z) nomme une « ligne neuve hors de la ligne 3 » : rien à porter dans ce texte.

## 3. Différentiels, par programme

| différentiel | morceaux (diff -U0) | annoncé | tous expliqués ? |
|---|---|---|---|
| préenregistrement v4 → v5 | 24 | 24 (28 points) | oui, sauf le morceau de l'en-tête déjà relevé par le compte rendu arrêté (correction 3), rétabli en v6 |
| devis v4 → v5 | 8 | 8 (11 points) | oui |
| préenregistrement v5 → v6 | 16 | 16 (23 points) | oui |
| devis v5 → v6 | 5 | 5 (8 points) | oui ; renvois seuls, aucun chiffre |

**v4 → v5** (lu à la main, morceau par morceau, contre la table « Différentiel avec la version 4 ») : titre, statut, auteur et date, mots de Lazar et registre, mandat v5, document « vérification v4 », calcul v2 et empreintes, Q3, Q4 (décision 1), P5 quater, P10, « Seuil », bras « double rendu », règle de portée, garde de recouvrement (quatre conditions, repli), appels, lecture par colonne (décision 2), ordre, liste d'arrêt, plafond (i) et (ii), réserve 11, « Contre-lecture », annexe A (deux puces), différentiel. Chacun vient d'une des neuf corrections, des quatre conditions de la mère, des deux décisions de GO-77 ou d'un ajout nommé à « Hors vérification, ajouté par le rédacteur en version 5 ». Seul écart : à l'en-tête, « par le même contre-lecteur » devenu « par le modèle du contre-lecteur », absent de la table v5 (correction 3 du compte rendu arrêté ; traité en v6, ligne 3 de la table v6). Devis v4 → v5 : statut, « Écrit par », mot de Lazar (GO-77), calcul, § 5 (i) (correction 7), § 6 bis (deux décisions), § 7, différentiel : propre.

**v5 → v6** : titre ; statut ; auteur et date (correction 3) ; mots de Lazar et registre (GO-81) ; mandats ; document « compte rendu arrêté » ; empreintes, devis, non lus ; Q3 (correction 1, conditions) ; P5 quater (correction 4) ; garde, chapeau et (1) (règle de l'empreinte, mandat point 3) ; (3), (4), (5), repli (corrections 1 et 2, conditions, ajouts déclarés) ; ordre ; liste d'arrêt (correction 1 avec écart déclaré, deux artefacts) ; « Contre-lecture » ; annexe A ; différentiel. Chaque morceau est à la table « Différentiel avec la version 5 ». Rien d'autre ne change (aucun montant, aucun appel, aucune hypothèse, aucune règle de lecture d'un verdict).

## 4. Les neuf corrections de la vérification v4 (lettre contrôlée par programme : texte neuf présent, ancien absent du corps)

| n° | lettre | juste | note |
|---|---|---|---|
| 1 | oui en v5 (1 fois) ; en v6 modifiée par la correction 1 du compte rendu, son début gardé à la lettre | oui | — |
| 2 | oui : appels (1), « Seuil » (1), annexe A (1) ; ancien texte absent | oui | devis non touché, juste (il était déjà juste) |
| 3 | oui : P5 quater et réserve 11 ; « réfutée partout » absent du corps | oui | bascules chiffrées par un calcul neuf, comme demandé (règle R6) |
| 4 | oui, placée après « ne porte pas de mot (règle R4). » | oui | — |
| 5 | oui, après la phrase « Lecture d'ensemble prédite » | oui | — |
| 6 | oui ; « la théorie ne le permet pas » absent du corps | oui | — |
| 7 | oui, au préenregistrement et au devis § 5 | oui | — |
| 8 | oui, après « Reprendre la mesure … ligne neuve. » | oui | — |
| 9 | oui (en-tête, « Contre-lecture ») | oui | le changement non déclaré de la parenthèse est rétabli en v6 |

## 5. Les quatre corrections du compte rendu arrêté

| n° | lettre | juste | note |
|---|---|---|---|
| 1 | puce « Repli » : texte donné présent à la lettre (1 fois) ; Q3 : phrase donnée présente, ancienne absente ; liste d'arrêt : « (règle de repli, « Garde de recouvrement ») » présent, « (Q3) » absent du corps | oui, sous les corrections 1 et 2 ci-dessous | écart à la lettre à la liste d'arrêt, voir § 7 |
| 2 | fin du (3) : phrase donnée, à la bonne place ; (4) : « d'un texte de carte, messages d'erreur et traces d'exception compris » | oui | — |
| 3 | parenthèse rétablie au texte donné (1 fois au corps) ; « par le modèle du contre-lecteur » ne reste qu'à la table | oui | — |
| 4 | « entre δ = 0,385 et 0,386 (bascule 0,3853) » ; « entre δ = 0,543 et 0,544 (bascule 0,5438) » ; anciens libellés absents | oui | égaux à la sortie (§ 8) |

## 6. Conditions de cloisonnement de la mère, au texte

Sources : mandat v6, point 2 ; aussi, sur main, `registres/decisions.md` R-3917 (15:39:45Z, quatre conditions) et R-3934 (16:44:40Z, cinquième condition, « repli compris ») — la version 6 ne les cite pas (correction 4).

- **(1) Entrée** : écrite (chemin, empreinte, 94 cartes « toutes et elles seules », refus de tourner sinon, aucun autre fichier de l'archive). Règle de l'empreinte (mandat, point 3) : écrite au (1), à l'en-tête, à l'annexe A ; l'empreinte se prend par le programme seul, la valeur attendue en constante du code. **Tient.**
- **(2) Lecture** : écrite (par programme seulement ; `meta` retiré au chargement ; bardeaux en mémoire seulement). **Tient.**
- **(3) Sortie** : la liste fermée est écrite au (3), mais trois champs que le texte fait rendre à la garde ailleurs n'y sont pas : le nombre de rejeux (il y est par la phrase de la correction 2 et par le (5)), le nom de classe et le lieu d'une exception (le (5) les fait « entrer » dans la liste), et **l'écart du repli « et sa cause », déclaré « au rapport de la garde »** (puce « Repli »), qui n'est dans aucune liste. Avec l'artefact « rapport portant un champ hors de la liste fermée : refus d'écrire », le code devrait soit refuser d'écrire le rapport du repli, soit tenir une liste que le texte ne dit pas en un seul lieu. La condition de la mère est « la garde ne rend que ce que le texte dit » : la liste doit être dite entière, et la cause nommée par une valeur fermée, non par un texte libre. Correction 1. Aucune sortie, message d'erreur et trace d'exception compris, ne peut porter un texte de carte : **tient**, sous la correction 1.
- **(4) Contrôle** : écrit à la lettre du mandat (contre-lecture du code de la banque, avant la première ouverture ; « sans ce contrôle passé et écrit, la garde ne tourne pas »). **Trou avec le repli** : le second déclencheur du repli est un contrôle du (4) « non conforme » ; la puce « Repli » énumère les règles de lecture qui valent sous le repli, mais ne dit pas que le (4) doit être passé sur le chemin du repli (extraction des sept cartes) et sur les autres points. Lu à la lettre, le repli ferait tourner la garde alors que le contrôle du (4) n'est pas « passé » : c'est contre la condition (4). Correction 2. La source « mot vers 16:39Z » de la confirmation de lecture n'est pas écrite ailleurs que par inférence : correction 4.
- **(5) Rejeux et sorties** : écrite (au plus cinq rejeux sans le mot de la mère ; premier passage non compté ; refus au sixième avant ouverture ; erreurs et traces dans la liste fermée ; rien d'autre ne sort). Lecture « cinq rejeux = six ouvertures au plus » : conforme au mot « rejeu » et à R-3934 ; la question est bien rendue à la mère. **Trou** : tout le compte tient au journal à ajout seul « lu au lancement », mais rien ne dit ce qui se passe s'il est absent ou illisible ; sans règle, un journal perdu remet le compte à zéro, en silence (règle R5 : aucun repli silencieux ; une garde s'éprouve sur un artefact). Correction 3.
- **Repli** : déclencheur mécanique unique, le même aux trois endroits (la puce le pose ; Q3 et la liste d'arrêt y renvoient ; l'annexe A aussi) : **tient**. « Sans rien regarder des cartes » : écrit. Écart au manifeste (et au rapport) : écrit. Sept cartes seulement, mêmes règles : écrit. Sous la condition (5) : écrit (ajout). Sous la condition (4) : non écrit (correction 2).

## 7. Écart déclaré et ajouts du rédacteur

- **Écart à la lettre de la correction 1, liste d'arrêt** : juste et nécessaire. Appliquée à la lettre, la correction laissait « si la mère refuse l'ouverture par programme (règle de repli, « Garde de recouvrement ») » : un seul des deux déclencheurs, ce que le compte rendu lui-même relevait comme défaut et que le mandat interdit. Les trois changements (« si la règle de repli se déclenche » ; « aux mêmes règles de lecture » ; « écart écrit » → « écart déclaré ») sont à la table du différentiel (ligne 20). Observation de forme, sans correction : la table des quatre corrections (ligne 1) et le rapport ne nomment pas tous les trois (« écrit » → « déclaré » n'y est pas) ; la table du différentiel suffit.
- **Tenue de la condition (5)** (journal, compte, refus, exceptions) : utile ; sans elle la condition n'est pas contrôlable au (4). Gardée, sous la correction 3.
- **Deux artefacts** (journal à cinq rejeux ; exception provoquée) : justes (règle R5). Un troisième manque (correction 3).
- **Deux phrases du repli** (compte des rejeux continu ; aucun repli hors des deux déclencheurs) : justes ; la seconde comble ce que le texte donné retirait. Gardées.
- **Règle de l'empreinte au (1)** : conforme au mandat, point 3.
- **Vérification sur deux différentiels, interdit en tête du mandat du vérificateur** : justes.

## 8. Rejeu du calcul des prédictions

Joué par moi depuis mon bloc-notes (`python3 -I -B` sur le chemin absolu du programme du dossier, sortie écrite dans mon bloc-notes ; Python 3.13.18) :
- `calcul_predictions_ligne_3_v2.py`, deux fois : `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724` les deux fois, **égales à l'octet à la sortie versée** (`cmp`).
- `calcul_predictions_ligne_3_v1.py` : `d0ea89843d450f9bbe983726e0cbccc9f5bf359cef50d54aab5571a4e7af9faf`, égale à l'octet.
- Clé par clé v1 → v2 : aucune clé retirée ; « version » change ; une clé ajoutée, « bascules_de_la_clause_i_du_double_rendu ». Différentiel des programmes : en-tête, une partie ajoutée, le nom de version ; aucune ligne de calcul existante touchée.
- Bascules lues dans la sortie : suiveur séduisant, un changement de mot « réfuté » → « tient » **entre 0,385 et 0,386, bascule 0,3853** ; lecteur séduit (troisième lecteur), **entre 0,543 et 0,544, bascule 0,5438** ; suiveur repoussant, un seul changement, « réfuté » → « sans prise » entre 0,999 et 1, jamais « tient ». Ce sont les valeurs écrites au texte ; « un seul changement de mot par loi » est juste.

## 9. Ce que je n'ai pas vérifié

- L'empreinte `ba65c411…` et le compte de 94 du fichier des cartes (interdit ; elle se prendra par le code de la banque).
- Le code de la banque et de la garde (non écrit) ; le code de l'organisme.
- Le mot de la mère de 16:39Z : aucune source écrite autre que le mandat v6.
- Le calcul du devis n'est pas rejoué (aucun chiffre ne change ; rejoué à l'octet par la vérification v4).

## 10. Corrections

Toutes au préenregistrement v6 ; aucune ne change un montant, un appel, une hypothèse, une règle de lecture ni une décision de Lazar. Chaque texte ancien figure une fois et une seule dans la v6 (contrôlé par programme).

1. **(3) Sortie — liste fermée entière.** Remplacer « la décision de la garde (banque passée ou refusée) ; l'identifiant de chaque témoin refusé. » par « la décision de la garde (banque passée ou refusée) ; l'identifiant de chaque témoin refusé ; le nombre de rejeux (condition (5)) ; pour toute exception, le nom de sa classe et le lieu dans le code (condition (5)) ; sous le repli, la mention « repli sur sept cartes » et sa cause, nommée par l'un des deux déclencheurs de la puce « Repli », sans autre texte. Aucun autre champ. » À l'annexe A, remplacer « aux mêmes règles, écart déclaré au manifeste), » par « aux mêmes règles, écart déclaré au manifeste et au rapport de la garde), ».
2. **Repli sous la condition (4).** À la fin de la puce « Repli », après « et d'ici là la garde ne tourne pas. », ajouter : « Sous le repli, la condition (4) vaut aussi : la garde ne tourne que si la contre-lecture du code de la banque a rendu « conforme », par écrit, tous les autres points du (4) et le chemin du repli lui-même (extraction des sept cartes du même fichier, mêmes règles) ; sinon, ni garde ni repli, la banque n'est pas scellée et la mère est saisie. »
3. **(5) Journal des rejeux absent ou illisible.** Remplacer « il ne repart jamais de zéro, et il est au rapport, parmi les comptes de la liste fermée. » par « il ne repart jamais de zéro, et il est au rapport, parmi les comptes de la liste fermée. Le journal est créé vide avant le premier passage, par un geste écrit au manifeste ; journal absent ou illisible au lancement : le programme refuse de tourner avant d'ouvrir le fichier, et la mère est saisie avec les seuls comptes. » À la liste d'arrêt, ligne « recouvrement », remplacer « journal portant déjà cinq rejeux, sans mot de la mère : refus de tourner avant toute ouverture » par « journal portant déjà cinq rejeux, sans mot de la mère : refus de tourner avant toute ouverture ; journal des rejeux absent ou illisible : refus de tourner avant toute ouverture ».
4. **Provenance des mots de la mère (règle R6).** À l'en-tête, remplacer « Je n'ai lu ces mots que par ce mandat, qui en est ici la seule source écrite. » par « Je n'ai lu ces mots que par ce mandat. Deux d'entre eux sont aussi écrits au registre des décisions, sur main : R-3917 (mot de 15:39Z, quatre conditions) et R-3934 (mot de 16:44Z, cinquième condition, repli compris) ; `registres/decisions.md` au commit `79da594ce55fb0f9941be082b02f3a7c01136838`, `8cd3e08cb59c290fe4b9990be54ce9abdb63f82f939139d2ee4e980b3b85a0a8`. Le mot de 16:39Z n'a pas d'autre source écrite que ce mandat. » Au (4), remplacer « (lecture de cette condition confirmée par la mère, mot vers 16:39Z) » par « (lecture de cette condition confirmée par la mère, selon le mandat de la version 6, point 2, condition (4)) ».

Le devis v6 est propre : aucune correction. Les corrections 1 à 3 portent sur des conditions de cloisonnement (trous de la garde, non de forme) ; la 4 est de provenance. Toutes sont localisées ; une version 7 (nom neuf) se vérifie sur son seul différentiel, sans commande sous `archives-reponses-modeles/`.

## Verdict

**Scellable après corrections** (quatre, numérotées au § 10 ; le devis v6 tel quel).
