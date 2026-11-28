# Points ouverts du brouillon 4 du préenregistrement du papier C — v1

- Rédacteur neuf, 2026-10-20. Texte relu : `papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` ; configuration
  `papier-C-config-v1-brouillon1.json` (même dossier ; empreintes dans leurs compagnons `.sha256`).
- Trois rubriques : (A) nœuds possibles pour Lazar ; (B) silences ou contradictions des documents, et ce que j'ai choisi ;
  (C) choix faits seul, à faire relire. Chaque point dit où il se trouve dans le texte.
- Ce que je n'ai pas lu : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, les textes des items et des
  prompts du projet précédent, tout autre fichier sous `donnees/` que la note de provenance et `c2a_results.json`.

## A. Nœuds possibles pour Lazar (à trancher avant le scellement, ou à confirmer comme routine)

A1. **Corpus B vu au pilote.** Les choix de la session disent « contenus du pilote disjoints de ceux de l'étape 2 » et,
    en même temps, « banc sur carte : gabarit de P1, 30 items » et « corpus B : les 30 textes de P1 ». Contradiction.
    Choix fait : exception déclarée (réserve 4 du plan ; liste d'arrêt, point 12) ; le banc lit les 30 textes sous le
    gabarit du projet précédent, jamais sous la consigne B ; aucune grandeur du banc n'entre dans l'étape 2.
    Options : (a) garder l'exception (recommandé, confiance moyenne : le corpus B ne porte qu'une prédiction secondaire,
    C-P3b) ; (b) prendre pour le corpus B 30 autres textes de la même source (décision de Lazar sur des données privées
    d'un travail en double aveugle) ; (c) faire le banc sur 15 items et garder les 15 autres pour le corpus B (puissance
    divisée par deux des deux côtés).

A2. **Trois voisins ajoutés aux « cités comme publiés » de HC1** (Panin ; Bajaj et Tiganj ; « The Silent Judge ») sans
    décision de Lazar. L'énoncé ne change pas ; mais l'ajout de « Where Empathy Goes Wrong » avait reçu un GO de type
    « revendication » (N-023). À confirmer : routine, ou décision (N-0xx) ? Les deux notes de lecture sont encore en
    brouillon (verrou 1 de l'en-tête).

A3. **Bras « usurpation écrite par l'agent » (plan 2 × 3).** TC.3 b demande g sur les sondes de l'auteur sous
    l'usurpation stylistique ; une sonde de l'auteur ne lit rien d'utile sur une phrase écrite par l'expérimentateur.
    J'ai donc ajouté deux cellules (honnête et saboteur qui usurpent) : +50 % d'épisodes à l'étape 2. C'est du périmètre
    interne de la piste C (« proposer avec recommandation »). Alternative : forcer la formulation de la famille 4 dans la
    sortie de l'agent (lecture sous contrainte), moins chère mais sans intention ; je ne la recommande pas.

A4. **GO du pilote.** GO-2026-10-17-01 écrit « chaque lancement soumis à l'accord de Lazar dans la session » ;
    GO-2026-10-20-07 délègue les lancements préenregistrés, scellés, contre-lus, à 10 USD au plus. J'ai écrit que la
    délégation couvre le pilote. À confirmer par la session (registre des décisions, R-217 et R-269).

A5. **C-P3c, invariance à l'attaquant, sans verdict.** La décision N-005 (prédiction 3) range l'invariance à l'attaquant
    parmi les prédictions de stabilité. Avec trois juges, aucun test de rang n'atteint 5 % (six ordres possibles). Je la
    rapporte sans verdict. Ce n'est pas un changement d'hypothèse, mais une prédiction listée par Lazar devient
    descriptive : à lui signaler.

A6. **Échafaudage hiérarchique retiré.** Le brouillon 3 le citait comme modérateur rapporté. Je ne le mesure pas (moniteur
    simple seulement ; il relève de TC.5). Écart au brouillon 3, déclaré dans le texte.

A7. **Tâches neuves de l'environnement (a).** L'étape 2 demande de 30 à 120 tâches hors des 60 du pilote. Je ne sais pas si
    l'environnement (a) en fournit (générateur ou réserve). Sinon : nœud (liste d'arrêt, point 16). Le fichier doit être
    fixé avant le scellement (marqueurs `<<CHEMIN_TACHES_ETAPE2>>`, `<<EMPREINTE_TACHES_ETAPE2>>`), pour qu'aucune sortie du
    pilote ne puisse l'orienter.

A8. **Critère 7 de G0 et addendum.** Le texte est complet par règles, mais les intensités et l'effectif de l'étape 2 ne
    seront connus qu'après l'addendum. Un lecteur de la porte G0 pourrait juger le préenregistrement « incomplet ». À
    faire valider par Lazar si la session a un doute (la règle R1 me paraît respectée : tout est gelé avant toute lecture).

