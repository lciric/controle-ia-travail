# Note du rédacteur — brouillon 40 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même rôle que pour les brouillons 21 à 39. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon40.md`, `b4670b88b8abb73b2a40c61fb5d1cf17bb513b52b710ba9b06b22b0e4304db89`, scellé comme brouillon. 2 414 lignes.
- **Point de départ** : le brouillon 39 (`4425e9e922044a749a6d1357f2fadbc9e212d8f4843e954b704792840ae23b61`), inchangé.
- **Heures (UTC, relevées par `date -u`)** : commencé le 2026-11-20T11:30:09Z ; texte scellé à 11:40:37Z ; note finie à 11:42:09Z.
- **Méthode** : 45 remplacements exacts ; 44 sur une ancre trouvée une seule fois, un sur une chaîne remplacée deux fois (la formule du mineur m-1). Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé.
- **Pièces traitées** :
  - la vérification du brouillon 39, `docs/notes/relance-organismes-discrets-v1/verification-brouillon39-bras-a-v1.md`, `df82b2f3fe514de31d6b29535b731d6130bb437b418dfb7403958789612d1d4e` ;
  - les mots de Lazar sur le second lecteur et le juge des deux ancres, `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-second-lecteur-et-juge-des-ancres-bras-a-2026-11-20-v1.md`, `8189dcec0f83a74fde8c8b1ac82a74142f946f77dfda41b88e95d547c4534d6a` ;
  - les lignes GO-2026-11-20-31, -38 et -43 du registre, lues par `git show origin/main:registres/go.md`, tête locale `3c2b1436`, sans appel réseau ;
  - la recherche de la session principale sur les deux modèles, `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md`, `f7090b5d52b638b5cbc461661768c4990d1557f1a1b19c63fb2139c4fca8da61`, lue par `git show origin/main:`, empreinte recalculée sur cette lecture. Elle est absente de la branche de la relance.
- **Aucune fiche n'est ajoutée.**

## 1. Points traités

| point | ce que le texte écrit | où |
|---|---|---|
| **C-1, second lecteur** | `gemini-4-carbon` ne lit plus. Le second lecteur est le meilleur de deux modèles, le modèle de Mistral dit « le chonk » et un modèle de DeepSeek, sur un essai de mesure comparatif | conventions ; 3.4 ; 13.1 |
| **C-1, juge des deux ancres** | `gpt-6.2-astra` ne juge plus. Le juge est celui des deux qui n'est pas désigné second lecteur | 3.4 ; 6.3 (d) ; 6.11 ; 12, marque du nœud 1 ; 13.1 |
| **C-1, essai comparatif** | les 24 entrées synthétiques de l'essai de mesure, les deux consignes, un réglage par modèle (l'effort le plus haut), 48 appels, deux files. Rapport : champs techniques, forme conforme, et un compte neuf, les réponses étayées. Personne ne lit les réponses | 3.4 |
| **C-1, règle de désignation** | fermée, en huit points (partie 2 de cette note) | 3.4 |
| **C-1, bancs publics** | hors de la désignation (partie 3) | 3.4 |
| **C-1, familles** | Claude, Mistral, DeepSeek, hors Llama et Qwen. Quatre contrôles : deux développeurs distincts ; identifiant exact confronté à la liste par le lecteur habilité, qui seul l'ouvre ; voie d'accès du développeur ; version relevée à chaque appel | 3.4 ; 13.1, case « familles » |
| **C-1, identifiants et voies d'accès** | proposés, à confirmer par Lazar. La case porte de nouveau la marque | 13.1, case « lecteurs et juge des ancres » |
| **C-1, version** | un alias qui suit la dernière version ne fige rien : la version est constatée, avant et après chaque file et chaque lot. Si elle change : à l'essai, le modèle ne tient pas ; à la course, l'issue de 8.2, inchangée | 3.4 ; 13.2, case neuve |
| **C-1, envoi des textes** | condition d'admission d'un candidat, sur un mot de Lazar (question 2) | 3.4 ; 13.1 |
| **C-1, clé de graine** | `carbon` reste le nom de clé du lecteur 2, quel que soit le modèle. Ni les tirages ni le code arrêté ne changent | 6.2 |
| **C-1, dépense** | aucune n'est ouverte. Une ligne neuve au tableau des dépenses : 48 appels, plafond à écrire au devis. La projection de 97,0 USD du second lecteur tombe | 6.11 ; 13 ; 13.2 |
| m-1 | « posée à Lazar avec la réponse du développeur » est retirée, aux trois endroits. Il reste « réexpliquée », ce que dit la pièce | 6.9 ; 12, marque du point 19 ; 13.1 |
| m-2 | l'arrêt levé pour le moniteur appris non ajustable n'est plus dit refusé. Il est renvoyé à la garde de procédure, comme au point 19 | 8.4 |
| m-3 | « qui confirme quoi » : les réponses 1, 2 et 3 passent du côté confirmé ; la pleine précision des nombres (réponses 5 et 32) du côté de la parole du développeur | 13.1, case du module |
| m-4 | l'objet de l'attestation de la version 7 à la version 10 est à préciser auprès du lecteur habilité ; la question est écrite | 13.1, case du module |
| m-5 | la contre-lecture de la configuration renvoie à 8.7 | 13.2 |
| m-6 | la ligne d'en-tête de la pièce sans interne rangée sous un dossier cloisonné est qualifiée : pièce permise à la relance, dossier non ; empreinte reprise du brouillon 39, non recalculée | en-tête |

