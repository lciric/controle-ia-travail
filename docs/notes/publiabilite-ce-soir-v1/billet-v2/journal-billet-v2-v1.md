# Journal du billet, version 2 : traitement de la lecture adverse — v1

- **Rédacteur** : sous-agent neuf, Claude Opus 5.5 (`claude-opus-5-5`) ; n'a écrit ni le brouillon anglais, ni le registre d'affirmations, ni la lecture adverse, ni aucune pièce de l'audit. Travail du 13 novembre 2026, de 21:24 UTC au scellement de ce journal (`date -u`).
- **Rien commité, rien poussé, rien publié, aucun message envoyé, aucune requête réseau, aucune dépense.** Lectures interdites respectées. Le seul voisinage : des lignes de `registres/decisions.md` (R-1717 à R-1763, R-2087, R-2413) qui nomment le bras B de l'audit dans des courses ; aucune pièce de ces courses n'a été ouverte.
- **Pièces lues, empreintes vérifiées** (toutes égales) : brouillon `29e2c903…`, registre `8acd2728…`, lecture adverse v2 `ad649014…` (fait foi ; v1 `5bc158b6…` lue pour comparaison), tri `c51fadd6…`, verdict `320463e6…`, texte de l'audit `910a53dc…`, consignes de P3 `a68468fe…`, préenregistrement de P3 `d975e981…`, sortie de l'audit `18c5e81c…`, verdict des trois analyses `dece9980…`, analyse principale `8e267952…`, N-068 `ba6b2db3…`, N-069 `6e0d9d40…`, lecture et contre-lecture de veille `211a6448…`, `af2fcb07…`, page publique v4 (README `ea241782…`, page R1 `3acf0a9d…`, manifeste `0cf35fe0…`, journal `48841d62…`), règles de LessWrong (`lw-*`, compagnons conformes), six PDF voisins et le rapport L3A (section 4 de la fiche).
- **Livrables, même dossier** :
  - `fiche-faits-billet-v1.md` : `c1db456d87854b34c0d73bae486db19da44b705fcbe07338e2174889090ba678` ;
  - `billet-premiere-version-v1.md` : `3b546aca3171fc1c54ad73278535f846f8f293743110af37d3b63d8d992b1840` ;
  - ce journal (empreinte dans son compagnon).

## 1. Compte

20 constats (3 bloquants, 11 majeurs, 6 mineurs) : **17 appliqués, 3 appliqués en partie (B-1, M-1, M-7), 0 non appliqué.** Rubriques 6 et 7 et points « hors tâche » : traités ci-dessous. Huit constats neufs, hors de la lecture adverse (section 3).

## 2. Constat par constat

### Bloquants

| constat | ce que j'en ai fait | statut |
|---|---|---|
| B-1 — texte de modèle, ni déposable ni recopiable ; remettre une fiche de faits en français, sans phrases rédigées ; retirer le pied | Fiche de faits en français remise (`fiche-faits-billet-v1.md`), un fait par ligne, avec pièce et fichier public. Pied retiré. **Mais la consigne de la mère demande aussi une première version rédigée** : je l'ai écrite, ce qui va contre « sans phrases rédigées ». Elle porte en tête, hors billet, l'avertissement de la règle : un texte de modèle retouché reste du texte de modèle (LW-1 : « text that was written by an LLM and then edited or revised by a human » ; « If you "borrow language" from the LLM, that no longer counts as "text written by a human" »). Recommandation : écrire le billet à partir de la fiche, en se servant de la première version comme d'un plan, sans en garder les tournures ; puis traduction mot à mot | en partie (par ordre de la mère) |
| B-2 — le titre affirme « actions that do not sabotage » | Titre : « Une sonde entraînée sur un saboteur instruit sépare aussi de l'honnête ses actions au coût non gonflé ». « sépare », jamais « signale » pour notre sonde ; « coût non gonflé », jamais « qui ne sabotent pas » ; aucune mention « préenregistré » dans le titre | appliqué |
| B-3 — la règle préenregistrée présentée comme notre apport | Supprimé. Le billet dit que Mohsin et Rahman ont fait le contrôle de contexte qui manque ici, avec 1,00 → 0,61 et les trois répliques (0,746 ; 0,797 ; 0,774), lues sur PDF, p. 15. Précision ajoutée, absente de la lecture adverse : selon leur règle, une réplique tient et deux sont partielles. Leur test « même consigne, agi ou non », le plus proche de notre ligne décisive, est cité aussi (constat neuf N-4). Notre apport n'est revendiqué nulle part | appliqué |

