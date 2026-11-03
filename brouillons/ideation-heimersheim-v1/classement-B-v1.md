# Classement B (cinq autres mentors) — étape D, classeur neuf — v1

Écrit le 3 novembre 2026 à 12:12 UTC (`date -u`). Consigne `ideation-rapport-classeur-D-B-prompt.md` (`26922b5de0aae3660e9f50d541eddbf9d3b79e6bfaf1d575f74b0ccfc94187b5`, vérifiée avant lecture). Protocole : `protocole-rapport-idees-v1.md` section 5 et `protocole-rapport-idees-v2.md` section 2, lus en entier avant les fiches.
Entrées : `melange-v1/fiches-classement-B-v1.json` (`84af169b1a5a2daad85367e5b7f3378527694943fb57d5a748f3889a15f1cd33`, 14 fiches) ; `moisson-C/moisson-fusionnee-v1.json` (`4033b82331eef2b7e3360c2e8af707899b43b23f7c83464d52dd5be4b3f85f20`, seules les 14 entrées de ces fiches lues). Aucune recherche, aucun appel de modèle, aucune clé de provenance ouverte.

**Sans témoin déguisé : l'axe d'originalité du classement B n'est pas contrôlé.**

## Porte
14 fiches sur 14 classées. Gardées : la moisson ne relève de contradiction pour aucune (champ vide ou « rien »). Dans le sujet : chacune est destinée à un mentor par son champ « classement ». La question de chaque mentor n'est pas dans les entrées : le sujet n'est pas contrôlé au-delà de cette destination.

## Lecture des ancres (la même pour toutes les fiches ; détail et raisons d'une ligne dans `notes-B-v1.json`)
- **O, originalité vérifiée** (moisson seule) : 0 déjà fait ; 1 voisin proche, si une source fait déjà la manipulation décisive avec le même type de contraste dans un autre cadre, ou éprouve la même question par une autre méthode ; 2 voisin lointain, si les sources ne partagent que le phénomène ou une composante ; 3 ouverte, classe de la moisson prise telle quelle, avec ses réserves.
- **T, testable en jours sur Llama-3.1-8B-Instruct** : ancres telles qu'écrites ; moniteurs et juges qui lisent les réponses de Llama-3.1-8B-Instruct comptés comme instruments ; « sur une carte » lu comme un ordre de grandeur de calcul. Il manque une condition de l'ancre 3, la note est 2 : soit le modèle étudié en génération est un autre (Llama-3.2-3B, Qwen2.5-7B), soit aucun seuil n'est donné, même illustratif.
- **M, prolonge un outil du mentor destinataire** (d'après ses travaux cités dans la fiche) : aucune fiche n'en cite, 0 partout (voir réserve 1).

## Ordre final, par mentor

### Ibrahim — 4 idées, paires dans les deux ordres (12 jugements), cohérence 1,0 (6 paires sur 6)
| Rang | Fiche | O | T | M | Somme | Victoires | Force de Bradley-Terry (log centré) | Drapeau de risque |
|---|---|---|---|---|---|---|---|---|
| 1 | M-062 | 3 | 3 | 0 | 6 | 6/6 | 0,608 (+1,330) | non (non établi) |
| 2 | M-060 | 3 | 3 | 0 | 6 | 4/6 | 0,243 (+0,415) | non (non établi) |
| 3 | M-051 | 2 | 3 | 0 | 5 | 2/6 | 0,106 (−0,415) | non (non établi) |
| 4 | M-053 | 1 | 3 | 0 | 4 | 0/6 | 0,043 (−1,330) | non (non établi) ; à vérifier avant d'écrire : arXiv:2608.05624 compare lexique et juge, auteurs non donnés, résultat non lu |

Seule l'égalité de somme entre M-062 et M-060 restait à départager : les deux ordres l'ont tranchée pour M-062 (jugements 6 et 9, serrés). Le reste suit la somme.

### Kirchner — 2 idées, sans paires (moins de quatre) : ordre par somme, égalité départagée par l'originalité
| Rang | Fiche | O | T | M | Somme | Drapeau de risque |
|---|---|---|---|---|---|---|
| 1 | M-065 | 3 | 2 | 0 | 5 | non (non établi) |
| 2 | M-041 | 2 | 3 | 0 | 5 | non (non établi) |

Ordre fragile (réserve 4) : M-065 ne passe devant que par le départage, et son « ouverte » vient de requêtes sur une autre cible.

### Scheurer — 4 idées, paires dans les deux ordres (12 jugements), cohérence 1,0 (6 paires sur 6)
| Rang | Fiche | O | T | M | Somme | Victoires | Force de Bradley-Terry (log centré) | Drapeau de risque |
|---|---|---|---|---|---|---|---|---|
| 1 | M-051 | 2 | 3 | 0 | 5 | 6/6 | 0,608 (+1,330) | non (non établi) |
| 2 | M-076 | 2 | 3 | 0 | 5 | 4/6 | 0,243 (+0,415) | non (non établi) |
| 3 | M-071 | 2 | 3 | 0 | 5 | 2/6 | 0,106 (−0,415) | non (non établi) |
| 4 | M-005 | 1 | 3 | 0 | 4 | 0/6 | 0,043 (−1,330) | non (non établi) ; à vérifier : arXiv:2603.25015, auteurs non donnés |

Trois fiches à égalité de somme et d'originalité (M-051, M-076, M-071) : les paires les ordonnent. M-051 passe devant M-076 parce que deux sources évoquent déjà le mécanisme des refus sans le tester (jugements 18 et 20, serrés), et M-071 est dernière des trois (moisson incomplète, issue d'équivalence).

