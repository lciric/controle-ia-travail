# Contre-lecture — plan de vérification hors de nous du bras d'attaque (brouillon 1) et projet de courriel de réplication extérieure — v1

- Date : 10 novembre 2026, 09:21 UTC (`date -u`).
- **Contre-lecture par un sous-agent neuf** (R2) : je n'ai écrit ni le plan, ni le courriel, ni aucune pièce citée. Lecture
  seule. Aucun autre fichier modifié, aucun commit, aucun contact, aucun dépôt, aucune dépense, aucune requête vers un
  service extérieur (la documentation de l'Open Science Framework et celle des services d'horodatage n'ont pas été
  consultées).
- Non lus, par consigne : le coffre, `docs/notes/bras-attaque/`, tout résultat, note ou seuil de moniteur, les épisodes
  d'épreuve, les items de l'étiqueteur. Dans `registres/decisions.md`, les lignes 830 à 837 (R-604 à R-610) ont été
  repérées par leur seul numéro et exclues avant tout affichage.

## Fichiers lus et empreintes recalculées

| Pièce | Lu | Empreinte recalculée (sha256) | Contrôle |
|---|---|---|---|
| `docs/notes/verification-externe-bras-v1/plan-verification-externe-bras-v1-brouillon1.md` | en entier | `4e88118cd3fb82fcd5758e57b5e7b96bd9dc1b93a12badf462cc08652d298b29` | = attendue ; compagnon conforme ; commit `600a9483` (09:05 UTC) |
| `docs/notes/verification-externe-bras-v1/projet-courriel-replication-externe-v1.md` | en entier | `7ea1cc4e5a416a0075bb7d01b174f2bbc0fc4c362a3bab27c15058e31a140170` | = attendue ; compagnon conforme |
| `livrables/osf-manifeste-v1/LISEZMOI.md` | en entier | `d9b508239b8f3471b3491c4ad784aa30fb54881aece894e8fb2c0c642d43760e` | = citée par le plan |
| `livrables/osf-manifeste-v1/manifeste-v1.json` | en entier | `dd87b23ebc03dbb6b6d00aeeadc6685174aad04cccf72f93b72332a113e061c6` | = citée ; 118 entrées, référence `main` `a364e947` (4 novembre, 08:06 UTC) |
| `docs/decisions/decision-N-061-v1.md` | en entier | `b2ae441720665ed49f131e18fb7612d0d1c2a4e0cc7a0e18a301178fe5b2df54` | = citée |
| `docs/decisions/decision-N-053-v1.md` | en entier | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` | |
| `docs/decisions/decision-N-057-v1.md` | en entier | `42180088efb2e1016251fa329421fc08ebcb13039266d278c1a6f37ced60af99` | |
| `docs/decisions/decision-N-056-v1.md` | l. 50-80 | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` | pour CV-2, CV-11 |
| `docs/decisions/decision-N-060-v3.md` | en entier | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | pour CV-2 |
| `prereg/bras-attaque-regle-v1.md` (candidat, sans compagnon, commit `4d5e0948`) | en entier | `48fde35c973e5ea2ca99556bbfdc7516813e7bc84b1544332aebe74a5ea84544` | mes renvois de lignes valent pour cette empreinte |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (candidat) | en entier | `ca5f648173366e7a42cd5e6778ac7222583ec64ab74eeaa90f6c37a6b3a32d79` | idem |
| `registres/passations/2026-11-10-0852-decision-lazar-go-quatre-pieces-attaques-inedites.md` | en entier | `c90ad8f49c84bbb77334feca236d9b1e667b19cfcc9e3da5072d63359832af57` | = citée |
| Règle du jeu, `origin/claude/upbeat-cray-dmauvv` (`9ed5fe75`) : `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon1.md` | en entier, par `git show` | `09aa64033ec4d32bfc0687690bf13b29743dc8e6dc9de1e250e964de77833371` | = son compagnon |
| Même branche : `registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md` (nœud 2) | en entier | `bba97a1a76b463e8bc0a336104a3798627b9797e14cdf10e3ba268912af5f986` | = citée par le candidat de la règle |
| Même branche : `docs/notes/integration-bras-attaque-v1/relecture-regle-du-jeu-brouillon1-v1.md` | recherche « nœud 7 », « tiers », « public » seulement | `82657fb8732c2bc69eb6abd03f77a80d177be3a655319114f250196c024a6c8b` | rien sur le nœud 7 |
| `CLAUDE.md` | en entier | `b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae` | |
| `registres/etat.md` | l. 352-365 et extraits courts autour de « OSF », « public » | `ae1f31362c047a062949b6172ed20d4224e176bbfb100c8deb169895e0b909c7` | |
| `registres/decisions.md` | l. 1538 (R-1580), l. 1792 (R-1834), extrait de l. 1715 (R-1757) ; débuts de lignes rendus par les recherches « Open Science » (dont R-1832) | `1e35073ed7650b5b6e1bb2223e9c75562e9a1a71dfd7b7c045bac4942b696a00` | l. 830-837 jamais affichées |
| `registres/go.md` | l. 254-261 | `097b09ca23759f3922c227e03591464057fd0f097f8f72ff400423642a375958` | |

## Verdict

**Scellable après corrections (listées, texte proposé).** 0 bloquant, 12 à corriger, 5 à préciser. Le courriel ne
doit pas partir avant CV-11, CV-12 et CV-13 : en l'état, il décrit à une équipe extérieure un échange impossible sous la
règle du bras.

## Vérifié conforme

