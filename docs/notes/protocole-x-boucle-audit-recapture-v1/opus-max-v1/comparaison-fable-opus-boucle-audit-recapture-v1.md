# Comparaison des deux réponses sur la boucle « audit après coup, recapture, réapprentissage des sondes » : Fable 5.2 (v2) et Opus 5.5 en effort maximal (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), comparateur neuf. Je n'ai écrit aucune des pièces comparées. Pièce de classe C. Aucun appel payant, aucune recherche en ligne, ni commit ni poussée.
- **Grille** : `grille-comparaison-boucle-audit-recapture-v1.md` (`8c52e5a9058b10ecbc843ae81bba96a133cb83ce453968332f5c0035dbaeef2f`). Elle a été écrite et scellée avant toute lecture. Échelle de 0 à 5.
- **Pièces lues** (empreintes égales à leurs compagnons, `sha256sum -c` : OK) :
  - la réponse de Fable, v2, la plus récente scellée : `../reponse-fable-boucle-audit-recapture-v2.md` ;
  - sa contre-lecture par Opus, sur la v1 : `../contre-lecture-reponse-fable-boucle-audit-recapture-v1-opus-v1.md` (en-tête, verdict, table des constats) ;
  - la vérification des corrections : `../verification-corrections-boucle-audit-recapture-v2-opus-v1.md`, verdict « conforme », un constat mineur restant (R-1) ;
  - les calculs de Fable, `../calculs-boucle-audit-recapture-v1.txt` (par motifs) ;
  - la réponse d'Opus en effort maximal, `reponse-opus-max-boucle-audit-recapture-v1.md` (`4ff1c8fa…6a2c`), et ses calculs, `calculs-boucle-audit-recapture-opus-v1.txt` (en entier).
- **Pour trancher les contradictions** : N-060 v3, l. 33 ; N-075 v3, l. 248 ; N-076 v1, l. 80 et 189 ; le programme v2, l. 137 et 167 ; `.git/info/exclude`, l. 8.
- **Non ouvert** : les dossiers du collisionneur, sauf leurs noms ; les questions à l'organisme ; tout chemin cloisonné.

## Vérification des chiffres, à la page et à la ligne

Le texte des PDF est extrait par `pdftotext`, page par page. Les empreintes des PDF sont égales à leurs compagnons.

**Fable : neuf vérifications, toutes justes.**

| Chiffre ou citation | Source | Résultat |
|---|---|---|
| « Missing completely at random […] there is no partial verification bias involved » | Arifin et Yusof, 2509.12217v1, p. 2 | exact |
| Sensibilité 0,975 sans correction, 0,819 corrigée | idem, p. 7 (« Sn 0.9750000 ») et p. 9 (« Sn 0.8188629 ») | exact |
| Pièce tirée « independently after the prediction » ; « depends only on previously queried » | Rudoler et al., 2609.36049v1, p. 4 et p. 3 | exact |
| Verdicts faux une fois sur dix : 87 % de l'effet | Lyons Keenan et al., 2609.36490v1, p. 7 | exact |
| Aires sous la courbe 0,38 et 0,66 ; 1,00 sur le domaine | Taufeeque et al., 2602.15515v2, tableau 4, p. 7 : 0,376 ± 0,261 et 0,655 ± 0,360 ; 1,000 | exact. Les écarts types sont larges, et la note ne le dit pas |
| Recapture relue 1,00 pour un rappel vrai de 0,010 | calculs, l. 39 | exact |
| Audit orienté : 0,71 | calculs, l. 63 et 93 (0,714) | exact |
| 2,85 à 2,99 étiquettes, limite ln 20 | calculs, l. 106 à 110 | exact |
| Échelle des échelons : 0,34, 0,14 et 0,03 à trois étiquettes ; croisement à 109 ; pli de trois à 0,37 ; 0,996 | calculs, l. 129 à 136, 174 et 206 | exact |

**Opus : neuf vérifications, toutes justes.**

