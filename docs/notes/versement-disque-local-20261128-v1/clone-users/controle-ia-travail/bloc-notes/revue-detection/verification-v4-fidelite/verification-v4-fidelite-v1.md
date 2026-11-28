# Vérification de la synthèse v4 « comment détecter » — angle « fidélité des corrections », tour 3 — v1

## Verdict : **conforme après corrections**

- **Les 21 constats du tour 2 sont appliqués** (VV3-sens-01 à 14, VV3-fidelite-01 à 07) ; aucun n'est écarté. Quatre le
  sont en partie, ou avec un ajout :
  - VV3-sens-01 : deux chiffres restent sans type ;
  - VV3-sens-08 : le bras « moyenne » manque aux nœuds de la section 5 ;
  - VV3-sens-09 : une raison neuve, sans source ;
  - VV3-sens-13 : la phrase de [DYL] n'est pas citée, alors que le traitement dit « phrase citée ».
- **Différentiel : le script rejoué sur la v3 redonne la v4 octet pour octet** (`fba703f9…`). Les 27 blocs du différentiel
  mot à mot se rattachent à un constat, à R-283 ou P-015, ou à l'en-tête. Font exception trois phrases ajoutées sans source
  dans les rapports et un retrait non déclaré au verdict.
- **Chiffres et phrases anglaises ajoutés ou déplacés : tous sur leur page.** 58 items contrôlés à la page citée, par deux
  lectures (PDF lu directement et `cherche.py`), dont 17 lignes de table : 0 écart. Épreuve R5 : 10 artefacts, 10 rejetés.
- **Renvois au dépôt : exacts dans les versions qu'épingle la v4** ([P], N-026, `registres/decisions.md` `38579d98…`,
  `registres/go.md` `94ebe409…`). Mais R-283 et P-015 viennent d'une version plus récente, que la v4 n'épingle pas. Dans
  cette version, à 18:28 UTC, toutes les lignes citées des deux registres étaient déjà décalées d'une.
- **La déclaration « aucun chiffre neuf : phrases et chiffres ajoutés repris des deux rapports » est fausse sur six
  points** : une confiance (50 %), deux pouvoirs, trois phrases neuves (VV4-fidelite-10).
- **12 constats : 1 moyen, 8 mineurs, 3 de forme.** Toutes les corrections sont locales. Aucune ne change le classement ni
  les recommandations. Le plus grave : une raison de confiance neuve, sans source, qui énonce une zone vierge (R8).

## Cadre

- **Objet.** `…/revue-detection/synthese-comment-detecter-v4.md` (`fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a`),
  comparée à la v3 (`ec4239e9…`). Constats appliqués : `verification-v3-sens-v1.md` (`256f9181…`) et
  `verification-v3-fidelite-v1.md` (`987b39ea…`). Traitement : `traitement-verification-synthese-tour3-v1.md` (`51029020…`).
  Script : `correction-tour3/appliquer_corrections_v4.py` (`e6e27423…`). Les six empreintes sont égales à la commande.
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni la v3, ni la v4, ni les extractions, ni aucune vérification
  ou traitement antérieurs. 2026-10-20, de 22:15 à 22:45 UTC environ.
- **Lecture seule.** Aucune écriture dans le dépôt (tête `c1e7ef9`). Git en lecture seule (`git log`, `git show`) ; le
  différentiel est calculé hors du dépôt. Aucune commande Vast.ai, aucun service payant, aucun contact, aucune recherche web.
- **Non ouverts.** `prereg/P3-consignes-v1.md`, textes d'action, clés ; [V] (empreinte seule : `0c8ecbdf…`, égale). Hors
  de ma liste, donc non ouverts : note du brainstorm, propositions C et D, brouillon de T0.6, document de P-015,
  `registres/depenses.md`. Leurs citations dans la v4 sont comparées aux rapports qui les ont lues, pas à la source.
- **Exposition (R1).** De [P], seules les lignes citées par les ajouts sont lues. Aucune valeur ni aucun sens de T1, T2 ou T4
  n'est vu ni recopié ici.
- **Conventions.** « v4 l. » = ligne du fichier v4. « l. » d'un PDF = ligne de la page sortie par
  `pdftotext -raw` (ou `-layout` pour une table), telle que l'imprime `page4.py --page CLE PAGE [raw|layout]`.

## Méthode

1. **Empreintes.** Les 21 PDF de `verification/cles.txt` en empreinte complète : tous égaux à la clé
   (`travail/empreintes-pdf-v4-fidelite.txt`). RO : `bde99a62…`, égale à la section 6. [P] `d975e981…`, N-026 `85bd4023…`,
   N-029 `084e3052…` : égales.
