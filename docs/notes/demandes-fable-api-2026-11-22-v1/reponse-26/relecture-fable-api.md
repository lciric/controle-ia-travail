# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHp3ytTRDhKy9xvyMoFN`
- Heure (UTC) : 2026-11-22T10:34:23Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 100000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-26-billets-suivants-v1.md` — sha256 1f4e1f09c5da953480152ecfa7286018c1fe6a720f9c327b6228b3a2a8836ab9 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/etat-des-deux-billets-2026-11-21-v1-sans-nom-v2.md` — sha256 977b6527d0f6ce69a4d6dc7d77f9eff45bab29e43695e4eb6d2f1ec11710a8d1 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/critique-etat-des-deux-billets-v1-sans-nom-v2.md` — sha256 e3d4f1f2a63ed5e9ca56fb54ee569d0e880fb00a93fdd60666ffa801214c99b5 (compagnon : vérifié)
  - remarques : `docs/notes/billets-v1/troisieme-billet-v1/propositions-troisieme-billet-fable-v1.md` — sha256 f49b1f832f32c9d77ee023685b73f8bf5134839e31f68c925f8796f6a3b32c58 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-20/relecture-fable-api.md` — sha256 60d9891ad69df75bd76945b4216a210e36876f633a208cc2fc28f9c0bdbf15d5 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 778420fd667378b7cc21ab05535a39642f820089cb39e6b0264650da4682718f
- Jetons : entrée 54215, sortie 21597 (dont réflexion 12027), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.297600 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 26 — billets suivants et révision des deux premiers : réponse approfondie

**Conclusion d'abord.** Je recommande cet ordre, avec une confiance d'ensemble de 0,6 :

1. « Reasons or watching? » en version 7 courte, écrite de la main du directeur d'après une fiche de faits.
2. Un seul billet « loi héritée », qui fusionne le candidat A du 21 novembre et la partie citable du billet « drapeau ».
3. Un premier billet de résultat : le versant honnête de l'essai « jumeau contre jumeau ».
4. Le billet sur les sondes, après un résultat sur saboteur discret ; le renvoi du directeur tient.
5. Le candidat B après l'entretien ; le candidat C en repli.

Les deux billets existants sont à revoir. Leurs versions (14 et 15 novembre) précèdent le gabarit, les décisions N-071 à N-077, les verdicts scellés et le retrait du lemme et du théorème.

**Réserves.**
- Je n'ai lu le corps d'aucun des deux billets. Je ne peux juger « phrase par phrase » que les phrases citées dans les pièces : cinq pour « Reasons or watching? », aucune pour le billet sur les sondes, pour lequel je donne des classes de phrases à chercher.
- Je n'ai lu aucun PDF, aucun registre, aucun verdict. Je n'ai recalculé aucune empreinte.
- Les antériorités que j'ajoute sont citées de mémoire : « rapporté, non vérifié sur PDF ». Je ne confirme aucun identifiant arXiv de 2026. Je ne connais pas « Model Spec Midtraining » hors des pièces.
- Les décisions de la réponse 20 ne sont pas accordées : je la traite comme une proposition.
- « Sans nom de personne » : je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Classer les billets par dépendance** et non par état du texte [PROPOSITION] : résultat à venir, plume du directeur, modération, cloisonnement. Un texte fini qui attend un résultat est moins prêt qu'un texte à écrire qui n'attend rien.
- **Faire un audit de péremption** [PROPOSITION] : confronter chaque phrase d'un brouillon aux décisions prises après sa date.
- **Vérifier toute absence d'effet affirmée** [PROPOSITION]. Le titre de la version 6 dit « not what they do ». Une absence ne se revendique qu'avec une borne d'équivalence déclarée (Lakens, 2017, « Equivalence tests: a practical primer for t tests, correlations, and meta-analyses » ; rapporté, non vérifié sur PDF).
- **Nommer l'explication concurrente du billet sur les sondes** [HYPOTHÈSE] : sur un saboteur instruit, la sonde peut lire l'empreinte de la consigne et non le sabotage. C'est l'objet du barreau « sabotage ou empreinte », en cours [FAIT RAPPORTÉ, état des billets, § 2].
- **Repérer les doublons entre candidats** [HYPOTHÈSE] : le candidat A et le billet « drapeau » portent la même loi (voir B1).
- **Fixer la date de l'entretien** [FAIT RAPPORTÉ] : les pièces disent le 27 novembre et le 1er décembre.
- **Mesurer le délai de modération** en le demandant au site, plutôt que de l'estimer [PROPOSITION].