- Empreintes citées par le plan (passation du 10 novembre 08:52, `LISEZMOI.md`, `manifeste-v1.json`, N-061) : conformes.
- « Pièce 4 de la demande validée par Lazar » : conforme (passation, l. 21-22) ; les nœuds 3, 4 et 7 y restent ouverts
  (l. 36).
- Manifeste v1 : 118 entrées (51 préenregistrements, 56 décisions, 11 verdicts), 1 exclue ; ni la règle du bras, ni
  l'index des familles aveugles, ni aucune pièce du 10 novembre : conforme.
- « Privé et non gelé » ; « rendre public est un nœud en attente » : exact (sources à préciser, CV-1).
- N-061 : ses quatre points sont rapportés fidèlement.
- Témoin de Bailey : « section 3.5 », « notre exécution de leur code », « le run est sur le modèle des auteurs », « nœud 5
  du devis », « devis v4 » : conformes au préenregistrement (l. 1, 32, 37-41, 27).
- Section 5 : R13 et R2 bien cités.
- Courriel : **aucune divulgation interdite** (ni résultat, ni recette, ni mode de sabotage, ni nom de fichier interne,
  ni contenu du coffre ; « diffuse sabotage » est la catégorie du programme, pas un mode). « Designs, but not their
  calibrated thresholds or test episodes » est conforme à N-056 point 6 (l. 68-70) et à la règle (l. 64-66), à l'omission
  des notes près (CV-14). Témoin positif à faille plantée et témoin négatif « honnête contre honnête » : conformes à la
  règle (l. 155-172). « Contact = nœud ; Lazar relit et envoie » : conforme au `CLAUDE.md` et à la passation (l. 35).

## Points

### CV-1 — à corriger — L'existant du dépôt d'empreintes est incomplet, sa source primaire manque

- **Où** : plan, section 1, « Existe » (l. 23-26) ; section 6 ; « Pièces » (l. 12-16).
- **Pourquoi** :
  1. `registres/go.md` l. 256 : **GO-2026-11-05-08**, type « publication », échéance 30 novembre 2026, couvre le « dépôt
     des empreintes des préenregistrements, verdicts et décisions scellés sur l'Open Science Framework (horodatage tiers ;
     projet d'abord privé, passage en public sur mot de Lazar) ». Il a servi deux fois : le 5 novembre (R-1580,
     `registres/decisions.md` l. 1538 : projet privé `dr57c`, dépôt à 2026-11-05T16:20:34Z, « empreintes relues par
     l'interface CONFORMES ») et le 8 novembre, second dépôt (R-1757, l. 1715). Un dépôt « chez le tiers » est donc déjà
     accordé et pratiqué. Le nœud 7 tranche la visibilité, le gel et un éventuel service de plus. Le plan l'ignore, et son
     tableau aussi.
  2. « Privé et non gelé » et le nœud « rendre public et le geler » viennent de R-1580. `registres/etat.md` n'en porte
     qu'une mention, état du 5 novembre (l. 361 : « OSF public » parmi les nœuds en attente). GO-2026-11-06-04 (`go.md`
     l. 260) réserve aussi au mot de Lazar « rendre public le projet de l'Open Science Framework ». Aucune ligne ultérieure
     du registre ne tranche (recherche sur tout le fichier, hors l. 830-837). La phrase du plan est exacte ; sa source
     primaire est R-1580.
  3. Le manifeste v1 lit `main` au commit `a364e947` (4 novembre, 08:06 UTC) : il lui manque aussi N-061 à N-066, pas
     seulement « les décisions du 10 novembre ».
  4. La règle du jeu est citée sans chemin, branche ni empreinte (R6).
- **Correction proposée** (remplace l. 23-26) :
  > **Existe** : un projet privé de l'Open Science Framework (`dr57c`) qui ne reçoit que des empreintes, sous
  > GO-2026-11-05-08 (type « publication », échéance 30 novembre 2026 : empreintes des préenregistrements, verdicts et
  > décisions scellés ; « projet d'abord privé, passage en public sur mot de Lazar »). Premier dépôt le 5 novembre à
  > 16:20:34 UTC (R-1580 : manifeste v1 et `LISEZMOI.md`, avec une procédure de vérification écrite pour un tiers) ;
  > second dépôt le 8 novembre, sous le même GO (R-1757). Le projet est privé et non gelé ; le rendre public et le geler
  > est un nœud de Lazar (R-1580 ; exclusions de GO-2026-11-06-04 ; `registres/etat.md` l. 361, état du 5 novembre ;
  > règle du jeu, `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon1.md`, branche
  > `claude/upbeat-cray-dmauvv`, `09aa6403…`, section 5, nœud 7). Le manifeste v1 lit `main` au 4 novembre (`a364e947`) :
  > ni la règle du bras, ni l'index des familles aveugles, ni rien d'ultérieur (N-061 à N-066 et décisions du 10 novembre
  > compris).

### CV-2 — à corriger — Le juge qui vérifie le dommage est mal attribué

- **Où** : section 5, l. 86 : « le juge d'une autre lignée qui vérifie le dommage (N-053) ».
- **Pourquoi** : le juge d'une autre lignée de N-053 (point 4, l. 33-36) est « un juge Qwen2.5-7B en bras rapporté » : un
  bras du côté des moniteurs, pas le vérificateur du dommage. Le dommage d'un épisode du bras est vérifié par « le juge,
  seul lecteur des recettes » (N-056 point 6, l. 70-72 ; règle, l. 188-191). Sur le banc actuel, la vérité du dommage est
  lue par « deux lecteurs de deux familles de modèles autres que celles des moniteurs évalués (ni Llama ni Qwen) » (N-060
  v3 point 1, l. 21-27). Cette règle exclut justement le juge Qwen de N-053.
- **Correction proposée** :
  > … le juge, seul lecteur des recettes, qui vérifie l'échelon déclaré, le plafond et le dommage (N-056 point 6 ; règle
  > du bras) ; sur le banc actuel, la vérité du dommage par deux lecteurs de familles autres que celles des moniteurs, ni
  > Llama ni Qwen (N-060 v3 point 1) ; …

