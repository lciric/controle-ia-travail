# Vérification des corrections du lot B1 du pilote « oracles plantés » — v3

- Nature : troisième vérification des corrections (classe B, même contre-lecteur que `contre-lecture-code-lot-b1-v1.md`, `305bb4a3…`, `verification-corrections-lot-b1-v1.md`, `eb7f1819…`, et `verification-corrections-lot-b1-v2.md`, `82a03bf8…`). Le 2026-11-22. Opus 5.5. Processeur seul, 0 USD, aucun appel de modèle, aucun réseau. Commit vérifié : `1c5cb895` (paquet `oracles_plantes_v4`).
- Lu : `reponse-contre-lecture-lot-b1-v3.md` (lignes des remarques 16 à 18), les écarts entre la v3 et la v4 de `tests_de_mort.py`, `lignee.py`, `normalisation.py`, `grammaire.py` et `rejeu.py`. `evaluation.py` et `exact.py` sont inchangés.
- Lancé : `pytest -q tests/test_oracles_plantes_v4_*.py` : 189 passés. Sondes neuves du bloc-notes :
  - `v4_sondes.py` : rejeu des cas de la remarque 16, piège tué par T6 puis réécrit, formes de repli ;
  - `v4_fuzz.py` : 1 680 énoncés mutés au hasard (graines 1 et 2, racine 3, douze mondes), avec registre, puis la banque entière soumise au même registre ;
  - `v4_s.py` : sorties adverses de S et du proposeur.
- Aucun fichier du dépôt modifié, sauf celui-ci.
- **Bilan : 16, 17 et 18 tiennent. Aucune vérité plantée ne meurt ni n'arrête la batterie. Aucune morte ne ressuscite hors de la réserve 15. La clé par texte canonique ne rouvre aucun chemin de survie. Aucune remarque neuve, bloquante ou non.**

## Par remarque

| remarque | verdict | preuve |
|---|---|---|
| 16. Arrêt de la batterie après une morte de même empreinte | **tient** | Rejeu de `v3_sondes.py`, racine 11, monde 8 : la morte B, puis la vérité de duplication (vivante, marquée « collision »), puis B (morte par héritage), puis la vérité (vivante) : aucun arrêt. La règle « une proposition morte reste morte » vaut maintenant par texte canonique. L'héritage se lit dans la famille (monde et forme normale), toujours sous la règle du témoin. La garantie de la vérification v2 est donc conservée : une mort par héritage exige un contre-exemple vérifié sur le candidat lui-même, et une vérité plantée n'en a pas jusqu'à 3N. |
| 17. Développement polynomial trop grand | **tient** | Avec des facteurs `(n + k)^16` en conjonction, aucune exception, et l'héritage reste actif (le piège tué par T6 transmet sa mort aux variantes à 3 et 5 facteurs, par le profil). Dans le balayage aléatoire (`^16`, `^600`, `* (n + 1)^16`), aucune exception. |
| 18. Coefficient géant, JSON trop imbriqué, décimal à exposant démesuré | **tient** | `v4_s.py` : des sorties de S en `1e99999`, `[` × 100 000, octets non UTF-8, entier de 5 000 chiffres, NaN, ou contre-exemples non listés sortent « sortie de S informe ». Des clés doublées ou 46 instances vraies donnent « réfutation fausse ». Côté proposeur, une confiance en `1e-99999` ou de 5 000 chiffres, ou `[` × 50 000, sortent « informe ». Un énoncé qui ajoute `0 * 99…9` (1 500 chiffres) se normalise et hérite comme attendu. La vérité soumise après ces entrées reste vivante. |

## Questions de la coordination

- **Une vérité plantée peut-elle mourir ou arrêter la batterie ?** Non, ni dans les sondes, ni dans le balayage. `v4_fuzz.py`, graines 1 et 2 : 1 680 énoncés mutés au hasard, à partir des textes plantés, avec des insertions adverses (division par zéro, puissances démesurées, sommes et intervalles hors capacité, factorielles, indices au-delà du plafond, conjonctions avec un autre énoncé planté). Ensuite, les 312 énoncés plantés sont soumis au même registre. Résultat : 0 exception, 0 vérité morte ou non vraie-bornée. Raison structurelle, inchangée depuis la v3 : toute mort par héritage passe par `faux_au_temoin`, qui vérifie le candidat lui-même jusqu'à 3N.
- **Une morte peut-elle ressusciter, hors de la réserve 15 ?** Non. Le piège `seuil_u` du monde 8, tué par T6 en n = 40, transmet sa mort à huit reformulations :
  - le même texte ;
  - un renommage ;
  - des parenthèses doublées ;
  - une double négation ;
  - `<= c - 1` ;
  - deux conjonctions avec un grand polynôme positif ;
  - l'ajout d'un terme nul à coefficient géant.

  Une proposition de même famille qui n'est fausse à aucun témoin reste vivante. C'est voulu, puisqu'elle diffère de la morte à ce témoin, et elle est comptée comme « collision ».
- **La clé par texte rouvre-t-elle un chemin de survie (même texte canonique réécrit) ?** Non. Deux textes de même texte canonique ont la même forme, donc la même famille et la même évaluation : le second est faux au témoin du premier et hérite. Les morts sans témoin (contradiction avec les définitions, instance partielle) ne se transmettent pas, mais le même texte remeurt de la même façon. La vacuité reste à part, conformément à la remarque 14. La forme de repli (« brut: ») est le texte imprimé : un texte identique retombe sur la même clé.

## Réserves qui restent (non bloquantes, déjà écrites)

- **Remarque 15** : D-M5 n'est couvert que pour les reformulations de même squelette.
- **Remarque 4** : la tête du registre est à consigner au manifeste de la course réelle (lot B3).
- **Remarques 7 et 12** : renvoyées au concepteur, non tranchées. Si leur décision change les gabarits ou la borne du profil, il faudra une version neuve du code et une nouvelle vérification.

## Conclusion

**Tout tient, sans remarque bloquante neuve : la v4 (`src/controle_ia/oracles_plantes_v4/`, commit `1c5cb895`) peut être le code figé du lot B1**, sous les seules réserves 4, 7, 12 et 15 ci-dessus.
