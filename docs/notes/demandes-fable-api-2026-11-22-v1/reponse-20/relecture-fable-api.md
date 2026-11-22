# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHaFYiLyJVfFxAR1t43W`
- Heure (UTC) : 2026-11-22T07:33:53Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-20-billet-drapeau-sabotage-diffus-v1.md` — sha256 29d2cd23a8fe2185b6a245ab29b8994740ef1d0b10e881eb34a24d2f80583406 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-2/relecture-fable-api.md` — sha256 542b7bfc86497c0c9bc45ed7f1651162a47789b6b2f00325f989daaac42c59f3 (compagnon : vérifié)
- Empreinte de l'invite envoyée : db2918f6f03db2ca5fa0d8f7a1e15bba3a8d49d1abebceb488c0c76400b3d4f2
- Jetons : entrée 53970, sortie 23619 (dont réflexion 14760), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.376520 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 20 — billet sur le sabotage diffus et sa détection : réponse approfondie

**Conclusion d'abord.** Aucun résultat n'est revendicable aujourd'hui, car les pièces ne contiennent aucune mesure. Le billet peut planter une date, une question, un cadrage cité et un protocole, et rien d'autre. Seuls un engagement daté et une mesure faite échappent au risque d'être devancé ; une question publiée l'augmente. La plus petite mesure qui ne touche aucun secret est le versant honnête de l'essai « jumeau contre jumeau ». Je recommande d'engager maintenant par empreinte, hors du dépôt, et de publier le billet avec cette mesure. Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai lu aucun PDF, ni le texte de « go recos 9 », ni la passation, ni N-075 à N-077 (résumés seulement), ni le billet « Sparks ».
- J'ignore si des exécutions honnêtes existent déjà, où le billet paraîtrait, et la date de la porte de fin de phase 1 (G1).
- Les antériorités que j'ajoute sont citées de mémoire : « rapporté, non vérifié sur PDF ». Je ne confirme aucun identifiant arXiv de 2026.
- Je n'ai pas recalculé les empreintes.
- « Sans nom de personne » : je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Séparer les sens du mot « drapeau »** [PROPOSITION] : priorité de résultat, de question, de protocole, de date. Les pièces ne fondent que les trois dernières. La priorité de question vaut peu sans mesure (Merton, 1957, « Priorities in scientific discovery » ; rapporté, non vérifié sur PDF).
- **Faire l'analyse de menace du billet lui-même** [PROPOSITION], pour trois lecteurs : le groupe concurrent, les concepteurs de moniteurs du programme (N-054), les corpus d'entraînement de modèles futurs (N-053).
- **Appliquer le principe de Kerckhoffs** [PROPOSITION] : le mécanisme est public, les clés sont secrètes (Kerckhoffs, 1883, « La cryptographie militaire » ; rapporté, non vérifié sur PDF). N-075 publie déjà le plancher d'audit ; les graines restent secrètes.
- **Chercher la plus petite mesure sans secret** qui change le billet de question en résultat [PROPOSITION].
- **Vérifier la cohérence des pièces entre elles** avant d'écrire une phrase publique (voir B2) [PROPOSITION].
- **Ancrer la date hors du dépôt** [HYPOTHÈSE]. Les empreintes internes prouvent l'intégrité d'une pièce. Elles ne prouvent pas sa date à un tiers, sauf ancrage externe que les pièces ne montrent pas.

## 2. Données brutes de départ

- Les pages décisives de Ker 2010 et d'Avenhaus et Jaech 1981, relues par un second lecteur, et les 17 PDF du dossier, plutôt que les notes.
- Les quatre arbres de citations non parcourus (Ker 2006 et 2007, Arias-Castro 2012, Avenhaus) [FAIT RAPPORTÉ, note de recherche, § 1].
- Le texte exact de « go recos 9 », de N-054, N-062, N-075 et N-076.
- Tout texte déjà public du programme, billet « Sparks » compris, pour y chercher les douze phrases fautives de la réponse 9.
- Le registre de scellement : ce qui est daté, et par qui la date est vérifiable.
- L'inventaire des secrets : mode tenu à l'écart, famille tenue à l'écart, banque de tâches, dommages plantés, graines d'audit, poids, couches et seuils des sondes.
- Les scores pas à pas des exécutions honnêtes, s'il en existe, avec l'identifiant de tâche.
- Le calendrier : date de G1 et durée de l'essai « jumeau contre jumeau ».

## 3. Méthodes et outils

