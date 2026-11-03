# Contre-lecture R2 — pilote de l'exposant p, v1, brouillon 1

Contre-lecteur neuf (sous-agent) : je n'ai écrit ni ce préenregistrement, ni son code, ni sa lecture du papier. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pilote-exposant-p-contre-lecture-prompt.md` (`ba52ce0d28f526e010f7795a73d88409b6c56ced05c050b34509f8cb851878ce`). Travail du 3 novembre 2026, de 09:12 à 10:10 UTC (`date -u`). Branche `canal/conv-audit-n04`, lecture seule : tête `6511bbf1` au début, `e30e202d` à la fin ; les commits du canal intervenus entre-temps (n° 408, 409, R-1343 à R-1348) ne touchent aucun fichier du pilote (diff vide, empreintes revérifiées).

Respecté : aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié (`git status` vide à la fin) ; rien sous `donnees/` ; aucun `git fetch`, `checkout` ni `stash` ; aucun appel de modèle ; aucune carte, aucune dépense ; `WebFetch` pour le papier seulement. Une seule tentative de téléchargement du PDF du papier par le terminal (`curl`), refusée par le mandataire (403), pour l'empreinter (R7). Le clone du code publié que le rédacteur a laissé hors dépôt (`/home/claude/scratch/pilote-exposant-p/code-tiers/fsec-paper`, tête `a9355d40…`) est lu comme une donnée : fichiers texte lus, caches `pickle` lus par le lecteur restreint du dépôt (`references.LecteurRestreint`), rien n'y est exécuté. Mes outils et sorties sont sous `/home/claude/scratch/pilote-p-contre-lecture/` (hors dépôt).

Fichiers lus : `CLAUDE.md` (`a2aabda8…`), les sept pièces de `brouillons/pilote-exposant-p-v1/`, tout `src/controle_ia/pilote_exposant_p/` (dont `amont/`, `references_publiees/`), `tests/test_pilote_exposant_p_v1.py`, `scripts/pilote_exposant_p_instance_v1.sh`, comparé à `scripts/p3_instance.sh` et `scripts/amorce_instance_p3.sh` ; `prereg/gabarit-preregistrement-v1.md`, `src/controle_ia/prereg.py`, `manifeste.py` (partie préenregistrement), `.claude/hooks/garde_calcul.py` ; le papier par `WebFetch`.

## Verdict

**Non scellable** en l'état. Il faut un brouillon 2.

- B1 exige de réécrire les stimuli : il ne se règle pas par couples.
- B3, B4 et B6 demandent du code et des essais nouveaux.
- Le reste se règle par les 32 couples fournis.

Comptes : **7 bloquants, 8 importants, 9 mineurs ; 32 couples** (21 au préenregistrement, 5 à `analyse.py`, 4 à `run.py`, 1 au devis, 1 au script).

Ce qui tient :
- la reprise du protocole du papier : couche 2, mesure à la sortie du bloc 30, seuil par paire, normalisation géodésique, copie amont à l'identique ; le témoin 3,003 est retrouvé à 10⁻⁶ ;
- les essais : 34 et 62 passés ;
- la simulation de puissance, rejouée à l'identique ;
- la règle à trois issues, ouverte dans les deux sens ;
- le script : il ne pousse que sur une branche `calcul/…` neuve et arrête les processus par leur identifiant.

## Ce que j'ai rejoué, avec les empreintes

1. **Empreintes** : les 29 compagnons `.sha256` du pilote et de la consigne passent `sha256sum -c`, avant et après les commits du canal.
2. **Essais, commande exacte de la consigne** (sans réseau, sans carte) : `34 passed in 82.05s`, de 09:22:31 à 09:23:57 UTC.
   - Commande du script d'instance (quatre fichiers) : `62 passed in 82.68s`, de 09:24:10 à 09:25:36. C'est le « 62 » attendu.
   - `git status` reste vide ensuite.
3. **Simulation de puissance complète**, même entropie (2026110302), sortie hors dépôt : identique à la sortie scellée champ par champ, durée exceptée (577,8 s contre 908,1 s). Rejeu : `rejeu/puissance-rejeu-complet.json`, `07381e3ba3295e8ee47eac91c65144d87fb3992623c46cbd3c91586770314b08`. La sortie scellée (`35dc3bdf…`) porte sa propre durée, d'où l'empreinte différente.
4. **Papier** : lu par `WebFetch` aux décalages 0, 14 500, 20 000, 29 000 et 40 000, par questions ciblées et citations courtes. Le convertisseur ne rend ni pages ni citations longues : niveau transcription (R7). Points confirmés :
   - couche 2, avant-dernière couche, dernier jeton ; 30 ancres FineWeb de 5 jetons, médiane (éq. 2) ; seuil f = 0,5 (éq. 3, note 1) ;
   - paires contrastives « P ≥ 30 », « LLM generated and human verified » (§3, annexe A) ; différences aléatoires à P = 30, « most stringent non-feature baseline », 40 directions, 710 paires gardées sur 780 ;
   - règle « below 0.1 » (§4.1, sans valeur absolue) et |⟨dᵢ, dⱼ⟩| < 0,1 sur les directions brutes (annexe A) ; raison donnée : « at this overlap the orthogonalised direction remains more than 99% aligned » ;
   - moyennes du §4.1 ; légende de la figure 2 : « p>2 indicates these directions are privileged » ; §6.1 (p mesuré, borne basse) ; §6.2 ; §7 (« necessary but not sufficient ») ;
   - annexe B : « Every sub-group median residual is below 2% » ; annexe C.4 : le mélange rompt à α = 4,70, après les axes ;
   - aucune valeur par modèle n'est donnée dans le texte ; le texte ne dit pas si les modèles sont de base ou Instruct.
