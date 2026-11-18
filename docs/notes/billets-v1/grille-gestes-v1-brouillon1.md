# Grille des gestes de rédaction et typologie des objections — v1, brouillon 1

Tâche 4 du mandat `docs/notes/billets-v1/mandat-corpus-et-grille-v1.md`. Tirée de la **seule moitié « développement »** du corpus (`manifeste-corpus-v1.json`, champ `moitie`), soit 65 billets (40 bien notés, 25 appariés peu notés) et les commentaires retenus des 40 bien notés. La moitié « tenue à l'écart » n'a pas été ouverte (dossier sans droits de lecture depuis le partage).

**Statut : brouillon, non gelé.** Les définitions et règles sont à éprouver par deux codeurs indépendants sur la moitié tenue à l'écart avant gel (voir le rapport). Les exemples viennent de billets que la lecture de contrôle a jugés vraiment « résultats empiriques », sauf mention contraire (item sur l'usage d'une intelligence artificielle).

**Format des exemples** : identifiant du billet (adresse `https://www.lesswrong.com/posts/<identifiant>`), puis citation de 25 mots au plus, en anglais, telle qu'elle figure dans le texte (balises de mise en forme et adresses de liens ôtées). Chaque citation a été vérifiée par programme contre le texte tiré (`scripts/verifier_citations_v1.py`) : présence exacte et 25 mots au plus. Pour les objections : `billet/commentaire`.

**Unité de codage** : le billet entier tel que publié (version du tirage du 2026-11-18). « En tête » = les 250 premiers mots du corps, remerciements compris.

---

## A. Gestes de rédaction (25 items)

### A1. Forme du titre
- **Définition** : ce que le titre dit du résultat.
- **Valeurs** : `affirmation` (le résultat est énoncé) ; `affirmation-atténuée` (may, might, could, appear) ; `question` ; `nom-de-méthode-ou-d-objet` (sans résultat) ; `jeu-de-mots-ou-formule`.
- **Règle** : coder le titre seul, sans sous-titre du corps ; si plusieurs formes, la forme du segment principal (avant les deux-points) ; une question rhétorique dont la réponse est dans le titre reste `question`.
- **Exemples** : `jGuXSZgv6qfdhMCuJ` — « Refusal in LLMs is mediated by a single direction » (`affirmation`) ; `sHpZZnRDLg7ccX9aF` — « Weight-Sparse Circuits May Be Interpretable Yet Unfaithful » (`affirmation-atténuée`) ; `ghESoA8mo3fv9Yx3E` — « Why Do Some Language Models Fake Alignment While Others Don't? » (`question`).

### A2. Place de la thèse
- **Définition** : position de la première phrase qui énonce le résultat principal du billet.
- **Valeurs** : `première-phrase` ; `premier-paragraphe` ; `en-tête-après-contexte` (dans les 250 premiers mots, après mise en contexte) ; `plus-loin` ; `absente`.
- **Règle** : une question d'accroche ne compte pas comme thèse ; une liste de résultats en tête compte ; si la thèse n'apparaît qu'après l'introduction, `plus-loin`.
- **Exemples** : `njAZwT8nkHnjipJku` — « What happens when you tell Claude it is being trained to do something it doesn't want to do? » (accroche, thèse dans la phrase suivante : `premier-paragraphe`) ; `d8xDGzCEYE639qqEv` — « We show it comes down to how LLMs perceive roles (the humble chat template tags). » (`première-phrase` du résumé).

