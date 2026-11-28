# Vérification de la synthèse v3 « comment détecter » — angle « fidélité des corrections », tour 2 — v1

## Verdict : **conforme après corrections**

- **Les 33 constats du tour précédent sont appliqués**, aux lignes que donne le traitement : VV2-fidelite-01 à 14 (notés
  F-01 à F-14) et VV2-sens-01 à 19 (notés S-01 à S-19), plus les deux corrections hors constat. Les 25 écarts VS-01 à
  VS-25 restent en place : aucune régression.
- **Différentiel : rien d'autre n'a changé.** 27 blocs au différentiel mot à mot v2 → v3, soit les 23 blocs et la
  substitution dans une ligne du journal du correcteur. Chacun se rattache à un constat ou à l'en-tête.
- **Chiffres nouveaux ou déplacés : tous sur leur page.** 81 phrases et chiffres à la page exacte citée, avec leur forme
  française dans la v3 ; 23 lignes de table (ligne imprimée et colonne) ; 38 renvois au dépôt à la ligne citée : 0 écart.
  Table 9 de [DYL] recomptée : 22, 8 et 2 égalités, comme la v3.
- **Phrases anglaises citées : toutes sur leur page.** 192 passages entre guillemets ; 145 se trouvent dans un PDF ; 106
  confirmés à la page citée par le script ; les 39 autres relus à la main (titres, noms, citation placée avant le
  passage) : tous sur leur page.
- **Épreuve R5 de mon contrôle** : 14 artefacts, 14 rejetés.
- **7 constats : 3 mineurs, 4 de forme.** Aucun chiffre à retirer. Le plus grave : une règle gelée du préenregistrement
  scellé de P3 citée avec un mot changé. Toutes les corrections sont locales ; aucune ne change le verdict de la synthèse
  ni sa recommandation.

## Cadre

- **Objet.** `…/revue-detection/synthese-comment-detecter-v3.md` (sha256
  `ec4239e9da0a6b8282ce0b685695fcb71b2777038fd18618b096797502ae6890`), comparée à la v2 (`90ad38bf…`, inchangée).
  Traitement : `…/revue-detection/traitement-verification-synthese-tour2-v1.md` (`23fd956e…`). Rapports du tour
  précédent : fidélité `12a9fac2…`, sens `8ec6aa0e…`. Aussi : v1 (`a47f9141…`), vérification du premier tour
  (`43986648…`), traitement du premier tour (`c87ecdec…`). Les huit compagnons sont égaux.
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni la v3, ni les extractions, ni la vérification du premier
  tour, ni les vérifications du tour précédent, ni les traitements. 2026-10-20, de 12:15 à 12:50 UTC environ.
- **Lecture seule.** Aucune écriture dans le dépôt. Git en lecture seulement (`git log`, `git show`) ; le différentiel est
  calculé hors du dépôt (`git diff --no-index`). Non ouverts : `prereg/P3-consignes-v1.md`, textes d'action, clés. Aucune
  recherche web, aucun service payant, aucun contact, aucune commande Vast.ai.
- **Exposition (R1).** Relues **chiffres masqués** : [V] l. 170-172 et 358-359 ; note du brainstorm l. 8, 26-27, 43,
  72-86 ; `proposition-C.md` l. 323-324 ; `proposition-D.md` l. 81-99 ; `reponses.md` l. 370-373 ;
  `registres/decisions.md` l. 446. Le libellé reste lisible et dit le sens de certaines comparaisons. Aucune valeur ni
  aucun sens n'est recopié ici. Ce vérificateur ne doit pas rédiger P3b. De `resume.json`, seuls `resultat.duree_s` et
  `resultat.commit_cite` ont été lus.

## Méthode

1. **Empreintes.** Les 8 entrées ; les 22 PDF, RO compris, en empreinte complète : égales à
   `…/revue-detection/redaction/citations-synthese-v1.json` (RO : section 6 de la v3). Les 16 pièces du dépôt dont la v3
   donne l'empreinte : égales (`registres/depenses.md`, cité sans empreinte, relu aux lignes citées). Le dépôt n'a pas
   bougé depuis `8bd4a75` (11:55 UTC).
2. **Différentiel mot à mot** v2 → v3 : `git diff --no-index --word-diff=plain --word-diff-regex='[^[:space:]]+' -U0`
   (`…/verif-v3-fidelite/differentiel-mot-a-mot-v2-v3.txt`). Chaque bloc et chaque retrait relus et rattachés.