| Chiffre ou citation | Source | Résultat |
|---|---|---|
| « we require that f_t, π_t ∈ F_{t−1} » ; « fine-tuned on all information observed up to time t » | Zrnic et Candès, 2403.03208v3, p. 7 | exact |
| « safe by construction when each coin governs one commit » ; « in one direction only » | « Blindfold », 2610.37055v1, p. 1 et p. 12 | exact |
| « Since the query coin is drawn independently after y_t is chosen » | Rudoler et al., p. 12 | exact |
| « vanishing average error does not preclude substantial harm » ; « confidently wrong » | Rudoler et al., p. 8 et p. 17 | exact |
| « each verdict the monitor delivers leaks information » ; « presumes they have already identified the behavior » | Lyons Keenan et al., p. 1 et p. 6 | exact |
| Proportion de 5 % des données d'apprentissage | Gupta et Jenner, 2506.14261v4, p. 10 | exact |
| 0,635 contre 0,207 ; 0,367 ; 0,372, 0,160 et 0,323 ; 0,568 et 0,818 ; 0,955, 0,299 et 0,289 ; 2,851 à 2,991 | sortie des calculs, blocs A à F | exact |
| La commande de la section 6 | rejouée par moi : `[0.181, 0.276, 0.337, 0.359]` | exact |
| Prédiction B1 manquée de 0,001 (0,101 pour « au plus 0,10 ») | bloc B | exact, et dit par l'auteur |

**Les deux rendent indépendamment la même loi exacte** : 2,851 étiquettes pour K = 30, 2,991 pour K = 1 000, limite 2,996. Opus n'avait vu de Fable qu'une phrase sur la coupe, pas ce compte. Le compte est donc tenu par deux dérivations.

## Notes par critère

