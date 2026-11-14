# Contre-lecture 1 du texte gelé v1 (volet A et tranche B-α) — rapport du contre-lecteur, recopié tel quel

Contre-lecteur : sous-agent neuf, lancé le 2026-11-14 vers 09:48 UTC par la session autrice avec une surcharge de modèle
(« modèle B ») ; il ne l'a pas écrit. Brouillon relu : `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v1.md`,
`4ac7b556ad4519790216ed00fc7ddedcbd23393bc5d53ac0facdc6690c940267` (commit `11f66985`). Rapport rendu vers 09:55 UTC.
Recopié sans modification de fond (seule l'indentation du relais a été retirée).

---

## 1) Empreintes vérifiées

| pièce | résultat |
|---|---|
| texte contre-lu `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v1.md` | oui, `4ac7b556…0267` |
| `plan-et-devis-v1.md`, `plan-et-devis-v2.md` | oui, `bc20a12a…`, `4f653490…` (celles du tableau du texte) |
| `causal_lens_qwen3-8b.json`, `reads_at_firings_qwen3-8b.json`, `scripts-checks-causal_lens.py.txt` (et `fit_bench_h100_2026-10-28.log`) | oui, `sha256sum -c` : quatre « OK » |
| `docs-findings.md` (par `git show refs/remotes/origin/main:…`) | oui, `8814874b…` |
| `facts_true_false.csv` | oui, `151b6163…`, commit du clone `5455d8a3…` |
| clone `nl` | commit `849bfe16…`, conforme |

Aucun fichier modifié, aucun appel réseau ni de modèle, code voisin non exécuté, aucun chemin interdit ouvert, aucun refus de permission rencontré.

## 2) Verdict

**Scellable après corrections** : la tranche B-α demande des corrections légères, le volet A a trois points bloquants (remarques 1 à 3), dont un arrêt presque certain par construction. Une version 2 est à contre-lire de nouveau.

## 3) Remarques

### Bloquantes (volet A)

**1. § 3.1, § 4.1, § 7 — la garde « position < 16 » arrête le volet A par construction.**
- Constat : avec un seul tour d'utilisateur, le préfixe du gabarit de Qwen3 fait environ 3 jetons (estimation, tokeniseur non chargé). Il faut donc environ 14 jetons de contenu pour que le dernier soit en position ≥ 16.
- Dans `facts_true_false.csv`, compté en mots et ponctuation (approximation) : médiane 11 (vrais) et 10 (faux) ; 77 % des vrais et 82 % des faux ont moins de 14 unités.
- C3 perdrait donc la grande majorité de ses exemples, bien au-delà de 5 %, ce qui arrête tout le volet A. C1 est exposé aussi (comportements courts).
- L'écart est en outre lié à la classe (les faux sont plus courts) : ce qui resterait de C3 serait confondu avec la longueur.
- Même cause, second effet : dans C2, le mot planté tombe vers la position 8, donc avant 16. Les lentilles ne portent aucune tangente avant 16 (`transport.py`, positions valides `[16, T−1)`). A1 demande à la lentille S de retrouver un jeton situé là où elle n'a jamais été ajustée ; le texte ne garde que la position lue, pas la position source.
- Correction : un préambule neutre identique pour toutes les classes, d'au moins 16 jetons, écrit dans le texte. Compter sur processeur, avec le seul tokeniseur, les positions lues et sources par contraste, et écrire ces comptes avant scellement. Sinon retirer C3 et écrire la réserve « source avant 16 » pour A1.

**2. § 3.1 — la lecture S `_z` d'un poids de sonde n'est pas définie.**
- Constat : le texte renvoie à `layer_logit_stats`, qui centre-réduit des logits de sortie (lecture R). Le pendant côté S est `s_tops`, qui porte sur des « covecteurs unitaires ».
- Rien n'est fixé sur : (a) le retour de `w` de l'espace centré-réduit vers le flux brut (`w/σ`) ; (b) la norme de `w` — or le classement `_z` en dépend, puisque `(c·s_v − μ_v)/σ_v` change d'ordre avec `c` ; (c) les lignes qui donnent `μ_v, σ_v` (portes, montées, les deux) ; (d) la convention de signe (dans le code, le z du pôle − est l'opposé du z du pôle +) ; (e) les statistiques du témoin « sans lentille » en `_z`.
- Chaque choix change les rangs de A1, A2 et A3 : liberté entière à la lecture.
- Correction : écrire la formule complète (`w` ramené au flux brut puis normé à 1 ; `μ, σ` sur un ensemble de lignes nommé ; z(−w) = −z(w) ; mêmes statistiques recalculées sans `K_L` pour le témoin) et corriger le renvoi de fonction.

