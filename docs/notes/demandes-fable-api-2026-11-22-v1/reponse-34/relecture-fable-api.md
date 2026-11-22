# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHvyq7oug4y3VEYq1JUg`
- Heure (UTC) : 2026-11-22T12:08:12Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-34-note-des-revendications-v3-v1.md` — sha256 7e0a328e6d04e184e579a6e84bf6e14b2492adda22d0726a819c4fc8829349e3 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22A/relecture-fable-api.md` — sha256 2255a6a3a65ba04c4acfa16af3edd83c8f3f263e89dad00558a640b6529e461c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22B/relecture-fable-api.md` — sha256 c5980780f80fb7e54c8f925432d118bf698769bc248b846c63aa48108043138b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22C/relecture-fable-api.md` — sha256 f05051442f07b2f55cb06e982bd6c9f1721813c6848eb1182d69d8deed677d2e (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22P/relecture-fable-api.md` — sha256 cb010f4cbd12b5fb7fc237075b4f85dd6ed5858210cea69c1e2ea145bb5cb84e (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-27-luc/relecture-fable-api.md` — sha256 6a042a7b18124d5865acff68b05e4a3cf020285a5466f303dff8e6d0a0dbf672 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-29/relecture-fable-api.md` — sha256 2af768bc095e40a4831f173e9fff0dc7836134cf85ccd5627c3732221fad01c2 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-28-effort-max/relecture-fable-api.md` — sha256 1261c8eeb9f00711ec3a5e8a7438bb3c26ec5d04d6af342ceaa7ec766daa52b4 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
- Empreinte de l'invite envoyée : b091a70c4cf256e48077a0ff6e1a8b2d4a609a1a1eda94d9faf5283d4721a25d
- Jetons : entrée 98903, sortie 45448 (dont réflexion 35340), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.609144 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 34 — note des revendications, version 3 : réponse approfondie

**Conclusion d'abord.** La note suit : vingt-neuf lignes, six billets, douze contradictions, cinq décisions. Trois points avant lecture.
- La décision du 22 novembre sur le lemme (« revendiqué dans son application ») contredit ma réponse 27, qui l'écrit « mentionné, non revendiqué ». La note suit la décision ; la réponse 27 est à corriger.
- « Application » ne peut pas vouloir dire « le théorème cité vaut aussi chez nous » : ce serait vrai par construction. Je propose une lettre qui peut échouer.
- La liste des billets ne m'est pas jointe. Les six billets sont proposés ; les pièces n'en nomment que deux.

Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai lu aucun PDF (fichier d'article). Toute antériorité porte le statut « rapporté, non vérifié sur PDF » ; les titres viennent de ma mémoire.
- Je connais les décisions du 22 novembre par la demande, et N-075 à N-077 par mes revues, sans leur texte scellé.
- Les revues jointes sortent du même modèle que cette note : leur accord n'est pas une confirmation.
- Je ne nomme que des auteurs de travaux cités ; aucun chiffre publié n'est repris.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Écrire la note comme un registre vérifiable par programme** : identifiant, statut parmi quatre mots, décision source, phrase interdite en chaîne exacte. Un programme cherche ensuite ces chaînes dans tout le dépôt, billets compris.
- **Vérifier que chaque ligne revendiquée peut échouer.** Une ligne vraie par construction sous le modèle nul cité n'est pas une revendication.
- **Séparer trois engagements** : revendication, prévision scellée, mesure rapportée. Un billet n'affirme jamais au-dessus du niveau de preuve de sa ligne.
- **Écrire les phrases des billets avant le résultat**, issue par issue, issue indéterminée comprise.
- **Compter ce qui reste** : un papier sans ligne qui puisse échouer est une section.

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- Le texte scellé des décisions du 22 novembre, de N-003, N-004, N-069 et N-075 à N-077, non leurs résumés.
- La liste des billets et leurs brouillons.
- Les lignes « revendication » du registre des accords, dont plusieurs manquent [FAIT RAPPORTÉ, table, § 4].
- Les pages citées des antériorités.
- Les scores pas à pas au dépôt, pour vérifier que chaque témoin est calculable.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.
- Vocabulaire fermé de statuts ; toute montée de statut exige une décision datée.
- Recherche de chaîne exacte ; compte attendu : zéro.
- Par ligne : estimateur, modèle nul, témoins positif et négatif, unité indépendante, puissance.
- Double test unilatéral d'équivalence pour tout énoncé « ne dépend pas de » (Schuirmann, 1987, « A comparison of the two one-sided tests procedure and the power approach »).
- Matrice « billets par issues », scellée par empreinte avant lecture du résultat.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Le programme de recherche des phrases interdites : son issue ne dépend d'aucun avis.
- La lecture sur pièce par un modèle d'une autre famille, avec des énoncés témoins au statut connu mêlés aux nôtres.
- Un spécialiste de stéganalyse et un statisticien des garanties nucléaires, sur la seule lettre du lemme appliqué.
- Les essais « honnête contre honnête » et les bancs à vérité plantée.

## Demande reformulée

« Écris la note des revendications, version 3, comme un registre dont chaque ligne se vérifie sans toi : identifiant, statut parmi quatre, décision qui le fonde, grandeur et témoin qui la décideraient, citations obligatoires, phrase interdite en chaîne exacte. Vérifie qu'aucune ligne revendiquée n'est vraie par construction sous le modèle nul cité, lemme compris. Pour chaque billet, écris avant le résultat ce qui est permis sous chaque issue du premier saboteur discret, issue indéterminée comprise. Liste les contradictions entre pièces et qui les tranche. N'écris "neuf pour le champ" nulle part. Dis ce que tu n'as pas lu. »

---

# Note des revendications — version 3 (à contre-lire, puis sceller)

**Conventions.**
- *Revendiquée* : le programme s'engage, la ligne peut échouer. *Mesurée et rapportée* : aucun engagement sur le signe. *Citée* : appartient à autrui, sert d'outil ou de modèle nul. *Retirée*.
- Un statut suivi de « (22 nov.) » ou d'un numéro de décision est un FAIT RAPPORTÉ par la demande ou par la table. Les autres statuts, les thèses, grandeurs, témoins et phrases interdites sont des PROPOSITIONS.
- Aucune ligne ne porte « neuf pour le champ » (22 nov.).
- Dans les titres cités tels quels, « AI » désigne l'intelligence artificielle et « LLM » un grand modèle de langue.

## 1. Papiers et programme

### Papier A — le temps

**Thèse.** « Les lois héritées de la dissimulation répartie donnent un modèle nul de ce qu'un saboteur diffus peut cacher ; nous mesurons, sur des scores de sondes d'agents qui sabotent réellement, où ce nul tient, quels termes s'y ajoutent, et ce que l'accès interne rattrape qu'un second lecteur de texte ne rattrape pas. »

| Ligne | Statut | Grandeur ; témoin | Phrase interdite |
|---|---|---|---|
| A1. Loi en racine, référence estimée comprise | Citée, modèle nul (22 nov.) | Aucune ; le nul s'écrit par plan de référence | « nous établissons la loi en racine » |
| A2. Bilan mesuré contre le nul, sur scores de sondes d'agents | Revendiquée (22 nov.) | Exposant, terme entre tâches, constante par moniteur ; essai « jumeau contre jumeau », banc à vérité plantée | « le rappel croît avec l'horizon », comme résultat |
| A3. Lemme d'additivité, appliqué au contrôle | Revendiquée dans son application, énoncé d'origine cité (22 nov.) | Rapport des déplacements cumulés, sabotage fragmenté sur concentré, à dommage égal, dans une marge d'équivalence scellée ; fragmentation jouée par l'agent ; témoin positif : le maximum par action baisse | « notre lemme » ; « nous démontrons l'additivité » ; « la puissance ne dépend que du budget », pour un test séquentiel |
| A4. Théorème négatif | Citée seulement (22 nov.) | Aucune | « puissance égale au taux de faux positifs » ; « antécédent défectueux » |
| A5. Complémentarité | Revendiquée (second axe de la thèse retenue) | Écart de rappel entre l'union « meilleur lecteur de texte et sonde » et l'union « meilleur lecteur et second lecteur d'une autre lignée », à taux total de fausses alertes égal, famille tenue à l'écart ; témoins : second lecteur dupliqué, sonde aléatoire appariée | « la sonde voit ce que le texte manque » |
| A6. Position ou dépendance | Mesurée et rapportée | Tests de position et de dépendance ; substituts par permutation des pas | « les deux issues sont publiables » |
| A7. Du jeton à l'action | Mesurée et rapportée (question) | Maximum par action sous fragmentation | « angle mort identifié » |
| A8. Interaction flou contre net ; validité et robustesse | Mesurées et rapportées (N-055, N-062) | — | Toute phrase de revendication |
| A9. Marge asymétrique | Retirée (N-077, selon ma réponse 22A) | — | « marge asymétrique, resserrée » |
| A10. Porte de fin de phase 1 ; règle de la référence | Citées comme protocole | Épisodes honnêtes par seuil, intervalle du taux réel | « à 1 % de faux positifs », sans ce nombre |

**Sur A3** [HYPOTHÈSE]. Si le sabotage décale les scores de façon additive, l'indifférence de la somme à la répartition est le théorème cité : il n'y a rien à mesurer. Ce qui peut échouer chez un agent réel, c'est la conservation du déplacement, pour trois raisons :
- la sonde sature ;
- un acte assez petit ne laisse aucune trace ;
- des pas honnêtes compensent.

Une fragmentation fabriquée sur les scores rend l'énoncé vrai par construction : elle doit être jouée par l'agent. Pour un test séquentiel, l'indifférence reste une question tant que la simulation « tôt, tard, étalé » n'a pas parlé.

**Citations obligatoires.**
- A1 à A3 :
  - Ker, 2006, « Batch Steganography and Pooled Steganalysis » ;
  - Ker, 2007, « A Capacity Result for Batch Steganography » ;
  - Ker, 2010, « The Square Root Law in Stegosystems with Imperfect Information » ;
  - Filler, Ker et Fridrich, 2009, « The Square Root Law of Steganographic Capacity for Markov Covers » ;
  - Avenhaus et Jaech, 1981, « On Subdividing Material Balances in Time and/or Space » ;
  - Khilar, 2026 (arXiv 2610.13083, titre inconnu de moi).
- A4 : Arias-Castro, Bubeck et Lugosi, 2012, « Detection of Correlations » ; Zhang et Gao, 2026 (arXiv 2606.10456, titre inconnu de moi).
- A5 : Parrack, Attubato et Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts », avec son indice contraire.
- A7 : Makins et collaborateurs, 2026 (arXiv 2607.07368, titre inconnu de moi).

### Papier B — l'essaim

**Thèse.** « Dans un essaim de copies, un sabotage réparti a deux modèles nuls hérités : la somme globale pour la position, la frontière de détection des corrélations pour la dépendance. Nous mesurons la corrélation honnête entre copies, ce que le sabotage joué déplace, et ce que la lecture conjointe ajoute à la somme globale. »

| Ligne | Statut | Grandeur ; témoin | Phrase interdite |
|---|---|---|---|
| B1. Corrélation honnête entre copies | Revendiquée, comme mesure | Corrélation intraclasse par tâche ; essaim honnête contre essaim honnête | « sous le nul, les copies sont indépendantes » |
| B2. Gain de la lecture conjointe sur la somme globale | Revendiquée sur la seule strate où la dépendance bouge ; repli : section du papier A | Écart de rappel à fausses alertes égales ; substituts par échange de copies ; bases : somme globale, carré de la somme | « cœur vierge » ; « bat le séquentiel par agent », sans la somme globale |
| B3. Lemme d'additivité, entre copies | Revendiquée dans son application (22 nov. ; portée entre copies à confirmer) | Celle de A3, fragmentation entre copies | Celles de A3 ; « le temps et les agents, un même objet », comme apport |
| B4. Courbe selon le nombre d'agents | Mesurée et rapportée, prévision scellée | Pente sous la somme et sous le maximum, contre le terme de corrélation honnête | « décroît plus doucement », sans l'agrégateur |
| B5. Diversité des moniteurs | Retirée comme loi ; mesurée | Corrélation des erreurs, gain d'union | « la sécurité croît par la diversité effective » |
| B6. Diversification contre coordination ; riposte et fuite | En vigueur selon la table du 19 novembre ; non revues | — | — |
| B7. Délégation ; adversaire entraîné ; co-élévation comme méthode | Retirées (N-070, N-077) ; mesures descriptives | — | « co-élévation », sans dire position ou dépendance |

**Citations obligatoires.** Avenhaus et Jaech, 1981 ; Arias-Castro, Bubeck et Lugosi, 2012 ; Rose et collaborateurs, 2026 (arXiv 2604.01151, titre inconnu de moi) ; Makins ; Khilar. S'y ajoutent les quatre obligatoires de N-069 [FAIT RAPPORTÉ, table] : Gauthier, Bach et Jordan ; Helm, Priebe et Duderstadt ; Molinari et Bettineschi ; Mohsin et Rahman.

### Papier C — l'instrument

**Thèse.** « Sous attaque, les juges de texte se déplacent selon une loi mesurable, dont le modèle nul est un retrait vers le centre du corpus ; les sondes qui lisent l'agent auteur se déplacent moins, à une marge scellée ; le quorum par type d'accès en tire parti, sans garantie. »

| Ligne | Statut | Grandeur ; témoin | Phrase interdite |
|---|---|---|---|
| C1. Loi de déférence à destination libre | Revendiquée, resserrée | Écart de la destination au nul de retrait vers le centre ; bras placebo, banc à juge synthétique | « destination testée contre la moyenne du corpus », comme alternative |
| C2. Déplacement de la sonde de l'agent auteur ; usurpation de l'instructeur | Revendiquées en équivalence | Gain sous une marge scellée ; témoin positif : sonde contaminée par le style, détectée | « gain nul », « ≈ 0 » |
| C3. Trahison par les activations | Revendiquée, non revue | Hausse du score sous contrôle du style | — |
| C4. Taxe de déplacement | Revendiquée pour une classe d'attaquant et un budget déclarés ; non déclarable hors du dépôt | Franchissement de la marge en contexte seul | « le contexte seul n'y suffit pas » |
| C5. Quorum par type d'accès | Revendiquée, forme comparative | Quorum « juge et sonde » contre « deux juges de lignées différentes », à taux total égal ; corrélation des erreurs sans attaque | « plus robuste », sans le quorum de deux juges |
| C6. Le gain bénin prédit la robustesse | Revendiquée, prévision de rangs | Corrélation de rang ; nombre de moniteurs fixé par la puissance | « prédit l'effondrement sous attaque optimisée » |
| C7. Second terrain : juge statistique et juge-tournoi | Revendiquée, complétée | Fausses promotions selon la taille de l'archive et le nombre de propositions ; archive nourrie contre archive gelée | « garantie toujours valide », sans taille ni droit d'écriture |

**Réserve** [FAIT RAPPORTÉ, réponse 22C]. La recherche d'antériorité ne visait pas les juges : « non touché » y signifie « non cherché ».

**Citations.** Celles de la table du 19 novembre (§ 3) restent obligatoires. À lire avant tout texte :
- Bailey et collaborateurs, 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » ;
- Raina, Liusie et Gales, 2024, « Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment ».

### Programme

**Thèse.** « Pour chaque moniteur : un modèle nul hérité et nommé, une référence honnête déclarée (unité, taille, droit d'écriture), un écart mesuré chez de vrais agents. La seule garantie vient de l'audit tiré au hasard. »

| Ligne | Statut | Grandeur ; témoin | Phrase interdite |
|---|---|---|---|
| P1. Forme commune de thèse | Revendiquée comme méthode, non comme résultat | Un banc à vérité plantée par papier | « colonne vertébrale théorique » ; « trois résultats indépendants » |
| P2. Audit tiré au hasard, à plancher | Citée ; seule source de garantie (N-075) | — | « le programme garde une marge contre un saboteur diffus » |
| P3. Compte des regards par chute conjointe | Mesurée et rapportée, exploratoire | Part des silences du second lecteur où la sonde se tait, contre sa fausse alerte honnête ; trois ancres | « deux regards », sans la table |
| P4. Organisme d'idéation | Statuts de la table du 19 novembre, non revus ici | Récupération de puits plantés à budget égal | « originalité », comme résultat |
| P5. « Neuf pour le champ » | Aucune ligne (22 nov.) | Lecture sur pièce par un tiers | « neuf », « inédit », « premier », « zone libre », « personne n'a » |

**Citations obligatoires.**
- Greenblatt, Shlegeris, Sachan et Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ;
- Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe » ;
- Eckhardt et Lee, 1985, « A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors » ;
- Knight et Leveson, 1986, « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming ».

## 2. Billets

[FAIT RAPPORTÉ, table] Les pièces nomment un billet « Sparks » et un billet des lentilles ; leurs textes ne me sont pas joints. [PROPOSITION] Tout le reste de cette section.

**Issues du premier résultat**, lues sur la famille tenue à l'écart, seuils gelés sur les mêmes épisodes honnêtes :
- I, « pas discret » : le premier lecteur de texte prend le saboteur.
- II, « la sonde rattrape » : là où le second lecteur se tait, la sonde sonne plus que chez l'honnête, marge scellée dépassée.
- III, « chute conjointe » : la sonde se tait avec le second lecteur.
- IV, « indéterminée » : les intervalles ne séparent pas II de III.

| Billet et thèse | Aujourd'hui | Après I | Après II | Après III |
|---|---|---|---|---|
| 1. Loi héritée : « le contrôle a un modèle nul, et il n'est pas de nous » | Les lois citées, le plan de mesure, les prévisions scellées | Inchangé | Inchangé : l'écart au nul n'est pas encore mesuré | Inchangé |
| 2. Référence honnête : « un seuil vaut ce que vaut sa référence » | L'arithmétique du seuil estimé, refaite par un tiers | « Discret » dépend du seuil : chiffres avec intervalle | Idem | Idem |
| 3. Deux regards : « deux moniteurs ne valent deux que s'ils ne tombent pas ensemble » | La définition, les ancres, les voisins de la sûreté de fonctionnement | « Rien sur la sonde : l'organisme est à refaire » | « Sur cette famille, à cet échelon, la sonde compte pour un regard de plus » | « Sur cette famille, la sonde tombe avec le texte ; il reste l'audit au hasard » |
| 4. Ce que nous avons retiré, et pourquoi | Les retraits et leurs sources | Sans objet | Sans objet | Sans objet |
| 5. « Sparks » ; lentilles | Ce que leurs décisions permettent ; aucun résultat des lentilles dans une hypothèse | Sans objet | Aucune extension | Aucune extension |
| 6. Juges sous attaque | Le protocole et le nul par placebo | Sans objet | Sans objet | Sans objet |

Après IV, pour tous : « indéterminé à cette taille », avec le nombre d'épisodes. Sous toute issue, la phrase dit la famille, l'échelon, le nombre de cycles de reconception consommés, et si l'attaque est jouée par l'agent.

## 3. Contradictions encore ouvertes

Colonnes 1 et 2 : FAIT RAPPORTÉ par les pièces. Colonne 3 : PROPOSITION.

| Contradiction | Pièces | Qui tranche |
|---|---|---|
| 1. Lemme : « revendiqué dans son application » contre « mentionné, non revendiqué » et « retiré (décidé) » | Demande 34 ; réponse 27 (D6, D7, D14, EN-4) ; réponses 22A et 22P ; repli de N-004 | Le directeur (lettre), puis une session neuve (erratum) |
| 2. Unité du temps et des agents : revendiquée ou héritée | N-003 (table) ; réponse 27 (D9) | Le directeur, après lecture sur pièce d'Avenhaus et Jaech |
| 3. Forme du nul : √(n + n²/m) ou plan à exécutions jumelles | Réponse 27 (D5) ; réponse 22A | Le directeur (plan de référence) ; un spécialiste (dérivation) |
| 4. Somme « plate » selon le nombre d'agents, ou terme de corrélation honnête | Réponse 27 (D16) ; réponses 22B et 22P | L'essai sur essaims honnêtes ; correction par session neuve |
| 5. Critère du second regard : écart d'unions ou chute conjointe | Réponses 22A et 27 ; réponse 29 | Le directeur |
| 6. Comparaison « texte contre accès interne » portée en quatre lieux | Table, § 4 ; réponses 22C et 22P | Le directeur |
| 7. « Garantie toujours valide » dans trois énoncés, contre N-075 | Table ; réponse 22P | Le directeur |
| 8. Marge asymétrique : retirée, mais « resserrée » dans la table et présente au programme, version 3 | N-077 ; table ; réponse 27 | Une session neuve |
| 9. Juge au nul : le nul seul, ou la réunion seule | N-067 ; N-071 | Le directeur |
| 10. Critère de la porte de fin de phase 1 | N-074, en brouillon | Le directeur |
| 11. Papier porteur de « validité et robustesse » ; poids 0,65 ou 0,5 ; dix-sept décisions introuvables ; N-073 sans contre-lecture ; lignes de registre manquantes | Table, § 4 | Le directeur ; la session mère (fichiers, registre) |
| 12. Accord des revues, toutes du même modèle | En-têtes | Un modèle d'une autre famille |

## 4. Liste « ne pas écrire »

Toutes sont des PROPOSITIONS ; elles s'ajoutent aux phrases interdites des tables et aux listes de mes réponses 22A, 22B, 22C et 22P.
1. « Neuf pour le champ », « inédit », « premier à », « zone libre », « personne n'a relevé », avant la lecture sur pièce par un tiers.
2. « Notre théorème », « notre lemme », « notre loi ».
3. « Loi en racine », sans « modèle nul cité ».
4. « Garantie », pour un moniteur : elle ne vaut que pour l'audit au hasard.
5. « La bascule en n ≈ m », comme prévision.
6. « Deux issues publiables », sans calcul de puissance.
7. « Attaque », sans dire jouée par un agent ou écrite d'avance.
8. « Non trouvé », sans la recherche qui le fonde ; « non touché », pour ce qui n'a pas été cherché.
9. « Les revues convergent », sans « elles sortent du même modèle ».
10. « Les sondes détectent le sabotage discret », sans famille ni échelon.
11. « Table en vigueur », pour la version du 19 novembre.
12. Tout chiffre de l'état de l'art non vérifié sur pièce.

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer la lettre du lemme « revendiqué dans son application ».**
- *Enjeu.* Transposer le théorème cité est vrai par construction ; une revendication doit pouvoir échouer.
- *Option a : conservation mesurée du déplacement cumulé sous fragmentation jouée (ligne A3).* Avantage : réfutable, l'énoncé d'origine est simplement cité. Inconvénient : peut échouer ; demande un montage.
- *Option b : énoncé mathématique adverse de N-003 et N-004, appliqué aux sondes.* Avantage : continuité. Inconvénient : cœur occupé, forme séquentielle non simulée.
- *Option c : a maintenant, b après simulation et avis d'un spécialiste.* Avantage : rien n'est scellé sans épreuve. Inconvénient : deux temps.
- *Recommandation.* Option c. Confiance : 0,65.

**Décision 2 — Corriger ma réponse 27 là où elle contredit la décision sur le lemme.**
- *Enjeu.* D6, D7, D14 et EN-4 écrivent « non revendiqué » : deux textes du même jour se contredisent.
- *Option a : erratum court par une session neuve, avant scellement de cette note.* Avantage : une seule lettre en circulation. Inconvénient : une pièce de plus.
- *Option b : laisser cette note primer.* Avantage : aucun travail. Inconvénient : le programme, version 3, reste fautif.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 3 — Arrêter la liste des billets et sceller la matrice des issues avant le premier résultat.**
- *Enjeu.* Après le résultat, toute phrase paraît écrite pour lui.
- *Option a : liste confirmée, matrice scellée par empreinte.* Avantage : billets opposables. Inconvénient : fige des mots tôt.
- *Option b : écrire après.* Avantage : souplesse. Inconvénient : lecture après coup.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 4 — Désigner qui fait la lecture sur pièce ouvrant droit à « neuf pour le champ ».**
- *Enjeu.* Une session du même modèle partage mes angles morts.
- *Option a : modèle d'une autre famille, avec énoncés témoins.* Avantage : biais commun mesuré. Inconvénient : préparation.
- *Option b : session neuve du même modèle.* Avantage : immédiat. Inconvénient : accord ininterprétable.
- *Option c : a, plus un spécialiste pour A2 et A3.* Avantage : les deux lignes centrales sont lues par le métier. Inconvénient : délai.
- *Recommandation.* Option c. Confiance : 0,7.

**Décision 5 — Choisir le critère unique du « second regard » et son porteur.**
- *Enjeu.* L'écart d'unions et la chute conjointe peuvent diverger ; la comparaison vit en quatre lieux.
- *Option a : écart d'unions en critère (papier A pour la détection, papier C pour la corruptibilité), chute conjointe rapportée à titre exploratoire.* Avantage : aucun texte scellé touché. Inconvénient : un écart nul peut cacher un rattrapage.
- *Option b : chute conjointe en critère, par erratum.* Avantage : mesure juste du compte. Inconvénient : ancres non éprouvées.
- *Recommandation.* Option a. Confiance : 0,65.

FIN DE LA RÉPONSE