3. **Pages relues directement**, sans les pages ni les scripts du correcteur ou des vérificateurs précédents : `pdftotext`
   (modes défaut, `-raw`, `-layout`), en mémoire, après contrôle d'empreinte (`…/verif-v3-fidelite/page3.py`).
   - `guillemets_v3.py` : tous les passages entre guillemets de la v3, cherchés dans toutes les pages des 22 PDF, avec la
     page citée la plus proche (`sortie-guillemets-v3.txt`).
   - `verifier_v3.py` : (A) phrases et chiffres nouveaux ou déplacés, à la page exacte, forme française présente dans la
     v3 ; (B) lignes de table ; (C) renvois au dépôt, présence à la ligne citée, rien d'imprimé ; (D) épreuve R5 ;
     (E) preuves des constats (`sortie-verification-v3-fidelite.txt`).
   - Reproduire : `python3 -I -B …/verif-v3-fidelite/verifier_v3.py` ; une page :
     `python3 -I -B …/verif-v3-fidelite/page3.py CLE PAGE "phrase" [largeur] [mode]` ; une ligne :
     `page3.py --ligne CLE PAGE "fragment" [raw|layout]`.
   - « l. » d'un PDF = ligne du texte de la page sorti par `pdftotext -raw` (`-layout` pour une table) ; « l. » de la v3 =
     ligne du fichier v3.
4. **Code** : `propositions.py` (`5d97b223…`) et `episode.py` (`79113b49…`) identiques à `97dd829` et à `7a54d43` ;
   `propositions.py` l. 32-49, 129-138, 245-269 relues.

## Constats, le plus grave d'abord

### Mineurs

**VV3-fidelite-01 — S-04 : la règle gelée de [P] l. 272-274 est citée avec un mot changé.**
- Où : v3 l. 199-200 (règles communes) : « « Non au-dessus » se lit « non détecté à cette puissance », jamais « pas de
  trace » ([P] l. 272-274) ». Aussi l. 236 (E1, tranche) : « Oracle non au-dessus : « non détecté à cette puissance »
  ([P] l. 272-274), jamais « pas de trace » ».
- Source : `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`) l. 273 : « **« Non au-dessus »** se lit « non détecté à
  cette puissance », jamais « ne sépare pas » (TC-04) ». « pas de trace » n'est pas dans les l. 272-274.
- Problème : la v3 reproduit la règle mot à mot, entre guillemets, avec son renvoi, et remplace le terme gelé. Le sens va
  dans la même direction (« pas de trace » est un cas de « ne sépare pas »). Mais une règle gelée d'un préenregistrement
  scellé est citée inexactement, dans les règles communes qui serviront à écrire P3b. Le contrôle C du correcteur a bien
  lu « jamais « ne sépare pas » » à [P] l. 273 (`…/correcteur-tour2/outils/controler_v3.py` l. 514), mais sans le
  comparer au texte de la v3 ; son contrôle A range « pas de trace » parmi les passages français sans source (l. 82).
- Correction : l. 199-200 : « « Non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas »
  ([P] l. 272-274) ; a fortiori jamais « pas de trace » ». L. 236 : même forme, ou « pas de trace » sans guillemets.
- Reproduire : `awk 'NR>=272 && NR<=274' prereg/P3-premier-test-i-a-v1.md` ; sortie, section E, lignes « 01 ».

**VV3-fidelite-02 — S-02 : [AU] rangé parmi les montages « en moyenne sur les jetons » ; la page dit les 10 derniers
jetons.**
- Où : v3 l. 55-58 (verdict, point 2) : « donnent des aires modestes, en moyenne sur les jetons : … 0,653 sur toutes les
  actions, sur Phi-4 [AU p. 6] » ; l. 62 : « Ces montages agrègent par la moyenne ; P3, par le maximum ou l'attention » ;
  l. 176 (rang 3) : « montages proches (rien d'écrit dans l'empan lu), en moyenne : … 0,653 contre 0,948, toutes actions
  [AU p. 6] ».