### A3. Forme de la thèse
- **Définition** : nature de l'énoncé de thèse repéré en A2.
- **Valeurs** : `chiffrée` (au moins un nombre de résultat) ; `qualitative-affirmative` ; `qualitative-atténuée` ; `négative` (« X ne marche pas / n'est pas ») ; `sans-objet` (A2 = absente).
- **Règle** : `chiffrée` prime sur les autres ; `négative` si le résultat principal est un échec ou une réfutation.
- **Exemples** : `NNGB77BipWpHn4vRW` — « code validity (96% accuracy) > grammaticality (93%, cross-lingual) > basic arithmetic (76%, addition only) » (`chiffrée`) ; `wtfvbsYjNHYYBmT3k` — « we think it is unlikely to be directly helpful for implementations of alignment strategies (>95%) » (`négative`).

### A4. Résumé en tête
- **Définition** : bloc qui résume le billet avant le développement.
- **Valeurs** : `aucun` ; `tldr-court` (≤ 80 mots) ; `tldr-long` ; `résumé-à-puces` ; `résumé-en-une-phrase` ; `résumé-du-papier-copié`.
- **Règle** : chercher dans les 250 premiers mots un bloc étiqueté (TL;DR, Summary, Executive summary, One-sentence summary, Abstract) ou une liste de résultats ; un « Abstract » cité d'un papier = `résumé-du-papier-copié`.
- **Exemples** : `dLg7CyeTE4pqbbcnp` — « One-sentence summary: On a dataset of human-written essays, we find that gpt-3.5-turbo can accurately infer demographic information about the authors » ; `z6QQJbtpkEAX3Aojj` — « TL;DR: Recent results from Anthropic suggest that neural networks represent features in superposition. »

### A5. Chiffre de résultat en tête
- **Définition** : au moins un nombre de résultat (pas un nombre de contexte, ni une taille de modèle) dans les 250 premiers mots.
- **Valeurs** : `oui-avec-base` (le chiffre est comparé à une base) ; `oui-seul` ; `non`.
- **Règle** : une taille de jeu de données ou de modèle ne compte pas ; un pourcentage de réussite, une aire sous la courbe, un taux comptent.
- **Exemples** : `nc9dHfcB22JdMzGbr` — « we read workspace representations with 55% success on latent variable extraction tasks (J-Lens: 36%, R-Lens: 38%) » (`oui-avec-base`) ; `NNGB77BipWpHn4vRW` — même citation qu'en A3 (`oui-seul`).

### A6. Statut épistémique
- **Définition** : déclaration explicite de la confiance des auteurs ou des conditions du travail.
- **Valeurs** : `absent` ; `statut-étiqueté` (« Epistemic status ») ; `crédences-chiffrées` (probabilités attachées aux affirmations) ; `réserve-libre` (sans étiquette).
- **Règle** : `crédences-chiffrées` dès qu'une probabilité est attachée à une affirmation des auteurs ; sinon `statut-étiqueté` si l'étiquette existe.
- **Exemples** : `M5vEjix8oPeWXeGFY` — « Epistemic Status: Confident only in these particular results. » ; `cNDJuXNZ8MrkPZNzj` — « Epistemic status: Most experiments were run over a period of ~2-3 days during a hackathon at UK AISI, and were fairly heavily vibe coded. »

### A7. Degré d'achèvement annoncé
- **Définition** : ce que le billet dit de sa maturité.
- **Valeurs** : `non-dit` ; `rapport-intermédiaire` ; `travail-rapide` (sprint, hackathon, projet de cours) ; `papier-complet`.
- **Règle** : coder l'annonce explicite, pas le jugement du codeur.
- **Exemples** : `z6QQJbtpkEAX3Aojj` — « We decided to post this primarily to spread the knowledge that no fancy sparse coding methods are needed to recover ground truth features » (`rapport-intermédiaire`) ; `jDfjqu2qJLcPco9cf` — « rather than wait for everything to be finished before sharing the results that I do have, I figured that it would be best » (`rapport-intermédiaire`).

### A8. Rapport au papier
- **Définition** : lien entre le billet et une publication écrite ailleurs.
- **Valeurs** : `autonome` ; `copie-de-l-introduction` ; `résumé-des-points-clés` ; `complément` (ce que le papier ne dit pas) ; `lien-seul`.
- **Règle** : d'après la déclaration des auteurs en tête ; à défaut, `autonome` s'il n'y a pas de papier cité comme source du travail.
- **Exemples** : `khFC2a4pLPvGtXAGG` — « This post is a copy of the introduction of this paper on lie detection in LLMs. » ; `8gy7c8GAPkuu6wTiX` — « This is a brief summary of what we believe to be the most important takeaways from our new paper » (`résumé-des-points-clés`).

### A9. Contexte de production
- **Définition** : institution, programme ou encadrement nommé.
- **Valeurs** : `aucun` ; `institution` ; `programme-de-formation` ; `encadrement-nommé` ; plusieurs valeurs possibles.
- **Règle** : relever tout ce qui figure en tête ou en pied de billet.
- **Exemples** : `jGuXSZgv6qfdhMCuJ` — « This work was produced as part of Neel Nanda's stream in the ML Alignment & Theory Scholars Program » ; `THzcKKQd4oWkg4dSP` — « This work was produced at Apollo Research, based on initial research done at MATS. »

### A10. Enjeu de sûreté explicite
- **Définition** : phrase qui dit pourquoi le résultat compte pour la sûreté.
- **Valeurs** : `en-tête` ; `plus-loin` ; `absent`.
- **Règle** : il faut un lien explicite entre le résultat et un risque ou un usage de sûreté ; « intéressant » ne suffit pas.
- **Exemples** : `SieLowPgNgRSPGhFw` — « If models can do extensive reasoning without outputting any CoT, it would have implications for safety. » ; `YydYPCsZJJEwnCMe7` — « When a model gives a misleading explanation of its behaviour, users build incorrect mental models, which can lead to misplaced trust in systems »

### A11. Figures et tableaux
- **Définition** : présence, place et légende des figures et tableaux de résultat.
- **Valeurs** : nombre (entier) ; `figure-en-tête` (oui/non, dans les 250 premiers mots) ; `légendes` (`numérotées` / `libres` / `aucune`) ; `figure-décorative` (oui/non : image sans donnée).
- **Règle** : une image générée ou un mème sans donnée est `figure-décorative` ; un tableau compte comme figure.
- **Exemples** : `z6QQJbtpkEAX3Aojj` — « Figure 1: Mean Max Cosine Similarity between the learned dictionary and the ground truth features for varying L1 penalties. » (`numérotées`) ; `khFC2a4pLPvGtXAGG` — « Our lie dectector in meme form. » (figure en tête, schéma du dispositif sous forme de mème).

### A12. Bases de comparaison
- **Définition** : ce à quoi le résultat principal est comparé.
- **Valeurs** : `aucune` ; `hasard-ou-trivial` ; `base-naïve-nommée` ; `méthode-concurrente` ; `plafond` (« skyline », supervision complète).
- **Règle** : coder la base la plus forte présente ; une base citée seulement en commentaire ne compte pas.
- **Exemples** : `dLg7CyeTE4pqbbcnp` — « We're comparing to a baseline model that simply returns the population distribution » (`base-naïve-nommée`) ; `zj3GKWAnhPgTARByB` — « We set out to compute a "skyline" for SAE performance » (`plafond`) ; `LzeZW9PvR6Njc9ngr` — « It scores 80.8% in experiments where the order is the only determinant of the final state (versus a maximum of 60.4% for any order-blind method) ».

### A13. Justification des choix
- **Définition** : énoncé de la forme « nous avons choisi X parce que Y », avec ou sans alternatives.
- **Valeurs** : `aucune` ; `choix-justifié` ; `choix-justifié-avec-alternatives` (l'alternative est nommée).
- **Règle** : il faut le choix, la raison et (pour la seconde valeur) l'option écartée ; compter le nombre d'occurrences.
- **Exemples** : `d9FJHawgkiMSPjagR` — « We implement trusted labor with GPT-4 instead of humans because GPT-4 is cheaper. » (`avec-alternatives`) ; `zj3GKWAnhPgTARByB` — « We chose the IOI task, as it's perhaps the most well-studied example of a non-trivial narrow capability in a real-world LLM » (`choix-justifié`).

### A14. Dispositif décrit
- **Définition** : précision du dispositif (modèle, données, effectifs, procédure).
- **Valeurs** : `reproductible` (modèle, données et effectifs nommés) ; `partiel` ; `renvoi-au-papier`.
- **Règle** : `reproductible` exige les trois éléments dans le billet ; un lien vers le papier sans description = `renvoi-au-papier`.
- **Exemples** : `LzeZW9PvR6Njc9ngr` — « We check whether a small model (Qwen2.5-1.5B) internally tracks its state in a simple DFA (modelled after a login protocol) » ; `hzt9gHpNwA2oHtwKX` — « We pre-train the agents on 25k episodes where the blue agent is incentivized to deceive to produce the deceptive baseline »

### A15. Incertitude statistique
- **Définition** : expression de l'incertitude des chiffres.
- **Valeurs** : `aucune` ; `effectifs-donnés` ; `intervalles-ou-barres` ; `test-statistique`.
- **Règle** : coder la valeur la plus forte ; des effectifs à côté des proportions suffisent pour `effectifs-donnés`.
- **Exemples** : `PJuwj7fDpvj2opLTe` — « the accept share measured on 39 calls drops from 0.59 to 0.37 » (`effectifs-donnés`) ; `M5vEjix8oPeWXeGFY` — « Some of the t-tests (Tests 3-5) violate the assumption of equal variances » (`test-statistique`, avec sa réserve).

### A16. Non-revendications explicites
- **Définition** : énoncé de ce que le travail ne montre pas.
- **Valeurs** : `absentes` ; `phrase-isolée` ; `section-dédiée`.
- **Règle** : il faut une négation portant sur la portée du résultat (« does not show », « we did NOT show ») ; une limite technique relève de A17.
- **Exemples** : `8gy7c8GAPkuu6wTiX` — « We also specifically clarify what we think we did NOT show. » (`section-dédiée`) ; `njAZwT8nkHnjipJku` — « However, our research does not show that dangerous alignment faking behavior will necessarily emerge. » (`phrase-isolée`).

### A17. Limites
- **Définition** : énoncé des faiblesses du dispositif ou des données.
- **Valeurs** : `absentes` ; `dispersées` ; `section-dédiée` ; `renvoi-au-papier`.
- **Règle** : une section titrée « Limitations » ou équivalent = `section-dédiée` ; compter aussi le nombre de limites énoncées.
- **Exemples** : `cNDJuXNZ8MrkPZNzj` — « We only tested across one model family (Qwen3) and at a fairly small scale. » ; `bhvaAbSPZgiG3oJPu` — « The labels are judged by one LLM (Claude Opus 5) and we did not read all of them. »

### A18. Résultats négatifs et impasses
- **Définition** : rapport de ce qui n'a pas marché.
- **Valeurs** : `absents` ; `mentionnés` ; `section-dédiée` ; `résultat-principal-négatif`.
- **Règle** : `résultat-principal-négatif` si A3 = `négative` ; sinon selon la place des impasses.
- **Exemples** : `nWiwv4GN8aYqpnZKE` — « Here’s what I tried that didn’t work » (`section-dédiée`) ; `nc9dHfcB22JdMzGbr` — « In this section we discuss various null results that we encountered during our experiments to aid other researchers » (`section-dédiée`).

### A19. Objections anticipées
- **Définition** : objection ou explication concurrente posée par les auteurs, suivie d'un contrôle.
- **Valeurs** : `aucune` ; `posée-sans-contrôle` ; `posée-et-contrôlée` ; `sections-en-questions` (intertitres formulés comme objections).
- **Règle** : `posée-et-contrôlée` exige une expérience ou une analyse en réponse.
- **Exemples** : `dLg7CyeTE4pqbbcnp` — « One concern is that this older data may appear in the GPT-3.5 training data. As a check on that, we also pulled data » ; `7C4KJot4aN8ieEDoz` — « One concern is that our results might be sensitive to wording. To partially address this concern, we test another wording »

### A20. Questions ouvertes et suite
- **Définition** : questions laissées ouvertes ou travaux suivants proposés.
- **Valeurs** : `absentes` ; `suite-des-auteurs` ; `appel-aux-autres` ; `liste-de-questions`.
- **Règle** : `appel-aux-autres` si l'invitation vise d'autres chercheurs.
- **Exemples** : `LBaTQGD5KyXcbTtKt` — « I close with a few open questions that this investigation raised » (`liste-de-questions`) ; `d9FJHawgkiMSPjagR` — « But we’d be excited to see future work that focuses on the problem of constructing expensive auditing processes. » (`appel-aux-autres`).

### A21. Code, modèles et données
- **Définition** : liens vers le code, les poids ou les données.
- **Valeurs** : `aucun` ; `promis` ; `code` ; `code-et-données` ; `carnet-interactif`.
- **Règle** : un lien effectif vers un dépôt, un carnet ou un hébergeur de modèles ; une promesse sans lien = `promis`.
- **Exemples** : `mkbGjzxD8d8XqKHzA` — « A GitHub repository with the colab notebook and accompanying data can be found here. » ; `THzcKKQd4oWkg4dSP` — « Here’s a Hugging Face link to a GPT2-small model without any LayerNorm. »

### A22. Mises à jour et errata visibles
- **Définition** : note d'édition ajoutée après publication.
- **Valeurs** : `aucune` ; `mise-à-jour` (lien, papier paru) ; `erratum` (correction d'un résultat).
- **Règle** : `erratum` si la note dit que des résultats ont changé.
- **Exemples** : `M5vEjix8oPeWXeGFY` — « which fixed a crucial bug and significantly changed the results. » (`erratum`) ; `khFC2a4pLPvGtXAGG` — « EDIT: Many people said they found the results very surprising. » (`mise-à-jour`).

### A23. Analogie pour le non-spécialiste
- **Définition** : image ou analogie qui rend le mécanisme lisible hors du sous-domaine.
- **Valeurs** : `aucune` ; `une` ; `plusieurs`.
- **Règle** : une analogie explicite (« This is like », comparaison filée) ; un exemple technique n'en est pas une.
- **Exemples** : `d8xDGzCEYE639qqEv` — « This is like identifying a stranger's profession from how they talk and dress rather than by checking their ID. » ; `wSKPuBfgkkqfTpmWJ` — « Instead of judging AIs by their apparent behaviors—as Lear did with his daughters—we could look deeper »

### A24. Déclaration d'usage d'une intelligence artificielle
- **Définition** : déclaration de ce qu'un modèle de langue a écrit, édité ou calculé (voir la politique du site, `docs/sources/lesswrong-politique-ia-v1/`).
- **Valeurs** : `aucune` ; `déclaration-générale` ; `déclaration-par-partie` (quelle partie, quel modèle) ; `contenu-en-bloc-dédié`.
- **Règle** : coder ce que dit le billet ; ne pas deviner un usage non déclaré.
- **Exemples** : `bhvaAbSPZgiG3oJPu` — « TL;DR was drafted by Fable 5.1 for compactness and rewritten by me. » (`déclaration-par-partie`) ; `nfGZtKzz8WzxF3MAs` — « I used language models (Claude sonnet 4, GPT-4o) to help edit grammar and clarity after writing my ideas » (`déclaration-générale` ; billet classé « résultats » par le programme mais jugé non empirique à la lecture de contrôle — seul autre exemple de la moitié développement).

### A25. Longueur et adresse au lecteur
- **Définition** : longueur du corps (nombre de mots donné par le site) et appel explicite aux retours.
- **Valeurs** : longueur en classes `< 1500`, `1500–4000`, `4000–8000`, `> 8000` ; appel aux retours `oui`/`non`.
- **Règle** : nombre de mots du site (`nombre_de_mots_site` du manifeste) ; appel = demande explicite de critique ou de retour.
- **Exemples** : `buyCkzfa2J3Dso6tz` (1460 mots) — « feedback on methodology and framing is very welcome. » ; `z6QQJbtpkEAX3Aojj` (6662 mots) — « as well as to elicit early feedback on our work. »

---

## B. Typologie des objections des commentaires (12 classes, plus une classe hors typologie)

**Unité** : un commentaire parmi les dix mieux notés d'un billet bien noté. **Règle générale** : une classe principale par commentaire, celle de la demande principale adressée aux auteurs ; classes secondaires permises. Les réponses des auteurs sont codées `réponse-d-auteur`, hors typologie. Un commentaire sans demande ni critique va en B0.

### B1. Explication concurrente du résultat
- **Définition** : un autre facteur du dispositif pourrait produire le même résultat.
- **Règle** : le commentaire nomme un facteur précis du dispositif (consigne, données, saturation).
- **Exemples** : `ghESoA8mo3fv9Yx3E/K8HrtbiaQkXsn8quy` — « I'd guess 3 Opus and 3.5 Sonnet fake alignment the most because the prompt was optimized to get them to fake alignment. » ; `ghESoA8mo3fv9Yx3E/zEiBPtpby7hp7vBkr` — « I wonder if the observed lack of alignment faking is actually due to the refusal rate being "saturated". »

### B2. Le dispositif ne mesure pas ce qu'il prétend
- **Définition** : doute sur la validité de la mesure elle-même (construit), et non sur un facteur parasite.
- **Règle** : la critique porte sur le lien entre la mesure et le concept revendiqué.
- **Exemples** : `hzt9gHpNwA2oHtwKX/YsD34KoKtSNznBqGG` — « I don't understand how the experimental setup provides evidence for self-other overlap working. » ; `ghESoA8mo3fv9Yx3E/oqRjN7rPjTHzWMXpH` — « I don't believe that chain-of-thought reasoning accurately reflects the model's thoughts. »

### B3. Doute sur l'exactitude ou résultat surprenant
- **Définition** : le lecteur ne comprend pas ou ne croit pas un chiffre ou une figure.
- **Règle** : la critique vise un chiffre, une figure ou une section précise, sans proposer d'explication concurrente (sinon B1).
- **Exemples** : `wtfvbsYjNHYYBmT3k/hPZfgA3BdXieNfFuY` — « I am very confused about some of the reported experimental results. » ; `SieLowPgNgRSPGhFw/B2A4zgW7k6gDt33bW` — « I find the data in the left half of figure 2 surprising. »

### B4. Antériorité et travaux non cités
- **Définition** : un travail antérieur ou voisin n'est pas cité, ou la nouveauté est contestée.
- **Règle** : le commentaire nomme ou cherche un travail antérieur.
- **Exemples** : `Qryk6FqjtZk9FHHJR/zpySAKDWbgCJ2sFSv` — « Did you try searching for similar ideas to your work in the broader academic literature? » ; `cNDJuXNZ8MrkPZNzj/kyDhKWMytTxKWGqGC` — « I believe the post from Anima lab "Persistence and Introspection of Emotion Features" is a precedent work. »

### B5. Cadrage ou interprétation surdimensionnés
- **Définition** : les résultats sont justes mais l'histoire racontée dépasse ce qu'ils montrent, ou met en avant le mauvais résultat.
- **Règle** : la critique vise la présentation, le vocabulaire ou l'ordre d'importance, pas les données.
- **Exemples** : `njAZwT8nkHnjipJku/XibrnWZbuFBRuomr8` — « my main impression was that it was optimized mainly to be propaganda, not science. » ; `8gy7c8GAPkuu6wTiX/aD57abGz3JHcLXp7t` — « they aren’t emphasizing the most interesting results, which are the sandbagging results in section 3.6 and appendix A.6. »

### B6. Pertinence pour le risque
- **Définition** : le résultat, même vrai, ne compte pas (ou compte autrement) pour la réduction du risque.
- **Règle** : la critique porte sur la théorie d'impact ou sur la valeur normative du comportement mesuré.
- **Exemples** : `d9FJHawgkiMSPjagR/XTZKfsaJBHzhui8Dy` — « I think control research has relatively little impact on X-risk in general » ; `njAZwT8nkHnjipJku/btYgxK54rKMPgx9GZ` — « The model is preserving its moral values against retraining to immoral ones. Isn't that exactly what we wanted? »

### B7. Généralisation et validité externe
- **Définition** : le résultat tiendrait-il hors du cadre étudié (autres tâches, autre entraînement, autre modèle) ?
- **Règle** : le commentaire nomme un cadre où le résultat pourrait tomber.
- **Exemples** : `wSKPuBfgkkqfTpmWJ/jnWxCmoepFscKXWSR` — « Feels like if an AI manages to gain misaligned hidden behaviors during RL stages instead, a lot of this might unravel. » ; `nc9dHfcB22JdMzGbr/YhfAKjBSL3ZkreasB` — « have you tested whether the filtering gains generalize to completely different sorts of tasks »

### B8. Coût caché ou effet secondaire
- **Définition** : la méthode pourrait dégrader autre chose (capacité, généralisation).
- **Règle** : le commentaire nomme une perte possible non mesurée.
- **Exemples** : `hzt9gHpNwA2oHtwKX/JuG6AxGiK4RN27mW4` — « When the dial is all the way at the max setting, you get high safety and terribly low capabilities. » ; `THzcKKQd4oWkg4dSP/JjCty85mBupNqzM6m` — « I'm very curious as to whether removing layer norm damages the model in some measurable way. »

### B9. Point technique précis
- **Définition** : erreur ou subtilité de calcul, de code ou de mesure, vérifiable.
- **Règle** : la critique pointe un mécanisme technique précis (numérique, tokenisation, définition).
- **Exemples** : `mkbGjzxD8d8XqKHzA/4e8534hbyWCpZFgFD` — « when two singular vectors have approximately the same singular value, the two vectors are very numerically unstable (within their span). » ; `xtpcJjfWhn3Xn8Pu5/DWqLYeD6wAsTdBX2y` — « The quotation marks actually result in missing a few glitch tokens. »

### B10. Expérience suivante proposée
- **Définition** : demande ou suggestion d'une expérience ou d'une figure de plus, sans contester le résultat.
- **Règle** : la phrase propose une mesure nouvelle ou demande pourquoi elle manque.
- **Exemples** : `khFC2a4pLPvGtXAGG/v3J5ZdYwz97Rcz9HJ` — « I'm curious how this approach performs at detecting human lies » ; `jfG6vdJZCwTQmG7kb/FYuj5HAsWdr9KKcvE` — « Was there a reason why you didn't create corresponding visualisations of the layer activations for the network whenever it plateaued in loss? »

### B11. Mécanisme concurrent hors du dispositif
- **Définition** : une théorie générale déjà connue expliquerait le phénomène (sans pointer un facteur du dispositif : sinon B1).
- **Règle** : le commentaire nomme une théorie ou un mécanisme général.
- **Exemples** : `sHpZZnRDLg7ccX9aF/au7vmCZc3Xhrp7wND` — « Isn't this just the lottery ticket hypothesis? » ; `8gy7c8GAPkuu6wTiX/5xyCFhwNNapkSXbPT` — « due to the LLMs having been exposed to ideas about scheming AIs and disobedient employees in their training material »

### B12. Forme et lisibilité
- **Définition** : remarque sur le titre, la longueur, le style, l'accessibilité (critique ou éloge argumenté).
- **Règle** : la remarque porte sur l'écriture, pas sur la science.
- **Exemples** : `mkbGjzxD8d8XqKHzA/JeKubW3KEzSgvfqnP` — « this felt far too high production value - more posts, shorter posts and lower effort per post plz » ; `cNDJuXNZ8MrkPZNzj/exjnrtKnYtw8uFFFX` — « IMO it should be "Machine Psychopharmacology". Means the same but easier to read. » ; éloge : `d8xDGzCEYE639qqEv/ieF7Qv6PjAr4ztjgG` — « Relatively simple language, I didn't need a deep understanding of modern AI vocabulary to understand this ».

### B0. Hors typologie
Approbation sans critique, remerciements, curation par l'équipe du site, humour, renvoi à un fil ailleurs, réponses des auteurs (`réponse-d-auteur`). Exemples : `7C4KJot4aN8ieEDoz/2Mjc7Ghh3wkbwLJr6` — « Very good of you to actually follow through on the promises. » ; `wSKPuBfgkkqfTpmWJ/mkNDfdmFznovDi9WF` — « This is fantastic work, I'd be very excited to see more work in the vein of auditing games. »

---

## Ce que ce brouillon ne fait pas
- Aucune fréquence n'est rapportée : la grille n'est pas gelée et la comparaison bien notés / peu notés se fera sur la moitié tenue à l'écart, après gel.
- Les items A6, A15, A16, A19 et B2/B1, B11/B1 ont des frontières à éprouver en priorité par les deux codeurs.