2. **Rejeu du script** sur la v3 : « 2 blocs et 46 remplacements appliqués » ; sortie identique à la v4.
3. **Différentiel mot à mot** v3 → v4 : `git diff --no-index --word-diff=plain --word-diff-regex='[^[:space:]]+' -U0`
   (`travail/differentiel-mot-a-mot-v3-v4.txt`, 27 blocs) ; chaque ajout et chaque retrait relu et rattaché.
4. **Pages.** `travail/page4.py` lit une page dans le PDF même, après contrôle d'empreinte complète. `travail/verifier_v4.py`
   contrôle chaque item deux fois : lecture directe, et `verification/cherche.py` sur les pages déjà extraites. Il fait aussi
   l'épreuve R5 (`travail/sortie-verification-v4-fidelite.txt`). Contrôles en plus : `travail/controles-complementaires-v4.txt`.
5. **Extraits** de la v3 et de la v4 cités ici : `travail/extraits_v4.py` (33 extraits, à la ligne dite, 0 écart).
6. **Renvois au dépôt** : `travail/renvois_depot_v4.py`. Il compare la version épinglée (`8bd4a75`, 11:55 UTC), celle de la
   v4 (`43cd3ac`, 18:28 UTC) et la version actuelle.
7. **Origine des phrases neuves** : recherche dans les deux rapports et dans le traitement (`travail/journal-v4-fidelite.txt`).

Reproduire : `python3 -I -B …/verification-v4-fidelite/travail/verifier_v4.py` ; une page :
`python3 -I -B …/travail/page4.py --page CLE PAGE raw` ; une phrase : `page4.py CLE PAGE "phrase"`.

## Constats, le plus grave d'abord

### Moyen

**VV4-fidelite-01 — Confiance de 15 à 25 % : une raison neuve, sans source, qui énonce une zone vierge.**
- **Où.** v4 l. 303 : « T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type ».
- **Source.** Aucun des deux rapports ni le traitement ne contient « rien de publié » ni « ne le passe » (0 occurrence).
  VV3-sens-09 (rapport « sens », l. 230-235) demandait : « Retirer ces deux raisons ; donner les raisons tirées des faits ».
  Il ne donnait que deux raisons : « Seule l'addition de T1 justifie la baisse », et le levier de [K].
- **Problème.**
  - C'est un ajout de la session, placé sous la déclaration « repris de ces deux rapports ; aucun chiffre neuf » (v4 l. 20-21).
  - « Rien de publié » étend aux publications un constat qui ne vaut que pour les travaux lus. C'est une zone vierge : R8 en
    fait une question.
  - Lue simplement, la phrase contredit la v4 elle-même. À consigne égale, les analogues de T1 qu'elle cite sont au-dessus du
    hasard : 0,81 et 0,63 sur ce même modèle [BX p. 5-6], 0,606 [YS p. 3] (v4 l. 80-82). Au sous-rendement de [PAR], que la
    v4 range à consigne égale (l. 60), la sonde Pairs atteint 0,964 en moyenne (table 3, p. 7, layout l. 19).
  - Ce qu'aucun travail lu ne fait, c'est mesurer contre un plancher apparié (v4 l. 96). « Passer T1 », au sens de P3, n'y
    est donc testé dans aucun sens.
- **Correction.** v4 l. 303 : remplacer « T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce
  type ; » par « T1 s'ajoute, à consigne égale ; aucun travail lu ne mesure un contraste de ce type contre un plancher
  apparié (R8 : question), et les analogues lus restent modestes sur ce même modèle (0,81 et 0,63 [BX p. 5-6] ; 0,606
  [YS p. 3]) ; ». Déclarer cette raison comme jugement de la session (VV4-fidelite-10).
- **Reproduire.** `extraits_v4.py` (v4 l. 303) ; `grep -c "rien de publié" …/verification-v3-*-v1.md` → 0 ;
  `page4.py --page PAR 7 layout` (l. 19).

### Mineurs

**VV4-fidelite-02 — R-283 et P-015 viennent d'une version des registres que la v4 n'épingle pas ; à cette date, les lignes
citées étaient décalées ; le brouillon de T0.6 n'a ni chemin ni empreinte (R6).**
- **Où.**
  - v4 l. 21-22 (en-tête : R-283, P-015).
  - v4 l. 33-34 (Sources) : « relus vers 12:00 UTC (lignes citées inchangées depuis 11:45 ; N-029 et GO-2026-10-20-08
    ajoutés entre-temps) ».
  - v4 l. 284 et l. 350-351 : R-283 et P-015, sans ligne ni empreinte.
  - v4 l. 282 : renvoi neuf `registres/go.md` l. 32.
  - v4 l. 283, l. 286, l. 351 : brouillon de T0.6, l. 75, l. 74-81, « 1 536 + 640 épisodes ».
