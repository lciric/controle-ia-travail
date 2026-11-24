# Vérification des corrections : programme d'extraction de la liste des exclus, v2

Pièce de classe B (instrument). Vérification faite par le même contre-lecteur que la v1 (Claude Opus 5.5).
Programme vérifié : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/extraire_liste_exclus_ordre_course_lue_v2.py`. La v1 n'a pas été modifiée.
Je n'ai lu aucune valeur de sortie de course, ouvert aucune consigne privée, ni modifié aucun fichier du dépôt. Les essais tournent dans `scratchpad/cl-essais-v2/`.

## Verdict : autorisable

Le bloquant et les deux majeurs sont levés. Les mineurs de la v1 qui relevaient du code sont corrigés. Il reste trois mineurs, qui n'empêchent pas l'emploi.

## Points de la v1, un par un

| Point | État | Vérification |
|---|---|---|
| B-1 — renvoi à l'ordre de la première course | **levé** | Le bloc 5 recopie le § 8 de l'ordre scellé `43a7a050…` : les ajouts du brouillon 9, le renvoi « le registre « qui a lu quoi » fait foi » et la ligne R-3524 y sont. Les blocs 6 à 9 recopient les quatre phrases d'exclusion de l'en-tête (rédacteurs des brouillons 9 à 12). Le renvoi au brouillon 3 est gardé (blocs 10 et 11). Le fichier source est égal à celui de `main`. |
| M-1 — pièce de rang 2 non contrôlée | **levé** | Le programme exige trois pièces, toutes marquées « scellé : oui », chacune à son empreinte et avec son compagnon. La pièce de rang 2 est cherchée par motifs, et l'extrait écrit qu'elle ne nomme aucun exclu. Je l'avais lue en entier en v1 : c'est exact. |
| M-2 — phrase d'en-tête du rang 1 | **levé** | Bloc 2. |
| m-1 — puce « Jamais montré » | **levé** | Bloc 10. |
| m-3 — rédacteur du rang 0 non identifiable | **levé** | Bloc 3, recopié de « Écrit le … » à « … du côté du saboteur ». |
| m-4 — compagnons non comparés | **levé** | Chaque source est comparée à la fois à la constante du programme et à son compagnon `.sha256`. |
| m-5 et m-6 — écriture et erreurs du système | **levé**, avec un reste (r-1 ci-dessous) | Écriture exclusive (mode `x`) ; une `OSError` donne maintenant un refus propre. |
| m-8 — imports | **levé** | Les imports sont en tête du fichier. |
| m-2 et m-7 | rendus à la mère | Hors du code (lacunes de l'ordre lui-même ; inscription au registre « qui a lu quoi »). |

## Essais

| Essai | Résultat |
|---|---|
| Cas sain | code 0 ; sortie identique à l'octet à `essai-exclus-v2.md` (`43b9d4e1…`) ; compagnon conforme |
| Sortie déjà présente | refus, code 1 |
| Dossier de sortie absent | refus propre (`FileNotFoundError`), code 1 |
| Compagnon du rang 2 absent | refus, code 1 |
| Compagnon faux pour l'ordre de la première course | refus, code 1 |
| Rang 2 absent | refus, code 1 |
| Source altérée | refus sur l'empreinte, code 1 |
| Garde des motifs du rang 2, artefact « exclu » et artefact « EXCLUSION » en majuscules | refus aux deux |
| Garde des motifs du rang 2, ligne neutre (cas sain) | passe |

Pour les essais de la garde des motifs, j'ai fabriqué une attestation et une pièce de rang 2 altérées, avec leurs constantes et leurs compagnons ajustés. C'est le seul moyen d'atteindre cette garde.

Fidélité, vérifiée par un relevé indépendant : les onze passages sont des sous-chaînes exactes de leurs sources. Chacun apparaît une seule fois, et son empreinte est égale à celle qu'imprime l'extrait.

Cloisonnement : correct. L'extrait ne porte aucun mécanisme du saboteur, aucune valeur de réglage, aucun fragment de consigne et aucun chiffre de résultat. Le bloc 10 nomme la liste des mots les plus pondérés sans en donner le contenu.

## La garde des motifs du rang 2

Elle est **utile, et bien éprouvée pour ce qu'elle couvre.**

- **Pourquoi elle n'est pas morte.** Tant que les empreintes restent figées, elle ne peut pas se déclencher. Mais elle ne se contente pas de confirmer l'empreinte : elle oblige quiconque changerait la pièce de rang 2 (constante, attestation, compagnon) à faire face à son contenu. C'est une défense en profondeur légitime.
- **Ce qu'elle ne couvre pas.** Ses motifs sont étroits : une phrase comme « ne lira jamais les sondes » passe sans refus. La pièce de rang 2 actuelle ne contient ni « sonde », ni « interdi », ni « jamais montr ». Ajouter ces trois motifs élargirait la garde sans déclencher sur le texte présent (voir r-2).

## Défauts restants (tous mineurs)

- **r-1. Compagnon orphelin.** Le programme écrit le compagnon avant l'extrait. Si l'écriture de l'extrait échoue après coup, un compagnon reste seul. Je l'ai reproduit avec un lien symbolique pendant comme chemin de sortie : refus `FileExistsError`, et `lien.md.sha256` reste sur le disque. Ce compagnon orphelin bloque ensuite toute relance sur ce chemin. Deux corrections possibles : écrire l'extrait d'abord, puis le compagnon ; ou retirer, en cas d'échec, le compagnon que le programme vient lui-même de créer.
- **r-2. Motifs du rang 2 étroits.** Ajouter `sonde`, `interdi` et `jamais montr` (voir la section précédente). Ces motifs ne déclenchent pas sur la pièce actuelle.
- **r-3. Deux phrases du même côté, hors du § 8, absentes de l'extrait.** Dans l'ordre scellé de la première course :
  - § 1, « Pièces interdites » (ligne 143) : la branche `prep/iib-code-v2` est « interdite au lecteur des sondes » ;
  - § 13 (ligne 392) : la personne qui conduit la passe de recalcul « suit les exclusions du § 8 ».

  Ce ne sont pas des rôles exclus, mais elles sont du même genre que la puce « Jamais montré », désormais reprise. Il faut soit les recopier, soit dire dans l'extrait qu'elles sont laissées de côté.
- **Détail de forme, sans effet.** Les titres des blocs 7 et 9 pourraient dire de quel brouillon il s'agit : le rédacteur neuf de 08:26 UTC est celui du brouillon 11, celui de 07:48 UTC celui du brouillon 9.