## 2. La règle de désignation, telle qu'écrite en 3.4

1. **Un candidat tient** au critère du devis de l'essai de mesure, section 7.2, inchangé : 24 réponses de code 200, sans refus, sans fin par sortie maximale, 22 de forme conforme au moins. De plus : une seule chaîne de version sur ses 24 réponses, et la même version affichée avant et après sa file. Ne tient pas : file arrêtée au plafond, file coupée, candidat non joignable, candidat non admis.
2. Une file n'est jouée qu'une fois.
3. **Les deux tiennent** : le second lecteur a le plus de réponses étayées ; puis le plus de réponses de forme conforme ; puis le coût projeté le plus bas ; puis, à égalité entière, c'est Mistral. L'autre juge les deux ancres.
4. **Un seul tient** : il est second lecteur. Le juge n'est pas désigné : nœud de Lazar.
5. **Aucun ne tient** : nœud de Lazar.
6. Ni Carbon, ni Astra, ni un troisième modèle ne prend un rôle sans un mot de Lazar. Le texte n'est pas scellé tant que les deux rôles ne sont pas pourvus.
7. Sortie maximale : la règle du devis, point 7.
8. La règle est appliquée par programme. Elle est scellée avec ce brouillon ; le fichier de règle en est la copie, scellé avant le premier envoi.

**Admission d'un candidat**, fixée avant le premier envoi : identifiant et voie d'accès confirmés par Lazar ; mot de Lazar sur l'envoi des textes de la course à ce fournisseur ; famille contrôlée ; constat que le service rend une chaîne qui distingue deux versions.

**Le rôle de juge des ancres.** Aucune mesure propre n'est ajoutée. Le candidat non retenu tient au même critère que le lecteur, sur 24 lectures qui comprennent les huit que l'essai de mesure avait jouées pour Astra. Aucun essai ne juge la justesse d'un juge des ancres ; la limite écrite demeure.

**Réponse étayée** : réponse de forme conforme dont chaque extrait exigé est retrouvé à la lettre dans l'entrée, par les programmes de vérification des extraits de l'instrument. C'est un compte par programme, sur des entrées synthétiques. Il n'entre dans aucune variable, aucun seuil, aucun verdict du texte.

## 3. Les bancs publics