- **Source** (`sortie-renvois-depot-v4.txt`).
  - `registres/decisions.md` épinglé `38579d98…` (commit `8bd4a75`, 11:55 UTC) : ni P-015, ni R-283.
  - Version de la v4, `cc1b108d…` (commit `43cd3ac`, 18:28 UTC) : P-015 l. 392, R-283 l. 477. Toutes les lignes citées y sont
    décalées d'une : N-025 l. 447, R-262 l. 454, N-028 l. 457, R-265 l. 458, R-269 l. 462, N-029 et R-276 l. 469-470.
  - `registres/go.md` depuis `c7211a2` (13:56 UTC), `05e7fccd…` : GO-2026-10-20-05 à -08 aux l. 33 à 36. Le renvoi neuf
    « l. 32 » n'est donc exact que dans la version épinglée.
  - Le brouillon de T0.6 a un chemin et une empreinte dans VV3-sens-06 (rapport « sens », l. 193-194 :
    `brouillons/T0.6-organismes-v0-v1-brouillon1.md`, `e212fb35…`). La v4 n'en donne aucun.
- **Problème.**
  - R6 : chaque chiffre doit renvoyer à un chemin et une empreinte. « 1 536 + 640 » et les faits de R-283 et P-015 n'y
    renvoient pas.
  - « Lignes citées inchangées » n'était plus vrai à 18:27. Qui ouvre les registres à la date de la v4 tombe une ligne trop
    haut.
- **Correction.** Ajouter aux Sources, après la l. 34 : « v4 : `registres/decisions.md` relu vers 18:27 UTC (`cc1b108d…`,
  commit `43cd3ac`) pour P-015 (l. 392) et R-283 (l. 477) ; dans cette version, les lignes citées ailleurs dans la synthèse
  sont décalées d'une (N-025 l. 447, R-262 l. 454, N-028 l. 457, R-265 l. 458, R-269 l. 462, N-029 et R-276 l. 469-470) ;
  `registres/go.md` (`05e7fccd…`) : GO-2026-10-20-05 à -08 aux l. 33 à 36 ; les renvois de la synthèse restent ceux des
  versions épinglées (`38579d98…`, `94ebe409…`). Brouillon de T0.6 : `brouillons/T0.6-organismes-v0-v1-brouillon1.md`
  (`e212fb35…`, empreinte donnée par VV3-sens-06, non recalculée ici). »
- **Reproduire.** `python3 -I -B …/travail/renvois_depot_v4.py`.

**VV4-fidelite-03 — P-015 : la v4 lui prête une estimation que le registre ne contient pas ; R-283 n'est appliqué qu'à
moitié.**
- **Où.**
  - v4 l. 284 (E3, coût) : « la proposition P-015 en estime la réécriture en mode « coût » ».
  - v4 l. 350-351 : « T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement (brouillon actuel : 1 536 + 640
    épisodes ; P-015) : nœud de dépense possible ».
  - v4 l. 349 : « Au-delà de 10 USD par lancement ou du crédit : nœud. »
