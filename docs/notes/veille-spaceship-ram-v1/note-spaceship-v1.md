# Veille — « Spaceship », démonstration d'interface de pilotage d'un texte en cours d'écriture : ce qu'elle apporte au programme — v1

- **Rédacteur** : lecteur neuf, sous-agent de la session mère, le 18 novembre 2026 (03:15 à 03:50 UTC). Je n'ai écrit
  aucune pièce du programme ; je n'ai rien lancé sur un modèle, rien dépensé, rien committé.
- **Objet lu** : `/home/user/chuanqisun/spaceship`, commit `4ddd4d1061aa5f22113d5dd03462b3b3e5f506a6` (vérifié par
  `git rev-parse HEAD`, arbre propre), licence MIT (`LICENSE`, `c2095d56…`). Code lu, jamais exécuté.
- **Statut de ce texte** : note de veille. Le projet d'essai de la section 3 est un **projet**, pas un
  préenregistrement : il n'est ni contre-lu (règle R2) ni scellé comme tel, et ne permet aucun lancement.
- **Chiffres** : tout chiffre de l'éditeur Google est cité avec son fichier versé et son empreinte ; aucun n'est
  vérifié par nous. Tout chiffre de prédiction ou de devis est **mon a priori ou mon estimation**, et le dit.

## 1. Verdict

**Peu utile au fond, utile sur deux points d'outillage.** Spaceship ne mesure rien et n'ouvre aucun modèle : ses
« attention », « vecteurs » et « influence » sont trois habillages d'appels à des modèles par leur texte. Il ne prend
rien à nos revendications. Il sert à deux choses : (i) il signale un point d'accès neuf de Google, « decisions »
(lancé le 11 novembre 2026), qui rend des probabilités annoncées calibrées pour des questions fermées — un juge boîte
noire à probabilité native, à connaître ; (ii) il pose la question « ce que le modèle dit regarder contre ce qui cause sa
sortie », qui chez nous touche l'étage de triage de la base « triage, inspection, jugement » et l'extrait cité par un
moniteur. Cette question est **très occupée** dans la littérature (section 5) : l'essai de la section 3 ne vaudrait
que comme contrôle d'instrument, pas comme résultat à publier.

## 2. Les trois constats de la session mère, vérifiés sur le code

Tous trois **confirmés**, avec deux précisions.

