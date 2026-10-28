# Antériorité — comment le champ mesure « généralise à des familles d'attaque jamais vues » — v1

Lignée conv-audit, 28 octobre 2026. Première des trois recherches d'antériorité lancées sur le « go » de Lazar (12:49
heure de Paris) pour la question élevée (défense universelle co-évolutive). Rendue par un sous-agent neuf de recherche.

**Statut R7 : tout ce qui suit est RAPPORTÉ d'après résumés et pages de dépôt, lu par un sous-agent, rien n'est vérifié sur
PDF empreinté. Aucun chiffre ni aucune formule n'est opposable avant vérification. Les points « à vérifier » sont listés en
fin.** Les noms de protocoles sont des noms propres et sont donnés tels quels, développés à la première occurrence.

## Verdict en quatre lignes

1. **Un « degré d'universalité » existe déjà sous un autre nom** : la robustesse aux attaques non prévues (*Unforeseen
   Attack Robustness*, UAR, Kang, Sun, Hendrycks, Brown, Steinhardt, 2019). Ne pas inventer de nom : s'aligner dessus.
2. **Il manquait une pièce à notre « degré k »** : la **normalisation par famille** par la meilleure performance atteignable
   en s'entraînant *contre* cette famille. Sans elle, k compte les familles faciles et gonfle.
3. **Notre protocole de rotation a un nom** : sortie d'un domaine à la fois (*leave-one-dataset-out / leave-one-category-out*,
   LODO / LOCO), emprunté à la généralisation entre domaines ; appliqué en 2026 à des classifieurs d'invites malveillantes,
   notre terrain exact — avec un diagnostic de raccourci (rétention des coefficients).
4. **Notre mode tenu à l'écart (N-054) a un précédent reconnu** : les familles « inconnues » tenues par l'organisateur,
   hors des mains du concepteur, dans la série ASVspoof (détection de parole truquée, depuis 2015).

## Les protocoles (RAPPORTÉ)

| protocole | origine | ce qu'il mesure | défaut connu |
|---|---|---|---|
| **UAR / mUAR**, banc ImageNet-UA | Kang, Sun, Hendrycks, Brown, Steinhardt, arXiv 1908.08016, 2019 | précision sous des familles **explicitement exclues de l'entraînement**, **normalisée par famille** par la meilleure précision atteignable en s'entraînant contre cette famille | pas exhaustif (dit par les auteurs) ; la normalisation dépend d'une défense de référence |
| union / pire cas sur modèles de perturbation | Tramèr et Boneh 2019 ; Maini, Wong, Kolter, arXiv 1909.04068, 2020 | **minimum** (pas moyenne) sur un ensemble **connu** | mesure la largeur sur l'ensemble visé, pas l'inédit |
| conditions connues / inconnues | série ASVspoof, arXiv 1904.05441, 2019 (depuis 2015) | détection à point de fonctionnement fixé sur des familles **inconnues**, tenues par l'organisateur | les secrets ne survivent pas à la publication du jeu |
| erreur par espèce d'attaque à point fixé | norme ISO/IEC 30107-3:2023 | une **norme** qui dit : rapporter **par famille**, à taux de fausses alertes fixé, **jamais** le taux d'erreur égal, **jamais** la moyenne | la taxonomie des espèces est toute la mesure |
| **LODO / LOCO** | Fomin, *When Benchmarks Lie*, arXiv 2602.14161, atelier ICLR 2026 — sur classifieurs d'invites malveillantes | famille tenue à l'écart **en rotation** ; **rétention des coefficients** r_j qui signale les traits-raccourcis liés au jeu de données | l'auteur le dit emprunté à la généralisation entre domaines |
| aire sous le temps (AUT) | Pendlebury et al., TESSERACT, arXiv 1807.07838, 2019 | décroissance graduée dans le temps ; contraintes de biais temporel et spatial | dérive ≠ famille inédite |
| ouverture (*openness*), OSCR | Scheirer et al. 2013 ; Vaze et al. ICLR 2022, arXiv 2110.06207 | degré continu d'« inédit » à partir des comptes de classes | Vaze : la compétence en ensemble fermé explique presque tout — confusion de protocole |
| OpenOOD proche / lointain | arXiv 2210.07242, NeurIPS 2022 | distance graduée de l'ensemble inédit | proche / lointain assigné à la main |