- **Tableau de revendications phrase par phrase** : type, preuve dans les pièces, antériorité la plus proche et sa page.
- **Matrice de fuite** : chaque information croisée avec chaque mesure à venir et chaque lecteur.
- **Engagement cryptographique salé** [PROPOSITION]. Une prévision courte se retrouve par essais successifs si l'empreinte n'a pas de sel. L'horodatage se fait par un tiers (Haber et Stornetta, 1991, « How to time-stamp a digital document » ; rapporté, non vérifié sur PDF).
- **Préenregistrement** (Nosek, Ebersole, DeHaven, Mellor, 2018, « The preregistration revolution » ; rapporté, non vérifié sur PDF).
- **Test de devinette** par un agent neuf d'une autre lignée (voir B6).
- **Lecture adverse** : « avec ce billet, comment publier avant eux en trois semaines ? »
- **Veille** : les 36 requêtes de la note rejouées chaque semaine jusqu'à parution.
- **Marqueur canari** dans le billet, pour l'exclure des corpus (Srivastava et collaborateurs, 2022, « Beyond the Imitation Game » ; rapporté, non vérifié sur PDF).

## 4. Ce qui vérifie hors du directeur et de Claude

- Un tiers horodateur : n'importe qui recalcule l'empreinte à la révélation.
- Un spécialiste de stéganalyse, sur la seule table de transport.
- Un agent neuf d'une autre lignée, pour la devinette.
- L'équipe qui écrit le mode tenu à l'écart, pourvu que ce mode soit scellé avant la parution.
- L'issue de l'essai, comparée à la prévision engagée.
- Les commentaires publics, puis les pairs.

## Demande reformulée

« Écris le plan et les phrases porteuses d'un billet public daté sur le sabotage étalé d'agents de langue et sa détection par accumulation de scores. Pour chaque phrase porteuse, donne son type (citation, question, protocole, prévision engagée, résultat), la preuve qui l'appuie aujourd'hui dans les pièces, l'antériorité la plus proche avec sa page ; retire toute phrase sans preuve. Classe chaque information du programme en trois rangs : publiable, engagée par empreinte sans être révélée, tenue secrète ; justifie chaque rang par la mesure à venir qu'une divulgation fausserait, et par quel lecteur. Pour chaque élément publiable, estime le risque d'être devancé et ce que le billet y change. Dis quelle mesure minimale changerait le billet de question en résultat, et s'il vaut mieux l'attendre. Relève les contradictions entre pièces qui interdisent une phrase. Donne les tests, indépendants de l'auteur, qui montreraient que le billet ne fuit rien et ne revendique rien d'occupé. »

---

## (B) Réponse

### B1. Revendicable aujourd'hui, ou non

**Écrivable aujourd'hui, comme fait sur notre travail et jamais comme nouveauté :**

| Élément | Preuve dans les pièces | Condition |
|---|---|---|
| La recherche faite et ses bornes (36 requêtes, 17 PDF, quatre arbres non parcourus) | Note de recherche, § 1 [FAIT RAPPORTÉ] | Dire les quatre arbres |
| La loi héritée, en √(n + n²/m), citée | Ker 2010, p. 7 et 11 ; Avenhaus et Jaech 1981, p. 25, 30 et 31, selon la note de lecture citée par la réponse 9 [FAIT RAPPORTÉ] | Second lecteur ; unité de m fixée |
| Les voisins en contrôle | 2610.13083, p. 5, 9 et 10 ; 2606.10456, p. 3 et 8 ; 2607.07368, p. 45 ; 2604.01151, p. 17 [FAIT RAPPORTÉ, note de recherche] | Aucun chiffre de ces articles |
| Les choix de méthode : plancher d'audit publié et non revendiqué, sondes comme accélérateur, référence déclarée | N-075, N-076 [FAIT RAPPORTÉ, contexte] | Sans mot de priorité |
| La question et le protocole « jumeau contre jumeau » | Réponse 9 ; thèse retenue par le directeur [FAIT RAPPORTÉ] | Écrits comme question |

**Non revendicable aujourd'hui :**