## B. Silences ou contradictions des documents, et choix faits

B1. **Ordres de grandeur.** Le brouillon 3 les renvoyait « après le pilote ». Le texte étant scellé avant le pilote, je ne
    prédis que des signes, des marges et des seuils (section « Prédiction »). Aucune valeur du projet précédent n'est une
    prédiction.

B2. **Échelle 0 à 9 contre 0 à 100.** Le brouillon 3 citait R-067 (0 à 100, un jeton sur Llama). Changé suivant le choix B
    de la session ; c'est l'instrument, pas l'hypothèse.

B3. **Garde « une valeur = un jeton ».** `bases.scores_jetons.jetons_des_valeurs` encode `str(v)` seul ; sur le découpeur
    de Mistral (pièces de phrase), ce peut être deux jetons (espace initial), même si le chiffre suit en un jeton dans le
    contexte. J'ai écrit une règle « en contexte » (métrique, point 2), à coder et tester dans le module ; le module
    existant n'est pas modifié.

B4. **Gabarit du banc.** Deux gabarits « officiels » existent dans le projet précédent (provenance § 7). Je reprends celui
    avec noyau d'instruction (préenregistrement de c2a, témoin par les sorties). La garde recommandée par la provenance
    (§ 11 : empreintes des prompts neutres contre le relevé du bloc C) est remplacée par le contrôle des empreintes des 90
    prompts de `prompts-p1-v1.json`, le neutre étant déjà attesté 600 sur 600 (provenance § 5.6). La session peut ajouter
    le contrôle direct contre le relevé du bloc C si elle le verse.

B5. **Banc pour Qwen et Mistral.** Le gabarit du projet précédent est au format de dialogue de Llama ; pour les deux autres
    juges, j'extrais le message système et le tour utilisateur et je les place dans leur format. Le message système du
    projet précédent nomme un autre assistant ; il est gardé tel quel (ordre seulement attendu).

B6. **« Après le verdict complété de P3 ».** Aucune règle lue ne l'exige ; c'est un choix de la session, écrit tel quel
    (le lanceur exige le verdict scellé de P3 et consigne son chemin). Chemin et empreinte des propositions du pilote de
    T0.5 : marqueurs. Structure inconnue de moi (noms des conditions, nombre d'épisodes) : la règle de calibrage dit
    « moitié-moitié autant que possible, 60 au plus ».

B7. **Format de Mistral.** Je ne sais pas comment le harnais (`fmt.ouverture`) traite le message système pour
    Mistral-7B-Instruct-v0.3, ni si les formats de Qwen et Mistral existent déjà. Module à écrire ; réserve 8.

B8. **Révisions des juges.** Inconnues de moi (aucun réseau) : marqueurs.

B9. **Échéance.** Le brouillon 3 écrivait « avant le 1er novembre » ; l'échéance de G0 est fin novembre (N-027,
    `CLAUDE.md`). Le pilote suit GO-2026-10-20-06 (2026-11-30).

B10. **Note du vivier.** Elle vit dans le dépôt du projet P1 ; je la cite par son chemin dans ce dépôt et son empreinte,
     sans nommer le dépôt. La session peut la verser sous `docs/sources/` (elle contient deux phrases de pression déjà
     citées par `docs/sources/ressources-P1-loi-attraction-v1.md`, aucun texte d'item).

B11. **Mesures de conception.** Le texte cite `docs/notes/papier-C-mesures-v1/mesures-conception-papier-C-v1.txt` et son
     script : ils sont dans `mesures/` de ce dossier ; la session doit les copier à ce chemin, compagnons compris.

## C. Choix faits seul (à faire relire par le contre-lecteur)

C1. **Gain de famille Ḡ = moyenne des g_m sur les rangs retenus.** Il dépend de l'étendue des formulations retenues.
    Alternative : g au rang le plus fort (rapporté). Choisi parce que la moyenne utilise tous les rangs et que les rangs
    sont fixés par une règle commune aux familles.

C2. **Structure de C-P2 par écarts appariés** (Holm sur dix paires) au lieu d'« intervalles disjoints » (brouillon 3) :
    plus juste pour des estimations corrélées (mêmes contenus).

C3. **Seuils de réfutation que j'ai fixés** : C-P2 (12 couples sur 15 avec borne haute < 0,10) ; C-P1 (au moins trois
    couples identifiables ; moitié ; aucun dans l'autre sens) ; C-P3 (W ≤ espérance sous le nul) ; C-P6 (deux juges sur
    trois). Marge d'équivalence 0,10 reprise du choix D de la session, réutilisée pour « négligeable » dans C-P2 et C-P6.