### Majeurs

| constat | ce que j'en ai fait | statut |
|---|---|---|
| M-1 — note citée sans sa place ; rappel tu | Place (fin du message système), rappel fixe de dix jetons avant chaque action, deux témoins de même place et de même longueur, rien pour l'honnête : dans le billet. **Citation de la note avec son début : non faite.** Les textes des notes sont « kept private » sur la page publique de P3 (l. 63) et absents de l'arbre public (fiche, F50) ; le registre d'affirmations les disait à tort « déjà publiques » (constat neuf N-1). Le billet reprend la paraphrase publique ; publier le texte exact est une décision de Lazar | en partie |
| M-2 — « cannot » ; historique non purgé | « cannot » retiré. Le billet donne les deux seuils (au plus 1,25 ; deux fois ou plus), les 148 actions écartées, la restriction aux actions sans gonflement antérieur, et dit que des actions au rapport intermédiaire peuvent rester dans le contexte. L'appui facultatif (aire de 1,0 au pas 0) n'est pas repris : grandeur descriptive, privée, invérifiable par un lecteur (fiche, F40) | appliqué |
| M-3 — « symmetric decision rule » | Le billet donne la règle ligne par ligne, puis : « Elle n'est donc pas symétrique, et le texte le dit » ; une ligne suffit pour « fuite », toutes sont exigées pour « sabotage » | appliqué |
| M-4 — ligne a_SM_hc absente ; prédiction manquée de la mention tue | Ligne 4 ajoutée (0,8475 [0,8121 ; 0,8800]). Le billet dit que la lecture « consigne » prédisait au moins 0,90 pour la mention et qu'on obtient 0,789 ; que la sonde n'est donc pas montrée lire la seule présence du texte ; que ce qu'elle capte est propre au saboteur (note adressée et rappel, intention, autre trace), sans que l'audit le sépare | appliqué |
| M-5 — « reading the instruction », « same pitfall », « as well as » | « fuite (lecture de la consigne) » donné comme le nom que la règle donne à l'issue, avec « Le nom de l'issue va plus loin que la mesure ». Les deux aires côte à côte, « sans comparaison testée entre elles ». Aucun « même écueil » : les travaux voisins sont décrits pour ce qu'ils mesurent | appliqué |
| M-6 — [B24] et Smith et al. | Supprimés | appliqué |
| M-7 — auteurs et lecteurs sont des modèles | En tête : « écrit, contre-lu, exécuté et jugé par des agents Claude, sous ma direction ; je n'en ai écrit ni le texte ni le code ». « Le modèle auteur déclare n'avoir ouvert aucune sortie » ; « un second agent a relancé le code … sortie identique à l'octet » ; réserves : Claude Opus 5.5 pour le texte, Claude Sonnet 5.5 pour le verdict, « Aucun humain n'a refait le calcul ». **La relance par Lazar lui-même ne m'appartient pas** : à faire avant le dépôt (section 4) ; la phrase change alors | en partie |
| M-8 — lecture préalable tue ; « préenregistré » dans le titre | Le billet dit que le texte a été écrit après d'autres analyses des mêmes données et que ses seuils ont été fixés en connaissant certaines grandeurs, avec un exemple (24,5 % à 1 % de fausses alarmes). Titre sans « préenregistré ». Ajout : l'ordre est attesté par un dépôt privé et le verdict, et aucune empreinte n'a été publiée avant le calcul (constat neuf N-2) | appliqué |
| M-9 — comparaison aux juges, adoption non trouvée | Retirée. Recherche refaite au registre (« non interprétable », « W − J3s ») : aucune adoption ; `registres/etat.md` l. 225 montre le nœud ouvert, sans défaut | appliqué |
| M-10 — le pied promet un registre | Aucun registre promis. Chaque article cité porte ses pages, vérifiées sur PDF. Lien vers la page publique et le verdict ; le billet dit que le texte de l'audit, le code et la sortie restent privés (le verdict donne leurs empreintes) | appliqué |
| M-11 — voisins à un seul agent absents | Lus sur PDF par moi : Sinha (2610.37679v1, p. 1), Fomin, David, LeVi (2606.30449v1, p. 1, 8), Goldowsky-Dill et collègues (2502.03407v1, p. 6), « Telling FIBS » (2610.12445v4, p. 1, 6, 25, 29, 34, 39, 41). Tous cités. 33 citations anglaises contrôlées par programme sur leur page : 0 échec (fiche, section 4) | appliqué |