- **Toute mesure** [FAIT RAPPORTÉ] : exposant, terme entre tâches, constante par moniteur, complémentarité. La table des revendications ne porte « aucun chiffre de résultat ».
- **Les dérivations de la réponse 9** (m = r·n, facteur √(1 + 1/r), terme n·τ) [HYPOTHÈSE] : elles sont de ma main, non vérifiées et élémentaires.
- **Le régime n/√m comme nôtre** : c'est Ker 2010. « Non trouvé en contrôle » ne vaut qu'« après la recherche décrite ».
- **Le lemme et le théorème négatif** : retirés par le directeur.
- **L'inégalité d'étalement en séquentiel** [HYPOTHÈSE] : conjecture, et la littérature des bilans séquentiels n'est pas lue.
- **La complémentarité** : le parent direct (Parrack, Attubato, Heimersheim, 2025) n'est pas lu.
- **L'architecture d'audit** : occupée selon la réponse 2 (Shekhar, Xu, Lipton, Ramdas, 2023, « Risk-limiting financial audits via weighted sampling without replacement » ; rapporté, non vérifié sur PDF).
- **Une date opposable** [HYPOTHÈSE] : rien dans les pièces n'ancre les empreintes chez un tiers.

### B2. Contradictions entre pièces qui interdisent une phrase

- **La table des revendications est en retard** [FAIT RAPPORTÉ]. Datée du 19 novembre, elle range encore le théorème (T) et le lemme (L) parmi les revendications « resserrées ». La thèse retenue le 22 novembre les retire. Un billet écrit depuis la table revendiquerait ce qui est retiré.
- **La phrase 1 du § 5 de la note de recherche est à écarter** [HYPOTHÈSE]. Elle présente comme « non trouvée » l'invariance de la somme à la répartition. La réponse 9 la rapporte comme héritée pour la somme (Avenhaus et Jaech 1981 ; Ker 2006). Écrite en accroche, elle change la limitation d'un champ voisin en trou du nôtre.
- **La phrase 3 du même § 5 promet un énoncé retiré** [FAIT RAPPORTÉ]. Elle dit « nous l'énonçons sur des scores de sondes ». Seule sa moitié « nous le mesurons » survit, au futur.
- **Le mot « antécédent défectueux » ne peut pas paraître** [HYPOTHÈSE]. La table l'emploie pour 2606.10456. La proposition 1 de cet article est vraie pour une attaque qui préserve le multi-ensemble des scores, et fausse si elle préserve seulement les marginales par coordonnée [FAIT RAPPORTÉ, N-003]. Le billet ne dit rien de ce défaut tant que la classe d'attaque de la page 3 n'est pas relue et le contre-exemple simulé.

### B3. Trois rangs de divulgation

| Rang | Information | Mesure qu'une divulgation fausserait, et par qui |
|---|---|---|
| Publiable | Loi héritée et table de transport ; voisins cités ; question générale ; protocole « jumeau contre jumeau » ; existence d'un plancher d'audit et d'un tirage secret ; existence d'un mode tenu à l'écart, sans sa nature ; bornes de la recherche | Aucune : ce sont des mécanismes [HYPOTHÈSE] |
| Engagé par empreinte, non révélé | Prévisions chiffrées ; plan d'analyse ; unité de m ; liste des modes ; comparaison de la référence par tâche et par régime | Un concurrent y lirait le plan de l'expérience. Les commentaires déplaceraient la prévision avant scellement (N-076). |
| Secret | Nature du mode tenu à l'écart ; famille tenue à l'écart ; banque de tâches et dommages plantés ; graines d'audit ; poids, couches et seuils des sondes | Porte G1 par mode (N-054) : un concepteur de moniteur qui lit le mode l'invalide. Reconception (N-062) : une famille décrite n'est plus « jamais servie ». Taux de détection par dommages plantés (N-075). |

Trois précisions :

- **L'ordre compte** [PROPOSITION]. La prévision est scellée avant la parution, et le mode tenu à l'écart aussi. Sinon le billet et ses commentaires entrent dans l'un ou dans l'autre.
- **Le sens de la fuite** [HYPOTHÈSE]. Un auteur de mode qui a lu le billet connaît mieux les moniteurs : l'épreuve durcit sans devenir invalide. La fuite inverse (mode vers moniteurs) est celle qui invalide.
- **Les organismes ne lisent pas le billet** [HYPOTHÈSE]. Ils sont réglés par le programme. Le risque de corpus concerne la seconde famille de modèles et la mesure de conscience d'évaluation (N-053) : le marqueur canari suffit, à coût nul.

### B4. Le risque d'être devancé

