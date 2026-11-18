# Extrait pour les codeurs — Grille des gestes de rédaction et classes d'objections des billets de résultats — v1

Extrait produit par programme (`extraire_grille_codeurs_v1.py`) depuis `grille-gestes-v1.md` (sha256 14cf4de9429bcc08dbe88a4f76f61badbadc1b3ff234163d21f5f573f6dbf6f0).

## 1. Conventions communes


- **Unité** : le billet entier, dans sa copie neutre (section 4), titre compris pour la question du titre seulement.
- **Corps** : le texte sous le titre. **Avant-propos** : ce qui précède la première phrase de contenu — listes d'auteurs, remerciements, liens vers l'article ou les fils de discussion, notes d'édition, statut épistémique. **Premier paragraphe** : le premier bloc de texte du corps hors avant-propos, jusqu'à la première ligne vide ou au premier intertitre ; une liste entière est un bloc ; une légende d'image n'est pas un paragraphe.
- **En tête** : avant la borne `⟦FIN DE L'EN-TÊTE — 250 MOTS⟧`, insérée par le script après le 250e mot réel du corps (marqueurs `[IMAGE …]`, `[lien : …]`, `[AUTEUR]`, `[ÉLÉMENT INTERACTIF]` et jetons de pure mise en forme exclus du compte). **L'avant-propos compte dans les 250 mots** : la borne mesure ce que le lecteur voit d'abord. **Un énoncé, une liste, un bloc ou une figure est en tête si son début est avant la borne**, même s'il se termine après.
- **Où chercher** : le billet entier, notes de bas de page et annexes comprises, sauf pour les questions d'en-tête. Un renvoi à l'article ne remplace jamais le texte du billet.
- **Résultat principal** : ce que les auteurs disent avoir trouvé et mettent en avant (résumé, titre, conclusion). Une question, un plan, une méthode annoncée ne sont pas un résultat ; l'annonce d'une réussite (« we solved the challenge ») en est un.
- **Des auteurs** : fait ou écrit par les auteurs du billet ; ce qu'ils rapportent d'autrui ne compte pas, ni le texte d'un modèle cité (transcriptions, sorties de modèle entre guillemets ou en bloc).
- **Images** : le codeur ne voit pas les images, seulement leur texte de remplacement et la légende qui suit. Une décision qui dépend d'une image se prend sur ce texte seul. En développement, 53 images sur 712 ont un texte de remplacement.
- **Doute** : chaque ligne de codage porte un champ `doute` (oui / non). Le doute n'autorise pas de modalité nouvelle ; on choisit la modalité la plus proche selon la règle, et on coche le doute.
- **Appui** : pour toute modalité **sauf** `aucun`, `aucune`, `absent`, `absente`, `absentes`, `non-dit`, `non`, `aucun-article`, `plus-loin`, `moins-de-trois`, `positif`, `sans-résultat`, le codeur copie une citation d'appui tirée de la copie neutre : un ou deux fragments, séparés par ` […] `, de 25 mots au plus chacun, copiés tels quels. Pour les modalités d'en-tête (liste en 4.5), l'appui commence avant la borne. Pour les modalités exceptées, l'appui est permis, non exigé. Tout appui donné est contrôlé par programme au dépôt ; le contrôle exige l'appui pour une partie des modalités non exceptées.
- **Format des exemples** : identifiant du billet, puis citation de 25 mots au plus, en anglais, telle qu'elle figure dans le texte (mise en forme et adresses de liens ôtées). Pour un titre : `(titre)`. Pour un commentaire : `billet/commentaire`.

## A. Gestes de rédaction (25 questions)


