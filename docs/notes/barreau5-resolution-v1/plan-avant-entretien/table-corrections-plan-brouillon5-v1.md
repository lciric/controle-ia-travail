# Table des corrections — plan « sabotage ou empreinte de l'adaptateur », brouillon 5 — v1

Écrite par le rédacteur (Claude Fable 5.2) dans la nuit du 19 au 20 novembre 2026, pour la vérification du différentiel par le même contre-lecteur (Claude Opus 5.5). Pièce de travail.

- Pièces produites : le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md`, le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md`, la fiche `fiche-v5-lazar-v1.md`. Empreintes : compagnons `.sha256`.
- Elles partent du texte du brouillon 4 (`dbe66dc9…`), de son devis (`084cd547…`) et de la fiche v4 (`a88a3a12…`), et de la vérification `verification-plan-brouillon4-v1.md` (`a091eed2…` : « scellable après ces couples »), lue en entier ; ses outils : sceaux vérifiés.
- **Méthode.** `fabrique-brouillon5-v1.py` charge la liste `COUPLES` du programme du vérificateur (`outils-verification-plan-brouillon4-v1/couples-verification-brouillon4-v1.py`) et l'applique telle quelle, dans son ordre ; puis il applique mes écritures (`sections_brouillon5_v1.py`). Chaque « avant » doit se trouver une fois, sinon rien n'est écrit. Compte rendu : `sortie-fabrique-brouillon5-v1.txt`. Les programmes sont écrits par l'outil d'écriture ; les trois pièces sont leurs sorties.
- Validateur du dépôt sur le texte : aucun problème.
- **Le différentiel est fermé** : 20 couples, 16 écritures « mots de Lazar », 13 écritures « tenue du brouillon ». Rien d'autre.

## 1. Les 20 couples de la vérification du brouillon 4

Tous appliqués à la lettre ; chaque « après » est présent à l'octet dans la pièce finale (vérifié par le programme, après mes écritures).

| repère | pièce | touche | où |
|---|---|---|---|
| W-M1a | texte | lecture | « Hypothèse », hypothèse de travail (d) |
| W-M1b | texte | lecture | « Métrique », demi-épreuve E2a |
| W-M1c | texte | lecture | « Hypothèse », table des rivales : une ligne « ouverte » de plus |
| W-M1d | texte | lecture | « Hypothèse », table des rivales, ligne « force » |
| W-M2a | texte | lecture | phrase de l'issue « sabotage » |
| W-M2b | texte | lecture | table des rivales, ligne « force et trace réunies » |
| W-M2c | texte | lecture | « Seuil », le mot « sabotage » |
| W-M2d, W-M2e | texte | lecture | « Puissance », taux d'erreur ; ce que la construction ne ferme pas |
| W-M2f | texte | lecture | « Ce qui change au brouillon 4 » |
| W-M2g, W-M2h | fiche | lecture | « Où en est le texte » |
| W-m1a | texte | lecture | « Contre-lecture », traitement de la vérification du brouillon 3 |
| W-m2a | texte | lecture | « Puissance », petit sabotage mêlé à une force |
| W-m3a | texte | formation | « Liste d'arrêt », point 14 |
| W-m3b | devis | formation | § 4, compteur commun |
| W-m4a à W-m4d | devis | devis | en-tête ; § 3, horloge et prix vus ; § 7 |

Aucun couple refusé ni modifié. Les nombres que ces couples citent (« vérification du brouillon 4 ») viennent des outils du vérificateur, que l'en-tête du texte cite maintenant.

## 2. Les mots de Lazar, écrits comme décidés (lignes `GO-2026-11-19-86`, `-87`, `-88` de `registres/go.md`, relues)

| décision | texte | devis |
|---|---|---|
| accord de calcul, plafond commun de 200 USD (`-86`) | en-tête, ligne des décisions ; « Calcul et dépense » ; « Nœuds », état ; marqueur M-3 | en-tête, « Plafond » ; § 3, ligne « ensemble » |
| enveloppe de relance de 56 USD, à part (`-87`) | « Calendrier », borne de la relance ; « Calcul et dépense » ; « Nœuds » | § 3, relance ; § 6, recharge |
| aucun comptage d'avance (`-88`) | « Nœuds » | — |
| répétition générale et points d'ancrage si le code de lecture est prêt, sinon modèle jouet (`-88`) | plan, point 18 (deux retouches) ; « Nœuds » | § 2, ligne de la répétition |
| garde des activations sur un volume de 200 Go, prix porté à Lazar avant dépense, replis sinon (`-88`) | « Données gardées » ; « Nœuds » | § 5 (a) |
| témoin à changement bénin après l'entretien (`-88`) | « Nœuds » | — |
| niveau déclaré de 95 % sous huit familles (`-88`) | « Critères », sous huit familles ; « Nœuds » | — |

« Le code de lecture est prêt à temps » est écrit par la règle mécanique que le calendrier portait déjà : la ligne `CODE-LECTURE-B5F` est inscrite à la fin de la formation. À dire si Lazar l'entendait autrement.

La condition de l'accord de calcul est recopiée : il ne vaut qu'après `SCELLEMENT-B5F` et `CODE-FORMATION-B5F`, et si le devis scellé ne dépasse ni l'attendu (88 à 132 USD) ni le plafond. Aucun chiffre du devis ne change au brouillon 5.

## 3. Tenue du brouillon (13 écritures)

Texte : titre ; date ; statut ; paragraphe « Ce qui change au brouillon 5 » ; documents (la vérification du brouillon 4 et ses outils) ; renvoi au devis du brouillon 5 (deux fois) ; calendrier, ligne « avant le départ » et premier risque, mis à l'état du jour ; « Contre-lecture » (vérification du brouillon 4 rendue, son traitement ; différentiel en attente) ; marqueur M-10. Devis : titre ; puce « Brouillon 5 » et texte chiffré. Fiche : titre ; une phrase d'état (les huit décisions sont prises).

## 4. Les marques « [à confirmer par le rapport v4] » : gardées

Le rapport v4 du développeur n'avait pas de compagnon `.sha256` à l'écriture, et la mère n'en avait pas donné l'empreinte : je ne l'ai pas ouvert. Les sept phrases restent marquées, cinq au texte et deux au devis (liste : table des corrections du brouillon 4, § 5). Le statut, « Ce qui change au brouillon 5 », le calendrier, « Contre-lecture » et le marqueur M-11 citent la marque sans rien supposer. La levée se fera par un erratum dès que l'empreinte du rapport arrive ; si le rapport contredit une phrase, je le dirai sans trancher.

## 5. Ce que je signale

- La fiche v5 n'était pas dans la liste des sorties : je l'ai faite parce que deux des 20 couples la visent. Elle ne demande plus rien à Lazar.
- Le constat W-m3 dit : « si la garde de dépense du code compte toutes les instances sous une même ligne, le rapport v4 doit le dire ». C'est une huitième question pour le rapport v4, sans marque dans le texte.
- Reste sans couple, signalé par le vérificateur : la dernière ligne de la sortie scellée de `calcul-devis-formation-trois-membres-v1.py` écrit « relecture 20 … = 203 » ; la coupure de la relecture à 39 adaptateurs est 21 et la somme 204. Le devis a raison ; le calcul scellé n'est pas refait.
