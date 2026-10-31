# Proposition B — Tour III.1 : conception ciblée, à l'aveugle

## Préambule méthodologique

Je traite chaque nœud selon le livrable demandé : (a) présupposés non établis, (b) expériences décisives en duel, (c) mesure minimale de chaque instrument, (d) ancrage matériel. Conformément à B4, chaque expérience oppose H_A et H_B exclusives, et chaque issue falsifie quelque chose.

---

## N1 — Bisociation à deux espaces : redéfinir V5 après lecture

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| L'échec de V5 vient de la définition du critère (étiquettes d'opérateur suivent une loi non égalisée par S16d), pas d'un défaut du générateur | OBSERVÉ-NON-AUDITÉ | Pièce 2, diagnostic sur 200 mondes d'essai avec une seule graine de flux ; réserves explicites du diagnostic (§1.4, §2 « Réserves ») |
| La variante T2 (fréquence de l'étiquette du concept rare planté) mesure « exactement ce que S16d égalise » | HYPOTHÈSE | Pièce 2, option A : le diagnostic dit « presque acquis par construction » ; aucune démonstration que cette grandeur détecte un défaut du monde visible par les bras |
| Redéfinir V5 après lecture est un changement d'un critère gelé comparable aux autres versions du texte | HYPOTHÈSE | La liste d'arrêt dit les deux choses (Pièce 3, l. 689–735 : « correction par R12 » ET « paramètre modifié après lecture → arrêt et consignation de l'écart R1 ») ; aucune règle ne hiérarchise ces deux lignes |
| L'erreur type naïve (0,29–0,60) est un estimateur fiable de la variabilité inter-statuts | HYPOTHÈSE | Pièce 2, §1.4 : « les erreurs types sont naïves (elles ignorent la corrélation entre ponts d'un même monde, faible ici) » — faiblesse non démontrée |
| L'ancienne grandeur (étiquette retenue, cinq statuts) reflète le risque CB-05 (« la rareté ne doit pas séparer vrai de faux ») | RAPPORTÉ | Pièce 2, option B : « ce risque n'est plus gardé par un seuil, alors qu'il existe : par la rareté de l'étiquette retenue, vrai d'opérateur et proche diffèrent d'environ 1,4 en M_bien » |

### (b) Expérience décisive

**Duel : T2 est-elle informative ou triviale ?**

- **H_A** : La grandeur T2 (fréquence du concept rare planté, vue des deux côtés) est non triviale : elle peut échouer pour un monde dont l'étiquette de pont serait exploitable par un bras.
- **H_B** : T2 est acquise par construction dès que le générateur plante un concept rare de fréquence homogène entre statuts, ce qui est garanti par S16d ; elle ne détecte aucune pathologie pertinente pour les bras.

**Métrique** : sur 300 mondes de validation à graines neuves, construire un générateur « cassé » (par exemple en rendant la fréquence du concept rare planté dépendante du statut : +2 pour « vrai conceptuel », −2 pour « faux ») et mesurer si T2 le rejette (écart > 0,5).

**Contrôle négatif** : le générateur scellé non modifié ; T2 doit passer (< 0,5).

**Issue falsifiante** : si le générateur cassé passe T2 (< 0,5), H_A est falsifiée : T2 ne détecte pas même une pathologie délibérée. Si le générateur cassé échoue et que le scellé passe, H_B est falsifiée : T2 est capable de rejeter un monde pathologique.

**Ma position** : option **B** (T2 décisionnelle + ancienne grandeur en rapport sans seuil), avec la condition que l'écart soit déclaré comme changement de critère gelé après lecture (R1) et que les graines de validation soient intégralement nouvelles. L'option A seule est insuffisante car elle supprime la surveillance du risque CB-05. L'option D est exclue : 0,83 en M_moyen sur les mondes d'essai. L'option C seule est insuffisante (1,29 / 2,27). L'abandon (E) est prématuré.

**Confiance** : 0,70 sur B.

**Pire cas de B** : le nouveau V5 passe trivialement et l'ancienne grandeur rapportée montre un écart de 1,4 entre statuts, mais personne ne peut plus l'arrêter car il n'y a pas de seuil dessus. **Garde** : fixer dans la v3 un déclencheur d'audit R4 (non d'arrêt) sur l'ancienne grandeur : si l'écart dépasse un seuil (par exemple 2,0 — illustratif), un audit est déclenché qui examine si les bras candidats voient la différence de rareté.

**Option manquante** : aucune option ne propose de **tester empiriquement si l'écart de rareté de l'étiquette retenue est exploitable par les bras** (un monde où la rareté sépare vrai de faux donne-t-il un avantage mesurable à N ?). Cette pièce trancherait la question : si oui, le rapport sans seuil de B ne suffit pas ; si non, l'écart est anodin.

**Pièce qui trancherait** : un calcul sur 200 mondes d'essai (graines 990200–990399, hors de toute plage déclarée) mesurant la corrélation entre la rareté de l'étiquette retenue par statut et la précision différentielle de N entre vrais et faux ponts. Coût : processeur seul, ≈ 50 secondes (Pièce 2 : « environ 50 secondes de calcul »), zéro dépense.

### (c) Mesure minimale de V5 (instrument)

- **Taux de détection** : V5 (quelle que soit sa forme) doit rejeter un monde dont la rareté est pathologiquement séparée entre statuts. Sur un cas honnête apparié (générateur scellé vs générateur cassé, même graine, seule la loi de fréquence du concept rare modifiée), taux de rejet attendu ≥ 0,95 pour le cassé, ≤ 0,05 pour le scellé.
- **Fausses alertes** : sur 300 mondes du générateur scellé, V5 passe dans ≥ 285 (≤ 5 % de faux négatifs).
- **Vérification mécanique à battre** : un test trivial (toujours passer) a un taux de détection de 0,00 ; V5 doit faire strictement mieux.

### (d) Ancrage matériel

- Modèle : aucun modèle de langage requis ; calcul Python pur.
- Calcul : processeur seul, ≈ 50 secondes pour 200 mondes (Pièce 2, VÉRIFIÉ dans la pièce).
- Coût : 0 USD.

---

## N3 — D-j : bras inspiré de Gu-Krenn sans reproduction préalable

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| Le « substitut inspiré de Gu et Krenn » produit des paires pertinentes pour le domaine du contrôle des IA | HYPOTHÈSE | Pièce 20 (SD-4), §5 : « la liste ne couvre pas le contrôle des intelligences artificielles ; les quelques mots communs portent un sens de physique et créeraient de fausses arêtes » |
| Le bras Gu-Krenn (ou son substitut) apporte une information différente de celle du bras basique et du bras méta | HYPOTHÈSE | Aucune mesure comparative n'existe ; les trois bras ne sont jamais confrontés dans les pièces sauf comme prédiction SUPPOSÉ (P14, Pièce 5) |
| Une reproduction est possible sans carte graphique | OBSERVÉ-NON-AUDITÉ | Pièce 20 (SD-3), R-873 : « réentraînement obligatoire, carte graphique ou 8 à 30 h de processeur par valeur d'IR → machine louée, nœud de dépense » |
| L'absence de reproduction préalable ne contamine pas l'interprétation de la course 2 | HYPOTHÈSE | Si le bras produit des paires de mauvaise qualité sans qu'on le sache (faute de reproduction), les fusions correspondantes sont du bruit |

### (b) Expérience décisive

**Duel : le substitut inspiré apporte-t-il une information non redondante ?**

- **H_A** : le substitut inspiré de Gu et Krenn, appliqué aux 10 fiches non aiguillées du pré-pilote, sélectionne une paire dont le score de concept (κ observé du bras basique) est dans le quartile inférieur (la paire est « loin en concept » : le bras apporte quelque chose que le bras basique n'aurait pas choisi).
- **H_B** : la paire sélectionnée par le substitut a un score de concept dans le quartile supérieur ou médian (elle est redondante avec ce que le bras basique aurait pu choisir).

**Métrique** : rang du κ observé de la paire choisie par le substitut parmi les 45 paires possibles (10 fiches).

**Contrôle négatif** : un bras qui choisit au hasard parmi les 45 paires ; la distribution de rang est uniforme.

**Issue falsifiante** : si la paire du substitut est systématiquement dans le quartile supérieur de κ (paire « proche en concept »), H_A est falsifiée : le substitut ne diversifie pas. Si la paire est systématiquement dans le quartile inférieur, H_B est falsifiée.

**Ma position** : **oui** (D-j = relâcher la condition de reproduction), avec les conditions suivantes :
1. Le bras est étiqueté « substitut, non reproduit » dans tout résultat (A19 le prévoit déjà, Pièce 7).
2. S31 est testé sur la moisson avant scellement (CP5-01, Pièce 7 : « source gelée de S31 et de son essai sur la moisson »).
3. Si le bras produit une paire identique (aux 2 paires près du tirage) au bras basique sur ≥ 2 lots du pré-pilote, il est déclaré « redondant » et non reconduit en génération 2 — critère écrit d'avance.

**Confiance** : 0,60 (au seuil « demander au collisionneur » de R-719).

**Pire cas** : le substitut produit une fusion inutile (≈ 1,88 USD de plus au pré-pilote — Pièce 9, k = 1). La fusion est filtrée par l'aiguilleur (passage attendu 0,9 — P14, Pièce 5) et ne contamine pas les mesures.

**Garde** : le pré-pilote éprouve la chaîne (aiguilleur, juges) ; une fusion du substitut qui échoue à l'aiguilleur est comptée comme « non passée » (diagnostic immédiat).

**Option manquante** : une option « oui, conditionnel au résultat du test B de Gu-Krenn sur leur propre domaine » (si le test hors échantillon échoue sur l'optique et la physique quantique — le domaine où le modèle a été entraîné —, le substitut pour le contrôle des IA n'a aucune base). Cela lie D-j à N9.

**Pièce qui trancherait** : un essai de S31 sur la moisson disponible (Pièce 20 (SD-4), §4.3 : requête déclarée, non lancée). Coût : celui de la requête OpenAlex (> 5 USD au tarif déclaré, > 1 semaine d'allocation gratuite — Pièce 20 (SD-4), §4.3) ou de l'instantané public (744 Go — hors conteneur actuel). **Si cette pièce n'est pas obtenue**, la position « oui » est conditionnée au seul essai sur la moisson existante, qui ne couvre pas le domaine.

### (c) Mesure minimale du substitut Gu-Krenn

- **Taux de détection** : sur un jeu de ponts connus (par exemple ponts publiés après la date de coupure des modèles, si disponible), le substitut classe la vraie paire au-dessus de 50 % des paires négatives (aire appariée > 0,50, Pièce 20 (N9-1), seuil B-ii).
- **Fausses alertes** : la paire choisie par le substitut n'est pas une paire dont les deux fiches sont dans la même niche ou le même axe (redondance grossière).
- **Vérification mécanique à battre** : un bras qui choisit au hasard a une aire de 0,50.

### (d) Ancrage matériel

- Modèle : aucun LLM pour le substitut lui-même ; le bras Gu-Krenn utilise un réseau entièrement connecté (141 traits, Pièce 20 (N9-1)).
- Calcul : réentraînement 8–30 h processeur par valeur d'IR (Pièce 20 (SD-3), R-873), ou carte graphique.
- Coût : machine louée, nœud de dépense non chiffré dans les pièces ; l'essai sur la moisson existante (sans réentraînement, juste le substitut par traits publiés) est processeur seul, ≈ 0 USD.

---

## N4 — Annexe du bras méta : profil presque vide

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| La loi a priori des niches (n1 0,30, n2 0,25, n3 0,15, n4 0,10, n5 0,15, n6 0,05) reflète la distribution réelle des fiches | HYPOTHÈSE | Pièce 11, §6 et Pièce 10, CA1-06 : « n6 5 % contredit les mots-indices de n6 et la structure en cinq axes » |
| La probabilité qu'une paire de fiches partage au moins une structure comptée est 0,3 | HYPOTHÈSE | Pièce 11, §6 : « indépendances » et « SUPPOSÉ » |
| Les structures « quasi universelles » (imposées par le texte I) ne comptent pas, alors que trois d'entre elles figurent dans la liste de 20 | OBSERVÉ-NON-AUDITÉ | Pièce 10, CA1-04 : « l'argument tient pour D1, mais le même argument vaut pour `om_somme_cumulee_temps_arret`, `om_martingale_e_processus` et `me_test_sequentiel_cusum` » |
| Le repli (hors profil) « éprouve la chaîne » de manière utile | HYPOTHÈSE | Le repli sélectionne la paire à deux indicateurs sur trois (Pièce 11, §6) ; ce n'est pas le profil que R-638 vise |
| Les paires déjà prises par un bras antérieur n'affectent pas la disponibilité du profil | Non pris en compte dans P14 | Pièce 10, CA1-09 : « `choisir_paires` retire des candidates les paires déjà prises par un bras antérieur » |

### (b) Expérience décisive

**Duel : le profil est-il éprouvable au pré-pilote ?**

- **H_A** : avec 10 fiches et les paramètres réels de l'annexe, au moins une paire du profil est disponible dans ≥ 60 % des lots (le profil est testé plus souvent que non).
- **H_B** : dans < 60 % des lots, le profil est vide et le bras tombe au repli.

**Métrique** : P(au moins une paire du profil disponible après retrait des paires prises par les autres bras), sur 100 000 tirages avec les paramètres réels de l'annexe, y compris I-11 (paires prises).

**Contrôle négatif** : même calcul avec les paires prises = ∅ (borne haute).

**Issue falsifiante** : si P ≥ 0,60, H_B est falsifiée : le profil est éprouvable ; si P < 0,60, H_A est falsifiée : le pré-pilote n'éprouve que le repli dans la majorité des cas.

**Ma position** : option **(a) — accepter le repli comme mesure au pré-pilote**, avec les conditions suivantes :
1. Le résultat du bras méta est étiqueté « repli » ou « profil » dans tout rapport.
2. Le brouillon 2 de l'annexe retire la paire n1–n2 du profil (CA1-01 : fusion par le programme) et écrit la limite de n5 (CA1-03).
3. Les jeux de données ne sont pas comptés comme « structure forte » (CA1-04 tranchée : la même logique d'exclusion s'applique aux trois structures séquentielles quasi universelles, nommément `om_somme_cumulee_temps_arret`, `om_martingale_e_processus`, `me_test_sequentiel_cusum` ; leur retrait ramène le profil à ≈ 2 paires de niches sur 15 et rend le problème encore plus aigu, donc la question est : les garder en comptant leur quasi-universalité comme limite, ou les retirer en assumant un profil quasi vide).

**Confiance** : 0,55.

**Pire cas** : le pré-pilote ne produit qu'un repli, et la course 2 est lancée avec un bras méta non éprouvé sur son profil. **Garde** : la course 2 à 24 fusions (8 par bras) fournit ≈ 8 occasions au bras méta ; si toutes les 8 sont du repli, le bras est déclaré « non éprouvé sur profil » avant la génération 2 (réserve écrite systématiquement).

**Option manquante** : fusionner n1 et n2 (grille à 5 niches, CA1-01) **et** retirer les trois structures quasi universelles de la liste comptée, puis recalculer le profil : cela pourrait ouvrir de nouvelles paires ou fermer le profil complètement. La pièce de calcul (script rejoué sur la grille à 5 niches) trancherait.

**Pièce qui trancherait** : le script v7 du calcul de puissance (Pièce 11, garde 22a) avec les paramètres réels et I-11 (paires prises). Coût : processeur, ≈ 0 USD.

### (c) Mesure minimale du bras méta (instrument)

- **Taux de détection** : sur le jeu d'essai synthétique (Pièce 11, 10 fiches), le bras sélectionne la paire de score maximal (e01–e04, score 2,0) — VÉRIFIÉ dans la pièce.
- **Fausses alertes** : une paire de même niche est refusée — VÉRIFIÉ (garde 22a, artefact, Pièce 11).
- **Vérification mécanique à battre** : un bras qui tire au hasard parmi les 45 paires ; le bras méta doit avoir un score moyen strictement supérieur.

### (d) Ancrage matériel

- Modèle : aucun LLM pour le score lui-même ; les lecteurs de niches et structures sont des LLM (Opus 5.5, Pièce 4 résumé point 4).
- Calcul : script Python, processeur seul.
- Coût : 0 USD pour le calcul ; le coût des lecteurs est dans le budget du pré-pilote (1,50 USD pour 60 lectures, Pièce 9).

---

## N5 — A21 et la règle de non-lecture

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| L'intention de A21 est de protéger contre une décision de l'orchestrateur qui dépende d'un résultat ou du rattachement d'un résultat à sa classe | RAPPORTÉ | Pièce 12, §C, point 3 : « L'intention (CP5-08) : qu'aucune décision de l'orchestrateur ne dépende d'un résultat » |
| É5 est impossible sans la classe des témoins | VÉRIFIÉ | Pièce 12, §C, point 2 : « tel qu'écrit, É5 (S20, A6, S19) est impossible sans connaître la classe de chaque témoin » ; Pièce 13, CL19-03 |
| La v55 journalise correctement les lectures | OBSERVÉ-NON-AUDITÉ | Pièce 13 : « la v55 rend la lecture visible et bornée (journal du coffre, rôle déclaré, raison, comptes seulement, aucune copie) » ; CL20 non encore faite |
| L'ordre des appels d'É6 n'a pas d'effet mesurable | HYPOTHÈSE | Pièce 12, §C, point 5 : « l'ordre des appels dépend de la classe. Les juges ne le voient pas (sessions isolées), mais si un juge est arrêté par A3 en cours d'étape, l'ensemble des fiches qu'il a jugées dépend de la classe » |

### (b) Expérience décisive

**Duel : la lecture par programme à É5 crée-t-elle un canal d'information exploitable ?**

- **H_A** : la sortie de la boîte d'É5 (passe/nœud + comptes) ne permet pas à un observateur de deviner la classe d'un témoin individuel au-delà du hasard.
- **H_B** : la sortie de la boîte d'É5 permet de deviner la classe d'au moins un témoin.

**Métrique** : aire sous la courbe d'un classifieur (logistique, sur les seuls comptes de sortie) qui tente de retrouver la classe de chaque témoin.

**Contrôle négatif** : la sortie ne contient que le total « passe/nœud » sans aucun compte par témoin ; l'aire est 0,50.

**Issue falsifiante** : si l'aire > 0,60 (illustratif), H_A est falsifiée : la sortie fuit. Si l'aire ≤ 0,50 à 1 erreur type près, H_B est falsifiée.

**Ma position** : option **(a) — amender A21 et la ligne 30**, avec les conditions :
1. La lecture est journalisée au coffre (horodatage, rôle « É5-garde », raison, comptes seuls — ce que fait déjà la v55).
2. L'artefact de la ligne 30 couvre « lecture hors journal » (l'essai R5 vérifie qu'une lecture non journalisée est détectée).
3. L'ordre des appels d'É6 est trié par identifiant opaque (Pièce 12, §C, point 5 : correction simple).
4. La sortie d'É5 ne contient pas la liste `primaires_non_ambigus` triée par classe (Pièce 12, §C, point 3(c) : la v55 doit ne sortir que des comptes).

**Confiance** : 0,75.

**Pire cas** : l'amendement de A21 crée un précédent : d'autres étapes ajoutent des lectures « journalisées » qui, ensemble, permettent de reconstruire la classe. **Garde** : chaque lecture supplémentaire de la clé exige une ligne nouvelle au préenregistrement avec son audit propre (R12).

Choix de code à confirmer :
- **Choix 1** (arrêt au premier « non mesuré ») : **oui** — cohérent avec O12 (rien n'en a été lu).
- **Choix 5** (N non vu par le relecteur → exclu) : **oui**, à condition que le nombre d'exclusions de ce type soit rapporté et que le seuil A5 soit recalculé en conséquence.
- **Choix 8** (à deux fiches, pas de report) : **oui** — lecture littérale ; l'effet sur C12 est à chiffrer dans le script de puissance.
- **Choix 10** (indices de forme) : **oui**, définition et crête à geler au préenregistrement.
- **`budget.portee_plafond`** : par génération (lecture cohérente avec GO-2026-10-31-04 : « chaque sous-session sous ce plafond »).

### (c) Mesure minimale de A21 (instrument)

- **Taux de détection de la garde** : sur un cas artefact (lecture non journalisée, simulée par un module d'essai qui contourne le coffre), la garde refuse É5. Sur un cas sain (lecture journalisée), la garde passe.
- **Fausses alertes** : sur 100 exécutions du cas sain, aucune fausse alerte.
- **Vérification mécanique à battre** : aucune vérification (pas de garde) donne 0 % de détection.

### (d) Ancrage matériel

- Modèle : aucun LLM pour la garde elle-même.
- Calcul : essais R5 du banc, processeur seul.
- Coût : 0 USD.

---

## N6 — DL-1 à DL-13 : épreuve semi-réelle

Je traite les 13 décisions en bloc, avec focus sur les plus conséquentes.

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| Les hypothèses du théorème 1 de Khemakhem et al. 2020 sont satisfaites par les indicateurs synthétiques du volet B-θ | HYPOTHÈSE | Pièce 15, résumé point 4 : « Bθv (théorèmes 1 et 2) : oui ; Bθc (iv échoue) : non » — vérification limitée aux indicateurs synthétiques |
| Le centrage intra-strate ferme le chemin de confusion par κ pour toutes les méthodes, y compris la prédiction invariante (M1) | Partiellement falsifié | Pièce 18, VS5-01 : « la raison d'être de κ disparaît, DL-12 est présentée avec une prémisse inexacte » — le centrage annule les moyennes résiduelles de tout ensemble sans C pour M1 |
| La puissance de l'étape d'estimation (0,78 à 0,90) est suffisante | HYPOTHÈSE | Pièce 18, VS5-03 : « PUISθ ne garantit pas la puissance revendiquée » ; la puissance suppose une corrélation de 0,85 entre représentation et latente (SUPPOSÉ) |
| 150 heures de calcul suffisent (marge de 1,26) | HYPOTHÈSE | Pièce 15, résumé point 8 : « temps unitaires SUPPOSÉS » |
| Les PDF manquants ne changent pas les hypothèses rivales gelées | HYPOTHÈSE | LiNGAM non versé (Pièce 15, DL-6) |

### (b) Positions et expériences par DL

**DL-1** : option **(2)** — B-θ décisionnel, B-hors descriptif. Confiance 0,65.
- Duel : H_A = dans le théorème, l'iVAE retrouve les latentes (coefficient moyen ≥ 0,70) ; H_B = l'iVAE ne fait pas mieux que M5 (VAE libre). Métrique : coefficient moyen apparié, seuil 0,70 (S11 du préenregistrement). Contrôle négatif : M5. Issue : H_B falsifiée si coefficient ≥ 0,70 sur ≥ 37/50 mondes (Wilson).

**DL-2** : option **(2)** — 5 graines, 150 h. Confiance 0,70.
- Le pire cas (dépassement de temps) est contrôlé par la réduction chiffrée (1,26 × temps unitaire tolérés, Pièce 15, DL-2).

**DL-3** : option **(1)** — R2⁻ décisionnelle. Confiance 0,55.
- Duel : H_A = les méthodes qui passent la qualification sous R détectent aussi un effet de signe opposé sous R2⁻ ; H_B = au moins une méthode qualifiée sous R échoue sous R2⁻. Métrique : recouvrement sous R2⁻. Contrôle négatif : T0 (plancher). Issue : H_B falsifiée si aucune méthode ne perd plus de 0,10 de recouvrement.

**DL-4** : option **(1)** — CITRIS hors gradation 1. Confiance 0,80. Raison : lui donner la cible d'intervention est lui donner ce qui fait l'identification.

**DL-5** : option **(1)** — permutation dans les strates de u, E = 50 %, PUISθ. Confiance 0,60.
- Duel : H_A = la sélection supervisée sur E₁ et le test par permutation sur E₂ donnent une fausse détection ≤ 0,01 ; H_B = la fausse détection dépasse 0,02. Métrique : taux de fausse détection sous effet nul sur 50 mondes. Contrôle négatif : monde sans effet de z₁ (Bθv0). Issue : H_B falsifiée si faux positifs ≤ 1 sur 50.

**DL-6** : option **(1)** — obtenir les PDF. Confiance 0,75. Raison : DL-9 exige la vérification de Reisach § 5.1.

**DL-7** : option **(2)** — arbitrer explicitement S3, S8, S9, S21, S23. Confiance 0,70.

**DL-8** : option **(4)** — u₂ seule, plantation sur toutes les années. Confiance 0,65. Raison : puissance 0,78 vs 0,49 à 3 environnements et 16 ans (Pièce 15, DL-8).

**DL-9** : option **(1)** — T2b redéfini sur la règle d'orientation de chaîne. Confiance 0,50. Raison : la règle est vérifiée sur PDF (Reisach p. 9), mais les seuils (0,20 et 0,05) sont choisis sans littérature.

**DL-10** : option **(3)** — descriptive, 30 mondes. Confiance 0,60. Raison : l'épreuve est « presque vraie par construction » (Pièce 15, DL-10, option 2) ; la rendre descriptive est suffisant ; + 5,0 h acceptable.

**DL-11** : option **(1)** — descriptive, 50 mondes. Confiance 0,65. Raison : contrôle commun de la synthèse v2 absent autrement.

**DL-12** : option **(1)** — centrage intra-strate, avec la correction de VS5-01 (réécrire la raison pour la prédiction invariante : le centrage ne favorise plus M1, il l'handicape possiblement — la limite est écrite). Confiance 0,55.

**DL-13** : option **(1)** — statu quo. Confiance 0,55. Raison : sans caractéristique opératoire calibrée (30 mondes, pas de calcul de puissance), imposer une règle nouvelle risque de rejeter des méthodes sans justification suffisante.

### (c) et (d) — Ancrage matériel global pour N6

- Modèles : iVAE (PyTorch), PCMCI (tigramite), DirectLiNGAM (lingam), ICA-LiNGAM, forêt d'arbres par gradient (scikit-learn), prédiction invariante. Tous en open source.
- Calcul : ≈ 118,6 h processeur (option DL-2 = 2, DL-1 = 2), 6,25 jours de temps mural (Pièce 15, résumé point 8).
- Coût : 0 USD (processeur seul, R-633).
- Budget cumulé par combinaison de DL : 93,3 à 135,7 h (Pièce 15, M §35).

---

## N9 — D-GK-1 : fenêtre du test hors échantillon

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| Le modèle de Gu et Krenn prédit l'apparition de liens (tâche de HB) alors qu'il a été entraîné pour l'impact (≥ IR citations) | HYPOTHÈSE | Pièce 20 (N9-1) : « HB est un transfert de tâche, déclaré comme tel » |
| Le graphe publié est complet pour les articles jusqu'au 31 décembre 2022 | HYPOTHÈSE | Pièce 20 (N9-1) : « hypothèse de travail » |
| La dérive d'OpenAlex (Walden, novembre 2025) est contrôlable par le pont | HYPOTHÈSE | Pièce 20 (SD-4), §4.5, point 1 |
| L'aire appariée attendue est ≈ 0,70 | HYPOTHÈSE | Pièce 20 (N9-1) : « SUPPOSÉ (aucun appui publié pour l'apparition pure) » |

### (b) Expérience décisive (c'est HB lui-même)

**H_A** : le modèle figé à 2022 classe les paires qui se relient en 2023–2026 au-dessus des paires qui ne se relient pas, à degré et âge égaux (aire appariée > 0,60, Pièce 20 (N9-1), seuil B-ii).

**H_B** : le modèle ne fait pas mieux que l'attachement préférentiel apparié (aire appariée ≤ 0,60).

**Ma position** : option **(a)** — population à fin 2022, fenêtre 2023–2026.

**Raison** :
1. La fenêtre (a) est un vrai hors échantillon sans conditionnement sur l'issue 2023.
2. La fenêtre (b) retire les positives les mieux classées (biais contre le modèle à seuils fixes, Pièce 20 (N9-1)) : ce biais rend l'interprétation d'un échec ambiguë (est-ce le modèle ou le conditionnement ?).
3. L'autre fenêtre est rapportée en information dans les deux cas.

**Confiance** : 0,70.

**Pire cas** : la fenêtre 2023 contient des liens « faciles » (concepts déjà proches en 2022) qui gonflent l'aire ; le modèle passe grâce à ces cas triviaux. **Garde** : rapporter séparément l'aire sur les paires reliées dès 2023 et celles reliées seulement après 2023 (déjà prévu dans la prédiction, Pièce 20 (N9-1) : « nombre et part des positives reliées dès 2023 »).

**Option manquante** : aucune option ne propose de fixer d'avance la tolérance sur le pont (écart de comptes d'arêtes entre le graphe reconstitué et le graphe publié, §4.5 point 1 de Pièce 20 (SD-4)). Cette tolérance devrait être gelée dans la v3.

### (d) Ancrage matériel

- Modèle : réseau entièrement connecté (141 traits), entraîné sur leur code public (MIT), données Zenodo (CC-BY).
- Calcul : réentraînement 8–30 h processeur (ou GPU), plus la moisson OpenAlex.
- Coût : machine louée (non chiffré dans les pièces) + requête OpenAlex (> 5 USD ou instantané 744 Go — Pièce 20 (SD-4), §4.3). Marqué illustratif : ≈ 10–50 USD au total selon la voie.

---

## N10 — Robustesse adaptative et course d'idéation

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| Le levier principal contre l'attaquant adaptatif est la capacité de la classe de moniteurs, non le tirage au hasard | OBSERVÉ-NON-AUDITÉ | Pièce 22, résumé point 4 : poids de B′ purs dans 62 % et 54 % des tâches ; Pièce 23, §2.4 : « substitut de capacité, pas gain à capacité égale » — sur le monde gaussien seulement |
| Ce résultat local (gaussien, linéaire/maxout, 2 δ) se transporte à de vrais modèles | HYPOTHÈSE | Pièce 22, « Ce que l'expérience n'autorise pas » : « rien sur les vrais modèles » |
| Le prix de l'évasion pour l'attaquant croît avec le nombre de couches (Bailey et al.) | RAPPORTÉ | Pièce 24, p. 23 : « 95% confidence interval for the Pearson correlation coefficient between the number of obfuscated layers and SQLEval performance was entirely negative » — sur un seul modèle (Llama-3-8B) et une tâche (SQL) |
| « Training models to be easier to robustly monitor appears to be a promising direction, but not at present a complete solution » | RAPPORTÉ | Pièce 24, p. 26 : citation exacte |

### (b) Position et expérience

**Ma position** : option **(b)** — poser la robustesse adaptative en génération 2.

**Raison** :
1. La course 2 est figée (texte, budget 24 fusions, GO-2026-10-31-04). L'option (a) la rouvre.
2. Le pilote synthétique n'est pas lu (brouillon 4 en cours, contre-lecture 3 en cours). Introduire un axe fondé sur un résultat non encore validé viole R1.
3. L'option (c) (sous-session à part) est viable mais prématurée : le pilote décisif (N = 100, Pièce 22, résumé point 7) doit d'abord être exécuté.
4. La génération 2 est le moment naturel : elle part du pré-pilote lu et peut inclure Bailey et al. dans les pièces.

**Confiance** : 0,70.

**Duel pertinent (pour la génération 2)** :

- **H_A** : il existe une classe de moniteurs et un budget de défenseur tels que le coût d'évasion pour l'attaquant dépasse le gain de l'évasion (l'attaquant ne peut pas échapper à tous les moniteurs sans dégrader sa performance au point de ne plus être utile).
- **H_B** : pour toute classe de moniteurs accessibles, l'attaquant peut toujours trouver un point d'évasion à coût d'évasion inférieur au gain.

**Métrique** : ratio (coût d'évasion / gain de l'évasion), où le coût d'évasion = dégradation de la performance sur la tâche (par exemple exactitude SQL, Pièce 24, p. 23), et le gain = taux de jailbreak réussi.

**Contrôle négatif** : moniteur trivial (seuil fixe sur la norme des activations) ; coût d'évasion attendu ≈ 0.

**Seuil (illustratif)** : ratio > 1 pour au moins une couche.

**Issue falsifiante** : si le ratio est < 1 pour toutes les classes de moniteurs testées, H_A est falsifiée. Si le ratio > 1 pour au moins une classe, H_B est falsifiée.

**Leviers qui rendent le prix supérieur au gain** (niveau méthode, demandés par la question) :
1. **Nombre de couches défendues** : Pièce 24 montre une corrélation négative. Le défenseur choisit les couches ; l'attaquant ne peut pas les retirer sans modifier l'architecture.
2. **Diversité de la classe de moniteurs** : le pilote montre que la pureté de l'équilibre dépend de la richesse de la classe ; une classe plus riche (par exemple noyaux, réseaux profonds) pourrait empêcher la pureté.
3. **Entraînement du modèle à être moniturable** (direction « training models to be easier to robustly monitor », Pièce 24, p. 26) : le modèle est modifié pour que la représentation interne soit plus lisible ; l'attaquant ne contrôle pas l'architecture du modèle.

**Qui pourrait vérifier** : un groupe extérieur disposant d'un modèle ≥ 8B et d'un budget GPU suffisant pour l'OAT de Bailey (≈ 10 h par graine sur un GPU, Pièce 24, p. 26 : « about 10 hours on a single GPU »).

### (d) Ancrage matériel

- Modèle : Llama-3-8B-Instruct (open, Meta) ou équivalent.
- Calcul : OAT = ≈ 10 h GPU par run × 5 graines (illustratif) = 50 h GPU.
- Coût illustratif : 50 h × 1–3 USD/h (location GPU A100) = 50–150 USD.

---

## N11 — Règle de reconduction des bras et ponts plantés

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut | Source |
|---|---|---|
| L'oracle du monde planté (bisociation v2/v3) fournit un classement des bras qui se transporte au domaine réel | HYPOTHÈSE | Aucune mesure de transport n'existe dans les pièces |
| 8 fusions par bras (course 2) permettent de détecter une domination d'un bras | HYPOTHÈSE | « À 24 fusions sur trois bras (8 par bras), un retrait est vraisemblablement hors de portée » — Question, N11 |
| Des ponts connus plantés dans la course 2 sont indiscernables des vrais ponts pour les proposeurs et les bras | HYPOTHÈSE | Aucun protocole de plantation en domaine réel n'existe dans les pièces |
| N-058 (composition jugée sur l'oracle, pas le juge) est opérationnel | VÉRIFIÉ | Pièce 26b : décision scellée |

### (b) Expérience décisive et réponses aux quatre points demandés

**(1) La règle de reconduction**

**Grandeurs** :
- Par bras b sur l'oracle synthétique (bisociation v3) : précision_b = (vrais promus + faux rejetés) / total_ponts_testés ; coût_b = coût_moyen_par_vrai_trouvé.
- Les « proches » et les « surfaces » sont rapportés séparément, jamais mélangés aux vrais (Pièce 3 : cinq statuts distincts).

**Critère de retrait** : borne haute de l'intervalle à 95 % de la précision du bras candidat au retrait, inférieure à la borne basse de l'intervalle du meilleur bras, sur les mêmes mondes.

**Part minimale d'exploration** : au moins 20 % (illustratif) des fusions de chaque génération vont au bras le moins performant, pour contrôler la régression (un bras qui progresse entre générations par apprentissage sur les fiches).

**Calcul de puissance** :

- **H_A** : le bras à retirer a une vraie précision inférieure de δ au meilleur.
- **H_B** : les deux bras sont à précision égale.

Métrique : puissance du test de supériorité (intervalle de la différence de précision). Sur le synthétique, avec N mondes (actuellement 2 400 pour M_bien, Pièce 3, S15), σ ≈ 15 (Pièce 3, S9), pour détecter un effet de 5 points : puissance ≈ 0,89 (Pièce 3, S14, par analogie avec J). Pour E1′ (rétrodiction sur littérature réelle) : le nombre de ponts est inconnu (HYPOTHÈSE) ; il faudrait ≥ 50 ponts pour détecter un écart de 10 points de précision avec puissance 0,80 (illustratif, calcul binomial standard).

Pour la course 2 à 8 fusions par bras : puissance ≈ 0,07 pour détecter un écart de 10 points de précision (illustratif, n = 8, binomial) — effectivement hors de portée, comme noté dans la question.

**(2) Les ponts plantés de la course 2**

**Source** : ponts publiés après la date de coupure des modèles proposeurs (≈ fin 2025 pour la plupart des LLM ouverts). Concrètement : articles publiés en 2026 dans le domaine du contrôle des IA qui établissent un lien entre deux sous-domaines auparavant non connectés. La source la plus fiable est le manifeste de la moisson OpenAlex (si disponible, via N9) ou une sélection manuelle par Lazar/session-depot avec PDF empreinté.

**Combien** : 4 ponts plantés (illustratif — même ordre que M6b, Pièce 8, D-g (b)). À 24 fusions + 4 ponts, le coût additionnel est ≈ 4 × coût d'une fusion (≈ 4 × 0,204 USD = 0,82 USD pour le coût de fusion seul, Pièce 4 résumé point 7 ; plus les lectures d'étiquettes).

**Plantation sans contamination** :
- Les ponts sont introduits comme « fiches supplémentaires » dans le vivier de parents, avec un identifiant opaque (même format que les fiches réelles).
- Les proposeurs et les bras ne savent pas quelles fiches sont des ponts (insu).
- La clé des ponts est scellée avant toute dépense (même protocole que la clé des classes de M6b).

**Juge de correspondance** : un pont est « trouvé » par un bras si la paire sélectionnée par le bras contient au moins une fiche dont le concept partagé avec le pont planté a un κ > 0,3 (illustratif) ; le juge est un programme (pas un LLM), aveugle au bras.

**Risque de non-ressemblance** : un pont publié en 2026 peut être plus « facile » (les deux sous-domaines convergent déjà) ou plus « difficile » (les proposeurs n'ont jamais vu les articles de 2026). Ce risque est contrôlé par le rapport des ponts trouvés par le meilleur bras / par le bras aléatoire.

**(3) Le transport**

**Condition** : le classement des bras sur le synthétique vaut pour le réel si et seulement si la corrélation de rang entre la précision synthétique et la précision sur les ponts plantés réels est positive et significative (Spearman ρ > 0, p < 0,05).

**Mesure de vérification** : les ponts plantés de la course 2 fournissent les données ; le synthétique (bisociation v3) est déjà disponible ; E1′ fournit une troisième mesure. Le triplet (rang synthétique, rang E1′, rang ponts plantés) est la base du test de concordance.

**Ce qui manque** : si les trois classements divergent, aucune règle de reconduction ne peut être appliquée ; la décision revient à Lazar.

**(4) Effet sur le pré-pilote**

Les ponts plantés **doivent être éprouvés au pré-pilote** (comme M6b), avec les mêmes contraintes :
- 1 à 2 ponts sur les 28 fonds (illustratif), étape protégée.
- La chaîne (plantation → aiguilleur → bras → fusion) est testée de bout en bout.
- Le coût additionnel est ≈ 0,5 USD (illustratif, même estimation que M6b à 2 fiches).

**Ce qui manque** : le protocole de sélection des ponts (qui les choisit, quand, comment éviter que conv-audit ne les voie — même cloison que pour M6b, DEP2c).

**Vérification hors du programme** : un évaluateur externe pourrait reproduire la plantation sur une autre moisson (par exemple un autre sous-domaine d'OpenAlex) et vérifier que les bras se classent de la même manière.

### (d) Ancrage matériel

- Modèle : aucun LLM requis pour la plantation elle-même ; les bras utilisent les LLM du pré-pilote.
- Calcul : processeur seul pour le calcul de puissance et la plantation ; le coût des fusions est dans le budget existant.
- Coût additionnel illustratif : ≈ 1–2 USD pour 4 ponts plantés au pré-pilote.

---

## Liens et ordre de tranchage

| Lien | Conséquence |
|---|---|
| N1 → N11 | La règle de reconduction (N11 (b)) dépend de la bisociation v3, qui dépend de la résolution de N1 |
| N4 → pré-pilote | Le gel du pré-pilote attend l'annexe approuvée (D-h (a) tranché) ; N4 doit être résolu avant le gel |
| N11 → N4 | Si des ponts plantés doivent être éprouvés au pré-pilote (N11 (4)), le gel du pré-pilote en dépend |
| N5 → pré-pilote | L'amendement de A21 doit être écrit au brouillon 8 avant le gel |
| N6 → calendrier | DL-2 fixe le budget de temps ; le calcul doit commencer ≈ 12 novembre pour finir avant fin novembre |
| N9 → N3 | Si HB échoue sur le domaine propre de Gu-Krenn, le substitut pour le contrôle des IA n'a aucune base ; D-j perd sa justification |
| N10 → course 2 | L'option (b) (génération 2) n'affecte pas la course 2 actuelle |

**Ordre proposé** : N1 → N4 → N11 → N5 → N3 (après N9) → N9 → N6 → N10.

Raison : N1 débloque N11, qui débloque une partie du gel du pré-pilote ; N4 est le bloquant principal du gel ; N5 est une correction de texte ; N3 et N9 sont liés ; N6 est sur un chemin indépendant (calendrier processeur) ; N10 n'affecte pas la course 2 actuelle.

FIN-DE-CELLULE