### Colognese et Ward — 3 idées, sans paires : ordre par somme, égalité départagée par l'originalité
| Rang | Fiche | O | T | M | Somme | Drapeau de risque |
|---|---|---|---|---|---|---|
| 1 | M-008 | 2 | 3 | 0 | 5 | non (non établi) |
| 2 | M-054 | 2 | 2 | 0 | 4 | non (non établi) |
| 3 | M-006 | 1 | 3 | 0 | 4 | non (non établi) ; tension publiée avec arXiv:2607.17425, qui va vers la rivale, auteurs non donnés : à vérifier |

### Jang et Feng — 2 idées, sans paires : ordre par somme
| Rang | Fiche | O | T | M | Somme | Drapeau de risque |
|---|---|---|---|---|---|---|
| 1 | M-018 | 1 | 3 | 0 | 4 | non (non établi) ; à vérifier : arXiv:2609.08236 et 2501.17969, auteurs non donnés |
| 2 | M-077 | 1 | 2 | 0 | 3 | non (non établi) ; tension publiée avec arXiv:2610.06522 (Huang, hors mentors), qui va vers la rivale |

M-006 et M-062 sont aussi dans le classement A ; elles ne sont notées ici que pour B.

## Cohérence
Globale 1,0 : 12 paires sur 12 concordent dans les deux ordres, 6 sur 6 pour chaque mentor. C'est au-dessus de 0,8 : pas de réserve au sens du protocole. Réserve de symétrie (R4, trop propre) en revanche : réserve 2.

## Forces de Bradley-Terry
Les jugements donnent pour chaque mentor un ordre parfait : aucune victoire du bas sur le haut. La condition de Ford n'est donc pas remplie et le maximum de vraisemblance n'existe pas. Le script le détecte et le dit. Il rapporte, sous ce nom, un estimateur régularisé : pseudo-compte 0,5 par sens et par paire comparée, algorithme MM de Hunter, 91 itérations. Ces forces ne valent que comme ordre, et elles sont identiques d'un mentor à l'autre par construction (même motif de victoires). Les gardes du script ont été éprouvées sur un cas sain et sur trois artefacts (`bradley_terry_v1-B-auto-test.txt`, tous passent). Le calcul vérifie que les 24 jugements suivent exactement le tirage.
Tirage : `numpy.random.SeedSequence(0x84af169b1a5a2daa = 9560885389348711850)`, un enfant par mentor (`spawn`, ordre de la consigne), `default_rng(enfant).permutation` ; numpy 2.5.3, Python 3.13.18 ; hors dépôt, sans commit.

