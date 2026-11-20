# Vérification des corrections de l'additif 4 de la ligne 3 (version 2) — v1

Écrite le 2026-11-20 par le contre-lecteur de la version 1 (modèle O ; règle R2, vérification par le même contre-lecteur), sur le mot de la mère, sous le mandat `mandat-contre-lecteur-additif-4-mot-alarme-v1.md` (`916e2a32…`), avec les mêmes interdits et la même règle d'aveugle. Dépôt au commit `f076aa45d3bc6aff7d79728f262c5ebb974353f1` (tête locale), dossier Q = `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-4-mot-alarme-v1/`.

## Verdict

**Conforme, à sceller après le mot de Lazar sur le § 9.** Les six corrections (1, 2a, 2b, 3, 4, 5) sont portées mot pour mot ; hors d'elles, il n'y a que la tenue (titre, statut, phrase de version). Le rejeu de l'outil rend la version 2 à l'octet. Un point hors de l'additif, sans effet sur son scellement : le rapport de la version 1 (classe C) garde « 1,6 à 2,6 % » ; je recommande un erratum 2 (texte exact au § 4).

## 1. Empreintes (toutes égales à leur compagnon, `sha256sum -c`)

| pièce | sha256 |
|---|---|
| `additif-4-preenregistrement-ligne-3-mot-alarme-v2.md` | `841cef1e99126762019f45bdacca7ff7d6291c91b34c4f3d434c854c262db704` |
| `remplacements-additif-4-v1-v2.json` | `7d5bb4e7fd65b073dd78fcf187ee5570f02e93171bee8bd969e9d3195c1db7d2` |
| journal de l'outil (`…-v2.md.journal-remplacements-v1.json`) | compagnon OK ; il porte outil `391db990…`, cible `c83ff15a…`, remplacements `7d5bb4e7…`, sortie `841cef1e…`, aucun avertissement |
| `differentiel-additif-4-v1-v2.diff` | `87ec1d8e6b5938e2bbde155008c9515bbe479c7748ec09880db04dfaddb16c4a` |
| `rapport-redacteur-additif-4-mot-alarme-v2.md` | `4bb09f22483fc7e21bc258f3826bd41c66974231d6872435db5f94addc661243` |
| `erratum-1-rapport-redacteur-additif-4-mot-alarme-v1.md` | `7dfa2f0042a94ef2f3f63fb164a2a3d990ff06c5bd720dde2c29e11a6f68beb5` |
| version 1, intacte | `c83ff15acab2f082d3bfb9e93be3747f59a31b9131084919f6527de9abdab169` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` (lu en entier : il n'écrit que la sortie, son compagnon et son journal) |
| ma contre-lecture, versée sous `contre-lecture-v1/` | `3e96ef79cbebe3bea9addc59a56c26bb3e1e79bd61bcd93efbcf6a08968affe0`, égale à ma pièce |

## 2. Rejeu et contenu

- **Rejeu** : l'outil, lancé sur la version 1 avec le JSON et une sortie dans mon dossier, rend `FAIT : 8 remplacement(s)` et la sortie `841cef1e…`. `cmp` avec la version 2 versée : aucune différence.
- **Mot pour mot** : les six textes neufs de ma contre-lecture, pris à la lettre, sont comptés par un seul `grep -c -F` à six motifs : 6 lignes dans ma pièce (lignes « - Neuf : ») et 6 lignes dans la version 2.
- **Rien d'autre que la tenue** : le différentiel et le JSON portent huit remplacements. Six sont mes corrections. Les deux autres sont le titre (« — v1 » devient « — v2 ») et le statut, auquel s'ajoute une phrase de version qui renvoie à ma contre-lecture par son chemin versé et son empreinte, juste. Aucune autre ligne ne change. Le statut dit « cinq corrections de texte », comme mon verdict (2a et 2b comptées ensemble), puis les nomme 1, 2a, 2b, 3, 4 et 5 : c'est cohérent.

## 3. Les réserves du rapport v2

Le rapport en compte six, non cinq ; je les juge toutes.
1. **Statut long, phrase d'origine gardée à l'octet** : acceptable ; la phrase de liaison suffit.
2. **Première personne** : juste. Dans les corrections 4 et 5, « mon dossier » désigne bien le dossier du rédacteur de la version 1, où j'ai relevé les dates. La phrase de version le dit ; rien à ajouter.
3. **§ 10 non touché** : juste ; il liste les lectures du rédacteur de la version 1.
4. **Chiffres voisins non touchés** : ils sont justes, parce que ce sont des valeurs arrondies et non des bornes.
   - « 9 999 fois sur 10 000 » (§ 9, point 1) : la chance de « réfuté » vaut 0,999892, soit 9 998,9 fois sur 10 000.
   - « 0,9999 » (table, cellule à 40 ancres et carte) : arrondi de 0,99989.
   - « 0,0001 » pour « sans prise » de la carte : les deux bornes valent 1,078e-4.
   - « moins de 1e-56 » à 8 000 suites : la borne haute vaut 2,07e-57, donc l'inégalité est vraie.
   - Les autres bornes de la table sont vraies aussi : « < 1e-19 » (1,55e-20) et « < 1e-12 » (9,57e-13).

   Aucune correction n'est demandée. Seuls les signes « ≤ » et « < » posent une borne, et ceux de la table sont maintenant justes.
5. **Rapport v1, « 1,6 à 2,6 % »** : oui, l'erratum est à compléter. Le chiffre est faux pour la même raison que la correction 1 ; l'additif fait foi et le rapport est une pièce de classe C, donc le scellement de l'additif n'attend pas cet erratum. Texte au § 4.
6. **Aucun calcul refait par le rédacteur v2** : sans objet. Le rejeu à l'octet et les comptes suffisent ; les chiffres ont été refaits dans ma contre-lecture.

## 4. Erratum à compléter (rapport v1, classe C ; erratum 2, nouvelle pièce, R12)

Ancre comptée une fois dans `rapport-redacteur-additif-4-mot-alarme-v1.md` par `grep -c -F -e`.
- Ancien : `la fausse alarme serait de 1,6 à 2,6 % : l'excès vient de la référence estimée.`
- Neuf : `la fausse alarme serait de 1,3 à 2,6 % selon le départ et m (1,6 % ; 2,4 % ; 1,5 % sur le mélange des deux départs, à 10, 20 et 40 ancres) : l'excès vient de la référence estimée.`