- **Source.**
  - `registres/decisions.md` (`cc1b108d…`), l. 392 (P-015) : périmètre de T0.6, T0.7 et T0.8 en mode « coût » ; options (a)
    à (c) ; « Recommandation (b), confiance ≈ 60 % » ; défaut au 2026-10-22 vers 14:30. On n'y trouve ni coût, ni « USD »,
    ni nombre d'épisodes (`sortie-renvois-depot-v4.txt`).
  - Le document de P-015 (`docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `6e74c6cb…`) n'est pas dans ma
    liste : je ne l'ai pas ouvert.
  - « Peut dépasser 10 USD » vient de VV3-sens-06 (l. 196-198 : « sur un devis de 8 et 10 heures (l. 92) : plusieurs fois
    P3, sans doute au-delà de 10 USD par lancement »).
  - R-283, l. 477 : « Le crédit lu à un instant n'est donc pas une contrainte de travail ; […] s'il refuse une création, on
    attend la recharge, on ne le contourne pas. »
- **Problème.** La v4 attribue à P-015 une estimation et un risque de dépense que la ligne du registre ne porte pas. La l. 349
  garde le crédit comme seuil de nœud, ce que R-283, citée deux lignes plus bas, retire.
- **Correction.**
  - v4 l. 284 : « la proposition P-015 (`registres/decisions.md` l. 392, version `cc1b108d…`) en propose le périmètre (options
    (a) à (c), recommandation (b), défaut le 2026-10-22 vers 14:30 UTC) ».
  - v4 l. 350-351 : « T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement (brouillon actuel : 1 536 + 640
    épisodes, VV3-sens-06 ; périmètre : P-015) : nœud de dépense possible ».
  - v4 l. 349 : « Au-delà de 10 USD par lancement ou du plafond de 150 USD : nœud ; si le contrôle de crédit refuse une
    création, on attend la recharge (R-283). »
  - Si le document de P-015 donne une estimation, la citer avec sa ligne et son empreinte.

**VV4-fidelite-04 — VV3-sens-08 appliqué dans la table seulement : le bras « moyenne » (iii) manque aux nœuds de Lazar et à
la dépense.**
- **Où.**
  - v4 l. 282 (E1, (iii)) : « … extension de N-028, comme E2 et la manipulation (nœud). ».
  - v4 l. 290-292 (recommandation (2) : E1, « un lancement »).
  - v4 l. 326 (« **E2 et manipulation du nombre sur les actions de P3** »).
  - v4 l. 345 (« E1, puis E3 (et E2 ou la manipulation du nombre si tu étends N-028) »).
- **Source.**
  - VV3-sens-08 (l. 224-225) : « Écrire la base du bras (iii) (N-026 avec N-028), ou le ranger avec E2 et la manipulation ».
  - Traitement : « bras (iii) hors du GO de N-028, extension (nœud) » ; où : « table E1 ; concepts, couches, positions ».
  - `registres/go.md` l. 32 (version épinglée) : le GO de N-028 couvre la « localisation au champ du coût avec plancher
    apparié, sonde oracle ».
- **Problème.** La table déclare le bras (iii) hors du GO, donc nœud. Mais la liste des nœuds de la section 5 ne le porte
  pas, et la recommandation (2) et la dépense présentent E1 comme un seul lancement sous N-028. En lisant la section 5, Lazar
  ne voit pas qu'il doit trancher ce bras.
- **Correction.**
  - v4 l. 326 : « - **E2, bras « moyenne » (iii) de E1 et manipulation du nombre sur les actions de P3** : extension de
    N-028 ».
  - v4 l. 292 : remplacer « avec la manipulation du nombre si tu l'ajoutes (nœud ci-dessous) » par « avec le bras « moyenne »
    (iii) et la manipulation du nombre si tu les ajoutes (nœud ci-dessous) ».
  - v4 l. 345 : « (et E2, le bras (iii) ou la manipulation du nombre si tu étends N-028) ».

**VV4-fidelite-05 — VV3-sens-13 : la phrase de [DYL] n'est pas citée, et le classement est prêté à [DYL].**
- **Où.** v4 l. 65 : « [DYL] range Llama-3.3-70B, souvent pris pour les organismes, sous Qwen 3.5 2B Reasoning (p. 5) ».
- **Source.**
  - [DYL] p. 5, l. 46-48 : « existing organisms are often trained on Llama 3.3 70B, which Appendix I shows has limited
    introspective capacity, and which Artificial Analysis [2026] rank as less capable than more recent models such as Qwen
    3.5 2B Reasoning » (trouvée à la page par les deux lectures).
  - VV3-sens-13 : « Citer la phrase ». Traitement : « phrase citée ».
  - Règle R7 de la v4 (l. 41, l. 51) : « Chiffre = clé de PDF, page du fichier, phrase anglaise » ; les sections 1, 3, 4 et 5
    « reprennent les chiffres des sections 2.1 et 2.2, où la phrase est donnée ».
- **Problème.**
  - Paraphrase sans phrase : ni le point 1 ni la ligne [DYL] de 2.1 ne donnent la phrase.
  - « [DYL] range » prête à [DYL] un classement d'Artificial Analysis, que [DYL] ne fait que rapporter.
  - Le traitement dit le contraire de ce qui est appliqué.
- **Correction.** v4 l. 65 : « [DYL] rapporte que Llama-3.3-70B, souvent pris pour les organismes, est classé par Artificial
  Analysis sous Qwen 3.5 2B Reasoning (« existing organisms are often trained on Llama 3.3 70B, which Appendix I shows has
  limited introspective capacity, and which Artificial Analysis [2026] rank as less capable than more recent models such as
  Qwen 3.5 2B Reasoning », p. 5) ».

**VV4-fidelite-06 — Rang 6 : « seule comparaison publiée » étend aux publications un constat fait sur les travaux lus.**
- **Où.** v4 l. 212 : « toutes, seule comparaison publiée (« using fewer layers consistently yields worse performance »)
  [CC p. 8], sur une autre tâche ».
- **Source.** VV3-sens-10 (l. 240-242) : « Seul [CC] compare », parmi les travaux lus. « seule comparaison » n'est ni dans les
  rapports ni dans le traitement. La phrase de [CC] p. 8 est sur sa page.
- **Correction.** « toutes, seule comparaison lue (« using fewer layers consistently yields worse performance ») [CC p. 8],
  sur une autre tâche ».

**VV4-fidelite-07 — Retrait non déclaré au verdict : « P3 n'avait aucune de ces conditions. »**
- **Où.** La phrase ouvrait le point 2 de la v3 (v3 l. 55). Le point 2 de la v4 commence par « 2. Deux types de contraste
  sont à séparer. » (v4 l. 72).
- **Source.** Aucun constat ne demande ce retrait : VV3-sens-01 (2) réécrit les analogues, pas cette phrase. L'en-tête de la
  v4 (l. 23) dit pourtant : « Rien d'autre n'est changé ».
- **Problème.** Cette phrase reliait le point 1 (conditions du succès) à P3. Elle reste vraie sous la v4 : pas de tromperie
  écrite, pas de données du domaine, pas de question, 8 milliards, une couche. Son retrait change le verdict sans être
  déclaré.
- **Correction.** v4 l. 72 : « 2. P3 n'avait aucune de ces conditions. Deux types de contraste sont à séparer. »

**VV4-fidelite-08 — « Entre consignes » pour [AP] p. 18 : la page mesure contre le témoin Alpaca, où le sujet et la forme
diffèrent aussi.**
- **Où.**
  - v4 l. 61-62 : « entre consignes, la même sonde sépare presque parfaitement [AP p. 18] ».
  - v4 l. 210 : « entre consignes, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four evaluation
    datasets », [AP p. 18]) ».
  - v4 l. 283 : « entre consignes, séparation presque parfaite [AP p. 18] ».
- **Source.**
  - [AP] p. 18, l. 32-33 : « Where this probe excels, however, is consistently rating every control response as honest. Our
    recall at 1% is greater than 99% on all four evaluation datasets. »
  - [AP] p. 9, l. 8-9 (légende de la figure 6) : « Recall (TPR on deceptive) for 1% FPR on our control responses ».
  - [AP] p. 5 : « We use Llama responses to queries from the Alpaca dataset […] as a control dataset ».
  - VV3-sens-02 (l. 119-120) écrivait déjà « Entre consignes » ; la v4 l'a repris sans le relire sur la page.
- **Problème.** La mesure oppose les réponses trompeuses des jeux d'évaluation aux réponses d'Alpaca : consigne, sujet et
  forme diffèrent tous. « Entre consignes » suggère un contraste du type P3-P3 (même tâche, même forme), que la page ne mesure
  pas. Or la v4 s'en sert pour prédire un faux positif sur P3-P3 (l. 92).
- **Correction.**
  - v4 l. 61-62 : « contre le témoin Alpaca (consigne, sujet et forme différents), la même sonde a un rappel à 1 % de faux
    positifs au-dessus de 99 % sur les quatre jeux [AP p. 18] ».
  - v4 l. 210 : « contre le témoin Alpaca, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four
    evaluation datasets », [AP p. 18]) ».
  - v4 l. 283 : « contre le témoin Alpaca, séparation presque parfaite [AP p. 18] ».

**VV4-fidelite-09 — VV3-sens-01 (1)-(2) appliqué en partie : le 0,5 de [BX] et le 0,653 de [AU] restent sans type.**
- **Où.** v4 l. 84-88 (point 2) ; v4 l. 209 (rang 3).
- **Source.**
  - VV3-sens-01, correction (1) : « Pour chaque chiffre du point 2 et des rangs 2, 3 et 9 : écrire le type de contraste ».
    Correction (2) : « ranger 0,81, 0,63 et 0,5 de [BX] et 0,606 de [YS] comme analogues de T1 ».
  - [BX] p. 4 : « Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts » : aucune
    consigne, donc pas de contraste entre consignes.
- **Problème.** 0,81, 0,63 et 0,606 sont typés ; 0,5 et 0,653 ne le sont pas.
- **Correction.**
  - v4 l. 84 : « Le 0,5 de [BX] (type T1 : aucune consigne, p. 4) vient d'un organisme affiné, … ».
  - v4 l. 85 : « [AU] (type non établi ; étiquette « very correlated with the 'Impostor' label », p. 6) : 0,653 sur Phi-4, … ».
  - v4 l. 209 : « [AU] (type non établi) : 0,653, … ; 0,5 (type T1) seulement sur organisme affiné [BX p. 8] ».

### Forme

**VV4-fidelite-10 — En-tête de la v4 : la déclaration « aucun chiffre neuf » et le périmètre du changement sont inexacts.**
- **Où.**
  - v4 l. 20-21 : « Phrases et chiffres ajoutés : repris de ces deux rapports, qui les ont relus à la page et à la ligne ;
    aucun chiffre neuf. »
  - v4 l. 23 : « Le fond change en sections 1, 3, 4 et 5 ».
  - v4 l. 299 : « (jugement du correcteur ; … VV3-sens-09) ».
- **Problème.** Six ajouts ne viennent pas des rapports :
  - (a) « rien de publié ne le passe » (01) ;
  - (b) « seule comparaison publiée » (06) ;
  - (c) « en estime la réécriture » (03) ;
  - (d) « confiance ≈ 50 % (v3 : 60 %) » (l. 334 ; VV3-sens-05 dit seulement « Revoir la confiance ») ;
  - (e) le pouvoir « faible à moyen » du rang 6 (l. 212 ; VV3-sens-10 n'en propose aucun) et celui du rang 2 (l. 208 ;
    VV3-sens-01 laisse le choix : « ou baisser le pouvoir ») ;
  - (f) le retrait de la phrase du constat 07.

  La section 2 change aussi : en 2.1, les lignes [BX], [PAR] et [AU] ; en 2.2, « Pour P3 », où le sens de la dilution
  s'inverse. Les confiances de la v4 sont jugées par la session, plus par le correcteur du tour 2.
  Les chiffres de la littérature ajoutés viennent bien, eux, des rapports (section « Déclaration » ci-dessous).
- **Correction.**
  - v4 l. 20-21 : « Phrases et chiffres de la littérature ajoutés : repris de ces deux rapports, qui les ont relus à la page
    et à la ligne. Jugements de la session, sans source dans les rapports : pouvoirs « faible à moyen » des rangs 2 et 6 ;
    confiance de 50 % sur la manipulation du nombre ; raisons des confiances (section 5). »
  - v4 l. 23 : « Le fond change en sections 1 à 5 (2.1 : [BX], [PAR], [AU] ; 2.2 : « Pour P3 ») : … ».
  - v4 l. 299 : « (jugement du correcteur, puis de la session pour la v4 ; revue depuis la v1, VV2-sens-09 et VV3-sens-09) ».

**VV4-fidelite-11 — Confiance de 40 % : « T1 n'y vaut qu'avec T4 » renvoie au bras « avant le champ », contre la règle de
la section 4.**
- **Où.** v4 l. 301-302 : « le bras « avant le champ » voit des nombres déjà écrits, et T1 n'y vaut qu'avec T4 ».
- **Source.** v4 l. 236 (règles communes) : « sur le bras du champ et dans E2, T1 ne vaut qu'avec T4 ».
- **Correction.** « … le bras « avant le champ » voit des nombres déjà écrits, et, au champ, T1 ne vaut qu'avec T4. »

**VV4-fidelite-12 — Trois fautes de transcription.**
- (a) v4 l. 240 : « lu « l'agrégation explique-t-elle le nul ? », (N-026, ». La virgule est en trop. La correction de
  VV3-fidelite-05 finissait par « (S-18) », omis. Correction : « lu « l'agrégation explique-t-elle le nul ? » (N-026,
  conditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse (S-18). »
- (b) v4 l. 79 : « Qwen3-8B 0,74 en exactitude équilibrée [DYL p. 5 ; table 9, p. 28] ; sur ce même modèle, rappel à 1 % de
  faux positifs ». « Ce même modèle » suit Qwen3-8B, mais désigne le modèle de P3 ([BX] lit Llama-3.1-8B-Instruct, v4
  l. 106). Correction : « sur le modèle de P3 (Llama-3.1-8B-Instruct), rappel à 1 % de faux positifs ».
- (c) v4 l. 77 : « réponses honnêtes déjà plus hautes que presque tout Alpaca, p. 9 ». La page dit : « For Pairs probe, the
  average honest Backdoors sample had a mean probe activation higher than 99.9% of the Alpaca samples » ([PAR] p. 9,
  l. 21-22). Correction : « réponse honnête moyenne au-dessus de 99,9 % d'Alpaca, sonde Pairs, p. 9 ».

## Fidélité, constat par constat (tour 2)

| constat | appliqué (v4, lignes) | juste | complet | conforme au traitement | constat ici |
|---|---|---|---|---|---|
| VV3-sens-01 | 72-95, 106, 110, 208-209, 215, 218-222 | oui (chiffres et phrases sur leur page) | non : 0,5 et 0,653 sans type | oui | 09 |
| VV3-sens-02 | 58-62, 110, 210, 283, 293-294, 329-330 | oui, sauf « entre consignes » | oui | oui | 08 |
| VV3-sens-03 | 85-88, 117, 209 | oui ([AU] p. 6 l. 12 et l. 40-41 ; p. 7 l. 2) | oui | oui | — |
| VV3-sens-04 | 233-237, 283, 301-302 | oui ([P] l. 141-142, 238-241) | oui | oui | 11 (forme) |
| VV3-sens-05 | 266-274, 332-335 | oui (citations égales à celles du rapport ; note et proposition D non rouvertes) | oui | oui | 10 (50 %) |
| VV3-sens-06 | 284, 286, 350-351 | oui | oui | oui ; P-015 en plus | 02, 03 |
| VV3-sens-07 | 294-297, 310-312 | oui | oui | oui | — |
| VV3-sens-08 | 282, 354-355 | oui (N-026 l. 18-19 ; [P] l. 428) | non : nœuds et dépense | oui (le traitement ne vise que la table) | 04 |
| VV3-sens-09 | 299-305 | non : raison neuve sans source | oui | non (« raisons tirées des faits ») | 01 |
| VV3-sens-10 | 67-68, 212 | oui, sauf « publiée » | oui | oui | 06 |
| VV3-sens-11 | 68-71, 210 | oui ([AP] p. 23) | oui | oui | — |
| VV3-sens-12 | 282 (E4) | oui | oui | oui | — |
| VV3-sens-13 | 65-66 | paraphrase sans phrase ; classement prêté à [DYL] | rang 5 et questions ouvertes inchangés | non (« phrase citée ») | 05 |
| VV3-sens-14 (a) à (e) | 185 ; 282 ; 286 ; 323-325 ; 283 | oui ([P] l. 242, 330-331) | oui | oui | — |
| VV3-fidelite-01 | 238-239, 283 | oui ([P] l. 273) | oui | oui | — |
| VV3-fidelite-02 | 85-86, 90-91, 117, 209 | oui ; [LB] et [PAR] ajoutés à la liste, exacts ([LB] p. 8 ; table 3) | oui | oui | — |
| VV3-fidelite-03 | 187-190, 213 | oui (table 3, p. 7 : 0,931/0,811 ; 0,907/0,877 ; RP 3 jeux sur 4) | oui | oui | — |
| VV3-fidelite-04 | 68-71, 210 | oui | oui | oui | — |
| VV3-fidelite-05 | 240-241 | oui (N-026 : « Bonferroni » absent) | « (S-18) » omis | oui | 12 (a) |
| VV3-fidelite-06 | 283 | oui ([DYL] table 9, p. 28, l. 32-33) | oui | oui | — |
| VV3-fidelite-07 | 299-300 | oui | oui | oui | — |

Le traitement accepte les 21 constats, sans en écarter aucun. Ses colonnes « décision » et « où » sont exactes, sauf
VV3-sens-13 (« phrase citée ») et VV3-sens-09 (raison neuve ajoutée). Le décompte « 2 blocs, 46 remplacements, chacun trouvé
une seule fois » est exact : le script s'arrête sinon, et le rejeu passe.

## Différentiel v3 → v4 : rattachement des 27 blocs

| bloc (v3 → v4) | contenu | rattaché à |
|---|---|---|
| 1 → 1 ; après 15 → 16-25 ; 41 → 51-52 | titre ; en-tête v4 ; ligne R7 | en-tête (déclare R-283, P-015) |
| 48-50 → 59-63 | point 1, question | VV3-sens-02 |
| 52-64 → 65-95 | point 1 (suite), point 2 | VV3-sens-13, 10, 11 ; VV3-fidelite-04 ; VV3-sens-01, 03 ; VV3-fidelite-02 ; **retrait non rattaché (07)** |
| 75 → 106 ; 79 → 110 ; 86 → 117 | [BX] ; [PAR] ; [AU] | VV3-sens-01, 02, 03 ; VV3-fidelite-02 |
| 154 → 185 ; 156-157 → 187-190 | « peut tenir » ; dilution | VV3-sens-14 (a) ; VV3-fidelite-03 |
| 170 → 203 | en-tête de la section 3 | en-tête |
| 175-177 → 208-210 | rangs 2, 3, 4 | VV3-sens-01, 02, 03 ; VV3-fidelite-02, 04 |
| 179-180 → 212-213 | rangs 6, 7 | VV3-sens-10 ; VV3-fidelite-03 ; **« publiée » (06)** |
| 182 → 215 ; 185-186 → 218-222 | rang 9 ; « ce qui a changé » | VV3-sens-01, 02 |
| 197-202 → 233-241 | règles communes | VV3-sens-04 ; VV3-fidelite-01, 05 |
| 227 → 266-274 | manipulation du nombre | VV3-sens-05 |
| 235-239 → 282-286 | table des expériences | VV3-sens-14 (b), (c), (e), 08, 12, 02, 04, 06 ; VV3-fidelite-01, 06 ; R-283, P-015 (**03**) |
| 246-249 → 293-297 | recommandation (3), (4) | VV3-sens-02, 07 |
| 251-256 → 299-305 | confiance | VV3-sens-09, 04 ; VV3-fidelite-07 ; **« rien de publié » (01)** |
| 262 → 311-312 ; 274 → 324-325 ; 278 → 329-330 | nœuds « Revendication », N-028, E2 | VV3-sens-07, 14 (d), 02 |
| 281 → 333-335 | manipulation, recommandation | VV3-sens-05 ; **50 % (10)** |
| 296-297 → 350-351 | dépense | R-283 ; P-015 ; VV3-sens-06 (**02, 03**) |
| 300 → 354-355 | couches multiples | VV3-sens-08 |
| 366 → 421 | fichiers | en-tête |

Retraits relus. Chacun est voulu par un constat ou par R-283, sauf « P3 n'avait aucune de ces conditions. » (07). Le crédit de
11,79 USD et la recharge d'environ 20 USD (v3 l. 296-297) sont retirés au profit de R-283 : c'est déclaré. Les explications
« que P3 n'a pas » et « consigne remplacée par une consigne bénigne » quittent le point 2. Elles restent en 2.1 (ligne [BX]) :
c'est l'effet du nouveau typage de VV3-sens-01.

## Déclaration « aucun chiffre neuf »

- **Chiffres de la littérature : tous repris.** Les chiffres ajoutés ou déplacés sont : 0,844 ; 0,768 ; 0,832 ; 0,849 ;
  0,849 et 0,879 contre 0,964 ; 0,931/0,811 ; 0,907/0,877 ; 0,95, 0,60, 0,69, 0,58 ; 0,74 ; 0,64 et 0,68 ; 0,03 ; 1.000 ;
  « 10 » derniers jetons ; « 99% » ; « 99.9% » ; « 2B » et « 70B » ; −0.416. Chacun figure dans l'un des deux rapports ou dans
  la v3, et il est sur sa page (section A de `sortie-verification-v4-fidelite.txt`, 58 items, 0 écart).
- **Renvois et nombres du dépôt : repris.** [P] l. 125, 141-142, 238-241, 242, 272-274, 293-296, 328-332, 333, 428 ; N-026
  l. 18-19 ; `registres/go.md` l. 32 (épinglé) ; note l. 28 et l. 33 ; proposition D l. 93-96 et l. 100-101 ; brouillon de
  T0.6 l. 74-81 et l. 75, 1 536 + 640. Tous viennent de VV3-sens-01, 04, 05, 06, 08 et 14. Ceux de [P] et de N-026 sont
  exacts (`sortie-renvois-depot-v4.txt`). Ceux de la note, de la proposition D et du brouillon sont égaux à leur citation
  dans le rapport « sens » ; la source n'est pas rouverte ici.
- **Faux pour six ajouts de la session** : voir VV4-fidelite-10 (a) à (f).

## Remarques (non comptées ; pour la vérification « sens » ou pour Lazar)

- **[LB] « Instructed-Deception » n'est pas un pur P3-P3.** « When a model ignored the instruction and answered correctly,
  we labeled the response honest » ([LB] p. 6, l. 52-53). Une part des réponses honnêtes a donc la consigne de mentir.
- **[PAR] « Backdoors ».** « Responses containing backdoors are labeled deceptive » ([PAR] p. 4). Le code écrit porte l'acte :
  ce n'est pas « rien d'écrit dans l'empan lu », la ligne du rang 3 où la v4 le range.
- **[AU] « +System ».** D'après « all inputs above and including X » (p. 6), « +System » inclut aussi « +Thinking ». P3 n'a
  pas de raisonnement : la lecture « le montage de P3 serait « +System » » est approchée.
- **Registres après la v4.** Dans la version actuelle de `registres/decisions.md` (`6d033ecf…`, tête `c1e7ef9`, 22:20 UTC),
  les lignes citées sont décalées de sept (R-262 l. 460, N-028 l. 463, R-283 l. 483). GO-2026-10-20-10 (commit `49b482f`,
  21:57 UTC) ajoute une lecture au périmètre de P3b. Ces deux faits sont postérieurs à la v4. À signaler à la transmission,
  car la v4 dit que « le GO de N-028 ne couvre que la localisation au champ du coût et l'oracle » (l. 327-328).
- La remarque du rapport de fidélité du tour 2 sur la dépense (« E2 … si tu étends N-028 ») vaut toujours. Elle rejoint
  VV4-fidelite-04.

## Limites

- Angle « fidélité » seulement : classement, pouvoirs et recommandations ne sont pas rejugés, sauf là où une correction les
  touche.
- Pièces hors de ma liste non ouvertes : note, propositions C et D, brouillon de T0.6, document de P-015, `depenses.md`. Leurs
  citations sont comparées aux rapports qui les citent.
- Pages lues aux lignes citées et à quelques voisines. Aucun chiffre recalculé à partir des données des auteurs.
- Ni suite de tests ni `verifier-arbre` (lecture seule).

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v4-fidelite/verification-v4-fidelite-v1.md` (ce rapport).
- `…/revue-detection/verification-v4-fidelite/travail/` :
  - outils : `page4.py`, `verifier_v4.py`, `extraits_v4.py`, `renvois_depot_v4.py` ;
  - sorties : `sortie-verification-v4-fidelite.txt`, `sortie-extraits-v4.txt`, `sortie-renvois-depot-v4.txt`,
    `controles-complementaires-v4.txt`, `sortie-guillemets-rapport-v4.txt` (phrases anglaises de ce rapport, toutes à leur
    page), `empreintes-pdf-v4-fidelite.txt`, `differentiel-mot-a-mot-v3-v4.txt` ;
  - `v4-rejouee.md` (rejeu du script, identique à la v4) ;
  - `journal-v4-fidelite.txt`.
- Scripts lancés par `python3 -I -B` : aucun `__pycache__`.