## Réserves
1. **Le critère M ne départage rien dans B.** Aucune fiche ne cite un travail de son mentor : les fiches ne portent que le noyau commun des champs. Le 0 veut dire « aucun lien lisible dans la fiche », pas une absence de lien vérifiée. Le classement B repose donc sur O, T et, dans les paires, sur le caractère mémorable. Pour noter M, il faudrait les papiers que cite la cellule d'origine ou la page du mentor ; je ne les ai pas ouverts, la consigne ne me les donne pas.
2. **Cohérence 1,0 trop propre (R4).** Un seul classeur a jugé les deux ordres dans la même session, après avoir écrit les notes. La cohérence mesure la stabilité à l'ordre de présentation, pas un accord entre juges, et les paires reprennent largement les notes. Quatre paires ont été serrées, et c'est là qu'un second juge pourrait différer : M-060 contre M-051 (jugements 3 et 10), M-062 contre M-060 (6 et 9), M-071 contre M-005 (14 et 16), M-051 contre M-076 (18 et 20).
3. **Drapeaux tous à « non », mais non établis.** Aucun papier des mentors n'est dans les entrées, ni cité par les fiches, ni identifié dans la moisson : la moisson donne les auteurs de quelques sources seulement, et aucun n'est un mentor. Ces « non » ne sont donc pas vérifiés contre les papiers des mentors. Pour M-053, M-005, M-006 et M-018, la source la plus proche a des auteurs non donnés : vérifier qu'elle n'est pas du mentor avant d'écrire. C'est surtout vrai pour M-006, que arXiv:2607.17425 tire vers la rivale, et pour M-053, dont arXiv:2608.05624 pourrait contredire « le juge est remplaçable ».
4. **Kirchner : M-065 en tête sur une originalité fragile.** M-065 n'est première que par le départage à l'originalité (sommes égales à 5). Or sa moisson « ouverte » a visé le transport d'un effet de pilotage : la loi d'attraction, les items R4 et les critères C1 et C2 ne sont pas définis dans la fiche. La moisson la juge elle-même « probablement un test de réplication interne plutôt qu'une question du champ ». Si l'on ne retient pas cette originalité, M-041 passe en tête.
5. **Moissons incomplètes**, qui affaiblissent le « vérifiée » : M-071 (deux requêtes non exécutées, dont LessWrong et Alignment Forum) ; M-062 (OpenAlex non interrogé, alors que sa classe est « ouverte ») ; M-041, M-076, M-077 (OpenAlex injoignable). Une zone vierge reste une question.
6. **La question de chaque mentor n'est pas dans les entrées.** Dans la question gelée des paires, « cette question » est lue comme la question de candidature du mentor, telle quelle, jugée sur les trois critères.
7. **Précisions sur deux raisons écrites au fil des jugements** (non réécrites) : au jugement 13, « parle à ce mentor » renvoie seulement à la destination de la fiche ; au jugement 21, « moisson complète » pour M-076 veut dire quatre requêtes exécutées, OpenAlex étant injoignable.

## Fichiers (`/home/claude/scratch/ideation-rapport/classement-D/`)
- `notes-B-v1.json` — `0ed3dd4f7fe287880344ed05c07fb6b1c972bac008252ba5745ce203c19cb9f9`
- `paires-B-v1.jsonl` — `86076d11692785098aa3415cc68edd9cdb4176803c623124f58c9df4fd0453e8`
- `bradley_terry_v1.py` — `1d420bcb8c141e022c196869e28ef12b362b3ea3cd9a3946eda1f8398017772b`
- `bradley_terry_v1-B-tirage.json` (ordre de présentation, tiré avant tout jugement) — `c9114de2556782026cde37e1eddd36fe68498d4a378a254b066e873b99501469`
- `bradley_terry_v1-B-sortie.json` — `d8e3042642a9be4e1872c2c73c33187bf150bca4080ba06284f5647e6235fe47`
- `bradley_terry_v1-B-sortie.txt` — `0d205e02d459b4e8972eb311271ca6812bdc899b9cb877c5ff0a3b7b210f7eca`
- `bradley_terry_v1-B-auto-test.txt` — `b969941cc9c70cea509292b3cef69e3d7d4091f3c03a8d137d0739ab352945c8`

Les annexes portent le suffixe B : un autre classeur écrit ses fichiers A dans ce dossier, et sa consigne nomme sans doute aussi `bradley_terry_v1.py`. Si le script est remplacé, son empreinte ci-dessus ne correspondra plus.
