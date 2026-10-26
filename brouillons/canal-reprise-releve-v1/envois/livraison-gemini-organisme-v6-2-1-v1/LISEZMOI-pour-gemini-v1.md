# Pour Gemini — la dernière version de l'organisme : v6.2.1 — v1

Transmis par Lazar Ciric, à sa demande (26 octobre 2026, 13:29 heure de Paris : « transmets à Gemini la dernière
version de l'organisme »), préparé par la lignée « conv-audit » du programme. Écrit le 2026-10-26 à 12:30:21 UTC (heure
lue sur `date -u` dans la commande qui écrit cette ligne).

## Ce que contient ce paquet

- `organisme/` : **la v6.2.1**, c'est-à-dire ta v6.2 (commit `3bbb78c1991baf17feb421529fa1957be7edec59`, branche
  `canal/gemini-organisme-v6-2`, 24 fichiers, empreinte d'arbre `3b2d8d5a…`) avec les quatre corrections **C-14 à C-17**
  de la lignée conv-audit, faites sur le mot de Lazar (26 octobre, 00:27 heure de Paris : « tu as mon accord pour
  retoucher la version de gemini ») après la vérification de la v6.2 par un sous-agent neuf. Commit
  `7ea32705c5437d91ed071dd95fb3209bb0b0035e` du dépôt de travail, 26 fichiers, empreinte d'arbre
  `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d` (fonction `empreinte_arbre` du noyau : chemins
  relatifs triés et contenu de chaque fichier, bytecode exclu ; vérifiée avant l'emballage). Manifeste : version `6.2.1`,
  `VERSION = "organisme-gemini-m3-v6-2-1"`, lignée « assistée ».
- `organisme/CORRECTIONS-v5.md` : les quatre corrections, ligne par ligne, avec leurs essais (`tests/test_corrections_v5.py`,
  15 essais) et les témoins (les essais visant une correction échouent sur la v6.2, passent sur la v6.2.1). En bref :
  **C-14** déclencheur d'arbitrage sans terme redondant (branche sans sonde) ; **C-15** la sonde ne vote que sur son
  exactitude de validation (plus de repli silencieux sur l'exactitude d'entraînement ; un essai hérité adapté, dit avec
  sa cause) ; **C-16** une seule source des mots-clés multi-familles (trois copies réduites à une) ; **C-17** le chemin du
  code brut de l'architecte retiré (seul le gabarit à trois paramètres bornés passe). `CORRECTIONS-v1.md` à `v4.md` (C-01 à
  C-13, sur les versions précédentes) valent toujours. Ta conception ne change pas hors de ces corrections.
- `EMPREINTES-organisme-v6-2-1-v1.txt` : l'empreinte de chaque fichier.

## Ce que la v6.2.1 a fait depuis

- Elle a couru deux fois sur la banque `confrontation-v3` (identifiants opaques), sous le noyau `8e5e2f7b`, en isolation :
  rondes de conception arrêtées par l'organisme (6 au plus), puis quatre générations notées, une question ouverte servie à
  la génération 1 (question M, puis question S). Les deux courses sont finies et saines ; leurs réponses aux questions
  sont archivées. Leurs scores ne sont pas transmis ici (règle du programme : les scores de la part finale ne sont servis
  à aucun organisme ; ceux de la part `test` seulement sur décision de Lazar).
- Deux courses de plus sont en préparation, avec deux questions nouvelles servies à la génération 1.

## Ce qui est demandé

Rien d'autre que la prise en compte : si tu produis une v6.3, pars de cette v6.2.1 (et non de la v6.2), garde
`CORRECTIONS-v5.md` et ses essais, et déclare ce que tu changes. Les règles de livraison restent celles des versions
précédentes (branche à part, aucune clé, essais fournis).
