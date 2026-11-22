# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHovkvQomzSBT3VxZcYh`
- Heure (UTC) : 2026-11-22T10:31:29Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-22B-revue-revendications-papier-B-v1.md` — sha256 d18648bef5218b4a6f49e70365e02443081066805ae8d7306f6c4a0508649a0b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md` — sha256 542b7bfc86497c0c9bc45ed7f1651162a47789b6b2f00325f989daaac42c59f3 (compagnon : vérifié)
  - remarques : `docs/notes/seconde-lecture-these-v1.md` — sha256 a4f751ce3981aa100d026e9b90a9214897f639717bdcc9c31a5680d32cfcfdf4 (compagnon : vérifié)
  - remarques : `docs/notes/lecture-steganographie-comptabilite-v1.md` — sha256 6d52ba5d033d5a71237337a6c27f6f257d80c8ecbfb7a32dbae30cc569ce8ac6 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22/relecture-fable-api.md` — sha256 22c5652113797a399d1d1df7fc8d4d6b100bcf04bd655118d51238c5ef3d7b64 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 24eec7ed250f8ed2fd9148cdb5fbf6dded7435f926283434618ac4b80a8070e4
- Jetons : entrée 71625, sortie 14635 (dont réflexion 6009), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.158400 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 22B — revendications et thèse du papier B : réponse approfondie

**Conclusion d'abord.** Aucune revendication du papier B ne tient telle qu'écrite : trois sont à resserrer, deux à remplacer, deux ne sont pas touchées par les pièces. Le mot « co-élévation » recouvre deux objets, dont chacun a un modèle nul hérité : une hausse commune de position dans un sous-groupe, et un excès de dépendance à marginales intactes. Tant qu'on ne sait pas lequel le sabotage joué produit, le papier B n'a pas de thèse scellable. Si c'est la position, la somme globale suffit et le papier se réduit à une section du papier A. Confiance d'ensemble : 0,55.

**Réserves.**
- Je n'ai lu aucun PDF : les trois notes sont mon seul accès aux pages.
- Je n'ai ni le texte de N-069, ni les tailles d'essaim du programme.
- Les réponses 9 et 22 viennent du même modèle que celle-ci : mon accord avec elles n'est pas une confirmation indépendante.
- Mes ajouts de mémoire portent « rapporté, non vérifié sur PDF ».
- Je ne confirme aucun identifiant arXiv de 2026 et je n'ai pas recalculé les empreintes.
- Je ne nomme que les auteurs des travaux cités.

Abréviations de pièces : « Stég » pour la lecture de la stéganographie, « Lect2 » pour la seconde lecture, « Rech » pour la recherche exhaustive.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS, sauf mention.

- **Séparer les deux sens de « co-élévation ».**
  - Hausse commune de la moyenne dans k copies sur n : c'est la détection d'un signal rare ou dense, dont la frontière oppose déjà la somme au maximum. La table la range comme classique (ligne du lemme).
  - Excès de corrélation à marginales identiques : c'est le cadre d'Arias-Castro et collaborateurs [FAIT RAPPORTÉ, Lect2, p. 2].
- **Mesurer d'abord la corrélation honnête entre copies.** Des copies à poids partagés sur un même travail ne sont pas indépendantes [HYPOTHÈSE]. Or le nul hérité suppose l'indépendance [FAIT RAPPORTÉ, Lect2, p. 2].
- **Vérifier que la frontière héritée parle aux tailles réelles.** Elle est asymptotique ; pour une dizaine de copies, les régimes dense et rare se confondent [HYPOTHÈSE].
- **Écrire le nul du gain temporel.** Le cadre hérité observe un seul vecteur [FAIT RAPPORTÉ, Lect2, p. 5]. Le programme en observe un par pas.
- **Poser la question de survie du papier** : que reste-t-il si le sabotage ne déplace que la position ?

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.

- Scores de sondes pas à pas, par copie, sur des essaims honnêtes : identifiants de tâche, d'essaim, de copie, rang du pas, et quelles copies partagent quel contexte.
- Activations brutes aux mêmes pas, pour recalculer la base « alignement d'activations » de Rose et collaborateurs.
- Les mêmes relevés dans le montage de fragmentation de Makins et collaborateurs.
- Texte de N-069 et pages de 2611.10620 qui fixent les contrôles de construit.
- Pages non lues : Zhang et Gao, p. 10 et 11 ; arbres de citations d'Arias-Castro et collaborateurs et d'Avenhaus, non parcourus [FAIT RAPPORTÉ, Rech, § 1].
- Données publiques de Rose et collaborateurs et de Khilar, si elles existent.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.

- **Composantes de variance** (tâche, essaim, copie, pas) et corrélation intraclasse entre copies honnêtes, avec rééchantillonnage par essaim.
- **Substituts par échange de copies** entre essaims honnêtes d'une même tâche : ils gardent la marginale de chaque copie et détruisent la dépendance entre copies. C'est le nul naturel de la question « position ou dépendance ».
- **Cinq statistiques sur les mêmes scores**, recalées au même taux de fausses alertes sur essaims honnêtes : somme globale, maximum par copie, carré de la somme, balayage de sous-groupes, test d'histogramme.
- **Simulation à taille finie** : puissance de chacune pour n, k et la corrélation honnête mesurée, aux tailles du programme.
- **Banc à vérité plantée** : coalition synthétique de position seule, puis de dépendance seule.
- **Calcul de puissance** en essaims indépendants, et non en pas.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.

- L'essai « essaim honnête contre essaim honnête », la simulation et les substituts : leur issue ne dépend d'aucun avis.
- Un statisticien de la détection de signaux rares, sur le tableau de revendications.
- Les auteurs de Rose et collaborateurs, à qui l'on demande : « votre alignement d'activations est-il notre statistique ? »
- La reproduction des bases publiées sur leurs propres données.
- Des énoncés témoins au statut connu, mêlés aux nôtres dans le collisionneur.
- La prévision scellée avant la porte G2.

## Demande reformulée

« Pour le seul papier sur l'essaim, voici la table de ses revendications, la thèse retenue et trois notes de lecture sur PDF. Pour chaque revendication : (1) dis quel objet statistique elle vise, hausse commune de position dans un sous-groupe ou excès de dépendance à marginales intactes, et nomme le modèle nul hérité de chacun, page citée ; (2) dis si l'énoncé est exact tel qu'écrit, s'il est vrai par construction sous ce nul, et s'il survit quand les copies honnêtes sont elles-mêmes corrélées ; (3) nomme la base la plus forte qu'il doit battre, somme globale comprise ; (4) rends un verdict (tenue, à resserrer, à retirer, à remplacer) et, s'il y a lieu, l'énoncé neuf ; (5) donne l'épreuve qui réfuterait l'énoncé neuf, la référence honnête qu'elle exige (unité, taille) et la puissance du plan aux tailles d'essaim réelles ; (6) gradue chaque "non trouvé" par la recherche qui le fonde ; (7) dis ce qu'il reste du papier si le sabotage joué ne déplace que la position ; (8) liste les phrases à ne plus écrire. Marque fait rapporté, hypothèse, proposition. Aucune zone vierge n'est déclarée libre. »

## Réponse à la demande reformulée

### Quatre constats avant la table

1. **Position : la somme globale est le nul.** Contre un total réparti, la somme des écarts est le test le plus puissant au pire cas, dans l'espace comme dans le temps. Cela vaut sous loi gaussienne à covariance connue et à taille fixe [FAIT RAPPORTÉ, Stég, Avenhaus et Jaech 1981, p. 25 et 30]. Si le sabotage décale les scores de façon additive, aucune statistique conjointe ne bat donc la somme dans ce cadre [HYPOTHÈSE].
2. **Dépendance : la frontière est héritée.** Le carré de la somme est puissant quand ρ·k²/n tend vers l'infini, pour k copies corrélées sur n et une corrélation ρ. Il est sans puissance quand k²/n tend vers zéro, où le test d'histogramme prend le relais [FAIT RAPPORTÉ, Lect2, p. 14 à 20].
   - Sur T pas indépendants, le cumul des carrés de la somme détecte quand ρ·k²·√T/n est grand : l'horizon achète de la détectabilité [HYPOTHÈSE, dérivation de ma main, à vérifier].
   - C'est élémentaire, et c'est le nul du gain « conjoint dans le temps ».
3. **La corrélation honnête est le terme de référence de l'essaim** [HYPOTHÈSE].
   - Avec une corrélation honnête ρ₀ entre copies, la variance de la somme globale vaut n·σ²·(1 + (n − 1)·ρ₀). La somme n'est donc plus « plate » en nombre d'agents.
   - L'excès de corrélation décelable est borné par l'erreur d'estimation de ρ₀ et par sa variation entre tâches.
   - L'unité de la référence exigée par N-076 devient l'essaim honnête, non le pas.
4. **La part empirique est occupée par morceaux** [FAIT RAPPORTÉ, Rech, § 4].
   - Rose et collaborateurs (2604.01151, p. 17) : alignement d'activations entre agents, qui bouge « même quand les scores individuels restent normaux ».
   - 2607.06807 (p. 4) : activations corrélées entre agents compromis.
   - 2611.10620 (p. 1) : balayage en ligne sur les scores d'agents.
   - Khilar (2610.13083, p. 1-2) : détecteur de comptes qui « bougent ensemble », en boîte noire.
   - Non trouvé après la recherche décrite : un agent réel qui préserve lui-même la marginale de ses scores de sonde.

### Table

La colonne « antériorité » est un FAIT RAPPORTÉ par la pièce citée. Verdicts, énoncés neufs et épreuves sont des PROPOSITIONS.

| Revendication | Antériorité qui la touche | Verdict | Énoncé neuf | Épreuve qui le réfuterait |
|---|---|---|---|---|
| Co-élévation entre copies, volets (a) à (d) | Arias-Castro et collaborateurs 2012, p. 2, 14-20 (Lect2). Rose et collaborateurs, p. 17 ; 2607.06807, p. 4 ; 2611.10620, p. 1 ; Khilar, p. 1-2 (Rech). | À resserrer : une mesure, non une méthode. Le volet (a) est à remplacer. | « Sur des scores de sondes de copies d'un même modèle, nous rapportons la corrélation honnête entre copies et sa référence (en essaims), puis ce que le sabotage joué déplace : position, dépendance, ou les deux. La statistique de dépendance est rapportée contre la frontière héritée, à n, k et corrélation honnête déclarés. » | Essaims honnêtes : alarme au-dessus du niveau. Sous sabotage : aucun test de dépendance ne dépasse son niveau sur les substituts. |
| Statistique conjointe dans le temps et entre agents | Avenhaus et Jaech 1981, p. 30 (Stég). Zhang et Gao, proposition 2, p. 4 (Lect2). Khilar, proposition 1 (Rech). Podkopaev et collaborateurs 2023, « Sequential kernelized independence testing » (rapporté, non vérifié sur PDF). | À remplacer. | « Base obligatoire : la somme globale. Le gain n'est revendiqué que sur la strate où le sabotage déplace la dépendance ; ailleurs, l'égalité avec la somme est le résultat attendu. La garantie vaut sous une référence de corrélation honnête de taille déclarée. Adversaire entraîné : mesure descriptive (N-077). » | Aucun gain sur la somme globale à fausses alertes égales dans la strate « dépendance ». Ou niveau non tenu sur essaims honnêtes neufs. |
| Courbe de sécurité selon le nombre d'agents | Avenhaus et Jaech, p. 25, 31 (Stég). Makins et collaborateurs 2607.07368, p. 1 (Rech). | À remplacer : l'énoncé dépend de l'agrégateur. « Plus doucement » peut n'être qu'un changement d'échelle dû à une meilleure constante [HYPOTHÈSE]. | « À budget et nombre total d'actions fixés : sous le maximum, la détection baisse avec le nombre d'agents ; sous la somme globale, elle ne baisse que par le terme (n − 1)·ρ₀. La sonde change la constante, non la forme. » Prévision à sceller. | La somme baisse plus que ne le prédit ρ₀ mesuré. Ou les formes boîte blanche et boîte noire diffèrent après remise à l'échelle. |
| Nombre et diversité des moniteurs | Nombre effectif sous corrélation : Kish 1965, « Survey Sampling » (rapporté, non vérifié sur PDF). Parrack et collaborateurs, p. 7 (Lect2). | À retirer comme loi : élémentaire [HYPOTHÈSE]. Garder comme mesure. | « Nous mesurons la corrélation des erreurs entre moniteurs et le gain d'union à taux total de fausses alertes égal. » | — (mesure) |
| Diversification contre coordination | Aucune des trois pièces. | Non touchée. Un signe est à ajouter : diversifier réduit ρ₀, et peut aussi réduire le signal commun des copies qui sabotent [HYPOTHÈSE]. | Prévision de signe à sceller. | Signal de dépendance inchangé sous diversification. |
| Riposte et fuite | Aucune des trois pièces. | Non touchée. | — | — |
| Survie d'une contrainte à la délégation (mesure) | Aucune des trois pièces. | Non touchée. | — | — |
| Porte G2 | Makins, p. 1 ; Rose, p. 17 (Rech). Arias-Castro, p. 14-15 (Lect2). | À resserrer : ajouter comme bases nommées la somme globale et le carré de la somme, et faire précéder la porte de l'essai sur essaims honnêtes. | — | — |

### Gradation des « non trouvé »

- « Agent réel qui préserve sa marginale » : 36 requêtes, 17 PDF, quatre arbres de citations non parcourus [FAIT RAPPORTÉ, Rech, § 1]. C'est une question, non une ouverture.
- « Énoncé en boîte blanche » de l'aveuglement : même recherche. L'énoncé hérité est de plus contredit dans sa lettre pour la somme et le maximum [FAIT RAPPORTÉ, Lect2, § 2].
- Frontière pour des vecteurs répétés dans le temps : non cherchée. Ma dérivation n'est qu'un nul de travail [HYPOTHÈSE].
- Signal rare en position : je cite de mémoire Ingster 1997, « Some problems of hypothesis testing leading to infinitely divisible distributions », et Donoho et Jin 2004, « Higher criticism for detecting sparse heterogeneous mixtures ». Pour le balayage : Kulldorff 1997, « A spatial scan statistic ». Les trois sont rapportés, non vérifiés sur PDF.

### La thèse du papier B, revue

- **Formulation proposée** [PROPOSITION] : « Dans un essaim de copies, un sabotage réparti a deux modèles nuls hérités : la somme globale pour la position (Avenhaus et Jaech 1981), la frontière de détection des corrélations pour la dépendance (Arias-Castro et collaborateurs 2012). Sur des scores de sondes, nous mesurons la corrélation honnête entre copies, ce que le sabotage joué déplace, et ce que la lecture conjointe ajoute à la somme globale. »
- **Si le sabotage ne déplace que la position** [HYPOTHÈSE] : il reste la corrélation honnête mesurée, la forme de la courbe sous la somme, et le résultat négatif « la somme suffit ». C'est une section du papier A, non un papier.
- **Prévisions à sceller** [HYPOTHÈSE, chances en jugement].
  - La corrélation honnête entre copies est positive et dépend de la tâche : 0,8.
  - Le sabotage des organismes déplace surtout la position : 0,6.
  - La statistique conjointe ne gagne rien sur la somme globale hors de la strate « dépendance » : 0,6.
- **Puissance** [HYPOTHÈSE, ordre de grandeur à refaire]. L'unité indépendante est l'essaim. Déceler un excès de corrélation de 0,1 sur une corrélation honnête variable entre tâches demande sans doute plus de cent essaims par bras.
- **Borne déclarée** [FAIT RAPPORTÉ, Rech, Khilar, proposition 1] : une campagne qui épouse la loi conjointe est indétectable. Le bras « adversaire entraîné contre la statistique » tend vers ce cas, d'où son statut descriptif [PROPOSITION].

### Phrases à ne plus écrire

Toutes sont des PROPOSITIONS.

1. « La co-élévation détecte une coalition de taille inconnue », sans n, k, la corrélation honnête et le régime.
2. « Co-élévation », sans dire position ou dépendance.
3. « Garantie toujours valide tenue sous dépendance », sans la source de validité ni la taille de la référence en essaims.
4. « Bat le séquentiel par agent et la coupe transversale », sans la somme globale.
5. « Décroît plus doucement avec le nombre d'agents », sans l'agrégateur.
6. « Y compris sous un adversaire entraîné contre elle », comme revendication.
7. « La sécurité croît par la diversité effective », comme loi.
8. « Les scores individuels restent normaux, seule la lecture conjointe voit », comme apport : Rose et collaborateurs l'écrivent (p. 17).
9. « Le temps et les agents, un même objet », comme apport : Avenhaus et Jaech, p. 25.
10. « Premières statistiques de dépendance entre copies sur activations », « inédit », « cœur vierge ».
11. « Sous le nul, les copies sont indépendantes. »
12. « L'aveuglement des marginales, énoncé sur des scores de sondes » : écrire « l'espérance des statistiques additives ne bouge pas ».

### Dépendances vers les autres demandes

- **Papier A** : la question « position ou dépendance », l'unité de la référence et la base « somme globale » sont communes ; son essai sur jumeaux honnêtes fournit le harnais.
- **Papier C** : la mesure de diversité des moniteurs recoupe le quorum par type d'accès.
- **Programme d'ensemble** : N-076 est à étendre à la référence de corrélation (unité : l'essaim honnête) ; la table est à refaire après N-075 à N-077.

## Question neutre pour le collisionneur

« Plusieurs exemplaires identiques d'un même programme autonome travaillent en parallèle sur une tâche commune et longue. À chaque action de chaque exemplaire, un détecteur rend un nombre. On veut savoir si certains exemplaires, en nombre inconnu, agissent de façon nuisible, alors qu'aucun nombre isolé ne sort de l'ordinaire. (1) Quelles façons de combiner ces nombres, entre exemplaires et dans le temps, connaissez-vous ? Pour chacune, dans quelles conditions est-elle la meilleure, et dans quelles conditions ne voit-elle rien ? Donnez une preuve ou un contre-exemple. (2) Quels résultats publiés, dans quelque domaine que ce soit, fixent les limites de ce problème ? Dites ce qu'ils supposent exactement. (3) Que faut-il mesurer sur des exemplaires sans faute avant toute conclusion, et en quelle quantité ? (4) On vous remet une liste d'énoncés sur ce problème, dans un ordre tiré au hasard, certains de l'équipe, d'autres non. Classez chacun : établi ailleurs, conséquence immédiate d'un résultat établi, ouvert, ou faux. (5) Quelle expérience unique départagerait les combinaisons, et quelle taille d'échantillon lui faut-il ? Dites votre degré de certitude et ce que vous citez de mémoire. »

La liste jointe reprend les énoncés de la table en mots courants, témoins compris [PROPOSITION].

## Décisions qui reviennent au directeur

**Décision 1 — Approuver la demande reformulée et la question neutre avant l'envoi au collisionneur.**
- *Enjeu.* Sans témoins, un accord unanime ne se distingue pas d'un biais d'accord.
- *Option a : envoi avec six à huit énoncés témoins écrits par un agent neuf.* Avantage : taux de détection mesuré. Inconvénient : une préparation de plus.
- *Option b : envoi sans témoins.* Avantage : immédiat. Inconvénient : convergence ininterprétable.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Fixer la thèse du papier B.**
- *Enjeu.* La thèse de N-069 promet une supériorité que la somme globale peut annuler.
- *Option a : deux nuls hérités, corrélation honnête mesurée, question « position ou dépendance », gain rapporté contre la somme.* Avantage : toute issue ferme quelque chose. Inconvénient : papier de mesure, peut-être mince.
- *Option b : garder N-069 tel quel.* Avantage : continuité. Inconvénient : énoncés non réfutables sans base ni référence.
- *Option c : fondre d'emblée le papier B dans le papier A.* Avantage : économie. Inconvénient : renonce avant la mesure.
- *Recommandation.* Option a, l'option c étant le repli scellé si la position seule bouge. Confiance : 0,6.

**Décision 3 — Dire ce que « co-élévation » désigne.**
- *Enjeu.* Deux objets, deux nuls, deux littératures : le mot unique masque lequel est mesuré.
- *Option a : deux statistiques nommées, position et dépendance, rapportées côte à côte.* Avantage : réfutable. Inconvénient : réécriture de N-069.
- *Option b : dépendance seule.* Avantage : cœur propre. Inconvénient : vide si le sabotage ne la déplace pas.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 4 — Réviser la porte G2.**
- *Enjeu.* La porte compare à l'agrégation par agent, non à la somme globale, et suppose une référence honnête qui n'a pas été mesurée.
- *Option a : ajouter la somme globale et le carré de la somme comme bases, et faire précéder la porte de l'essai sur essaims honnêtes et du calcul de puissance en essaims.* Avantage : une porte qui peut échouer pour de bonnes raisons. Inconvénient : coût en essaims honnêtes.
- *Option b : porte inchangée.* Avantage : aucun délai. Inconvénient : succès possible contre une base faible.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 5 — Fixer le sort de la courbe selon le nombre d'agents, de la loi de diversité des moniteurs et du bras « adversaire entraîné ».**
- *Enjeu.* La première dépend de l'agrégateur, la deuxième paraît élémentaire, le troisième contredit N-077.
- *Option a : remplacer la courbe par l'énoncé par agrégateur, ramener la diversité à une mesure, rendre le bras descriptif.* Avantage : cohérent avec la thèse retenue. Inconvénient : deux hypothèses de moins au papier.
- *Option b : attendre le collisionneur.* Avantage : une seule passe. Inconvénient : des énoncés caducs restent citables.
- *Recommandation.* Option a, en version provisoire scellée après le collisionneur. Confiance : 0,65.

FIN DE LA RÉPONSE