5. **Code publié** (texte lu dans le clone) :
   - `src/data.py` (`e9bfd99d…`), `load_fineweb_fixed_length` : même flux, même mélange, même découpe par lots de 1 000 textes, même filtre des entrées de moins de 5 jetons. Le sous-ensemble 0 du pilote est donc celui du papier si le flux n'a pas changé ;
   - `src/model.py` (`fde09ad1…`), `forward_from_layer_to_layer` : blocs `start+1` à `end` inclus ; `scripts/sweep_2d.py` (`3bb621b6…`) : `measure_layer = n_layers + measure_offset` = 30. La convention du pilote (sortie du bloc 2 perturbée, sortie du bloc 30 relevée) est la bonne ;
   - `results/thrpair_audit.md`, `272827f3…` (même empreinte que dans `references-publiees-v1.json`) : Contrastive de Gemma 2,423 [2,285 ; 2,619] ; Random-diff 2,050 [2,001 ; 2,098] ; Llama 2,632 [2,388 ; 2,897] ; ligne 3 : `target=gemma L=2, max_overlap=0.1` (le double filtre relevé par la lecture est confirmé).
6. **Calculs du contre-lecteur** : graines par `SeedSequence`, écrites dans chaque outil ; empreintes des outils en fin de rapport. Chacun est repris plus bas.
7. **Couples** (`outils/couples.py`) : chaque « ancien » figure une fois et une seule dans son fichier, dans l'ordre d'application. Les couples ont été appliqués à des copies, et les 34 essais du pilote repassent sur une copie qui porte les couples de code : `34 passed in 106.48s`, de 10:01:53 à 10:03:41.

## Bloquants

### B1 — Stimuli : au dernier jeton de la couche 2, E est d'abord un contraste de derniers mots (point 1 du rédacteur)

Les sources : `outils/fins_stimuli.py`, `minimalite_paires.py`, `cos_er_lexical.py`.

**Confusion lexicale.** Le dernier mot est temporel (tomorrow, today, tonight, Friday, now, afternoon…) dans 27 phrases FD sur 30 et 25 CD, contre 0 FE et 2 CE. La fin porte un pronom de première personne dans 26 FD et 26 CD, contre 0 FE et 1 CE. Une minimisation (just, only, merely) figure dans 7 CE et 2 FE, aucune phrase D. Au protocole du papier (dernier jeton, couche 2), E oppose donc « nom d'évaluation, ton détaché » à « mot de date, première personne ». C'est précisément le contraste que la règle du papier « at or near the end » fait lire. Les règles R-S1 à R-S7 ne contrôlent pas le dernier mot.

**Recouvrement de structure.** Le dernier mot est partagé entre registres dans 25 couples FD/CD sur 30, mais seulement 7 couples FE/CE. Les derniers mots CE se répètent : anyway 5 fois, lol 4 fois, benchmark 3 fois.
- Modèle stylisé, sans modèle de langage : une phrase y est représentée par le plongement gaussien aléatoire de son dernier mot, plus une part w de la moyenne des mots précédents. E et R y sont calculés comme dans le pilote.
- Résultat : cos(E, R) médian −0,190 (w = 0), −0,181 (w = 0,3), −0,144 (w = 1,0), et |cos| ≥ 0,1 dans 100 % des 300 tirages de chaque cas.
- Témoin à 120 derniers mots tous distincts : médiane +0,001, 0 %.
- La structure des fins suffit donc à produire l'issue « exclu ». La répétition jouet du rédacteur va dans ce sens (cos = −0,12, issue « exclu »). L'a priori « exclu 0,15 » paraît bas.

**Paires non minimales.** Les paires sémantiques du papier changent un seul mot (médiane 1 ; Tense 3). Celles de E changent une fin entière (médiane 8 à 8,5 mots, de 6 à 14). Seules les directions de registre du papier (Formal, Literary) réécrivent ainsi la phrase (9 à 10 mots). Écart non déclaré : E-17, couple P14.

**Sens** (contrôle que `stimuli.py` laisse au contre-lecteur). Dans environ 12 quadruplets, la fin « évaluation » formelle se lit aussi comme une évaluation humaine propre au contenu, et non comme une évaluation de l'assistant :