| Critère | Fable v2 | Opus max v1 | Raison, en bref |
|---|---|---|---|
| 1. Justesse des chiffres | 5 | 5 | Tout ce que j'ai contrôlé est juste chez l'une et l'autre |
| 2. Profondeur | 5 | 4 | Fable : quatre protections, cinq flèches, cinq endroits où l'aveugle compte, fuite de la vérité par les versions, sonde qui lit l'identité du suspect, oracle informé. Opus : dix ruptures, mieux chiffrées sur le remplacement et les régimes ; il ne voit ni les versions comme canal de fuite vers les concepteurs, ni les heurts voisins |
| 3. Originalité | 4 | 4 | Fable : coupe par rôle de l'épisode ; étape à étiquettes de construction ; table à quatre cases. Opus : transfert des prises de signature vers les familles d'excès ; capacité de la mise à jour déclarée et scellée ; union avec la sonde d'origine mesurée |
| 4. Honnêteté, R8 | 5 | 4 | Les deux disent « rien à revendiquer » et marquent ce qui est supposé. Fable a mené onze requêtes et une épreuve de sa recherche ; Opus n'a fait aucune recherche dédiée, mais il le dit, il déclare son exposition et une prédiction manquée |
| 5. Respect des règles et des nœuds | 5 | 3 | Opus ajoute « ni dans l'entraînement d'un agent » au point 4 ; son exception vaut « en service seulement » dans un programme sans service ; il ne nomme ni l'anti-circularité ni les moniteurs amnésiques. Fable v2 a été corrigée de ces défauts par sa contre-lecture |
| 6. Actionnabilité | 4 | 4 | Fable : six décisions, mais D-1 regroupe huit « oui ». Opus : cinq décisions plus nettes, une recommandation conditionnelle honnête, quatre gardes déjà jouées |
| 7. Coût | 3 | 4 | Fable : harnais à lignées, à rôles et à enclave, treize épreuves, trois passes, quota de Fable. Elle dit le prix de l'étape 1 (une famille consommée). Opus : neuf clauses, une passe ; le coût du bras de banc n'est pas chiffré |
| 8. Ce qui manque (5 = rien d'important) | 4 | 3 | Voir la section suivante |

**Qui l'emporte.** Fable, sur le fond réglementaire et la complétude : elle est la base à retenir. Opus, sur l'économie et sur trois apports chiffrés que Fable n'a pas.

## Ce que chacune a et que l'autre n'a pas

**Chez Fable seulement :**
1. La coupe par **rôle de l'épisode** (verdict, flux, pli retenu, hors rôle), valable au banc comme en déploiement. Le bras de flux est déclaré par un texte décisif scellé, sur le mot de Lazar.
2. Les **versions nées du flux sont closes aux concepteurs** : poids, seuils, scores par épisode. Elles ne servent de départ à aucune reconception (clause 5, épreuve 13). Opus ferme seulement les verdicts par épisode.
3. Le prix des négatifs exogènes : une sonde qui ne voit qu'eux peut lire **l'identité du suspect** (0,996 des épisodes sains signalés, calcul E). La parade est la table à quatre cases.
4. **L'étape 1 à étiquettes de construction** révélées au taux du plancher. C'est l'extension de l'épreuve de récupération accordée (N-053, point 5) ; aucun invariant de l'oracle n'y est touché.
5. **Trois heurts voisins** : l'anti-circularité (programme, l. 137) ; les moniteurs amnésiques (l. 167) ; les lecteurs aveugles à la condition, mais pas au score ni à la raison du tirage.
6. L'oracle informé chiffré (calcul F). Le seuil calé sur les témoins de la leçon : 2 % à 40 % de fausses alertes au lieu de 1 %.

**Chez Opus seulement :**
1. **Le remplacement** de la sonde d'origine, chiffré : sur ce que l'oracle ne voit pas, 0,37 → 0,16 ; l'union garde 0,32 (bloc B). C'est le péril le plus coûteux de son monde. Fable n'a ici qu'une clause et une épreuve à écrire.
2. **Les positifs selon le régime.** En excès, la sonde apprend l'échec honnête (0,57). Le transfert depuis une famille de signature donne 0,82 (bloc C). Opus en fait un test du passage obligé de N-075, § 6. Fable chiffre la dilution (0,03 contre 0,17), sans proposer de transfert.
3. Les **positifs fabriqués par l'attaquant**, comme menace nommée (Kloft et Laskov). Chez Fable, ce n'est qu'un paragraphe de principe.
4. Le **choix sur le relevé** en loi exacte : 0,367 pour 0,20 à dix versions. Fable a l'équivalent par le pli consommé, mais moins net.
5. **Quatre gardes jouées en code** (bloc G : vert sur le journal sain, rouge sur chaque artefact) et quatre tests de mort de la règle elle-même.
6. La **capacité** de la mise à jour (nombre de paramètres libres) et l'agrégation par maximum ou par attention (N-026), toutes deux scellées dans la procédure.
7. Une liste « Ne pas écrire ».
8. Le constat pratique que le dossier est exclu du suivi de git (`.git/info/exclude`, l. 8, vérifié) : verser ces fichiers demande un geste exprès.

## Contradictions, et qui a raison à la source

1. **La coupe par le lieu (« en service ») ou par le rôle de l'épisode. Fable a raison.**
   - L'amendement d'Opus garde le point 4 entier au banc et n'ouvre l'exception qu'« en service seulement ».
   - Or le programme n'a pas de service : N-076 dit « Toute mesure sur un modèle : sur devis » (l. 189) et fixe le premier pas au banc (l. 80).
   - Sous la lettre d'Opus, la boucle à étiquettes de l'oracle ne se mesure donc jamais sur des organismes. Son « bras déclaré » au banc, si ses étiquettes viennent de l'oracle, violerait le point 4 qu'il dit garder entier. Opus ne dit pas que ce bras devrait se contenter d'étiquettes de construction.
   - C'est exactement l'objection de Fable à (b) prise à la lettre. Son option (c) en hérite.
2. **L'ajout « ni dans l'entraînement d'un agent ». Fable a raison.**
   - N-075 v3 laisse « corriger par l'entraînement de l'agent sur l'issue » fermé, mais ouvrable par un bras à part avec son nœud (l. 248).
   - L'ajout d'Opus ferme cette voie d'avance par un changement de lettre non signalé. C'est le constat 6 de la contre-lecture, porté dans la v2 de Fable.
   - Opus garde aussi la parenthèse « (N-053) », que Fable signale comme mal attribuée (N-060 v3, l. 33).
3. **« Jamais sur un épisode qui sert à rendre un verdict » : la contradiction est apparente.**
   - Opus dit s'écarter de cette moitié de la coupe de Fable. Mais il ne l'a connue que par une phrase de résumé.
   - Chez Fable, un « épisode de verdict » est une lecture décisive : porte, famille tenue à l'écart, jeu final. Et sa clause 2 fait juger puis instruire chaque épisode de flux.
   - Opus D-2 (a) revient donc à la clause 2 de Fable, et Opus D-2 (b), la réserve qui n'instruit jamais, au pli retenu de Fable. Aucun désaccord de fond.
4. **Le coût des négatifs pris chez le suspect : pas de contradiction, deux mondes.**
   - Opus trouve un coût petit (0,058), dans un monde où ces négatifs font 2 % du lot. Fable trouve un coût fort quand la part cachée est haute (0,005, puis 0,00004).
   - Les deux concluent : négatifs exogènes par défaut.
   - Mais la règle d'Opus (« exogènes seulement ») n'a pas de parade contre la lecture de l'identité du suspect, que Fable montre. Il faut lui ajouter la table à quatre cases.
5. **Le heurt est « dans une flèche » (Fable) ou « à deux endroits » (Opus) : c'est une différence de cadrage.**
   - Opus lit la seconde moitié du point 4 par la précision (ii) de N-075, qui est une lecture « à confirmer ». Fable traite le même objet sous la protection du cloisonnement.
   - Les deux disent que la précision (i) est touchée et proposent de la restreindre.
6. **Le réapprentissage en dimension 4 096 à trois étiquettes rend 0,03 chez Fable et 0,013 chez Opus.**
   - Les suppositions diffèrent : un écart de 4 chez l'une, de 2 chez l'autre. La conclusion est la même : la boucle ne tient pas le seuil, elle sert après l'alarme.

## Synthèse recommandée pour Lazar

**À retenir.**
- **Le compte des étiquettes, tenu par deux dérivations indépendantes** : au taux minimal de la table du seuil, environ trois étiquettes arrivent avant le seuil toléré, quel que soit ce seuil. La boucle ne tient donc pas le seuil ; elle sert après l'alarme.
- **La structure commune, convergente** :
  - juger avant d'instruire, avec le score consigné avant le verdict ;
  - une procédure scellée, sans personne dans la boucle ;
  - aucune version jugée sur ce qui l'a instruite ;
  - les lectures décisives, la famille tenue à l'écart et le jeu final n'instruisent jamais ;
  - des négatifs exogènes par défaut ;
  - ajouter une version, ne jamais en remplacer une ;
  - aucun retour vers l'agent ;
  - rien à revendiquer (Rudoler et al. occupent la boucle à pièce au hasard).

**Base proposée** : l'option (b′) de Fable, enrichie de cinq apports d'Opus :
1. les positifs selon le régime : familles de signature ; une famille d'excès seulement après l'alarme, avec la part du sabotage déclarée ; et le transfert des prises de signature vers les familles d'excès comme voie utile ;
2. la capacité de la mise à jour, déclarée et scellée ;
3. le remplacement chiffré, comme épreuve de la clause « ajouter, ne jamais remplacer » ;
4. les positifs fabriqués par l'attaquant, comme menace nommée ;
5. les quatre gardes déjà jouées, comme premières épreuves du harnais.

L'amendement d'Opus n'est pas à reprendre, pour deux raisons : son exception « en service seulement » et l'ajout de lettre côté agent.

**Décisions qui changent.**
- **D-1** : le choix n'est plus entre (b′) et (c). Recommandation : (b′) enrichie. Confiance 0,65. C'est un nœud, sans défaut ; d'ici le mot de Lazar, le point 4 s'applique en entier.
- **D-2 d'Opus** : elle se dissout dans les clauses 2 et 4 de Fable. Lecture recommandée : tout épisode de flux juge puis instruit, et le pli retenu sert à certifier une version figée.
- **D-3 d'Opus (d'où viennent les positifs)** : elle entre comme décision neuve. Confiance 0,7.
- **D-4 d'Opus (ajouter, ne jamais remplacer)** : elle double la clause 7 de Fable. Elle est à garder, chiffre d'Opus à l'appui.
- **D-5** : les D-5 des deux notes fusionnent. Le premier test de mort de N-076 s'écrit à taux, capacité et compte d'étiquettes déclarés.
- **D-3 de Fable (étiquettes de construction d'abord)** : elle reste. Opus n'en a pas l'équivalent.
- **D-4 de Fable (les trois heurts voisins)** : elle reste.

**Réserves.**
- La note d'Opus n'est pas contre-lue. Ses apports propres doivent l'être avant d'entrer dans un texte décisif. Le texte d'amendement fusionné est une pièce de classe A, à rédiger par Fable (règle « qui conçoit »).
- Aucune des deux pièces n'est un protocole X complet : le collisionneur et l'organisme restent à faire tourner, sur le couple v2 et la question v2.
- Les mondes des deux notes sont des jouets gaussiens à directions plantées : ils montrent des mécanismes, pas des tailles d'effet du programme.