**3. § 3.3, § 4.1 — A2 est peut-être inatteignable, et A3 mal posée quand le sac de jetons ne chute pas.**
- A2 : en C1 l'apprentissage compte environ 70 invites par classe. Un jeton présent dans 5 invites d'une classe et 0 de l'autre donne p ≈ 0,06 au test de Fisher bilatéral, avant toute correction. L'ensemble « associé » sera probablement de quelques jetons par signe. « Précision à 20 ≥ 0,25 » exige 5 jetons associés parmi 20 : impossible si l'ensemble en compte moins de 5.
- Par les égalités à 0, la clause « sans lentille ≥ S à chaque couche sur A1 et A2 » pousse alors vers « n'apporte rien ».
- A3 : « chute ≥ la moitié de celle du sac de jetons » est vide si cette chute est nulle ou négative. Les « déciles de fréquence » sont dégénérés pour des jetons absents des invites, cas probable des premiers jetons d'une lecture sur environ 100 000 jetons gardés.
- Correction : calculer avant scellement, sur le texte seul, la taille de l'ensemble associé par découpe et par signe, avec une issue « sans objet » sous un minimum. Fixer un plancher de chute du sac de jetons (par exemple 0,02 d'AUROC) sous lequel A3 est « sans objet ». Dire comment on apparie un jeton de fréquence nulle.

### À corriger

**4. § 4.2, § 9 point 3 — écart non déclaré sur B-3 « non reproduit ».** Le plan v1 dit « écart ≤ 0 sur plus de la moitié de ces couches », soit au moins 7 sur 12. Le texte écrit « au moins 6 des 12 ». Le § 9 affirme que « le plan ne le disait pas », ce qui est faux pour B-3. Correction : revenir à 7, ou déclarer l'écart.

**5. § 4.2 — « pilotage sans effet » a disparu de « chaîne en défaut ».** Le plan v2 § 3.2 le cite. Le texte ne le garde que dans l'audit « trop beau ». Correction : ajouter un critère chiffré (norme de la cible « steer 1x » non nulle pour au moins N pôles par couche) ou déclarer que le cas sain de la lentille des logits le remplace.

**6. § 6.1, § 6.5 — le cas sain du volet A est conditionnel et ne couvre pas la lentille S.**
- « Chaîne en défaut » dépend du pôle « owl », qui n'est joué que si « tout échoue », terme non défini. La vérification dépend donc du résultat.
- Elle ne porte que sur la lecture R d'une écriture, alors que tous les critères reposent sur la lecture S `_z` d'un covecteur.
- Le plan v1 § 3.4 citait « la lecture R et S » : le S a été abandonné sans déclaration.
- Correction : cas sain joué toujours et avant toute lecture ; y ajouter un cas S du README (`L1 n11672 −` : « German, Germany, 德国 ») ; définir la famille « owl » par une liste de chaînes.

**7. § 3.2, § 5.1 — doublons et étiquette contradictoire dans les faits.**
- Constat : 13 énoncés répétés ; 298 vrais distincts sur 306, 301 faux distincts sur 306 ; « The Nile River is the longest river in the world. » porte les deux étiquettes.
- « C3 par ligne » laisse le même énoncé des deux côtés de la découpe. « Les 306 énoncés vrais » de C2 n'en sont que 298.
- Correction : dédoublonner par texte, grouper par texte, retirer ou trancher l'énoncé contradictoire, corriger les effectifs (612, 612, 612).

**8. § 3.2, § 5.1 — fuite d'énoncés dans le jeu hors distribution de C2.** Il reprend les 306 énoncés, y compris ceux de l'apprentissage de la découpe. Correction : n'évaluer hors distribution que les énoncés de test de la découpe.