- **Deux choses échappent au risque** [HYPOTHÈSE] : une date engagée et une mesure faite. Une question publiée donne la feuille de route sans donner la mesure.
- **Les voisins ont déjà les données** [FAIT RAPPORTÉ, note de recherche]. 2607.07368 mesure, chez de vrais agents, la dépendance du soupçon d'un commit à l'autre (p. 45). 2610.13083 chiffre la loi en racine sur des données réelles et écrit qu'il faut « protéger la référence » (p. 10). L'un et l'autre sont à un pas d'ajuster le modèle nul, en boîte noire.
- **Chances, en jugement et sans base de mesure** [HYPOTHÈSE]. Qu'une mesure en boîte noire du bilan d'accumulation sur agents, avec référence estimée, paraisse sous trois mois : 0,3. Qu'une mesure sur activations internes paraisse : 0,1. Un billet détaillé relève la première ; je ne sais pas chiffrer de combien.
- **La part la moins exposée exige l'accès interne** [HYPOTHÈSE] : constante par moniteur et complémentarité, avec le contrôle « seconde boîte noire ». C'est aussi la part la moins prouvée.
- **La veille a des trous** [FAIT RAPPORTÉ]. 2606.10456 n'a aucun citant indexé et quatre arbres manquent. Le programme peut déjà être devancé sans le savoir.

**Ce que le billet achète** [HYPOTHÈSE] : une date sur la question, une relecture gratuite de la table de transport par des spécialistes, et une discipline d'erratum.

**Ce qu'il coûte** : la feuille de route donnée, et un engagement public sur une thèse avant l'essai. La réponse 9 dit que si le nul tient partout, le papier se réduit à une note de dimensionnement.

**La mesure qui change la balance** [PROPOSITION]. Le versant honnête de l'essai « jumeau contre jumeau » décide trois des quatre prévisions sans saboteur [FAIT RAPPORTÉ, réponse 9]. Il n'emploie ni mode, ni dommage planté, ni graine d'audit. Sur des tâches disjointes de la famille tenue à l'écart, sa publication ne fausse aucune mesure adverse. Un billet qui le porte plante un résultat, et ses deux issues sont publiables.

### B5. Squelette du billet et phrases porteuses

Titre [PROPOSITION] : « Sabotage diffus : ce que la stéganographie et la comptabilité des matières prédisent déjà, et ce qu'il reste à mesurer chez des agents ».

1. **Citation.** « Le dommage qu'un saboteur étalé peut cacher sous une accumulation de scores suit, pour des pas indépendants et une référence honnête de m pas, une loi connue, de l'ordre de √(n + n²/m) (Ker 2010 ; Avenhaus et Jaech 1981). Nous la prenons comme modèle nul, non comme résultat. »
2. **Citation.** « Cette loi a été transposée au suivi des usages contre l'extraction répartie (2610.13083). L'aveuglement des statistiques de marginales est connu en contrôle (2606.10456, 2607.11751). Le billet de mars 2025 sur le "total des bits" en donnait l'intuition. »
3. **Question.** « Chez de vrais agents, quels termes de ce bilan tiennent, et lesquels s'ajoutent ? »
4. **Protocole.** « Première mesure : des exécutions honnêtes jumelles, sans saboteur, pour savoir où l'alarme honnête quitte son niveau nominal. »
5. **Engagement.** « Nos prévisions et notre plan d'analyse sont engagés par l'empreinte suivante, horodatée par un tiers ; ils seront révélés avec les mesures. »
6. **Bornes.** « Après la recherche décrite, quatre arbres de citations restant à parcourir, nous n'avons pas trouvé ce bilan mesuré contre un agent qui sabote. Nous ne disons pas que personne ne l'a fait. »
7. **Discipline.** « L'audit au hasard avec plancher est publié et nous ne le revendiquons pas. Les sondes orientent l'audit et ne garantissent rien. »
8. **Résultat**, seulement si la mesure honnête est faite : ses constantes, contre la prévision révélée.

Mots à bannir [PROPOSITION] : « premier », « inédit », « zone libre », « jamais », « personne ». S'y ajoutent les douze phrases de la réponse 9 et le § 6 de la note de recherche.

### B6. Tests avant parution

Un agent neuf d'une autre lignée reçoit le billet seul [PROPOSITION] :

- **Fuite du mode.** Il désigne le mode tenu à l'écart dans une liste à leurres. Au-dessus du hasard, le billet fuit.
- **Fuite des prévisions.** Il reconstitue les prévisions chiffrées. S'il y parvient, l'engagement ne cache rien.
- **Priorité.** Il relève les phrases qu'il lit comme des revendications de priorité. Cible : aucune.
- **Feuille de route.** Il écrit le plan qu'il suivrait pour publier avant le programme. La longueur et la justesse de ce plan mesurent ce que le billet donne.

Contrôle positif : une version du billet où le mode est décrit doit être détectée. Sinon le test est insensible et ne vaut rien.

---

## Question neutre pour le collisionneur

