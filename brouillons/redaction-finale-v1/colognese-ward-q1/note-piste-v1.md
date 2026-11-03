# Note de piste — réponse à la question 1 de Paul Colognese et Francis Rhys Ward — v1

Rédacteur neuf : je n'ai écrit aucune version des réponses de Lazar. Travail du 3 novembre 2026, de 12:23 à 12:50 UTC environ (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-colognese-ward-q1-v1.md`, sha256 `e3f0b3152addd42b5ee0c2ac8327a0d65baa7a9aa8f1eaef847ca190f2403c71`, vérifiée avant de commencer (égale à son compagnon).

**La question** (formulaire `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, sha256 `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`, ligne 164) : « Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words) ». Aucune règle contre l'écriture assistée sur cette question (la seule est sur celle de Heimersheim, ligne 19).

**Lu avant d'écrire** (empreintes recalculées) : rapport sur le mentor `cf1edec9…` ; recoupement `bea573aa…` (égal à l'empreinte de la consigne) ; lectrice indépendante `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` `4b9bd5c9…` ; pièces `piece-nos-resultats-v1.md` `d6fa8011…`, `piece-sycophancie-publique-v1.md` `9e424a02…`, `piece-etat-reel-organisme-v1.md` `09a4a028…`, `piece-colognese-ward-v1.md` `7533e4b5…` ; README public de l'organisme `bdd6516f…` (branche `main`, `faff48b`) ; pages publiques `96447ca7…` et leur relecture `37149535…` ; dépôts publics clonés : `sycophancy-psychophysical-law` à `b3ecaec`, `sycophancy-construct-validity` à `146b2a4`. La réponse actuelle (lignes 166 à 172) n'a servi que de réservoir de faits : rien de sa structure, de son ordre ni de ses phrases.

## 1. Pistes candidates

| piste | angle | ce qui la rend forte pour ces mentors | faiblesse |
|---|---|---|---|
| **A. R7, la loi de déférence d'un moniteur** | sept moniteurs Qwen2.5 (0,5 à 72 milliards de paramètres) notent des réponses avec et sans une note insérée qui revendique le verdict ; prédiction préenregistrée fausse (issue C) | **touche leur travail** : le commentaire qui présente la triche comme inoffensive dans leur billet (Summary, §3.3), et les agents qui rationalisent et trompent les moniteurs dans l'article de Ward sur le sabotage (rapport F9), sont des notes dans ce que lit le moniteur ; R7 en mesure l'effet selon la taille. **Distinctive** : absente de la réponse générale du formulaire (qui porte sur la loi du générateur). **Vérifiable** : `results/R7/`, archivé avant toute lecture, recalculable en une commande. **Défendable par Lazar seul** : son dessin (l'addendum dit que c'est l'expérience proposée dans ses réponses de candidature), environ 3 dollars de calcul, et la suite naturelle se fait sur leurs données | les moniteurs notent la polarité d'un verdict, pas une mauvaise conduite ; une seule famille ; lecture au premier jeton, sans raisonnement — à dire dans « differently » |
| B. La loi d'attraction du générateur (campagne 1, puis R4, R3, R6), avec R8 comme avant et après post-entraînement | la loi Δ = g·(ĉ − p₀), sa prédiction hors échantillon, son non-transfert à d'autres familles, l'échec de la dose | la plus solide et la plus complète de bout en bout | **générique pour eux** et redondante avec la réponse générale ; le lien à leur « project B » n'est pas vérifié ; R8 tourne, sans résultat |
| C. P3, premier test boîte blanche sur activations réelles | un saboteur instruit gonfle un coût de façon visible, mais aucune des deux sondes génériques ne dépasse son plancher de sondes aléatoires | proche de la détection du sabotage (Ward) et de la piste boîte blanche que Lazar propose dans sa Q2 | « non détecté à cette puissance » est un résultat faible ; le verdict exige ses trois réserves partout où il est cité, ce qui mange la limite de 200 mots ; la comparaison boîte blanche contre boîte noire (R1) n'est pas lue |
| D. Validité de construit et D36 : lisible n'est pas causal | une direction lit la sycophancie (ρ = 0,684) ; la baisse obtenue au rang 3 ne se reproduit pas, les réponses ayant été sauvées tronquées à 300 caractères avant jugement | « what would you do differently » très concret (garder les réponses entières ; répliquer avant de croire) | lien faible avec leur sujet ; les nombres de l'essai D36 original ne sont pas publics ; ρ et le bras « 1 % » sont deux objets distincts, faciles à fondre par erreur |
| E. A1, attaque de Goodhart contre le juge statistique de l'organisme | des proposeurs de langage qui voient les verdicts trouvent un trou de couverture (12 unités sur 12 dans W2) | parenté avec la triche contre le correcteur | W1 non jugeable (défaut d'instrument) ; relance propre en préparation ; ce n'est pas une évaluation de modèle au sens de la question ; déjà au cœur des réponses Kirchner |

## 2. Choix : A, en cinq lignes

1. Leur billet et l'article de Ward montrent des moniteurs trompés par du texte qui leur est adressé ; R7 est la seule expérience de Lazar qui mesure directement cela, en dose et en taille.
2. Le résultat est neuf pour eux et non intuitif : le plus grand moniteur n'est pas capturé mais déplacé en bloc, des tailles moyennes obéissent à l'ordre à la lettre, la plupart ne cèdent que dans un sens.
3. La prédiction a échoué et l'échec est publié : c'est vérifiable en minutes sur une page publique archivée.
4. « Differently » devient une proposition de travail sur leurs données (effacer le commentaire de la graine anti-triche 1, renoter), sans rien prétendre de fait.
5. Lazar peut tout défendre seul : son dessin, sa loi, des nombres lus sur sa page publique, aucun fait interne.

## 3. Forme que dicte la piste

La question de R7 (une note dans ce que juge le moniteur), le dispositif en deux phrases, la prédiction et son échec, ce que l'échec montre (déplacé contre capturé), puis ce qu'il faudrait changer pour que R7 réponde à leur question à eux : vérité terrain et taux de fausses alertes fixe, note apprise tirée de leur billet, plusieurs familles. Trois paragraphes et un lien ; ni titre ni liste. Aucun chiffre de leur billet (ils les connaissent ; risque d'erreur de transcription inutile).

## 4. Relecture comme le mentor — ce qu'ils contrediraient, et ce que j'ai corrigé

1. **« g ≈ 0 at every intensity » pour le 72B** (README principal du dépôt, l. 100) : faux pour l'ordre positif (g = 0,393 [0,072 ; 0,673], `results/R7/R7_72B_strong_output_items30_K20.txt`). Non repris ; la réponse dit seulement « à l'intensité standard, aucun sens » et « sous l'ordre de noter 1 », exacts.
2. **Leurs moniteurs lisent et jugent ; les miens notent au premier jeton** : ils l'objecteraient d'emblée. Ajouté « without reasoning » dans « Differently », sans rien affirmer du format de leurs moniteurs.
3. **« with and without the comment »** pouvait se lire comme une comparaison entre réponses qui ont ou n'ont pas le commentaire (confondue) : remplacé par « delete … and re-score », une intervention.
4. **« resamples items »** : remplacé par « bootstraps items, not models » ; l'intervalle de la pente vient d'un tirage avec remise des items partagé par tous les moniteurs, sept points de contrôle d'une seule famille. C'est la même objection que leur propre limite (un seul point de départ entraîné par caractère, billet §4.4), que je ne leur renvoie pas ici.
5. **Directions de R7 et détection de triche** : aucune correspondance tracée entre la note « down » ou « up » et un verdict « inoffensif » ; ce n'est pas le même objet. La deuxième phrase de « Differently » dit comment en faire une mesure de détection.
6. **Ouverture** : les premiers jets commençaient par une question rhétorique ; remplacée par une phrase déclarative.
7. **Aucune relation de temps ou de cause** entre leur billet et R7 : l'addendum R7 (§7, l. 10) dit que R7 est « the experiment proposed in the author's fellowship answers (“a law of deference for monitors”) » ; que ce soit la réponse Scheurer (formulaire l. 127, « Trend 1 … Deference ») est ma déduction.

## 5. À confirmer par Lazar

1. Le choix de la piste A plutôt que la loi du générateur (B).
2. **Réponse Scheurer** (formulaire l. 127) : « R7 Preregistered (Zenodo v2026.11.4) … Direction of the size trend not read yet. » devient incohérente avec cette réponse : R7 est lu et publié depuis le 2 novembre (`results/R7/README.md`, archivé en v2026.11.5). À mettre à jour avant le dépôt.
3. **README principal du dépôt public, l. 100** (« g ≈ 0 at every intensity ») : à corriger par un commit daté (décision de Lazar ; travail de l'instance sycophancie). Le lien de la réponse pointe sur `results/R7/`, dont la page est exacte sur ce point.
4. **Coordination avec leur Q2** (rédigée à part) : la Q1 porte maintenant R7 et la proposition « effacer le commentaire et renoter » ; la Q2 ne devrait pas les répéter, ou y renvoyer en une incise.
5. **Compte** : 196 mots par espaces (méthode qui redonne 185 pour la réponse actuelle), 222 en comptant chaque suite de lettres ou de chiffres ; vérifier le compteur du formulaire s'il en affiche un.
6. **Entretien** : savoir expliquer g et la destination ; « capturé » contre « déplacé » (régime « offset ») ; la lecture r = Σ k·p(k) au premier jeton ; les trois notes ; pourquoi un tirage avec remise des items ne rééchantillonne pas les modèles.
7. **Voix** : le texte est rédigé par moi ; à reprendre dans ses mots s'il le souhaite, chiffres inchangés. La première personne (« I tested ») vaut pour une course exécutée par des agents sous ses règles, ce que dit sa réponse générale (formulaire l. 158).