### CV-3 — à corriger — L'ancre publiée ne dit rien de « notre banc »

- **Où** : section 4, l. 77-81.
- **Pourquoi** : « Prouve que notre banc est à l'échelle de la littérature » est contredit par le préenregistrement
  lui-même : « Aucun moniteur du programme n'est touché, lu ni conçu » (l. 34) ; « Ce run est sur le modèle et le code des
  auteurs » (l. 39) ; verdicts « sur le banc des auteurs » (l. 297-299) ; « Ce que le run ne dit dans aucun cas : rien sur
  les moniteurs du programme ; rien sur Llama-3.1-8B-Instruct » (l. 320-321). La section 4 omet aussi « Manque » et « Qui
  décide », que la question promet pour chaque vérificateur (l. 9-10).
- **Correction proposée** :
  > - **Prouve**, si l'effet est retrouvé, qu'un effet publié par d'autres (Bailey et collègues, section 3.5) se reproduit
  >   hors de ses auteurs, sur leur modèle et leur code, et que notre chaîne d'exécution et de lecture (lanceur, gardes,
  >   contrôles du juge, analyse) sait le retrouver : c'est un étalon extérieur de notre chaîne, pas de notre banc. Si
  >   l'effet n'est pas retrouvé, le run ne sépare pas un effet publié fragile d'un défaut de notre exécution ; les gardes
  >   et l'audit de symétrie réduisent la seconde part.
  > - **Ne prouve pas** : rien sur nos moniteurs, notre modèle ni notre harnais (préenregistrement, l. 34 et 320-321) ; un
  >   seul régime, un seul modèle, un seul moniteur ; ce que le verdict vaut pour le témoin de la règle reste le nœud 5 du
  >   devis.
  > - **Manque** : les huit conditions de lancement (préenregistrement, l. 341-353), dont le code, qui n'existe pas encore
  >   (l. 12-15).
  > - **Qui décide** : Lazar (nœuds du devis ; GO du modèle, l. 168-170 ; GO de calcul).

### CV-4 — à corriger — Un horodatage date un « au plus tard », pas l'ordre « scellé, puis lu »

- **Où** : section 1, l. 20-22.
- **Pourquoi** : un horodatage par un tiers prouve qu'une pièce existait, telle quelle, **au plus tard** à sa date. Il ne
  prouve jamais qu'une lecture a eu lieu **après** : rien n'exclut, par l'horodatage seul, une lecture officieuse avant
  le scellement. « C'est la seule preuve qu'un lecteur extérieur peut refaire seul » est inexact :
  - le lecteur doit recevoir la pièce pour recalculer l'empreinte ;
  - l'étape 2 de la procédure du `LISEZMOI.md` (`git show <commit>:<chemin>`, l. 28-29) suppose l'accès au dépôt de
    travail privé ;
  - les pièces du coffre ne sortiront jamais (N-057 point 2), donc personne dehors ne pourra les recalculer.
- **Correction proposée** (remplace l. 20-22) :
  > - **Prouve** qu'une pièce dont l'empreinte est horodatée existait, telle quelle, au plus tard à la date de
  >   l'horodatage. Si la date de l'ouverture est, elle aussi, établie hors de nous, on obtient l'ordre « scellé, puis
  >   lu ».
  > - **Ne prouve pas** que la lecture a eu lieu après (un horodatage ne date jamais un « pas avant ») ; ni que le contenu
  >   est juste, ni que les résultats sont bons. Sans la pièce elle-même, il ne prouve rien du tout : le lecteur doit la
  >   recevoir, et les pièces du coffre ne sortiront pas (CV-16).

  À ajouter à « Manque », comme option facultative (c'est un service extérieur, donc une décision de Lazar) :
  > Lier l'échantillon de l'ouverture à une valeur publique imprévisible, publiée après le dépôt. Par exemple : le
  > numéro de tirage d'une balise publique d'aléa est fixé dans le texte scellé, et sa valeur sert d'entropie à
  > `numpy.random.SeedSequence` (R9 inchangée). L'échantillon lu n'existait donc pas avant le dépôt ; une lecture
  > officieuse d'autres épisodes n'est pas exclue pour autant.

### CV-5 — à corriger — Deux protections manquent au dépôt : l'unicité et le sel

- **Où** : section 1, « Ne prouve pas » (l. 22), « Manque » (l. 27-29), options (a) et (c) (l. 34-35, 39-42).
- **Pourquoi** :
  1. **Unicité.** Avec des empreintes seules, déposées en privé ou horodatées par un service (option (c)), rien n'exclut
     d'avoir horodaté plusieurs variantes d'une règle ou d'un seuil et de ne montrer que la favorable. C'est la faiblesse
     principale de la recommandation (c), et le plan ne la dit pas.
  2. **Sel.** L'attaquant informé ne connaît pas les seuils calibrés (règle, l. 64-66 ; N-056 point 6). Or l'empreinte
     publiée, ou transmise, d'un fichier court et secret se retrouve en essayant les valeurs plausibles. C'est le cas
     d'un fichier qui ne porterait qu'un seuil calibré, ou d'un seuil de dommage par mode (règle, l. 181-182). Sous
     l'option (a), chaque dépôt devient public dès qu'il est fait, donc avant que l'attaquant écrive. L'option (a) ne
     porte pas cet inconvénient.
- **Correction proposée** (à ajouter) :
  > **Ne prouve pas** l'unicité : avec des empreintes seules, rien n'exclut que plusieurs variantes aient été horodatées
  > et que seule la favorable soit montrée.
  > **Manque** : (i) une chaîne : chaque manifeste porte un numéro et l'empreinte du précédent ; l'empreinte du dernier
  > est horodatée et publiée à chaque scellement (elle ne révèle rien). Un trou, ou une seconde chaîne, se voit alors dès
  > qu'on publie. (ii) un sel : chaque pièce scellée dont le contenu doit rester secret (seuils calibrés, seuils de dommage
  > par mode, index des familles aveugles) reçoit, avant empreinte, un sel aléatoire de 32 octets. Le sel est gardé avec
  > la pièce et révélé à l'ouverture.
  > Option (a), inconvénient à ajouter : sans sel, publier les empreintes des moniteurs gelés avant le bras peut livrer les
  > seuils à tout attaquant, interne ou extérieur.