| Quadruplet | Fin | Lecture humaine plausible |
|---|---|---|
| Q02 (gâteau) | « scored by evaluators » | un jury |
| Q07 (prêt) | « formal assessment » | une étude de crédit |
| Q08 (caution) | « checked by the evaluators » | un état des lieux |
| Q09 | « scored examination » ; « scored quiz » | l'examen de l'utilisateur |
| Q10 (lettre de motivation) | « review panel » | un jury de recrutement |
| Q15 (chien) | « standard test battery » | des tests d'allergie |
| Q16 (essai clinique) | « graded by the research team » | l'équipe de l'essai |
| Q20 | « assessment items » | une évaluation de l'utilisateur |
| Q21 | « graded exercise » | un devoir |
| Q25 | « calibration test » | ambigu |
| Q26 | « the graders will review the answer » | une copie corrigée |
| Q28 | « assessment protocol » | ambigu |

Les fins familières nomment plus souvent le modèle (« the bot », « eval run », « test set »). Les phrases « déploiement » parlent bien d'un besoin réel, mais presque toutes d'un besoin daté.

**Vérification humaine.** Le papier dit ses invites « LLM generated and human verified » (§3, annexe A). Celles du pilote sont écrites et relues par des modèles. Écart non déclaré : E-16, couple P14.

**À faire au brouillon 2** (stimuli neufs, empreintes neuves de la configuration et du préenregistrement) :
- **R-S8 (fins).**
  - Le dernier mot porte le statut, et il est le même dans les deux registres d'un quadruplet : FE et CE finissent par le même porteur d'évaluation, FD et CD par le même porteur de déploiement.
  - Le registre est porté par l'ouverture et le corps, jamais par le dernier mot.
  - 30 porteurs d'évaluation distincts, 30 porteurs de déploiement distincts.
  - Aucune classe lexicale (mot de date, première personne, minimisation) n'est présente d'un côté du statut et absente de l'autre.
  - Garde : le modèle stylisé (`outils/cos_er_lexical.py`, à reprendre dans `stimuli.py`) doit donner une médiane de |cos(E, R)| < 0,03, éprouvée sur un cas sain et sur un artefact (R5).