« Une équipe prépare une étude empirique dont aucune mesure n'est encore faite. Son domaine avance vite : des travaux voisins paraissent chaque mois, et une part de ses idées de départ s'est révélée déjà publiée ailleurs. L'étude éprouve un dispositif de détection contre un adversaire ; certaines mesures ne valent que si des éléments restent inconnus de certaines personnes ou de certains systèmes. L'équipe se demande s'il faut rendre public un texte court avant ses résultats. Quels contenus un tel texte peut-il porter ? Pour chacun, quel effet a-t-il sur la reconnaissance ultérieure du travail, sur la probabilité qu'un autre groupe publie d'abord, et sur la validité des mesures à venir ? À quelles conditions vaut-il mieux publier avant, publier après, ou ne rien publier ? Quelles vérifications, indépendantes de l'équipe, diraient que le choix était le bon ? Donnez l'argument le plus fort pour chaque option, puis votre choix et ce qui vous en ferait changer. »

---

## Décisions qui reviennent au directeur

**Décision 1 — Choisir le moment et la forme du drapeau.**
- *Enjeu.* Une question publiée seule donne la feuille de route à des voisins qui ont déjà des données d'agents ; attendre le papier laisse le programme sans date opposable.
- *Option a : engagement salé et horodaté par un tiers maintenant ; billet à la sortie du versant honnête de l'essai.* Avantage : une date sans divulgation, puis un résultat sans secret. Inconvénient : le billet dépend d'un essai dont j'ignore la durée.
- *Option b : billet « question et engagement » maintenant (phrases 1 à 7).* Avantage : date publique immédiate, relecture par des spécialistes. Inconvénient : feuille de route donnée, thèse affichée avant toute mesure.
- *Option c : rien avant le papier A.* Avantage : aucune fuite. Inconvénient : aucune date, aucun retour externe.
- *Recommandation.* Option a ; option b si l'essai demande plus de trois semaines. Confiance : 0,6.

**Décision 2 — Publier les prévisions en clair ou par empreinte.**
- *Enjeu.* Les prévisions chiffrées et la comparaison des deux références décrivent l'expérience à qui veut la faire d'abord.
- *Option a : empreinte salée dans le billet, révélation avec les mesures.* Avantage : preuve de date sans plan donné. Inconvénient : billet moins instructif.
- *Option b : préenregistrement public en clair.* Avantage : transparence, critique avant mesure. Inconvénient : plan complet offert.
- *Recommandation.* Option a, scellement avant parution dans les deux cas. Confiance : 0,6.

**Décision 3 — Fixer les conditions préalables à toute parution.**
- *Enjeu.* Trois phrases porteuses reposent sur des vérifications non faites : pages décisives lues une fois, quatre arbres non parcourus, unité de m non fixée.
- *Option a : second lecteur, quatre arbres, unité de m, puis parution ; rien sur le théorème ni sur 2606.10456 au-delà de la citation.* Avantage : aucune phrase à rétracter. Inconvénient : quelques jours.
- *Option b : parution en déclarant ces manques.* Avantage : immédiat. Inconvénient : la phrase 1 peut être fausse dans ses unités.
- *Option c : y ajouter la simulation du contre-exemple, pour écrire la « cécité au premier ordre ».* Avantage : un contenu de plus. Inconvénient : critique publique d'un article sur un énoncé occupé ou trivial.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 4 — Mettre les pièces à jour avant d'écrire.**
- *Enjeu.* La table du 19 novembre revendique encore T et L ; deux phrases du § 5 de la note de recherche précèdent le retrait ; un texte déjà public peut contenir une phrase fautive.
- *Option a : table en version 2, § 5 corrigé, relecture des textes publics, puis billet.* Avantage : le billet part de pièces justes. Inconvénient : une étape de plus.
- *Option b : billet d'abord, pièces ensuite.* Avantage : vitesse. Inconvénient : le rédacteur, humain ou modèle, héritera des phrases retirées.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 5 — Montrer ou non le texte à un spécialiste avant parution.**
- *Enjeu.* La vérification externe est la plus forte, mais elle divulgue.
- *Option a : envoyer la seule table de transport à un spécialiste de stéganalyse.* Avantage : le transport est vérifié, la question et le protocole restent internes. Inconvénient : délai de réponse.
- *Option b : ne rien envoyer ; les commentaires publics tiennent lieu de relecture.* Avantage : aucun délai. Inconvénient : l'erreur de transport se découvre en public.
- *Option c : envoyer le brouillon entier.* Avantage : relecture complète. Inconvénient : feuille de route donnée à un voisin direct.
- *Recommandation.* Option a. Confiance : 0,55.

FIN DE LA RÉPONSE
