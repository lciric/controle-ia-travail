# Contre-lecture du préenregistrement du crible (iii), brouillon 8 — tour 2 de la lecture du brouillon 7 — v1

- Lecteur : sous-agent neuf du modèle C (R2), qui n'a écrit aucune des pièces ; auteur de la pièce : modèle A. Rédigé le 2026-11-16 de 15:29Z à 15:36Z (`date -u`).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon8.md`, `d3406878de798040561e77289066c9c99bf2cee1c644f1f92a3510d52f6bcd1d` (égale à son compagnon). Brouillon 7 : `8be79b00430f06a3f74f5abe9d0985d8246036565c92220c202689d3d004a7fd` (égale à son compagnon). Rapport du tour 1 : `4803c83b98d6c8fba7a5d9b8e8a5915a65694f995fc0b68138eb197d16c9a5b3` (recalculée, égale à son compagnon). Programme `appliquer-corrections-crible-iii-brouillon8.py` : `50e2ae426d3c2bb5c394f53055c7c58275a83da33e7c2964365fd255317c18c1` (égale à son compagnon).
- Non lu, par consigne : sortie du pilote MR-2 v14, `diag/`, `runs/`, `donnees/`, 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque, dossiers jetables du premier contre-lecteur.

## Verdict

**« scellable »** : aucune correction exigée. Les onze couples du rapport du tour 1 sont appliqués fidèlement et rien d'autre ne change hors l'en-tête et la section « Contre-lecture ». Quelques remarques facultatives (section 4).

## 1. Fidélité des corrections (différentiel brouillon 7 vers 8)

- Rejeu par programme (bibliothèque standard) : les 11 couples « ancien → nouveau » extraits du rapport du tour 1 (A1 à A3, B1 à B3, C1 à C4, D1) ; chaque « ancien » figure **une seule fois** dans le brouillon 7 ; appliqués en mémoire, ils donnent un texte qui ne diffère du brouillon 8 que par : le titre (« brouillon 8 »), une puce d'en-tête (brouillon 8), le statut, la ligne du validateur, l'entrée 7 de la section « Contre-lecture » (nouvelle), les deux paragraphes « Tour suivant » et « Fichiers à lui donner » (mis à jour au brouillon 8). Rien d'autre (`diff` ligne à ligne vérifié). Aucune correction appliquée de travers, aucune oubliée.
- Le texte du rapport lui-même est celui lu par le programme (empreinte citée juste).

## 2. Passages touchés relus et vérifications dérangées

1. **Ligne du minimum (A1 à A3)** : « complets + en cours + non commencés < 16, évalué à chaque fin de monde, 20 à l'instant 0 » ; équivaut à « au moins 5 mondes incomplets » ; cohérent avec l'essai sain (démarrage : 0 + 5 + 15 = 20, continue), l'artefact (cinq mondes incomplets sur 20 d'emblée : arrêt) et avec la condition finale n_c ≥ 16 (section « Seuil », étage 1) : à l'arrêt, n_c ≤ 15, donc l'étage 1 donne bien « non concluant ». L'exception de l'étage 0 est cohérente. Les probabilités du minimum (section « Seuil ») ne changent pas : elles portent sur la condition finale, identique. Aucun autre passage n'emploie l'ancienne forme.
2. **Garde de taille (B2, B3)** : le texte servi vaut ≤ 52 000 octets, G2 ajoute moins de 1 000 octets (ligne des hypothèses de coût) : le cas sain (≤ 53 000) passe, l'artefact de 53 001 est refusé. Recompte : (53 976 + 1 024) = 55 000 ; 55 000 × 4 + 89 000 × 20 = 2 000 000 soit 2,00 USD (Pr-2) ; 55 000 × 8 + 64 000 × 40 = 3 000 000 soit 3,00 USD (Pr-4) : égaux aux plafonds de session. À 53 000 octets servis : 1,996 et 2,992 USD, sous les plafonds. Juste.
3. **III-7 (B1)** : D = passe 1 de Pr-2 + un appel de Pr-4 ; S = un appel de Pr-4 ; donc $_D/$_S = 1 + c₁/c₄ : la formule est juste, la fourchette de ± 0,05 est écrite, le repli sans sonde (1,05 à 1,25) est écrit, aucune autre prédiction ne se refait. Pas de porte de sortie après lecture.
4. **Enveloppe (C3)** : 123 + 483 + 243 + 196,60 + 263 = 1 308,60 ; + 7 = 1 315,60 : juste. Devis inchangé et recompté : 100 appels (Pr-4 : 60 ; Pr-2 : 40) ; attendu 60 × 1,60 + 40 × 0,80 = 128,00 + 0,30 de machine = 128,30 ; pire 60 × 3,00 + 40 × 2,00 = 260 + 3 = 263. Plafond de 2,34 USD (deux proposeurs de la forme fidèle) : non employé dans la variante, la pièce n'en use pas. Ligne GO-2026-11-15-06 (`registres/go.md`, l. 339) : 1 275 USD au pire pour les cinq cribles, « crédits de Claude employés au maximum » ; la pièce dit elle-même que la somme des pires cas dépasse 1 275 (nœud de Lazar, R-2992 point 3).
5. **Étage 5 (C2)** : le libellé nouveau est exact : B (Pr-2 écrit sur les ensembles de D) compare deux écrivains et ne retire pas la frontière ; le nom de R-2977 est rappelé. N-045 point 3 est cité avec cette réserve ; voir le point de la mère 2.
6. **Durée (C1, D1)** : « deux étapes en série : passe 1, puis D et B ; S et H en même temps » ; l'essai à blanc éprouve le lanceur et non la limite réelle du fournisseur, la concurrence réelle étant éprouvée au premier tour des files, sous la ligne « limite de débit » (point 13). Cinq files de quatre mondes, 3 000 s par appel, 7 200 s par monde, pire cas d'une file 8 h, garde de départ 10 h, sous la minuterie de 17 h ; le code du pilote ne suffit pas, lanceur, gabarits, filtre, files et mesure sont neufs et la pièce le dit nettement. Inchangé et juste.
7. **Annexe A (C4)** : la demande de versement au dépôt avec compagnons avant le scellement est écrite ; le versement n'est pas fait (l'application ne change que le texte, dit ainsi) : c'est un acte de la mère avant le scellement, voir point 3.