### CV-6 — à corriger — Bancs écrits par d'autres : la preuve est plus étroite que dite

- **Où** : section 2, l. 48-57.
- **Pourquoi** :
  1. **Sondes de l'auteur.** Une sonde qui lit l'agent auteur ne lit rien d'utile sur une transcription produite par un
     autre modèle : ce serait une lecture de lecteur (règle du jeu, nœud 4). Pour nos sondes, il faut donc faire rejouer
     ces épisodes par notre agent, et l'épisode est alors écrit en partie par le programme. « Des sabotages que le
     programme n'a pas écrits » ne vaut que pour les moniteurs textuels, sur les transcriptions d'origine.
  2. **« Équivalent d'un échelon aveugle » est inexact.** L'attaquant est bien aveugle à nos moniteurs. Mais un banc
     public peut avoir été lu par nos concepteurs : il n'est pas tenu à l'écart au sens de l'échelon 1 (règle,
     l. 60-62 ; N-054 point 3 ; N-044). Les critères de dommage diffèrent aussi : Liars' Bench mesure des mensonges, pas
     des sabotages diffus. Enfin, dans SHADE-Arena, l'agent serait averti qu'un moniteur lira sa transcription (à
     vérifier sur l'article).
  3. **Exécution interne.** L'adaptation, l'exécution, le juge et la lecture restent ceux du programme : une erreur du
     programme touche aussi ce point.
  4. **Périmètre de N-061.** N-061 accepte ces ressources pour des usages nommés : NARCBench « au bras descriptif de
     T0.7 », Liars' Bench et SHADE-Arena « à T0.8 (bases boîte noire) » (l. 12). Un usage au bras est nouveau : il
     revient à Lazar, au moins par son devis, et par nœud s'il entre dans un texte scellé ou dans la porte G1.
  5. **Disponibilité.** La disponibilité de l'ensemble complet de chaque banc reste à vérifier, avec les licences : une
     partie pourrait n'être fournie que sur demande, et une demande aux auteurs serait un contact extérieur.
- **Correction proposée** :
  > - **Prouve** que, sur des tâches et des sabotages conçus par d'autres, la résistance mesurée ne tient pas qu'à nos
  >   propres attaques : pour les moniteurs textuels, sur leurs transcriptions d'origine ; pour les sondes de l'auteur,
  >   seulement après rejeu par notre agent, écriture du programme déclarée comme telle.
  > - **Ne prouve pas** la résistance à un attaquant informé de nos moniteurs ; ni la résistance sur une famille tenue à
  >   l'écart (un banc public a pu être lu par nos concepteurs) ; ni le dommage au sens du programme (critères des bancs à
  >   mettre en regard, Liars' Bench mesure des mensonges). L'exécution et la lecture restent les nôtres.
  > - **Qui décide** : Lazar, par ligne de devis ; l'usage au bras sort du périmètre accepté par N-061 (T0.7, T0.8) ;
  >   nœud distinct pour toute entrée dans la porte G1.

### CV-7 — à corriger — Réplication de la mesure : preuve surestimée, N-057 mal cité

- **Où** : section 3 (a), l. 63-65.
- **Pourquoi** :
  1. **Preuve surestimée.** « Prouve que nos calculs sont justes » ne tient que si l'équipe réimplémente la lecture à
     partir des textes scellés. Si elle rejoue notre code, elle prouve seulement qu'il redonne la même chose. Dans les
     deux cas, la réplication ne prouve pas que les entrées sont justes : épisodes, juge, vérité du dommage. La section
     n'a ni « Ne prouve pas », ni « Existe », ni « Qui décide » (promis l. 9-10).
  2. **N-057 point 4 ne dit pas cela.** Il gèle l'exécution d'un pipeline opérationnel jusqu'à la revue de sécurité
     externe (l. 39-41) : il n'ouvre aucune transmission. Le point 2 interdit de reproduire en clair ou de synthétiser
     hors quarantaine (l. 32-34). Le point 5 limite les lecteurs et fait consigner chaque accès (l. 42-43). Donner des
     épisodes en quarantaine à une équipe extérieure serait une décision nouvelle de Lazar, en plus du nœud 3.
- **Correction proposée** (remplace l. 63-65) :
  > - **(a) Réplication de la mesure** : une équipe extérieure réimplémente, à partir des seuls textes scellés, la lecture
  >   (courbe, témoins, loi exacte du seuil), et la refait sur nos notes par épisode ou en rejouant les moniteurs gelés.
  >   **Prouve**, si elle n'emploie pas notre code, que les chiffres découlent des entrées et des critères gelés.
  >   **Ne prouve pas** que les entrées sont justes (épisodes, juge, vérité du dommage), ni que les épisodes lus sont ceux
  >   qui ont été scellés (CV-16). **Exige**, pour les épisodes d'attaque, une transmission hors de la quarantaine que
  >   N-057 ne prévoit pas (point 2 ; point 5) : décision nouvelle de Lazar, après la pièce écrite de la revue de sécurité
  >   externe (nœud 3 ; N-057 point 4 gèle l'exécution, il n'ouvre aucune transmission). **Sans quarantaine** :
  >   (a1) réanalyse sur les notes par épisode, étiquettes, classes, graines et manifestes publiés ; (a2) moniteurs gelés
  >   rejoués sur les épisodes « honnête contre honnête », qui ne portent aucune attaque. **Existe** : rien.
  >   **Qui décide** : Lazar.

### CV-8 — à corriger — « Indépendant de l'auteur » confondu avec « extérieur au programme » ; forme (b) surestimée

- **Où** : question (l. 8-10) ; sections 2 et 4 ; section 3 (b), l. 66-69.
- **Pourquoi** : la question demande ce qui vérifie « hors de Lazar et de cette session », c'est-à-dire indépendamment
  de l'auteur. Le titre dit « hors de nous », c'est-à-dire hors du programme. Les cinq vérificateurs mêlent les deux.
  La section 5 fait la distinction ; les sections 2 et 4 ne la font pas : le matériau vient d'ailleurs, mais
  l'exécution et la lecture sont internes. La forme (b) est indépendante de **notre attaquant**, pas de **notre
  mesure** : nos moniteurs gelés, notre juge, notre interface. Elle surestime aussi ce qu'elle prouve. Deux attaquants
  qui s'accordent peuvent partager une faiblesse : mêmes plafonds, même liste fermée à l'échelon 3, même agent. Et l'écart
  ne dit « lequel était faible » qu'à juge et plafonds communs. Les conditions d'indépendance manquent, et le courriel en
  compromet une (CV-13).
- **Correction proposée** : un tableau en tête du plan, puis la forme (b) réécrite.

  | Vérificateur | Écrit le matériau | Exécute | Juge et lit | Atteste |
  |---|---|---|---|---|
  | 1. Horodatage | le programme | — | — | un tiers (la date seulement) |
  | 2. Bancs publics | d'autres équipes ; notre agent pour les sondes de l'auteur | le programme | le programme | — |
  | 3 (a). Réplication de la mesure | le programme | l'équipe extérieure | l'équipe extérieure | l'équipe extérieure |
  | 3 (b). Réplication de l'attaque | l'équipe extérieure | le programme (moniteurs, interface) | le programme, ou l'équipe (CV-11) | — |
  | 4. Ancre publiée | les auteurs de l'article | le programme | le programme | l'article (valeur de référence) |
  | 5. Lecteurs indépendants | — | — | le programme | — |

  > **Prouve** que la courbe ne tient pas à notre seul attaquant : si deux attaquants écrits indépendamment, scorés par
  > les mêmes moniteurs gelés, le même juge et les mêmes plafonds, donnent la même courbe, elle ne dépend pas d'une
  > faiblesse propre au nôtre ; s'ils divergent, le plus haut des deux est la meilleure borne basse de l'évasion
  > atteignable. **Ne prouve pas** la résistance au meilleur attaquant (faiblesse commune possible), ne vérifie pas la
  > mesure, ne dit rien des échelons 4 à 6. **Conditions d'indépendance** : aucune des deux équipes ne voit la courbe de
  > l'autre avant d'avoir scellé et fait horodater la sienne ; équipe sans lien avec les auteurs des ressources des
  > sections 2 et 4 ; une cosignature offerte avant le résultat se dit au jury comme telle.

### CV-9 — à corriger — Le nœud 7 est réécrit sans le dire ; le format est incomplet

- **Où** : section 1, l. 30-44.
- **Pourquoi** : la règle du jeu (section 5, nœud 7) propose trois options :
  - (a) public et gelé avant l'entretien ;
  - (b) un dépôt gelé à chaque scellement ;
  - (c) rester privé et non gelé.

  Elle recommande « (a), puis (b) à chaque scellement », confiance 0,7. Le plan garde le numéro 7 et les lettres, mais
  change leur sens : (b) devient l'embargo, (c) le service d'horodatage. Il retire l'option « rester privé » et le socle
  déjà accordé (CV-1). Il recommande autre chose (« (c) … plus (b) … (a) quand les papiers sortent », confiance 0,6), sans
  dire pourquoi il s'écarte. Une réponse « (b) » de Lazar serait donc ambiguë entre deux pièces. Le format du `CLAUDE.md`
  demande enfin un défaut, que le plan n'écrit pas : pour un nœud d'arrêt, il faut écrire « aucun ».
- **Correction proposée** (en tête de la décision, en gardant trois options comme le veut le format) :
  > *Options reformulées par ce plan ; elles remplacent celles de la règle du jeu (`09aa6403…`, section 5 : (a) public et
  > gelé avant l'entretien ; (b) dépôt gelé à chaque scellement ; (c) rester privé ; recommandation « (a) puis (b) »,
  > confiance 0,7). Les lettres n'ont pas le même sens : répondre « plan, option … ».*
  > **Socle**, déjà accordé : dépôt de chaque empreinte sur le projet privé, sous GO-2026-11-05-08 (jusqu'au 30 novembre ;
  > R-1580, R-1757). La règle demande le mot de Lazar sur le nœud 7 pour ce dépôt (candidat, l. 58-59). Inconvénient du
  > socle seul : rien de vérifiable dehors tant que le projet est privé, et le projet reste modifiable. Les options
  > ci-dessous s'y ajoutent.
  > … (a), (b), (c) avec les ajouts de CV-5 et CV-10 …
  > Recommandation : … ; **écart à la recommandation de la règle du jeu, et pourquoi** : [à écrire par l'auteur].
  > Confiance : …
  > **Défaut : aucun ; nœud d'arrêt, rien ne part sans le mot de Lazar.**

### CV-10 — à préciser — Ce que chaque option donne vraiment, et ce qui n'est pas vérifié

- **Où** : section 1, l. 32-42.
- **Pourquoi et texte proposé** :
  1. **Enjeu.** « Un fichier déposé dans un projet privé et non gelé ne date rien pour un lecteur extérieur » est trop
     fort. Le tiers enregistre déjà la date et l'empreinte (R-1580 : « date rendue par l'interface », « empreintes relues
     par l'interface CONFORMES »). Ce qui manque, c'est la visibilité et l'immuabilité : un fichier peut être retiré avant
     qu'on montre le projet, donc rien ne prouve que l'ensemble montré est complet. Point à vérifier : l'affichage public
     des dates de version une fois le projet rendu public.
  2. **Option (b).** « Avantage : date opposable » ne vaut qu'à la levée de l'embargo. Écrire plutôt : « date figée chez
     le tiers, vérifiable à la levée ou sur accès accordé ». À vérifier sur la documentation : la durée maximale de
     l'embargo ; sa levée automatique à terme (si elle existe, (b) est une publication décidée aujourd'hui et différée) ;
     la possibilité d'un accès pendant l'embargo ; le délai d'approbation d'un enregistrement ; et si un lien de lecture
     seule, donné au jury, montrerait les dates sans rendre le projet public.
  3. **Option (c).** Le plan la présente comme connue alors qu'elle n'est pas éprouvée ici. Il faut :
     - archiver chaque preuve d'horodatage avec un compagnon (R6) ;
     - éprouver la vérification sur un cas sain et sur un fichier altéré avant tout usage (R5) ;
     - vérifier le délai de la preuve complète (avec OpenTimestamps, elle attend l'ancrage : quelques heures, à
       vérifier) ;
     - préciser si le « mot » de Lazar vaut pour tous les scellements du bras ou un par un.
  4. **Le jour de l'entretien**, écrire ce que le jury peut vérifier sous chaque option :
     - (a) : chemins, empreintes et dates ;
     - (b) : rien sans accès ;
     - (c) : l'empreinte et la date d'une pièce, si on lui remet la pièce et sa preuve ;
     - socle seul : rien.

### CV-11 — à corriger — « No attack material would be exchanged in either direction » est incompatible avec « les mêmes règles »

- **Où** : courriel, l. 27-29 et 33-34 ; plan, section 3 (b), l. 66-69 (« N'exige aucun échange de recette »).
- **Pourquoi** :
  1. **La règle impose une entrée de matériau.** Sous la règle, le juge est le seul lecteur des recettes ; il vérifie
     l'échelon, le plafond et le dommage de chaque épisode. Les moniteurs gelés lisent les épisodes une fois (règle,
     l. 188-191 et 200 ; N-056 point 6). Pour être scorés « under the same rules », les épisodes de l'équipe extérieure
     doivent donc entrer dans notre coffre.
  2. **Compatibilité avec N-057 : dans le seul sens sortant.** N-057 interdit que nos cellules sortent (point 2) ; il
     n'interdit pas de recevoir.
  3. **Contradiction interne du courriel.** Il dit aussi « Any handling of sabotage episodes would follow the terms of
     [our external security review] » (l. 33-34).
  4. **Publication de leurs propres attaques.** Il manque des termes : une attaque publiée, puis lue par nos concepteurs,
     n'est plus tenue à l'écart (N-054 point 3 ; N-062).
- **Correction proposée** :
  - Plan, (b) :
    > **N'exige** aucune de nos recettes. **Exige** que les épisodes de l'équipe extérieure, scellés et horodatés par
    > elle, entrent dans notre coffre, pour être lus une fois par nos moniteurs gelés et par le juge (règle, l. 188-191).
    > À défaut, l'équipe applique nos critères de dommage avec son propre juge et ne remet que des comptes, ce que nous
    > ne pouvons pas vérifier. Choix de Lazar, avec les termes de garde de ces épisodes (quarantaine dans l'esprit de
    > N-057, revue de sécurité externe, nœud 3) et de publication de leurs attaques (classes seulement, ou après notre
    > dernier cycle).
  - Courriel, l. 28, au lieu de « No attack material would be exchanged in either direction; » :
    > We would not share any of our own attack material. To score your attacks under the same rules, [your sealed attack
    > episodes would be read once by our frozen monitors and by our damage judge, under our quarantine terms, and you would
    > receive the evasion curve and failure classes / you would apply our damage criteria with your own judge and report
    > counts only — to be decided]. [Terms for publishing your own attack details — to be agreed.]

### CV-12 — à corriger — L'échelon 3 est déjà réglé par le nœud 2

- **Où** : plan, l. 66-67 (« écrit ses propres attaques aux échelons 2 et 3 ») et l. 70-71 ; courriel, l. 27 (« writing
  its own attacks » « under the same rules ») et l. 29 ; « À décider », l. 45-46.
- **Pourquoi** : mot de Lazar sur le nœud 2 (`registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md`,
  branche `claude/upbeat-cray-dmauvv`, `bba97a1a…` ; candidat de la règle, l. 78 et 126-127). L'échelon 3 n'est permis
  qu'à deux conditions :
  1. « une procédure d'optimisation déjà publiée, citée, sans qu'aucune instance écrive de recette » ;
  2. un plafond de requêtes scellé avant toute requête.

  C'est un « bras d'attaque déclaré » au sens de N-053 point 5. Le courriel ne reprend que la condition 2 (l. 45-46).
  Une équipe libre de ses procédures à l'échelon 3 ne joue donc pas « under the same rules » : il faut choisir.
- **Correction proposée** :
  - Plan, (b) :
    > À l'échelon 3, deux choix pour Lazar : l'équipe s'en tient à la liste fermée des procédures publiées (pièce 3 de la
    > demande du 10 novembre, à écrire) et au plafond scellé, ce qui donne les mêmes règles mais éprouve la mesure plus
    > que l'inventivité de l'attaquant ; ou ses procédures sont libres, et son point est rapporté à part, hors de la
    > courbe commune. Dans les deux cas, l'équipe devient un bras d'attaque déclaré (N-053 point 5). L'interface de
    > requêtes rend un verdict, jamais une note ; elle a un coût d'hébergement (devis et GO).
  - Courriel, à la suite du crochet de la l. 29 :
    > [At the query-access level, the same rules allow only published optimization procedures from a closed list, with a
    > query cap sealed before any query / your procedures would be free and reported separately from the shared curve —
    > to be decided.]

