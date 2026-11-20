# Cadre de la v70 de l'orchestrateur de l'organisme d'idéation — lecture du registre des tentatives par la génération suivante — v2

- Auteur de la v1 : rédacteur neuf, modèle F, le 2026-11-20 (relevé de `date -u` : 02:39:15Z). **Version 2**, par un autre rédacteur neuf, modèle F, le 2026-11-20 ; relevé de `date -u` : 04:51:32Z, après la lecture des pièces et avant l'écriture. La v1 (`cadre-lecture-registre-orchestrateur-v70-v1.md`, `84651a4c658e88f0bca7d299746ae05c267ae7f9f2002d8371dd19fccef4a5ee`) reste telle quelle (règle R12).
- Statut : **pièce de travail ; la v1 a été contre-lue (contre-lectures v1 et v2 de l'additif, modèle O, sans correction numérotée sur le cadre), cette v2 ne l'est pas. Un cadre, pas un additif** : rien ici n'est scellable comme règle d'un lancement. Il sert la conception suivante. Il n'allume rien et ne dépense rien.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-additif-orchestrateur-v69-v1.md` (`0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736`), sur `GO-2026-11-20-05` (2b). Mandat de la v2 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/mandat-redacteur-additif-orchestrateur-v69-v2-v1.md` (`34a63552217626c8a3ec187dfbc6cf270352723cdcaa28a076c2ae60bc66d70d`). La v2 ne change que trois choses : la tenue (titre, lignes de version), la décision D3 marquée tranchée (§ 3, point 1) et une précision de la contre-lecture v1 (§ 3, point 3).
- Sources avec chemin et empreinte : rapport joint, § 1. Je n'ai pas lu le code de l'orchestrateur.

## 1. Ce que (2b) demande

Mot de Lazar (`GO-2026-11-20-05`, 2b) : alignement complet sur l'héritage. La génération suivante lit ce que sert le registre des tentatives : **toutes les tentatives, avec leur classe d'issue**. La divergence entre `GO-2026-11-19-89` et `GO-2026-11-19-76` est tranchée du côté de la lecture de l'héritage.

| ce qui est lu | source |
|---|---|
| le registre des tentatives : une entrée par problème, une ligne par tentative ; champs `probleme`, `tentative`, `justification`, `prediction`, `resultat`, `gardee`, `provenance` | plan de l'héritage v5, § 1 |
| **toutes** les tentatives, gardées ou non ; aucun tri, aucune sélection, aucun rang, aucun compte de survivantes | plan v5, § 1 ; `GO-2026-11-20-05`, 2b |
| `resultat` : la classe d'issue de l'épreuve de la tentative, ou le statut « non éprouvée (budget) », et son coût ; rien de plus fin (ni la valeur de la statistique, ni la distance au seuil) | plan v5, § 3.2 ; `GO-2026-11-19-76`, point 2 |
| **rien du juge** : aucune note, aucun rang, aucun verdict, aucun texte d'un juge, à modèle ou statistique | `GO-2026-11-19-89` ; plan v5, § 3.1 |
| rien de la clé du monde planté, rien du monde de la mesure finale, aucun nombre d'items plantés | plan v5, § 1 |
| les champs libres entre balises de donnée | plan v5, § 1 (section c.8 du plan d'origine) |

Conséquence de (2b), à écrire en tête de la conception : **servir les seules survivantes n'est pas la règle de l'organisme.** La lecture de la v68 (nom et énoncé des seules fiches retenues) est un tri ; elle reste éteinte.

## 2. Ce que la v68 sait faire, et ne sait pas faire

| | la v68 |
|---|---|
| sait | jouer plusieurs générations sous un plafond de course ; lire, à la génération suivante, la sélection scellée d'un étage, en objet, vérifiée (sceau, empreinte) ; passer chaque ligne servie à la garde des étiquettes interdites ; omettre la section quand il n'y a rien à servir ; écrire sur la ligne de la génération ce qu'elle a lu (`heritage_lu`) |
| ne sait pas | lire un registre des tentatives : elle ne lit que la sélection d'un étage, et seulement les fiches retenues, par leur nom et leur énoncé |
| ne sait pas | servir une tentative non gardée, une classe d'issue, un statut, un coût, une justification, une prédiction |
| ne sait pas | tenir un registre : ajout seul, chaîne d'empreintes, prédiction scellée avant l'épreuve, scellement par génération |
| ne sait pas | faire payer la lecture sur le budget du bras (règle 6 du plan : appels retirés par permutation semée) |
| ne sait pas | cloisonner des bras, remettre à zéro l'historique de la source, geler un registre en lecture seule pour une génération finale |
| ne sait pas | lire sans étage : la lecture exige l'interrupteur des tests de mort |

Source : rapport du développeur de la v68, § 3 à § 5 et § 8 ; contre-lecture de la v68, constats 4 et 6 ; plan v5, § 1 et § 2.

## 3. Ce qui reste à concevoir, dans l'ordre

1. **Ce qui est servi, champ par champ.** `GO-2026-11-19-76`, point 2, sert `resultat` et `gardee` « à revoir au point 7 du palier 0b » ; (2b) dit « toutes les tentatives et leur classe d'issue ». La décision D3 du rapport joint est tranchée, option (a), par le mot de Lazar du 2026-11-20 (« go reprise, go recos », lu comme l'accord sur D1 (a′), D2 (a), D3 (a)), sous réserve de l'inscription de cette lecture par la mère : la réserve de `GO-2026-11-19-76`, point 2, tient ; la v70 se conçoit maintenant avec les deux formes (registre servi avec `resultat` et `gardee`, et registre servi sans ces deux champs), et la lecture du point 7 du palier 0b choisit entre elles. La conception n'attend pas ; l'allumage de la lecture reste un nœud, et rien n'est servi à un agent sans un mot de Lazar. Le repli écrit du plan (registre servi sans `resultat` ni `gardee`) est une valeur de configuration, non une version de plus.
2. **Les mots des classes servies.** Les trois classes et le statut de l'additif de la v69 (§ 4.2). À trancher : le verdict précis de chaque « tient » (R-3209, point 3) est-il servi, ou reste-t-il sur disque ? Il est plus fin qu'une classe ; le plan borne le grain à la classe. Proposition du rédacteur : non servi tant qu'aucune épreuve ne l'a mesuré.
3. **La garde des étiquettes interdites face aux classes servies.** Elle refuse aujourd'hui des mots de verdict dans les consignes (sa liste est une valeur de configuration, `conf["etiquettes_interdites"]`, `course2_v68.py` l. 246 ; les essais de la v68 cherchent « survit », « éliminée », « non concluant », « notable », « verdict agrégé », `test_v68_course2.py` l. 505). Servir « tient » et « ne tient pas » est permis par (2b) ; la liste de la garde et ses essais sont à reprendre pour que la classe d'une épreuve exécutée passe et que tout mot d'un juge reste refusé. À confirmer sur le code.
4. **Un interrupteur neuf, nommé**, distinct des deux de la v68 : « lecture du registre par la génération suivante ». L'interrupteur de lecture de la sélection reste refusé en réel. Les régimes : lecture du registre avec étage (l'héritage) ; lecture du registre sans étage, si une épreuve le demande (la v68 refuse la lecture sans étage).
5. **Le lecteur du registre** : module neuf ; lit le registre scellé de la génération précédente (sceau, chaîne, empreinte consignée) ; rend un objet ; aucune analyse de texte ; chaque ligne passée à la garde ; l'empreinte du texte servi écrite sur la ligne de la génération, comme `heritage_lu`.
6. **Le coût de lecture** : la règle 6 du plan, dans la garde de budget de la course ; le reliquat rapporté.
7. **Registre vide, registre trop long.** Section omise ou servie vide ; borne de longueur, et ce qui est servi quand le registre la dépasse, sans tri par issue (ordre de scellement, ou tirage par graine).
8. **Les gardes**, chacune avec son cas sain et son artefact : rien d'un juge dans le registre ni dans ce qui est servi ; tranche d'épreuve jamais servie ; grain du retour ; champs du bras sans registre jamais servis ; génération finale sans écriture ; cloisonnement des bras ; historique de départ vide.
9. **Additif de la v70, lanceur suivant, devis, ligne d'accord** qui nomme l'interrupteur neuf. L'allumage reste un nœud : ce qui est servi à un agent.

## 4. Ce qui précède la v70

- Le palier 0b lu (issue, point 7), et le palier 1 joué par la v69 : il mesure la taille d'un registre d'une génération, donc la part que prend sa lecture (devis v5, § 3).
- La première épreuve de la v70 est le premier palier de l'héritage qui sert un registre (le pilote de bruit, palier 2a), sous son préenregistrement, son devis et sa ligne.

## 5. Ce que ce cadre ne prend pas

La course « nouvelles attaques » demande elle aussi un lecteur d'un registre, pour une course sans épreuve exécutée ; sa conception (`docs/notes/ideation-nouvelles-attaques-v1/conception-v3/ordre-course-nouvelles-attaques-v3.md`, `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22`) le porte sous un nom de version neuf, jamais v69 ni v70, avec ses propres issues d'aiguillage. Ce cadre ne fixe ni sa forme ni ses issues. Question ouverte, pour les deux conceptions : un seul module de lecture pour les deux, ou deux ; je ne la tranche pas.
