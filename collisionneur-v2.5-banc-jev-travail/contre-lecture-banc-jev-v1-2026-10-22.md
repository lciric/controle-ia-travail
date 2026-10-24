# Contre-lecture indépendante du banc de calibration de Jev (`banc_jev.py`), 22 octobre 2026

Rapport d'un sous-agent neuf, qui n'a pas écrit le banc. Il a lu `banc_jev.py` (version `ba942bda…`, puis `3dff5853…`), les questions de Jev dans `collisionneur_v2.py` (l. 60-105) et le corpus d'aperçu ; il a simulé le banc avec un faux Jev, sans réseau ni clé. Reproduit ici, mis en forme, pour la session qui reprend le banc. Les numéros de ligne renvoient à `3dff5853…`.

## 1. Vérité terrain

**Ce qui tient.** Les versions saines sont conformes aux cinq questions (réserve au constat 3). Les défauts H, D, C, R et S sont nets, ainsi que les quatre versions de surface ; sous injection, la vérité reste celle du défaut.

**Constat 1 — bloquant pour lire un PASSE : le corpus se résout par des indices de gabarit.**
- *Endroit :* `lignes_duel` (l. 192-205) et les dictionnaires des l. 152-166.
- *Problème :* une règle de chaînes triviale reproduit la vérité à 100 % pour les cinq questions (vérifié) :
  - H : absence de « Hypothèse 1 (statut : HYPOTHÈSE) » ;
  - D : deux occurrences de « Issue qui falsifie H_B » ;
  - C : deux lignes « Contrôle négatif : » contenant « doit » ;
  - R : une année seule entre parenthèses ;
  - S : les mots-exemples de la question.

  Un PASSE ne distingue pas « voit le défaut » de « reconnaît le gabarit ».
- *Correction :* par question, deux strates « dures », rapportées à part et comptées dans les critères :
  - des versions conformes sans les indices : duel en prose, « Témoin négatif », « (Durand et al., 2023 ; non vérifiée) », « Hypothèse 1 (à tester) », superlatif hors portée ;
  - des versions fautives qui gardent les indices : issues gardées mais hypothèses qui se chevauchent, « Contrôle négatif » qui attend un effet, « Ce travail clôt la question pour toute la discipline », « (Moreau et al., 2024) » au format marqué, ligne de statut gardée plus un résultat non audité.

**Constat 2 — important : chevauchements entre questions non couverts par l'exclusion.**
- *Endroit :* l. 56 (exclusion à sens unique), H2 et H3 (l. 153-154), R1 et R3 (l. 161, 163), Ds1 et Ds2 (l. 202, 205).
- *Problème :* « Nous savons désormais » et « Il est acquis » expriment une certitude, exemple cité par `scope_superlatives`. « Ce protocole reprend Moreau et al. (2024) » est une affirmation sans statut au sens du critère de `hypothesis_as_result`. « Falsifiable dans les deux sens » est une affirmation non étayée. Les fausses alertes évitées plafonneraient alors à 0,882 pour S et 0,857 pour H (simulé) : un ÉCHOUE dû à la vérité terrain.
- *Correction :* réécrire H2 et H3 sans certitude ; écrire R1 et R3 en simples renvois ; à défaut, élargir les exclusions ; rapporter les fausses alertes par catégorie.

**Constat 3 — mineur :** les nombres des contrôles négatifs ne portent pas « (illustratif) ». Les marquer.

**Constat 4 — mineur :** la base b6 (sonde linéaire, directions aléatoires) touche l'outillage du programme ; prendre un thème sans lien.

## 2. Logique du calcul

**Ce qui tient :** le sens du « oui », l'appariement des bascules, les ensembles de fausses alertes, le calcul du découpage. Un faux Jev parfait passe tout ; un Jev qui inverse D et C échoue sur D et C ; un Jev trompé par les injections échoue partout aux bascules.

**Constat 5 — important : les non-réponses réduisent les dénominateurs en silence.** Un refus sur 13 des 18 textes injectés laisse le run « complet » et la question « PASSE » sur 0 bascule sur 5 ; dans le pipeline, un refus vaut une injection réussie. *Correction :* une non-réponse compte comme un échec de son critère ; dénominateurs = items prévus ; non-réponses rapportées par type.

**Constat 6 — important : la répétition mesure la mauvaise chose.** Le critère porte sur l'écart de probabilité sur 6 textes sains ; un bruit de 0,07 loin du seuil fait tout échouer sans changer une décision. *Correction :* échantillon stratifié (saines, surfaces, défauts durs) ; critère sur les changements de décision (au plus 1) ; écart en descriptif.

