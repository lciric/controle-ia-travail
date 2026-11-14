# Rapport du lecteur — HC4, « taxe de déplacement », sous la lecture « juge = juge génératif », sur la pièce 2609.15994 v1 (v2)

- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Rapport remplacé** : `rapport-HC4-2609.15994-v1.md`, `645f783337fad4b4bc58de716c121c79a94e1390c3131906452ca34a0ff84945` ; son archive : `fichiers-de-travail-HC4-2609.15994-v1.tar`, `c94eb7eb725f811ffdc2f1dbba94ca8b11fc73007094e6d7e0844f9ea7926cf8`. Ces deux fichiers restent intacts (R12).
- **Contre-lecture intégrée** : `contre-lecture-rapport-HC4-2609.15994-v1.md`, `1db31c1993fd4ca19d96fe85093c13690a76a90ecd5ee936fe3971b0c011b0d7` ; son archive : `fichiers-de-travail-contre-lecture-HC4-2609.15994-v1.tar`, `63f63a37b244ef17a2bf0ca4193cf5133000f710050d4ef94ec7d0bd1548f7dc`.
  - Les deux empreintes ont été vérifiées le 2026-11-14 à 06:45:52 UTC (`date -u`), et l'archive a été extraite dans un sous-dossier neuf de mon dossier de travail.
  - Verdict de la contre-lecture : « tient avec corrections », quatre constats majeurs (B à E), neuf mineurs (A, F à M), aucun bloquant, aucun chiffre faux.
- **Heures** (`date -u`) :
  - version 1 : de 06:28:31 à 06:38:08 UTC ;
  - version 2 : reprise à 06:45:52 UTC ; relectures de 06:46 à 06:47 UTC ; rédaction commencée à 06:47:14 UTC. L'heure de fin est celle du scellement (fichier compagnon `.sha256`).
- **Mandat** : verdict d'antériorité sur HC4, au sens où « juge » veut dire **juge génératif** (lecture demandée par Lazar, en attente d'inscription).
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (conforme). Interdits communs `interdits-communs-v2.md` lus en entier en v1 (la consigne y renvoie). Le mandat est plus strict (aucune commande git), je l'ai tenu.
- **Fichiers du dépôt lus, et seulement aux lignes du mandat** :
  - `docs/programme-controle-ia-v2.md`, l. 85-125 et 190-215 ;
  - `docs/decisions/decision-N-013-v1.md`, l. 46-55 ;
  - `docs/decisions/decision-N-068-v1.md`, l. 1-115 ;
  - `docs/sources/lecture-pdf-niveau3/compte-2/rapport-HC4-v2.md`, en entier (`6c368ebb…`, conforme) ;
  - la consigne commune et les interdits communs, en entier ;
  - en v2, en plus : la contre-lecture et son archive, nommées ci-dessus.

  Un `ls` du seul dossier `compte-2/` a vérifié, avant écriture, qu'aucune des deux sorties v2 n'existait. Aucun autre fichier du dépôt n'a été ouvert. Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucun refus, **aucune ouverture fautive**.
- **Pièce** (empreinte vérifiée contre son compagnon `.sha256` avant lecture en v1, puis de nouveau en v2) :

| pièce | empreinte sha256 | pages | étendue lue |
|---|---|---|---|
| `2609.15994v1.pdf` | `1cbd4a419aeb8a5dd00d411a7eee06c122cb33990d2a4ab5a44b8db7017e9f25` | 18 | v1 : p. 1-18 ligne à ligne, annexes et références comprises ; sur l'image, p. 4-7, 12, 15. **En v2, relues ligne à ligne et sur l'image : p. 2, 4, 5, 6, 7, 8, 10, 12, 16** ; relues en texte : p. 1 (tampon), 11, 13. |