### G01. Forme du titre
- **Question** : que dit le titre du résultat ?
- **Modalités** : `affirmation` ; `affirmation-atténuée` ; `question` ; `sans-résultat`
- **Règle** : coder le titre seul. `affirmation` : le titre énonce un résultat sans atténuation, positif ou négatif. `affirmation-atténuée` : le résultat est énoncé avec may, might, could, appears, seems, towards, initial. `question` : le titre est une question directe, avec point d'interrogation. `sans-résultat` : nom de méthode, d'objet, de tâche ou formule, sans résultat énoncé.
- **Cas limites** : titre en deux segments (deux-points, tiret) → coder le segment qui porte un résultat s'il y en a un ; question dans un segment et affirmation dans l'autre → `affirmation` ; titre négatif (« isn't strong ») → `affirmation` ; « (Yet) » n'atténue pas ; **gérondif ou groupe nominal d'action (« Solving … », « Steering … ») → `sans-résultat`, même si le verbe suggère une réussite** ; **interrogative indirecte sans point d'interrogation (« How X works ») → `sans-résultat`**.
- **Exemple** (`affirmation`) : `nmxzr2zsjNtjaHh7x` (titre) — « Actually, Othello-GPT Has A Linear Emergent World Representation »
- **Exemple** (`affirmation-atténuée`) : `69fachkoAs2ZHeSst` (titre) — « J-space auditing might be unreliable »
- **Exemple** (`question`) : `xwdRzJxyqFqgXTWbH` (titre) — « How Does A Blind Model See The Earth? »
- **Contre-exemple** (`sans-résultat`, gérondif, bien que le billet ait un résultat net) : `v7f8ayBxLhmMFRzpa` (titre) — « Steering Llama-2 with contrastive activation additions »

### G02. Place de la thèse
- **Question** : où apparaît pour la première fois l'énoncé du résultat principal ?
- **Modalités** : `premier-paragraphe` ; `en-tête` ; `plus-loin`
- **Règle** : `premier-paragraphe` (au sens de la section 1, avant-propos exclu) ; `en-tête` : ailleurs avant la borne ; `plus-loin` : après la borne, ou jamais.
- **Cas limites** : une question d'accroche n'est pas une thèse ; un plan (« in this post we will ») n'est pas une thèse ; une liste de résultats en tête compte ; un résumé d'article copié compte s'il énonce le résultat ; l'annonce d'une réussite sans son contenu compte (section 1) ; le résultat d'autrui que le billet reprend (« the paper claims ») ne compte pas. **Après l'essai pilote** : une phrase qui présente le billet ou l'article (« this post is… », « in this paper we… ») fait partie de l'avant-propos, même si elle précède immédiatement un bloc « Summary » ou « Abstract » ; le premier paragraphe est alors le premier paragraphe de ce bloc ; une annonce de résultats sans leur contenu (« we find a number of surprising results, described below ») n'est pas un énoncé du résultat ; une annonce de réussite compte seulement si elle nomme ce qui a réussi (« we solved the first challenge »).
- **Exemple** (`premier-paragraphe`) : `69fachkoAs2ZHeSst` — « Across these preliminary experiments, decoded J-space did not seem particularly informative about reward-hacking behaviour. »
- **Exemple** (`en-tête`, après un paragraphe d'image) : `3PaLrzxagpbnNtPLT` — « In a new paper, we present evidence that a similar distinction has emerged in modern language models like Claude. »
- **Exemple** (`plus-loin` : conclusion d'un billet dont l'en-tête reprend la thèse d'un article d'autrui) : `qpwsdu7qBaHTaujE3` — « Through the lens of the Mess3 process, we have seen that transformers are capable of internalizing complex, structured belief states »
- **Contre-exemple** (accroche, pas thèse) : `zsr4rWRASxwmgXfmq` — « Claude can speak dozens of languages. What language, if any, is it using "in its head"? »

### G03. Polarité du résultat principal
- **Question** : le résultat principal est-il positif, négatif ou mixte ?
- **Modalités** : `positif` ; `négatif-ou-nul` ; `mixte`
- **Règle** : `négatif-ou-nul` : le résultat principal est un échec d'une méthode, une réfutation, une absence d'effet, une réplication ratée. `mixte` : les auteurs mettent en avant à égalité un oui et un non (« possibly, but not reliably »). Sinon `positif`.
- **Cas limites** : un résultat nul secondaire dans un billet positif ne change pas la polarité (voir G18) ; montrer qu'une méthode d'autrui échoue est `négatif-ou-nul` même si le ton est triomphant ; une méthode nouvelle qui bat une autre est `positif`. **Après l'essai pilote** : un billet dont le résultat principal est un défaut trouvé dans une méthode ou un résultat d'autrui (« finds systematic defects ») → `négatif-ou-nul`, même si la mesure des auteurs « réussit » ; un billet qui reproduit un effet et dont les auteurs mettent en avant, à égalité avec lui, qu'il exige des contrôles ou s'accompagne d'une dégradation → `mixte` ; si cette réserve est secondaire → `positif`.
- **Exemple** (`négatif-ou-nul`) : `wtfvbsYjNHYYBmT3k` — « At this point, we think it is unlikely to be directly helpful for implementations of alignment strategies (>95%). »
- **Exemple** (`mixte`) : `QQQAcKuWK6k98FivY` — « For open-weight NLAs, the answer seems to be: "possibly, but definitely not reliably". »
- **Contre-exemple** (nul secondaire dans un billet `positif`) : `JdHhtE73AwTBH8LKf` — « Experiment 4: Attention Patterns (Null result) »

### G04. Résumé dans les 250 premiers mots
- **Question** : y a-t-il, en tête, un bloc qui résume les résultats ?
- **Modalités** : `aucun` ; `bloc-étiqueté` ; `liste-non-étiquetée`
- **Règle** : `bloc-étiqueté` (prime) : bloc dont l'étiquette commence en tête (TL;DR, TLDR, Summary, Executive summary, Abstract, Overview, Key results, High-level takeaways, One-sentence summary, Bottom line) et qui énonce au moins un résultat. `liste-non-étiquetée` : liste numérotée ou à puces de résultats sans étiquette. Sinon `aucun`.
- **Cas limites** : un résumé d'article copié sous « Abstract » est `bloc-étiqueté` ; une étiquette suivie d'une simple motivation sans résultat → `aucun` ; un plan du billet n'est pas un résumé ; **un paragraphe de résumé sans étiquette ni liste → `aucun`** (la thèse relève de G02) ; une étiquette qui commence après la borne → `aucun`. **Après l'essai pilote** : une énumération dans le corps d'un paragraphe (« we study 1) …, and 2) … ») n'est pas une liste : il faut des éléments à la ligne, numérotés ou à puces ; un bloc étiqueté qui commence en tête reste `bloc-étiqueté` même s'il suit une phrase de cadrage.
- **Exemple** (`bloc-étiqueté`) : `LQBFqyXA5to4iHEBC` — « This is an informal progress update with some preliminary results using Sparse Autoencoders (SAEs) to detect AI-generated text. Summary »
- **Exemple** (`liste-non-étiquetée`) : `bWxNPMy5MhPnQTzKz` — « In this post, I present experimental results which highlight the strengths and weaknesses of CCS. 1. CCS is able to find a single linear probe »
- **Contre-exemple** (plan, pas résumé) : `d9FJHawgkiMSPjagR` — « In this post: We summarize the paper; We compare our methodology to the methodology of other safety papers. »

### G05. Chiffre de résultat en tête
- **Question** : un nombre de résultat des auteurs figure-t-il en tête ?
- **Modalités** : `avec-comparaison` ; `seul` ; `aucun`
- **Règle** : nombre produit par l'expérience des auteurs (taux, score, effet, compte). `avec-comparaison` (prime) : il est mis en regard d'un autre nombre (base, avant / après, autre méthode) dans la même phrase ou la suivante, ou il est lui-même un rapport (« 4x », « doubles »). `seul` : sinon.
- **Cas limites** : taille de modèle, de jeu de données, nombre de tâches, date → contexte, pas résultat ; une probabilité subjective des auteurs (crédence) n'est pas un résultat (voir G06) ; un nombre d'une légende compte.
- **Exemple** (`avec-comparaison`) : `yHmJrDSJpFaNTZ9Tr` — « we train small EM models which are misaligned 40% of the time, and coherent 99% of the time, compared to 6% and 69% prior. »
- **Exemple** (`avec-comparaison`, rapport) : `S9xyqRAziRMCcJQmz` — « Within-family activations are much stronger (4~9x) »
- **Exemple** (`seul`) : `T64JQFZ5NwSzx4mJu` — « A fair amount of these LoRAs (25%) correspond to linear, interpretable vectors that can be extracted using mean activation differences. »
- **Contre-exemple** (nombre de contexte donné par autrui) : `sTe78dNJDGywu9Dz6` — « the test set accuracy is 95.58% »

### G06. Statut épistémique déclaré
- **Question** : le billet déclare-t-il sa confiance sous une forme explicite ?
- **Modalités** : `absent` ; `statut-étiqueté` ; `crédences-chiffrées`
- **Règle** : `crédences-chiffrées` (prime) dès qu'une probabilité est attachée à une affirmation des auteurs ; `statut-étiqueté` si l'une de ces étiquettes, et elle seule, figure n'importe où et qualifie le billet ou le travail entier : « Epistemic status », « Epistemic state », « Epistemic note », « Epistemic effort », « Confidence level » ; sinon `absent`. Une réserve libre sans étiquette relève de G07.
- **Cas limites** : « confidence » dans un résultat de modèle (score de confiance) ne compte pas ; **une mention locale qui qualifie un seul passage (« Interpretation (speculative): ») ne compte pas**.
- **Exemple** (`statut-étiqueté`) : `M5vEjix8oPeWXeGFY` — « Epistemic Status: Confident only in these particular results. »
- **Exemple** (`crédences-chiffrées`) : `wtfvbsYjNHYYBmT3k` — « Credences are based on a poll of Seb, Vikrant, Zac, Johannes, Rohin »
- **Contre-exemple** (mention locale) : `bWxNPMy5MhPnQTzKz` — « Interpretation (speculative): »
- **Contre-exemple** (réserve sans étiquette, codée en G07) : `HLJoJYi52mxgomujc` — « This post is best viewed as an informal report on preliminary results done over a couple days, rather than a very polished analysis. »

### G07. Caractère préliminaire annoncé
- **Question** : le billet dit-il que l'ensemble du travail est préliminaire, rapide ou inachevé ?
- **Modalités** : `annoncé` ; `non-dit`
- **Règle** : `annoncé` si une phrase des auteurs qualifie le billet ou le travail entier de préliminaire, intermédiaire, rapide, en cours, non poli, fait en quelques jours.
- **Cas limites** : « preliminary » qui qualifie une méthode ou une seule section → `non-dit` ; le cadre seul (programme, hackathon, laboratoire, candidature) ne dit rien de la maturité (voir G09) **sauf si le billet lie lui-même ce cadre à la hâte** (« done in two days at a hackathon, so … ») ; **un aveu d'inexpérience de l'auteur → `non-dit`** ; **une étape de validation non faite (« we haven't yet verified ») → limite (G17), `non-dit` ici** ; « work in progress » dans une note de mise à jour compte. **Après l'essai pilote** : le titre ne compte pas (section 1) ; « progress report », « progress update », « interim report » dans le corps, qualifiant le billet → `annoncé` ; une seule partie annoncée comme en attente (« results are still pending ») → `non-dit` ici (limite, G17).
- **Exemple** : `z6QQJbtpkEAX3Aojj` — « This post is not intended to be a polished research product. »
- **Contre-exemple** (préliminaire qualifie une méthode) : `mkbGjzxD8d8XqKHzA` — « our approach also provides a preliminary way to edit the knowledge of the network. »
- **Contre-exemple** (hackathon sans lien à la hâte) : `sTe78dNJDGywu9Dz6` — « We spent the last Alignment Jam hackathon attempting to solve the two challenges presented there »
- **Contre-exemple** (validation non faite : limite) : `rbqJoxFZtae9x93mx` — « We haven't yet verified how well these improvements transfer to LLM SAEs »

### G08. Rapport à un article des auteurs
- **Question** : le billet est-il lié à un article (papier, prépublication, mémoire) des mêmes auteurs ?
- **Modalités** : `aucun-article` ; `présente-l-article` ; `complète-l-article`
- **Règle** : `présente-l-article` : le billet annonce, résume ou copie un article des auteurs. `complète-l-article` : il rapporte surtout ce que l'article ne contient pas (expériences de suite, ablations, réévaluation) et se présente comme sa suite. Sinon `aucun-article`.
- **Cas limites** : un article d'autrui discuté ou rejoué → `aucun-article` ; un mémoire de master ou de stage des auteurs compte comme article ; l'article publié après le billet et signalé par une note d'édition → `aucun-article` ici (G22) ; **un article antérieur des auteurs employé comme outil ou point de départ → `aucun-article`, sauf si le billet se présente comme sa suite**.
- **Exemple** (`présente-l-article`) : `khFC2a4pLPvGtXAGG` — « This post is a copy of the introduction of this paper on lie detection in LLMs. »
- **Exemple** (`complète-l-article`) : `qGRk7uF92Gcmq2oeK` — « We ran some follow-up experiments that we added to the paper in two new appendices B.5 and B.6. »
- **Contre-exemple** (article d'autrui) : `bWxNPMy5MhPnQTzKz` — « Discovering Latent Knowledge in Language Models Without Supervision describes Contrast-Consistent Search (CCS) »
- **Contre-exemple** (article antérieur employé comme outil) : `rbqJoxFZtae9x93mx` — « In the paper, we found that the best SAE architecture we tested »

### G09. Contexte de production nommé
- **Question** : le billet nomme-t-il le cadre dans lequel le travail a été fait ?
- **Modalités** : `aucun` ; `programme-de-formation` ; `organisation`
- **Règle** : `programme-de-formation` (prime) : programme d'encadrement, bourse de recherche à cohorte, camp, hackathon, cursus (MATS, SPAR, AI Safety Camp, Astra, master), **candidature à un tel programme comprise** ; `organisation` : laboratoire, entreprise, université, institut nommé comme lieu du travail ; sinon `aucun`.
- **Cas limites** : un financement seul ne compte pas ; des remerciements à des personnes d'une organisation ne comptent pas ; une adresse électronique est masquée dans la copie neutre ; **les noms affichés des auteurs sont masqués quand ils sont écrits tels quels ou par une de leurs parties ; les autres formes (nom réel d'un auteur à pseudonyme, signature de section) et les affiliations restent**.
- **Exemple** (`programme-de-formation`) : `47CYFbrSyiJE2X5ot` — « Produced as part of the ML Alignment & Theory Scholars Program »
- **Exemple** (`programme-de-formation`, candidature) : `69fachkoAs2ZHeSst` — « This was originally produced as part of application to Neel Nanda's MATS research stream »
- **Exemple** (`organisation`) : `HhF5kESdtPHku7kim` — « Produced as part of the UK AISI Model Transparency Team. »
- **Contre-exemple** (financement seul) : `BuRt2igbFx9KaB5QG` — « was also supported by a grant from the Future Fund regranting program while working on this project. »

### G10. Enjeu de sûreté explicite
- **Question** : où le billet dit-il pour la première fois pourquoi le résultat compte pour la sûreté ?
- **Modalités** : `en-tête` ; `plus-loin` ; `absent`
- **Règle** : il faut une phrase des auteurs qui relie le résultat ou la question étudiée à la sûreté **et** qui contient un mot de cette liste fermée (ou de sa famille) : safety, safe, risk, danger, harm, catastroph-, x-risk, misalign-, alignment, oversight, monitor-, audit-, control (au sens du contrôle des modèles), deceptive / deception, scheming, sabotage, trust. Début de la phrase avant la borne → `en-tête`.
- **Cas limites** : « intéressant », « mystère », « progrès de l'interprétabilité » sans mot de la liste → ne compte pas ; **une liste de comportements étudiés (complaisance, recherche de pouvoir) sans phrase de lien ne suffit pas** ; **un usage de sûreté sans mot de la liste (« stepping stone towards recovering superhuman beliefs ») ne compte pas** ; une étiquette de sujet ne compte pas ; mot de la liste au sens technique sans lien au risque (« alignment of vectors ») ne compte pas. **Après l'essai pilote** : un mot de la liste qui qualifie le comportement étudié sans le relier à un risque pour la sûreté des systèmes (« two biases that seem particularly harmful ») ne compte pas : la phrase doit relier le résultat ou la question étudiée à la sûreté, à la surveillance, à l'audit ou au contrôle des systèmes.
- **Exemple** (`en-tête`) : `SieLowPgNgRSPGhFw` — « If models can do extensive reasoning without outputting any CoT, it would have implications for safety. »
- **Contre-exemple** (intérêt sans risque) : `N6WM6hs7RQMKDhYjB` — « in my opinion is one of the most fascinating mysteries in deep learning. »
- **Contre-exemple** (usage de sûreté sans mot de la liste) : `bWxNPMy5MhPnQTzKz` — « It might be a stepping stone towards recovering superhuman beliefs of AI systems »

### G11. Figure légendée de résultat en tête
- **Question** : en tête, y a-t-il une figure, et laquelle, à en juger par sa légende ?
- **Modalités** : `figure-de-résultat` ; `autre-figure` ; `aucune`
- **Règle** : décider sur le texte de remplacement et la légende : `figure-de-résultat` (prime) si la légende ou la phrase voisine décrit des données des auteurs (courbe, score, effet, tableau de résultats) ; `autre-figure` : schéma, illustration, mème, capture sans donnée, ou légende muette ; `aucune` sinon. Un tableau compte comme figure. Le nombre total d'images et de tableaux est mesuré par programme, non codé. Ce geste mesure une **figure légendée** : une figure de résultat sans légende est invisible au codeur.
- **Cas limites** : image sans légende → `autre-figure` ; figure de résultat d'autrui → `autre-figure` ; une figure de résultat et une autre figure en tête → `figure-de-résultat`. **Après l'essai pilote** : une capture d'une invite et de la réponse d'un modèle → `autre-figure`, même si elle illustre le résultat ; une courbe ou un tableau qui compare les données des auteurs à celles d'autrui → `figure-de-résultat`.
- **Exemple** (`figure-de-résultat`) : `v7f8ayBxLhmMFRzpa` — « The effects of subtracting or adding a "sycophancy vector" to one bias term. »
- **Contre-exemple** (`autre-figure`) : `khFC2a4pLPvGtXAGG` — « Our lie dectector in meme form. »

### G12. Base externe de comparaison du résultat principal
- **Question** : à quoi le résultat principal est-il comparé, chiffre à l'appui ?
- **Modalités** : `aucune` ; `référence-interne` ; `base-externe`
- **Règle** : `base-externe` (prime) : méthode concurrente, base naïve nommée qui est une vraie autre méthode (classifieur simple, protocole publié), résultat antérieur rejoué ou cité chiffré. `référence-interne` : seulement hasard, réponse constante, ablation, condition de contrôle, plafond ou supervision complète. `aucune` sinon.
- **Cas limites** : le mot « baseline » qui nomme une architecture ou un point de départ sans comparaison chiffrée ne suffit pas ; une comparaison visible seulement dans une image sans légende chiffrée ne compte pas ; une comparaison entre modèles étudiés n'est une base que si l'un sert de référence déclarée ; une sonde aléatoire est une `référence-interne`. **Après l'essai pilote** : **base externe = une méthode ou un résultat qui existe hors du billet** (publié, ou standard nommé) ; des variantes construites par les auteurs pour la comparaison (autres critères de choix, autres réglages de leur méthode) → `référence-interne` ; une comparaison sans chiffre (« very well-aligned », comparaison décrite qualitativement) ne compte pas ; une comparaison dite dans le texte mais chiffrée seulement dans une image sans légende chiffrée ne compte pas ; le chiffre d'un article antérieur cité en regard du chiffre des auteurs (« notably higher than the approximately 30% reported in … ») → `base-externe`.
- **Exemple** (`base-externe`) : `Qe3jdphWCg9kny3e5` — « It also scores 0.805 compared to 0.665 for Cywiński's method on Gemma-2-9B-it »
- **Exemple** (`référence-interne`) : `S9xyqRAziRMCcJQmz` — « cross-architecture yields better than random guessing, but not strong enough to be practically useful. »
- **Contre-exemple** (le mot seul) : `47CYFbrSyiJE2X5ot` — « 2.1 Baseline Sparse Autoencoder Let $d$ be the dimension of the language model activations. »

### G13. Choix justifié contre une option écartée
- **Question** : le billet justifie-t-il au moins un choix du dispositif en nommant l'option écartée ?
- **Modalités** : `présent` ; `absent`
- **Règle** : il faut les trois — le choix fait, l'option écartée **nommée en toutes lettres**, la raison — **dans la même phrase ou deux phrases voisines**. L'appui peut tenir en deux fragments.
- **Cas limites** : « we chose X because » sans option écartée → `absent` ; une option écartée par autrui ne compte pas ; une note de bas de page compte ; **un choix qui est le résultat lui-même (« the best architecture is X ») ne compte pas** ; **une recommandation aux autres (« one should use X rather than Y ») ne compte pas**. **Après l'essai pilote** : un résultat d'ablation (« if I drop X, loss increases ») n'est pas un choix justifié ; un choix de nom ou de terminologie n'est pas un choix du dispositif ; un changement de modèle ou de tâche raconté comme un essai qui a échoué (« X was the only one it could do, so I moved to Y ») compte si les trois éléments y sont ; la méthode proposée par le billet contre la méthode existante est la contribution, pas un choix justifié.
- **Exemple** : `d9FJHawgkiMSPjagR` — « We implement trusted labor with GPT-4 instead of humans because GPT-4 is cheaper. »
- **Contre-exemple** (raison sans option écartée) : `zj3GKWAnhPgTARByB` — « We chose the IOI task, as it's perhaps the most well-studied example of a non-trivial narrow capability in a real-world LLM »

### G14. Dispositif nommé
- **Question** : le billet nomme-t-il, dans son texte, (a) le ou les modèles étudiés, (b) les données ou la tâche, (c) un effectif (nombre d'exemples, d'essais, d'épisodes, de graines) ?
- **Modalités** : `trois-éléments` ; `moins-de-trois`
- **Règle** : chaque élément doit être dans le billet ; un renvoi à l'article ne le remplace pas. Il suffit que l'expérience principale ait les trois.
- **Cas limites** : une taille de modèle (paramètres) n'est pas un effectif ; un effectif dans une légende compte ; **une taille de jeu de données vaut effectif si la mesure porte sur ce jeu** ; **une quantité vague (« dozens of ») n'est pas un effectif**. **Après l'essai pilote** : modèle nommé = nom propre ou famille avec taille (« GPT-Neo-1.3B », « GPT2-small ») ; une description d'architecture sans nom (« a 16-layer decoder-only transformer ») ne suffit pas, sauf modèle jouet entraîné par les auteurs, décrit avec sa tâche ; effectif = nombre d'unités sur lesquelles porte la mesure principale (exemples, phrases, problèmes, épisodes, graines, modèles entraînés).
- **Exemple** (modèle et effectif dans la même phrase) : `JdHhtE73AwTBH8LKf` — « I ran 16k rollouts on Gemma-3-12B, labeled outcomes, and constructed two preliminary activation directions »
- **Contre-exemple** (taille de modèle, pas effectif) : `yHmJrDSJpFaNTZ9Tr` — « We demonstrate EM in a 0.5B parameter model »
- **Contre-exemple** (quantité vague) : `v7f8ayBxLhmMFRzpa` — « with the average taken over dozens of these dataset contrast pairs »

### G15. Incertitude statistique
- **Question** : le texte exprime-t-il l'incertitude des chiffres ?
- **Modalités** : `aucune` ; `intervalles-ou-barres` ; `test-statistique`
- **Règle** : `test-statistique` (prime) : test nommé ou valeur p ; `intervalles-ou-barres` : intervalle de confiance, erreur type, écart type, variance, barres d'erreur dites dans le texte ou une légende, ± ; sinon `aucune`.
- **Cas limites** : « p = » qui note une probabilité d'un modèle ou d'un exemple n'est pas un test ; « statistically significant » sans test ni valeur p → `aucune` ; barres invisibles (image sans légende) ne comptent pas ; **chercher dans tout le billet : l'incertitude tient souvent en une phrase courte** (« The bars show variance. »).
- **Exemple** (`test-statistique`) : `Qe3jdphWCg9kny3e5` — « paired sign-flip p ≈ 0.19 »
- **Exemple** (`intervalles-ou-barres`) : `5SKRHQEFr8wYQHYkx` — « Error bars are bootstrapped 90% confidence intervals. »
- **Contre-exemple** (probabilité d'un exemple) : `qpwsdu7qBaHTaujE3` — « one likely stays at $A$ (with $p = 0.9$) »

### G16. Non-revendications
- **Question** : le billet dit-il ce que le travail ne montre pas ?
- **Modalités** : `absentes` ; `phrase` ; `section`
- **Règle** : il faut une négation portant sur la **portée ou l'interprétation** du résultat (« we are not claiming », « this does not show », « this does not mean ») ; `section` si un intertitre l'annonce.
- **Cas limites** : **la tournure tranche** : « nous ne prétendons pas / cela ne montre pas » → ici ; « nous n'avons pas vérifié / testé / nous n'avons qu'un modèle » → limite (G17) ; une restriction de portée entre parenthèses (« (only for small models) ») → limite. **Après l'essai pilote** : une négation sur ce qu'une mesure ou une méthode ne distingue pas (« these do not differentiate between … ») → limite (G17) ; une négation qui écarte une explication (« it's not a variational vs deterministic issue ») n'est pas une non-revendication (voir G19) ; seule compte une négation sur ce que **le résultat du billet** permet de conclure.
- **Exemple** (`section`) : `8gy7c8GAPkuu6wTiX` — « What we are not claiming: »
- **Exemple** (`phrase`) : `SieLowPgNgRSPGhFw` — « We're not claiming current models are actually hiding reasoning from CoT. »
- **Contre-exemple** (limite, codée en G17) : `69fachkoAs2ZHeSst` — « These results are limited to one model family, one model organism, and one behavioural setting »

### G17. Limites
- **Question** : le billet énonce-t-il les faiblesses de son propre dispositif ?
- **Modalités** : `absentes` ; `dispersées` ; `section`
- **Règle** : `section` (prime) si un intertitre contient « limitation(s) » ou équivalent ; `dispersées` si au moins une limite des auteurs est dite ailleurs.
- **Cas limites** : les limites d'une méthode d'autrui qu'on étudie ne comptent pas ; une limite dans la section « travaux futurs » compte comme `dispersées` sauf si l'intertitre nomme les limites ; **une part non expliquée chiffrée (« ~6% of model behavior is not compatible ») → `dispersées`** ; une validation non faite → `dispersées`. **Après l'essai pilote** : une réserve brève sur l'interprétation d'une courbe (« this may mainly be caused by … ») n'est pas une limite du dispositif (voir G19) ; une phrase qui dit qu'une partie des résultats est en attente (« results are still pending ») → `dispersées` ; une réserve sur la reproductibilité (version de modèle retirée) → `dispersées`.
- **Exemple** (`section`) : `nLRKKCTtwQgvozLTN` — « Key limitations =============== We still aren’t sure about best practices for applying gradient routing. »
- **Exemple** (`dispersées`) : `v7f8ayBxLhmMFRzpa` — « Before concluding superadditivity in general, remember that this is just one datapoint »
- **Exemple** (`dispersées`, part non expliquée) : `sTe78dNJDGywu9Dz6` — « showing ~6% of model behavior is not compatible with our hypothesis »
- **Contre-exemple** (limites d'autrui) : `QL7J9wmS6W2fWpofd` — « Many people in the community were surprised when I mentioned some of the limitations of ROME »

### G18. Impasses rapportées
- **Question** : hors du résultat principal, le billet rapporte-t-il une tentative des auteurs qui n'a pas marché ?
- **Modalités** : `absentes` ; `mentionnées` ; `section`
- **Règle** : `section` (prime) si un intertitre annonce un essai raté ou un résultat nul ; `mentionnées` sinon dès une phrase. **Ne compter que les tentatives distinctes de celles qui font le résultat principal** (dans un billet à résultat négatif, l'échec principal relève de G03).
- **Cas limites** : l'échec d'une méthode d'autrui rapporté de seconde main ne compte pas ; une erreur corrigée en note d'édition relève de G22 ; **une expérience non menée faute de temps ou de moyens est une limite (G17)**. **Après l'essai pilote** : une variante des auteurs qui fait moins bien dans une comparaison voulue (une des conditions comparées, « why X underperforms ») fait partie du résultat, pas une impasse ; il faut une tentative abandonnée ou annoncée comme ratée (« we tried … it did not work », « null result ») ; un résultat inattendu (« were more effective in the opposite scenario ») n'est pas une impasse ; une conjecture négative (« it seems unlikely that … ») n'est pas une tentative.
- **Exemple** (`section`) : `JdHhtE73AwTBH8LKf` — « Experiment 4: Attention Patterns (Null result) »
- **Exemple** (`mentionnées`) : `mkbGjzxD8d8XqKHzA` — « We tried sampling 'best-of' approaches and found that they did not work »
- **Contre-exemple** (échec d'autrui) : `nmxzr2zsjNtjaHh7x` — « They found that linear probes did not work to recover board state »

### G19. Explication concurrente anticipée
- **Question** : les auteurs posent-ils une autre cause possible de leur résultat, et y répondent-ils par une expérience ou une analyse ?
- **Modalités** : `aucune` ; `posée-sans-contrôle` ; `posée-et-contrôlée`
- **Règle** : il faut **une phrase qui nomme une autre cause possible du résultat** (confusion, artefact, consigne, données) ; `posée-et-contrôlée` (prime) si une expérience ou une analyse des auteurs lui répond, **avant ou après, dans n'importe quel ordre** ; `posée-sans-contrôle` sinon (ou avec un seul argument).
- **Cas limites** : un contrôle du dispositif sans phrase qui nomme la cause qu'il écarte → `aucune` ; une objection d'un lecteur citée en note d'édition et contrôlée après coup compte. **Après l'essai pilote** : l'expérience qui répond doit être présentée comme réponse à la cause nommée (même paragraphe, ou renvoi explicite) ; un contrôle présent ailleurs sans lien écrit → `posée-sans-contrôle` ; une hypothèse des auteurs sur l'origine d'un détail secondaire (« this may mainly be caused by the decrease … ») n'est pas une cause concurrente du résultat principal → `aucune` ; une précaution du dispositif annoncée contre un risque nommé (« to reduce the chance of benchmark contamination, I randomize … ») → `posée-et-contrôlée`.
- **Exemple** (`posée-et-contrôlée`) : `7C4KJot4aN8ieEDoz` — « One concern is that our results might be sensitive to wording. To partially address this concern, we test another wording »
- **Exemple** (`posée-sans-contrôle`) : `qdxNsbY5kYNqcgzFb` — « they are not conclusive enough to eliminate alternative explanations. »
- **Contre-exemple** (décrit le travail d'un modèle, pas une cause concurrente du résultat) : `rbqJoxFZtae9x93mx` — « without thinking through all the possible reasons why the sprint may have gone wrong or what alternative explanations might be for the results. »

### G20. Appel à poursuivre
- **Question** : le billet invite-t-il d'autres chercheurs à poursuivre ?
- **Modalités** : `appel-aux-autres` ; `suite-des-auteurs-seule` ; `absente`
- **Règle** : `appel-aux-autres` (prime) : questions ouvertes adressées au lecteur, projets proposés, « we'd be excited to see », demande d'idées pour la suite ; `suite-des-auteurs-seule` : seuls les travaux prévus des auteurs ; sinon `absente`.
- **Cas limites** : une section « Future work » au « nous » sans invitation → `suite-des-auteurs-seule` ; la mention de travaux ultérieurs d'autrui n'est pas une suite ; **une question ouverte impersonnelle isolée (« remains an open question ») → `absente`** ; **une liste de travaux futurs sans sujet « nous » ni annonce de plan → `appel-aux-autres`**. **Après l'essai pilote** : une proposition de travail adressée à d'autres, y compris aux auteurs d'une méthode critiquée (« we suggest pooling … over more positions ») → `appel-aux-autres` ; un constat que la recherche est devenue accessible, sans travail proposé → `absente` ; l'annonce que l'auteur passe à autre chose, sans travail futur nommé → `absente` ; « future work could explore X » → `appel-aux-autres`.
- **Exemple** (`appel-aux-autres`) : `d9FJHawgkiMSPjagR` — « But we’d be excited to see future work that focuses on the problem of constructing expensive auditing processes. »
- **Exemple** (`appel-aux-autres`, demande d'idées) : `rbqJoxFZtae9x93mx` — « I'd be curious to hear any ideas on this from others in the community too! »
- **Exemple** (`suite-des-auteurs-seule`) : `qdxNsbY5kYNqcgzFb` — « We plan to continue working on it to validate and extend these preliminary results. »
- **Contre-exemple** (question impersonnelle isolée) : `S9xyqRAziRMCcJQmz` — « Whether this holds at larger scales remains an open question. »
- **Contre-exemple** (travail ultérieur d'autrui) : `8uMA6vwitdwqs5AH4` — « Future work by Anthropic "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" »

### G21. Code, modèles et données des auteurs
- **Question** : le billet donne-t-il accès au matériel des auteurs ?
- **Modalités** : `aucun` ; `promis` ; `lien`
- **Règle** : `lien` (prime) : un lien effectif (hôte visible dans la copie neutre : dépôt de code, carnet, hébergeur de modèles ou de données) vers le matériel des auteurs ; `promis` : promesse sans lien ; sinon `aucun`.
- **Cas limites** : un dépôt d'autrui ne compte pas ; « code available on request » → `promis` ; lien vers l'article seul → `aucun`.
- **Exemple** (`lien`) : `yHmJrDSJpFaNTZ9Tr` — « We open source all code, datasets, and finetuned models on GitHub and HuggingFace. »
- **Exemple** (`promis`) : `z6QQJbtpkEAX3Aojj` — « Code will be included in any final research report we decide to publish »
- **Contre-exemple** (dépôt d'autrui) : `8uMA6vwitdwqs5AH4` — « I first fixed the errors in the repo »

### G22. Note d'édition visible
- **Question** : le billet porte-t-il une note ajoutée après publication ?
- **Modalités** : `aucune` ; `mise-à-jour` ; `erratum`
- **Règle** : `erratum` (prime) : la note dit que des résultats ont changé ou étaient faux ; `mise-à-jour` : toute autre note datée ou marquée EDIT / UPDATE.
- **Cas limites** : « edit » au sens de l'édition d'un modèle ou d'un fait n'est pas une note ; une parenthèse « (edit: …) » compte.
- **Exemple** (`erratum`) : `M5vEjix8oPeWXeGFY` — « which fixed a crucial bug and significantly changed the results. »
- **Exemple** (`mise-à-jour`) : `aPeJE8bSo6rAFoLqg` — « UPDATE (14th Feb 2023): ChatGPT appears to have been patched! »
- **Contre-exemple** (édition de modèle) : `QL7J9wmS6W2fWpofd` — « Before edit: The mother tongue of Jeff Bezos is English »

### G23. Analogie pour le non-spécialiste
- **Question** : le billet rend-il un mécanisme ou un résultat lisible par une analogie hors du sous-domaine ?
- **Modalités** : `présente` ; `absente`
- **Règle** : une comparaison explicite (« like », « similar to », « analogous to », « just as ») avec un domaine extérieur (cerveau, vie courante, autre science), écrite par les auteurs, **qui éclaire un mécanisme ou un résultat**.
- **Cas limites** : la comparaison avec une expérience ou une méthode voisine n'est pas une analogie ; une analogie dans un texte de modèle cité ne compte pas ; une analogie en légende compte ; **expressions figées et métaphores mortes (« black box », « under the hood ») ne comptent pas** ; **une comparaison qui décrit l'expérience de travail des auteurs, pas un mécanisme, ne compte pas**. **Après l'essai pilote** : une comparaison avec une technique d'une autre discipline (traitement du signal, physique) compte si elle éclaire le mécanisme (« reminiscent of the apodization of peaks … ») ; un nom emprunté à une autre discipline sans comparaison du mécanisme (« inspired by the concept from quantum mechanics ») ne compte pas ; une comparaison au comportement humain courant (« like most people ») compte si elle éclaire le résultat.
- **Exemple** : `3PaLrzxagpbnNtPLT` — « In a sense, this is similar to how some people “think in words,” without having to say them out loud. »
- **Contre-exemple** (comparaison technique) : `nv8oedrnLXKRzNEL9` — « This is similar to the experiment from Figure 32 of the J-lens paper. »
- **Contre-exemple** (expérience de travail, pas mécanisme) : `rbqJoxFZtae9x93mx` — « Overall this feels like having a really fast and extremely smart masters student »

### G24. Déclaration d'usage d'une intelligence artificielle dans l'écriture
- **Question** : le billet déclare-t-il qu'un modèle de langue a écrit, édité, mis en forme, paraphrasé ou résumé une partie du texte ?
- **Modalités** : `déclarée` ; `aucune`
- **Règle** : coder la déclaration, ne pas deviner un usage.
- **Cas limites** : un modèle objet de l'étude, juge, générateur de données ou agent de recherche n'est pas une aide à l'écriture ; **du code écrit par un modèle → `aucune`** ; **figures ou schémas produits par un modèle → `aucune`** (la question porte sur le texte).
- **Exemple** : `nmxzr2zsjNtjaHh7x` — « Thanks to ChatGPT for formatting help. »
- **Exemple** : `S9xyqRAziRMCcJQmz` — « alongside with some paraphrasing support. »
- **Contre-exemple** (modèle juge) : `v7f8ayBxLhmMFRzpa` — « highly effective, as rated by Claude 2 »
- **Contre-exemple** (code écrit par un modèle) : `LQBFqyXA5to4iHEBC` — « A lot of the code is written by ChatGPT or Claude »

### G25. Appel aux retours
- **Question** : le billet demande-t-il explicitement aux lecteurs une critique, une correction ou un retour sur le billet ?
- **Modalités** : `oui` ; `non`
- **Règle** : demande adressée aux lecteurs du billet, qui porte sur le billet lui-même.
- **Cas limites** : remerciements pour des retours sur un brouillon → `non` ; « let me know if I missed a reference » → `oui` ; **une demande d'idées pour la suite → G20, `non` ici**. **Après l'essai pilote** : une demande d'avis sur des propositions faites dans le billet (« here are a few ideas. I'd love to hear your thoughts on these ») → `oui` (retour sur le contenu du billet) ; une demande d'idées nouvelles pour la suite → G20, `non` ici.
- **Exemple** : `S9xyqRAziRMCcJQmz` — « would really appreciate the feedback. »
- **Exemple** : `aPeJE8bSo6rAFoLqg` — « In the meantime, feedback is welcome, either here or at »
- **Contre-exemple** (remerciements) : `bWxNPMy5MhPnQTzKz` — « Thanks to Marius Hobbhahn and Oam Patel for helpful feedback on drafts. »

## B. Classes d'objections des commentaires


**Unité** : un commentaire parmi les dix retenus d'un billet (les dix mieux notés, réponses comprises). **Une seule classe par commentaire** : la première, dans l'ordre de priorité ci-dessous, que le commentaire **énonce lui-même** (et non qu'il laisse deviner). Limite dite d'avance : un long commentaire à plusieurs points tombe dans la première classe de l'ordre ; les parts des classes basses (O4, O11, O9, O12, O10, O13) sont sous-estimées.

**Réponses des auteurs** : marquées par programme (nom affiché du commentateur égal à un nom non vide de l'auteur ou d'un coauteur du manifeste), montrées pour le contexte avec la mention « ne pas coder », hors typologie. En développement : 80 commentaires sur 296. Un coauteur absent de la liste du site n'est pas reconnu ; le codeur le code `O0` s'il se présente comme auteur.

**Réponses dans un fil** : une réponse se code par l'objection qu'elle énonce elle-même ; si elle défend le billet, précise ou poursuit sans objection nouvelle → `O0` ; incompréhensible sans un parent non retenu → `O0`, doute coché. En développement, 63 commentaires codables sur 216 sont des réponses, dont 18 à un parent non retenu.

**Ordre de priorité** : O1, O2, O3, O7, O8, O6, O5, O4, O11, O9, O12, O10, O13, O0.

**Partage entre O2, O3 et O5** : conteste ce que la mesure saisit → O2 ; conteste un calcul, un chiffre, une définition ou le code → O3 ; ne conteste ni l'un ni l'autre mais la conclusion tirée ou sa mise en avant → O5.

### O1. Explication concurrente du résultat
- **Code** : `O1`
- **Définition** : un autre facteur, du dispositif ou général (théorie connue, contamination des données), produirait le même résultat ; ou la base de comparaison est jugée faible, injuste ou mal réglée.
- **Cas limites** : un facteur nommé sans lien au résultat → O9 ou O0 ; **base de comparaison jugée faible, injuste ou mal réglée → O1**.
- **Exemple** : `8gy7c8GAPkuu6wTiX/5xyCFhwNNapkSXbPT` — « due to the LLMs having been exposed to ideas about scheming AIs and disobedient employees in their training material »
- **Exemple** (base jugée injuste) : `v7f8ayBxLhmMFRzpa/AP72BpS9CQuYCbjs3` — « Hmm, yeah, that seems like a quite unfair comparison. »
- **Contre-exemple** (une autre façon de mesurer, pas une explication concurrente : O9) : `xwdRzJxyqFqgXTWbH/kcoWTGfidMgyfFcFs` — « I wonder what would happen if you used a different way of eliciting the model's mental maps of the world. »

### O2. La mesure ne mesure pas le concept revendiqué
- **Code** : `O2`
- **Définition** : doute sur le lien entre la mesure ou le vocabulaire et le concept (validité de construit).
- **Cas limites** : un nom mal choisi sans doute sur la mesure → O10.
- **Exemple** : `BuRt2igbFx9KaB5QG/3GjMyMGbXyoyRt2iD` — « The operationalization of myopia with large language models here seems more like a compelling metaphor than a useful technical concept. »
- **Exemple** : `3PaLrzxagpbnNtPLT/EwojCnTw23xnLuFr5` — « They call it 'J-space', but reading the paper, it isn't a subspace of the residual stream, or any kind of vector space. »
- **Contre-exemple** (doute sur un chiffre, pas sur le concept : O3) : `SieLowPgNgRSPGhFw/B2A4zgW7k6gDt33bW` — « I find the data in the left half of figure 2 surprising. »

### O3. Exactitude d'un chiffre, d'un calcul ou du code
- **Code** : `O3`
- **Définition** : doute, incompréhension ou erreur pointée sur un chiffre, une figure, un calcul, une définition technique ou le code.
- **Cas limites** : simple question de sens sans doute → O11.
- **Exemple** : `wtfvbsYjNHYYBmT3k/hPZfgA3BdXieNfFuY` — « I am very confused about some of the reported experimental results. »
- **Exemple** : `47CYFbrSyiJE2X5ot/ntRqbHsSMDD8BCXkK` — « I think this means that the FLOP scaling laws claim is misleading »
- **Exemple** : `mkbGjzxD8d8XqKHzA/4e8534hbyWCpZFgFD` — « when two singular vectors have approximately the same singular value, the two vectors are very numerically unstable (within their span). »
- **Contre-exemple** (question de sens : O11) : `bWxNPMy5MhPnQTzKz/CzXjsuPdLBEvbQyo2` — « What do you mean by "random linear probe"? »

### O4. Antériorité, travaux et techniques voisins
- **Code** : `O4`
- **Définition** : le commentaire nomme ou cherche un travail antérieur ou voisin, conteste la nouveauté, ou propose une technique connue et nommée, même sur un ton amical.
- **Cas limites** : **technique connue proposée par son nom (« DPO on contrast pairs ») → O4**, avant l'expérience suivante (O9) par l'ordre de priorité.
- **Exemple** : `aPeJE8bSo6rAFoLqg/r4cYjKb8ozJqthZeK` — « You also may want to checkout Universal Adversarial Triggers »
- **Exemple** : `mkbGjzxD8d8XqKHzA/snXYLcgexytzX5BGo` — « Is applying SVD a new idea in interpretability? »
- **Exemple** (technique connue) : `v7f8ayBxLhmMFRzpa/mfixbQMzhJSNfe9XZ` — « I think DPO on contrast pairs seems like a pretty natural approach. »
- **Contre-exemple** (le lecteur rapporte sa propre expérience nouvelle : O12) : `rbqJoxFZtae9x93mx/FNjFjaGSzbrJnEuHo` — « Funnily enough, I did the exact same thing on the same task two weeks ago and my army of Claude agents found a different solution »

### O5. Cadrage surdimensionné ou mal hiérarchisé
- **Code** : `O5`
- **Définition** : les données ne sont pas contestées, mais l'histoire racontée dépasse ce qu'elles montrent, ou met en avant le mauvais résultat.
- **Exemple** : `8gy7c8GAPkuu6wTiX/aD57abGz3JHcLXp7t` — « they aren’t emphasizing the most interesting results, which are the sandbagging results in section 3.6 and appendix A.6. »
- **Exemple** : `yHmJrDSJpFaNTZ9Tr/Ckz5Ws6cuKgJhWeTq` — « I'm surprised to see these results framed as a replication rather than failure to replicate the concept of EM »
- **Contre-exemple** (la portée pour le risque, pas le cadrage : O6) : `d9FJHawgkiMSPjagR/XTZKfsaJBHzhui8Dy` — « I think control research has relatively little impact on X-risk in general »

### O6. Pertinence ou effet pour le risque
- **Code** : `O6`
- **Définition** : le résultat, même vrai, compte peu ou autrement pour le risque ; ou le travail crée lui-même un risque (diffusion, détournement).
- **Exemple** : `d9FJHawgkiMSPjagR/XTZKfsaJBHzhui8Dy` — « I think control research has relatively little impact on X-risk in general »
- **Exemple** : `yHmJrDSJpFaNTZ9Tr/kg3onHFExrwzcmrWt` — « Considering the purpose of the datasets, I think putting them up as readily downloadable plaintext is terribly unwise. »
- **Contre-exemple** (un cadre où le résultat tomberait : O7) : `wSKPuBfgkkqfTpmWJ/jnWxCmoepFscKXWSR` — « Feels like if an AI manages to gain misaligned hidden behaviors during RL stages instead, a lot of this might unravel. »

### O7. Généralisation hors du cadre étudié
- **Code** : `O7`
- **Définition** : le commentaire nomme un cadre (tâche, entraînement, modèle, échelle) où le résultat pourrait ne pas tenir.
- **Exemple** : `wSKPuBfgkkqfTpmWJ/jnWxCmoepFscKXWSR` — « Feels like if an AI manages to gain misaligned hidden behaviors during RL stages instead, a lot of this might unravel. »
- **Contre-exemple** (proposition d'expérience sans doute sur la portée : O9) : `khFC2a4pLPvGtXAGG/v3J5ZdYwz97Rcz9HJ` — « I'm curious how this approach performs at detecting human lies »

### O8. Coût caché ou effet secondaire de la méthode
- **Code** : `O8`
- **Définition** : la méthode pourrait dégrader autre chose (capacité, performance, coût de calcul) ; la perte est nommée et non mesurée.
- **Exemple** : `nLRKKCTtwQgvozLTN/zcqzorSPkxcXjoWKv` — « do you have any experimental results on how much gradient routing degrades task performance compared to normal training? »
- **Contre-exemple** (risque pour la sûreté, pas coût de la méthode : O6) : `3PaLrzxagpbnNtPLT/abqEm88jECWvfRAtW` — « I fear you're just gonna filter for schemers that are deliberate about which consequences of their thinking reach the output »

### O9. Expérience suivante proposée
- **Code** : `O9`
- **Définition** : demande ou suggestion d'une mesure, d'une variante ou d'une figure de plus, sans contester le résultat et sans nommer une technique connue (O4).
- **Exemple** : `khFC2a4pLPvGtXAGG/v3J5ZdYwz97Rcz9HJ` — « I'm curious how this approach performs at detecting human lies »
- **Exemple** : `xwdRzJxyqFqgXTWbH/kcoWTGfidMgyfFcFs` — « I wonder what would happen if you used a different way of eliciting the model's mental maps of the world. »
- **Contre-exemple** (demande de matériel : O11) : `FF8i6SLfKb4g7C4EL/dHvqjfmcSJPjWbugw` — « It would be great if you could share some code from your experiments. »

### O10. Critique de la forme et de la présentation
- **Code** : `O10`
- **Définition** : critique argumentée de l'écriture, de la longueur, du titre, des figures ou de la manière de présenter les preuves.
- **Exemple** : `mkbGjzxD8d8XqKHzA/JeKubW3KEzSgvfqnP` — « this felt far too high production value - more posts, shorter posts and lower effort per post plz »
- **Contre-exemple** (éloge argumenté : O13) : `nv8oedrnLXKRzNEL9/CFHaWvrn3xegRZmcQ` — « It has comparison to other models, comparison to baselines, error bars, random control, no graph crimes, and its not in appendix. »

### O11. Demande de précision ou de matériel
- **Code** : `O11`
- **Définition** : question sur ce qui a été fait ou voulu dire, ou demande de code, de données, de détails, sans doute exprimé.
- **Exemple** : `bWxNPMy5MhPnQTzKz/CzXjsuPdLBEvbQyo2` — « What do you mean by "random linear probe"? »
- **Exemple** : `FF8i6SLfKb4g7C4EL/dHvqjfmcSJPjWbugw` — « It would be great if you could share some code from your experiments. »
- **Contre-exemple** (doute exprimé : O3) : `wtfvbsYjNHYYBmT3k/hPZfgA3BdXieNfFuY` — « I am very confused about some of the reported experimental results. »

### O12. Réplication ou prolongement par le lecteur
- **Code** : `O12`
- **Définition** : le commentateur rapporte une expérience, une réplication ou des données qu'il a faites lui-même à partir du billet. Signal favorable, pas une objection (hors des objections à prévenir, section 8).
- **Cas limites** : renvoi à un travail publié du commentateur, sans expérience faite à partir du billet → O4 ; réplication suivie d'une crainte énoncée → la crainte prime par l'ordre (voir le cas d'école).
- **Exemple** : `xwdRzJxyqFqgXTWbH/CvqAjm9jQgXSfZdDa` — « Very cool! I decided to try the same with Mandelbrot. »
- **Exemple** : `rbqJoxFZtae9x93mx/FNjFjaGSzbrJnEuHo` — « Funnily enough, I did the exact same thing on the same task two weeks ago and my army of Claude agents found a different solution »
- **Contre-exemple** (travail voisin publié : O4) : `mkbGjzxD8d8XqKHzA/KYa6vs9gRpgYKmE7r` — « In case it’s of interest, we have also performed some exploratory interpretability work using the SVD of model weights. »
- **Cas d'école** (réplication puis crainte : O1 par l'ordre) : `HhF5kESdtPHku7kim/zMh7XM5wm68hCSo9b` — « I was somewhat worried that some of the results you see are because the AI did not have a super strong association between misalignment »

### O13. Éloge argumenté (classe nouvelle au brouillon 3)
- **Code** : `O13`
- **Définition** : éloge qui dit ce qui est bien fait (méthode, présentation, preuves). Signal favorable, pas une objection (section 8).
- **Exemple** : `nv8oedrnLXKRzNEL9/CFHaWvrn3xegRZmcQ` — « It has comparison to other models, comparison to baselines, error bars, random control, no graph crimes, and its not in appendix. »
- **Contre-exemple** (éloge sans argument : O0) : `7C4KJot4aN8ieEDoz/2Mjc7Ghh3wkbwLJr6` — « Very good of you to actually follow through on the promises. »

### O0. Hors typologie
- **Code** : `O0`
- **Définition** : approbation sans argument, remerciements, curation ou modération par l'équipe du site, humour, lien sans contenu, défense du billet ou poursuite d'un fil sans objection nouvelle, discussion entre lecteurs qui ne dit rien du travail.
- **Exemple** : `xwdRzJxyqFqgXTWbH/jpDCfcYZsGzTHGjsm` — « Curated. This was wholesome curious fun. »
- **Exemple** (un lecteur défend le billet dans un fil) : `v7f8ayBxLhmMFRzpa/5H64rdESFnCDZ3yez` — « The finetuning worked fine for just getting the model to answer which of A/B is more/less sycophantic. »
- **Contre-exemple** (éloge argumenté : O13) : `nv8oedrnLXKRzNEL9/CFHaWvrn3xegRZmcQ` — « It has comparison to other models, comparison to baselines, error bars, random control, no graph crimes, and its not in appendix. »

## Format de sortie

Un fichier par codeur et par passe, en lignes JSON.
- **Gestes** : une ligne par billet et par geste, `{"codeur": "C1", "billet": "<neutre>", "geste": "G01", "modalite": "<valeur exacte de la grille>", "appui": "<fragment ou deux fragments séparés par ' […] '>", "doute": false}` ; **puis, après les 25 lignes du billet, une ligne** `{"codeur": "C1", "billet": "<neutre>", "geste": "AVEUGLE", "reconnu": false, "pari_statut": "bien-noté" | "peu-noté" | "ne-sait-pas"}` (`reconnu` : le codeur pense connaître ce billet ou ses auteurs). Nombre de lignes attendu : nombre de billets × 26 (1 612 pour la tenue à l'écart, 312 pour le pilote).
- **Objections** : `{"codeur": "C1", "billet": "<neutre>", "commentaire": "<neutre>", "classe": "O3", "appui": "…", "doute": false}`.
- **Contrôle de dépôt** (`pieces-grille-v3/controler_depot_v1.py`, un fichier à la fois, avant scellement) : refuse un fichier incomplet, une modalité absente de la grille, un doublon, une ligne `AVEUGLE` absente ou mal formée ; refuse un appui absent là où le code du contrôle l'exige (modalités qui entrent dans l'indicateur du geste ; toutes sont parmi les modalités non exceptées de la section 1) ; refuse un appui (chaque fragment, 25 mots au plus) introuvable dans la copie neutre après la normalisation de la grille ; pour les modalités d'en-tête — G02 `premier-paragraphe` et `en-tête`, G04 `bloc-étiqueté` et `liste-non-étiquetée`, G05 `avec-comparaison` et `seul`, G10 `en-tête`, G11 `figure-de-résultat` — refuse un appui dont le début est après la borne. Aucun repli silencieux.