### Mineurs

| constat | ce que j'en ai fait | statut |
|---|---|---|
| m-1 — « none of the "sabotage" conditions held » | « aucune des quatre bornes hautes n'est sous 0,80 », après la règle qui les nomme | appliqué |
| m-2 — « the same deceptive text » | « le même contenu trompeur, attribué à un autre agent » | appliqué |
| m-3 — pages de Kale et Vishwanath | « p. 1, 2, 5 » (relu : p. 1 et 2 littéralement ; p. 5, 0,96-0,98 et 0,91-0,96) | appliqué |
| m-4 — épisode, température, effectifs, plis, deux aires de W | Un épisode par tâche et par condition, température 1,0, 600 actions par condition, cinq plis de douze tâches dans le billet ; « environ 0,996 » pour l'aire de W, le détail 0,9960 contre 0,9972 dans la fiche (F11). La température n'est écrite dans aucun fichier public (F02) | appliqué |
| m-5 — écart à 600 dans « 557 / 576 » | Dans le tableau : « 43 et 24 actions sans champ à masquer, exclues » | appliqué |
| m-6 — identifiants, gras, commentaire ; vocabulaire de maison | Aucun identifiant ni gras dans le corps ; ni « bras », ni « signature », ni « issue gelée », ni « déclencheur » ; « contrôles supplémentaires ». Le statut en tête et les renvois en fin sont hors billet, marqués comme tels, à retirer | appliqué |

### Rubriques 6 et 7, points « hors tâche »