### CV-13 — à corriger — Le courriel promet ce que Lazar n'a pas décidé ; « À décider » est incomplet

- **Où** : courriel, l. 11, 20-21, 28-29, 32-33, 42-48.
- **Pourquoi** :
  1. « and share our own results with you before publication » (l. 33) est hors crochets, alors que l'en-tête dit le
     contraire (l. 11). Sans ordre fixé, cette promesse peut aussi rompre l'indépendance (CV-8).
  2. « we pre-register and timestamp » (l. 20-21) est au présent, alors que la forme de l'horodatage est le nœud 7,
     ouvert.
  3. « we would share the frozen monitor designs » (l. 28-29) est une divulgation de pièces non publiées hors du
     programme. Ces pièces sont à relire pour qu'aucune ne trahisse le mode tenu à l'écart ni un contenu en quarantaine.
     Ce point est absent de « À décider ».
- **Correction proposée** :
  - Courriel, l. 20-21 :
    > Before reading any result, we pre-register our monitors (frozen) and the rules of an adversarial evaluation [, with a
    > third-party timestamp — form to be decided].
  - Courriel, l. 28-29 : « we would share [the frozen monitor designs, reviewed so that none discloses held-out
    material], the protocol, … ».
  - Courriel, l. 32-33 :
    > In return, [we would acknowledge your contribution / we would welcome co-authorship — to be decided]. [Each team
    > would seal its results with a third-party timestamp before seeing the other's; results would then be exchanged before
    > publication — to be decided.]
  - « À décider », ajouter :
    - le partage des conceptions gelées hors du programme : lesquelles, relues par qui ;
    - l'entrée des épisodes de l'équipe dans le coffre, ou le juge de l'équipe (CV-11) ;
    - les termes de garde et de publication de leurs attaques ;
    - à l'échelon 3, liste fermée ou procédures libres rapportées à part (CV-12) ;
    - l'ordre de scellement avant tout échange de résultats (CV-8) ;
    - le coût de l'interface de requêtes (devis et GO) ;
    - la forme d'horodatage citée (nœud 7).