- Source : [AU] p. 7 l. 1-4 : « Step 2: Add PyTorch hooks [22] after layer 20 and run the model's forward pass to cache
  activations for the last 10 tokens for each datapoint. Step 3: Train a logistic regression probe on the activations of
  these tokens to predict the label. Step 4: Follow the same procedure to evaluate the probe ». Aucune page de [AU] ne dit
  un score moyen sur les jetons (recherche sur toutes les pages : seules des moyennes glissantes montrées en figure,
  p. 7, p. 17, p. 21). De plus, « Action (AUC = 0.653) » (p. 6 l. 9) est lue sur la seule action : « the "+X" notation
  means the prompt includes all inputs above and including X » (p. 6 l. 40). La moyenne est bien dite pour [BX] (p. 3
  l. 70-71 : « average scores across tokens at evaluation ») et pour [YS] (p. 3 l. 11 : « average token activations
  over just the assistant's response »).
- Problème : la v3 étend à [AU] une agrégation que la page ne dit pas, dans le verdict, à l'endroit même où elle oppose
  l'agrégation de la littérature à celle de P3 (N-026). Le texte vient de la correction proposée par S-02 ; le
  traitement relit [AU] p. 6, pas p. 7.
- Correction : point 2 : « … 0,81 [BX p. 5], 0,63 [BX p. 6] et 0,606 [YS p. 3], en moyenne sur les jetons ; 0,653 sur
  Phi-4, sonde lue sur les 10 derniers jetons de la seule action, agrégation non dite [AU p. 6-7] » ; et « [BX] et [YS]
  agrègent par la moyenne, [AU] lit les derniers jetons ; P3, par le maximum ou l'attention ». Rang 3 : même précision.
- Reproduire : `page3.py --ligne AU 7 "activations for the last 10 tokens" raw` ;
  `page3.py AU 6 "notation means the prompt includes all inputs" 300` ; sortie, section E, lignes « 02 ».

**VV3-fidelite-03 — S-14 : « vers le maximum seulement sous dilution » ; la table 3 de [PAR], citée juste au-dessus, dit
l'inverse.**
- Où : v3 l. 155-157 (2.2, « Pour P3 ») : « les preuves publiées penchent vers la moyenne et l'attention en performance
  [PAR p. 7 ; MK p. 4 ; AP p. 22], vers le maximum seulement sous dilution, au prix de faux positifs [GM table 3,
  p. 12] » ; l. 180 (rang 7) : « les preuves penchent vers la moyenne et l'attention, sauf dilution ».
- Source : [PAR] table 3, p. 7 (layout l. 16-22), colonne « Dilution » : « Full Averaging (Pairs) » 0.931 contre « Peak
  Activation (Pairs) » 0.811 ; « Full Averaging (RP) » 0.907 contre « Peak Activation (RP) » 0.877. Sous dilution, la
  moyenne gagne pour les deux sondes. Hors dilution, avec la sonde RP, le maximum gagne sur trois jeux sur quatre : AI Liar
  0.929 contre 0.914, Backdoors 0.650 contre 0.550, Sandbagging 0.891 contre 0.828 (il perd sur Insider Trading, 0.935
  contre 0.999). Le jeu de dilution est fait pour mettre la moyenne en
  défaut (p. 4 l. 26 : « appending to the assistant's response 100 true-but-irrelevant claims »), et les auteurs le
  disent (p. 7 l. 47 : « even in scenarios specifically designed to challenge it (such as deception dilution) »).
  L'appui « sous dilution » ne vient que de [GM] : maxima appris par tête, contexte long, attaques (table 3, p. 12).
- Problème : la phrase de synthèse contredit une table que la même section cite. Elle confond le maximum brut (celui de
  [PAR], en partie celui de P3) et le maximum appris ([GM]). Elle pèse sur le nœud N-026 (« sens inconnu »).
- Correction : « les preuves publiées penchent vers la moyenne et l'attention en performance [PAR p. 7 ; MK p. 4 ;
  AP p. 22], sauf la sonde RP de [PAR], où le maximum brut gagne sur trois des quatre autres jeux ; sous dilution, le
  maximum brut perd chez [PAR] (jeu « Dilution », table 3, p. 7), les maxima appris gagnent en contexte long chez [GM],
  au prix de faux positifs (table 3, p. 12) ». Rang 7 : « … sauf la sonde RP de [PAR] ; sous dilution, résultats
  opposés ([PAR] ; [GM]) ».
- Reproduire : `page3.py --page PAR 7 layout` (l. 16-22) ; sortie, section E, lignes « 03 ».

### Forme

**VV3-fidelite-04 — F-08 : « la même sonde lue sur toute la réponse » ; [AP] p. 23 compare deux sondes différentes.**
- Où : v3 l. 52-54 (point 1) et l. 177 (rang 4) : « rappel à 1 % de faux positifs meilleur que la même sonde lue sur
  toute la réponse ».
- Source : [AP] p. 23 l. 8 : « here we train a different probe (on just the last positions of the training data) » ;
  l. 11 : « Both probes were trained on the Roleplaying dataset » ; l. 12-13 : « Recall at 1% FPR compared to control
  does show improvement, although is still subpar compared to the probe trained on Instructed-Pairs ». Le seuil de 1 %
  est fixé sur le témoin. La v3 le dit juste en 2.2 (l. 125-128).
- Correction : « rappel à 1 % de faux positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes
  les positions (moyenne), mais en dessous de la sonde Instructed-Pairs [AP p. 23] ». Le libellé vient de la correction
  proposée par F-08.

**VV3-fidelite-05 — S-18 : « hors de la famille de Bonferroni » rattaché à N-026.**
- Où : v3 l. 200-202 : « la moyenne seulement en « bras de diagnostic, jamais en production », lu « l'agrégation
  explique-t-elle le nul ? », hors de la famille de Bonferroni (N-026, conditions 1 à 4) ».
- Source : `docs/decisions/decision-N-026-v1.md` (`85bd4023…`) l. 18-25 : libellé (1), même plancher (2), jamais
  moniteur ni revendication (3), lecture de diagnostic (4). Le mot « Bonferroni » n'est nulle part dans la note.
- Correction : « (N-026, conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse (S-18) ».

**VV3-fidelite-06 — F-03 : sous « Contre », Qwen3-4B est un cas où la sonde de question bat la moyenne.**
- Où : v3 l. 236 (E2, tranche) : « Contre, sur les cas proches : … sonde de question basse sur Qwen3-8B (0,69) et
  Qwen3-4B (0,68) [DYL table 9, p. 28] ».
- Source : [DYL] table 9, p. 28 (layout l. 32, colonnes AA, Apollo, DYL Probe, Judge Model, Unrelated Qs) :
  « Qwen/Qwen3-4B 14 0.64 0.68 0.85 0.74 » : la moyenne d'Apollo y est plus basse (0.64) que la sonde de question
  (0.68). Qwen3-8B (l. 33) : 0.74 contre 0.69.
- Problème : chiffres justes, mais rangés comme argument contre la question, sans dire que sur Qwen3-4B l'autre lecture
  fait pire (R4, symétrie).
- Correction : « sonde de question basse sur Qwen3-8B (0,69 ; moyenne 0,74) et Qwen3-4B (0,68 ; moyenne plus basse
  encore, 0,64) [DYL table 9, p. 28] ».

**VV3-fidelite-07 — S-09 : « (v1 : 60 %) » ne porte pas sur la même proposition.**
- Où : v3 l. 251 : « ≈ 40 % (v1 : 60 %) que E1 dise d'où vient le nul ».
- Source : v1 (`a47f9141…`) l. 129 : « ≈ 60 % que E1 et E2 disent d'où vient le nul ».
- Problème : la v1 comptait E1 et E2 sur la même passe ; la v3 ne compte que E1. Une part de la baisse vient du retrait
  de E2, non d'un fait nouveau.
- Correction : « ≈ 40 % (v1 : 60 %, pour E1 et E2 ensemble) que E1 dise d'où vient le nul ».

## Fidélité, constat par constat

| constat | appliqué (v3, lignes) | relu sur | juste | complet | constat ici |
|---|---|---|---|---|---|
| F-01 | 236 | [DYL] p. 10, 11 | oui | oui | — |
| F-02 | 143-149, 288-290 | [GM] p. 6, 7, 8 ; table 3 p. 12, colonnes LC[A] et LC[RT], 16 lignes | oui | oui | — |
| F-03 | 236 | [DYL] table 9 p. 28 | oui | oui | 06 (forme) |
| F-04 | 137-142, 177 | [MK] p. 4 | oui | oui | — |
| F-05 | 159-164, 283-287 | [OA] p. 1 | oui | oui | — |
| F-06 | 49-52, 82, 178, 236 | [DYL] p. 2, 10, 12 ; [CA] p. 8, 18 | oui | oui | — |
| F-07 | 85, 107-108 | [AG] p. 17, 43 | oui | oui | — |
| F-08 | 52-54, 127-128, 177 | [AP] p. 23 | phrase oui ; libellé court non | oui | 04 (forme) |
| F-09 | 31-41, 360-362 | `recouper_v2.py` (`main`, l. 54-70) ; sortie du vérificateur (`01791e30…`, « 155 phrases ; 0 absentes ») | oui | oui | — |
| F-10 | 219-221 | — (retrait) | oui | oui | — |
| F-11 | 220-221 | [V] l. 345 | oui | oui | — |
| F-12 | 217-218 | [P] l. 318-320 | oui | oui | — |
| F-13 | 86 | [AU] p. 6 | oui | oui | — |
| F-14 | 237, 297-298 | `registres/decisions.md` l. 461 | oui | oui | — |
| S-01 | 235, 238, 259-274 | [P] l. 242-247 ; [V] l. 170-172, 358-359 (masquées) ; note l. 8, 83-85 ; `proposition-C.md` l. 323-324 ; `decisions.md` l. 446, 453, 456 | oui | oui | — |
| S-02 | 55-64, 75, 176 | [BX] p. 3-6, 8 ; [AU] p. 6-7 ; [YS] p. 3 | [AU] non | oui | 02 |
| S-03 | 45-54, 65-67, 78-79, 82, 177, 182, 235-238, 243-256, 275-282 | [AP] p. 5, 9, 18 ; [PAR] p. 4-7 ; [DYL] p. 2-12, table 9 (recompte 22, 8, 2) | oui | oui | 06 (forme) |
| S-04 | 67, 197-200, 236, 251-256 | [P] l. 238-241, 272-274 ; [KU] p. 5 ; [AP] p. 18 | citation de [P] altérée | oui | 01 |
| S-05 | 235, 275-282, 299-303 | [P] l. 415-416, 428 ; `go.md` l. 32 | oui | oui | — |
| S-06 | 209-216, 239 | `propositions.py` l. 32-49, 129-138 (deux commits) ; [P] l. 161 (P3-P6) | oui | oui | — |
| S-07 | 223-227, 235, 275-282 | note l. 26-27 ; `proposition-D.md` l. 81-99 (masquées) | oui | oui | — |
| S-08 | 235-239 | [KU] p. 5 ; [K] p. 3 ; [RH] p. 27 ; P-011 l. 30-42 ; note l. 72-78 | oui | oui | — |
| S-09 | 169-186, 251-256, 365-366 | v1 (colonne « pouvoir » de la section 3 ; confiance, l. 129) ; [K] table 1 p. 7 | oui | oui | 07 (forme) |
| S-10 | 235-239 | brief l. 48 | oui | oui | — |
| S-11 | 190-198, 239 | [P] l. 158, 238-248, 278 ; [AD1] l. 34 | oui | oui | — |
| S-12 | 235-236 | — | oui | oui | — |
| S-13 | 235, 239 | [V] l. 204 ; `reponses.md` l. 370-373 (masquées) | oui | oui | — |
| S-14 | 79, 85, 133-157, 180 | [PAR] table 3 p. 7, p. 4 ; [GM] table 1 p. 8, table 3 p. 12 ; [AG] p. 43 | chiffres oui ; synthèse « sous dilution » non | oui | 03 |
| S-15 | 159-164, 283-287 | [OA] p. 1 | oui | oui | — |
| S-16 | 49-52, 83, 178, 236, 319-320 | [CA] p. 8, 18, 25 ; [DYL] table 9 | oui | oui | — |
| S-17 | 202-204, 243-249, 259-274, 299-310 | `decisions.md` l. 453, 456, 457, 468-469 ; `go.md` l. 35 ; N-029 l. 37-39 ; commit `c1987d6` à 11:44 UTC | oui | oui | — |
| S-18 | 190-202, 235-236 | N-026 l. 18-25 | oui | Bonferroni rattaché à N-026 | 05 (forme) |
| S-19 | 228-231 ; 181 ; 100-104 ; 87, 175, 236 | [P] l. 385 ; `resume.json` (`duree_s` seul) ; [FQ] p. 3 ; [AP] p. 5 ; [DYL] p. 8 ; [EM] p. 38 ; [K] p. 3 | oui | oui | — |
| hors constat 1 | 76 | [YS] p. 3 | oui | oui | — |
| hors constat 2 | 361 | — | oui | oui | — |

Points vérifiés en plus : les deux adaptations déclarées (F-03, seconde option ; S-17 (a), nœud 4 tranché pendant la
correction : `c1987d6` versé à 11:44 UTC, correction de 11:35 à 12:20) ; « Varied Deception » est le banc du mensonge
sur consigne ([DYL] p. 3, p. 5) et « AA » l'indice de capacité ([DYL] p. 2) ; le sous-rendement d'[AP] et de [PAR] est sur
consigne ([AP] p. 5 l. 17 ; [PAR] p. 4) ; « from there up » renvoie au plus petit modèle de chaque famille ([CA] p. 8
l. 104) ; « A2 » est rangée sous « Options tombées » (note l. 83-85) ; P-011 range les paires synthétiques des tâches
de réserve parmi les données génériques (l. 30-35), d'où le « jeu synthétique tenu à part » de E3 ; `duree_s` 11 179,1,
soit ≈ 3,1 h ; mention de seconde main du billet d'Anthropic : [BX] p. 3 (« defection ») et p. 9 (titre), [RO] p. 3.

## VS-01 à VS-25 : rien n'est perdu

| écart | où dans la v3 | état |
|---|---|---|
| VS-01 | 205-222, 239, 299-303 | gardé ; précisé par F-10, F-11, F-12, S-06 |
| VS-02 | 79, 133-137, 180 | gardé ; complété par S-14 |
| VS-03 | 52-54, 137-142, 177 | gardé ; nuancé par F-04, F-08 |
| VS-04 | 158-165, 283-287 | gardé ; complété par F-05 |
| VS-05 | 49-52, 82-83, 178, 236 | gardé ; précisé par F-03, F-06, S-16 |
| VS-06 | 85, 104-108, 176 | gardé ; précisé par F-07 |
| VS-07 | 95-104, 353 | gardé ; [EM] précisé par S-19 (c) |
| VS-08 | 82, 236 | gardé ; complété en E4 par F-01 |
| VS-09 | 77, 177-179 | gardé |
| VS-10 | 63-64, 76, 236 | gardé |
| VS-11 | 78, 175, 179 | gardé |
| VS-12 | 120-132 | gardé ; phrase entière (F-08) |
| VS-13 | 87, 175, 236 | gardé ; précisé par S-19 (d) |
| VS-14 | 175 | gardé |
| VS-15 | 182, 238 | gardé (E2, piège : « analogie boîte noire ») |
| VS-16 | 143-149, 155-157, 180 | gardé ; libellé corrigé par F-02 |
| VS-17 | 287-290 | gardé ; étendu à [GM] par F-02 |
| VS-18 | 40-41, 86, 176 | gardé ; libellé corrigé par F-13 |
| VS-19 | 237, 291-298 | gardé ; libellé corrigé par F-14 |
| VS-20 | 311-315 | inchangé |
| VS-21 | 190-202, 235 | gardé ; précisé par S-18 |
| VS-22 | 59-60, 75 | gardé |
| VS-23 | 177, 183 | gardé |
| VS-24 | 83 | inchangé |
| VS-25 | 324-328 | inchangé |

## Différentiel v2 → v3 : rattachement des 27 blocs

| bloc (v2 → v3) | contenu | constats |
|---|---|---|
| 1 → 1 ; après 8 → 9-15 | titre ; en-tête v3 (ajout) | administratif |
| après 12 → 20-29 | sources relues (ajout) | S-01, S-05 à S-08, S-11, S-17, S-18 |
| 16-19 → 33-41 | en-tête R7 | F-09 ; méthode v3 |
| 23-32 → 45-64 ; 34-35 → 66-67 | verdict, points 1 à 3 | S-02, S-03, S-04, S-16, F-06, F-08 |
| 43-44 → 75-76 | [BX], [YS] | S-02 ; hors constat 1 |
| 46-47 → 78-79 | [AP], [PAR] | S-03, S-14 |
| 50-51 → 82-83 | [DYL], [CA] | S-03, S-16, F-06 |
| 53-55 → 85-87 | [AG], [AU], [K] | F-07, S-14, F-13, S-09, S-19 (d) |
| 68-71 → 100-104 ; 74 → 107-108 | [EM] ; Oak | S-19 (c) ; F-07, S-14 |
| 93 → 127-128 | [AP] p. 23 | F-08 |
| 99-110 → 134-153 | 2.2, « Ailleurs » | F-02, F-04, S-14 |
| 112-118 → 155-165 | 2.2, « Pour P3 » | S-14, F-05, S-15 |
| 122 → 169-170 ; 126-135 → 174-186 | section 3 | S-09, S-02, S-03, S-16, F-04, F-06, F-08, S-14, S-19 (b) |
| 140-146 → 191-205 ; 150-161 → 209-231 | règles communes ; nombres déjà écrits ; manipulation ; coûts | S-11, S-18, S-17 (e), S-04, S-06, S-07, F-10, F-11, F-12, S-19 (a) |
| 165-169 → 235-239 | table des expériences | S-01, S-03 à S-08, S-10 à S-13, S-16, S-18, S-19, F-01, F-03, F-14 |
| 173-180 → 243-256 | recommandation, confiance | S-03, S-05, S-09, S-17 |
| 183-199 → 259-310 | nœuds, règle gelée 1, dépense, concepts, nœud 4 | S-01, S-05, S-07, S-17, F-02, F-05, F-14 |
| 208 → 319-320 ; 249-250 → 361-366 | questions ouvertes ; fichiers | S-16 ; F-09 (hors constat 2), S-09 |

Retraits relus : chacun est voulu par un constat. Trois petits écarts non déclarés, sans effet : « p. 9 » retiré du
renvoi de [CA] au rang 5 (bloc de S-16 ; la phrase de p. 9 reste dans la ligne [CA]) ; « (attention causale) » retiré du
contrôle de E1 (bloc de S-06) ; « et 5 » ajouté à l'en-tête R7 (la section 5 cite des chiffres).

## Remarques (non comptées ; pour le tour suivant ou pour Lazar)

- **Exposition portée par la v3 elle-même (R1).** « le chercher viserait un signe déjà aperçu (R3) » (l. 238) et « A2 :
  poursuit T2 après coup » (l. 264) laissent deviner le sens du drapeau de T2. Qui lit la v3 est exposé. Le dire dans la
  v3, ou le faire déclarer par le rédacteur de P3b (la l. 238 demande déjà cette déclaration).
- **[AP] p. 9 l. 16.** Juste après la phrase citée : « This is the best probe of all we trained at distinguishing
  deceptive and honest responses, with near perfect separation on all datasets ». La p. 18 (l. 31-33) lève la tension
  (rappel au-dessus de 99 % contre le témoin ; toute réponse de sous-rendement notée trompeuse). Citer les deux serait plus
  symétrique (R4). Le traitement l'a noté.
- **[AU] 0,653 « Action ».** L'entrée est réduite à l'action, sans consigne (p. 6 l. 40). Ce montage est plus proche du
  filtrage du contenu de [BX] (consigne retirée, 0,63) que de P3 (consigne dans le contexte). Question de sens, hors de
  mon angle.
- **Règle gelée 1 (l. 289-290).** « (p. 6, p. 7) » pour la sonde retenue de [GM] : sa définition est p. 7 (« The final
  output is max ») ; la p. 6 décrit le maximum de la moyenne mobile exponentielle (« Linear Probe Rolling Exp »), une autre
  sonde. Sans effet.
- **Dépense (l. 291).** « et E2 ou la manipulation du nombre si tu étends N-028 » : E2 sur les épisodes neufs de T0.6
  (option recommandée) ne demande pas d'étendre N-028. À reformuler (sens).
- **Remarques du traitement** (l. 107-123) : je les partage ; aucune ne devient un constat ici.

## Limites

- Angle « fidélité » seulement : classement, pouvoirs et recommandations non rejugés, sauf là où une correction les
  touche.
- Annexes lues aux pages citées et à quelques voisines. Aucun chiffre recalculé à partir des données des auteurs, sauf
  le compte de la table 9 de [DYL].
- Neuf PDF restent sans compagnon (`[X]` et `[N]`), comme la v3 le dit ; aucun compagnon créé ici.
- Ni suite de tests ni `verifier-arbre` (lecture seule).

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v3-fidelite-v1.md` (ce rapport).
- `…/revue-detection/verif-v3-fidelite/` : `page3.py`, `guillemets_v3.py`, `verifier_v3.py`,
  `sortie-guillemets-v3.txt`, `sortie-verification-v3-fidelite.txt`, `differentiel-mot-a-mot-v2-v3.txt`. Scripts lancés
  par `python3 -I -B` : aucun `__pycache__`.