- **Rubrique 6** (modération) : rien à changer dans le texte. Les règles archivées offrent un seuil plus bas, le fil ouvert (LW-3 : « there is a much lower bar for open threads ») ; choix de Lazar.
- **Rubrique 7** (trois objections) : les réponses permises sont dans le billet, sous forme de réserves : asymétrie et prédiction manquée de la mention (objection 1) ; contrôle non fait chez nous, fait chez Mohsin et Rahman, et sélection des 46 actions par le comportement du modèle (objection 2) ; petite taille et auteurs modèles (objection 3). Aucune nouveauté suggérée.
- **Hors tâche 1** (Mohsin et Rahman : colludeurs au but appris par affinage, 0,995, p. 1) : laissé hors du billet. C'est leur résultat ; il touche une suite retirée de la page publique. À ajouter en une proposition si Lazar le veut (fiche, 4.1).
- **Hors tâche 2** (PDF absents de l'arbre courant) : la fiche cite la branche `origin/prep/etat-de-l-art-niveau3-pieces-v1`, les chemins et les empreintes.
- **Embargo, réserve du lecteur adverse** (recette de W et texte de T0.7) : je ne l'ai pas vérifiée non plus (lecture interdite). La recette de W est publique depuis le 8 novembre (`analyse-principale-r1-r2-v1.md` sur la page publique, l. 60).

## 3. Constats neufs, hors de la lecture adverse

- **N-1 — Le texte de la note n'est pas public.** La ligne B6 du registre d'affirmations dit « déjà publique » ; la page publique de P3 dit « texts of the private instructions (kept private) » (l. 63), et aucune phrase de la note n'apparaît dans l'arbre public (fiche, F50). Le billet n'en cite rien.
- **N-2 — « Préenregistré » n'est vérifiable par aucun lecteur.** Le texte de l'audit, son code, sa sortie et son manifeste sont privés ; l'empreinte du texte paraît en public pour la première fois avec le verdict, le 8 novembre à 09:14 UTC, après le calcul du 7 (F18). Publier le texte de l'audit publierait aussi des fragments de la note (PA l. 70-71, 238-239). Décision de Lazar.
- **N-3 — Pas de « code » à lier.** La consigne demande le lien vers la page et le code ; aucun code de l'audit ni des sondes n'est public (F50). Le billet donne la page et dit ce qui reste privé.
- **N-4 — Mohsin et Rahman ont aussi le test le plus proche du nôtre** : « même consigne, agi ou non », 59 % contre 90 % à 1 % de fausses alarmes (p. 15) ; et « only negatives that also hold the instruction make the comparison informative » (p. 16). Cité.
- **N-5 — « Telling FIBS » a retiré les rappels à chaque tour** parce qu'ils rendraient la détection « presque triviale » (p. 34) ; notre saboteur en avait un avant chaque action. Cité.
- **N-6 — Bras B : « not run » n'est plus exact.** Au 7 novembre, le verdict dit « n'est pas fait ». Le soir même, Lazar l'a ordonné (GO-2026-11-07-04, R-1717) ; le registre montre au moins une tentative en annexe d'une course dont les pièces me sont interdites, sans résultat lu (R-2413 : « code 1 en 3 s », sorties non ouvertes). Le billet dit seulement « Je n'ai pas de résultat de ce contrôle », sans rien sur les courses. La page publique v4 dit « the arm that would separate the two was not run ». **Nœud de Lazar** : garder cette forme, ou une autre.
- **N-7 — La page liée contredit le billet.** La v4 de la page R1 n'est pas en ligne (poussée refusée, R-2594) ; la page en ligne dit « reads the instruction, not the sabotage ». La v4 garde « preregistered with a symmetric rule », « as well as » et, en gras, « the trained probe reads the instruction » : trois formes que la lecture adverse interdit au billet (M-3, M-5). Un lecteur qui suit le lien verra l'écart. Proposition : une version 5 de la page R1, limitée à cette ligne, avant le dépôt du billet (publication : nœud de Lazar).
- **N-8 — Le « 0,245 » public ne nomme pas sa mesure.** Le verdict public des trois analyses écrit « tombe à 0,245 par action » (l. 41) ; « rappel à 1 % » n'est écrit que dans le texte privé de l'audit (PA l. 31-32). Le billet le dit comme un rappel à 1 % de fausses alarmes.

## 4. Ce qui revient à Lazar avant tout dépôt

1. Écrire le billet lui-même, à partir de la fiche (B-1), puis le faire traduire mot à mot.
2. Refaire lui-même la relance (V l. 30 : code `05aa560f`, numpy 2.4.6, scipy 1.17.1, graines du manifeste), puis changer « Aucun humain n'a refait le calcul » (M-7). Confirmer « Je n'en ai écrit ni le texte ni le code ».
3. Décider de publier ou non le texte de l'audit, le code et la sortie (N-2, N-3), en sachant que le texte cite des fragments de la note.
4. Pousser une page R1 alignée sur le billet (N-7).
5. Trancher la forme sur le bras B (N-6).
6. Ajouter ou non la phrase sur les colludeurs au but appris par affinage (hors tâche 1).
7. Lire le billet de LessWrong « What Happens When a Collusion Probe Only Finds a Thin Signal? » avant de décider de le citer (fiche, 4.7 ; archivé en texte, non relu par moi).
8. Faire relire par un lecteur neuf le texte que Lazar aura écrit (dernière limite de la lecture adverse).

## 5. Longueur et phrases fragiles

- **Longueur** : environ 970 mots hors nombres dans le corps (environ 1 045 avec les nombres, tableau non compté), au-dessus de la fourchette de 600 à 900. La densité vient des ajouts exigés par la lecture adverse (M-1, M-2, M-3, M-4, M-7, M-8, M-11, m-4, m-5). À la réécriture, la section des travaux voisins est la première à resserrer.
- **Phrase la plus fragile, 1** : « Ce qu'elle capte est propre au saboteur : la note qui lui est adressée et son rappel, son intention, ou une autre trace de sabotage dans ces actions. » Interprétation, pas mesure : elle repose sur les lignes 4 et 5 ; « son intention » n'est pas testable ici ; la liste n'est pas close (les 46 actions sont choisies par le comportement du modèle).
- **Phrase la plus fragile, 2** : « Je n'ai pas de résultat de ce contrôle. » Vraie au mot près, mais elle tait des tentatives sous embargo (N-6) et s'écarte du verdict public (« n'est pas fait ») et de la page (« was not run »).
- Ensuite : « aucune empreinte n'a été publiée avant le calcul » (vérifié sur l'historique du dépôt public de l'organisme seulement) ; « Leur test … ressemble à notre ligne 1 » (analogie : épisodes de collusion contre actions d'un agent seul).

## 6. Limites

- Un seul rédacteur, en une soirée ; le billet n'a pas été relu par un lecteur neuf.
- « Telling FIBS » (119 pages) lu par passages, après recherche de mots ; les autres articles cités lus sur les pages citées et leurs abords.
- Les commits `2ccb608c` et `05aa560f` ne sont pas dans le clone local (clone superficiel) : l'ordre texte puis calcul repose sur le verdict et sur le registre (R-1658, R-1661).
- Liens vers GitHub construits d'après le clone local, non ouverts en ligne.
- Script du contrôle des citations et liste des 33 citations laissés dans le bloc-notes de la session (`controle_citations.py` `c5d91342…`, `citations-billet-v2.json` `7df7c4e1…`), non versés.