**Défenses certifiées** (lissage aléatoire, Cohen et al. ICML 2019, et parentes) : certifient **seulement** une boule de rayon
spécifié. INFÉRÉ, quasi certain : la certification est par définition muette sur les familles inédites (Hayes, CVPRW 2020).

## Critiques à prendre comme contraintes de conception (RAPPORTÉ)

- Athalye et al. 2018 : gradients obscurcis, fausse sécurité.
- Tramèr et al., NeurIPS 2020 : des attaques **adaptatives** cassent des défenses évaluées sur des suites **fixes**.
- Arp et al., USENIX Security 2022 : dix pièges (biais d'échantillonnage, corrélations fallacieuses, erreur du taux de base).
- RobustBench, arXiv 2010.09670 : la standardisation invite au surajustement à un seul modèle de menace.
- **Le cas truqué : KDD'99 / NSL-KDD** (critique de Tavallaee 2009) — un banc qui livrait des attaques inédites au test et
  qui est **quand même** devenu le banc surajusté canonique. C'est l'avertissement direct pour notre banque scellée : une
  fois réutilisée, elle est jouée. (Nos défenses : tâches fraîches N-049, test final lu une fois N-050 — on a maintenant la
  raison citable.)

## Recommandation du sous-agent, que je reprends

**Aucun « degré d'universalité » n'existe en tant que tel.** Aligner notre « degré k » sur **UAR / ImageNet-UA**, et
**emprunter quatre choses plutôt que les inventer** :

- (a) la **normalisation par famille** d'UAR, par une référence entraînée contre cette famille — sinon k compte les faciles ;
- (b) le rapport d'ISO 30107-3 : **à taux de fausses alertes fixé, par famille, jamais le taux d'erreur égal, jamais la
  moyenne**, plus le **maximum sur les familles** ;
- (c) la **rotation** de LODO **plus son diagnostic de rétention** (traits-raccourcis) ;
- (d) les **familles tenues par quelqu'un d'autre que le concepteur**, d'ASVspoof (= N-054).

**Rapporter k ET le vecteur par famille ; une moyenne cache le trou.**

## Portée pour nous

- Ce que je t'ai proposé à 12:42 (« universel au degré k s'il tient son rappel sur k familles non conçues ») était
  **incomplet** : il manquait la normalisation par famille. Corrigé par (a).
- La **rotation** que j'ai décrite à 12:54 (vivier de conception / vivier tenu à l'écart, une famille sortie par tour, un
  mode jamais mis en rotation) **est** LODO plus l'examen unique d'ASVspoof. On l'appelle par son nom.
- **Avertissement direct pour N-044 et N-054** : le papier LODO affirme que des bancs d'invites sont **séparables par le
  seul artefact de source** (quel générateur a produit la famille). Si nos familles tenues à l'écart différent par artefact,
  un moniteur peut « généraliser » en détectant l'artefact, pas le sabotage. À traiter dans la conception des familles et
  dans le bras « fuite textuelle » de N-053.
- La métrique n'est **pas** une zone vierge (UAR 2019). Ce qui pourrait l'être, c'est son **application** à des moniteurs
  internes d'agents sous juge figé — les deux autres recherches (co-évolution ; moniteurs boîte blanche) diront si c'est
  occupé.

## À vérifier sur PDF avant tout préenregistrement (R7)

1. La formule UAR / ATA et la liste des familles de mUAR.
2. Si ISO/IEC 30107-3:2023 **impose** le pire cas par famille (les diapositives ne le disent pas).
3. La formule d'ouverture de Scheirer (deux variantes circulent).
4. Les détails de LODO (papier d'atelier, provenance mince).

Sous-agent : 20 appels d'outils, ≈ 3 minutes. Liens tels que rendus : arxiv.org/abs/1908.08016 ; arxiv.org/abs/1909.04068 ;
arxiv.org/pdf/1904.05441.pdf ; arxiv.org/abs/2602.14161 ; arxiv.org/pdf/1807.07838v4.pdf ; arxiv.org/abs/2110.06207 ;
arxiv.org/pdf/2210.07242 ; proceedings.mlr.press/v97/cohen19c.html ; arxiv.org/pdf/2010.09470 ; arxiv.org/pdf/2010.09670.
