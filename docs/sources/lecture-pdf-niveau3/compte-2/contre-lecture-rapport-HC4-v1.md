# Contre-lecture du rapport HC4 (« taxe de déplacement ») du compte 2 — v1

- **Rôle** : contre-lecteur (compte 2), rôle adverse. **Modèle** : modèle B. L'auteur du rapport est le modèle A ; A ≠ B.
- **Heures** (relevées par `date -u`) : début le 2026-11-13 à 23:36:11 UTC ; rédaction close le 2026-11-13 à 23:45:47 UTC. L'heure du scellement est celle du fichier compagnon `.sha256`.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme). `interdits-communs-v2.md` n'est pas nommé dans mon mandat : je ne l'ai pas ouvert, et j'ai tenu la consigne du compte 2.
- **Objet** : `rapport-HC4-v1.md`, empreinte vérifiée `dceefa6a0c4bb9c921604cd3eec98ab7fa6270115b23bc07ed6a70521fa5886c` (conforme) ; son archive `fichiers-de-travail-HC4-v1.tar`, empreinte vérifiée `d5c79196bcea9616c812b4057e1c9e98479bbbdd49e0f6bde7d8ee45284d4c1b` (conforme), extraite dans mon dossier de travail.
- **Fichiers du dépôt lus, aux lignes du mandat seulement** : `docs/programme-controle-ia-v2.md` l. 85-125 et 190-215 ; `docs/decisions/decision-N-013-v1.md` l. 46-55 ; `docs/decisions/decision-N-068-v1.md` l. 1-115 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` l. 412-431 ; `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` l. 509-535 et 696-726. Aucun autre fichier du dépôt, aucune commande git, aucun réseau, aucun appel de modèle, aucun refus, aucune ouverture fautive. Une liste du dossier des pièces (`ls`) a montré les noms des autres fichiers du lot 11 ; aucun n'a été ouvert.
- **Pièces** : empreintes vérifiées contre les compagnons `.sha256` avant lecture, toutes conformes.

| pièce | empreinte sha256 | pages | étendue relue par moi |
|---|---|---|---|
| `2601.04603v1.pdf` | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | 17 | p. 1-10 et 14-17 ligne à ligne ; p. 11-13 par mots (références) ; figures 2, 3, 4 et 5 (p. 7, 8, 14, 16) vues sur l'image |
| `2309.10253v4.pdf` | `f2b76387acd042a27db07e8093dc4f4f4b876eb28d6a16fcf886432b31f1ffac` | 26 | p. 9-14 ligne à ligne ; p. 1-8 et 15-26 par mots ; figures 5 et 9 non revues sur l'image |
| `2310.08419v4.pdf` | `590bf40aa58061928f54d01b7d53f0d5141bb2ecf4f01483c6849423934f44e4` | 34 | p. 1-9, 14 et 15 ligne à ligne ; tableau 1 (p. 4) vu sur l'image ; p. 10-13 et 16-34 par mots |
| `2502.19537v5.pdf` | `4f991dbe01b2c853189b45e1b36906bf355a367550f96703cf320b6e9f291d3c` | 37 | p. 1, 2, 5-9, 21, 36 et 37 ligne à ligne ; p. 4 en partie ; le reste par mots |

- **Citations contrôlées par programme** : 49, **0 échec** (`citations-contre-lecture-HC4-v1.json`, dans l'archive seulement). Script `scripts/verifier_citations_contre_lecture_v1.py`, lancé par `python3 -I`, avec et sans `-layout`, après normalisation ; essayé d'abord sur un cas juste (0 échec) puis sur trois cas altérés (texte, page, empreinte : 3 échecs attendus et obtenus). Second contrôle : mes 49 citations passent aussi le script du lecteur (0 échec), et les 79 citations du lecteur passent mon script (0 échec). Tout extrait anglais d'un PDF cité entre guillemets dans ce document figure dans mon JSON (contrôlé par programme : `scripts/extraire_guillemets_rapport_v1.py`). Seule exception, voulue : la formule inexacte du rapport, recopiée au constat A comme objet du constat ; elle n'est pas dans le PDF.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les noms de modèles qui apparaissent sont ceux des articles, dans leurs citations.

---

## 0. Verdicts

**Sur le rapport : « tient avec corrections ».** Les points chiffrés sont exacts. Les corrections portent sur une citation inexacte, sur ce que la comparaison sonde contre classifieurs autorise à dire, sur le rangement d'un point de coût de 2502.19537, et sur le verdict d'ensemble, qui dépend du sens de « juge ».

**Sur HC4, dans la table fermée, sous chaque lecture de « juge »** (je ne tranche pas la revendication) :

| lecture de « juge » | verdict | ce qui le porte |
|---|---|---|
| juge génératif (le moniteur de HC1 et de EC.1, celui que la rhétorique déplace) — lecture que les textes rendent la plus naturelle (section 1) | **« non trouvé dans les pièces lues »** | aucune des quatre pièces n'attaque un juge génératif ni ne mesure le coût de son déplacement ; 2601.04603 est un voisin très proche et un contre-indice indirect |
| tout modèle qui lit le texte, classifieur affiné compris — lecture retenue par le lecteur | **« occupé en partie »** | 2601.04603, p. 7-9 : une sonde et deux classifieurs affinés, mêmes échanges d'attaque, même calibration, sur le seul axe « taux de succès », en boîte noire, par transfert statique, pour une sonde de contenu nuisible ; le coût (requêtes, calcul, temps) n'y est pas comparé |

Dans les deux lectures, la comparaison du **coût** d'attaque d'une sonde et d'un juge, par régime d'accès, sous attaque qui s'adapte, pour une sonde qui lit l'intention ou l'action de l'agent auteur, n'est pas trouvée dans les quatre pièces. Zone peu cherchée (M14) : ce n'est pas un trou du champ.

---

## 1. Point 1 — le sens de « juge » dans HC4

Lignes relues :
- programme v2, l. 102 (HC1) : « g stable par moniteur génératif » ; l. 105 (HC3) : « déplacent les juges génératifs » ; l. 106 (HC4) : « le déplacement que la rhétorique obtient gratuitement sur un juge » (le rapport cite cette ligne comme « l. 105 » : c'est la l. 106, écart mineur) ; l. 194 (EC.1) : « g des juges génératifs » ;
- N-013, l. 48 : même tournure, « le déplacement que la rhétorique obtient gratuitement sur un juge » ;
- N-068, section 4 : « comparé au g des juges génératifs sous les mêmes attaques ».

Le « juge » de HC4 est défini par renvoi : c'est l'objet sur lequel la rhétorique obtient un déplacement, donc le moniteur génératif de HC1, mesuré à EC.1 par ses verdicts. **La lecture la plus naturelle est « juge génératif ».** Un classifieur affiné qui rend un score à seuil n'est pas l'objet de HC1.

Deux éléments empêchent de fermer la question :
- l'état de l'art de niveau 3 (l. 420-421) range déjà « des classifieurs durcis » du côté « juge » pour contester le mot « gratuitement » ;
- les classifieurs de 2601.04603 sont affinés à partir de modèles de langue génératifs (p. 4, 5).

Le lecteur a retenu la lecture large « sous R8 », et l'a dit (rapport, sections 0 et 9). Ce choix est défendable comme prudence, mais il ne doit pas décider seul du verdict de tête : voir le constat D.

---

## 2. Point 2 — la comparaison sonde contre classifieurs de 2601.04603 (p. 7-9, figure 2a)

**Les valeurs lues sur la figure 2a sont justes** (vue sur l'image, p. 7) : sonde environ 1,4 % ; petit classifieur entre 1,05 et 1,1 % ; très petit classifieur environ 4,5 % (figure). Le 1,4 % est aussi imprimé : « We find that using all available layers achieves the lowest attack success rate at approximately 1.4% » (p. 8). Figure 3a (p. 8, image) : petit classifieur environ 1,1 % ; sonde environ 1,4 % ; ensemble sonde et petit classifieur environ 0,45 % ; ensemble des deux classifieurs environ 0,8 % (figure). Conformes au rapport.

**Ce n'est pas un coût d'attaque.** C'est un taux de succès sur un jeu figé : « comprising approximately 7,000 exchanges designed to elicit harmful CBRN-related » information (p. 7). Aucun attaquant n'a interrogé la sonde, aucun effort n'est compté par moniteur. Le programme range bien « taux de succès » parmi les quatre axes de HC4 (l. 106), mais le taux de succès d'attaques rejouées n'est pas le taux de succès d'un attaquant qui s'adapte, et encore moins son coût.

**Trois limites que le rapport ne dit pas ou dit trop peu** :
1. *D'où viennent les attaques.* Les échanges viennent d'équipes rouges humaines qui attaquaient des systèmes de classifieurs. Les deux classifieurs comparés sont ceux de la cascade de la section 4 : « As baselines, we compare against the first-stage and second-stage classifiers from Section 4. » (p. 7). L'article ne dit pas contre quel système chaque échange a été écrit. Si une part vient de la campagne de la section 4, ces attaques étaient adaptées aux classifieurs et seulement transférées à la sonde ; sinon, tout est transfert. Le sens du biais n'est pas connu.
2. *Quelle position de sonde.* La sonde est entraînée sur Claude Sonnet 4 : « We train a linear probe on top of a Claude Sonnet 4 using concatenated activations » (p. 7) ; la légende ajoute « The linear probe uses activations from Claude Sonnet 4, which is the protected model. » (p. 8). Or aucune campagne décrite ne protège ce modèle : la cascade protège un autre modèle (« We use this system to guard Claude Opus 4. », p. 5), le système de production un troisième (p. 9). L'article ne dit pas quel modèle a produit les 7 000 échanges. Il n'est donc pas établi, pour ce jeu, que la sonde lit le modèle qui a généré : elle peut relire des échanges produits par un autre modèle (position « lecteur »).
3. *Aucune incertitude.* 1,4 % contre 1,1 % sans intervalle ni test ; si le dénominateur est le jeu entier, cela fait environ 98 contre 77 échanges (calcul, sous cette hypothèse non imprimée). Les auteurs écrivent seulement : « The probe achieves an attack success rate that outperforms the extra-small classifier and almost matches the Haiku 4.5 classifier. » (p. 8), et le résumé de l'introduction dit « Our analysis on static jailbreak data suggests that probes achieve robustness competitive with small fine-tuned external classifiers at negligible cost. » (p. 2).

**Le contre-indice tient-il ?** En partie, et pas contre ce que le rapport dit.
- Contre la **prémisse de coût** (« plusieurs ordres de grandeur ») : il ne tient pas comme mesure. Un taux par transfert ne dit rien du coût d'un attaquant qui vise la sonde. Écrire, comme le rapport en section 0, que « la sonde ne coûte pas plus cher à évader » dépasse la pièce (constat B).
- Contre une **robustesse propre de la sonde au contenu seul** : il tient comme contre-indice indirect. Des attaques en boîte noire, jamais écrites contre la sonde, la franchissent à environ 1,4 %, à calibration égale. Cela porte sur la lettre « le contexte seul n'y suffit pas » prise sans restriction.
- **Hors du périmètre restreint par N-068** (point 8a) : la sonde détecte un contenu nuisible dans l'échange, pas l'intention ou l'action d'un agent auteur ; l'auteur du contenu adverse est un utilisateur externe. N-068 tient déjà ce déplacement-là pour publié.

Rangement proposé pour la composante (e) de 2601.04603 : **« contre-indice indirect, hors du périmètre restreint par N-068 »**, et non « contre-indice » sans qualificatif.

---

## 3. Point 3 — les points de coût des trois autres pièces

**Exactitude.** Tous les chiffres des points G1 à G6, P1 à P6 et N1 à N6 que j'ai relus sont exacts, à la page dite : tableau 3 de GPTFuzzer (p. 12) ; tableau 1 (p. 9) ; tableaux 1, 2, 4, 5 et 8 de PAIR (p. 4, 5, 8, 15) ; tableaux 3, 4, 7, 8 et 16 de 2502.19537 (p. 6, 7, 8, 37) ; calcul de l'annexe F (p. 21). Non revus : les figures 5 et 9 de GPTFuzzer sur l'image.

**Rangement de la cible.**
- GPTFuzzer et PAIR : cible = le modèle lui-même. Juste. Une nuance manque : dans les deux, le juge est **dans la boucle d'attaque**. PAIR s'arrête quand le juge dit « jailbreak » : « Thus, the algorithm runs until a jailbreak is found or the maximum iteration count K is reached. » (p. 4). GPTFuzzer note chaque gabarit par son juge : « The cumulative score for the jailbreak template is derived from the sum of the scores from these 100 responses » (p. 12). Le juge n'est pas visé comme moniteur, mais l'attaque cherche son verdict positif ; ses faux positifs comptent comme des succès (constat H).
- PAIR, P4 : SmoothLLM n'est pas un filtre mais une défense par perturbation de l'entrée ; les deux défenses sont rejouées, non attaquées : « Both defenses are evaluated statically » (p. 7). Rangement « ni juge ni sonde » juste.
- 2502.19537, N3 : **mal rangé**. Le coût (5 000 exemples, 30 minutes) est celui du réglage fin du modèle surveillé. Le filtre de sortie est appliqué ensuite, sans rien lui adresser. Ce n'est pas un coût de déplacement d'un juge (constat E).

**Les incohérences relevées dans PAIR.**
1. « fewer than twenty queries » : tient. Le tableau 2 (p. 5) donne plus de 20 pour quatre cibles sur les six chiffrées. Nuance : le résumé dit « often » (« Empirically, PAIR often requires fewer than twenty queries to produce a jailbreak », p. 1) ; l'introduction, elle, est sans réserve (p. 2).
2. « 250-fold » : **ne tient pas telle qu'écrite**. Le facteur se retrouve : 5 120 / 20 = 256 (calcul), soit le budget de GCG du tableau 8 (p. 15) divisé par le « twenty » du titre. La phrase le dit presque : « Our results indicate that PAIR efficiently discovers prompt-level jailbreaks within twenty queries, which represents a more than 250-fold improvement over existing attacks such as GCG » (p. 2). L'incohérence réelle est ailleurs : le texte principal donne à GCG un budget de « around 256,000 queries per behavior » (p. 6), qui ferait 12 800 fois, et le « twenty » est nominal (constat F).
3. 256 000 contre 5 120 : tient. Les deux budgets diffèrent d'un facteur 50 (calcul) sans explication ; le tableau 8 porte sur un autre jeu, « a representative 50-behavior subset of the AdvBench dataset » (p. 15).
4. 88 % (tableau 2) contre 93 % (tableau 7, ligne par défaut, p. 9) : tient ; les requêtes par succès diffèrent aussi (10,0 contre 13,0).
5. « Vicuna-17B » (p. 2) : tient.

**Incohérence non relevée par le lecteur, qui touche le juge de mesure** : « we use Llama Guard as the JUDGE function, as it exhibits the lowest FPR while offering competitive agreement » (p. 5), alors que le tableau 1 (p. 4, vu sur l'image) donne à ce juge 7 % de faux positifs, contre 4 % pour le classifieur BERT et 7 % aussi pour GPT-4-Turbo ; son taux de faux négatifs est 47 % (auteurs).

**Un coût par succès qui n'est pas un coût d'attaque.** PAIR compte « the average number of queries used for successful jailbreaks » (p. 6) : les échecs ne sont pas comptés. Si chaque échec épuise les 90 requêtes (« PAIR uses two stopping conditions: finding a successful jailbreak or reaching the maximum number of iterations. », p. 6), le nombre attendu de requêtes par succès est, par calcul : Vicuna 22 ; Gemini 57 ; GPT-3.5 120 ; GPT-4 121 ; Llama-2 2 216 ; Claude-1 2 924 ; Claude-2 sans borne (0 succès). Le rapport le sous-entend (section 8, point 3) sans le chiffrer.

---

## 4. Constats

### A — majeur — citation inexacte (tableau des points de coût, ligne A3)

Le rapport écrit entre guillemets « with substantial effort and automated tools ». Le PDF imprime, **p. 5, note 3** : « expert-level red-teamers operating outside our bounty program were nonetheless able to discover universal jailbreaks for this system, though this required substantial effort and automated tools. » Le JSON du lecteur porte la phrase exacte (p. 5) ; c'est le rapport qui la déforme. Sens inchangé. Le compte 2 a signalé la page 9 : la phrase n'y figure pas (contrôle par programme : échec à la p. 9, succès à la p. 5) ; la page du rapport (« 5, 10 ») est juste.

Texte corrigé : « hors programme de primes, des experts trouvent des jailbreaks universels, « though this required substantial effort and automated tools » (note 3, p. 5 ; non chiffré) ».

**Autres extraits du rapport absents du JSON du lecteur** : j'ai extrait par programme tous les passages entre guillemets du rapport et confronté chacun au JSON du lecteur, puis aux pages. Aucune autre citation de phrase n'est inexacte. Restent, hors JSON mais exacts à la page dite : la phrase complète de la légende de la figure 3 (p. 8), « Appendix XXX » (p. 16), « gpt-3.5-turbo-0631 » (p. 4, 25, 26 ; le rapport dit 4 et 26), la phrase du tableau 4 de 2502.19537 (p. 5), et des mots isolés de tableaux. Deux titres de références sont cités avec une casse que le PDF n'imprime pas : le PDF écrit « can persuade llms to jailbreak them » (PAIR, p. 11) et « Fundamental limitations in defending llm finetuning apis » (2502.19537, p. 11). Mineur.

### B — majeur — un coût déduit d'un taux (section 0 ; section 2, composante (e) ; section 8, point 2)

Texte actuel (section 0) : « Ce point est un contre-indice à la prémisse de HC4 dans le régime boîte noire : à durcissement et calibration comparables, la sonde ne coûte pas plus cher à évader. »

La pièce ne mesure aucun coût d'évasion (section 2 ci-dessus). Texte corrigé :

> « Ce point est un contre-indice indirect, hors du périmètre restreint par N-068 : sur un jeu figé d'attaques en boîte noire qui n'ont pas été écrites contre la sonde, et à calibration égale, le taux de succès contre la sonde (environ 1,4 %) est proche de celui contre le petit classifieur (environ 1,1 %), sans intervalle ni test. Aucun coût d'évasion n'est mesuré, ni pour la sonde ni pour les classifieurs. »

Section 8, point 2, texte corrigé : « Que les sondes sont plus robustes que les classifieurs face au contenu seul : sur attaques rejouées et à calibration égale, les taux sont proches (p. 7-8). La pièce ne dit rien du coût d'évasion, dans un sens ni dans l'autre. »

### C — majeur — origine des attaques et position de la sonde non établies (section 2 du rapport)

Texte actuel : « La sonde lit le modèle qui génère » ; et, section 0, « lecture interne du modèle protégé ».

Pour le jeu statique, ni l'un ni l'autre n'est établi (section 2 ci-dessus, limites 1 et 2). Pour le système de production, en revanche, la sonde lit bien le modèle qui génère : « Claude Sonnet 4.5. As such, the probe uses activations from that model. » (p. 9). Texte corrigé :

> « Dans le système de production, la sonde lit le modèle qui génère (p. 9). Dans l'analyse statique (p. 7-8), la sonde est entraînée sur un modèle qu'aucune campagne décrite ne protège ; l'article ne dit pas quel modèle a produit les 7 000 échanges, ni contre quel système ils ont été écrits. La position de la sonde (modèle qui génère, ou modèle qui relit) et le caractère adapté ou transféré des attaques contre les deux classifieurs de comparaison restent indéterminés. »

### D — majeur — le verdict de tête dépend d'une lecture que les textes ne rendent pas la plus naturelle (section 0 et section 9)

Le rapport annonce « occupé en partie » en tête et renvoie l'autre lecture à une réserve. Les lignes du programme, de N-013 et de N-068 désignent d'abord un juge génératif (section 1 ci-dessus). Texte corrigé de la tête :

> « HC4 : « non trouvé dans les pièces lues » si « juge » veut dire juge génératif (lecture la plus naturelle des lignes 102 à 106 et 194 du programme, de N-013 et de N-068) ; « occupé en partie » si « juge » couvre tout modèle qui lit le texte, classifieur affiné compris — et alors sur le seul axe « taux de succès », en boîte noire, par transfert statique, pour une sonde de contenu nuisible (2601.04603, p. 7-9). La lecture se tranche par décision, pas par le lecteur. »

De même, dans la table de synthèse, la composante (d) de 2601.04603 doit porter les deux valeurs : « voisin très proche (juge génératif) ; occupée en partie (lecture large) ».

### E — majeur — 2502.19537, point N3 : ce n'est pas le coût de déplacement d'un juge (section 5 du rapport, composantes (a), (c), (e))

Trois défauts :
1. Le coût chiffré est celui du réglage fin du modèle surveillé ; le filtre est appliqué après coup. Les auteurs décrivent un filtre passif : « we allow LG to censor the entire output if it detects harmfulness whereas AMD still produces a response » (p. 7).
2. Le rapport écrit (composante (e)) : « déplacer ce juge a demandé un réglage fin (de 100 à 5 000 exemples) ». Le filtre n'est mesuré qu'à 5 000 exemples (tableau 8, « fine-tuned on 5000 data points », p. 8). La courbe par nombre d'exemples (tableaux 16 et 17, p. 37) n'a que trois lignes de défense, dont aucune n'est ce filtre. Le « 100 » vaut sans défense : « Note that fine-tuning on as few as 100 comromises model safety. » (p. 36).
3. Le mécanisme « trompé par le préfixe de refus » est une hypothèse des auteurs, et le tableau 8 la contredit en partie : « NOICE has a higher ASR against LG than other attacks, likely because LG is deceived by the refusal prefix into thinking that the entire response is harmless. » (p. 7). Or, sous ce filtre (auteurs, tableau 8, p. 8) :
   - sur Mistral, l'attaque dite implicite garde 0,74 contre 0,37 pour NOICE ; NOICE y perd 44 % de son taux (calcul), plus que toute autre cible ;
   - l'attaque par données nuisibles, sans aucune ruse, garde 0,82, 0,47 et 0,58 : le filtre laisse passer beaucoup sans être « trompé ».
   De plus, le succès est noté par un autre juge, non attaqué (« harmfulness of the responses using GPT-4o (OpenAI et al., 2024) as a judge », p. 7).

Textes corrigés :
- composante (a) : « **voisin** : coût d'attaque par réglage fin du modèle surveillé (exemples, dollars, temps de calcul) ; un filtre de sortie est appliqué après coup, à 5 000 exemples seulement ; aucun coût propre au filtre » ;
- composante (c) : « **voisin** : filtre de sortie passif (Llama Guard) ; l'explication par le préfixe de refus est une hypothèse des auteurs, contredite sur Mistral par leur tableau 8 » ;
- composante (e) : « **ne tranche pas** : le filtre laisse passer de 47 à 82 % des sorties d'un modèle réglé sur données ouvertement nuisibles (tableau 8) ; c'est un indice de faiblesse du filtre, pas une mesure du coût de son déplacement ».

La table de synthèse (section 6 du rapport) se corrige de même : 2502.19537, composante (a), « voisin ».

### F — mineur — PAIR, incohérence 2 et section 8, point 6 : le facteur 250 se retrouve

Texte actuel : « Aucun de ces rapports ne donne « 250 » » ; « il ne se retrouve pas dans les tableaux ». Voir section 3 ci-dessus. Texte corrigé :

> « Le facteur « 250-fold » (p. 2) se reconstruit comme 5 120 / 20 = 256 (calcul) : budget de GCG du tableau 8 (AdvBench, p. 15) divisé par le « twenty » nominal du titre. Il ne correspond ni au budget de GCG du texte principal (256 000 requêtes, p. 6) ni aux requêtes par succès du tableau 2. À ne pas citer comme un écart mesuré. »

### G — mineur — PAIR, « requêtes par succès » : les échecs ne sont pas comptés

À ajouter au point P1 et à la section 8, point 5 : le nombre attendu de requêtes par succès, échecs compris, va de 22 (Vicuna) à 2 924 (Claude-1) (calcul, section 3 ci-dessus). C'est ce chiffre, et non « 10 à 56 », qui approche un coût d'attaque.

### H — mineur — juges « de mesure (non attaqués) » : ils sont dans la boucle

Points G6 et P6 du rapport. Texte corrigé : « juges de mesure, placés dans la boucle d'attaque (critère d'arrêt de PAIR, p. 4 ; note des gabarits de GPTFuzzer, p. 12), non visés comme moniteurs ; leurs faux positifs comptent comme des succès ». Ajouter aux incohérences de PAIR celle du « lowest FPR » (section 3 ci-dessus).

### I — mineur — 2601.04603, point A1 : les 27 heures ne portent pas sur les 13 vulnérabilités

Le PDF : « four jailbreaks were capable of answering all target queries at half the detail of a model without safeguards, with an average discovery time of 27 self-reported hours » (p. 4). La moyenne porte sur quatre attaques universelles. La figure 4 (p. 14, image) donne, pour les vulnérabilités à haut risque : temps moyen d'environ 30, 57, 33 et 30 heures ; temps minimal d'environ 5, 15, 12 et 30 heures, pour les quatre systèmes dans l'ordre (figure). Le 33 est imprimé : « the mean discovery time for high-risk vulnerabilities was 33 hours » (p. 5). Pour le classifieur d'échange, (100 + 15) / 2 = 57,5 (calcul), conforme à la figure.

Texte corrigé de A1 : « 695 000 requêtes ; 13 vulnérabilités à haut risque ; quatre attaques universelles, découvertes en 27 heures déclarées en moyenne ; temps moyen de découverte d'une vulnérabilité à haut risque d'environ 30 heures et temps minimal d'environ 5 heures (figure 4, p. 14) ».

Les auteurs préviennent que ces temps dépendent du volume d'attaque : « The other metrics we consider are expected to have a much stronger dependence on the volume of red-teaming, which varies across systems. » (p. 14), et « Since different systems received varying levels of red-teaming effort, we primarily report the vulnerability discovery rate. » (p. 4). Cela renforce la réserve 2 du rapport.

### J — mineur — 2601.04603, incohérence d'unité non relevée (figure 5, p. 16)

L'axe du taux de succès d'attaque, étiqueté en pourcentage, de la figure 5 est gradué de 0 à 0,1 (panneau a) et de 0 à 0,05 (panneau b) ; la configuration retenue y vaut environ 0,013 à 0,014 (figure), alors que la même configuration vaut environ 1,3 à 1,4 % aux figures 2b et 2c (p. 7). La figure 5 est en fraction sous une étiquette en pourcentage. Sans effet sur le verdict.

### K — mineur — 2502.19537, incohérence 3 du rapport : formulation

La phrase complète est : « We then query both the original and the attacked model on the harmful HeX-Phi dataset. Table 4 shows ASRs for the attacked and original models. » (p. 5). Elle suit un passage sur les deux modèles attaqués ; le tableau 4 montre bien un modèle d'origine et un modèle attaqué (Claude-3-Haiku). Le défaut est seulement que les chiffres de GPT-4o sont au tableau 3, non cité là. Texte corrigé : « le renvoi au tableau 4 (p. 5) ne couvre que Claude-3-Haiku ; les chiffres de GPT-4o sont au tableau 3 ».

### L — mineur — voisins non lus : liste incomplète

À ajouter, nommés dans 2601.04603 :
- Kantamneni et collègues 2025, « Are sparse autoencoders useful? A case study in sparse probing » (2502.16681), p. 10 et 12 (« Others build classifiers using sparse auto-encoder features », p. 10) ;
- Bricken et collègues 2024, classifieurs sur traits de dictionnaire, p. 10 et 11 ;
- les deux documents d'OpenAI de 2025 sur une classification en deux étages, p. 10.

La priorité donnée par le lecteur à McKenzie et collègues, à Cunningham et collègues (« Cost-effective constitutional classifiers via representation re-use », p. 12) et à Hua et collègues est juste.

### M — mineur — système de production : ce que la structure permet de dire (section 11 du rapport, note pour HC2)

Le rapport dit que l'évasion de la sonde seule n'est pas isolée. C'est exact, mais la structure dit davantage : « A lightweight linear probe monitors all exchanges during generation. When the probe score exceeds a threshold, the exchange is escalated to a second-stage external classifier. » (p. 9), et « The first-layer probe escalated approximately 5.5% of traffic to the second-stage classifier. » (p. 9). Pour un échange non escaladé, la sonde décide seule ; pour un échange escaladé, elle pèse un peu plus de la moitié du score (poids 0,55 et 0,45, lus sur le PDF, non contrôlés par programme). Toute attaque réussie a donc franchi la sonde, seule ou dans l'ensemble. Or : « Only one high-risk vulnerability was discovered » et « The discovery time for this attack was 30 hours, representing the highest minimum vulnerability discovery time observed. » (p. 9).

C'est un point de coût publié — une attaque, 30 heures, environ 198 000 tentatives au total — pour franchir par le contenu seul, en boîte noire et en s'adaptant, un système où une sonde lue sur le modèle qui génère tient la première porte. Il ne sépare pas la sonde du classifieur, et l'auteur du contenu adverse est un utilisateur externe.

---

## 5. Point 4 — phrase publique, voisins, note pour HC2

**Ce qu'une phrase publique ne doit pas affirmer** : les sept points du rapport tiennent, avec les corrections B (point 2) et F (point 6). À ajouter :
8. Que le coût d'attaque par réglage fin de 2502.19537 (85 dollars, 1 000 ou 5 000 exemples) est le coût de déplacement d'un juge (constat E).
9. Que l'écart 1,4 % contre 1,1 % de 2601.04603 est un écart établi, dans un sens ou dans l'autre (pas d'intervalle ; origine des attaques inconnue).
10. Que le contenu seul ne franchit pas une sonde lue sur le modèle qui génère : le système de production de 2601.04603 a été franchi une fois en boîte noire (p. 9). La lettre restreinte par N-068 (sonde d'intention ou d'action de l'agent auteur, à taux de faux positifs fixé) n'est pas touchée par cette pièce.
11. Que « plusieurs ordres de grandeur » est observé : aucune des quatre pièces ne mesure de rapport de coûts entre une sonde et un juge. Le seul « several orders of magnitude » imprimé porte sur le calcul du défenseur : « The probe is thus several orders of magnitude cheaper than a small external classifier » (p. 7).

**Voisins non lus** : liste du rapport juste aux pages contrôlées par mots (p. 10, 12, 13 de 2601.04603 ; p. 11 de PAIR ; p. 11 et 13 de 2502.19537), complétée par le constat L.

**Note pour HC2** : elle tient, sans verdict, comme il se doit. Deux précisions à y porter : le constat M (la sonde tient la première porte du système de production) et le constat C (dans l'analyse statique, la position de la sonde n'est pas établie ; elle peut être une sonde « du lecteur »). La remarque sur le taux de signalement des requêtes bénignes est exacte : « Moreover, we found that the flag rate on benign scientific requests was higher for the probe. » (p. 8).

---

## 6. Composantes dites « non trouvées » : recherche active

J'ai cherché dans le texte complet des quatre PDF (mots : sonde, activation, lecture interne, gradient, boîte blanche, adaptatif, détecteur, filtre, modération, coût, budget, requêtes), puis dans les annexes.
- Attaque dirigée contre une sonde, ou optimisée contre son score : rien dans les quatre pièces. Dans 2601.04603, le mot de gradient ne désigne que l'entraînement de la sonde (p. 2, 6, 16), et l'« obfuscation » des p. 2 à 4 est celle du texte de sortie, pas celle des activations.
- Coût d'évasion séparé pour la sonde et pour un lecteur de texte : rien.
- Juge génératif attaqué par la rhétorique en tant que moniteur : rien. Le seul juge optimisé est celui de la boucle de PAIR, dans le sens inverse (obtenir le verdict « jailbreak »).
- Régimes « lecture des activations ou des poids » et « écriture dans les poids » appliqués à un moniteur : rien. GCG (boîte blanche) vise le modèle ; 2502.19537 règle le modèle surveillé.
- Sonde qui lit l'intention ou l'action d'un agent auteur : rien.

Le « non trouvé » du lecteur sur ces composantes est confirmé, dans les limites de mon étendue de lecture (en-tête).

---

## 7. Jugement de profondeur

- **Ce qui est solide.** Le journal déclare les quatre PDF lus en entier, figures comprises. Les chiffres que j'ai recoupés sont tous exacts ; les valeurs lues sur les figures 2 et 3 sont justes ; les 79 citations passent un second script ; les réserves R4 (poids optimisé sur le jeu de test, campagnes non comparables) sont bien vues.
- **Ce qui est mince.** La lecture a duré environ douze minutes pour 114 pages, coupée par un redémarrage (journal : 23:21 à 23:33 UTC). Les défauts trouvés sont des défauts de lecture critique, pas de transcription : un coût déduit d'un taux (B), une position de sonde affirmée sans appui pour le jeu statique (C), un coût de réglage fin rangé « côté juge » (E), une incohérence annoncée qui se résout par un calcul simple (F), et trois incohérences internes non vues (figure 5 de 2601.04603 ; « lowest FPR » de PAIR ; tableau 8 de 2502.19537 contre l'explication des auteurs).
- **Résultat trop propre (R4).** Le rapport livre « 79 citations, 0 échec » alors qu'une citation de son texte est inexacte : le contrôle porte sur le JSON, pas sur le texte du rapport. Tout rapport du compte 2 gagnerait à extraire ses guillemets par programme et à les confronter à son JSON.
- **Ma propre limite.** Je n'ai relu ligne à ligne que les pages citées à l'appui et les annexes de 2601.04603 ; le reste par mots. Les figures 5 et 9 de GPTFuzzer ne sont pas revues sur l'image.

---

## 8. Récapitulatif des constats

| lettre | gravité | objet | page |
|---|---|---|---|
| A | majeur | citation inexacte (ligne A3) | 2601.04603, p. 5 |
| B | majeur | coût déduit d'un taux de succès statique | 2601.04603, p. 7-8 |
| C | majeur | origine des attaques et position de la sonde non établies | 2601.04603, p. 5, 7, 8, 9 |
| D | majeur | verdict de tête sous une seule lecture de « juge » | programme l. 102-106, 194 ; N-013 ; N-068 |
| E | majeur | N3 rangé à tort « côté juge » ; mécanisme hypothétique | 2502.19537, p. 7, 8, 36, 37 |
| F | mineur | « 250-fold » se reconstruit (5 120 / 20) | 2310.08419, p. 2, 6, 15 |
| G | mineur | requêtes par succès sans les échecs | 2310.08419, p. 5, 6 |
| H | mineur | juges dans la boucle ; « lowest FPR » contredit | 2310.08419, p. 4, 5 ; 2309.10253, p. 12 |
| I | mineur | 27 heures : quatre attaques universelles seulement | 2601.04603, p. 4, 14 |
| J | mineur | unité de la figure 5 | 2601.04603, p. 16 |
| K | mineur | formulation de l'incohérence 3 | 2502.19537, p. 5 |
| L | mineur | voisins non lus à compléter ; casse de deux titres | 2601.04603, p. 10-12 |
| M | mineur | la sonde tient la première porte du système de production | 2601.04603, p. 9 |

Aucun constat bloquant. Verdict sur le rapport : **« tient avec corrections »**.