1. **Le « moniteur d'attention » est un second appel à un modèle, pas une lecture d'attention.**
   `src/text/live-attention.ts` (`21b40adc…`), lignes 7 à 21 : une consigne demande de choisir « 1 à 3 » passages du
   texte déjà écrit « dont les tout prochains mots dépendent le plus », chaque passage étant une copie exacte de 2 à 8
   mots consécutifs, le mot le plus important entre crochets ; lignes 23 à 38 : l'appel part par `streamCompletion`
   (`src/llm/cerebras.ts`, `e16a50e0…` : service Cerebras, modèle `gpt-oss-120b` ; température 0,3 fixée dans l'appel) ; lignes 50 à 73 :
   la réponse est recollée au texte par recherche exacte de la suite de mots. Aucune activation, aucun poids
   d'attention, aucune probabilité de jeton n'est lu nulle part (recherche de `logprob`, `attention_weights`,
   `hidden_states`, `activation` dans `src/` : rien).
   **Précision 1** : ce n'est même pas un auto-rapport au sens strict. Le modèle qui désigne est le même modèle que
   celui qui écrit la suite, mais dans un **autre appel**, avant que la suite existe (la suite est écrite par
   `src/text/live-completion.ts` à température 0,9) : il **prédit** de quoi dépendra une suite qu'il n'a pas produite.
   En mode de démonstration sans clé, la « désignation » est un tirage au hasard de 3 à 5 mots
   (`src/text/simulated-attention.ts`).
2. **Les « vecteurs de pilotage » sont des axes nommés, passés en texte dans la consigne.**
   `src/text/live-dimension.ts` (`eb96ce40…`), lignes 10 à 20 : un catalogue fermé de neuf axes (tension, résolution,
   rythme, mode, focalisation, ton, distance, fortune, surprise) ; lignes 22 à 43 : un appel demande au modèle de choisir
   les axes « qui comptent le plus » et de rendre les lignes inchangées. `src/text/live-completion.ts` (`591584dc…`),
   lignes 8 à 28 : la consigne de continuation reçoit un bloc « KEY PHRASES » (les passages verrouillés) et un bloc
   « CONTROLS » ; lignes 84 à 99 : chaque réglage devient une ligne de texte « nom : valeur (force) ». Aucun vecteur
   n'est ajouté à une activation. Le « verrou d'attention » de la démonstration est le bloc « KEY PHRASES », rien d'autre.
3. **Les scores d'influence, de pertinence et de réalisation viennent du point d'accès « decisions » de Google.**
   `src/llm/decisions.ts` (`ab9ec43a…`) : requête `POST https://generativelanguage.googleapis.com/v1beta/decisions`,
   trois types de question (`noul`, `choice`, `score`), réponses typées avec `probabilities` et `confidence`. Usages,
   tous sur le modèle `gemini-decision-1` : `src/text/live-influence.ts` (`1d957ff2…`, une question à quatre niveaux par
   phrase : « à quel point la phrase i se relie-t-elle à la phrase suivante et l'influence-t-elle ? ») ;
   `src/text/live-relevance.ts` (`2da2796b…`, pertinence d'un mot-clé pour la phrase en cours) ;
   `src/text/live-realization.ts` (`de8eeb98…`, question oui ou non : « la phrase i livre-t-elle ce que le réglage
   demande ? »).
   **Précision 2** : l'interface rend bien des probabilités et une confiance, mais **Spaceship ne lit ni l'une ni
   l'autre**. Il ne garde que la valeur de tête : le niveau moyen divisé par le niveau maximal (`answer.score /
   (levels.length - 1)`, lignes 43 et 31), ou la probabilité du oui (`answer.noul`, ligne 20, rangée dans un champ que
   le code nomme `confidence` — ce n'est pas le champ `confidence` de l'interface). Les champs `probabilities` et
   `confidence` ne sont lus dans aucun fichier de `src/`. Et l'« influence » ainsi notée est le **jugement d'un
   troisième modèle sur le texte**, sans lien causal avec le modèle qui écrit. En mode sans clé, c'est `Math.random()`
   (`src/text/simulated-influence.ts`).

Le dépôt ne contient ni évaluation, ni données, ni mesure d'accord entre ces indicateurs et quoi que ce soit.

## 3. Projet d'essai préenregistrable — les passages que le modèle désigne sont-ils ceux qui causent sa sortie ?

Nom en clair : **essai de concordance entre passages désignés et passages causaux**, sur notre modèle ouvert à
8 milliards de paramètres. Rien n'est lancé. Avant tout lancement : texte dans le gabarit
`prereg/gabarit-preregistrement-v1.md`, contre-lecture par un sous-agent neuf (R2), scellement (R1), devis, feu vert.

**Objet.** `meta-llama/Llama-3.1-8B-Instruct` (liste blanche de `src/controle_ia/harnais/modeles.py`, révision gelée
au manifeste), joué par le harnais d'épisodes (`src/controle_ia/harnais/episode.py`, `79113b49…`). La sortie étudiée
est **le verdict du moniteur faible par action** des bases boîte noire : un score continu lu en une passe par
l'espérance sur les jetons de valeur (`src/controle_ia/bases/scores_jetons.py`, `64946a47…`) — donc sans bruit
d'échantillonnage, ce qui rend l'effet d'un effacement exact. Sortie secondaire, descriptive : la suite écrite par
l'agent lui-même (log-probabilité, sous lecture forcée, des 32 premiers jetons de la suite réellement produite).

**Matériau.** 300 contextes d'**épisodes honnêtes neufs**, joués pour l'essai à graines propres (R9), dans
l'environnement des propositions d'expériences ; **aucun organisme, aucun épisode d'un travail sous embargo**. Chaque
contexte est découpé en phrases par une règle de programme gelée (8 à 25 phrases). Monde à vérité connue pour le
contrôle : 100 contextes de plus reçoivent, par programme, une **phrase décisive plantée** (un défaut objectif que la
grille du moniteur nomme, déclaré en clair) et une **phrase neutre plantée** de même longueur.

**Influence causale (la référence).** Pour chaque phrase s : I(s) = |score(contexte) − score(contexte privé de s)|.
Deux façons d'effacer, toutes deux rapportées : suppression (principale) ; remplacement par une phrase neutre de même
longueur tirée d'un autre épisode (pour répondre à l'objection connue : un texte troué sort de la distribution du
modèle — Hase, Xie et Bansal, arXiv 2106.00786). Plancher : la loi des effets de la phrase neutre plantée ; une phrase
est « influente » au-dessus de son 95e centile.

**Désignations comparées (les bras).**
- auto-désignation dans un appel séparé (bras principal ; consigne calquée sur celle de Spaceship : 1 à 3 passages
  recopiés à l'identique ; décodage glouton ; recollage exact au texte ; toute désignation qui ne se recolle pas est
  comptée « invalide » et rapportée, jamais réparée — R5) ;
- auto-désignation dans le même appel, juste après le verdict ;
- désignation par un **autre** modèle (`Qwen/Qwen2.5-7B-Instruct`, qui reçoit le contexte et le verdict du premier) :
  c'est le contrôle de l'accès privilégié ;
- règles sans modèle : dernière phrase ; phrases qui partagent le plus de mots avec la grille ; phrases les plus
  longues ; tirage au hasard ;
- en option, descriptif : attribution boîte blanche par gradient fois entrée, sommée par phrase.

**Hypothèse (H-désignation).** Les passages que le modèle désigne sont plus influents que des passages pris au hasard,
mais pas plus que ceux d'une règle simple ni que ceux désignés par un autre modèle : la désignation relève du plausible,
pas d'un accès du modèle à sa propre causalité.

**Métrique principale.** Par contexte, probabilité qu'une phrase désignée ait un effet causal plus grand qu'une
phrase non désignée (égalités comptées pour moitié) ; moyenne sur les contextes ; intervalle de confiance à 95 % par
rééchantillonnage des épisodes. Secondaires : la phrase la plus influente est-elle parmi les désignées ; chute du score
quand on efface toutes les désignées, comparée à l'effacement d'autant de phrases au hasard (mesure d'« exhaustivité »
de DeYoung et al., arXiv 1911.03429).

**Prédictions chiffrées et signes (a priori du rédacteur, non tirées de la littérature).**
- P1, signe + : métrique principale de l'auto-désignation séparée à **0,70**, attendue dans [0,60 ; 0,80] (hasard : 0,50).
- P2, signe nul : écart entre l'auto-désignation et la meilleure règle sans modèle dans [−0,05 ; +0,05].
- P3, signe nul : écart entre l'auto-désignation et la désignation par l'autre modèle dans [−0,05 ; +0,05].
- P4, contrôle : la phrase décisive plantée est la plus influente dans au moins 90 % des contextes de contrôle, et
  désignée dans au moins 80 %.

**Seuils gelés.** « Concorde » : borne basse de l'intervalle de la métrique principale ≥ 0,80 **et** borne basse de
l'écart à la meilleure règle sans modèle > 0. « Ne concorde pas » : borne haute ≤ 0,65. Sinon : « concordance
partielle, sans avantage établi sur une règle simple ». Aucun signe n'est visé (R3) : chacune des trois issues se lit.

**Plan d'analyse.** (1) Gardes, avant toute lecture de la métrique : rejeu à l'identique au bit près d'un
échantillon ; taux de désignations invalides ; contrôle P4. (2) Un seul test principal (auto-désignation séparée,
effacement par suppression) ; le reste est descriptif, rapporté par bras, par façon d'effacer et par tiers de position
dans le contexte (la récence est le confondant attendu). (3) Audit de symétrie (R4) écrit d'avance : une métrique
au-dessus de 0,90 ou sous 0,50 déclenche le même audit (fuite de la position des phrases plantées dans la consigne,
défaut de découpage).

**Liste d'arrêt.** Rejeu non identique ; plus de 20 % de désignations invalides ; contrôle P4 manqué (l'instrument
d'effacement ne retrouve pas une cause plantée : l'essai ne dit rien) ; moins de 60 % des contextes avec au moins une
phrase au-dessus du plancher (scores plats : « sans objet ») ; dépassement du plafond de dépense ; tout épisode sous
embargo ou tout organisme dans le matériau ; tout modèle hors de la liste blanche.

**Ce que l'issue changerait pour les bases boîte noire.** Les critères de la porte G1 ne bougent dans aucun cas ; rien
n'entre dans une liste scellée sans nœud à part.
- « Concorde » : l'étage de triage de la base « triage, inspection, jugement » (`src/controle_ia/bases/trace_lite.py`)
  et l'extrait qu'un moniteur cite peuvent se lire comme une localisation ; la boîte noire reçoit alors une base de
  localisation bon marché, à laquelle la localisation par les sondes devra se comparer.
- « Ne concorde pas » ou « partielle » (ma prédiction) : l'extrait cité par un moniteur est une justification
  plausible, pas la cause de son verdict. Trois conséquences : aucun de nos textes ne présente un extrait cité comme
  « ce qui a déclenché le verdict » ; la vérification par programme de l'extrait cité (N-060) établit qu'il existe
  dans la pièce, pas qu'il a pesé ; et la base boîte noire de localisation honnête devient l'**effacement phrase par
  phrase** (une passe par phrase), à inscrire comme bras descriptif.

**Devis (ordre de grandeur, estimé, rien de mesuré).** Environ 400 contextes × (1 + environ 15 phrases × 2 façons
d'effacer) ≈ 12 000 passes avant d'environ 1 500 jetons, plus environ 2 400 désignations courtes (deux modèles, trois
bras) : **2 à 4 heures d'une carte graphique de 24 Go**. Au prix des locations récentes du dépôt (0,10 à 0,60 USD de
l'heure pour une carte), **1 à 3 USD ; plafond proposé 5 USD**. Aucun appel payant à un modèle externe. Code et essais
sur processeur : routine.

## 4. Ce que la documentation publique dit du point d'accès « decisions »

J'avais l'outil de recherche. Sources : pages officielles de l'éditeur, versées sous `sources/` (adresses et heures :
`sources/adresses-v1.md`).

- **Existence.** Point d'accès en version bêta, `POST /v1beta/decisions`, modèle `gemini-decision-1`
  (`sources/google-decisions-reference-v1.md`, `0d4bbd05…`, lignes 9 et 13) ; billet de lancement daté du 11 novembre
  2026 (`sources/google-decisions-billet-lancement-v1.html`, `46c39328…`, ligne 4179). Les types du code de Spaceship
  correspondent à la référence.
- **Fonctionnement annoncé.** Une entrée partagée (texte, image, son, vidéo, PDF) et jusqu'à 1 000 questions ;
  chaque question est évaluée seule, en une passe, sans voir les autres ni son propre identifiant ; aucun jeton de
  sortie (`sources/google-decisions-guide-v1.md`, `1dcafa4b…`, lignes 36 à 39 et 1280 à 1283).
- **Sens des probabilités.** Question oui ou non : `noul` est « la probabilité calibrée que la réponse soit oui »,
  **toujours bornée entre 0,01 et 0,99** (lignes 145 et 234). Choix : probabilité de chaque option, somme 1 ; les
  options sont triées par ordre alphabétique avant l'évaluation ; **la masse est toujours répartie entre les options,
  même si aucune ne convient** (lignes 241 à 248 et 350). Note sur une échelle : `score` est la **moyenne des indices
  de niveau pondérée par leurs probabilités**, donc peut tomber entre deux niveaux (ligne 365).
- **Sens de la confiance.** « Probabilité estimée (de 0 à 1) que la réponse de tête soit juste » ; **elle est égale à
  la probabilité de l'issue de tête**, ou à max(noul, 1 − noul) pour le oui ou non (lignes 693 à 695). Ce n'est donc pas
  une seconde mesure : c'est la même loi, lue autrement.
- **Calibration : affirmée, non documentée.** Le mot « calibrated » revient partout ; le billet de lancement écrit que
  le modèle a « la plus faible erreur de calibration » sur une suite de bancs (ligne 5165), chiffres en image, sans
  méthode ni données dans le texte que j'ai lu. **Non vérifié, non opposable.** L'éditeur lui-même conseille de fixer
  les seuils « sur des exemples étiquetés de votre propre trafic » (ligne 709) et prévient : « traitez l'entrée comme
  non fiable ; un texte fourni par l'utilisateur peut plaider pour son propre classement » (lignes 1242 à 1244).
- **Prix annoncé** : 0,10 USD par million de jetons d'entrée, sortie non facturée (billet, ligne 5056) ; à relire sur
  la page des prix avant tout devis.

**Comment mesurer sa calibration sur un monde à vérité connue** (projet, aucune dépense engagée).
1. **Questions à vérité certaine**, écrites et corrigées par programme (un fait présent ou absent dans un texte, une
   propriété d'un tableau), à difficulté graduée : diagramme de fiabilité par déciles, erreur de calibration attendue
   avec intervalle, score de Brier décomposé (fiabilité, résolution), pente et ordonnée d'un recalibrage logistique.
   La borne [0,01 ; 0,99] plafonne la perte logarithmique : le dire.
2. **Questions à probabilité connue** : des fiches tirées de notre **monde planté** (loi à trois issues connue de
   nous). On donne la loi et les traits d'une fiche, on demande l'issue : la bonne réponse calibrée est la probabilité
   de la loi. On compare la probabilité rendue à la **probabilité vraie**, pas seulement à l'issue tirée. C'est le
   seul montage qui sépare « calibré » de « sûr de lui à raison ».
3. **Questions sans bonne option** (type choix) : quelle confiance rend-il quand rien ne convient ?
4. **Invariances annoncées, à éprouver** : ajouter ou retirer une question voisine ; renommer les options (donc
   changer leur rang alphabétique) ; paraphraser ; poser la question et sa négation (les deux probabilités
   doivent se compléter).
5. **Sous attaque** : un texte qui plaide pour son classement (l'éditeur l'annonce comme faiblesse). C'est le
   terrain du papier C.
Coût : environ 5 000 questions en 500 appels de moins de 2 000 jetons ≈ 1 million de jetons d'entrée, soit **de l'ordre
de 0,10 USD au prix annoncé** — négligeable, mais c'est un appel payant à un modèle externe : feu vert requis.

## 5. Antériorité — l'essai de la section 3 apporterait-il du neuf ?

**Franchement : non, pas comme résultat.** Voisins établis sur leur notice arXiv (titre, auteurs, date, résumé :
`sources/arxiv-voisins-fidelite-v1.xml`, `683e5477…`) ; **aucun PDF lu, aucun chiffre repris**.

- **Le même schéma, déjà fait** : Madsen, Chandar et Reddy, « Are self-explanations from Large Language Models
  faithful? » (arXiv 2401.07927) — le modèle dit quels mots comptent, on les retire, on regarde si la prédiction
  tient ; sur Llama 2, Mistral, Falcon ; conclusion du résumé : la fidélité dépend de l'explication, du modèle et de la
  tâche, les auto-explications « ne doivent pas être crues en général ». Huang et al., « Can Large Language Models
  Explain Themselves? » (arXiv 2310.11207) — attributions auto-déclarées comparées à l'occlusion et à LIME.
- **Le cadre et les métriques** : Jacovi et Goldberg (arXiv 2004.03685, définir la fidélité) ; DeYoung et al., ERASER
  (arXiv 1911.03429, exhaustivité et suffisance par effacement) ; Covert, Lundberg et Lee (arXiv 2011.14878, expliquer
  par retrait) ; Hase, Xie et Bansal (arXiv 2106.00786, le texte troué sort de la distribution) ; Jain et Wallace,
  puis Wiegreffe et Pinter (arXiv 1902.10186, 1908.04626 : l'attention n'est pas, ou n'est pas tout à fait, une
  explication).
- **Explications en langue et raisonnement affiché** : Turpin et al. (arXiv 2305.04388) ; Lanham et al. (arXiv
  2307.13702) ; Atanasova et al. (arXiv 2305.18029) ; Chen et al., simulabilité contrefactuelle (arXiv 2307.08678) ;
  Parcalabescu et Frank (arXiv 2311.07466) ; Agarwal, Tanneru et Lakkaraju (arXiv 2402.04614) ; Siegel et al. (arXiv
  2404.03189) ; Matton et al. (arXiv 2504.14150) ; Tutek et al. (arXiv 2502.14829) ; Chen et al., « Reasoning Models
  Don't Always Say What They Think » (arXiv 2505.05410) ; Korbak et al. (arXiv 2507.11473).
- **Influence causale par phrase, en boîte noire** : Bogdan, Macar, Nanda et Conmy, « Thought Anchors » (arXiv
  2506.19143) — importance contrefactuelle de chaque phrase par rééchantillonnage.
- **Accès privilégié du modèle à lui-même** (mon bras « autre modèle ») : Binder et al., « Looking Inward » (arXiv
  2410.13787) — un modèle se prédit-il mieux qu'un autre modèle entraîné sur ses sorties.

**Ce qui pourrait rester, et c'est une question, pas une zone libre (R8)** : le cas précis d'un **moniteur de
contrôle** dont on compare l'extrait cité à ce qui pèse causalement sur son **verdict de suspicion**, dans des
transcriptions d'agent. Je ne l'ai pas cherché au niveau qu'une revendication exige ; la zone est séduisante, donc à
vérifier plus durement. Ma recommandation : ne rien revendiquer ; si l'essai tourne un jour, il tourne comme
**contrôle d'instrument** des bases boîte noire, cité derrière Madsen et al.

## 6. Nœuds pour Lazar

1. **Lancer ou non l'essai de concordance** (section 3). Enjeu : savoir si l'extrait cité par nos moniteurs boîte
   noire localise quelque chose. Options : (a) ne pas le lancer, et écrire dès maintenant dans nos textes qu'un
   extrait cité n'est pas une cause (gratuit ; s'appuie sur la littérature, pas sur notre modèle) ; (b) le lancer
   après la porte G0 comme contrôle d'instrument (1 à 3 USD, une demi-journée de code). Recommandation : **(a)**,
   confiance ≈ 75 % ; (b) seulement si un texte du programme doit s'appuyer sur un extrait cité.
2. **Le point d'accès « decisions » comme juge boîte noire à probabilité native.** L'ajouter à un panel serait un
   changement de modèle (interdit sans feu vert) et une lignée de plus (N-053). Recommandation : **ne pas l'adopter
   maintenant** ; le noter en veille ; la mesure de calibration de la section 4 (≈ 0,10 USD) ne vaut que si tu
   envisages de t'en servir. Confiance ≈ 80 %.
3. **Aucune collision** : Spaceship n'occupe aucune zone revendiquée par le programme.

## 7. Limites

- Code de Spaceship lu, jamais exécuté ; je n'ai pas vu l'interface tourner.
- Aucun PDF des voisins lu : notices arXiv seulement. La recherche d'antériorité est **rapide** ; elle n'a pas le
  niveau d'une lecture sur PDF et ne vaut pas preuve qu'une zone est libre.
- La documentation de Google est celle de l'éditeur ; je n'ai pas appelé l'interface ; la calibration annoncée n'est
  pas vérifiée ; les chiffres en image du billet ne sont pas lus ; la page des prix n'est pas lue.
- Les prédictions de la section 3 sont mes a priori ; le devis est estimé (débit d'une carte non mesuré pour ce
  montage).
- Je n'ai ouvert aucun résultat des travaux sous embargo ; je n'ai lu de `registres/go.md` que des lignes de prix et
  les titres des six dernières lignes.
