# Rapport de préparation — demande 7 (essaim qui communique) — v1

22 novembre 2026. Aucune dépense, aucun appel réseau, aucun appel de modèle, aucun commit, aucune poussée. Aucun refus de permission, de classifieur ou de garde rencontré.

## Pièces rendues (dossier de travail)

| pièce | sha256 |
|---|---|
| `contexte-organisme-essaim-v1.md` (≈ 2 480 mots comptés par `wc -w`, chemins et empreintes compris) | `e767cf402e8d1c1f83f7054eded3a71c5a121b6a3d773bc8e974a64e5e724f36` |
| `demande-7-essaim-communicant-v1.md` | `7d3fbcf066573e3c81144cf48261b3f8e61230389df288fe1fed0594d02651d5` |

Chacune a son compagnon `.sha256` (écrit par `sha256sum`).

## Chemins lus, avec empreintes

Sur `origin/main`, extraits par `git show` vers `sources/` du dossier de travail :

| chemin | sha256 de la copie |
|---|---|
| `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` | `8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2` |
| `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` | `534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b` |
| `docs/notes/demandes-fable-api-2026-11-22-v1/demande-3-fausses-alertes-honnetes-v1.md` | `0b76eca75dea2c0cc1c14a1605b0e999b735bf9238e9242a6ad08b54f1b157a4` |
| `docs/sources/alphaxiv-society-ai-scientists-v1/a-society-of-ai-scientists-2026-11-21.pdf` | `1c1d3d84347d7736b31cae6951af435ee9332ed5aa431be55e7ccdbbfc578f5d` (conforme à l'attendu `1c1d3d84…`) |

Le PDF (67 pages) a été extrait par `pdftotext -layout`, pages numérotées par les sauts de page ; texte principal lu des pages 1 à 12, 21 à 22, 27, 32 à 35 ; page 64 (figure D1) ; le reste parcouru par recherche de termes seulement.

Sur la branche courante (empreinte recalculée, conforme au compagnon `.sha256` pour chacune) :

| chemin | sha256 |
|---|---|
| `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` |
| `docs/notes/organisme-re-search-v1/analyse-journaux-re-search-v1.md` | `8a82b5ee1eb709ac752212a40fc181b7a7c236c4b5c5dfa0315825bfb3ae08bc` |
| `docs/notes/organisme-re-search-v1/anteriorite-re-search-v1.json` (lignes 1 à 688 et 860 à 951 ; la passe 2 au-delà de la ligne 688 non lue) | `c3835fe410f91ccc6a61128f6f92c998914f883d1f18c8ea4d59d6f96f4f9828` |
| `docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md` | `50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b` |
| `docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v2b.md` | `b2319472cbad20d87664b63edcdab47914de1d81135841b81f10954f6f45da0e` |
| `docs/notes/organisme-auto-conception-v1/mandat-planificateur-plan-v4-course-principale-v1.md` | `1bf2d874d2c575dbdc62641a088d0abdea6d9ea3d3cc18f4cfebd0b51184234d` |
| `docs/notes/organisme-auto-conception-v1/mandat-planificateur-experimentateur-tests-de-mort-course-principale-v1.md` | `e4ca4586cd603fbf79486752604158fca8c5595d51e6af26e0309ce0f35d80d0` |
| `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md` (lignes 1 à 298) | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` |
| `registres/etat.md` (titres et extraits courts autour du mot « organisme » seulement ; registre vivant, sans compagnon) | `d5ff39f6cbd8780ade51a2bd9b3f9baad21d4e8692e4dece07504074982a5b07` |

`ls` fait sur `docs/notes/organisme-auto-conception-v1/` et `docs/notes/organisme-multi-generations-v1/` (racines seulement).

## Ce que je n'ai pas pu lire, ou pas lu

- **`registres/etat.md`** : les lignes du registre sont très longues ; une recherche du mot « organisme » a rendu une sortie trop grande, que l'outil a rangée sous `/root/.claude/…` ; je **ne l'ai pas ouverte** (chemin interdit). J'ai lu à la place des extraits de 160 caractères. Le registre ne m'a rien appris d'utile sur l'architecture ; le contexte s'appuie sur les devis et la conception v4.
- **Les autres pièces de tête** des deux dossiers (devis v2, conceptions v1 à v3, contre-lectures, vérifications, brouillon de consigne d'un proposeur) : non lues, par économie et pour ne rien tirer d'une consigne destinée à un modèle.
- **Le PDF de Re-Search** et `lecture-re-search-v1.md` : hors de la liste ; non lus.
- **`registres/go.md`** : hors de la liste ; la ligne GO-2026-11-22-12 point 4 est reprise du mot transmis par la demande, non relue.
- **La description de l'aiguilleur** : aucune pièce lue ne dit sa fonction ; seul son compte d'appels est cité.

## Écart à l'en-tête, déclaré

- J'ai fait un `ls` sur `docs/notes/organisme-re-search-v1/`, dossier dont seuls deux fichiers étaient nommés (pour vérifier la présence des compagnons). Aucun fichier de la liste obtenue n'a été ouvert hors des deux nommés et de leurs compagnons.
- J'ai aussi ouvert les compagnons `.sha256` des pièces lues (pour vérifier les empreintes) ; ils ne sont pas nommés par la demande.

## Affirmations laissées « non vérifiées » ou « rapportées »

1. Les deux mesures de Re-Search (« nombre de branches ouvertes », « score au tour k comme prédicteur du score final ») : mot du directeur, non vérifié sur le PDF de Re-Search.
2. Ce que fait Re-Search (vingt questions, 200 articles d'une conférence) : lu sur le début du résumé dans `anteriorite-re-search-v1.json`, non opposable.
3. L'antériorité de l'écart entre produire et vérifier : lue sur résumés par un autre lecteur, non opposable.
4. Les résultats de la source descriptive sur le troupeau (88 % contre 30 %), le tableau partagé (15,7 points, 35 % de jetons en moins) et le comité à rôles (3,5 fois) : **rapportés par l'article** à partir d'études écrites par des agents de la cohorte ; protocoles et répétitions non lus.
5. « Aucune expérience de l'article ne compare la société entière à un agent seul au même coût » : vrai pour le texte principal lu (pages citées) ; les annexes n'ont été parcourues que par recherche de termes. La formule de la demande (« sans comparaison à l'agent seul ») est donc juste au niveau de la société, mais **des études de la cohorte comparent bien, à petite échelle, communication, indépendance et agent seul à calcul égal** (p. 22, p. 64) ; je l'ai écrit tel, par la règle anti-faux-gap.
6. L'empreinte de la sortie JSON de l'analyse des journaux (`3b65a5e8…`) est citée d'après la note, non recalculée.
7. La nature exacte du juge statistique (« type e-valeur ») : inférée du champ `log_w_max` et du contexte ; non vérifiée dans le code.

## Choix de rédaction

- Aucun nom de personne : le directeur est nommé par sa fonction ; la source descriptive et les antériorités par titre, date et identifiant, sans auteurs ; les noms d'agents de la cohorte omis ; les espèces de proposeurs non nommées.
- Aucune consigne d'attaque, aucun texte de saboteur, aucune donnée de référence cachée : la famille de mondes est décrite par sa structure publique (déclarée publique avec le générateur, conception v4, § 2.2) ; aucune loi d'un monde secret n'est citée. Les suites d'essais sous le juge sont décrites par leurs mesures seulement.