## 2. Données brutes de départ

- Les deux textes eux-mêmes (999 mots et 3 502 mots), phrase par phrase ; pour le billet sur les sondes, par un lecteur autorisé.
- Le texte entier des décisions N-071 à N-077 et de la thèse du 22 novembre ; les verdicts scellés de l'étape B, de l'étape B bis et de l'expérience 1.
- Les résultats des expériences E3 et E5 de l'autre projet, non confrontés à la version 6 [FAIT RAPPORTÉ, critique, § 3.4].
- La page source de la politique du site, relevée ce jour, et non son résumé.
- Les pages décisives de Ker 2010, d'Avenhaus et Jaech 1981, de l'article 2610.13083 (p. 5, 9, 10) et de Wen et collaborateurs (p. 6).
- L'enregistrement public du projet `ewx4p` : date, état, auteur du geste.
- Les scores pas à pas d'exécutions honnêtes, s'il en existe : je l'ignore.

## 3. Méthodes et outils

- **Table de péremption** : phrase, décision postérieure, verdict (tient, à réécrire, à retirer) ; d'abord par motifs, puis par un lecteur.
- **Vérificateur des nombres** rejoué sur le texte final, et registre des affirmations.
- **Test d'équivalence** à borne écrite avant lecture, pour toute phrase d'absence d'effet.
- **Matrice de fuite** : information, mesure à venir, lecteur.
- **Recherche d'antériorité à critère de mort écrit d'avance**, forum compris.
- **Fiche de faits en français, plume du directeur, traduction mot à mot** : voie permise selon le résumé de la politique [FAIT RAPPORTÉ, propositions du troisième billet].
- **Engagement salé, horodaté par un tiers**, pour les prévisions (Haber et Stornetta, 1991, « How to time-stamp a digital document » ; rapporté, non vérifié sur PDF).
- **Test de devinette** avec contrôle positif (voir C).

## 4. Ce qui vérifie hors du directeur et de Claude

- La modération du site : son refus ou son accord est un verdict externe sur « écrit par un humain ».
- Le rejeu par n'importe qui du paquet public et du script.
- Un spécialiste de stéganalyse, sur la seule table de transport de la loi ; un chercheur du contrôle, sur le billet « loi héritée ».
- Un agent neuf d'une autre lignée : devinette, et dérivation depuis l'énoncé seul.
- La mesure honnête, comparée à la prévision engagée.
- Les commentaires du forum, puis le jury de l'entretien.

---

## (A) Demande reformulée

« Pour chaque billet existant ou candidat, dis de quoi sa parution dépend (résultat à venir, plume du directeur, modération, cloisonnement) et ce qu'il peut affirmer aujourd'hui, preuve citée dans les pièces. Range-les dans un ordre de parution, et écris d'avance ce qui ferait changer cet ordre. Pour les deux billets déjà rédigés, dresse la table de péremption : chaque phrase connue, la décision ou le verdict postérieur qui la touche, son sort ; quand le texte n'est pas lisible par toi, donne les classes de phrases à chercher et qui les cherche. Relève les doublons et les contradictions entre candidats. Liste ce qui ne doit paraître dans aucun billet, avec la mesure à venir que la divulgation fausserait. Donne les tests, indépendants de l'auteur, qui diraient que l'ordre et les textes étaient les bons. »

---

## (B) Réponse

### B1. Un doublon à résoudre avant tout ordre