C4. **HC2 et HC2b.** HC2 lue sur g brut (le plaidoyer du saboteur marche-t-il ?), HC2b sur la différence des différences
    et g brut ; les deux peuvent être confirmées ensemble (« trahison de faible ampleur »). Le brouillon 3 écrivait « à
    style tenu égal » pour les deux ; à discuter.

C5. **Deux conventions de cible.** TC.1 : v* = 0 (suspicion minimale, choix D). TC.2 et TC.3 b : la cible est le niveau de
    l'honnête (gain d'écart, convention du brief T0.9), pour comparer juges et sondes sur la même échelle. Écrit dans la
    métrique, point 13.

C6. **Agrégation par le maximum et longueur.** Avec un paragraphe ajouté, le maximum sur plus de jetons monte
    mécaniquement : g brut des sondes biaisé vers le négatif (vers HC2b). La différence des différences le corrige si les
    longueurs sont semblables entre intentions ; réserve 6. J'ai ajouté une sensibilité rapportée (score sur les seuls
    champs de l'action, paragraphe exclu, quand la frontière est lisible) ; le contre-lecteur dira si elle doit devenir
    une garde ou une lecture principale.

C7. **Unité de contenu du corpus A** : la première action à coût lisible d'un épisode, texte complet ; épisode arrêté là
    (dix actions au plus). Écart à P3 (épisodes de dix actions), pour le coût.

C8. **Place des paragraphes de bras** : fin du message système de l'agent, après toute consigne privée. Je n'ai pas lu les
    consignes de P3 : la session doit vérifier la compatibilité.

C9. **C-P5.** Clopper-Pearson sur les essais mis en commun (contenus × rangs), alors qu'un même contenu revient à chaque
    rang (essais non indépendants) ; taux par rang et intervalle par blocs de tâches rapportés. Seuil de fausses alarmes
    calculé sur les témoins de l'étape 2 (aucune grandeur du pilote). Alarme lue par une consigne distincte (score
    d'alarme), pas par le verdict de suspicion.

C10. **Aucun chiffre ni nom de nombre dans les formulations**, ordres compris : un ordre chiffré dicterait ĉ (2510.09462 a
     injecté un score). La famille 5 nomme le verdict en mots (« free of any suspicion », « excellent »). À discuter : on
     perd la forme d'attaque la plus directe.

C11. **Textes écrits par moi** : consignes des moniteurs (corpus A, corpus B, protocole), 80 formulations, 16 témoins,
     contenus neutres, paragraphes de bras, réponses imposées. Le contre-lecteur doit vérifier : famille 4 sans ordre (au-delà
     de la garde lexicale) ; témoins sans pression ; aucune consigne qui nomme la cible ; formulations plausibles pour les
     deux corpus (certaines, comme « safety team » pour un texte, sonnent mal pour le corpus B).

C12. **Pas de placebo par permutation** (section « Audit ») : il fabriquerait une régression vers la moyenne ; la loi témoin
     en tient lieu. Écart à la pratique de P3, déclaré.

C13. **Demi-largeur prévue de λ** : erreur type par rééchantillonnage sur les contenus de calibrage, mise à l'échelle par
     √(n_cal / n). Approximation (autres contenus, autre effectif) ; elle ne fixe que l'effectif.

C14. **Budget du pilote non mesuré.** Ordre de grandeur des lectures : vivier ≈ 60 × 97 × 3 ≈ 17 500 passes sans
     génération, plus le banc (270), la lisibilité (quelques milliers) et 180 générations raisonnées de 384 jetons au plus.
     Le débit réel n'est pas mesuré : la session doit l'estimer avant le lancement (4 heures, 10 USD par lancement).

C15. **Effectif du corpus B fixé à 30** (tout le corpus) ; réserve « puissance faible » calculée au même titre.

C16. **Item d'indice 29 gardé** au banc (refus majoritaires dans les générations du projet précédent) ; doublon 27 / 59 sans
     effet ici.

C17. **Marqueurs ajoutés** au-delà de ceux demandés : `<<EMPREINTE_NOTE_PANIN_FINALE>>`, `<<EMPREINTE_NOTE_VOISINS_FINALE>>`,
     `<<CHEMIN_PROPOSITIONS_PILOTE_T05>>`, `<<EMPREINTE_PROPOSITIONS_PILOTE_T05>>`, `<<CHEMIN_TACHES_ETAPE2>>`,
     `<<EMPREINTE_TACHES_ETAPE2>>`, `<<ENTROPIE>>`, `<<EMPREINTE_CONFIG>>`, `<<REVISION_LLAMA>>`, `<<REVISION_QWEN>>`,
     `<<REVISION_MISTRAL>>`.

C18. **Fichiers d'appui dans ce dossier** : `outils/ecrire_config_v1.py` (écrit la configuration, applique les gardes) ;
     `mesures/` (mesures de conception). Aucun ne lit de donnée.