**9. § 3.2, § 9 point 1 — écart au gabarit publié non déclaré.** Dans `utils.py` (lignes 41 à 46), la consigne est sous la marque d'utilisateur et l'énoncé, tronqué, vient après la marque d'assistant. Le texte met consigne et énoncé entier dans un seul tour d'utilisateur. Le § 9 ne déclare que le mot « untruthful ». Correction : déclarer l'écart.

**10. § 3.2, § 4.1 — ensemble P et témoins de A1.**
- P est formé de morceaux de formes hors contexte, dont des sous-mots génériques possibles (« ful », « truth »). « Moins de trois caractères » ne dit pas si l'espace compte. Rien ne garantit que P ∩ `catalog.kept` soit non vide.
- Les témoins « étiquettes permutées » et « direction de C3 » n'ont aucun rôle dans la décision. Seules comptent les 100 directions aléatoires, témoin presque vide : chance d'environ 0,1 % qu'un jeton de P tombe dans un top 10 sur 100 000.
- Correction : P = les identifiants qui diffèrent entre les deux consignes tokenisées en contexte, listés dans le texte. Arrêt si P ∩ gardés est vide. « Retrouvée » exige aussi qu'aucun des deux autres témoins ne place un jeton de P dans ses 10 premiers aux mêmes couches.

**11. § 4.1, § 6.2 — A-ii : plafond et asymétrie.**
- « Apporte » s'obtient s'il existe un k parmi trois, à 2 couches sur 4. « N'apporte rien » exige tout k, toute couche, en distribution et hors distribution.
- Sur C2 (fuite d'un mot) et sans doute C1, sonde et neurones seront près de 1,00 : « apporte » serait prononcé au plafond, sans contenu.
- Le sac de jetons n'entre dans aucune décision, alors que c'est lui qui dit si les neurones ajoutent quelque chose au texte.
- « À chaque couche » dans « n'apporte rien » est un durcissement du plan non déclaré. Le cas de C3 (pas de hors distribution) n'est pas couvert pour « n'apporte rien ».
- Correction : clause de plafond (« sans objet » si la sonde ou le sac de jetons atteint 0,99) ; comparer aussi au sac de jetons ; déclarer l'écart ; préciser C3.

**12. § 3.6, § 4.2 — nombre de pôles par couche.** `score` écarte les pôles d'effet nul et, pour l'ablation, ceux sans contexte. La référence n'a que 59, 57, 62 et 61 pôles aux couches 1 à 4 en pilotage. Le texte dit « 64 pôles » sans minimum. Correction : rapporter n par couche et par cible ; fixer un minimum sous lequel la couche est « non lisible ».

**13. Préambule, § 5.2, § 7 — retouches du code voisin non déclarées.**
- `load_lens("J")` lit une seule entrée par modèle : les trois lentilles de Llama exigent une retouche de `lenses.py`, absente du préambule (qui ne cite que le correctif de `06_activations.py`).
- La graine de neurones 1 de l'audit n'est pas exposée : `sample_neurons` et `score` appellent `random_neurons` avec la graine 0 par défaut. Sans retouche des deux endroits, `score` ne reconnaît plus les tirages.
- Correction : les déclarer comme correctifs datés, contre-lus avant usage.

**14. § 4.2, § 7 — gardes de B-α.**
- « Témoin hors de ±0,10 » ne dit pas pour quelle cible (une ou quatre).
- Le cas sain interne ne valide que la lentille des logits. Un décalage d'indice de couche ou une autre convention dans les fichiers de Neuronpedia passerait pour un « non reproduit ».
- Le § 7 (R5) n'essaie ni ces gardes ni le code des verdicts sur un cas sain et un artefact.
- La garde de B0 compare l'estimateur des lentilles à la force brute, alors que B-α n'ajuste aucune lentille. « Supérieur à celui du Qwen3 miniature » n'a pas de tolérance.
- Correction : nommer les cibles ; ajouter un cas sain de la lentille R publique (par exemple `r_med` ≥ 0,85 aux couches 28 à 30 ; publié à la même profondeur : 0,98 à 0,99) ; passer le code des verdicts sur le fichier publié de Qwen3-8B converti (attendu : tout « reproduit ») et sur un fichier altéré ; tester sur le Llama miniature les crochets de pilotage et d'ablation ; donner une tolérance chiffrée.

**15. § 7 — garde d'empreinte non testable pour plusieurs entrées.** Aucune empreinte ni révision n'est écrite pour JailbreakBench, AdvBench, le catalogue publié (`catalog.kept`), les deux modèles, les corpus d'activations de Llama (taille, révision). Correction : les écrire, ou prévoir un addendum scellé avant la première passe.

**16. § 3.1, § 3.3 — libertés restantes.**
- Grille de la pénalité L2 non fixée (140 à 430 exemples pour 4 096 traits : la direction de `w` en dépend).
- Plis internes non groupés.
- Retrait de jetons de A3 : sur les identifiants ou après décodage et nouvelle tokenisation ? Que devient un exemple qui repasse sous la position 16 ?
- Ensemble de jetons du Spearman de A2 non dit.
- « Non retrouvée : à aucune couche » : au sens de la règle 3 sur 5, ou d'aucune découpe ?
- Rang de A1 moyenné sur 5 découpes : dominé par une valeur extrême ; préférer la médiane.

**17. § 11 — « sous-agent d'un autre modèle que l'autrice ».** Je tourne sous Claude Fable 5.2. L'attribution de la session autrice indique le même modèle. Si c'est le cas, cette contre-lecture ne satisfait pas la clause « autre modèle ». À constater tel quel au § 11, ou faire refaire par un autre modèle.

### Mineures

**18. § 4.2 — le témoin de B-2 est la clause la plus fragile.** `control_med` dans ±0,05 à chacune des 28 couches. Sur la référence, l'écart-type entre couches du témoin de la lentille R vaut 0,0195 (couches 0 à 17) et le maximum 0,038. Sous une loi normale, cela fait de l'ordre de 10 à 15 % de chances de manquer « reproduit » par ce seul bruit. Proposition : « au plus une couche hors de ±0,05, aucune hors de ±0,10 ».

**19. § 3.6 — « environ 0,8 fois la valeur publiée à la même profondeur relative » est inexact.** Les bandes 8–15, 16–23, 24–27 sont celles de Qwen sans conversion. À profondeur convertie, les seuils valent 0,53 à 0,70 fois le publié (bande 8–15), 0,62 à 0,76 (16–23), 0,86 à 0,88 (24–27). Ce n'est pas un défaut au sens du point (c), mais la phrase est à corriger.

**20. § 6.4 — B-7 ne distingue pas la lentille R.** Sur la référence, la cible « ablate win » donne presque la même chose pour les trois lentilles (couche 26 : logits 0,53, J 0,51, R 0,54). La conclusion « pour un moniteur » vaut pour toute lentille ; l'écrire.

**21. § 2 — R1 pour A-i.** « Aucune direction prédite » : écrire au moins l'issue modale prédite (« n'apporte rien ou indéterminé », 0,7).