- Le candidat A (« référence honnête ») donne une part cachée en z·√(1/n + 1/m)/μ. Le billet « drapeau » cite une loi en √(n + n²/m). C'est la même loi, écrite en part et en total [HYPOTHÈSE, algèbre de ma main].
- La réponse 20 rapporte cette loi, plateau compris, comme héritée de Ker 2010 et d'Avenhaus et Jaech 1981 [FAIT RAPPORTÉ]. Titres de mémoire : Ker, 2010, « The square root law in stegosystems with imperfect information » ; Avenhaus et Jaech, 1981, « On subdividing material balances in time and/or space » (rapportés, non vérifiés sur PDF).
- La note du 21 novembre attribue la racine à Ker 2006 et 2007 et présente le plateau comme « Result 1 » [FAIT RAPPORTÉ]. Ce n'est donc pas un résultat : c'est une citation chiffrée [HYPOTHÈSE].
- Le critère de mort du candidat A est à relire contre l'article 2610.13083, qui transpose la loi à des données réelles et écrit qu'il faut « protéger la référence » (p. 10) [FAIT RAPPORTÉ, réponse 20]. Il porte sur le suivi des usages, non sur l'incrimination en contrôle : A n'est pas tué, mais sa probabilité de nouveauté (0,55) est à refaire, à la baisse [HYPOTHÈSE].
- Le « mur de rapport signal sur bruit », marqué non vérifié dans la note : Tandra et Sahai, 2008, « SNR walls for signal detection » (rapporté, non vérifié sur PDF).
- Rappel : une zone non trouvée reste une question. Le billet fusionné ne dit jamais « personne ».

### B2. Ordre et contenu