## 3. Points 1 à 9 de la consigne, état après corrections

(1) R1 complet, sans porte de sortie après lecture. (2) R3 : justifications avant toute donnée présentes ; bras « tout bon marché » (B) réemploie la passe 1 et reste comparable à D sans fuite (texte servi égal à l'octet, H indépendant). (3) Forme : la variante répond à la question de la note en mettant 99,8 % de l'attendu (127,70 sur 128,30 ; 3 USD hors crédits sur 263 au pire) sur crédits de Claude ; elle change un peu la question (deux paliers de prix d'une même maison, diversité d'espèces perdue), ce que la pièce dit sans trancher ; **recommandation nette pour la mère : retenir la variante, déjà tranchée par R-2992**, confiance 0,65, sous réserve du solde de crédits (260 + 7 au pire) ; la forme fidèle ne tiendrait le contraste de prix qu'au prix public promotionnel. (4) Devis recompté : section 2, points 2 et 4. (5) Durée : section 2, point 6. (6) Liste d'arrêt : chaque garde a son cas sain et son artefact (la ligne du minimum et la garde de taille comprises) ; graines par `numpy.random.SeedSequence`, clés sans collision ; minimum 16 sur 20 avec sa règle corrigée. (7) Ablation de la frontière aux critères gelés : bien définie (comparaison d'écrivains), sans contradiction de N-045 hors du crible, la pièce disant que les courses la gardent rapportée. (8) Aucun chiffre de l'état de l'art ; antériorités à chercher ; citations obligatoires présentes. (9) `controle_ia.prereg.problemes` sur le brouillon 8 : liste vide ; aucun identifiant de modèle (restent les clés de configuration `opus55`, `fable52`, `argon` permises) ; mentions « lettre C » : seulement dans les entrées historiques ; empreintes de la nouvelle entrée 7 (brouillon 7, rapport du tour 1) recalculées par `sha256sum` : justes, avec leurs deux empreintes entières ; tête de `main` `64540acd` : exacte.

## 4. Remarques facultatives (non exigées)

- R-a : le statut dit que la version qui fera foi ne refait « que ce que la table liste », alors que la règle de III-7 est écrite sous la table, non dans une de ses lignes ; le même paragraphe dit « seule III-7 se refait », ce qui lève l'ambiguïté. Le rédacteur l'a relevé lui-même. Laisser tel quel, ou ajouter une ligne III-7 à la table dans la version qui fera foi.
- R-b : « sans perte notable » de P2 et fourchette de la machine en série : voir tour 1, inchangés.
- R-c : la puissance de P1 reste à calculer avant le scellement (annoncée, sans effet sur un seuil).

## 5. Points pour la mère

1. Scellement : la pièce est scellable sous réserve de ses trois valeurs processeur (part des distracteurs, puissance de P1 et P2, taux d'erreur de l'intervalle), de la table de mise à jour d'après la lecture du pilote et du taux recopié ; un tour différentiel sur ces ajouts reste prudent.
2. Étage 5 de (iii) aux critères gelés (R-2977) contre (v) hors critères gelés (R-2992 point 2) : à confirmer, ou passage en « rapporté sans verdict ».
3. Avant le scellement : verser au dépôt, avec compagnons, les deux programmes de l'annexe A et leurs sorties (C4) ; inscrire le gel de III-6 dans `registres/decisions.md`, daté à l'heure, avant la lecture du pilote par son lecteur neuf.
4. Enveloppe 1 308,60 (1 315,60 avec la sonde) contre 1 275 : nœud de Lazar si le dernier crible n'y tient pas ; solde de crédits de Claude à vérifier.
5. Fragilité du minimum à N = 20 (environ 0,49 de « non concluant » à un taux de 0,95 par appel) : risque à accepter ou démarrage échelonné ; la concurrence réelle de 20 sessions n'est éprouvée qu'au réel.
6. Code neuf, lancement visé du 21 au 24 novembre, au-delà de l'autonomie : mot de Lazar requis ; GO-2026-11-15-06 jusqu'au 30 novembre.

## Incidents (de ma main)

Aucun. Aucun appel de modèle, aucune dépense, aucune machine, aucun `pytest`, aucun clone, aucun `git fetch` ; lectures seules (fichiers du dossier des cribles, lignes de `registres/go.md` et de `registres/decisions.md` par `grep`) ; rejeu léger du différentiel et du validateur sur processeur ; aucun fichier existant modifié.