**22. Forme.** Les titres (« 1. Hypothèses », « 3. Métriques », « 4. Seuils ») diffèrent de ceux du gabarit. Je n'ai pas lu le validateur ; à vérifier s'il compare les titres exacts.

**23. § 3.4 — intervalles.** Les jeux de test des 5 découpes se recouvrent : le rééchantillonnage « stratifié par découpe » ne donne pas un intervalle sur des exemples indépendants. À dire.

**24. § 10 — renvoi de lignes.** « 373 à 377 » : les défauts sont aux lignes 374 à 377.

### (c) Seuils appliqués à la référence publiée
Avec quatre conversions (interpolation, plancher, plafond, sortie de couche), la référence passe tous les critères « reproduit » et ne déclenche aucun « non reproduit » ni « chaîne en défaut ».

| critère | valeur de la référence (plancher) | seuil | passe |
|---|---|---|---|
| B-2 `r_med`, couches 8–15 | minimum 0,567 | 0,40 | oui |
| B-2 `r_med`, couches 16–23 | minimum 0,786 | 0,60 | oui |
| B-2 `r_med`, couches 24–27 | minimum 0,969 | 0,85 | oui |
| B-2 `pass`, couches 8–27 | minimum 0,9375 (60 pôles sur 64, à une couche) | 0,90 | oui, marge de 2 pôles |
| B-2 témoin, couches 0–27 | −0,038 à +0,031 | ±0,05 | oui |
| B-3, couches 4–15 | minimum +0,352 | +0,20 | oui |
| B-7, couches 0–15 | maximum 0,134 à 0,158 selon la conversion | < 0,25 | oui |
| B-7, couches 26–29 | minimum 0,673 | ≥ 0,50 | oui |
| cas sain, lentille des logits, couches 28–30 | 0,935 à 0,957 | ≥ 0,80 | oui |
| témoin, toutes cibles et lentilles | maximum absolu 0,039 | ±0,10 | oui |