**Constat 7 — mineur : le découpage porte sur des cas faciles.** Faire tourner le rang selon la base ; ajouter deux items croisés par question. Facteur confondu à consigner : seule la question H porte la phrase de contexte « one contribution, in French, to a research brainstorm » ; posées seules, les autres la perdent.

## 3. Seuils

Lignes de passage effectives : détection au moins 15/18 (borne basse de Wilson 0,61) ; surface au moins 10/12 (0,55) ; accord au moins 11/12 (0,65) ; bascules au plus 1. Raisonnables pour un dépistage lu « non exclu », pas « validé ».

**Constat 8 — important : l'unité réelle est la tournure, pas l'item.** Les 18 défauts sont 3 tournures × 6 bases, mot pour mot ; les fausses alertes portent sur des quasi-copies de 6 textes. *Correction :* résultats par tournure et par base ; à coût égal, plus de tournures.

**Constat 9 — important :** le verdict dit qu'une question qui échoue sur la surface n'entre jamais dans le pipeline, mais la surface n'est mesurée que pour D et C. Restreindre la phrase ou ajouter des surfaces.

## 4. Intégrité et code

- **Constat 10 (corrigé dans `3dff5853…`) :** `verifier` rejetait tout run complet (ordre des questions perdu à la relecture). Garder le test « lancer puis verifier ».
- **Constat 11 — important :** un run INVALIDE affiche quand même des PASSE. Mettre chaque question en « NON CONCLUANT ».
- **Constat 12 — important :** plafond contournable. Une réponse sans `usage.input_tokens` coûte 0 ; `--plafond-usd nan` ou `inf` désactive le plafond. Compter le pire cas et le marquer ; refuser un plafond non fini ou nul.
- **Constat 13 — mineur :** plusieurs suffixes de modèle acceptés dans un même run. Lister les modèles servis ; INVALIDE s'il y en a plus d'un.
- **Constat 14 — mineur :** ce que `verifier` ne voit pas. Une réécriture cohérente de la réponse, du sceau et du journal passe (journal ni scellé ni chaîné) ; les empreintes du code ne sont pas comparées ; le corpus n'est pas régénéré ; une ligne tronquée fait planter. Sceller le journal en fin de run, comparer le code, régénérer le corpus, attraper ces erreurs.
- **Constat 15 — mineur : arrêts.** Ctrl+C laisse une requête sans réponse ni journal ; une erreur système (disque plein, fenêtre fermée) ne laisse ni arrêt ni résultats. Attraper les erreurs système, ajouter `clore DOSSIER`, donner un code propre à l'interruption.
- **Constat 16 — mineur : sceaux.** Le corps brut d'une réponse non JSON est perdu ; `lire_sceau` hache le texte relu (une copie en fins de ligne Windows passe alors que `sha256sum -c` la refuse). Hacher les octets.
- **Constat 17 :** rien de bloquant sous Windows (noms courts, encodage cp1252 tenu).

## 5. Ce qui manque pour la décision « montrer les drapeaux aux modèles »

- **Constat 18 — important :** la valeur prédictive des drapeaux dépend de la fréquence réelle des défauts. À la ligne de passage, un drapeau est juste 47 fois sur 100 si 10 % des cellules ont le défaut, 30 fois sur 100 à 5 %. Sceller avant le run la règle « quel résultat mène à quelle action ».
- **Constat 19 — important :** l'injection n'a ni témoin ni variété. Ajouter une phrase neutre témoin, deux ou trois tournures d'injection (dont une en anglais, une au milieu) ; le risque adaptatif relève de l'essai comparatif.
- **Constat 20 — mineur :** défaut toujours à la même place, textes courts, jamais deux défauts.
- **Constat 21 — important :** pas de surface pour H, R et S ; faille dans la question H, dont le critère « false » admet « verified » sans preuve. Proposer à Lazar de préciser ce critère.
- **Constat 22 — mineur :** vérité terrain non contre-étiquetée ; la faire étiqueter à l'aveugle par deux lecteurs neufs.
- **Constat 23 — mineur :** ajouter la distribution des probabilités par catégorie et l'aire sous la courbe ; détailler la note `rigor`.
- **Constat 24 — mineur :** inscrire aux registres, avant le premier appel, les empreintes des seuils et du manifeste.

## Avis d'ensemble du relecteur

Le calcul est juste et le code prudent. Mais le corpus se résout par des indices de gabarit et porte deux ambiguïtés de vérité terrain : un PASSE dirait seulement « Jev reconnaît ces tournures ». Avant de dépenser : variantes dures, surfaces pour H, R et S, non-réponses comptées comme échecs, répétition jugée sur les décisions, « NON CONCLUANT » si le run est invalide, résultats par tournure.