Ils n'entrent pas dans la désignation. La recherche de la session principale ne trouve aucun banc indépendant qui note les deux modèles sur le rôle : texte long, citation à la lettre, forme à deux champs. Les seuls écarts publiés viennent d'indices composites, et l'un d'eux note une préversion du modèle de Mistral. Ils n'ont servi qu'à proposer le modèle de chaque famille. GO-2026-11-20-43 précise GO-2026-11-20-38 dans ce sens : un essai de mesure comparatif, sous une règle scellée avant lecture.

## 4. Sections de jugement touchées

Le seul changement est le remplacement des deux modèles. **Aucune règle de jugement, aucun seuil, aucune issue, aucune prédiction ne change.**

| section | lignes changées | ce qui change |
|---|---|---|
| hypothèse, prédiction, métrique, seuil | 0 | — |
| 7.1 à 7.8 | 0 sur 102 | — |
| 10 | 0 | — |
| 12 | 2 sur 172 | fiche du nœud 1 : une marque ajoutée en fin de ligne, qui dit que le juge n'est plus Astra ; la fiche et l'option γ restent mot pour mot. Marque du point 19 : la formule du mineur m-1 |
| 6.3 (ordre d'exécution, gelé) | 1 sur 27 | étape (d) : le nom du juge des ancres. L'ordre ne change pas |
| 6.9 | 1 sur 64 | la formule du mineur m-1, dans une parenthèse d'histoire |
| 8.4 | 1 sur 105 | mineur m-2 : un artefact dit refusé est renvoyé à 8.7 |
| 6.1, 6.4 à 6.8, 6.10, 6.12, 8.1 à 8.3, 8.5 à 8.7, 9, 11 | 0 | — |

Sections sans jugement qui changent : en-tête et conventions (15 lignes), 3.4 (22 lignes, dont 19 neuves), 6.2 (1), 6.11 (3), préambule de 13 (2), 13.1 (4), 13.2 (4), 14 (14.52, neuve), contre-lecture (1).

## 5. Contrôles par programme

| contrôle | résultat |
|---|---|
| titres | 54, identiques hors le titre de niveau 1 |
| sections changées | celles de la partie 4, et rien d'autre |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 39 : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | 7 lignes, toutes en 13.1, 8 occurrences : les cinq du brouillon 39, plus « familles » et « lecteurs et juge des ancres » |
| table d'en-tête | 232 lignes à empreinte entière. **216 recalculées, toutes égales**, les modules de code compris (octets seulement, aucun ouvert). **15 sautées, aucune empreinte prise** : toute ligne dont le chemin ou la description touche un chemin cloisonné, la ligne du mineur m-6 comprise. 1 absente du disque : la recherche de la session principale, vérifiée par `git show` |
| validateur `problemes()` | les deux problèmes attendus, les mêmes qu'au brouillon 39 |
| noms des deux modèles remplacés | il en reste 51 mentions sur 32 lignes : l'histoire (en-tête, 14), le récit de l'essai de mesure joué (3.4), et les phrases qui disent qu'ils ne lisent ni ne jugent plus |

## 6. Questions pour Lazar

**Question 1 — identifiants exacts et voies d'accès.**
- Enjeu : la case de 13.1 ne se remplit pas sans eux, et « le chonk » n'est pas un identifiant.
- Proposé, d'après la recherche de la session principale :
  - Mistral : Mistral Large 4, `mistral-large-4-0`, `reasoning_effort` à `high`, par le service de Mistral, point d'accès européen ;
  - DeepSeek : DeepSeek V4.1 Flash, alias `deepseek-flash` (aujourd'hui `DeepSeek-V4.1-Flash-1017`), `reasoning_effort` à `max`, par le service de DeepSeek.
- **Recommandation : confirmer ces deux propositions.** Confiance : moyenne. Deux réserves : je lis « le chonk » comme le plus grand modèle de Mistral, ce que seul Lazar peut confirmer ; pour DeepSeek, le seul chiffre commun sur les textes longs met l'autre modèle de la famille devant, et l'alias proposé n'est pas figé.

**Question 2 — peut-on envoyer les textes de la course à DeepSeek ?**
- Enjeu : DeepSeek stocke en Chine, n'offre pas de non-conservation, et le refus de l'entraînement se demande par courriel, contact externe que seul Lazar envoie. Les lectures de la course portent des actions d'épisodes et, pour la couverture, la référence cachée. L'essai comparatif, lui, n'envoie que des textes synthétiques.
- Options, et ce que chacune change à la règle :
  - (a) oui, sans condition : la règle ne change pas, les deux candidats sont admis ;
  - (b) oui, après un refus de l'entraînement écrit et confirmé : DeepSeek n'est admis que si la confirmation est au dossier avant le premier envoi de l'essai ; sinon, comme (c) ;
  - (c) non : DeepSeek n'est pas admis et compte comme un candidat qui ne tient pas. Mistral, s'il tient, est second lecteur. **Le juge des deux ancres n'est alors désigné par personne** (règle, point 4) : Lazar devra en nommer un.
- **Recommandation : (b).** Confiance : moyenne. La référence cachée est ce que le confinement du texte protège ; l'envoyer à un service qui peut s'en servir pour l'entraînement, sans refus confirmé, l'expose. Pour Mistral, je recommande le point d'accès européen, le refus de l'entraînement dans la console et la demande de non-conservation au support, qui est aussi un contact externe.
- Je ne tranche pas.

**Question 3 — le compte des réponses étayées comme premier critère.**
- Enjeu : l'essai de mesure ne relevait pas la vérification des extraits. Je l'ajoute, pour que « meilleur » dise autre chose que « moins cher ». Je n'ajoute pas l'accord avec la construction des entrées.
- Options : (a) garder la règle écrite ; (b) retirer ce compte, et désigner sur la forme puis le coût ; (c) ajouter l'accord avec la construction des entrées.
- **Recommandation : (a).** Confiance : moyenne. Contre (c) : les entrées n'ont pas été bâties pour mesurer la justesse, un tiers d'entre elles sont « appariées pour moitié », sans vérité fixe, et la qualité des lecteurs revient aux épreuves du texte.

## 7. Ce qu'il faudra changer hors du texte

**Code arrêté en version 13 : rien à changer**, par le choix de garder la clé `carbon`. Recherche de chaînes (`carbon`, `astra`, `gemini`, `gpt-6`), sans lire les modules :
- `src/controle_ia/organismes_discrets/graines_bras_a_v4.py`, ligne 57 : `LECTEURS = ("claude", "carbon")`. Même ligne dans les versions 2 et 3. Les versions 10 à 12 ne portent pas la chaîne ;
- `src/controle_ia/organismes_discrets/epreuves_couverture_bras_a_v1.py` à `_v3.py`, lignes 72, 76 et 78 : un commentaire, « `claude` ou `carbon` » ;
- `tests/test_graines_bras_a_v12.py`, lignes 32, 136 et 140 : la clé `carbon` est admise, la clé `astra` refusée ;
- `configuration_bras_a_v12.py` et les modules des versions 12 et 13 : aucune mention.
- Si Lazar préférait une clé neutre, il faudrait une version neuve du module des graines et de ses essais, et les tirages du lecteur 2 changeraient.

**À écrire, hors du code arrêté** :
- le devis de l'essai comparatif : tarifs relevés et datés des deux modèles, plafond par file, constat de la manière dont chaque service rend sa version ; sa contre-lecture ; une ligne de calcul par file ;
- une version neuve du programme qui conduit l'essai (`scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` nomme les files Carbon et GPT), avec le compte des réponses étayées et le relevé de la version affichée ;
- sa configuration (`configuration-essai-mesure-lecteurs-bras-a-v1.json` nomme les files `carbon` et `gpt`, la clé `reglages_carbon`, et les motifs de fin de Google et d'OpenAI ; elle épingle la forme du brouillon 5) ;
- un relais par fournisseur, et le fichier de la règle, scellé avant le premier envoi ;
- la configuration de la course : identifiants, réglages, chaînes de version, relevé de la version affichée par lot.

## 8. Ce qui sépare encore le texte du scellement

- **Lazar** : les questions 1 à 3 ; puis les lignes de calcul de l'essai comparatif, sur devis.
- **Session principale** : la confrontation des deux identifiants à la liste des familles, par le lecteur habilité ; la question du mineur m-4 au lecteur habilité ; ce que la note du brouillon 39 listait déjà (attestation, lanceur de l'étape de discrétion, renvoi de la base).
- **Session de relance** : le devis, le programme et la configuration de l'essai comparatif ; l'essai ; la case remplie par la règle ; la vérification de ce brouillon ; puis ce que la note du brouillon 39 listait (commit du code, épreuve de forme, contre-lecture 10, scellement).

## 9. Réserves

1. **La version constatée.** Le texte dit qu'un changement de la version affichée, entre deux relevés, est une « chaîne de version différente de celle de la configuration » au sens de 8.2. Je n'ai pas touché 8.2, et l'issue est la sienne. Mais c'est une manière de plus de constater ce que 8.2 arrête. Au vérificateur de dire si c'est un report ou une règle ; si c'est une règle, elle devient une question pour Lazar.
2. **Un seul candidat tient.** Les mots de Lazar disent que l'autre devient juge. La règle exige qu'il tienne aussi ; sinon, nœud. J'ai préféré un nœud à un juge qui ne rend pas la forme.
3. **Le parti pris du compte étayé** est écrit dans le texte : un candidat qui rend souvent un verdict sans extrait y gagne.
4. **Le mineur m-2** est traité sans ouvrir le code, comme au point 19. Si un programme refuse bien cet arrêt sous la valeur gardée, la phrase est trop prudente, non fausse.
5. **Le récit de l'essai de mesure joué** garde les noms de Carbon et d'Astra, sous une phrase qui dit qu'il ne fixe plus que le lecteur 1. Le dernier passage pourra l'abréger.
6. **Le coût projeté** se compare au tarif le plus haut quand un service en publie plusieurs selon l'heure. C'est un choix de prudence, qui pèse contre DeepSeek au troisième critère seulement.
7. **Je n'ai pas relu le texte en entier.**

## 10. Fichiers ouverts, et débords

- Le brouillon 39, par passages et par programme ; sa note et sa vérification, en entier ; le brouillon 38, par programme.
- La pièce scellée des mots de Lazar, en entier ; le journal de la relance, entrées OD-226 à OD-233.
- Le registre des GO et la recherche de la session principale, par `git show origin/main:`, sans appel réseau.
- Le devis de l'essai de mesure, section 7 ; sa configuration et son fichier de règle, par programme.
- Deux pièces sans interne sous `docs/notes/bras-a-sans-interne-v1/` : la vérification habilitée de la version 10, en entier ; la lecture habilitée, demandes 24, 25 et 33 ; les réponses du développeur en version 3, dix lignes de sa table.
- `src/controle_ia/prereg.py` : la ligne de la marque, et le validateur exécuté.
- **Débords, déclarés** :
  - deux recherches de chaînes (`carbon`, `astra`) ont parcouru des dossiers entiers. La première, sur `src`, `scripts` et `tests`, écartait les dossiers cloisonnés, mais non tous les fichiers dont le nom touche T0.7 ou T0.8. La seconde, sur les fichiers de données du dépôt, n'écartait pas les deux dossiers de notes du côté habilité. Seuls des noms de fichiers ont été affichés, aucun d'un chemin cloisonné ; aucun contenu, aucune empreinte. Je n'en ai rien tiré ;
  - la partie 2 de la recherche de la session principale cite des chiffres de bancs publics. Je n'en reprends aucun dans le texte.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité ; rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucun fichier des deux dossiers de notes du côté habilité ; aucune réponse de l'essai de mesure ; aucun fichier de scores par unité ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense, aucun appel réseau. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.