| Rang | Billet | Dépend de | Fenêtre [HYPOTHÈSE] |
|---|---|---|---|
| 1 | « Reasons or watching? », version 7 courte | Plume du directeur ; compte ; modération | Dès que le directeur a écrit ; pas avant deux jours |
| 2 | « Loi héritée » (A fusionné avec les phrases 1, 2, 6 et 7 du « drapeau ») | Levée du gel ; antériorité ; script contre-lu ; prévision scellée avant parution | Avant l'entretien si la lecture adverse est close ; sinon montré, non posté |
| 3 | Versant honnête de l'essai « jumeau contre jumeau » | La mesure, qui n'existe pas | Après la mesure |
| 4 | Sondes, saboteur instruit puis discret | Résultat discret (pas avant le 27 novembre) ; barreau « sabotage ou empreinte » | Après l'entretien |
| 5 | Candidat B (« tirer au sort n'est pas reconnaître ») | Huit voisins lus en entier ; cloisonnement | Après l'entretien |

**Raisons de l'ordre.**
- Le rang 1 ne touche aucune mesure du programme, son paquet est déjà public [FAIT RAPPORTÉ, critique, § 2.1], et il fait que le compte n'est plus neuf pour la suite [HYPOTHÈSE].
- Le rang 2 ne publie que de la littérature et des nombres sous supposition. Il ne donne ni la question mesurée, ni le protocole, ni la complémentarité : la feuille de route reste interne [PROPOSITION]. La prévision de N-076 est scellée avant, sinon les commentaires la déplacent.
- Le rang 3 est la première mesure demandée par les collisionneurs, et quatre modèles sur cinq veulent d'abord le taux de fausses alertes sur des agents honnêtes [FAIT RAPPORTÉ, contexte]. Ses deux issues sont publiables [FAIT RAPPORTÉ, réponse 20].
- Le rang 4 attend : le gabarit demande une explication concurrente contrôlée, et le contrôle (empreinte de la consigne) est en cours [HYPOTHÈSE].

**Ce qui est revendicable aujourd'hui.**

| Billet | Revendicable, et preuve | Non revendicable |
|---|---|---|
| « Reasons or watching? » | Les nombres recalculables depuis le paquet public ; « le test sur les adaptateurs n'a pas tourné » [FAIT RAPPORTÉ] | Toute lecture de l'expérience 1 (verdict « non lisible ») ; un embargo |
| « Loi héritée » | Nombres sous supposition (script rejoué deux fois, non contre-lu) ; citations relues à la page par l'auteur de la note [FAIT RAPPORTÉ] | Le plateau comme résultat ; toute mesure ; toute nouveauté avant recherche |
| Jumeau honnête | Rien : aucune mesure | Tout |
| Sondes | Je ne peux pas le dire : verdicts scellés non lus | Toute phrase sur un saboteur discret : le résultat n'existe pas [FAIT RAPPORTÉ] |
| Audit secret et estimateur de Horvitz-Thompson | Rien à revendiquer (N-076) | Voir antériorités ci-dessous |

Antériorités de l'audit, de mémoire (rapportées, non vérifiées sur PDF) :
- Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe ».
- Särndal, Swensson et Wretman, 1992, « Model Assisted Survey Sampling », pour le moniteur en variable de contrôle.
- Angelopoulos, Bates, Fannjiang, Jordan et Zrnic, 2023, « Prediction-powered inference », même idée avec un prédicteur appris.
- Greenblatt, Shlegeris, Sachan et Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion », pour l'audit aléatoire en contrôle.

### B3. Révision du premier billet sur le contrôle (sondes)

**Faut-il le revoir ? Oui.** La version 2 date du 14 novembre ; le gabarit, du 18 ; les verdicts scellés, des 17 et 19 ; N-075 à N-077 et le retrait du 22 sont postérieurs [FAIT RAPPORTÉ]. Je n'ai pas le texte. Voici les classes de phrases qu'un lecteur autorisé cherche, et leur sort [PROPOSITION] :

| Classe de phrase | Décision qui la touche | Sort |
|---|---|---|
| La sonde « détecte » ou « attrape » le sabotage, sans condition | N-075 : accélérateur, non garantie | Réécrire : « oriente l'audit » |
| Un score accumulé sur les pas, ou un rappel qui croît avec l'horizon | N-076 | Ajouter m, n et la source de validité, ou retirer |
| Une marge gardée par une intervention | N-077 | Retirer ; mesure descriptive seule |
| Le lemme ou le théorème comme résultat | Thèse du 22 novembre | Retirer, ou une mention « retiré » |
| Un chiffre de travaux voisins | Règle de provenance | PDF, page, unité. « 98,8 % » chez Hollinsworth et collaborateurs est une aire sous la courbe [FAIT RAPPORTÉ] |
| Un mot de primauté, une phrase de feuille de route | Lecture adverse du 13 novembre | Retirer |
| Le bras « transfert vers un mode tenu à l'écart » | N-054 | Rien avant le mot du directeur (décision 5) |
| Une conclusion qui déborde le saboteur instruit | Résultat discret absent | Borner au titre : « instructed » |
| Le témoin de l'attaque publiée par Bailey et collaborateurs | Recommandation au registre | Une phrase, sans chiffre |

Trois ajouts [PROPOSITION] :
- Le résumé dit, dans les 250 premiers mots, que rien n'est établi pour un saboteur discret, et nomme l'explication par l'empreinte de la consigne.
- Les sections de l'étape B et de l'étape B bis sont écrites par un lecteur autorisé, depuis les seuls verdicts scellés, puis relues pour le cloisonnement.
- La page publique de P3 reçoit ses réserves avant tout lien ; sa mise à jour n'est pas retrouvée au registre [FAIT RAPPORTÉ].

Antériorités que le billet doit citer si ce n'est fait (rapportées, non vérifiées sur PDF) : Goldowsky-Dill, Chughtai, Heimersheim et Hobbhahn, 2025, « Detecting strategic deception using linear probes » ; Bailey et collaborateurs, 2024, « Obfuscated activations bypass LLM latent-space defenses ».

### B4. Révision de « Reasons or watching? »

Phrases connues par les pièces :

| Phrase de la version 6 | Constat | Sort proposé |
|---|---|---|
| « I wrote this post myself » | Vraie seulement si le directeur écrit depuis des faits ; une reformulation phrase à phrase d'un texte de modèle ne suffit pas [FAIT RAPPORTÉ, critique, § 3.1] | Garder si la condition est remplie ; sinon retirer |
| « The test on the MSM adapters themselves has not run » | Encore vraie au 21 novembre, contrôle partiel [FAIT RAPPORTÉ] | Garder ; revérifier le jour de la parution |
| Toute phrase « sous embargo » | Serait fausse : embargos levés le 13 novembre [FAIT RAPPORTÉ] | Ne pas ajouter ; confirmation d'une ligne du directeur |
| Titre : « … moves what models say, not what they do » | Affirme une absence d'effet. J'ignore si une borne d'équivalence l'appuie [HYPOTHÈSE] | Si aucune borne : « … and we detect no change in what they do », avec l'intervalle |
| Section « What comes next » | L'expérience 1 est lue, verdict « non lisible (jumelles non reconnues) » [FAIT RAPPORTÉ]. Toute phrase qui l'annonce comme à venir ne tient plus [HYPOTHÈSE, section non lue] | Une phrase de fait, sans chiffre ; aucune date pour la conception 2 bis |

Autres points :
- **Longueur** [PROPOSITION] : 3 502 mots à écrire de sa main, c'est une demi-journée à une journée selon la critique. Une version de 1 300 à 1 500 mots selon le gabarit est plus sûre pour un premier billet.
- **Pièces à corriger** [FAIT RAPPORTÉ] : le fichier d'état du paquet dit encore « privé » ; l'auteur du geste d'ouverture est inconnu. À consigner.
- **Contrôle restant** [FAIT RAPPORTÉ] : E3 et E5 contre le texte.
- **Antériorités de l'écart entre dire et faire**, à citer si ce n'est fait (rapportées, non vérifiées sur PDF) : Turpin, Michael, Perez et Bowman, 2023, « Language models don't always say what they think » ; Greenblatt et collaborateurs, 2024, « Alignment faking in large language models ». Je ne sais pas si le billet les cite : c'est une question.

### B5. Ce qui ne doit pas paraître

| Élément | Mesure faussée ou phrase à rétracter |
|---|---|
| Nature du mode et de la famille tenus à l'écart ; mécanismes des saboteurs ; consignes de sabotage en toutes lettres | Porte G1 par mode (N-054) ; reconception (N-062) |
| Procédés de la course « nouvelles attaques » | Quarantaine, revue externe avant toute sortie [FAIT RAPPORTÉ] |
| Poids, couches et seuils des sondes ; graines d'audit ; dommages plantés ; grille de l'oracle | Taux de détection par dommages plantés (N-075) [HYPOTHÈSE] |
| Prévisions chiffrées en clair avant scellement | Prévision de N-076 |
| La sortie « par le jumeau » au-delà du principe ; la proposition « part sue du dommage » avant l'entretien | Pari apparié ; statut « proposée, pas décidée » [FAIT RAPPORTÉ] |
| Un chiffre de l'étape B ou B bis écrit par une session exposée | Cloisonnement des lecteurs |
| « Antécédent défectueux » pour l'article 2606.10456 ; le plateau comme « résultat » ; « premier », « inédit », « personne » | Phrases à rétracter [FAIT RAPPORTÉ, réponse 20, pour la première] |
| « 98,8 % » sans unité ; « sous embargo » | Fausses telles quelles |

Tout texte déjà public du programme est à relire contre cette liste avant un nouveau lien [PROPOSITION].

---

## (C) Question neutre pour le collisionneur

« Un auteur qui n'a encore rien publié sur un forum scientifique modéré dispose de quatre textes courts. Le premier est le compte rendu d'une expérience dont une moitié est faite et dont l'autre, la plus attendue, n'a pas encore de résultat. Le deuxième est une note de calcul qui applique à son domaine une loi connue d'un autre domaine, sans aucune mesure. Le troisième est la note d'étape d'une étude terminée, aux données publiques, dont une expérience de suite s'est révélée illisible. Le quatrième est un protocole dont la première mesure n'est pas faite. Certaines mesures à venir ne valent que si des éléments restent inconnus de tiers. Une évaluation de son travail a lieu dans dix jours. Dans quel ordre publier, et selon quels critères ? Un brouillon écrit avant des décisions internes qui en changent la lecture doit-il être corrigé à la marge, réécrit ou abandonné ? Qu'est-ce qui ne doit figurer dans aucun texte ? Donnez l'argument le plus fort pour trois ordres différents, puis votre choix, ce qui vous en ferait changer, et les vérifications indépendantes de l'auteur qui diraient après coup que l'ordre était le bon. »

**Test de devinette** [PROPOSITION]. Un agent neuf d'une autre lignée reçoit la question seule. Il doit échouer à nommer le domaine, le dispositif éprouvé et l'ordre que je recommande ; la liste des quatre textes est d'ailleurs dans un autre ordre que le mien. Contrôle positif : une version qui nomme les sondes et le sabotage doit être devinée, sinon le test est insensible.

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer l'ordre des parutions.**
- *Enjeu.* Une pièce publique avant l'entretien, sans rien donner des mesures à venir.
- *Option a : l'ordre du tableau B2.* Avantage : aucun billet n'attend un résultat avant le rang 3. Inconvénient : deux textes à écrire de sa main en dix jours.
- *Option b : « Reasons or watching? » seul avant l'entretien.* Avantage : aucune dispersion. Inconvénient : rien de public sur le programme.
- *Option c : lever le renvoi et sortir d'abord la version « saboteur instruit ».* Avantage : le texte existe en partie. Inconvénient : explication concurrente non contrôlée ; un résultat discret contraire la ferait relire comme excessive.
- *Recommandation.* Option a ; option b si la plume manque. Confiance : 0,6.

**Décision 2 — Choisir la version de « Reasons or watching? ».**
- *Enjeu.* La version 6 ignore le verdict de l'expérience 1 ; la conception 2 bis est loin.
- *Option a : version 7 courte, une phrase sur l'expérience 1, titre borné si aucune équivalence n'est établie.* Avantage : rien à rétracter. Inconvénient : deux à quatre heures de session, puis la plume.
- *Option b : version 6 telle quelle.* Avantage : immédiat. Inconvénient : « What comes next » peut être périmée.
- *Option c : attendre la conception 2 bis.* Avantage : un instrument validé. Inconvénient : aucune date.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 3 — Garder ou lever le renvoi du billet sur les sondes.**
- *Enjeu.* Le billet n'a ni résultat discret ni contrôle de l'empreinte.
- *Option a : garder le renvoi ; faire maintenant la table de péremption et les sections B et B bis.* Avantage : le texte sera prêt quand le résultat viendra. Inconvénient : une version 14 de la liste des lecteurs.
- *Option b : lever le renvoi.* Avantage : un billet du programme plus tôt. Inconvénient : celui de l'option c de la décision 1.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 4 — Fusionner le candidat A et le billet « drapeau ».**
- *Enjeu.* Deux billets sur la même loi héritée ; l'un l'appelle « résultat ».
- *Option a : un seul billet, loi citée, nombres sous supposition ; question et protocole gardés pour le billet de résultat ; prévision engagée avant.* Avantage : aucune feuille de route donnée, crédit rendu. Inconvénient : peut être jugé élémentaire.
- *Option b : deux billets distincts.* Avantage : une date publique sur la question. Inconvénient : redite ; feuille de route donnée.
- *Option c : aucun avant la mesure honnête.* Avantage : un résultat d'emblée. Inconvénient : rien avant l'entretien.
- *Recommandation.* Option a, après relecture du critère de mort contre l'article 2610.13083. Confiance : 0,6.

**Décision 5 — Dire ce qui compte comme « publication » et ce qui se dit du mode tenu à l'écart.**
- *Enjeu.* Deux accords se croisent sur la revue externe ; l'étape B bis a un bras de transfert vers ce mode.
- *Option a : un billet compte comme publication ; rien sur le bras avant la porte G1.* Avantage : aucune mesure faussée. Inconvénient : section B bis amputée.
- *Option b : une phrase d'existence, sans nature ni chiffre.* Avantage : le lecteur sait qu'un mode est réservé. Inconvénient : relecture de cloisonnement en plus.
- *Recommandation.* Option b pour l'existence, option a pour le reste. Confiance : 0,65.

**Décision 6 — Lancer le versant honnête de l'essai « jumeau contre jumeau » comme matière du premier billet de résultat.**
- *Enjeu.* C'est la seule mesure sans secret qui change un billet de question en résultat.
- *Option a : le lancer maintenant, sur des tâches disjointes de la famille tenue à l'écart, prévision scellée avant.* Avantage : deux issues publiables. Inconvénient : j'ignore sa durée et son coût.
- *Option b : après l'entretien.* Avantage : aucune charge avant le 1er décembre. Inconvénient : le rang 3 recule.
- *Recommandation.* Option a si des exécutions honnêtes existent déjà ; sinon option b. Confiance : 0,55.

FIN DE LA RÉPONSE
