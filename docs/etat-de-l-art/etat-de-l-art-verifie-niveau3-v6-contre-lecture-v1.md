# Contre-lecture de la synthèse de l'état de l'art vérifié de niveau 3, version 6 — v1

- **Date et heures** (`date -u`) : commencée le Sat Nov 14 07:48:40 UTC 2026 (relevé recopié de la sortie de la première commande) ; fin de rédaction, relevée dans la commande qui écrit ce fichier : Sat Nov 14 07:50:02 UTC 2026.
- **Contre-lecteur : sous-agent, modèle B ; auteur de la synthèse : modèle A ; A ≠ B.** J'ai écrit la contre-lecture de la v5 (`6188e80040468b32ab97ab28f7c101e44510d365dc07ef7c750c44cc838f17cf`) ; je n'ai écrit ni la v6, ni aucun rapport, ni aucune décision.
- **Objet** : confirmation courte — les constats A à M de ma contre-lecture de la v5 sont-ils appliqués ?

**Empreintes recalculées, égales à l'attendu.**
- `etat-de-l-art-verifie-niveau3-v6.md` : `8b9a27282c3d6175462c6f35f391758d68a34d57fa325762bd974cab34e379de` (« la v6 », 826 lignes ; numéros de ligne du fichier).
- `etat-de-l-art-verifie-niveau3-v6-journal.md` : `b6e778ead5892dbaef9e514319a186846df5eb47c7ffeefe22ec2d0ac295fb67`.
- `etat-de-l-art-verifie-niveau3-v5.md` : `303c5f2f6d7e52d8cd7e6aefa4f44577474903f6c7477069244059c468af018b`.
- `docs/decisions/decision-N-003-N-004-v1.md` : `cc1be39369bc4dae9b3166c513d783b4744c62d839951f047a44396aa3a81a5a`, égale à son compagnon.

