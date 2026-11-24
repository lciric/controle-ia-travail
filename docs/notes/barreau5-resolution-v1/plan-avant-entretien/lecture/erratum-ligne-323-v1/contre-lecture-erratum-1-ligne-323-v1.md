# Contre-lecture de l'erratum 1, ligne 323, du préenregistrement « sabotage ou empreinte, adaptateurs tenus à l'écart » (barreau 5), version 1

- **Pièce contre-lue** : `barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-erratum-1.md` (même dossier), sha256 `38fe79d2cf458d9b45d47fd887a796237fe4702720b86e1cc7b17c241280ee58`, recalculée, égale à l'empreinte attendue. Calcul joint `calcul_rangs_signes.py`, sha256 `b696ae812855df65388f934c00103895d4001a414cc518baa47bb649f2d7b014`.
- **Contre-lecteur** : agent neuf (R2), Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni l'erratum, ni le texte visé, ni le programme de lecture, ni le verdict.
- **Date** : 2026-11-24, de 12:12:05Z à 12:15:23Z (`date -u`).
- **Classe** : A, contre-lecture d'une pièce décisive.

## Ce que j'ai lu

Empreintes recalculées avant lecture, toutes égales :
- texte visé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` (égale aussi à son compagnon `.sha256`) : **lignes 181 à 199 et 323 seulement**. Hors de ce périmètre, une seule recherche par motif, sur les lignes 106 et suivantes, ne rendant que des numéros de ligne (constat 4) ; jamais les lignes 1 à 105 ;
- bloc K : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/sortie-simulation-puissance-adaptateurs-tenus-a-l-ecart-v3.json`, `1b0cf4cde2baf6d6dcb11b807f4fb84e70c72fdb0ded228eb1396836e6a14f7d`, clé `K_plan_retenu_rangs_signes.tables` (de cinq à quatorze familles) ;
- programme de lecture figé, `git show c76e79169eee337ce66c7d88f62d039e853eebfc:src/controle_ia/barreau5_familles/lecture_v1.py`, sha256 de la sortie `ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f` : table `NIVEAUX` (l. 113), fonctions `comptes_rangs_signes`, `probabilite_au_plus`, `seuil_rangs_signes`, `niveau_de` (l. 188 à 232), et, pour voir où le niveau est appliqué, `epreuve_rangs_signes` et `epreuve` (l. 243 à 264) ;
- addendum 1 scellé, `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md`, `2afa2186c9f11e0a477cdf628348d2cad3bce90de5933597ff09a4a3048499e4` : en-tête et point 1 (l. 1 à 59 de l'addendum) ;
- registre `registres/barreau5-familles-jumelles-v1.md`, lignes `CODE-LECTURE-B5F` et `EPREUVE-B5F` seulement ; `registres/go.md`, recherche de l'accord cité.

Non lu : aucun résultat, verdict, score, activation ni fichier de `diag/`. Fait reçu de la mère, vérifié par le lecteur habilité sur le résultat scellé : dans la lecture faite, M1, M3, E1, E2a, E2b et E3 avaient toutes dix familles présentes.

## Vérifications

**(1) Recopie à la lettre.** Le passage « tel qu'il est » est une sous-chaîne exacte de la ligne 323 (comparaison par programme : présent, une occurrence de « à six : aucune » dans la ligne). C'est une phrase de la ligne, non la ligne entière ; le titre « ligne 323, à la lettre » l'annonce comme passage, sans ambiguïté gênante.

**(2) Seul changement.** Comparaison caractère à caractère du passage tel qu'il est et du passage corrigé : une seule différence, le mot « aucune » remplacé par « 0, les six différences du même côté, probabilité exacte 1/64 par sens ». Rien d'autre ne bouge (constat 2 pour la phrase qui le décrit).

**(3) Calcul.** Mon propre dénombrement exact des 2^K attributions de signes aux rangs 1 à K (sans tirage, fractions exactes), seuil 1/40 = 0,025 par sens :

| K | w | attributions à W = w | cumul | P(W ≤ w) | ≤ 0,025 |
|---|---|---|---|---|---|
| 6 | 0 | 1 | 1 | 1/64 = 0,015625 | oui |
| 6 | 1 | 1 | 2 | 1/32 = 0,03125 | non |
| 7 | 0 | 1 | 1 | 1/128 = 0,0078125 | oui |
| 7 | 1 | 1 | 2 | 1/64 = 0,015625 | oui |
| 7 | 2 | 1 | 3 | 3/128 = 0,0234375 | oui |
| 7 | 3 | 2 | 5 | 5/128 = 0,0390625 | non |

Donc w(6) = 0 et w(7) = 2 au niveau de 95 % bilatéral. Accord exact avec l'erratum, avec le calcul joint (exécuté : mêmes sorties), avec le bloc K (`6_familles` : `somme_des_rangs_contraires_admise_95: 0`, `p_un_sens_au_seuil_95: 0.015625`, `niveau_bilateral_le_plus_fort_atteignable: 0.96875` ; `7_familles` : `2`, `0.0234375`) et avec le programme figé, exécuté sur ses propres fonctions extraites : `niveau_de(6)` = « 95 », `seuil_rangs_signes(6, "95")` = 0, `seuil_rangs_signes(7, "95")` = 2, `seuil_rangs_signes(6, "99")` = `seuil_rangs_signes(7, "99")` = aucune, `niveau_de(5)` = aucun. Les entrées de 99 % de la table du texte (lignes 190 et 191, « aucune ») restent justes.

**(4) Portée.** L'erratum ne touche ni hypothèse, ni prédiction, ni métrique, ni critère, ni épreuve, ni liste d'arrêt ; le seul nombre qu'il écrit (w(6) = 0 à 95 %) est celui que le bloc K portait déjà et que le programme figé (`CODE-LECTURE-B5F`, commit `c76e7916…`, lecture `ed0999df…`) appliquait déjà : `epreuve` passe `niveau_de(len(familles))` à `epreuve_rangs_signes`, qui prend `seuil_rangs_signes(K, niveau)`. Le seuil appliqué ne change donc pas. Il ne contredit pas l'addendum 1, point 1, règle 1 (« 95 si elle en a six ou sept ; aucun si elle en a moins de six ») : il le rejoint. La phrase qui suit à la ligne 323 (« Sous six familles : issue N ») confirme la lecture retenue. Avec le fait reçu (dix familles dans toutes les épreuves), la règle des six et sept familles n'a joué dans aucune épreuve de la lecture faite.

## Constats

1. **Mineur — accord cité introuvable au registre.** L'erratum se réclame de `GO-2026-11-24-21`, point 12. `registres/go.md` ne porte, pour le 24 novembre, que `GO-2026-11-24-01` à `-09` ; aucune occurrence de `GO-2026-11-24-21` dans `registres/` ni `docs/` à 12:15Z. Rien à changer dans l'erratum ; la mère consigne cet accord dans `registres/go.md` avant le scellement, faute de quoi l'en-tête cite un accord non vérifiable.
2. **Détail — phrase qui décrit le changement.** « Seuls les mots « à six : aucune » changent » : « à six : » reste ; seul « aucune » est remplacé. Couple facultatif :
   - avant : « Seuls les mots « à six : aucune » changent ; le reste de la ligne 323 et du texte est inchangé. »
   - après : « Seul le mot « aucune » de « à six : aucune » change, remplacé par « 0, les six différences du même côté, probabilité exacte 1/64 par sens » ; le reste de la ligne 323 et du texte est inchangé. »
3. **Détail — affirmation hors de ce qui est déclaré lu.** « Pourquoi », point 2, s'appuie sur `niveau_de` (« lit à 95 % dès six familles »), que la ligne « Lu » de l'en-tête ne nomme pas (elle nomme `seuil_rangs_signes` et `NIVEAUX`). L'affirmation est juste (vérifiée ici, `niveau_de(6)` = « 95 »). Couple facultatif :
   - avant : « ; `niveau_de` lit à 95 % dès six familles ; »
   - après : « ; `niveau_de` lit à 95 % dès six familles (vérifié par la contre-lecture : `niveau_de(6)` rend « 95 ») ; »
4. **Information — autres lieux du texte, hors de mon périmètre.** Sur les lignes 106 et suivantes, le motif « à six : aucune » ne se trouve qu'à la ligne 323 ; le motif « six familles » se trouve aux lignes 323 et 359. Je n'ai pas lu la ligne 359 (hors des lignes confiées) : je ne dis pas qu'elle porte la même erreur, ni qu'elle ne la porte pas. Si la mère veut que l'erratum soit complet sur ce point, un lecteur habilité à cette ligne le vérifie ; rien n'oblige à retoucher l'erratum.
5. **Information — « les six différences du même côté ».** Dans le programme, une différence nulle compte contre la conclusion essayée ; « du même côté » veut donc dire strictement du côté de la conclusion. C'est la tournure déjà employée par le texte à la ligne 193 pour huit familles (« il y faut les huit différences du même côté ») : aucune ambiguïté nouvelle, aucun couple.

Aucun sigle seul ; empreintes citées toutes justes (texte visé, bloc K, programme figé, lecture de `EPREUVE-B5F`) ; la phrase de portée sur les dix familles est donnée comme relayée et non vérifiée par le rédacteur, ce qui est exact, et le fait reçu la confirme.

## Verdict

**Scellable.** Zéro constat grave, un mineur (accord à consigner au registre, sans toucher l'erratum), deux détails à couples facultatifs, deux informations.
