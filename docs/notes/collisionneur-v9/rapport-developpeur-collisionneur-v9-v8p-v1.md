# Rapport du développeur : collisionneur v9-v8p (v1), lignée de l'essaim

**En bref.** La v8p est écrite : tour III.3 à la seule place « fin », phrase de Fable insérée, ligne de format propre au
tour III.3. Essais : **360 passés, 3 sautés**, sous `env -u` de toutes les clés ; sept mutations, toutes prises.

Pièce de classe B, écrite par Claude Opus 5.5 le 22 novembre 2026. La v8p est une copie de la v8f (`445fe2d3…`,
inchangée), et non de la v8m : le jumeau isolé reste dans la lignée du moteur de l'essaim. Elle suit la relecture de
Fable `essaim-v1/demande-fable-essaim-pilote-v1/reponse-fable-v1/relecture-fable-api.md` (`28cc1d81…`).

Rien n'est scellé ni commité. Aucun fournisseur n'a été appelé.

## Fichiers

| Fichier | sha256 |
| --- | --- |
| `collisionneur_v9_v8p.py` | `5979c712101034265d5a7dcacc2110b691f97e69b3c4158d8a3c6c2af6704290` |
| `fabriquer_v8p_depuis_v8f_v1.py` | `6609368e…` ; il contrôle l'empreinte de la v8f et celle de la relecture |
| `test_collisionneur_v9_v8p.py` | `4fcc6b5b…` |

Les essais sont une copie de ceux de la v8f (`efde1e0f…`). Trois essais sont accordés, marqués « v9-v8p » :
- la version ;
- la place « fin » seule, avec la phrase neuve ;
- l'essai des consignes servies, réduit à « fin » ; « avant-livrable » y est maintenant refusée.

## Changements

1. **Tour III.3.** `PLACES_III3` ne garde que « fin ». « avant-livrable » est refusée par `--place-iii3`.
   - La consigne servie est la consigne de la v8d, puis la phrase du remplacement 1 (`PHRASE_DUELS_III3`), puis la forme
     imposée.
   - La phrase « Livrable » n'est pas coupée.
2. **Ligne de format du tour III.3 (remplacement 5).**
   - Dans la v8f, cette ligne vient du préambule commun à tous les tours : « Format : français, Markdown, au plus
     {mots} mots. Termine par une ligne qui contient exactement : FIN-DE-CELLULE ». Au tour III.3, elle se lit
     « au plus 3500 mots ».
   - Le texte « 3 500 mots au plus », cité comme « Ancien » par Fable, n'y figure donc pas.
   - Changer la ligne pour le seul tour III.3 est possible. `construire_prompt` remplace, pour ce tour seulement, le
     segment « au plus 3500 mots » par le texte neuf de Fable : « 3 500 mots au plus pour l'ensemble de la réponse ; la
     page ne vaut que pour le point (c) ».
   - Le gabarit commun et les autres tours sont inchangés.
   - La fonction `ligne_format(tour)` donne la ligne servie à chaque tour ; l'essaim la reprend.
3. **Mot « duel » au tour III.1 (constat demandé par Fable).** Le livrable du tour III.1 dit bien « les expériences
   décisives qui la trancheraient, chacune en duel H_A contre H_B ». Un essai le vérifie. Le remplacement 1 garde donc le
   mot « duels ».

## Essais

Les textes sont comparés par programme à la relecture, dont l'empreinte est contrôlée. Les essais vérifient :
- **remplacement 1** : phrase mot pour mot, et ordre Livrable < phrase < forme ;
- **remplacement 5** :
  - le texte neuf est celui de Fable, et l'ancien cité est bien « 3 500 mots au plus » ;
  - la ligne est servie au seul tour III.3 ;
  - les tours III.1 et III.2 gardent la ligne de la v8f ;
- **dossier** : `verifier` ne trouve rien sur un dossier complet.

Mutations prises :
- P1 : phrase absente ;
- P2 : phrase après la forme ;
- P3 : « avant-livrable » remise ;
- P4 : un mot changé dans la phrase ;
- P5 : format non changé au tour III.3 ;
- P6 : format changé à tous les tours III ;
- P7 : texte neuf du format altéré.

## Points ouverts

- La ligne de format n'est pas scellée dans `consignes-etage3.json`, qui ne porte que les consignes : elle tient au
  script, dont l'empreinte est au journal.
- La formulation de la phrase neuve n'a jamais été essayée (confiance de Fable : 0,6).
