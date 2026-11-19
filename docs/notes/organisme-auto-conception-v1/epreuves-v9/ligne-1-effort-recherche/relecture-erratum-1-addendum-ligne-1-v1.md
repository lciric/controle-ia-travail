# Relecture de l'erratum 1 à l'addendum 1 scellé de la ligne 1 — v1

Relecteur : le contre-lecteur de l'addendum (versions 1 à 4), modèle O. Date : 2026-11-19, après 22:34Z (temps universel). Rien lancé ; aucune graine dérivée ; aucun réseau sauf `git fetch` et `git show` ; aucune écriture dans le dépôt ; aucun refus d'outil. Rien n'a été touché sous `archives-reponses-modeles/`.

## Verdict

**Scellable après corrections (deux, à texte exact, § 4).** Les quatre cellules sont remplies avec des valeurs justes contre le registre des scellements, R-3980, R-3981 et les commits. La phrase du § 9, point 5, est la mienne au caractère près. Les deux corrections portent sur un compte inexact (« huit valeurs ») et sur la phrase de statut de la copie scellée, qu'un lecteur doit pouvoir lire juste.

## 1. Empreintes et valeurs, vérifiées par programme

| objet | relu | état |
|---|---|---|
| erratum (commit `e7d91969`) | `a370cf6ac9285c0c933fff299d43d5098f8fcd1432fe57c1db0c38006d2884bb` | conforme à son compagnon |
| rapport du rédacteur | `578f903a9f1523b3dc2c90b3cb4744e783627350d0e9528551fc88fee3552700` | conforme |
| mandat | `d2b68c3aa5c04fae922c452a55f834b29dd1d63e2fe126308b866703a9da1064` | conforme |
| addendum scellé sur `main`, et au commit `061aeff58d64b43a4843d61137123f3db5d8d650` | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | identique ; le commit porte le texte, son compagnon et la ligne du registre des scellements |
| `registres/scellements-v1.md`, ligne de la clé `ADDENDUM-1-ORGANISME-V9-LIGNE-1` | heure `2026-11-19T22:25:03Z`, chemin et empreinte égaux à ceux de l'erratum | juste ; empreintes des deux registres au commit `0dedbcaf` (`a435dd60…`, `3ebbcabc…`) égales à celles que l'erratum cite |
| R-3980 et R-3981 (`main`, commit `3f64028f13dff8ac98fe1eb3e8260e400042d1a0`, daté 22:25:19Z) | « scellé par la mère à 22:25:03Z » ; « le commit 061aeff5 porte le texte, son sceau et la clé » | juste |
| mon contrôle v4 au commit `991e4229233e864def74b525b09d28685c331bb7` | `def81ef33381acd6bbd10926c79f025743cd16de17b0e35621706a262e1bb2c2`, verdict « Scellable tel quel » | juste |

**Places « À PORTER » du texte scellé.** Une recherche dans le texte scellé en compte huit lignes :
- **quatre cellules à remplir :** les lignes 209, 210 et 211 (§ 6) et la ligne 232 (§ 8) ;
- **quatre récits de versions antérieures :** au § 10, au § 11 (deux fois) et au § 12.

Le recensement de l'erratum est donc exact. Il cite chaque cellule par son texte exact.

## 2. Ce que l'erratum change : seulement ce qui est permis

L'erratum dit en tête qu'il ne change ni règle, ni garde, ni décision. Il remplit les quatre cellules et porte la seule phrase permise au § 9, point 5, présentée comme une précision de lecture qui ne change pas le § 6. Il ne fait rien d'autre, hors le paragraphe « pour mémoire » et la phrase de compte jugés ci-dessous.

## 3. Écarts

- **Paragraphe « pour mémoire » sur 22:25:19Z : à garder.** Le § 6 de l'addendum demande de comparer les dérivations à l'« heure du scellement de cet addendum consignée au registre (`date -u`) ». Or deux heures existent :
  - 22:25:03Z, dans le registre des scellements ;
  - 22:25:19Z, dans les lignes R-3980 et R-3981, avec leur estampille `date -u`.

  Sans ce paragraphe, un lecteur pourrait hésiter entre les deux. Le paragraphe lève l'ambiguïté et ne change aucune valeur. L'écart au mandat est de forme ; il sert la garde A14. L'écart de seize secondes est en outre sans effet, puisque rien n'est lancé avant le mot de Lazar, qui nomme l'empreinte de la version scellée (§ 6 de l'addendum).
- **Phrase de statut de la copie scellée (« non scellée, avant le contrôle de son différentiel ») : à dire.** Le texte scellé ne peut pas être changé. Mais un lecteur qui ouvre la copie scellée y lit « non scellée ». Une précision de lecture d'une phrase lève cela, sans toucher aucune règle (correction 2). C'est un second écart à la lettre du mandat, de même nature que la phrase du § 9 : je le recommande à la mère.
- **« Huit places » contre quatre cellules : la phrase de l'erratum est inexacte.** Les quatre cellules appellent sept valeurs, et non huit :
  - au § 6 : chemin, empreinte, commit et heure ;
  - au § 8 : chemin, empreinte et verdict, selon le texte même de la cellule.

  L'erratum donne en plus le commit du contrôle, ce qui est utile mais n'était pas demandé. Les « huit places » de R-3980 sont donc un compte approximatif de la mère ; l'erratum ne doit pas le reprendre comme un fait (correction 1).

## 4. Corrections (texte exact)

1. **§ 2, premier paragraphe.** Remplacer « Elles appellent huit valeurs (le compte de R-3980). Toutes les huit sont remplies ; aucune ne reste ouverte. » par :
   « Elles appellent sept valeurs : chemin, empreinte, commit et heure du scellement au § 6 ; chemin, empreinte et verdict du contrôle au § 8 ; le commit de ce contrôle est donné en plus. R-3980 parle de « huit places » : ce sont ces quatre cellules. Toutes sont remplies ; aucune ne reste ouverte. »
2. **Fin du § 3, après la phrase citée.** Ajouter le paragraphe :
   « Précision de lecture, sans règle changée : la phrase de statut de la copie scellée (« version 4 (erratum de la version 3), non scellée, avant le contrôle de son différentiel par le vérificateur ») décrit la version 4 avant son scellement ; la copie est scellée depuis 2026-11-19T22:25:03Z (registre des scellements, clé `ADDENDUM-1-ORGANISME-V9-LIGNE-1`), après le contrôle de son différentiel (`def81ef33381acd6bbd10926c79f025743cd16de17b0e35621706a262e1bb2c2`, « Scellable tel quel »). »

Le paragraphe « pour mémoire » reste tel quel. Si ces deux textes sont appliqués à la lettre et que rien d'autre ne change, l'erratum est scellable sans nouvelle relecture de fond ; un contrôle du différentiel suffit.

## 5. Rappels hors du texte

L'erratum n'a pas de compagnon `.sha256` dans le bloc-notes du rédacteur ; la version versée en a un. Il se scelle par la mère comme pièce de classe A, avec cette relecture citée. Le programme de l'audit de symétrie, la décision 4 de Lazar et son mot avec chemins et empreintes restent dus avant le départ.
