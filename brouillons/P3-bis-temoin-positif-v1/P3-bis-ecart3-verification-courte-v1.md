# P3-bis, écart 3 (R-2492) — vérification courte du brouillon 2 de l'addendum 3 — v1

- Vérificateur : sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`), auteur de la contre-lecture
  `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart3-contre-lecture-v1.md`
  (`fac5fb91af1b4abc11eb52c4ca4b43231e29261bdbb0f6f39f6535cf21048cd3`). Ce n'est donc pas un lecteur neuf : c'est le
  contre-lecteur qui vérifie que ses corrections sont appliquées, à la demande de la mère.
- Écrit le 2026-11-13 de 08:36 à 08:37 UTC (heures relevées par `date -u`).
- Demande : message de la mère relayé dans la session ; mêmes interdits que pour la contre-lecture. Aucun `fetch` (les
  commits étaient dans le clone local), aucun commit, aucune poussée, aucun appel externe, aucune dépense, aucun chemin
  interdit ouvert, aucun refus d'un contrôle.
- Pièce vérifiée : `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-3-relance-credit-v1-brouillon2.md`, lue par
  `git show 09fd663f:…`, empreinte recalculée
  `02674ff7693d4dee069abea8d48fd27826f98455084dbf4da4724d8bf72cb103`, égale à son compagnon et au message de la mère.
  Méthode : diff entier contre le brouillon 1 (`4f7bb2b0…`), 24 blocs, tous lus.

## Verdict

**Scellable tel quel.** Les six corrections exigées sont appliquées à la lettre ; rien d'autre n'a changé que ce que dit
la section « Changements depuis le brouillon 1 » ; le code est inchangé. Une remarque de forme (R1), à régler dans
l'en-tête au scellement, sans brouillon 3.

## Corrections exigées

| Correction | Où, dans le brouillon 2 | Constat |
|---|---|---|
| A1 cause « probable » | R1 (i), l. 130-137 ; Q1, l. 229-232 ; risque résiduel | appliquée : cinq constats (a) à (e), « probable, non confirmée par le loueur », « tenue pour suffisante par le mot de Lazar (R-2492) » ; le mot « établie » n'y est plus |
| A2 relance sans retour | R1, « Portée », l. 150-156 | appliquée : destruction à 07:48:11Z sans récupération, branche égale à S, lots qui n'existent plus ; lecture sur la tentative 2 seule ; tentative 1 rapportée comme avortée |
| A3 tentative 3 | R1, « Tentative 3 », l. 158-160 ; Q1 | appliquée : « par la tentative 2 » ; nouvel écart écrit, contre-lu et scellé ; « un mot seul ne suffit pas » |
| A4 réserve de l'écart 1 | l. 280-283 ; réserves, l. 441-443 | appliquée : phrase de A1 l. 176-177 citée mot pour mot (relue dans l'addendum 1) ; identifiants en information |
| A5 crédit présent | préalable 2, l. 348-365 | appliquée : condition de la session « crédit présent ≥ M + K », 27,50 et 40,92 USD ; variante prudente 42,20 et 55,62 en information ; dette sortie ; constat à 23,80 USD ; « sinon, aucun lancement et retour à Lazar » |
| A6 refspec | préalable 8, l. 403-409 | appliquée : « dans le clone local de lancement » ; clone temporaire des contrôles déclaré ; branche contenant S gardée |

Mises à jour : ligne de la contre-lecture, registres au commit `0324eb79`, mots de Lazar R-2494 et R-2496 : faites.

## Suggestions et engagements

- **S2, S3, S5, S6** : prises telles quelles, sans risque. S3 : la phrase de A2 l. 353-354 est citée mot pour mot
  (relue dans l'addendum 2) ; le sort des préalables 1 à 4 de A2 est dit.
- **E1 (S1)** : conforme à la suggestion. **L'ajout du rédacteur** (« un relevé qui contredit la cause — solde encore
  positif à l'heure de l'arrêt — : aucun lancement, nœud de Lazar ») **est bon** : il resserre la condition (i), ne
  relâche rien, et ne dépend d'aucun résultat de la course.
- **E2 (S4)** : conforme ; la facture de 60432755 remplace le majorant et le stockage estimé.
- **S7, S8** : laissées au registre, comme suggéré.

## Empreintes et renvois

- Registres au commit `0324eb79e855d9428eea891674ae94d440f6a8da` (08:33:48Z) : décisions `bdd4d430…`, dépenses
  `c79537ba…`, arrêts `3b9cb6ae…`, GO `405e4b56…` : **recalculées, égales**.
- R-2494, R-2496 : verbatim égaux au registre. R-2495 (23,80 USD), R-2497 (contre-lecture, `fac5fb91…`) : justes.
  R-2476 : nomme bien `60417353:GO-2026-11-10-10`. `registres/go.md` l. 300 : ligne GO-2026-11-10-10, de calcul.
- Table des pièces : inchangée, empreintes vérifiées à la contre-lecture. Empreinte du brouillon 1 citée : juste.
- Les nombres : 27,50 ; 40,92 ; 42,20 ; 55,62 ; 6,07 : justes. « ≈ 50 USD » et « ≈ 90 USD » : ceux de R-2496.

## Rien d'autre n'a changé ; code inchangé

- Les 24 blocs du diff se rangent tous sous A1 à A6, les mises à jour, S2, S3, S5, S6, E1, E2. Hors de ces points,
  seuls changent le titre, la date, et deux phrases d'accord (réserves ; section « Pièces »). Les lectures Q2 à Q7, les
  règles R2 et R3, « Ce qui ne change pas » et les conditions d'emploi sont octet pour octet celles du brouillon 1.
- Le préalable 3 porte un fait neuf, hors de mes corrections mais déclaré : le mot de Lazar R-2496, option (a) (le
  témoin Bailey relance son instance, nommée en marche sous GO-2026-11-10-10). Il est juste au registre et ne change
  aucune règle.
- `git diff --name-status 02017d32 09fd663f` : quatre ajouts, les deux brouillons et leurs compagnons, sous
  `brouillons/`. `enchaineur_p3bis_v6.sh` au commit `09fd663f` : `1b49b701…`, inchangé.

## Remarque de forme

- **R1** — La ligne « Statut » (l. 44) annonce une vérification courte « par un lecteur neuf ». Elle est faite par le
  contre-lecteur, comme pour les addendums 1 et 2. À écrire ainsi dans l'en-tête du texte scellé.

## Points ouverts (inchangés, hors de l'addendum)

1. À 23,80 USD, la condition du préalable 2 n'est pas atteinte : recharge de plus avant le lancement.
2. Sort de 60417353 : geste de Lazar dans la session du témoin (R-2496).
3. Engagements E1 et E2 : à relever avant le lancement.
