# Grille des gestes de rédaction et classes d'objections des billets de résultats — v1, brouillon 2

Écrite par le réviseur de la grille (agent neuf, ni auteur de la grille v1 ni du tri), le 2026-11-18, sous le mandat `docs/notes/billets-v1/mandat-revision-grille-v1.md` (empreinte `4056df38…`, vérifiée) et son complément de la session mère (second marquage, billets en désaccord entre les deux lecteurs du tri). Remplace pour le codage le brouillon 1 (`grille-gestes-v1-brouillon1.md`, `715ddbd6…`), qui reste archivé sans modification.

**Statut : brouillon, non gelé.** Rien n'a été codé. Aucun texte de la moitié tenue à l'écart n'a été ouvert. Pièces : `docs/notes/billets-v1/pieces-grille-v2/` (scripts et sorties scellés, liste en fin de document).

## 0. Ce qui change par rapport au brouillon 1

- **Corpus** : tout vient de la moitié « développement » du corpus v2 (58 billets : 36 bien notés, 22 appariés peu notés ; commentaires des 36 bien notés), `manifeste-corpus-v2.json`. Le codage « billet de résultats ou non » disparaît : les 120 billets du corpus v2 le sont par construction (règle `regle-tri-a-la-lecture-v2.md`).
- **Exemples** : tous les exemples du brouillon 1 tirés d'un billet absent de la moitié développement v2 sont retirés (17 billets cités : 12 passés en tenue à l'écart v2, 5 absents du corpus v2 ; tableau en section 6). Les exemples gardés ou nouveaux sont tirés de la moitié développement v2, **hors des deux billets de développement marqués par le désaccord des lecteurs du tri** (« Some Lessons Learned from Studying Indirect Object Identification in GPT-2 small », `3ecs6duLmTfyra3Gp` ; « Discriminating Behaviorally Identical Classifiers », `s7uD3tzHMvD868ehr`), et vérifiés par programme (section 7).
- **Forme** : chaque geste devient **une question fermée par billet**, à modalités exclusives (deux à quatre), avec règle de décision, cas limites, un exemple et un contre-exemple. Chaque geste a un **indicateur** binaire écrit d'avance (les modalités qui valent 1), sur lequel portent la fiabilité et la comparaison.
- **En-tête objectif** : « en tête » = les 250 premiers mots du corps, titre exclu. Le script de préparation des copies insère une borne visible (`⟦FIN DE L'EN-TÊTE — 250 MOTS⟧`) ; le codeur ne compte rien.
- **Mesures par programme, non codées** : longueur (mots du site, variable d'appariement, donc descriptive seulement), nombre d'images, nombre de tableaux. Elles sortent du codage humain.
- **Gestes** : 25 au brouillon 1 → **25 questions** au brouillon 2. Aucun geste retiré en entier ; deux fusions, quatre scissions, des sous-valeurs retirées (détail en section 5).
- **Objections** : 12 classes + hors typologie → **12 classes + hors typologie**, une seule classe par commentaire, ordre de priorité écrit ; deux fusions, deux classes nouvelles nées de la lecture des commentaires de développement v2 (section 3).

## 1. Conventions communes

- **Unité** : le billet entier, dans sa copie neutre (section 4), titre compris pour la question du titre seulement.
- **Corps** : le texte sous le titre. **Avant-propos** : ce qui précède la première phrase de contenu — listes d'auteurs, remerciements, liens vers l'article ou les fils de discussion, notes d'édition, statut épistémique. **Premier paragraphe** : le premier bloc de texte du corps hors avant-propos, jusqu'à la première ligne vide ou au premier intertitre.
- **Résultat principal** : ce que les auteurs disent avoir trouvé et mettent en avant (résumé, titre, conclusion). Une question, un plan, une méthode annoncée ne sont pas un résultat.
- **Des auteurs** : fait ou écrit par les auteurs du billet ; ce qu'ils rapportent d'autrui ne compte pas, ni le texte d'un modèle cité (transcriptions, sorties de modèle entre guillemets ou en bloc).
- **Images** : le codeur ne voit pas les images, seulement leur texte de remplacement et la légende qui suit. Une décision qui dépend d'une image se prend sur ce texte seul.
- **Doute** : chaque ligne de codage porte un champ `doute` (oui / non). Le doute n'autorise pas de modalité nouvelle ; on choisit la modalité la plus proche selon la règle, et on coche le doute.
- **Appui** : pour toute modalité autre que la modalité d'absence, le codeur copie une citation d'appui de 25 mots au plus. L'appui sert à l'arbitrage et à l'audit, pas au calcul.
- **Format des exemples** : identifiant du billet, puis citation de 25 mots au plus, en anglais, telle qu'elle figure dans le texte (mise en forme et adresses de liens ôtées). Pour un titre : `(titre)`. Pour un commentaire : `billet/commentaire`.

---

## A. Gestes de rédaction (25 questions)

### G01. Forme du titre
- **Question** : que dit le titre du résultat ?
- **Modalités** : `affirmation` ; `affirmation-atténuée` ; `question` ; `sans-résultat`
- **Indicateur** : `affirmation`, `affirmation-atténuée`
- **Analyse** : comparée
- **Règle** : coder le titre seul. `affirmation` : le titre énonce un résultat sans atténuation, positif ou négatif. `affirmation-atténuée` : le résultat est énoncé avec may, might, could, appears, seems, towards, initial. `question` : le titre est une question, même rhétorique. `sans-résultat` : nom de méthode, d'objet, de tâche ou formule, sans résultat énoncé.
- **Cas limites** : titre en deux segments (deux-points, tiret) → coder le segment qui porte un résultat s'il y en a un, sinon `sans-résultat` ; question dans un segment et affirmation dans l'autre → `affirmation` ; un titre négatif (« isn't strong ») est une `affirmation` ; « (Yet) » ne suffit pas à atténuer.
- **Exemple** (`affirmation`) : `nmxzr2zsjNtjaHh7x` (titre) — « Actually, Othello-GPT Has A Linear Emergent World Representation »
- **Exemple** (`affirmation-atténuée`) : `69fachkoAs2ZHeSst` (titre) — « J-space auditing might be unreliable »
- **Exemple** (`question`) : `xwdRzJxyqFqgXTWbH` (titre) — « How Does A Blind Model See The Earth? »
- **Contre-exemple** (`sans-résultat`, bien que le billet ait un résultat net) : `v7f8ayBxLhmMFRzpa` (titre) — « Steering Llama-2 with contrastive activation additions »

### G02. Place de la thèse
- **Question** : où apparaît pour la première fois l'énoncé du résultat principal ?
- **Modalités** : `premier-paragraphe` ; `en-tête` ; `plus-loin`
- **Indicateur** : `premier-paragraphe`, `en-tête`
- **Analyse** : comparée
- **Règle** : `premier-paragraphe` (au sens de la section 1, avant-propos exclu) ; `en-tête` : ailleurs avant la borne des 250 mots ; `plus-loin` : après la borne, ou jamais.
- **Cas limites** : une question d'accroche n'est pas une thèse ; un plan (« in this post we will ») n'est pas une thèse ; une liste de résultats en tête compte ; un résumé d'article copié compte s'il énonce le résultat ; une thèse coupée par la borne compte comme `en-tête`.
- **Exemple** (`premier-paragraphe`) : `69fachkoAs2ZHeSst` — « Across these preliminary experiments, decoded J-space did not seem particularly informative about reward-hacking behaviour. »
- **Exemple** (`en-tête`, après un paragraphe d'image) : `3PaLrzxagpbnNtPLT` — « In a new paper, we present evidence that a similar distinction has emerged in modern language models like Claude. »
- **Contre-exemple** (accroche, pas thèse) : `zsr4rWRASxwmgXfmq` — « Claude can speak dozens of languages. What language, if any, is it using "in its head"? »

### G03. Polarité du résultat principal
- **Question** : le résultat principal est-il positif, négatif ou mixte ?
- **Modalités** : `positif` ; `négatif-ou-nul` ; `mixte`
- **Indicateur** : `négatif-ou-nul`, `mixte`
- **Analyse** : comparée
- **Règle** : `négatif-ou-nul` : le résultat principal est un échec d'une méthode, une réfutation, une absence d'effet, une réplication ratée. `mixte` : les auteurs mettent en avant à égalité un oui et un non (« possibly, but not reliably »). Sinon `positif`.
- **Cas limites** : un résultat nul secondaire dans un billet positif ne change pas la polarité (voir G18) ; montrer qu'une méthode d'autrui échoue est `négatif-ou-nul` même si le ton est triomphant ; une méthode nouvelle qui bat une autre est `positif`.
- **Exemple** (`négatif-ou-nul`) : `wtfvbsYjNHYYBmT3k` — « At this point, we think it is unlikely to be directly helpful for implementations of alignment strategies (>95%). »
- **Exemple** (`mixte`) : `QQQAcKuWK6k98FivY` — « For open-weight NLAs, the answer seems to be: "possibly, but definitely not reliably". »
- **Contre-exemple** (nul secondaire dans un billet `positif`) : `JdHhtE73AwTBH8LKf` — « Experiment 4: Attention Patterns (Null result) »

### G04. Résumé en tête
- **Question** : y a-t-il, avant la borne des 250 mots, un bloc qui résume les résultats ?
- **Modalités** : `aucun` ; `bloc-étiqueté` ; `liste-non-étiquetée`
- **Indicateur** : `bloc-étiqueté`, `liste-non-étiquetée`
- **Analyse** : comparée
- **Règle** : `bloc-étiqueté` : bloc qui commence avant la borne sous une étiquette (TL;DR, TLDR, Summary, Executive summary, Abstract, Overview, Key results, High-level takeaways, One-sentence summary, Bottom line) et qui énonce au moins un résultat. `liste-non-étiquetée` : liste numérotée ou à puces de résultats sans étiquette. Sinon `aucun`.
- **Cas limites** : un résumé d'article copié sous « Abstract » est `bloc-étiqueté` ; une étiquette suivie d'une simple motivation sans résultat → `aucun` ; un plan du billet n'est pas un résumé.
- **Exemple** (`bloc-étiqueté`) : `LQBFqyXA5to4iHEBC` — « This is an informal progress update with some preliminary results using Sparse Autoencoders (SAEs) to detect AI-generated text. Summary »
- **Exemple** (`liste-non-étiquetée`) : `bWxNPMy5MhPnQTzKz` — « In this post, I present experimental results which highlight the strengths and weaknesses of CCS. 1. CCS is able to find a single linear probe »
- **Contre-exemple** (plan, pas résumé) : `d9FJHawgkiMSPjagR` — « In this post: We summarize the paper; We compare our methodology to the methodology of other safety papers. »

### G05. Chiffre de résultat en tête
- **Question** : un nombre de résultat des auteurs figure-t-il avant la borne des 250 mots ?
- **Modalités** : `avec-comparaison` ; `seul` ; `aucun`
- **Indicateur** : `avec-comparaison`, `seul`
- **Analyse** : comparée
- **Règle** : nombre produit par l'expérience des auteurs (taux, score, effet, compte). `avec-comparaison` : il est mis en regard d'un autre nombre (base, avant / après, autre méthode) dans la même phrase ou la suivante. `seul` : sinon.
- **Cas limites** : taille de modèle, de jeu de données, nombre de tâches, date → contexte, pas résultat ; une probabilité subjective des auteurs (crédence) n'est pas un résultat (voir G06) ; un nombre d'une figure dont seule la légende est visible compte s'il est dans la légende.
- **Exemple** (`avec-comparaison`) : `yHmJrDSJpFaNTZ9Tr` — « we train small EM models which are misaligned 40% of the time, and coherent 99% of the time, compared to 6% and 69% prior. »
- **Exemple** (`seul`) : `T64JQFZ5NwSzx4mJu` — « A fair amount of these LoRAs (25%) correspond to linear, interpretable vectors that can be extracted using mean activation differences. »
- **Contre-exemple** (nombre de contexte donné par autrui) : `sTe78dNJDGywu9Dz6` — « the test set accuracy is 95.58% »

### G06. Statut épistémique déclaré
- **Question** : le billet déclare-t-il sa confiance sous une forme explicite ?
- **Modalités** : `absent` ; `statut-étiqueté` ; `crédences-chiffrées`
- **Indicateur** : `statut-étiqueté`, `crédences-chiffrées`
- **Analyse** : comparée
- **Règle** : `crédences-chiffrées` dès qu'une probabilité est attachée à une affirmation des auteurs (prime) ; `statut-étiqueté` si une étiquette « Epistemic status » ou équivalente existe n'importe où ; sinon `absent`. Une réserve libre sans étiquette relève de G07, pas d'ici (la valeur `réserve-libre` du brouillon 1 est retirée).
- **Cas limites** : « confidence » dans un résultat de modèle (score de confiance) ne compte pas ; une étiquette placée au milieu d'une section compte.
- **Exemple** (`statut-étiqueté`) : `M5vEjix8oPeWXeGFY` — « Epistemic Status: Confident only in these particular results. »
- **Exemple** (`crédences-chiffrées`) : `wtfvbsYjNHYYBmT3k` — « Credences are based on a poll of Seb, Vikrant, Zac, Johannes, Rohin »
- **Contre-exemple** (réserve sans étiquette, codée en G07) : `HLJoJYi52mxgomujc` — « This post is best viewed as an informal report on preliminary results done over a couple days, rather than a very polished analysis. »

### G07. Caractère préliminaire annoncé
- **Question** : le billet dit-il que l'ensemble du travail est préliminaire, rapide ou inachevé ?
- **Modalités** : `annoncé` ; `non-dit`
- **Indicateur** : `annoncé`
- **Analyse** : comparée
- **Règle** : `annoncé` si une phrase des auteurs qualifie le billet ou le travail entier de préliminaire, intermédiaire, rapide, en cours, non poli, fait en quelques jours, en hackathon, ou comme candidature. Fusionne la valeur « réserve-libre » du statut épistémique et les valeurs de maturité du brouillon 1.
- **Cas limites** : « preliminary » qui qualifie une méthode ou une seule section → `non-dit` ; le programme ou l'institution seuls (MATS, laboratoire) ne disent rien de la maturité (voir G09) ; « work in progress » dans une note de mise à jour compte.
- **Exemple** : `z6QQJbtpkEAX3Aojj` — « This post is not intended to be a polished research product. »
- **Contre-exemple** (préliminaire qualifie une méthode) : `mkbGjzxD8d8XqKHzA` — « our approach also provides a preliminary way to edit the knowledge of the network. »
- **Contre-exemple** (contexte, pas maturité) : `rbqJoxFZtae9x93mx` — « This work was done as part of MATS 7.1 »

### G08. Rapport à un article des auteurs
- **Question** : le billet est-il lié à un article (papier, prépublication, mémoire) des mêmes auteurs ?
- **Modalités** : `aucun-article` ; `présente-l-article` ; `complète-l-article`
- **Indicateur** : `présente-l-article`, `complète-l-article`
- **Analyse** : comparée
- **Règle** : `présente-l-article` : le billet annonce, résume ou copie un article des auteurs (fusion des valeurs « copie », « résumé », « lien seul » du brouillon 1). `complète-l-article` : il rapporte surtout ce que l'article ne contient pas (expériences de suite, ablations, réévaluation). Sinon `aucun-article`.
- **Cas limites** : un article d'autrui discuté ou rejoué → `aucun-article` ; un mémoire de master ou de stage des auteurs compte comme article ; l'article publié après le billet et signalé par une note d'édition → `aucun-article` ici (la note relève de G22).
- **Exemple** (`présente-l-article`) : `khFC2a4pLPvGtXAGG` — « This post is a copy of the introduction of this paper on lie detection in LLMs. »
- **Exemple** (`complète-l-article`) : `qGRk7uF92Gcmq2oeK` — « We ran some follow-up experiments that we added to the paper in two new appendices B.5 and B.6. »
- **Contre-exemple** (article d'autrui) : `bWxNPMy5MhPnQTzKz` — « Discovering Latent Knowledge in Language Models Without Supervision describes Contrast-Consistent Search (CCS) »

### G09. Contexte de production nommé
- **Question** : le billet nomme-t-il le cadre dans lequel le travail a été fait ?
- **Modalités** : `aucun` ; `programme-de-formation` ; `organisation`
- **Indicateur** : `programme-de-formation`, `organisation`
- **Analyse** : comparée
- **Règle** : `programme-de-formation` : programme d'encadrement, bourse de recherche à cohorte, camp, hackathon, cursus (MATS, SPAR, AI Safety Camp, Astra, master) — prime si les deux sont nommés ; `organisation` : laboratoire, entreprise, université, institut nommé comme lieu du travail ; sinon `aucun`.
- **Cas limites** : un financement seul ne compte pas ; des remerciements à des personnes d'une organisation ne comptent pas ; une adresse électronique d'une organisation ne compte pas ; les noms d'auteurs sont masqués dans la copie neutre, l'affiliation écrite reste.
- **Exemple** (`programme-de-formation`) : `47CYFbrSyiJE2X5ot` — « Produced as part of the ML Alignment & Theory Scholars Program »
- **Exemple** (`organisation`) : `HhF5kESdtPHku7kim` — « Produced as part of the UK AISI Model Transparency Team. »
- **Contre-exemple** (financement seul) : `BuRt2igbFx9KaB5QG` — « was also supported by a grant from the Future Fund regranting program while working on this project. »

### G10. Enjeu de sûreté explicite
- **Question** : où le billet dit-il pour la première fois pourquoi le résultat compte pour la sûreté ?
- **Modalités** : `en-tête` ; `plus-loin` ; `absent`
- **Indicateur** : `en-tête`
- **Analyse** : comparée
- **Règle** : il faut un lien explicite entre le résultat (ou la question étudiée) et un risque, un usage de surveillance, d'audit, d'alignement ou de contrôle ; avant la borne → `en-tête`.
- **Cas limites** : « intéressant », « mystère », « progrès de l'interprétabilité » sans risque nommé → ne compte pas ; une étiquette de sujet (« deception ») sans phrase de lien ne compte pas.
- **Exemple** (`en-tête`) : `SieLowPgNgRSPGhFw` — « If models can do extensive reasoning without outputting any CoT, it would have implications for safety. »
- **Contre-exemple** (intérêt sans risque) : `N6WM6hs7RQMKDhYjB` — « in my opinion is one of the most fascinating mysteries in deep learning. »

### G11. Figure de résultat en tête
- **Question** : avant la borne des 250 mots, y a-t-il une figure, et laquelle ?
- **Modalités** : `figure-de-résultat` ; `autre-figure` ; `aucune`
- **Indicateur** : `figure-de-résultat`
- **Analyse** : comparée
- **Règle** : décider sur le texte de remplacement et la légende : `figure-de-résultat` si la légende ou la phrase voisine décrit des données des auteurs (courbe, score, effet, tableau de résultats) ; `autre-figure` : schéma, illustration, mème, capture sans donnée, ou légende muette ; `aucune` sinon. Un tableau en tête compte comme figure. Le nombre total d'images et de tableaux est mesuré par programme, non codé (les sous-valeurs « légendes numérotées » et « figure décorative » du brouillon 1 sont retirées : invisibles au codeur).
- **Cas limites** : image sans légende → `autre-figure` ; figure de résultat d'autrui → `autre-figure`.
- **Exemple** (`figure-de-résultat`) : `v7f8ayBxLhmMFRzpa` — « The effects of subtracting or adding a "sycophancy vector" to one bias term. »
- **Contre-exemple** (`autre-figure`) : `khFC2a4pLPvGtXAGG` — « Our lie dectector in meme form. »

### G12. Base de comparaison du résultat principal
- **Question** : à quoi le résultat principal est-il comparé, chiffre à l'appui ?
- **Modalités** : `aucune` ; `hasard-ou-trivial` ; `base-nommée`
- **Indicateur** : `base-nommée`
- **Analyse** : comparée
- **Règle** : `base-nommée` : méthode concurrente, base naïve nommée, condition de contrôle, ablation, plafond, résultat antérieur rejoué, chiffré dans le texte (prime) ; `hasard-ou-trivial` : seule comparaison au hasard ou à une réponse constante ; `aucune`.
- **Cas limites** : le mot « baseline » qui nomme une architecture ou un point de départ sans comparaison chiffrée ne suffit pas ; une comparaison visible seulement dans une image sans légende chiffrée ne compte pas ; une comparaison entre modèles étudiés (modèle A contre modèle B) n'est une base que si l'un sert de référence déclarée.
- **Exemple** (`base-nommée`) : `Qe3jdphWCg9kny3e5` — « It also scores 0.805 compared to 0.665 for Cywiński's method on Gemma-2-9B-it »
- **Exemple** (`hasard-ou-trivial`) : `S9xyqRAziRMCcJQmz` — « cross-architecture yields better than random guessing, but not strong enough to be practically useful. »
- **Contre-exemple** (le mot seul) : `47CYFbrSyiJE2X5ot` — « 2.1 Baseline Sparse Autoencoder Let $d$ be the dimension of the language model activations. »

### G13. Choix justifié contre une option écartée
- **Question** : le billet justifie-t-il au moins un choix du dispositif en nommant l'option écartée ?
- **Modalités** : `présent` ; `absent`
- **Indicateur** : `présent`
- **Analyse** : comparée
- **Règle** : il faut les trois : le choix fait, l'option écartée nommée, la raison. Le brouillon 1 comptait aussi le choix justifié sans option écartée et le nombre d'occurrences : retirés (trop fréquents pour discriminer, comptage peu fiable).
- **Cas limites** : « we chose X because » sans option écartée → `absent` ; une option écartée par autrui ne compte pas ; une note de bas de page compte.
- **Exemple** : `d9FJHawgkiMSPjagR` — « We implement trusted labor with GPT-4 instead of humans because GPT-4 is cheaper. »
- **Contre-exemple** (raison sans option écartée) : `zj3GKWAnhPgTARByB` — « We chose the IOI task, as it's perhaps the most well-studied example of a non-trivial narrow capability in a real-world LLM »

### G14. Dispositif nommé
- **Question** : le billet nomme-t-il, dans son texte, (a) le ou les modèles étudiés, (b) les données ou la tâche, (c) un effectif (nombre d'exemples, d'essais, d'épisodes, de graines) ?
- **Modalités** : `trois-éléments` ; `moins-de-trois`
- **Indicateur** : `trois-éléments`
- **Analyse** : comparée
- **Règle** : chaque élément doit être dans le billet ; un renvoi à l'article ne le remplace pas. Les effectifs, qui étaient une valeur de l'incertitude statistique au brouillon 1, sont ici (scission).
- **Cas limites** : une taille de modèle (paramètres) n'est pas un effectif ; un effectif dans une légende compte ; plusieurs expériences : il suffit que l'expérience principale ait les trois.
- **Exemple** (modèle et effectif dans la même phrase) : `JdHhtE73AwTBH8LKf` — « I ran 16k rollouts on Gemma-3-12B, labeled outcomes, and constructed two preliminary activation directions »
- **Contre-exemple** (taille de modèle, pas effectif) : `yHmJrDSJpFaNTZ9Tr` — « We demonstrate EM in a 0.5B parameter model »

### G15. Incertitude statistique
- **Question** : le texte exprime-t-il l'incertitude des chiffres ?
- **Modalités** : `aucune` ; `intervalles-ou-barres` ; `test-statistique`
- **Indicateur** : `intervalles-ou-barres`, `test-statistique`
- **Analyse** : comparée
- **Règle** : `test-statistique` (prime) : test nommé ou valeur p ; `intervalles-ou-barres` : intervalle de confiance, erreur type, écart type, barres d'erreur dites dans le texte ou une légende, ± ; sinon `aucune`. Les effectifs passent en G14.
- **Cas limites** : « p = » qui note une probabilité d'un modèle ou d'un exemple n'est pas un test ; « statistically significant » sans test nommé → `test-statistique` seulement si une valeur p ou un test est donné, sinon `aucune` ; barres invisibles (image sans légende) ne comptent pas.
- **Exemple** (`test-statistique`) : `Qe3jdphWCg9kny3e5` — « paired sign-flip p ≈ 0.19 »
- **Exemple** (`intervalles-ou-barres`) : `5SKRHQEFr8wYQHYkx` — « Error bars are bootstrapped 90% confidence intervals. »
- **Contre-exemple** (probabilité d'un exemple) : `qpwsdu7qBaHTaujE3` — « one likely stays at $A$ (with $p = 0.9$) »

### G16. Non-revendications
- **Question** : le billet dit-il ce que le travail ne montre pas ?
- **Modalités** : `absentes` ; `phrase` ; `section`
- **Indicateur** : `phrase`, `section`
- **Analyse** : comparée
- **Règle** : il faut une négation portant sur la portée ou l'interprétation du résultat (« we are not claiming », « does not show ») ; `section` si un intertitre l'annonce.
- **Cas limites** : une faiblesse du dispositif (un seul modèle, petit effectif) est une limite (G17), pas une non-revendication ; « we did not test X » est une limite.
- **Exemple** (`section`) : `8gy7c8GAPkuu6wTiX` — « What we are not claiming: »
- **Exemple** (`phrase`) : `SieLowPgNgRSPGhFw` — « We're not claiming current models are actually hiding reasoning from CoT. »
- **Contre-exemple** (limite, codée en G17) : `69fachkoAs2ZHeSst` — « These results are limited to one model family, one model organism, and one behavioural setting »

### G17. Limites
- **Question** : le billet énonce-t-il les faiblesses de son propre dispositif ?
- **Modalités** : `absentes` ; `dispersées` ; `section`
- **Indicateur** : `dispersées`, `section`
- **Analyse** : comparée
- **Règle** : `section` si un intertitre contient « limitation(s) » ou équivalent ; `dispersées` si au moins une limite des auteurs est dite ailleurs. Le renvoi aux limites de l'article et le comptage des limites du brouillon 1 sont retirés.
- **Cas limites** : les limites d'une méthode d'autrui qu'on étudie ne comptent pas ; une limite dans la section « travaux futurs » compte comme `dispersées` sauf si l'intertitre nomme les limites.
- **Exemple** (`section`) : `nLRKKCTtwQgvozLTN` — « Key limitations =============== We still aren’t sure about best practices for applying gradient routing. »
- **Contre-exemple** (limites d'autrui) : `QL7J9wmS6W2fWpofd` — « Many people in the community were surprised when I mentioned some of the limitations of ROME »

### G18. Impasses rapportées
- **Question** : hors du résultat principal, le billet rapporte-t-il une tentative des auteurs qui n'a pas marché ?
- **Modalités** : `absentes` ; `mentionnées` ; `section`
- **Indicateur** : `mentionnées`, `section`
- **Analyse** : comparée
- **Règle** : `section` si un intertitre annonce un essai raté ou un résultat nul ; `mentionnées` sinon dès une phrase. Le résultat principal négatif relève de G03 (scission avec le brouillon 1).
- **Cas limites** : l'échec d'une méthode d'autrui rapporté de seconde main ne compte pas ; une erreur corrigée en note d'édition relève de G22.
- **Exemple** (`section`) : `JdHhtE73AwTBH8LKf` — « Experiment 4: Attention Patterns (Null result) »
- **Exemple** (`mentionnées`) : `mkbGjzxD8d8XqKHzA` — « We tried sampling 'best-of' approaches and found that they did not work »
- **Contre-exemple** (échec d'autrui) : `nmxzr2zsjNtjaHh7x` — « They found that linear probes did not work to recover board state »

### G19. Explication concurrente anticipée
- **Question** : les auteurs posent-ils une objection ou une explication concurrente de leur résultat, et la contrôlent-ils ?
- **Modalités** : `aucune` ; `posée-sans-contrôle` ; `posée-et-contrôlée`
- **Indicateur** : `posée-et-contrôlée`
- **Analyse** : comparée
- **Règle** : `posée-et-contrôlée` (prime) : l'objection est suivie d'une expérience ou d'une analyse faite pour y répondre ; `posée-sans-contrôle` : l'objection est dite, sans contrôle ou avec un seul argument. La valeur « sections en questions » du brouillon 1 est retirée : on code le contenu.
- **Cas limites** : un « contrôle » prévu dès le dispositif sans objection nommée → `aucune` ; une objection d'un lecteur citée en note d'édition et contrôlée après coup compte.
- **Exemple** (`posée-et-contrôlée`) : `7C4KJot4aN8ieEDoz` — « One concern is that our results might be sensitive to wording. To partially address this concern, we test another wording »
- **Exemple** (`posée-sans-contrôle`) : `qdxNsbY5kYNqcgzFb` — « they are not conclusive enough to eliminate alternative explanations. »
- **Contre-exemple** (décrit le travail d'un modèle, pas une objection au résultat) : `rbqJoxFZtae9x93mx` — « without thinking through all the possible reasons why the sprint may have gone wrong or what alternative explanations might be for the results. »

### G20. Appel à poursuivre
- **Question** : le billet invite-t-il d'autres chercheurs à poursuivre ?
- **Modalités** : `appel-aux-autres` ; `suite-des-auteurs-seule` ; `absente`
- **Indicateur** : `appel-aux-autres`
- **Analyse** : comparée
- **Règle** : `appel-aux-autres` (prime) : questions ouvertes adressées au lecteur, projets proposés, « we'd be excited to see » ; `suite-des-auteurs-seule` : seuls les travaux prévus des auteurs ; sinon `absente`. Fusionne « appel aux autres » et « liste de questions » du brouillon 1.
- **Cas limites** : une section « Future work » à la première personne du pluriel sans invitation → `suite-des-auteurs-seule` ; la mention de travaux ultérieurs d'autrui n'est pas une suite.
- **Exemple** (`appel-aux-autres`) : `d9FJHawgkiMSPjagR` — « But we’d be excited to see future work that focuses on the problem of constructing expensive auditing processes. »
- **Exemple** (`suite-des-auteurs-seule`) : `qdxNsbY5kYNqcgzFb` — « We plan to continue working on it to validate and extend these preliminary results. »
- **Contre-exemple** (travail ultérieur d'autrui) : `8uMA6vwitdwqs5AH4` — « Future work by Anthropic "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" »

### G21. Code, modèles et données des auteurs
- **Question** : le billet donne-t-il accès au matériel des auteurs ?
- **Modalités** : `aucun` ; `promis` ; `lien`
- **Indicateur** : `lien`
- **Analyse** : comparée
- **Règle** : `lien` : un lien effectif (hôte visible dans la copie neutre : dépôt de code, carnet, hébergeur de modèles ou de données) vers le matériel des auteurs ; `promis` : promesse sans lien ; sinon `aucun`. Les sous-valeurs « code », « code et données », « carnet » du brouillon 1 sont fusionnées.
- **Cas limites** : un dépôt d'autrui ne compte pas ; « code available on request » → `promis` ; lien vers l'article seul → `aucun`.
- **Exemple** (`lien`) : `yHmJrDSJpFaNTZ9Tr` — « We open source all code, datasets, and finetuned models on GitHub and HuggingFace. »
- **Exemple** (`promis`) : `z6QQJbtpkEAX3Aojj` — « Code will be included in any final research report we decide to publish »
- **Contre-exemple** (dépôt d'autrui) : `8uMA6vwitdwqs5AH4` — « I first fixed the errors in the repo »

### G22. Note d'édition visible
- **Question** : le billet porte-t-il une note ajoutée après publication ?
- **Modalités** : `aucune` ; `mise-à-jour` ; `erratum`
- **Indicateur** : `mise-à-jour`, `erratum`
- **Analyse** : descriptive (geste postérieur à la publication, qui peut suivre l'audience au lieu de la causer : jamais une consigne)
- **Règle** : `erratum` (prime) : la note dit que des résultats ont changé ou étaient faux ; `mise-à-jour` : toute autre note datée ou marquée EDIT / UPDATE.
- **Cas limites** : « edit » au sens de l'édition d'un modèle ou d'un fait n'est pas une note ; une parenthèse « (edit: …) » compte.
- **Exemple** (`erratum`) : `M5vEjix8oPeWXeGFY` — « which fixed a crucial bug and significantly changed the results. »
- **Exemple** (`mise-à-jour`) : `aPeJE8bSo6rAFoLqg` — « UPDATE (14th Feb 2023): ChatGPT appears to have been patched! »
- **Contre-exemple** (édition de modèle) : `QL7J9wmS6W2fWpofd` — « Before edit: The mother tongue of Jeff Bezos is English »

### G23. Analogie pour le non-spécialiste
- **Question** : le billet rend-il un mécanisme lisible par une analogie hors du sous-domaine ?
- **Modalités** : `présente` ; `absente`
- **Indicateur** : `présente`
- **Analyse** : comparée
- **Règle** : une comparaison explicite avec un domaine extérieur (cerveau, vie courante, autre science), écrite par les auteurs. Le compte « une / plusieurs » du brouillon 1 est retiré.
- **Cas limites** : la comparaison avec une expérience ou une méthode voisine n'est pas une analogie ; une analogie dans un texte de modèle cité ne compte pas ; une analogie en légende compte.
- **Exemple** : `3PaLrzxagpbnNtPLT` — « In a sense, this is similar to how some people “think in words,” without having to say them out loud. »
- **Contre-exemple** (comparaison technique) : `nv8oedrnLXKRzNEL9` — « This is similar to the experiment from Figure 32 of the J-lens paper. »

### G24. Déclaration d'usage d'une intelligence artificielle dans l'écriture
- **Question** : le billet déclare-t-il qu'un modèle de langue a écrit, édité, mis en forme ou résumé une partie du texte ?
- **Modalités** : `déclarée` ; `aucune`
- **Indicateur** : `déclarée`
- **Analyse** : descriptive (la consigne vient de la politique du site, pas de la mesure ; voir `docs/sources/lesswrong-politique-ia-v1/`). Les sous-valeurs « générale », « par partie », « bloc dédié » sont fusionnées : trop rares dans la moitié développement (un seul cas trouvé) pour être départagées.
- **Règle** : coder la déclaration, ne pas deviner un usage.
- **Cas limites** : un modèle objet de l'étude, juge, générateur de données ou agent de recherche n'est pas une aide à l'écriture.
- **Exemple** : `nmxzr2zsjNtjaHh7x` — « Thanks to ChatGPT for formatting help. »
- **Contre-exemple** (modèle juge) : `v7f8ayBxLhmMFRzpa` — « highly effective, as rated by Claude 2 »

### G25. Appel aux retours
- **Question** : le billet demande-t-il explicitement des critiques ou des retours aux lecteurs ?
- **Modalités** : `oui` ; `non`
- **Indicateur** : `oui`
- **Analyse** : comparée
- **Règle** : demande adressée aux lecteurs du billet. La longueur, couplée à cet item au brouillon 1, sort du codage (mesure par programme ; variable d'appariement, donc descriptive).
- **Cas limites** : remerciements pour des retours sur un brouillon → `non` ; « let me know if I missed a reference » → `oui`.
- **Exemple** : `S9xyqRAziRMCcJQmz` — « would really appreciate the feedback. »
- **Exemple** : `aPeJE8bSo6rAFoLqg` — « In the meantime, feedback is welcome, either here or at »
- **Contre-exemple** (remerciements) : `bWxNPMy5MhPnQTzKz` — « Thanks to Marius Hobbhahn and Oam Patel for helpful feedback on drafts. »

---

## B. Classes d'objections des commentaires

**Unité** : un commentaire parmi les dix retenus d'un billet bien noté (vue des mieux notés, réponses comprises). **Une seule classe par commentaire** : la première, dans l'ordre de priorité ci-dessous, que le commentaire **énonce** (et non qu'il laisse deviner). Les classes secondaires du brouillon 1 sont retirées : elles ne se mesurent pas de façon fiable et n'entrent pas dans l'analyse.

**Réponses des auteurs** : marquées par programme (nom affiché du commentateur égal à l'auteur ou à un coauteur du manifeste), montrées pour le contexte avec la mention « ne pas coder », hors typologie. Dans la moitié développement : 80 commentaires sur 296 (`pieces-grille-v2/verification-citations-v2.json`, champ `commentaires`). Limite : un coauteur absent de la liste du site n'est pas reconnu ; le codeur le code alors `O0` s'il se présente comme auteur.

**Ordre de priorité** : O1, O2, O3, O7, O8, O6, O5, O4, O11, O9, O12, O10, O0. Le doute se coche comme pour les gestes.

**Unité de contexte** : le codeur voit le texte du billet et le commentaire parent (s'il est retenu) ; il code ce que le commentaire dit du travail, même s'il répond à un autre lecteur.

### O1. Explication concurrente du résultat
- **Code** : `O1`
- **Définition** : un autre facteur, du dispositif ou général (théorie connue, contamination des données), produirait le même résultat. Fusion des classes 1 et 11 du brouillon 1 (frontière non codable de façon sûre ; même consigne pour le gabarit : anticiper les explications concurrentes).
- **Cas limites** : un facteur nommé sans lien au résultat → O9 ou O0.
- **Exemple** : `8gy7c8GAPkuu6wTiX/5xyCFhwNNapkSXbPT` — « due to the LLMs having been exposed to ideas about scheming AIs and disobedient employees in their training material »
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
- **Définition** : doute, incompréhension ou erreur pointée sur un chiffre, une figure, un calcul, une définition technique ou le code. Fusion des classes 3 et 9 du brouillon 1 (même cible, la vérifiabilité ; la frontière « doute » / « point technique » n'était pas codable).
- **Cas limites** : simple question de sens sans doute → O11.
- **Exemple** : `wtfvbsYjNHYYBmT3k/hPZfgA3BdXieNfFuY` — « I am very confused about some of the reported experimental results. »
- **Exemple** : `47CYFbrSyiJE2X5ot/ntRqbHsSMDD8BCXkK` — « I think this means that the FLOP scaling laws claim is misleading »
- **Exemple** : `mkbGjzxD8d8XqKHzA/4e8534hbyWCpZFgFD` — « when two singular vectors have approximately the same singular value, the two vectors are very numerically unstable (within their span). »
- **Contre-exemple** (question de sens : O11) : `bWxNPMy5MhPnQTzKz/CzXjsuPdLBEvbQyo2` — « What do you mean by "random linear probe"? »

### O4. Antériorité et travaux voisins
- **Code** : `O4`
- **Définition** : le commentaire nomme ou cherche un travail antérieur ou voisin, ou conteste la nouveauté, même sur un ton amical.
- **Exemple** : `aPeJE8bSo6rAFoLqg/r4cYjKb8ozJqthZeK` — « You also may want to checkout Universal Adversarial Triggers »
- **Exemple** : `mkbGjzxD8d8XqKHzA/snXYLcgexytzX5BGo` — « Is applying SVD a new idea in interpretability? »
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
- **Définition** : demande ou suggestion d'une mesure, d'une variante ou d'une figure de plus, sans contester le résultat.
- **Exemple** : `khFC2a4pLPvGtXAGG/v3J5ZdYwz97Rcz9HJ` — « I'm curious how this approach performs at detecting human lies »
- **Exemple** : `xwdRzJxyqFqgXTWbH/kcoWTGfidMgyfFcFs` — « I wonder what would happen if you used a different way of eliciting the model's mental maps of the world. »
- **Contre-exemple** (demande de matériel : O11) : `FF8i6SLfKb4g7C4EL/dHvqjfmcSJPjWbugw` — « It would be great if you could share some code from your experiments. »

### O10. Forme et présentation
- **Code** : `O10`
- **Définition** : remarque argumentée, critique ou éloge, sur l'écriture, la longueur, le titre, les figures ou la manière de présenter les preuves.
- **Exemple** (critique) : `mkbGjzxD8d8XqKHzA/JeKubW3KEzSgvfqnP` — « this felt far too high production value - more posts, shorter posts and lower effort per post plz »
- **Exemple** (éloge argumenté) : `nv8oedrnLXKRzNEL9/CFHaWvrn3xegRZmcQ` — « It has comparison to other models, comparison to baselines, error bars, random control, no graph crimes, and its not in appendix. »
- **Contre-exemple** (éloge sans argument : O0) : `7C4KJot4aN8ieEDoz/2Mjc7Ghh3wkbwLJr6` — « Very good of you to actually follow through on the promises. »

### O11. Demande de précision ou de matériel (classe nouvelle)
- **Code** : `O11`
- **Définition** : question sur ce qui a été fait ou voulu dire, ou demande de code, de données, de détails, sans doute exprimé. Née de la lecture des commentaires de développement v2 : le brouillon 1 rangeait ces questions dans le « doute sur l'exactitude », qui devient O3 et exige un doute.
- **Exemple** : `bWxNPMy5MhPnQTzKz/CzXjsuPdLBEvbQyo2` — « What do you mean by "random linear probe"? »
- **Exemple** : `FF8i6SLfKb4g7C4EL/dHvqjfmcSJPjWbugw` — « It would be great if you could share some code from your experiments. »
- **Contre-exemple** (doute exprimé : O3) : `wtfvbsYjNHYYBmT3k/hPZfgA3BdXieNfFuY` — « I am very confused about some of the reported experimental results. »

### O12. Réplication ou prolongement par le lecteur (classe nouvelle)
- **Code** : `O12`
- **Définition** : le commentateur rapporte une expérience, une réplication ou des données qu'il a faites lui-même à partir du billet. Née de la lecture des commentaires de développement v2 (au moins cinq cas sur 36 billets), absente du brouillon 1.
- **Cas limites** : renvoi à un travail publié du commentateur, sans expérience faite à partir du billet → O4.
- **Exemple** : `HhF5kESdtPHku7kim/zMh7XM5wm68hCSo9b` — « Cool work! I replicated Figure 12 on our model organism »
- **Exemple** : `rbqJoxFZtae9x93mx/FNjFjaGSzbrJnEuHo` — « Funnily enough, I did the exact same thing on the same task two weeks ago and my army of Claude agents found a different solution »
- **Contre-exemple** (travail voisin publié : O4) : `mkbGjzxD8d8XqKHzA/KYa6vs9gRpgYKmE7r` — « In case it’s of interest, we have also performed some exploratory interpretability work using the SVD of model weights. »

### O0. Hors typologie
- **Code** : `O0`
- **Définition** : approbation sans argument, remerciements, curation ou modération par l'équipe du site, humour, lien sans contenu, discussion entre lecteurs qui ne dit rien du travail.
- **Exemple** : `xwdRzJxyqFqgXTWbH/jpDCfcYZsGzTHGjsm` — « Curated. This was wholesome curious fun. »
- **Exemple** : `aPeJE8bSo6rAFoLqg/wcex2xAxovQad4oSL` — « This reads like an SCP, including the use of the word "anomalous". »
- **Contre-exemple** (éloge argumenté : O10) : `nv8oedrnLXKRzNEL9/CFHaWvrn3xegRZmcQ` — « It has comparison to other models, comparison to baselines, error bars, random control, no graph crimes, and its not in appendix. »

Note sur O1 et O3 : l'exemple `HhF5kESdtPHku7kim/zMh7XM5wm68hCSo9b` contient à la fois une réplication et une crainte (« I was somewhat worried that some of the results you see are because the AI did not have a super strong association between misalignment ») : l'ordre de priorité le classe **O1**, pas O12. Il est gardé comme exemple de O12 pour sa première phrase et comme cas d'école de la priorité ; les codeurs le voient dans le protocole.

---

## 4. Protocole de codage (deux codeurs indépendants, moitié tenue à l'écart)

### 4.1 Codeurs
Deux codeurs neufs, ni auteurs de la grille v1 ou v2, ni du tri, ni l'un de l'autre. Ils ne se parlent pas et ne voient jamais les fichiers de l'autre. Un troisième, l'arbitre, neuf lui aussi, tranche les désaccords après dépôt et scellement des deux fichiers. Choix des codeurs : point à trancher (section 9).

### 4.2 Copies neutres (ce qui leur est caché, et comment)
Préparées par `pieces-grille-v2/preparer_copies_neutres_v1.py` (écrit, essayé sur la moitié développement en dossier temporaire supprimé, **jamais exécuté sur la tenue à l'écart** ; le script refuse la tenue à l'écart sans un identifiant de GO en argument, et ce refus est testé avant toute lecture). Il retire ou masque :
- score, nombre de votants, nombre de commentaires, date, étiquettes, statut bien noté ou peu noté, appariement, adresse du billet, auteur (champs du manifeste : jamais copiés) ;
- les noms de l'auteur et des coauteurs du manifeste dans le texte (remplacés par `[AUTEUR]`) ;
- les adresses des liens et des images : un lien devient `texte [lien : hôte]`, une image `[IMAGE n : texte de remplacement]` ; les éléments interactifs (`widget`) deviennent `[ÉLÉMENT INTERACTIF]` ;
- l'identifiant du site, remplacé par un identifiant neutre tiré au hasard (graine ci-dessous) ;
- l'ordre : chaque codeur reçoit sa propre liste d'ordre de lecture, tirée au hasard, les deux membres d'une paire n'étant pas adjacents (rejet et nouveau tirage, au plus 1 000 fois, sinon arrêt signalé).
Il insère la borne `⟦FIN DE L'EN-TÊTE — 250 MOTS⟧` après le 250e mot du corps neutre (mots = suites séparées par des blancs, marqueurs exclus).
Pour les commentaires (seconde passe seulement) : nom du commentateur, score, votes, date retirés ; réponses d'auteur marquées « ne pas coder » ; ordre mélangé au hasard (l'ordre d'origine suit le score) ; lien vers le parent par identifiant neutre ; parent non retenu signalé.
La table de correspondance (identifiant neutre → identifiant du site) est écrite dans un dossier séparé `cles/`, jamais remis aux codeurs.
Graine : `numpy.random.SeedSequence(159121083548737780390099018299333639900)` ; enfants par `spawn(3)` dans cet ordre : identifiants neutres, ordre du codeur 1, ordre du codeur 2 ; mélange des commentaires par un enfant de l'enfant 0 par billet, dans l'ordre lexical des identifiants neutres.
Fuite résiduelle, dite d'avance : notes d'édition (« many people said… »), mentions de revues annuelles ou de curation dans le texte, notoriété d'un laboratoire nommé, sujet. Elles ne sont pas retirées (on toucherait au geste mesuré).

### 4.3 Deux passes
1. **Gestes** : les 62 billets de la tenue à l'écart, lecture intégrale de chaque copie neutre, grille section A, dans l'ordre propre au codeur. Le fichier est déposé et scellé avant la seconde passe.
2. **Objections** : les commentaires retenus des 39 bien notés de la tenue à l'écart (dix au plus par billet), avec la copie neutre du billet pour contexte, grille section B. Cette passe révèle quels billets sont bien notés : c'est pourquoi elle vient après le scellement de la première.

### 4.4 Ce que lisent les codeurs
La grille brouillon 2 gelée (version scellée qui suivra ce brouillon), ce protocole, leur dossier de copies neutres, leur liste d'ordre. Rien d'autre : ni manifeste, ni métadonnées, ni le site (aucune requête, aucun lien suivi), ni la moitié développement au-delà des exemples de la grille.

### 4.5 Format de sortie
Un fichier par codeur et par passe, en lignes JSON (une ligne par billet et par geste ; une ligne par commentaire) :
- gestes : `{"codeur": "C1", "billet": "<neutre>", "geste": "G01", "modalite": "<valeur exacte de la grille>", "appui": "<≤ 25 mots ou vide>", "doute": false}` — 62 × 25 = 1 550 lignes attendues ;
- objections : `{"codeur": "C1", "billet": "<neutre>", "commentaire": "<neutre>", "classe": "O3", "appui": "…", "doute": false}`.
Un contrôle par programme (dans `analyser_codage_v1.py`) refuse un fichier incomplet, une modalité absente de la grille, un doublon : aucun repli silencieux.

### 4.6 Arbitrage
L'arbitre voit les deux codages en désaccord et la copie neutre, jamais le statut des billets ; il choisit une des deux modalités (pas de troisième) et écrit un motif d'une ligne. Les fréquences de la section 5 portent sur le codage arbitré ; les codages bruts de chaque codeur sont rapportés en sensibilité.

## 5. Plan d'analyse, écrit avant tout codage

Implémenté par `pieces-grille-v2/analyser_codage_v1.py`, qui lit les modalités et indicateurs **dans ce fichier** (la grille est la seule source) ; essayé seulement sur des codages synthétiques tirés au hasard (`essai-analyse-synthetique-v1.json`), jamais sur un codage réel.

### 5.1 Ensembles
- **Tenue à l'écart** : 62 billets ; 39 bien notés dont 16 sans apparié ; 23 paires.
- **Marquage 1, billets déjà lus pour la grille v1** : 18 billets (`pieces-grille-v2/billets-marques-v1.json`), dont 12 bien notés, 6 appariés, 3 bien notés sans apparié ; 10 paires touchées, 13 intactes.
- **Marquage 2, désaccord des deux lecteurs du tri** : 4 billets de la tenue (`marques-desaccords-second-lecteur-v1.json`, `78234d6d…`).
- Chaque résultat est rapporté sur quatre ensembles : **tous** ; **sans marquage 1** ; **sans marquage 2** ; **sans leur réunion**. Une paire est retirée si l'un de ses membres est retiré.

### 5.2 Fiabilité par geste
- Sur le couple de codages bruts (avant arbitrage), pour chaque geste : accord brut et kappa de Cohen sur les modalités complètes, puis sur l'indicateur binaire ; intervalle à 95 % par rééchantillonnage des billets (10 000 tirages, percentile).
- **Seuil, fixé ici** : un geste est **fiable** si le kappa de l'indicateur est ≥ 0,60 sur les 62 billets **et** sur les billets hors marquage 1 (44). Exception écrite d'avance : si la prévalence de l'indicateur (deux codeurs réunis) dépasse 90 % ou est sous 10 %, le kappa est instable ; le geste est alors fiable si l'accord brut est ≥ 0,90 (prévalence haute) et **non évaluable** (prévalence basse, rare : rapporté, jamais consigne).
- Un geste non fiable est rapporté comme tel et exclu du gabarit ; il n'est jamais redéfini puis recodé sur la même moitié.
- Objections : kappa sur la classe principale (13 modalités), puis kappa binaire par classe ; même seuil 0,60 ; une classe sous le seuil n'entre pas au gabarit.

### 5.3 Fréquences et différence appariée (gestes fiables, analyse « comparée »)
- Fréquence de l'indicateur chez les 39 bien notés, chez les 23 appariés, chez les 16 bien notés sans apparié (rapportée à part, hors comparaison).
- Différence appariée `d = moyenne sur les paires de (indicateur du bien noté − indicateur de l'apparié)`, intervalle à 95 % par rééchantillonnage des **paires** (10 000 tirages, percentile) ; intervalle ajusté de Bonferroni (niveau 1 − 0,05 / m) rapporté à côté.
- Test : signe exact sur les paires discordantes (équivalent au test de McNemar exact), bilatéral.
- **Multiplicité** : m = nombre de gestes fiables d'analyse « comparée » (au plus 23 : les gestes G22 et G24 sont descriptifs). Correction de Holm au niveau familial 0,05 sur les m valeurs p. Puissance faible, dite d'avance : avec 23 paires, seule une différence d'au moins 0,4 environ a une chance raisonnable de passer ; un résultat nul est le résultat attendu et ne dit pas « pas d'effet ».
- **Graines** : `numpy.random.SeedSequence(17963430407690202368587404665739133625)` ; `spawn(4)` : un enfant par ensemble de la section 5.1 dans l'ordre écrit ; chaque enfant `spawn(27)` : un petit-enfant par geste G01…G25 dans l'ordre, le 26e pour la fiabilité, le 27e pour les objections ; `numpy.random.default_rng` ; version de numpy consignée (2.4.6 à l'écriture).
- Sensibilités : codeur 1 seul, codeur 2 seul ; quatre ensembles.

### 5.4 Objections
Descriptives (pas de comparaison possible : seuls les bien notés ont des commentaires retenus) : part de chaque classe parmi les commentaires codables (hors réponses d'auteur), intervalle par rééchantillonnage des billets (grappes) ; part des billets ayant au moins un commentaire de la classe. Liens entre gestes et objections : exploratoires, signalés comme tels, jamais au gabarit.

### 5.5 Ce que l'analyse ne peut pas dire
- Le score dépend de l'auteur, de son audience, du laboratoire, de la promotion par l'équipe du site, de la date et du sujet ; l'appariement tient l'année, une étiquette et la longueur, pas l'auteur ni le sujet. Une différence n'est pas un effet de la rédaction.
- 45 paires en tout, 23 dans la tenue à l'écart, 13 hors marquage 1 ; 2022 n'a que 3 appariés dans tout le corpus.
- Un seul site, neuf étiquettes, billets rejetés par la modération exclus ; textes au jour du tirage, édités après coup pour certains.
- Le tri à la lecture est imparfait : sur 100 décisions relues en aveugle par un second lecteur, accord brut 0,972 (kappa 0,941, 72 lignes tirées au hasard) mais 0,679 (kappa 0,241, 28 lignes) sur les cas que le premier lecteur disait serrés ; six billets du corpus sont en désaccord (marquage 2). Le second lecteur demande que la règle de tri précise la mesure de « plus de la moitié du corps », ce qu'est une figure de résultat (captures de sorties de modèle) et le cas du modèle jouet simulé (`rapport-second-lecteur-v1.md`, section 4).
- Les codeurs ne voient pas les images ; les gestes visuels sont mesurés sur les légendes.
- La grille a été écrite sur la moitié développement : les gestes choisis sont ceux qu'on voit dans ces billets ; les codeurs, s'ils sont des modèles, peuvent partager les biais du réviseur.
- Le tirage des bien notés suit le score : la comparaison porte sur le haut et le bas d'un genre déjà filtré, pas sur le genre.

## 6. Exemples du brouillon 1 retirés ou remplacés

Tous les exemples dont le billet n'est pas dans la moitié développement v2 sont retirés (règle du mandat). Billets cités au brouillon 1 :
- **Passés en tenue à l'écart v2 (12, tous dans le marquage 1)** : `LBaTQGD5KyXcbTtKt`, `NNGB77BipWpHn4vRW`, `PJuwj7fDpvj2opLTe`, `bhvaAbSPZgiG3oJPu`, `Qryk6FqjtZk9FHHJR`, `THzcKKQd4oWkg4dSP`, `cNDJuXNZ8MrkPZNzj`, `d8xDGzCEYE639qqEv`, `dLg7CyeTE4pqbbcnp`, `ghESoA8mo3fv9Yx3E`, `hzt9gHpNwA2oHtwKX`, `jGuXSZgv6qfdhMCuJ`, `jfG6vdJZCwTQmG7kb`, `nc9dHfcB22JdMzGbr`, `njAZwT8nkHnjipJku`, `sHpZZnRDLg7ccX9aF`, `xtpcJjfWhn3Xn8Pu5` (17 identifiants : 12 bien notés, 4 appariés peu notés, plus `bhva…` apparié — tous en tenue à l'écart v2) ;
- **Absents du corpus v2 (5)** : `LzeZW9PvR6Njc9ngr`, `YydYPCsZJJEwnCMe7`, `buyCkzfa2J3Dso6tz`, `nWiwv4GN8aYqpnZKE`, `nfGZtKzz8WzxF3MAs`.
- **Gardés car en développement v2** : citations de `M5vEjix8oPeWXeGFY`, `zj3GKWAnhPgTARByB`, `7C4KJot4aN8ieEDoz`, `8gy7c8GAPkuu6wTiX`, `SieLowPgNgRSPGhFw`, `d9FJHawgkiMSPjagR`, `khFC2a4pLPvGtXAGG`, `mkbGjzxD8d8XqKHzA`, `wSKPuBfgkkqfTpmWJ`, `wtfvbsYjNHYYBmT3k`, `z6QQJbtpkEAX3Aojj` reprises quand elles servent la nouvelle question, revérifiées contre le texte v2. `jDfjqu2qJLcPco9cf` n'est plus cité.

(Correction du décompte ci-dessus : 17 identifiants passés en tenue à l'écart v2 ; ils sont tous dans le marquage 1, qui en compte 18 — le 18e, `xE3Y9hhriMmL4cpsR`, n'était pas cité.)

## 7. Vérification des citations
`pieces-grille-v2/verifier_citations_v2.py` lit ce fichier, extrait chaque citation, et vérifie : billet dans la moitié développement v2 (manifeste) ; billet hors des deux marqués du marquage 2 ; présence exacte dans le texte (ou dans le titre si `(titre)`) ou dans le commentaire nommé, après la normalisation du brouillon 1 (liens réduits à leur texte, `* _ \` et blancs multiples ôtés) ; 25 mots au plus ; commentaire retenu et non écrit par un auteur ; chaque geste et chaque classe a au moins un exemple et un contre-exemple vérifiés ; chaque geste a ses modalités, son indicateur (inclus dans les modalités) et son statut d'analyse. Il lit **seulement** `/home/user/billets-corpus-v2/developpement/`. Sortie : `pieces-grille-v2/verification-citations-v2.json`.

## 8. Du geste mesuré à la consigne du gabarit (règle écrite avant le codage)

Un geste devient une **consigne** du gabarit de billet si, sur le codage arbitré de la tenue à l'écart :
1. il est **fiable** (section 5.2) ;
2. son analyse est « comparée » (G22 et G24 en sont exclus : la note d'édition suit l'audience, la déclaration d'usage d'une intelligence artificielle relève de la politique du site, qui l'impose de toute façon si un modèle a écrit) ;
3. son indicateur est présent chez **au moins la moitié des 39 bien notés** de la tenue à l'écart ;
4. la différence appariée `d` est **≥ 0** sur les 23 paires **et** sur les paires hors réunion des deux marquages.

Qualificatifs : **consigne distinctive** si de plus `d > 0` après correction de Holm ; **consigne sous réserve** si le point 4 tient sur un seul des deux ensembles ; **à éviter** si `d < 0` après correction de Holm, quel que soit le point 3 ; **piste** (jamais consigne) si 1 et 2 tiennent, le point 3 non, et la borne basse de l'intervalle non ajusté de `d` est > 0.
Une classe d'objection devient une **objection à prévenir** dans le gabarit si elle est fiable (kappa binaire ≥ 0,60), compte pour au moins 10 % des commentaires codables et touche au moins un quart des 39 bien notés.
Le gabarit cite pour chaque consigne la fréquence chez les bien notés, `d` et son intervalle, et l'ensemble sur lequel elle tient. Aucune consigne ne vient de la moitié développement.

## 9. Points à trancher (pour la session mère)
1. **Qui code** : deux agents neufs d'un même modèle, ou au moins un d'une autre lignée (ou une personne). Recommandation : deux agents neufs de deux modèles différents, arbitre neuf ; confiance moyenne.
2. **Images invisibles** aux codeurs : accepter (recommandé, confiance moyenne) ou leur fournir les images (téléchargement depuis l'hébergeur d'images du site, hors du mandat actuel).
3. **Seuil de fiabilité** à 0,60 (recommandé) ou 0,70 (plus sûr, plus de gestes perdus).
4. **Classes nouvelles** O11 et O12 et fusions O1, O3 : à confirmer avant gel.
5. **Gel** : contre-lecture de ce brouillon par un agent neuf sur la moitié développement avant scellement de la version gelée (règle de contre-lecture du dépôt).

## Pièces
Sous `docs/notes/billets-v1/pieces-grille-v2/`, chacune avec son compagnon `.sha256` : `marquer_billets_lus_v1.py` et `billets-marques-v1.json` ; `verifier_citations_v2.py` et `verification-citations-v2.json` ; `preparer_copies_neutres_v1.py` et `essai-copies-neutres-dev-v1.json` (essai sur la moitié développement, copies supprimées) ; `analyser_codage_v1.py` et `essai-analyse-synthetique-v1.json`.