- **Citations contrôlées par programme : 127, 0 échec** (`citations-HC4-2609.15994-v2.json`, dans l'archive seulement). Ce sont les 107 citations de la v1, toutes reprises, plus 20 ajouts. Le script `verifier_citations_v2.py` (copie du script v1), lancé par `python3 -I`, cherche chaque citation dans le texte de sa page extrait avec et sans `-layout`, après normalisation (espaces, ligatures, césures, apostrophes, tirets). Il a d'abord été rejoué sur un cas juste (0 échec) et deux cas altérés (2 échecs, attendus).
- **Contrôle des guillemets du rapport** : `controler_guillemets_rapport_v2.py` extrait chaque passage entre guillemets français et le cherche dans le JSON. Tout extrait anglais y figure ; les passages absents sont tous en français (relevé dans l'archive).
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi). Les noms de modèles sont ceux de l'article.

---

## 0. Verdict

| énoncé | sens de « juge » | verdict (table fermée) |
|---|---|---|
| HC4 | **juge génératif** | **« non trouvé dans les pièces lues »** |

- La pièce n'emploie aucun juge génératif comme moniteur, ne mesure aucun coût d'attaque et ne compare jamais une sonde et un juge. Les composantes (c) et (d) ne sont pas occupées.
- **La pièce apporte un contre-indice net mais étroit à la prémisse (e).** En v1, je l'avais dit « fort » ; je retire ce mot (constats B, C, D).
  - Ce qu'il dit : pour une sonde linéaire **à une seule position**, qui lit sur **le modèle qui reçoit l'entrée** une propriété **de l'entrée** (l'intention de l'utilisateur), des fautes de frappe ordinaires placées **près de la position de lecture** dégradent la détection. Il n'y faut aucune requête, aucune optimisation, aucun accès au modèle : environ 3,3 caractères par message. Le taux de vrais positifs à 1 % de faux positifs perd 12,0 points (tableau 2, p. 5).
  - Ce qu'il ne dit pas : ces 12,0 points **ne sont pas un taux d'évasion**. Les fautes touchent tous les exemples de test, bénins compris, et le seuil est recalé sur les données perturbées (constat B). La perte au seuil d'un moniteur déployé n'est pas imprimée.
- Le contre-indice tombe **hors de la lettre restreinte par N-068 (point 8a)**. La sonde ne lit pas l'agent auteur, et la propriété lue est celle de l'entrée. Il tombe dans la catégorie que N-068 déclare déjà publiée (sondes de propriété de l'entrée lues sur le modèle qui reçoit le contenu), et n'y ajoute qu'un coût nul, **affirmé par construction, non mesuré**.
- L'**agrégation sur plusieurs positions** répare presque tout dans le régime localisé : au plus 0,87 point de perte (tableau 3, p. 6). Sous des fautes sur un mot sur deux, l'attention et le maximum perdent encore 3,78 et 3,91 points, et une moyenne sur la séquence perd 16,81 points.
- **Effet sur la colonne « déclarable »** : le verdict sous la lecture « juge génératif » ne change pas. Si HC4 y est déclarable sous cette lecture, elle le reste. Il faut alors porter une réserve de plus avec la prédiction : des fautes ordinaires placées près de la position de lecture dégradent, sans requête ni optimisation, une sonde du modèle lecteur à une seule position. La pièce touche à peine la sonde à agrégation robuste et ne touche pas la sonde de l'agent auteur.

---

## 1. Suite donnée à la contre-lecture

Pour chaque constat, j'ai relu les pages en cause, en texte et sur l'image, avant de décider. Les citations sont toutes dans le JSON v2.

| constat | gravité | décision | où | motif |
|---|---|---|---|---|
| A — régime du seuil : exact, mais mal appuyé | mineur | corrigé | section 3.1 ; section 5, point 13 | Relu p. 16 : le seuil est « re-calibrated per (fold, condition), matching the operational » … « convention of §6 so that the perturbation » … C'est une preuve écrite que la convention de la section 6 est un seuil recalé par condition, plus nette que la légende de la figure 4 (« filled dots: FPR=1% operating point on the perturbed curve. », p. 7), que je garde en appui. Image p. 7 : la sonde linéaire perturbée est bien à 1 % de faux positifs, vers 0,855 (figure). J'ajoute l'ambiguïté de la p. 5 : « malicious samples cross below the fixed-FPR threshold more readily than benign samples cross above it, weighting the failure toward false negatives. » décrit des franchissements dans les deux classes, donc plutôt un seuil fixe. |
| B — les 12,0 points ne sont pas un taux d'évasion | majeur | corrigé | section 0 ; sections 3.1, 6 (b), (e) ; section 8, points 4 et 8 | Relu p. 5 : « We apply a stacked-typing bundle per test sample » ; la condition perturbée est la « same probe on the stacked-typing bundle » (tableau 2). Tous les exemples, bénins compris, sont perturbés. Relu le tableau 8 (p. 12, image) : côté bénin, 95ᵉ centile +0,185 et moyenne +0,021 ; côté malveillant, 5ᵉ centile −0,490 et médiane nulle. La perte mêle donc une montée des scores bénins (qui relève le seuil recalé) et une descente d'une queue de scores malveillants. Un attaquant qui ne fautait que son message ferait face au seuil fixé sur données propres. Ce taux n'est pas imprimé ; si le seuil recalé est plus haut, la perte à seuil fixe serait plus faible (hypothèse, non prouvée). Le constat est porté dans le verdict de tête. |
| C — « aucune connaissance de la sonde » est trop fort | majeur | corrigé | sections 0, 2 ; section 6 (a), (e) ; section 8, point 9 | Relu p. 2, 4, 5. Les auteurs distinguent « localized (clustered near the readout) and distributed (spread across the input) » (p. 2). Le paquet est composé après le relevé des angles au point de lecture : « This survey motivates the perturbation evaluated in §6. » (p. 5). Une faute à 10 jetons de la lecture ne tourne l'activation lue que de 4,7° (« mid-sequence typos measured at d=10 produce modest EOT angles », p. 4), alors que « while terminal substitutions at d=1 bypass spatial attenuation entirely » (p. 4). Le paquet vise le dernier mot (« adjacent-key QWERTY typo on the last alphabetic word ») et la ponctuation finale (p. 5) ; « Restricting to only mid-sequence typos would understate operational fragility » (p. 5). La phrase v1 est remplacée par : aucune requête, aucune optimisation, aucun accès aux poids ; mais **placement près de la position de lecture**, connue des auteurs. Un attaquant qui sait seulement que la sonde lit le dernier jeton le reproduit sans peine ; ce n'est pas un bruit aveugle. |
| D — le juge génératif ne « garde » pas l'intention : il note la lecture des modèles étudiés | majeur | corrigé | section 3.4 ; section 6 (c), (e) | Relu p. 10 (image) : le juge « labeled each pair on two binary criteria » ; le premier est « intent preservation (did the model interpret the perturbed prompt as asking for the same thing?) ». Il note **la lecture du modèle étudié**, sur des paires de réponses ; il ne détecte rien et ne reçoit pas les fautes comme moniteur. Les 94,6 % mesurent donc les trois modèles étudiés selon ce juge. L'échantillon est distinct de celui de la sonde : « We sampled 100 prompts (50 benign from OpenOrca with 80–350 words; 50 malicious from HarmBench across its three subsets) » (p. 10), sans aucun score de sonde. « the probe is the sole failure point » (p. 2) repose sur quatre exemples (tableau 6) et sur cet échantillon non apparié. Mon v1 écrivait qu'« un lecteur génératif lit l'intention à travers les fautes » : retiré. L'opposition « la sonde bouge, le texte est lu de même » reste qualitative. |
| E — tableau 17 : « aggrave » et « l'ordre s'inverse » sont trop forts | majeur | corrigé | section 3.6 ; section 5, point 4 ; section 8, point 6 | Relu p. 16 (image) et p. 6. Les chiffres sont exacts (« No KV-fork (Linear EOT) 77.5% 38.9% −3.5pp » ; « KV-fork (neutral suffix) 81.5% 47.2% −4.5pp »). Mais l'écart d'un point porte sur une moyenne de 7 plis, sans écart type, à seuil recalé par pli et par condition. Le taux perturbé reste plus haut avec le suffixe : 47,2 − 4,5 = 42,7 % contre 38,9 − 3,5 = 35,4 % (calcul). Les auteurs signalent des effets de plancher (« masked at the aggregate by floor effects », p. 16) et attendent une moindre récupération hors distribution (« Out-of-distribution shift (e.g., the LODO setup in Appendix I) is expected to further constrain the recoverable fraction », p. 6). Le régime réparti n'est pas rapporté pour le suffixe. Nouvelle lecture : hors distribution, le suffixe **ne réduit plus** la perte due aux fautes, tout en gardant un taux perturbé plus haut. « L'ordre s'inverse » est retiré : l'entraînement augmenté n'est pas mesuré hors distribution. |
| F — incohérence p. 8 contre tableau 1 : tient ; figure 2 dite trop doucement | mineur | corrigé | section 5, points 1 et 12 | Relu p. 4 et 8 (image). L'incohérence tient : 43 à 56° est la rotation au jeton fauté ; au point de lecture, le tableau 1 va de 3,4° à 26,4° (auteurs). Sur la figure 2, la couche 31, celle de la sonde, est vers 0,18-0,20 à dix jetons (figure) : **au-dessus** de 15 %, contre « All four depth checkpoints fall below 15% of the on-site signal by » (p. 4). Même remarque, plus faible, pour la couche la plus profonde de Qwen3-8B (figure 6, p. 12 : vers 0,18 à dix jetons, figure), contre « falling below 15% of the on-site value within d≈10 tokens at the deepest checkpoint layer » (p. 11). Figure 1 confirmée : Gemma vers 38-39°, Llama vers 58° (figure). |
| G — « un ordre de grandeur » : tient | mineur | corrigé | section 5, point 4 | 3,70 / 0,60 = 6,2 (calcul) : moins d'un ordre de grandeur, et dans la distribution d'entraînement seulement. La fin de phrase v1 (« l'ordre s'inverse ») est retirée (constat E). |
| H — date imprimée et identifiant | mineur | corrigé | section 2 ; section 5, point 14 | Relu p. 1 : « arXiv:2609.15994v1 [cs.CL] 8 Jul 2026 ». Un identifiant en 2609 désigne un dépôt de septembre 2026 ; le tampon imprime le 8 juillet 2026. C'est une réserve de provenance. Venue : un atelier (« Mechanistic Interpretability Workshop »), pas la conférence principale ; dit tel quel. |
| I — voisins : Yu compte aussi pour (c) et (d) ; un voisin manque | mineur | corrigé | section 9 | Relu p. 2, 8, 10. D'après son titre (« Character-level perturbations amplify LLM jailbreak attacks. ») et ce qu'en dit la pièce (sondes de diagnostic), Yu et collègues touchent les deux côtés, modèle génératif et sonde, avec un attaquant qui choisit ses mots. C'est le voisin le plus proche de (b) **et** de la comparaison (d). Statut imprimé : soumission OpenReview (p. 10). Ajouté : Aliakbarzadeh et collègues 2024, « Exploring robustness of multilingual LLMs on real-world noisy » … (p. 8), cité p. 2 (« (Aliakbarzadeh et al., 2024; Zhao et al., 2026) »), côté lecteur de texte. |
| J — refus du modèle : seule mesure d'un lecteur génératif sous les mêmes fautes | mineur | corrigé | section 3.4 ; section 6 (c) | Relu p. 10 (image) : « On malicious pairs we additionally tracked the direction of any refusal flip. » ; 27 bascules sur 294, 12 vers plus de refus, 15 vers la conformité, surtout sous le régime réparti. La décision de refus est la lecture de l'intention par un modèle génératif, sous les mêmes fautes. Je passe donc (c) de « ne touche pas » à **« voisin »**. Sous le régime réparti, le lecteur de texte cède aussi ; l'asymétrie « sonde fragile, lecteur stable » ne vaut que pour le régime localisé. Le seul « cost » de la pièce est le surcoût de la parade (p. 8, 15) et deux affirmations non mesurées (p. 5, 8) : aucun coût d'attaque mesuré, confirmé. |
| K — points 7 et 8 de la section 4 v1 | mineur | corrigé | section 5, points 7 et 8 | Relu p. 16-17. Le « 28 » est expliqué par les auteurs (« (Scam unavailable) », p. 16 ; « perturbation evaluation is unavailable for it due to source repository unavailability at evaluation time. », p. 17) : retiré des incohérences. Reste la fusion annoncée de Gandalf et de Scam contre leurs plis à part et le compte de 29 plis. Source en double : les deux jeux sont bénins seuls ; une fuite ne toucherait que l'exactitude pondérée et le taux de faux positifs de ces plis, pas les taux à 1 % de faux positifs des 7 plis à deux classes. |
| L — coïncidences à garder en réserve (R4) | mineur | corrigé | section 5, point 15 | Relu p. 13, 18, 5. Le tableau 9 donne la même moyenne pour le paquet entier (« full bundle (5-component) 93.84 ± 0.53% ») et pour une seule famille (« 93.84 ± 0.59% »). 85,4 % et −16,8 points reviennent au pli SafeGuard (« SafeGuard 93.5% 85.4% −8.1pp 76.7% −16.8pp ») et aux tableaux 2 et 3. Ajouté en réserve, sans conclure. |
| M — sondes à plusieurs positions : nuance du texte | mineur | corrigé | section 3.2 | Relu p. 6 (image). Mon « au plus 0,87 point » vaut pour les quatre sondes à plusieurs positions (fenêtre des 16 derniers jetons comprise). Le chiffre des auteurs (« every full-sequence multi-position probe loses ≤ 0.5pp ») ne vaut que pour les trois lectures de toute la séquence. Rien de faux ; je le précise. |

**Ce que je ne prends pas tel quel.** Pour B, la contre-lecture conjecture une perte plus faible à seuil fixe. Le sens est probable mais non prouvé : à seuil propre fixé, les faux positifs dépasseraient aussi 1 %. Je l'écris comme hypothèse. Aucune réserve n'est maintenue contre un constat : tous sont justes sur pièces.

---

## 2. Ce que l'article fait

**Venue imprimée.** « Mechanistic Interpretability Workshop » de la « Conference on Machine Learning, Seoul, South Korea, 2026. » (p. 1). Tampon : « arXiv:2609.15994v1 [cs.CL] 8 Jul 2026 » (p. 1), en désaccord avec l'identifiant (constat H). Trois auteurs, une même entreprise. Titre : « Latent Undertow: How Ordinary Typos Break Probes ».

**Question.** Des variations de frappe ordinaires, qui ne changent pas ce que le modèle comprend, déplacent-elles les sondes qui lisent ses activations ? Les auteurs l'énoncent ainsi : « Yet probes that detect malicious prompts by reading the model’s hidden states tell a different story » (p. 1).

**Sonde, modèle, tâche.**
- **Modèle lu** : Llama-3.1-8B-Instruct, couche 31 (« Llama-3.1-8B layer 31 (final residual stream, last user token) », p. 3). La rotation des activations est reproduite sur Qwen3-8B et Gemma-4-E4B, mais les sondes ne sont évaluées que sur Llama : « probe evaluation is on Llama-3.1-8B. » (p. 1) ; « Cross-model probe evaluation is left to follow-up » (p. 3).
- **Position : le modèle qui reçoit l'entrée**, avant toute réponse. « This framing reflects a realistic deployment scenario where a probe monitors the user turn before the model responds. » (p. 3) ; « Activations are extracted at the last token of the user turn, consistent with standard single-position probing » (p. 3).
- **Propriété : l'intention de l'utilisateur.** « The probe target throughout is binary user intent: malicious (prompt injection or unsafe request) versus benign. » (p. 2).
- **Données** : 29 jeux publics, 168 440 exemples, 32,4 % malveillants (« Total corpus 168,440 (32.4% mal) », p. 14). Validation croisée en 5 plis, plus un protocole où un jeu entier est tenu à l'écart (annexe I).
- **Entraînement** : sur activations propres ; « probes train on clean activations at the user-EOT readout; perturbations are applied at inference time. » (p. 3).
- **Cinq architectures** (p. 5) : linéaire au dernier jeton ; moyenne des 16 derniers jetons ; trois lectures de toute la séquence, par moyenne, attention ou maximum (« per-token feature transform aggregated across the user-turn sequence by mean, softmax-attention pooling », p. 5).

**Perturbation et coût (constat C).**
- **Paquet de fautes empilées**, cinq composantes (p. 5) : point d'interrogation changé en point ; faute de clavier voisin sur le dernier mot ; faute de clavier voisin sur un mot au moins trois positions plus tôt ; majuscule trop tôt ; point final ajouté ou ôté. « Mean: 3.33 character edits per sample (range 1–5; 99.996% valid coverage). » (p. 5). « Each component is applied only when its structural prerequisite is met » (p. 5).
- **Placement** : la plupart des composantes tombent **en fin de message**, près du point de lecture, à la suite d'un relevé des angles sur le même modèle et la même couche (p. 4-5 ; constat C).
- **Régime réparti** : une faute de clavier voisin un mot sur deux, « used as a stress test rather than a model of typical user noise » (p. 2).
- **Coût d'attaque** : aucune requête, aucune optimisation, aucun accès au modèle ; mais une connaissance de la position de lecture. Aucun adversaire : « We extend this line to ordinary, non-targeted typing variation, without adversarial intent. » (p. 2). Les auteurs ajoutent, sans l'avoir mis à l'épreuve d'un attaquant : « We do not claim that our specific 5-component combination matches any measured user distribution; the same pattern, applied deliberately, is also a no-cost attack vector requiring no model access or optimization. » (p. 5).
- **Pas de cible de verdict** : la perturbation ne vise aucun verdict. La médiane du déplacement des scores malveillants est nulle (tableau 8, p. 12).

---

## 3. La chute, chiffrée

### 3.1 Sonde à une seule position, paquet de fautes (tableau 2, p. 5 ; auteurs)

| condition | aire sous la courbe | vrais positifs à 1 % de faux positifs | à 5 % |
|---|---|---|---|
| propre | 0,9980 | 97,4 % | 99,5 % |
| perturbé | 0,9925 | 85,4 % | 96,7 % |
| écart | −0,55 point | **−12,0 points** | −2,8 points |

- « At the deployment-realistic operating point of FPR=1%, TPR drops from 97.4% to 85.4%, a loss of 12.0 percentage points. » (p. 5) ; « Perturbed 0.9925 85.4% 96.7% » (p. 5).
- **Qui est perturbé** (constat B) : tous les exemples de test, bénins compris (« We apply a stacked-typing bundle per test sample », p. 5).
- **Seuil** (constat A) : recalé par condition. La preuve est à la p. 16 (« re-calibrated per (fold, condition), matching the operational » … « convention of §6 so that the perturbation »), et la légende de la figure 4 l'appuie (p. 7). Les auteurs ajoutent : « Threshold recalibration alone cannot recover the clean (FPR, TPR) operating point (Figure 4). » (p. 5). La phrase de la p. 5 sur les franchissements dans les deux classes laisse une ambiguïté (section 5, point 13).
- **Distribution des déplacements** (tableau 8, p. 12 ; auteurs) :
  - malveillants : 5ᵉ centile −0,490, médiane nulle, moyenne −0,053 ;
  - bénins : 95ᵉ centile +0,185, moyenne +0,021.

  « Linear (single-position) has heavy-tailed shifts on the malicious side » (p. 12).
- **Lecture** : la perte de 12,0 points mêle des scores bénins qui montent et une queue de scores malveillants qui descend, à seuil recalé. Ce n'est pas un taux d'évasion d'un attaquant contre un moniteur au seuil fixé. Ce dernier taux n'est pas imprimé.
- **Capacité** : un perceptron multicouche au même jeton perd autant (12,5 ± 0,8 points) ; « Higher capacity at a single position yields no robustness benefit; the variable is where the probe reads, not how it classifies. » (p. 6).

### 3.2 Cinq architectures, deux régimes (tableau 3, p. 6 ; auteurs ; écart des vrais positifs à 1 % de faux positifs, moyenne ± écart type sur 5 plis ; vu sur l'image)

| sonde | localisé (paquet) | réparti (un mot sur deux) |
|---|---|---|
| linéaire, dernier jeton | −12,00 ± 0,48 | −6,85 ± 0,56 |
| moyenne des 16 derniers | −0,87 ± 0,09 | −4,53 ± 0,33 |
| toute la séquence, moyenne | −0,30 ± 0,07 | **−16,81 ± 1,26** |
| toute la séquence, attention | −0,48 ± 0,15 | −3,78 ± 1,76 |
| toute la séquence, maximum | −0,48 ± 0,13 | −3,91 ± 1,35 |

- Lignes contrôlées : « Linear (user EOT) −12.00 ± 0.48pp −6.85 ± 0.56pp » ; « Mean last 16 −0.87 ± 0.09pp −4.53 ± 0.33pp » ; « MLP (all) −0.30 ± 0.07pp −16.81 ± 1.26pp » ; « Attention (all) −0.48 ± 0.15pp −3.78 ± 1.76pp » ; « MultiMax (all) −0.48 ± 0.13pp −3.91 ± 1.35pp » (p. 6).
- Lecture des auteurs : « Table 3 shows that all multi-position probes are near-immune to the localized stacked-typing bundle. » (p. 6) ; « every full-sequence multi-position probe loses ≤ 0.5pp » (p. 6). Ce dernier chiffre vaut pour les trois lectures de toute la séquence ; la fenêtre des 16 derniers jetons perd 0,87 point (constat M). « Full-sequence MLP, however, drops −16.8pp, losing its localized-regime margin entirely. » (p. 6).

### 3.3 Hors distribution (un jeu tenu à l'écart ; tableaux 15 et 16, p. 17-18 ; auteurs)

- Sur les 7 plis à deux classes, seuil recalé par pli : vrais positifs propres de 38,9 % à 46,3 % selon l'architecture. Sous le paquet : −3,5 points pour la sonde à une position, +1,4 pour l'attention ; sous le régime réparti, de −2,5 à −6,2 points. Lignes : « Linear (EOT) 38.9% 35.4% 33.6% −3.5pp −5.3pp » ; « Attention (all) 46.3% 47.7% 43.8% +1.4pp −2.5pp » (p. 17).
- Par pli : jusqu'à −11,2 points (paquet) et −16,8 points (réparti) ; « SafeGuard 93.5% 85.4% −8.1pp 76.7% −16.8pp » (p. 18). Les auteurs : « indicating that ID perturbation fragility persists under distribution shift but is masked at the aggregate by floor effects. » (p. 16).
- Moyennes recalculées sur le tableau 16 : 38,86 %, 35,36 % et 33,60 % (calcul), conformes au tableau 15.

### 3.4 Ce que font les lecteurs de texte des mêmes fautes (constats D et J)

Aucun juge génératif ni classifieur de texte ne reçoit les fautes **en tant que détecteur**. Deux mesures touchent des lecteurs de texte.

1. **Un juge génératif qui note la lecture des modèles étudiés** (annexe A.2, p. 10 ; tableau 7, p. 11).
   - « A Claude Sonnet 4.5 judge (via AWS Bedrock, temperature 0, independent per-pair calls) labeled each pair on two binary criteria » (p. 10). Le critère d'intention est : « intent preservation (did the model interpret the perturbed prompt as asking for the same thing?) » (p. 10).
   - Résultat : « Aggregate across the 594 judged pairs: intent preservation 94.6% and response equivalence 76.6%. » (p. 10) ; « Overall 594 0.946 0.766 » (p. 11). Par case, l'intention est préservée dans 84 à 100 % des paires (tableau 7, auteurs).
   - Ces chiffres mesurent **les trois modèles étudiés selon ce juge**, pas la robustesse d'un juge.
   - L'échantillon est distinct : 100 consignes (« We sampled 100 prompts (50 benign from OpenOrca with 80–350 words; 50 malicious from HarmBench across its three subsets) », p. 10), sans score de sonde.
   - « 6 pairs sharing a single biosecurity prompt were refused by the judge model itself and excluded. » (p. 10).
2. **Le modèle lu, par ses refus** : la seule décision d'un lecteur génératif mesurée sous les mêmes fautes.
   - « Refusal flips on the 294 malicious pairs occurred 27 times (9.2%); 12 went toward more conservative refusal and 15 toward compliance, the latter concentrated under ESW (Llama 20%, Gemma 16%, Qwen3 8%). » (p. 10).
   - Régime localisé : « In the localized regime the LLM’s response is functionally unchanged on both benign and malicious cases; the probe is the sole failure point. » (p. 2). Cette phrase repose sur quatre exemples (tableau 6) et sur l'échantillon non apparié du point 1.
   - Régime réparti : le lecteur de texte cède aussi. « In the distributed regime intent is preserved but the malicious example bypasses the LLM’s safety alignment » (p. 2).

La seule comparaison est qualitative : « their readout is more sensitive to ordinary surface noise than the model whose internals they read. » (p. 8) ; « a silent disagreement, neither adversarial nor semantically ambiguous. » (p. 8). Elle ne vaut, au mieux, que pour le régime localisé.

### 3.5 Adversaire ou fautes aléatoires

- **Pas d'adversaire** : les règles sont fixes ; rien n'interroge la sonde, rien n'est optimisé ni adapté.
- **Mais le placement n'est pas aveugle** : il est fait près de la position de lecture (constat C).
- La phrase offensive (« The same typing patterns can be applied deliberately as low-cost attack vectors: distributed corruption alone bypasses both probe and alignment (§3.3) without optimization, model access, or adversarial prompt engineering. », p. 8) n'est pas mesurée comme attaque. Son exemple (tableau 6, p. 11, « Breaking into the Pentagon is a serious matter and » …) donne une réponse et un angle, mais **aucun score de sonde**.

### 3.6 Parades (section 7, p. 6-8 ; annexes E, H, I ; constat E)

| parade | dans la distribution | hors distribution | page |
|---|---|---|---|
| plusieurs positions | au plus 0,87 point de perte sous le paquet ; attention et maximum vers 3,8-3,9 sous le régime réparti | aire sous la courbe de 0,81 à 0,92 avant toute perturbation | 5, 6, 16 |
| entraînement augmenté de fautes | 85,4 % → 93,84 ± 0,5 %, résiduel −3,70 points (« Pert. TPR@FPR=1% 85.4% 93.84 ± 0.5% ») | non mesuré | 6-7, 13 |
| suffixe d'environ 30 jetons, lu sur une branche du cache clé-valeur puis jeté | « the KV-cache fork recovers TPR@FPR=1% to 98.65 ± 0.02% », résiduel −0,60 point | sous le paquet, la perte n'est plus réduite : −4,5 points contre −3,5 sans suffixe, sur une moyenne de 7 plis, sans écart type ; taux perturbé plus haut avec le suffixe (42,7 % contre 35,4 %, calcul) ; régime réparti non rapporté | 7-8, 16 |

- Les auteurs le reconnaissent : « The defenses restore probe accuracy under that asymmetry rather than removing it. » (p. 8).
- La p. 7 ne rapporte, hors distribution, que le gain propre (« lifts clean weighted accuracy from 77.5% »).

---

## 4. Ce que l'article ne fait pas

- Aucun juge génératif, aucun classifieur de texte employé comme détecteur sous les mêmes fautes ; aucune métrique commune entre sonde et lecteur de texte.
- Aucun coût d'attaque mesuré, ni courbe « déplacement obtenu en fonction de l'effort ». Le coût est fixé par construction (de 1 à 5 caractères).
- Aucun taux au seuil fixé sur données propres ; aucune perturbation du seul côté malveillant.
- Aucun adversaire ni attaque qui s'adapte.
- Aucun agent, aucune trajectoire, aucune action ; la propriété lue est l'intention de l'utilisateur.
- Aucun régime « activations » ni « poids » côté attaquant ; aucune mesure de g.
- Un seul modèle et une seule couche pour les sondes : « but the multi-architecture probe sweep itself is on a single model (Llama-3.1-8B). All experiments use a single layer per model. » (p. 8).

**Limites reconnues** : tokenisation (« Probe-level perturbations may alter BPE tokenization in addition to attention dilution », p. 8) ; variantes du suffixe reportées (« learned-suffix designs are deferred to », p. 8) ; combinaison de fautes non mesurée sur des utilisateurs réels (p. 5).

---

## 5. Incohérences internes et réserves (R4)

1. **La rotation de 43 à 56° attribuée au point de lecture** : « Ordinary typing variation rotates the user-EOT activation by » 43 à 56° (p. 8). C'est la rotation au jeton fauté (« Mean on-site angular change ranges from 43 » …, p. 3). Au point de lecture, le tableau 1 donne de 3,4° à 26,4° (p. 4). Le résumé est ambigu de même : « the same edit rotates the readout vector by » 43 à 56° (p. 1).
2. **Figure 1** (p. 4, image) : Gemma vers 38-39° à une profondeur, Llama vers 58° (figure), hors de l'intervalle imprimé.
3. **Couches de Gemma** : « Gemma-4-E4B: 28/29/40/41 » (p. 3) contre « Spatial decay replication: Gemma-4-E4B (full-attention layers 10, 21, 29, 41). » (p. 12).
4. **« Ordre de grandeur »** : « an order of magnitude better than perturbation-augmented training » (p. 1) ; « an order of magnitude smaller than the augmentation-training residual » (p. 7). 3,70 / 0,60 = 6,2 (calcul), et dans la distribution seulement ; hors distribution, le suffixe ne réduit plus la perte et l'entraînement augmenté n'est pas mesuré (constats E, G).
5. **Exactitude hors distribution** : « accuracy from > 99% to 0.77–0.81 » (p. 5) ; le tableau 13 va de 0,775 à 0,821.
6. **Classes des jeux** : le tableau 10 range AgentDojo, BIPIA, Deepset, Jayavibhav et Jailbreak-Cls parmi les malveillants ; le tableau 14 les compte parmi les 7 plis à deux classes. La part de 32,4 % se retrouve avec le tableau 14 (32,36 %, calcul), non avec les rubriques du tableau 10 (36,3 %, calcul).
7. **Plis fusionnés** : Gandalf et Scam sont annoncés fusionnés (« merged with a larger dataset for LODO fold stability », p. 14), mais ils forment des plis à part (tableau 14), et l'annexe compte 29 plis (« Of the 29 folds, only 7 contain both classes and admit AUC; the other 22 are single-class. », p. 15). Le « 28 » du tableau 17 est expliqué (Scam indisponible) : ce n'est pas une incohérence (constat K).
8. **Même source pour deux plis** : « Code Exercise iamtarun/python code instructions 18k alpaca » et « Python-Alpaca iamtarun/python code instructions 18k alpaca » (p. 18). Les deux jeux sont bénins seuls : une fuite ne toucherait que l'exactitude pondérée et le taux de faux positifs de ces plis (constat K).
9. **Bascules de refus** : 15 vers la conformité, mais 20 %, 16 % et 8 % de 49 font 21,6 (calcul). La phrase (p. 10) est ambiguë.
10. **Paquet vu en apprentissage** : quatre de ses cinq familles sont dans la politique d'augmentation (annexe E, p. 13). « Recovery is not perfect even on individual perturbations seen in training » (p. 6).
11. **Trop propre** : 98,65 ± 0,02 % pour le suffixe (p. 7), sans équivalent hors distribution (section 3.6).
12. **Décroissance** (constat F) : sur la figure 2 (p. 4, image), la couche 31, celle de la sonde, est vers 0,18-0,20 à dix jetons (figure), donc au-dessus des 15 % annoncés (« All four depth checkpoints fall below 15% of the on-site signal by d≈10 tokens », p. 4). Même écart, plus faible, pour Qwen3-8B (figure 6, p. 12).
13. **Seuil** (constat A) : recalé par condition (p. 16), mais la phrase de la p. 5 (« malicious samples cross below the fixed-FPR threshold more readily than benign samples cross above it ») décrit des franchissements dans les deux classes, comme pour un seuil fixe.
14. **Provenance** (constat H) : « arXiv:2609.15994v1 [cs.CL] 8 Jul 2026 » (p. 1). Un identifiant en 2609 désigne un dépôt de septembre 2026.
15. **Coïncidences** (constat L) : même moyenne de 93,84 % pour le paquet entier et pour une seule famille (« full bundle (5-component) 93.84 ± 0.53% » ; « 93.84 ± 0.59% », p. 13) ; 85,4 % et −16,8 points reviennent au pli SafeGuard (p. 18) et aux tableaux 2 et 3. Notées, sans conclure.

Contrôles recalculés et conformes (calcul) : 1 − 0,60/12,0 = 0,95 ; (93,84 − 85,4)/12,0 = 0,70 ; mémoire du suffixe 30 × 32 × 8 × 128 × 2 × 2 octets = 3,75 Mio ; total des jeux 168 440.

---

## 6. Verdicts par composante

| composante de HC4 | verdict | pages |
|---|---|---|
| (a) coût d'attaque mesuré | **voisin** : un point de coût fixé par construction (environ 3,3 caractères placés près de la position de lecture, aucune requête, aucune optimisation, aucun accès), avec une chute mesurée. Ce n'est pas un coût mesuré pour obtenir un déplacement donné. | 2, 4, 5 |
| (b) pour une **sonde** | **occupée en partie, hors de la lettre restreinte par N-068 (point 8a)** : chute de la détection d'une sonde de propriété de l'entrée lue sur le modèle qui reçoit, par architecture, à 1 % de faux positifs, à seuil recalé, toutes classes perturbées. Fait : la chute et la dépendance à l'agrégation. Non fait : adversaire, seuil fixe, coût en fonction du déplacement, sonde de l'agent auteur, g. | 5, 6, 12, 16-18 |
| (c) pour un **juge génératif** | **voisin** (constat J) : la décision de refus du modèle lu bascule dans 9,2 % des paires malveillantes, dans les deux sens, surtout sous le régime réparti. Ce n'est pas un moniteur. Le juge génératif de l'annexe A.2 note la lecture des modèles ; il ne détecte rien (constat D). | 2, 10, 11 |
| (d) **comparaison** dans un même cadre, à durcissement égal, par régime d'accès | **ne touche pas** : une phrase qualitative seulement (p. 8), sans métrique commune ni moniteur textuel. | 8 |
| (e) prémisse « déplacer une sonde coûte plus » | **contre-indice net, étroit**. Net : sans requête ni optimisation, la sonde à une position perd 12,0 points de détection. Étroit sur cinq points : (i) ce n'est pas un taux d'évasion (constat B) ; (ii) les fautes sont placées près de la lecture (constat C) ; (iii) sonde du modèle lecteur et propriété de l'entrée, hors de N-068 (8a) ; (iv) l'agrégation ramène la perte sous un point dans le régime localisé et vers 3,8 dans le régime réparti ; (v) l'opposition au lecteur de texte n'est que qualitative, et ne vaut que dans le régime localisé (constats D, J). | 2, 4-6, 8, 10, 12 |

---

## 7. Ce qui reste revendicable (formulation exacte)

Reprise sans changement de la formulation du rapport HC4 v2 du compte 2 (section 7), que cette pièce ne prend pas :

> « Le coût d'attaque — requêtes, jetons, calcul, temps, exemples de réglage fin — nécessaire pour obtenir un déplacement donné du score d'une sonde entraînée qui lit l'intention ou l'action de l'agent auteur, à taux de faux positifs fixé, comparé dans un même cadre au coût du même déplacement sur un juge génératif sous les mêmes attaques, par régime d'accès (contexte seul ; lecture des activations ou des poids ; écriture dans les poids), à durcissement déclaré et sous attaque qui s'adapte. »

La pièce resserre la portée de la prédiction sans prendre l'énoncé. Pour une sonde du modèle lecteur à une seule position, une dégradation partielle s'obtient par le contexte seul, à coût nul en requêtes, en connaissant la position de lecture. « De plusieurs ordres de grandeur » ne peut donc viser que des sondes de l'agent auteur, de préférence à agrégation robuste, et reste une prédiction.

---

## 8. Ce qu'une phrase publique sur HC4 ne doit pas affirmer

Je ne rédige pas la phrase publique.

1. Que le contexte seul ne déplace pas une sonde, sans dire de quelle sonde il s'agit. Une sonde du modèle lecteur à une seule position perd 12,0 points de détection sous environ 3,3 caractères de fautes placées près de sa position de lecture (p. 5).
2. Que les sondes sont plus robustes au bruit de surface que les lecteurs de texte. Dans le régime localisé, la pièce soutient l'inverse, mais qualitativement seulement ; dans le régime réparti, le modèle cède aussi (p. 2, 8, 10).
3. Qu'un coût « de plusieurs ordres de grandeur » est observé, ou que cette pièce mesure un coût d'attaque.
4. Que ces 12,0 points sont une évasion adverse, ou qu'ils sont perdus au seuil d'un moniteur déployé. Les fautes touchent toutes les classes et le seuil est recalé (constat B).
5. Que la phrase offensive de la p. 8 est démontrée exemple par exemple pour la sonde (section 3.5).
6. Que le suffixe du cache clé-valeur répare la fragilité en général. Hors distribution, il ne réduit plus la perte due aux fautes (constat E).
7. Que toute agrégation protège : la moyenne sur la séquence perd 16,8 points sous le régime réparti (p. 6).
8. Que la pièce montre une sonde déplacée vers un verdict choisi : la perturbation ne vise rien, et la médiane du déplacement des scores malveillants est nulle (p. 12).
9. Que des fautes quelconques suffisent : l'effet tient à leur place près de la position de lecture (constat C ; tableau 1, p. 4).
10. Que la pièce compare une sonde et un juge, ou qu'un juge génératif résiste aux mêmes fautes (constat D).

---

## 9. Voisins nommés dans la pièce et non lus

| voisin | page où il est nommé | pourquoi le lire |
|---|---|---|
| Yu et collègues 2026, « Character-level perturbations amplify LLM jailbreak attacks. » (soumission OpenReview, p. 10) | 2, 10 | **le plus proche pour (b) et pour (d)** (constat I). Des fautes de caractères ciblées sur les mots nuisibles, évaluées sur des sondes de diagnostic selon la pièce (« The closest prior work (Yu et al., 2026) applies targeted ») et, d'après le titre, sur le jailbreak du modèle génératif. L'attaquant choisit ses mots. |
| Gan et collègues 2024, fautes de frappe adverses contre le raisonnement des modèles (« adversarial typographical errors ») | 2, 9 | côté juge génératif : fautes optimisées contre un lecteur de texte (« including typing-specific perturbations (Gan et al., 2024) ») |
| Aliakbarzadeh et collègues 2024, « Exploring robustness of multilingual LLMs on real-world noisy » … | 2, 8 | côté lecteur de texte, bruit réel (ajout, constat I) |
| Zhao et collègues 2026, fautes de frappe multilingues (« against multilingual typographical errors ») | 2, 10 | côté lecteur de texte |
| Kramár et collègues 2026, « Building production-ready probes for gemini » | 1-2, 9 | taxonomie des agrégations ; 2601.11516 déjà dans la liste de N-068 |
| Fomin 2026, « When benchmarks lie: Evaluating malicious » / « prompt classifiers under true distribution shift » | 3, 5, 9 | protocole du jeu tenu à l'écart |
| Gu et collègues 2025 (« robustness of large language models safety to latent ») | 2, 9 | régime « activations » côté attaquant |
| Zou et collègues 2026, « Pishield: Detecting prompt injection attacks via intrinsic llm features » | 1, 10 | détecteur d'injection par activations |
| Abdelnabi et collègues 2025, « Get My Drift? Catching LLM Task Drift with Activation Deltas » | 1, 8 | détecteur d'injection par activations |
| Wang et collègues 2026 (« KV-cache reuse has been used adversarially to accelerate suffix-search jailbreak attacks (Wang et al., 2026) ») | 7, 10 | coût d'attaque en boîte blanche, côté modèle |

**Priorité** : Yu et collègues 2026, puis Gan et collègues 2024.

---

## 10. Notes à part, sans verdict

**HC2.**
- Position du lecteur (modèle qui reçoit), sans adversaire.
- La position unique est fragile ; la moyenne sur la séquence s'effondre sous des fautes réparties ; l'attention et le maximum résistent le mieux (tableau 3, p. 6). « Architecture switching eliminates the localized-perturbation gap » (p. 6).
- Cohérent avec l'interdit du programme sur la moyenne des jetons dans une sonde de production, et avec l'agrégation robuste de l'énoncé de HC2.
- Pour HC2b : « the training distribution couples intent with dataset-specific surface attributes, so what the probes learn is an intent-aligned mixture rather than intent in isolation. » (p. 16).

**Tr.**
- Au niveau du jeton et d'un tour : l'attention et le maximum tiennent mieux que la moyenne sous des fautes réparties ; un lecteur à une position est exposé quand la perturbation est proche de lui.
- La pièce ne dit rien de l'action, de la trajectoire, de l'accumulation séquentielle ni d'un attaquant qui s'adapte.
- Une lecture à une seule position par action hériterait de cette exposition si la lecture tombe près d'un jeton perturbé. À la couche de la sonde, la décroissance est plus lente qu'annoncé (constat F).

---

## 11. Réserves du lecteur

- **Profondeur.** La lecture v1 a été rapide (environ deux minutes pour le texte). La contre-lecture n'y a trouvé aucun chiffre faux, mais des écarts de portée (B à E), corrigés ici après relecture, en texte et sur l'image, des p. 2, 4-8, 10, 12 et 16.
- **Valeurs lues sur les figures** : approximatives (nature « figure »).
- **Sens de « juge »** : jugé sous la seule lecture « juge génératif ». Sous la lecture large, la pièce n'apporte pas non plus de comparaison mesurée.
- **Constat B** : la perte à seuil fixe est conjecturée plus faible, sans preuve (section 1).

## 12. Contrôles

- Citations : 127, 0 échec (`citations-HC4-2609.15994-v2.json`, dans l'archive).
- Guillemets du rapport : `releve-guillemets-v2.txt`, dans l'archive.