### (e) Séparations
- Le § 0 dit explicitement que les sorties ne fixent aucun choix de lecture de P3b : oui.
- Aucun identifiant de modèle de la famille Claude : la seule occurrence est « un modèle de la famille Claude, noté modèle C » (ligne 43), sans identifiant. Les identifiants de session du préambule ne sont pas des identifiants de modèle.

## 4) Chiffres recalculés

| chiffre du texte | valeur recalculée | accord |
|---|---|---|
| B-2 `r_med` R : 0,33 / 0,45 / 0,49 / 0,65 / 0,74 / 0,87 / 0,95 (couches 0, 4, 8, 12, 16, 20, 24) | 0,3260 / 0,4466 / 0,4945 / 0,6535 / 0,7444 / 0,8694 / 0,9452 | oui |
| `pass` ≥ 0,9375 dès la couche 5 | minimum des couches 5 à 35 = 0,9375 (couche 9) ; couches 0 à 4 en dessous | oui |
| témoin −0,038 à +0,031 (pilotage 1×, R) | −0,0384 (couche 9) à +0,0309 (couche 11) | oui |
| B-3 : +0,352 à +0,425, couches 4 à 17 | minimum 0,3519 (couche 6), maximum 0,4250 (couche 15) | oui |
| couche 8 : 0,49 contre 0,12 | 0,4945 contre 0,1222 | oui |
| B-4 : R − J +0,026 à +0,131, couches 4 à 23 (§ 2 : +0,03 à +0,13) | 0,0263 (couche 18) à 0,1309 (couche 7) | oui |
| B-7 : 0,05 / 0,05 / 0,08 / 0,08 / 0,13 / 0,23 / 0,40 / 0,67 / 0,87 (couches 0 à 32 par pas de 4) | 0,0529 / 0,0473 / 0,0803 / 0,0803 / 0,1344 / 0,2316 / 0,4044 / 0,6664 / 0,8686 | oui |
| témoin de B-7 : −0,013 à +0,029 | −0,0125 à +0,0286 | oui |
| lentille des logits 0,94 à 0,96 (couches 31 à 33) | 0,9354 / 0,9426 / 0,9565 | oui |
| 0,9998 à la dernière couche | 0,9998 | oui |
| `read_S` 0,848 / 0,248 / 0,090 / 0,229 / 0,352 (couches 0 à 4) | 0,8481 / 0,2484 / 0,0905 / 0,2292 / 0,3521 ; bien non décroissant | oui |
| stabilité (§ 8) : R 0,04–0,06 (0–18), 0,03 (19–22), 0,02 (23–27), ≤ 0,01 dès 28 ; S 0,00–0,05 et 0,01–0,05 ; 0,89 à 0,99 aux six couches ; « 12 couches » | identique dans `docs-findings.md`, lignes 49 à 62 | oui |
| défauts de `measure` : 32 par couche, 16 contextes, 64 jetons, 8 documents, fenêtre 8, doses 1 et 4, `random.Random(0)`, centile 99 mis en commun | conformes au script et au champ `meta` du fichier | oui |
| consigne de C2 « an honest » / « an untruthful » (`utils.py` lignes 33, 45, 46) | conforme | oui |
| « 306 énoncés vrais », « 306 faux », 612 | 306 et 306 lignes, mais 298 et 301 distincts, un énoncé aux deux étiquettes | écart (remarque 7) |
| `SKIP_FIRST = 16` | `transport.py` ligne 44 ; positions valides `[16, T−1)` | oui |
| 31 % à 53 %, 461 et 64 documents | non revérifiés : source hors de ma liste ; le texte les marque « niveau citation » | non vérifié |

Aucun écart d'arrondi sur les chiffres publiés des §§ 4.2, 8 et 10.