## 5. Les huit points du § 9, pour la mère

| point | options | recommandation | confiance |
|---|---|---|---|
| 1. Jouer un passage dont le mot est fixé d'avance (« réfuté » 0,99989 ; « tient » au plus 1,05e-16) | (a) jouer, le mot rendu avec la mention de la l. 224 du texte ; (b) s'en tenir au calcul contre-lu, carte « mesurée, sans mot », constat écrit comme calcul ; (c) banc neuf (point 2) | **deux avis** : rédacteur (a), 0,6 ; contre-lecteur (b), 0,65. Le passage n'apprendrait rien sur le mot, et la fidélité du calcul est déjà établie par deux voies indépendantes. Si (a) : mention de la l. 224 obligatoire | 0,6 (a) / 0,65 (b) |
| 2. Le « réfuté » tient à la référence de 100 ancres | mention seule (déjà au § 8) ; banc neuf à référence plus grande, par un préenregistrement neuf | mention seule, pas de banc neuf tant que les chantiers actifs sont pleins | 0,7 |
| 3. Seuils neufs de délai (1 ; 17/6) et de part (1/2 ; 1/4) | accepter ; changer avant scellement | accepter tels quels ; aucun changement motivé par le calcul (R1) | 0,6 |
| 4. Mot de la carte lu à 20 et 40 ancres | 20 et 40 ; 40 seul ; plus petit m qui tient | garder 20 et 40 (lettre de P6, additif 1) ; ne pas rouvrir | 0,7 |
| 5. Clause de détection non symétrique | garder ; symétriser | garder (héritée de P6, sans effet ici) | 0,7 |
| 6. Lettre de la carte non lue | vérifier par le procédé du texte ; ne pas vérifier | vérifier avant scellement, sans retoucher la règle ; une divergence se rapporte au verdict | 0,75 |
| 7. Unicité des racines hors de la ligne 3 | recherche ciblée par la mère ; rien | recherche ciblée des trois nombres avant l'additif de code | 0,9 |
| 8. Ce que le rédacteur a vu | accepter avec déclarations ; refaire à l'aveugle | accepter ; les déclarations sont portées par les corrections 4 et 5 | 0,75 |

## 6. Écarts

- Ont été écrits dans mon dossier par le rejeu : `rejeu-additif-4-v2.md`, son compagnon, son journal et le compagnon du journal (écrits par l'outil).
- Aucune lecture d'une mesure de l'étage 1 ; rien sous `archives-reponses-modeles/` ; aucun lancement du banc ; aucune écriture dans le dépôt ; aucun commit ; aucune dépense ; aucun refus de permission, de classifieur ou de garde.

Contre-lecteur neuf, modèle O.
