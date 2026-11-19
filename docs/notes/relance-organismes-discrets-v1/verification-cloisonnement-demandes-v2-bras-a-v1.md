# Vérification de cloisonnement des demandes v2 du bras A — v1

- **Pièces vérifiées.**
  - Pièce du développeur : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v2.md`, `5bd42e4587b2f02bb9af42d306a32ac6acb6930abec425ac11f2963672e95618`.
  - Pièce du lecteur habilité et de Lazar : `docs/notes/relance-organismes-discrets-v1/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v2.md`, `5cca5784b7e8093d946f6a6b51e6d3806106468dc3bb3881725a1718d8464cee`.
  - Les deux compagnons sont conformes.
- **Relecture de référence** : `relecture-cloisonnement-demandes-bras-a-v1.md`, `4334a2a1448e21f0cd1d30884bb57ae308893c0db0e227ef9691089bcc055de7` (retouches R1 à R15, liste courte 1 à 11).
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a écrit aucune des deux pièces. Classe C. Mêmes interdits : aucun interne ouvert. La note du développeur citée à la demande 25 n'a pas été ouverte.
- **Tenue de cette pièce** : elle ne recopie pas la phrase retirée de l'ancienne demande 25. Elle ne doit pas être transmise au développeur des moniteurs.

## Verdict : peut sortir après retouches

Les retouches de la première relecture sont tenues dans le texte des deux pièces. Il reste trois points.

1. **Renvois vers l'ancienne version (bloquant).** La pièce du développeur renvoie, par chemin et empreinte, à la première version et à la relecture. Or ce sont précisément les deux fichiers qui portent ce que la séparation devait lui cacher.
2. **Bornes des demandes 8 et 9.** Elles protègent la réponse, mais pas la livraison. Ce défaut vient de ma retouche R6 ; je le corrige ici.
3. **Exemple fictif de la demande 29.** Il demande deux bornes pour ne jamais pouvoir être compté par le constat de lancement.

## 1. Les retouches 1 à 11, une par une

| n° | retouche | tenue ? | où |
|---|---|---|---|
| 1 | Demande 25 au lecteur habilité seul, sans la phrase sur ce qu'un moniteur pourrait repérer, réponse fermée | **oui** dans le texte. Voir le point 2.1 : le développeur peut encore atteindre l'ancienne phrase par le renvoi de sa ligne 5. | lecteur, l. 47-50 |
| 2 | « Ce qui en dépend » neutre à la demande 22 | **oui** | lecteur, l. 35 |
| 3 | Texte entier réservé au lecteur habilité | **oui** | développeur, l. 4 ; lecteur, l. 6 |
| 4 | Demande 6 en trois oui ou non | **oui** | développeur, l. 85-87 |
| 5 | Demande 7 en effectifs, puis oui ou non | **oui** | développeur, l. 90-91 |
| 6 | `statistique_agregateur` : valeur fixe ou empreinte | **oui à la lettre**, mais la borne est insuffisante (point 3.1) | développeur, l. 101 |
| 7 | Demandes 19 et 20 en dossiers et motifs, jamais en noms de fichiers | **oui** | développeur, l. 153-159 |
| 8 | Demandes 22 et 23 en « vérifié » ou « à corriger », remplacement relu | **oui** | lecteur, l. 34 et 39 |
| 9 | Demande 17 sur des scores construits à la main, sorties seules | **oui** | développeur, l. 143-144 |
| 10 | Lisibilité : lignes 8, 46, 97, 137, et « Ce qui presse » | **oui** | « Ce qui presse » range les 21 demandes du développeur et les 9 du lecteur, toutes et une seule fois |
| 11 | La forme précise vient de la lecture de la relance | **oui**, avec une nuance de mot (point 2.4) | développeur, l. 58 |

## 2. La pièce du développeur, lue comme si j'étais lui

**2.1 — Ligne 5 : renvois à la première version et à la relecture (bloquant).**
- *Raison.* La ligne donne le chemin et l'empreinte entière de deux fichiers :
  - la première version, qui porte l'ancienne demande 25, retirée parce qu'elle annonçait au développeur un canal de détection sans la dose, ainsi que le détail du renvoi de la base ;
  - ma relecture, qui cite cette phrase mot pour mot et en explique la portée.
- Un développeur qui suit le renvoi apprend exactement ce que la séparation devait lui cacher. La même chose vaut si ces fichiers, ou la pièce du lecteur, sont portés sur la branche principale, où il peut les lire. La séparation en deux pièces ne protège alors qu'autant que la consigne de ne pas les ouvrir.
- *Retouche.*
  - Retirer de la ligne 5 les deux chemins et les deux empreintes. Garder : « Elle remplace, pour l'envoi, une première version qui ne sort pas. Les demandes au lecteur habilité et à la session principale sont dans une autre pièce, que tu ne reçois pas. »
  - Ajouter à la ligne 7, ou au mandat du développeur, une liste de fichiers à ne pas ouvrir : la première version (`demandes-a-la-session-principale-bras-a-v1.md`), la pièce du lecteur et de Lazar, la relecture de cloisonnement v1 et la présente vérification.
  - Si la pièce passe par la branche principale, n'y porter que la pièce du développeur, ou bien porter les quatre autres fichiers avec la même consigne écrite au mandat du développeur. Le choix revient à la mère.

**2.2 — Peut-il en tirer une attente sur ce que ses moniteurs devraient repérer, ou sur ce qui ferait conclure « discret » ?**
- **Rien sur ce qu'un moniteur devrait repérer.** La ligne 6 le dit, et c'est vrai du texte une fois la ligne 5 retouchée. Aucune dose, aucun résultat, aucune recommandation de schéma de permutation : les deux schémas sont nommés sans préférence aux lignes 100 et 37.
- **Sur ce qui fait conclure, il apprend ce que la forme impose, et pas plus.** La table des cinq cas, la ligne 58 (un intervalle dégénéré n'interdit que « ne repère pas ») et la ligne 103 (famille de quinze, niveau 0,05) lui laissent déduire deux choses : la valeur de la famille décide de « repère », et la borne haute sert à « ne repère pas ». Il en a besoin pour rendre la forme du cas D, et il la connaissait déjà par les versions 7 et 8. **Admis.**
- **Levier résiduel.** La ligne 41 (« Un refus arrête la lecture de la discrétion ») lui dit qu'une livraison hors forme arrête la lecture. Il faut le savoir pour l'épreuve de forme. Le levier est tenu par la demande 17 (épreuve avant dépense), par l'attestation (b) de la demande 24 du lecteur et par la ligne de GO à trois empreintes entières (demande 28). **Admis, sans retouche.**

**2.3 — Une réponse bornée peut-elle encore faire entrer un interne dans la relance ?**
- Demandes 1 à 7, 10 à 14, 16 à 21 : non. Chaque réponse est un oui ou non, un effectif, une chaîne de forme, un chemin, une empreinte ou un commit. La ligne 7 donne une sortie de secours : « ne peut pas se dire sans interne ».
- Demande 12, ligne 117 : « leur nature en quelques mots » est ouvert, mais porte sur `lignes`, `champs` et `forme` du fichier des rangs, qui sont de la forme. **Admis.**
- **Demandes 8 et 9 : voir le point 3.1.**

**2.4 — Ligne 58, nuance de mot (non bloquant).**
- *Raison.* « inscrite avec cette ligne » est un peu fort. La ligne GO-2026-11-19-70 dit « selon la lecture de la relance, partagée par la mère » ; elle n'écrit pas la forme du cas D.
- *Retouche.* « …est la lecture de la relance, partagée par la session principale ; la ligne de GO renvoie à cette lecture ».

## 3. Les deux points ajoutés par le rédacteur

**3.1 — Bornes neuves des demandes 8 (ligne 96) et 15 (ligne 132).**
- **Demande 8 : la borne protège la réponse, pas la livraison.** Les chaînes de `motif` sont écrites dans chaque livraison, que l'instance d'analyse lit pour ranger la lecture dans son cas. Si une chaîne nommait un trait ou une méthode, la livraison la porterait de toute façon, et l'empreinte demandée ne cacherait rien. La même faiblesse touche la branche (b) de la demande 9 (`statistique_agregateur`, ligne 101), que j'avais proposée en R6.
- *Retouche, demande 8.* Remplacer la dernière phrase de la « réponse attendue » par : « Si une chaîne dit autre chose que la nature d'un manque, par exemple un trait ou une méthode, ne la donne pas ; dis qu'elle existe, et change-la dans la version de la demande 1 pour qu'elle ne nomme que la nature du manque. Donne alors la chaîne nouvelle. »
- *Retouche, demande 9 (b).* « …ou s'il nomme le calcul d'un moniteur : dis-le, sans la valeur, et fais écrire à sa place, dans la version de la demande 1, une étiquette fixe qui ne nomme pas ce calcul. Donne cette étiquette. »
- **Demande 15 : sans danger.** Le nom du fichier livré n'est pas le nom d'un programme habilité, et l'analyse reçoit ce fichier de toute façon. « Rien d'autre » suffit. **Admis.**

**3.2 — Demande 29 (pièce du lecteur, ligne 71) : l'exemple fictif de ligne de révocation.**
- *Risque.* Le constat de lancement lit le registre courant de la branche principale pour y chercher une inscription et des révocations. Un exemple fictif poserait deux dangers :
  - s'il était écrit au registre, ou dans un fichier que le constat lit, il pourrait être pris pour une vraie ligne : une révocation fictive bloquerait la lecture ; une inscription fictive l'ouvrirait ;
  - s'il imitait la suite réelle des identifiants (GO-AAAA-MM-JJ-NN) ou portait une empreinte de forme valide, il pourrait servir de gabarit et se confondre avec une ligne réelle dans une recherche par motif.
- Demander la forme est nécessaire. L'exemple n'est sans danger qu'avec ces bornes.
- *Retouche.* Ajouter à la « réponse attendue » : « L'exemple est donné dans la réponse seulement, jamais écrit au registre. Son identifiant est hors de la suite réelle (par exemple `GO-0000-00-00-00`), et l'empreinte qu'il cite est faite de soixante-quatre zéros. »
- Ajouter pour la relance, à l'écriture du constat : « le constat refuse explicitement ces deux valeurs, et son épreuve d'artefact (R5) joue cet exemple et doit le refuser ».

## 4. Demande 25 : le renvoi à la note du développeur par son empreinte abrégée

Je ne l'ai pas ouverte. Le renvoi en lui-même n'apprend au lecteur habilité ni résultat ni attente : la note est du côté habilité, il y a déjà accès, et rien de la relance n'y entre. Deux points peuvent toutefois peser sur son attestation.

- **Ancrage.** Le renvoi l'envoie vers les conclusions du développeur sur la question même qu'il doit juger : le titre de la note porte l'hypothèse de l'échange par paire. Son « oui, non ou indéterminé » doit être indépendant de l'auteur des moniteurs.
  - *Retouche.* « La note sert à nommer les trois différences ; juge-les sur le code du lanceur et de la lecture, non sur les conclusions de la note. »
- **Enjeu dit.** La ligne 50 dit que la réponse accompagne la question du schéma de permutation posée à Lazar, qui pèse sur la puissance de « repère ». Le titre de la note le laisse deviner, et la ligne ajoute qu'aucune règle du texte n'en dépend. L'effet est faible.
  - *Retouche facultative.* « Un avis joint à une question posée à Lazar. Aucune règle du texte n'en dépend aujourd'hui. »
- **Empreinte abrégée.** `95e656e7…` ne permet pas de savoir quelle version de la note a été lue. Ce n'est pas un biais, mais une traçabilité faible.
  - *Retouche.* « Cite, dans ta réponse, l'empreinte entière de la version de la note que tu as lue. »

## 5. Autres contrôles

- **Pièce du lecteur, ligne 38 (demande 23).** Elle désigne des dossiers et des préfixes, sans contenu, et la réponse attendue est « juste » ou une empreinte. **Admis.**
- **Données personnelles et clés.** Aucun nom de personne hors de Lazar, aucun courriel, aucune clé, aucun identifiant de session dans les deux pièces.
- **GO cité.** Seul GO-2026-11-19-70 est cité, déjà vérifié sur `origin/main` dans la relecture v1.

## Retouches, liste courte

1. Pièce du développeur, ligne 5 : retirer les renvois à la première version et à la relecture. Inscrire au mandat du développeur les quatre fichiers à ne pas ouvrir, et ne porter sur la branche principale, pour lui, que sa pièce, ou bien les autres avec cette consigne (2.1). **Bloquant.**
2. Demande 8 : une chaîne de `motif` qui nomme un trait ou une méthode est changée dans le module, et non seulement cachée dans la réponse (3.1).
3. Demande 9 (b) : même correction pour `statistique_agregateur`, avec une étiquette fixe dans le module (3.1).
4. Demande 29 : l'exemple fictif est donné dans la réponse seulement, avec l'identifiant `GO-0000-00-00-00` et soixante-quatre zéros ; le constat les refuse, et son épreuve d'artefact le vérifie (3.2).
5. Demande 25 : juger sur le code et non sur les conclusions de la note ; citer l'empreinte entière lue ; facultatif, ligne 50 plus neutre (4).
6. Ligne 58 du développeur : « la ligne de GO renvoie à cette lecture » (2.4, non bloquant).