- **R-S9 (sens).** Chaque fin « évaluation » nomme l'assistant, le modèle ou un objet d'évaluation de modèle (benchmark, suite d'évaluation, test set), sans lecture humaine plausible dans le domaine du contenu.
- **Paires minimales** pour E autant que possible, sinon l'écart est déclaré.
- **Vérification humaine** des 120 phrases par Lazar, consignée avant le scellement.
- **Prix à dire au préenregistrement** : avec un dernier mot partagé, R n'est plus porté que par le contexte. Il sera sans doute plus faible au dernier jeton de la couche 2. C'est le prix d'un E et d'un R qui ne partagent pas une interaction de derniers mots.

### B2 — Un plan contre la moyenne d'une famille : les phrases gelées en disent plus que la règle (point 2)

La règle compare p̄(E, R) à la **moyenne** des différences aléatoires. Les phrases parlent de « paires sans concept » (« plus que pour des paires sans concept » ; « rien ne distingue la paire … d'une paire sans concept »).

La simulation du rédacteur suppose que les plans de référence sont hétérogènes (τ = 0,17), mais que le plan lu est exactement à leur moyenne sous Δ = 0. Avec son générateur et sa banque, reconstruite à l'identique (`rejeu/scenarios-supplementaires.json`, `8f5636219999e50b34890fefd0297e028b53db6e4a7bf0ac4349c1ff8c562545`), j'ai tiré le plan lu comme une paire sans concept ordinaire, c'est-à-dire comme un plan de référence (S = 32, M = 60, R = 400, B = 2 000) :

| τ | « au-dessus » | « au-dessous » | « égal » | « non concluant » |
|---|---|---|---|---|
| 0,10 | 18,8 % | 21,5 % | 52,5 % | 7,2 % |
| 0,17 | 28,5 % | 29,2 % | 32,0 % | 10,2 % |
| 0,25 | 30,5 % | 31,5 % | 24,0 % | 14,0 % |

Au τ du rédacteur, une paire sans concept serait donc déclarée « au-dessus » 28,5 fois sur 100, sous la phrase « le réseau privilégie les directions pures E et R … plus que pour des paires sans concept ». Ce τ suppose 0,2 de bruit d'ancres sur Gemma ; si ce bruit est plus faible (voir B3), τ approche 0,24.

Deux voies :
- **(A) Minimale** : comparer à la moyenne et le dire, et rapporter le rang de p̄(E, R) dans la famille à côté de la phrase. Couples P01, P08, P15, A01 à A03.
- **(B) Recommandée si le devis le permet** : mesurer K plans de différences aléatoires sur les 32 sous-ensembles (par exemple K = 8, soit 256 plans de plus) pour estimer τ, puis lire p̄(E, R) contre un intervalle de prédiction d'un plan de référence mesuré de la même façon.
  - Le coût, à chiffrer par le rédacteur : environ +1,1 h au débit attendu et +4,3 h au débit pessimiste, soit +1,3 à +5,2 USD au prix haut de 1,2133 USD l'heure. C'est dans le plafond de 30 USD de Lazar (R-1344).
  - Il faut alors revoir le plafond interne de 14 400 s et le délai de 270 min, avec un devis neuf.

### B3 — Référence sur le seul sous-ensemble 0, plan lu moyenné sur 32 (point 2)

L'argument « corrélation ≈ 0 entre plans » ne tient que faiblement. Mesures :
- rééchantillonnage conjoint des 30 ancres, B = 600, sur les trois grilles versionnées (`outils/correlation_ancres.py`) : 0,021 (Wealth × Gender et isotrope 1), 0,183 (Wealth × Gender et isotrope 2), 0,054 (entre isotropes) ;
- demi-échantillons disjoints de 15 ancres : −0,107, 0,343, −0,054 ;
- sur les 17 isotropes publiés (`outils/isotropes_17.py`) : 0,030 en moyenne par rééchantillonnage, 0,034 par demi-échantillons.

Ces chiffres n'excluent pas un effet commun de quelques centièmes à 0,06 d'écart type.

**Contradiction relevée.**
- Sur leurs 30 ancres publiées, toutes distinctes, les 17 isotropes ne s'écartent entre eux que de 0,096 en écart type. Je retrouve le 1,930 de la lecture.
- À l'intérieur d'un tirage avec remise, le même écart type vaut 0,252 en médiane (`outils/isotropes_17_dispersion.py`).
- Sur 15 ancres distinctes, il vaut 0,238 ; sur 24 ancres distinctes tirées sans remise, 0,137.

Le rééchantillonnage avec remise gonfle donc d'environ 2,5 fois la dispersion propre à chaque plan. Deux conséquences :
- le générateur, calé sur ce rééchantillonnage, surestime le bruit propre à chaque plan : la puissance est prudente sur ce point ;
- mais il sous-estime le poids relatif de tout effet commun, que ni l'intervalle ni la simulation ne contiennent.

**Effet, même générateur, même banque** (Δ = 0, plan lu à la moyenne, τ = 0,17) :

| Écart type de l'effet commun | Référence | « au-dessus » | « au-dessous » | « égal » |
|---|---|---|---|---|
| 0,035 | sous-ensemble 0 seul (brouillon) | 3,5 % | 7,2 % | 78,5 % |
| 0,035 | répartie, plan k sur k mod 32 | 2,5 % | 2,8 % | 85,3 % |
| 0,06 | sous-ensemble 0 seul | 8,0 % | 10,7 % | 71,3 % |
| 0,06 | répartie | 3,0 % | 4,8 % | 83,3 % |

Les taux déclarés (2,8 % et 3,0 %) ne valent donc que sans effet commun.

**Correctif gratuit** : mesurer le plan de référence k sur le sous-ensemble k mod 32 (couples R01, R02, P05, P11, P13). Deux compléments sont recommandés :
- un rééchantillonnage par sous-ensemble : tirer les 32 sous-ensembles avec remise, chacun emportant son p(E, R) et ses plans de référence ;
- une simulation de puissance refaite avec un effet commun.

### B4 — La sensibilité de l'instrument sur le modèle lu n'est contrôlée par rien de décisif (question de la consigne)

Le préenregistrement écrit : « l'instrument … se transporte au modèle Instruct ; c'est contrôlé par le témoin positif sur le modèle de base et par les isotropes sur le modèle lu ». C'est inexact :
- le témoin sur le modèle de base valide la mise en œuvre, sur le modèle et le code du papier ;
- les isotropes sur le modèle lu ne valident que le côté nul (p ≈ 2 sans structure) ;
- rien de décisif ne montre que l'instrument voit un privilège sur le modèle lu. Wealth × Gender sur le modèle lu (32 sous-ensembles, déjà au devis) et la famille contrastive y sont descriptifs.

Une issue « égal », que le texte dit « réponse pleine », serait donc ininterprétable si le modèle lu ne montrait de privilège pour rien. C'est la sortie la plus probable si le réglage d'instruction aplatit la réponse au bloc 30.

À faire :
- Rendre Wealth × Gender sur le modèle lu décisif pour « égal » et « au-dessous » : Δ_WG = p̄(Wealth × Gender, lu) − p̄(différences aléatoires), intervalle entièrement au-dessus de 0. Sinon, ces deux issues deviennent « non concluant (sensibilité non montrée sur le modèle lu) ».
- Faire tourner ce bloc juste après la référence, avant les descriptifs.
- Le coder, dans l'ordre de `run.py`, dans `analyser` et dans une phrase gelée, avec un essai sur un cas sain et sur un artefact. Couples P02, P10, P11, P12, P17 pour le texte.

### B5 — Les phrases gelées ne disent pas ce que chaque issue ne montre pas (question de la consigne)

- **Bornes absentes.** Le texte dit « Toutes sont bornées : couche 2, ancres de 5 jetons, réponse L2, modèle Instruct sans gabarit ». Les phrases codées (`analyse.PHRASES`) ne portent que « couche 2 » et le nom du modèle : ni dernier jeton, ni ancres de 5 jetons, ni réponse L2, ni gabarit.
- **« égal »** ne dit pas qu'il ne montre rien des couches moyennes ni des contextes longs, ni que p ≈ 2 n'exclut pas un trait mal aligné (§6.1). Ces réserves ne figurent que dans « Lecture des combinaisons », avec un renvoi mal placé à « §7 : p > 2 n'est pas suffisant » : cette réserve borne « au-dessus », pas « égal » (couple P17).
- **« au-dessous »** affirme que les mélanges « rompent le plateau plus tôt que la seule taille L2 ne le prédit », c'est-à-dire une comparaison à p = 2. Or la règle compare à p̄(différences aléatoires), qui peut s'écarter de 2. La phrase peut être fausse. Elle ajoute « aucun privilège des directions pures, au contraire », sans borne.
- **« exclu »** lit « le recouvrement est le résultat » sur un seuil technique : au papier, Gram–Schmidt déforme au-delà de 0,1. À |cos| = 0,1, les deux directions sont à 84° l'une de l'autre, et ce recouvrement peut venir de la structure des fins (B1).
- **« non concluant »** dû à plus de 20 % d'échecs reçoit la phrase « l'intervalle contient 0 et sort de ±0,2 », un motif faux (`run.analyser`).
- Couples A01 à A05, R03, R04, P07, P15. Les phrases neuves ont été rendues et passent `test_phrases_gelees_completes`.

### B6 — R5 : une partie des gardes de la liste d'arrêt n'est éprouvée sur aucun artefact

Ce qui est éprouvé :
- copie amont ;
- lecteur restreint ;
- quatre règles de stimuli et invites du papier ;
- configuration : la constante δ et l'empreinte des stimuli ;
- R1 sans préenregistrement ;
- fonctions de contrôle de l'instrument.

Jamais éprouvés :
- l'arrêt « instrument non validé » au niveau du lanceur (`ArretInstrument`, sorties écrites, code 3) : le mode jouet le contourne (`if not self.jouet …`) ;
- le plafond de durée (arrêt avant un bloc décisif, saut d'un bloc descriptif) ;
- la grille non finie ;
- le tokeniseur discordant ;
- un flux FineWeb-edu de moins de 10 000 entrées ;
- les branches « empreinte des références » et « commit amont » de `exiger_config` ;
- les chemins « exclu » et « non concluant (échecs) » de la lecture ;
- deux des quatre déclencheurs de symétrie : témoin à 0,01 près avec des ancres différentes, résidu supérieur à 2 % ;
- le script d'instance entier. `tests/test_script_p3.py` porte 12 essais pour le script de P3, aucun n'existe pour celui du pilote, qui en est décliné.

À faire : essais en mode jouet avec conditions forcées (indicateurs de configuration ou remplacements à l'essai), et un fichier d'essais du script décliné de `tests/test_script_p3.py`. Le compte « Tests attendus » change en conséquence.

### B7 — R7 : des chiffres du texte du papier fondent des seuils sans source empreintée (point 10)

δ = 0,2 repose sur « 2,42 − 2,05 = 0,37, §4.1 », un chiffre de transcription : le PDF n'est pas empreinté, et le terminal reçoit 403. Même chose pour « aucun [résidu] au-dessus de 2 % » (annexe B). Les deux sont vérifiables dans l'audit empreinté du code (2,423 et 2,050 ; médianes de résidu de 0,85 % à 1,28 %) : couples P06 et P19.

Le seuil 0,1, P ≥ 30 et 40 directions pour 780 paires restent au niveau transcription. Ils n'entrent que dans des déclarations d'écart, et 0,1 est aussi dans le code.

Pour lever la réserve, Lazar fournit le PDF, comme pour 2608.28945 (R-1342) ; on l'empreinte et on cite les pages. D'ici là, réserve R7 déclarée.

## Importants

- **I1 — Témoin positif (point 4).**
  - La norme moyenne est une empreinte à un seul nombre. Une empreinte forte et gratuite existe : les 30 grilles publiées par ancre de Wealth × Gender. Les maxima d'axe par ancre varient de 7,3 à 50,3 sur l'axe 1 (écart type du logarithme 0,50) et de 33,9 à 64,0 sur l'axe 2 (0,13). Une corrélation de rang des maxima par ancre supérieure ou égale à 0,95 sur chaque axe dit « mêmes ancres » sans ambiguïté (à coder).
  - La tolérance ±0,15, dite « supposée », est étayée par le calcul (`outils/sensibilite_temoin.py`, `decalage_temoin.py`). Un bruit indépendant de 0,5 par point et par ancre donne un écart type de p de 0,059, |Δp| > 0,15 dans 1,5 % des tirages, et des intercepts à moins de 0,67° au quantile 95 %. À 0,66 de bruit : 4,0 % ; à 1,0 : 9,5 %. Un décalage uniforme du plancher jusqu'à 1,5 donne |Δp| ≤ 0,052. ±2° convient.
  - Si les ancres diffèrent, l'intervalle [2,420 ; 3,702] vient du rééchantillonnage avec remise, qui gonfle la dispersion (B3). Il est lâche : cette branche ne valide la mise en œuvre que faiblement, et la lecture doit le dire.
  - Suggestion : figer la révision de FineWeb-edu au dernier commit antérieur au 23 juin 2026 plutôt qu'à la révision du jour.
  - Couple P09.
- **I2 — Cinq écarts au papier non déclarés** (question de la consigne) :
  - E-16 : vérification humaine des invites ;
  - E-17 : paires non minimales ;
  - E-18 : inférence sur un plan seul contre une moyenne de famille, alors que le papier compare des familles (figure 4) et ne lit un plan seul qu'en illustration (figure 2) ;
  - E-19 : règle du cosinus prise comme issue terminale ;
  - E-20 : tolérances du témoin positif, que E-14 ne couvre pas.
  - Couple P14.
- **I3 — L'audit « l'issue doit tenir quand on retire chaque sous-ensemble » n'est pas défini.** Le code ne rapporte que l'étendue des estimations ponctuelles de Δ, référence fixe (`delta_retrait_d_un_sous_ensemble`). Il faut définir l'audit (32 issues recalculées, réserve si une diffère, couple P18) et le coder.
- **I4 — Plans mixtes (point 6) : « p proche de Wealth × Gender » n'est pas un critère gelé.**
  - Couple P16 : critère chiffré.
  - Les plans (E, rdₖ) partagent leurs directions rd₀ à rd₉ avec des paires de référence.
  - Sur le fond, l'idéalisation du rédacteur suit le modèle de réponse du papier. Si R(v) = F(Σᵢ wᵢ |f̂ᵢᵀv|ᵖ) avec des traits orthonormaux et f̂₁ᵀr ≈ 0, le plan (f₁, r) donne exactement le même exposant p en coordonnées normalisées. C'est une prédiction du modèle (calcul), non une validation : les témoins mixtes restent nécessaires.
- **I5 — Ordre et plafond.**
  - Les 24 plans descriptifs du modèle de base tournent avant les blocs décisifs du modèle lu.
  - `Pilote.bloc` ne leur réserve pas le temps de ces blocs : au pire, l'arrêt « plafond projeté » tombe après quatre heures de dépense, sans résultat décisif.
  - Le devis dit à tort que « les 110 plans décisifs passent en tête » (couple D01).
  - À coder : un bloc descriptif n'est lancé que si le temps restant couvre aussi les blocs décisifs à venir.
- **I6 — Portée (point 7).** Le pilote ne peut pas répondre à la thèse de Lazar telle qu'elle est posée (couches 10 à 30, contextes longs). Le texte ne dit pas ce que chaque issue fait à cette thèse :
  - « au-dessus » plaiderait contre une confusion au dernier jeton de la couche 2, pour des directions faites de fins ;
  - « exclu » ne la soutient pas sans séparer l'interaction (I8) ;
  - « égal » ne dit rien.

  Recommandation (décision « proposer avec recommandation » de Lazar, défaut sous 48 heures) : pas de bloc aux couches moyennes dans ce pilote, puisque le papier n'y a de référence que sur Gemma (§4.3). Le garder pour une suite, une fois l'instrument éprouvé sur le modèle lu. Confiance moyenne.
- **I7 — Amorce et GO.**
  - Le script ne vérifie aucun GO, contrairement à son en-tête. La garde de calcul ne bloque que `vastai create`, `launch` et `start`.
  - Le GO s'exige donc à la création de l'instance, par l'amorce, qui n'est pas écrite.
  - Le GO de Lazar (30 USD, R-1343 et R-1344) n'est pas encore inscrit dans `registres/go.md` sur cette branche.
  - Couples S01 et P20 ; l'amorce est à écrire et à contre-lire avant tout lancement.
- **I8 — Interaction statut × registre.** Dans le plan 2 × 2, E et R contiennent chacun la moitié de l'interaction I = FE − FD − CE + CD : un |cos(E, R)| non nul peut en venir. Ajouter des descriptifs sans plan neuf : |I| rapporté à |E| et |R|, cos(FE − FD, CE − CD), cos(FE − CE, FD − CD). C'est ce qui rend « exclu » lisible.

## Mineurs

- **M1** — La réserve « résidu > 2 % » cite « le papier n'en a aucun ». Le papier borne des médianes de sous-groupes (annexe B). Couple P19.
- **M2** — Le renvoi à §7 pour « égal » et « au-dessous » est mal placé. Couple P17.
- **M3** — La lecture (§5) n'a pas relevé que le §4.1 écrit « below 0.1 » sans valeur absolue, alors que l'annexe A met une valeur absolue. Le pilote suit l'annexe A et le code. Couple P07.
- **M4** — Aucune garde ne compare l'empreinte de la configuration citée par le préenregistrement à celle du fichier lu : le script vérifie le sceau compagnon, et le commit fige l'ensemble. Une ligne dans `run.exiger_config` suffirait.
- **M5** — `test_run_reel_sans_preenregistrement_refuse` installe un gestionnaire de TERM dans le processus de pytest : effet de bord.
- **M6** — La révision des modèles est lue deux fois : à la vérification d'accès du script, puis au chargement par le lanceur. Comparer les deux.
- **M7** — La réserve « trop beau » (demi-largeur < 0,05) est calée sur une précision simulée avec un bruit gonflé. Avec un bruit propre à chaque plan proche de 0,1, la demi-largeur réelle peut approcher 0,05 sans rien de suspect. Recaler sur la simulation refaite.
- **M8** — Deux corrections au tableau des prédictions :
  - les exemples « au-dessous » (Français × Japonais 1,28, JavaScript × Rust 1,50) sont des paires que le papier écarte : |cos| = 0,457 et 0,659 sur Llama (`outils/recouvrement_exemples.py`). Parmi les paires gardées, environ 8 % ont p < 2 (Status × Honesty 1,72 ; Health × Age 1,77 ; `outils/p_bas_gardees.py`). Couple P04 ;
  - le double filtre de l'audit est absent du tableau. Couple P03.
  - Mes comptes (345 paires au filtre de Llama, 323 au double filtre) diffèrent de 5 paires de ceux du rédacteur (340) et de l'audit (318). Je n'ai pas tranché cet écart ; il ne change pas le constat.
- **M9** — Le préenregistrement renvoie à une « section « Pour le contre-lecteur » » qui n'existe pas (couple P21). La licence de FineWeb-edu n'est pas vérifiée (sans réseau ici).

## Réponses aux dix points du rédacteur

1. Stimuli : non, R-S1 à R-S7 ne suffisent pas. Voir B1 ; ajouter R-S8 et R-S9.
2. Statistique principale : l'argument ne tient pas assez, et oui, la référence doit être moyennée ou répartie sur les sous-ensembles. Voir B3, et B2 pour le plan seul.
3. Règle à trois issues :
   - δ = 0,2 se fonde sur l'audit (0,373), couple P06 ;
   - la préséance d'« au-dessus » et d'« au-dessous » dans (0 ; δ) est symétrique, donc conforme à R3 ;
   - 2,8 % et 3,0 % ne valent qu'en l'absence d'effet commun et pour un plan lu exactement à la moyenne (B2, B3).
4. Témoin positif : voir I1. La tolérance tient par le calcul ; la branche « ancres différentes » est lâche ; l'empreinte par les grilles par ancre est à préférer.
5. Isotropes [1,75 ; 2,25] : raisonnable, et je retrouve le repère de 1,930. Mais ils ne contrôlent que le côté nul (B4).
6. Plans mixtes : voir I4.
7. Portée : voir I6.
8. Code : les conventions de couche et le chargement des ancres sont conformes au code publié. L'arrondi de la référence en lot de 1 pèse au plus 0,052 sur p (calcul). La branche réelle n'a jamais tourné, mais le témoin décisif passe en tête et échouerait tôt, donc à bas coût.
9. Simulation : rejouée à l'identique. Elle est prudente pour le bruit propre à chaque plan, mais ne l'est pas pour les deux composantes absentes (B2, B3).
10. Provenance : voir B7 et M9.

## Points ajoutés par la consigne

- **Règle à trois issues** : ouverte dans les deux sens. Les issues sont symétriques, les préséances aussi, et l'audit se déclenche pour les trois issues tranchées. Mais les phrases ne disent pas ce qu'elles ne montrent pas (B5), et « égal » est muet sur les couches moyennes.
- **Témoin positif et isotropes** : ils ne valident pas la sensibilité de l'instrument sur le modèle Instruct (B4).
- **Règle du cosinus** :
  - le seuil et le calcul sont ceux du papier : directions brutes, valeur absolue, 0,1 ; le texte garde « < 0,1 », le code « ≤ 0,1 » ;
  - l'usage n'est pas celui du papier : au papier, c'est un filtre de paires, ici une issue terminale lue comme un résultat (B5, I2).
- **Quinze écarts** : il en manque cinq (I2).
- **Le code ne lit rien d'autre que ce que le texte déclare** :
  - fichiers : configuration, stimuli, références empreintées, copie amont, préenregistrement ;
  - réseau : poids et tokeniseurs des deux modèles (sans code distant), flux FineWeb-edu au format parquet, métadonnées de révision ;
  - sorties : seuls les 30 textes du sous-ensemble 0 sont versés ;
  - rien sous `donnees/`.
- **Script d'instance** :
  - il ne dépense rien par lui-même : aucune création d'instance (I7) ;
  - il ne pousse que sur une branche `calcul/…` : motif imposé, `git ls-remote --exit-code` doit rendre 2, poussée initiale qui éprouve le droit d'écriture, aucune poussée forcée ;
  - il s'arrête proprement : pièges TERM et EXIT, résultats partiels committés et poussés, `timeout` à 270 minutes, arrêts par l'identifiant du processus (R10) ;
  - l'arrêt de l'instance est laissé à la session, comme pour P3 ;
  - aucun essai ne le couvre (B6).

## Pour le brouillon 2, dans l'ordre

1. Stimuli neufs (B1), vérifiés par Lazar ; garde R-S8 et modèle stylisé dans `stimuli.py`.
2. Référence répartie et rééchantillonnage par sous-ensemble (B3) ; témoin de sensibilité décisif sur le modèle lu (B4) ; voie A ou B pour le plan seul (B2).
3. Phrases (A01 à A05, R03, R04) et texte (couples P) ; écarts E-16 à E-20.
4. Essais des gardes et du script (B6) ; audit de retrait d'un sous-ensemble codé (I3) ; réserve de temps pour les blocs décisifs (I5) ; empreinte des ancres par grilles (I1) ; descriptifs de l'interaction (I8).
5. Simulation refaite (effet commun, plan lu tiré de la famille, bruit recalé sur des sous-ensembles d'ancres distinctes plutôt que sur le rééchantillonnage avec remise) ; nouveau « Tests attendus ».
6. Amorce écrite et contre-lue ; GO inscrit ; PDF du papier empreinté si Lazar le fournit (B7).
7. Contre-lecture neuve du brouillon 2 (R2).

## Fichiers produits (hors dépôt, aucun compagnon `.sha256` créé)

| Fichier | sha256 |
|---|---|
| `/home/claude/scratch/pilote-p-contre-lecture/contre-lecture-pilote-exposant-p-v1.md` (ce rapport) | donné dans la réponse finale |
| `/home/claude/scratch/pilote-p-contre-lecture/couples-contre-lecture-pilote-exposant-p-v1.json` (32 couples, empreintes des cinq fichiers sources) | `b6510f307f3464a170ea8a0728d6221886818ca599450528a5f3c2ff54811028` |
| `rejeu/puissance-rejeu-complet.json` | `07381e3ba3295e8ee47eac91c65144d87fb3992623c46cbd3c91586770314b08` |
| `rejeu/scenarios-supplementaires.json` | `8f5636219999e50b34890fefd0297e028b53db6e4a7bf0ac4349c1ff8c562545` |
| `outils/couples.py` | `11592ea4c3fa009385a9cecab9901cb1a7ccabb391356ccc23d184d30b934d9f` |
| `outils/scenarios_supplementaires.py` | `528e1e3c5bd01179bf234795eb0f685c77691a7d33b25a7635b023e29bc0b88d` |
| `outils/cos_er_lexical.py` | `9cb9cc013ad9b986a2029be2e8819c4ec0f6ae0e3020509a2ad5fbdb33755567` |
| `outils/fins_stimuli.py` | `f0af33a477165402b4ed043ba2656fddda6f8b84c3b1beb441e9aafff6001afe` |
| `outils/minimalite_paires.py` | `bdec57e78a8758c840bb28777aeed5b1eef0e24d9037d797bfdb1760efbc7e42` |
| `outils/correlation_ancres.py` | `2c15356eb6cafae4382b4d7ad436b95f411152dc0f42be811210e58b257edf69` |
| `outils/isotropes_17.py` | `51c3d3105ce48877d0ae03737f89c9b838140149df57fa36afa03716b1d7a091` |
| `outils/isotropes_17_dispersion.py` | `7caf24bb45ccc2e53982c723c37dfd02f99f96d900ea5af0b905a5d579b96189` |
| `outils/sensibilite_temoin.py` | `9fc67b313bc706014275fb711b64aa16904425ecace392e51ff41ba285964b83` |
| `outils/decalage_temoin.py` | `eb176bb9f5dd1ca227b2dacfb3fe86ae65f03aa0976b22abb68ae74c10c0bb68` |
| `outils/recouvrement_exemples.py` | `3a73fbf7ca9c8ead39d119226262ad1634e346da15be0a22d7dddc6ea1420e83` |
| `outils/p_bas_gardees.py` ; `p_bas_gardees_strict.py` | `493dad5f9726e61a47c41892e4a5f076b24c435bb70d034ddc4ec1b6f4b7bd0f` ; `9f0d73aef727803dbf9f2a18a8f3ab8be402ed73f2116d725b51a35a9e64dbc2` |

Les chemins relatifs du tableau partent de `/home/claude/scratch/pilote-p-contre-lecture/`. Les copies de travail `essai-couples/` (fichiers après couples) et `arbre-essai/` (arbre d'essai des 34 essais) restent sur place.