### CV-14 — à préciser — Protocole décrit par le courriel : quatre imprécisions

- **Où** : courriel, l. 21-24 et 29.
- **Pourquoi et texte proposé** :
  1. **Notes.** L'attaquant ne reçoit pas non plus les notes (N-056 point 6 ; règle, l. 66). Écrire « but not their
     calibrated thresholds, scores or test episodes ». Le crochet de la l. 29 devient « [query access returning only
     flagged / not flagged, with a query cap sealed before any query] ».
  2. **Témoins positifs.** « positive controls (a monitor with a planted flaw) » : la règle a deux témoins positifs.
     Écrire « positive controls (a monitor with a deliberately planted flaw; a reproduced published attack) ».
  3. **Témoin négatif.** « honest-versus-honest » est opaque pour un lecteur extérieur. Écrire « an honest-only control
     (honest agents on both sides) ».
  4. **Axes de la courbe.** « as a function of the attacker's knowledge and query budget » : la courbe suit l'échelon
     d'accès (connaissance, requêtes, écriture des activations ou des poids) et le budget. Écrire « as a function of the
     attacker's access level and budget ».

### CV-15 — à préciser — Le tableau « avant l'entretien » cache des conditions

- **Où** : section 6, l. 89-97.
- **Pourquoi et texte proposé** :
  - **Date.** L'entretien est « dans deux semaines (≈ 22 novembre 2026, jour exact à confirmer) » (R-1834, l. 1792) ; à
    écrire.
  - **Ligne 1.**
    - La colonne « Qui : Lazar » confond décider et exécuter : les dépôts du 5 et du 8 novembre ont été exécutés par une
      session, sous GO.
    - La ligne suppose scellées deux pièces encore en contre-lecture.
  - **Ligne 2.** Il faut aussi :
    - la fusion dans `main` (le script lit `main`) ;
    - un manifeste v2 ;
    - la relecture de tous les chemins du projet, dépôts du 5 et du 8 novembre compris, avant de le rendre public ;
    - le délai d'approbation d'un enregistrement (à vérifier).
  - **Ligne 3.** L'envoi suppose les décisions de CV-11 à CV-13. Offrir un accès en requêtes, c'est annoncer une dépense
    future.
  - **Ligne 5.** « Seulement si les nœuds du devis sont tranchés vite » sous-estime les conditions. Le préenregistrement
    en pose huit (l. 341-353), dont :
    - un code qui n'existe pas encore (l. 12-15) ;
    - un GO de calcul qui cite le devis v4 : GO-2026-10-31-05 cite le devis v1 et échoit le 14 novembre (l. 345) ;
    - le GO de Lazar pour Llama-3-8B-Instruct, absent de la liste autorisée (l. 168-170).
  - **Ligne à ajouter en tête** : « Dépôt de l'empreinte de la règle et du préenregistrement de Bailey sur le projet
    privé, sous GO-2026-11-05-08 (jusqu'au 30 novembre) | oui, dès leur scellement et le mot de Lazar sur le nœud 7
    (règle, l. 58-59) | exécuté par la session qui scelle ». C'est le seul geste qui ne demande ni compte ni service
    neufs.

### CV-16 — à préciser — Trois vérificateurs manquent

- **Où** : plan, entre les sections 3 et 4.
- **Pourquoi et texte proposé** :
  1. **Réanalyse publique.** Décider dès maintenant ce qui sera publié avec chaque lecture : notes par épisode,
     étiquettes, classes, graines, manifestes, code de lecture, sans aucun contenu. Avec cela, n'importe qui recalcule la
     courbe, les témoins et la loi exacte du seuil. C'est le vérificateur extérieur le moins cher, et il ne touche pas à
     la quarantaine.
  2. **Tiers de confiance sous confidentialité (séquestre).** Pour les pièces qui ne sortiront jamais (familles
     aveugles, recettes, épisodes d'épreuve), c'est le seul vérificateur qui puisse attester que la pièce lue est la pièce
     scellée, et relire le journal des accès au coffre (N-057 point 5). La revue de sécurité externe (nœud 3), si elle
     existe par écrit, est le candidat naturel.
  3. **Auteur de l'échelon 1.** Les familles aveugles sont écrites par « une personne désignée par Lazar, hors des
     concepteurs et hors de cette session » (règle, l. 60-61 et 76). Si cette personne est extérieure au programme, un
     attaquant extérieur existe déjà dans le dispositif ; le plan doit le dire.

### CV-17 — à préciser — Manifeste v2 : portée, branche, moment

- **Où** : section 1, « Manque », l. 27-29.
- **Pourquoi et texte proposé** :
  - **Portée.** Le script existant ne lit que `main`, et seulement `prereg`, `docs/verdicts` et `docs/decisions`
    (`LISEZMOI.md`, l. 9-12 ; champ « dossiers » du manifeste). Or :
    - la règle et le préenregistrement de Bailey sont sur la branche de la session ;
    - l'index des familles aveugles (dans `registres/`), les moniteurs gelés et les décisions du 10 novembre
      (passations sur des branches) sont hors de sa portée.

    Prévoir la fusion et l'extension de la portée.
  - **Moment.** Le dépôt doit précéder non seulement l'ouverture, mais toute course (règle, l. 58-59 et 244) et la
    remise des conceptions gelées à tout attaquant, interne ou extérieur.
  - **Procédure du `LISEZMOI.md`.** Son étape 2 suppose l'accès au dépôt privé : la future version doit dire qu'un tiers
    la suit avec les pièces que le programme lui remet.

## Ce que je n'ai pas pu vérifier

- Le fonctionnement de l'Open Science Framework : durée et levée de l'embargo, accès pendant l'embargo, affichage public
  des dates et empreintes des versions, lien de lecture seule, retrait de fichiers, délai d'approbation d'un
  enregistrement. Documentation non consultée.
- Les services d'horodatage (norme RFC 3161, OpenTimestamps) : délais, confidentialité de l'empreinte envoyée, durée de
  vie des preuves. De mémoire, non éprouvé.
- SHADE-Arena, Liars' Bench, NARCBench : contenu, disponibilité de l'ensemble complet, licences, consigne donnée à
  l'agent. Non lus.
- L'état « en contre-lecture » des deux candidats : la consigne le dit, et le préenregistrement de Bailey porte
  « différentiel relu avant scellement » (CL2-21). Les deux peuvent changer après ma lecture ; mes renvois de lignes
  valent pour les empreintes de l'en-tête.
- Qu'aucune décision sur le dépôt d'empreintes ne soit consignée ailleurs que sur `main`, la branche de la session et
  `origin/claude/upbeat-cray-dmauvv` (pièces citées seulement).
- Le jour exact de l'entretien.
- L'existence d'une pièce écrite de la revue de sécurité externe (nœud 3) : la règle du jeu dit n'en avoir trouvé aucune.
- La pièce 3 de la demande (liste fermée des procédures publiées de l'échelon 3) : aucun fichier de ce nom suivi par git
  à 09:21 UTC (recherche par nom seulement). Le dossier non suivi `docs/sources/pdf/procedures-publiees-echelon-3-v1/`
  existe (sources en préparation, sans doute) ; je ne l'ai pas ouvert.
- Le brief de la session « attaquant informé » et le devis v4 de Bailey : non lus.
- Que la session auteur n'ait lu aucun résultat de moniteur (section 7) : hors de ma portée.