**Étendue réelle de ma lecture.** La v6 comparée à la v5 par `diff` (41 lignes retirées, 68 ajoutées, 33 blocs), puis mot à mot par programme (`scripts/diff_mots_v1.py`, dans l'archive) : **tous les mots changés lus**, dont la section 2 quinquies en entier, les lignes L, H1, T, H5, H8 de la table, le prononcé (points 2, 4, 6, 7), les phrases pour un jury de L et de HC4 relues en entier (l. 801, 815), la ligne M4 (l. 182). Les lignes HC4 et HC6 de la table sont identiques à la v5 (aucun bloc du `diff`) : non relues. Le journal de la v6, en entier. La décision N-003/N-004, en entier (87 lignes). `rapport-L-voisins-v2.md`, section 2.1 (l. 88 à 129), en entier, pour le constat B. Le reste de la v6 n'est connu que comme identique à la v5. Aucun PDF, aucune archive, aucun registre.

Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive, aucune suppression ; rien sous `registres/`, `diag/`, `runs/`, `donnees/` ; rien de T0.7, de 7a ni de 7b. **Aucun refus ; aucune ouverture fautive.**

---

## Verdict

**Utilisable.** Les treize constats sont appliqués, dont un autrement que mon texte et mieux (B). Deux restes mineurs (N, O), sans effet sur un verdict, une ligne « déclarable » ou une phrase : à porter si une version suivante est écrite.

Lignes « déclarable : oui » : **H3, H5, H7, T pour (c) à (f)**. Je n'en conteste aucune ; la réserve que je portais sur T (constat F) est levée. Limite inchangée : ni les rapports du niveau 3 ni K-T ne sont rouverts.

## Application des constats A à M

| constat | état | où je l'ai vérifié dans la v6 | remarque |
|---|---|---|---|
| A — mot de Lazar sur L1 inscrit, porté « en attente » | appliqué | en-tête (l. 18) ; prononcé, points 2, 4, 7 (l. 47, 49, 55) ; table, L (l. 103) ; R7 (l. 257) ; section 3 (l. 339) ; sections 7, 8, 9 (l. 580, 592, 601, 608) ; section 12 (l. 801, 821) | Les onze endroits sont à jour. Le mot fixe L1 seulement ; L reste « non » par la condition 4 ; le nœud devient « portée du mot ». La phrase d'ensemble garde « quatre » entre guillemets (texte de B2) et sa réserve dit « cinq » : acceptable. L'état « examiné par la mère (R-2657) » du mot sur H6 vient du message de la coordination : non vérifiable par moi. |
| B — contre-indice de Ker (L2, fragmentation) non reporté | appliqué autrement mais acceptable | table, L (l. 103) ; section 3 (l. 334, 335) ; section 12 (l. 801) | **L'auteur a raison contre mon texte.** K-Lv, section 2.1 : la loi de la moyenne est indépendante de la répartition (p. 7) — elle est indifférente, l'étalement ne la « sert » pas ; face au rapport de vraisemblance généralisé, l'attaquant étale si la charge est petite et concentre si elle est grande (p. 9-10) ; face au compte des signes il concentre (p. 6) ; la synthèse de Ker conclut à la concentration (p. 11). Mon « étaler ne sert l'attaquant que face à la moyenne » était inexact sur ces deux points. La version de la v6 est celle du rapport ; L2 est dit « voisin et contre-indice ». |
| C — phrase pour un jury de L plus forte ou autre que les pièces | appliqué | section 12 (l. 801) ; section 3 (l. 337) | « Pour la somme » ajouté ; « réserve » ne porte plus que sur le séquentiel ; deux valeurs, objets tirés au hasard ; « sans preuve » ; contre-indice et borne ajoutés. Mention « proposition, non publiée, à décider par Lazar » gardée. Pas plus forte que les pièces. |
| D — intervalle faux pour les écarts de H1 | appliqué | table, H1 (l. 101) ; section 3 (l. 302) | « d'environ −51 à +33,1 points », cinq valeurs imprimées ou calculées sur l'imprimé, quatre fourchettes : conforme à K-H1b. |
| E — borne de Ker 2007 sur les règles lues en séquence | appliqué | table, L (l. 103) ; section 3 (l. 334) ; section 12 (l. 801) | Marquée déduction non imprimée, à vérifier avant usage. |
| F — « ne touche pas T » non vérifié, pour une ligne « oui » | appliqué | prononcé, point 7 (l. 52) ; table, T (l. 104) ; section 3 (l. 339) ; table 10.2 (l. 644) | **Vérifié par moi sur la décision** : « invariances exactes » figure à la l. 75, dans la revendication de L (section 2), et renvoie à L1 (l. 60, « exacte ») et à L4 (l. 61, « exactement invariante ») ; la revendication de T (l. 45 à 49) ne l'emploie pas : unification par sous-groupes, distinction C / K et ses signes, garanties locales, mesure. La zone touchée par Ker est celle de L seul. La phrase de la v6 sur ce que posent les deux pièces (« sans classe de permutations ni lecture séquentielle ») est une lecture de l'auteur d'après les rapports, dite telle. Réserve levée. |
| G — H5 : 2609.15994 non rattachée | appliqué | table, H5 (l. 120) ; table 10.2 (l. 651) | — |
| H — H8 : 2609.15994 dite non lue | appliqué | table, H8 (l. 110) | — |
| I — « R1 à R7 » ; R1 sans renvoi à 11.3 | appliqué | prononcé, point 6 (l. 51) ; R1 (l. 251) | — |
| J — Filler, Ker et Fridrich 2009 mal attribué ; liste incomplète | appliqué, sauf un endroit | prononcé (l. 55) ; table, L (l. 103) ; R7 (l. 257) ; section 3 (l. 340) | La ligne M4 (l. 182) n'a pas changé : constat N. |
| K — non-compensation attribuée à K-Lv, section 5 | appliqué | table, L (l. 103) | — |
| L — phrase de HC4 : préférence devenue restriction | appliqué | section 12 (l. 815) | « de préférence » rétabli ; zone peu cherchée et voisin non lu dits dans la phrase. |
| M — prononcé : occupation de HC6 | appliqué | prononcé, point 2 (l. 47) | — |

## Constats nouveaux

| constat | gravité | endroit | preuve | texte corrigé proposé |
|---|---|---|---|---|
| N — | mineur | l. 182 (section 2.1, ligne M4) ; l. 279 (section 2 quinquies, J, colonne « où ») | La section 2 quinquies dit J corrigé en « section 2.1 (M4) » ; la ligne M4 est identique à celle de la v5 (aucun bloc du `diff`) et finit toujours par « restent non lus Huang, Wang et Poor 2021, Bash et collègues 2014 et 2016, Arumugam et Bloch 2016, Trivedi et Chandramouli 2003 ». La liste complète est juste aux quatre autres endroits. | Ajouter à la ligne M4 : « ; Filler, Ker et Fridrich 2009 (K-Lv, section 7 ; K-Lk, section 5) ; Cachin 2004 (K-Lk, section 5) ». |
| O — | mineur | l. 338 (section 3, L, « Ce qui reste distinctif … ; non tranché ») | La parenthèse « non tranché » reprend le titre des rapports ; depuis le mot inscrit (R-2657), L1 est tranché (l. 339, deux lignes plus bas). | « (… ; non tranché par les lecteurs ; tranché depuis pour L1, puce suivante) ». |

Version 1 ; ne sera jamais réécrite (R12). Fichiers de travail (script de différence mot à mot, ses sorties) dans `fichiers-de-travail-contre-lecture-synthese-niveau3-v6.tar`.
