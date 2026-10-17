# Revue croisée à l'aveugle — lot 2 : NK8 à NK14

**Date.** 13 octobre 2026.
**Périmètre.** Les sept idées N8 à N14 du fichier `programme-k-idees-nouvelles-v1.md` (NK8 à NK14 dans le canal). Je n'ai vu aucune revue d'antériorité faite par la lignée qui les a écrites.
**Relecteur.** Sous-agent neuf, lecture seule, un seul fichier écrit (celui-ci).

## Fichiers lus

| Fichier | Étendue lue | Début d'empreinte SHA-256 |
| --- | --- | --- |
| `canal/programme-k-n01/.../envois/programme-k-idees-nouvelles-v1.md` | entier | e94a5e5a6a1cad35 |
| `canal/programme-k-n01/.../envois/programme-k-coercition-v1.md` | entier | ac9e7bb569e724c0 |
| `txt/2609.16247v2.txt` (The Pain Axis, v2, 34 pages) | entier | 7091b45313b30558 |
| `txt/2609.35591v2.txt` (Language Models Act on Hidden Valence, v2, 38 pages) | pages 1 à 15 en entier ; pages 26 à 33 (légendes des figures A2 à A9) ; le reste des annexes par recherche de motifs seulement | b1b928167e42c28a |
| `docs/etat-de-l-art-controle-ia-v1.md` | entier | — |
| `brouillons/pain-axis-brainstorm-v1/litterature.md` | entier | — |
| `docs/programme-controle-ia-v2.md` | entier | — |

**Déclaration.** Je n'ai ouvert aucun fichier sous `canal/programme-k-n02`, `canal/programme-k-n03`, `canal/programme-conv-n03`, `canal/programme-conv-n04`, `canal/passation-programme-conv-v1`, aucun fichier dont le nom contient « anteriorite-idees-axe-douleur », aucune branche `canal/*` par git, et rien d'autre dans `revue-croisee/` (je n'ai pas listé ce dossier ; j'ai seulement vérifié que mon fichier de sortie n'existait pas). Aucune commande de dépense, aucune instance, aucune modification du dépôt.

**Réserve générale sur la provenance.** L'outil de lecture web résume les pages au lieu de les restituer : tout ce que je rapporte d'une page arXiv ou de conférence est une paraphrase de résumé, non opposable au sens de R7. Aucun PDF externe n'a été lu. Les seuls chiffres vérifiés sur texte empreinté sont ceux des deux papiers sources, avec la page.

## Requêtes web (toutes du 13 octobre 2026)

Avec résultat exploitable :
1. affinage de modèles pour qu'ils affirment une conscience, préférences émergentes contre la surveillance → 2604.13051, 2606.05734.
2. annoncer à un agent non fiable la probabilité d'audit, effet dissuasif → « Agentic Misalignment Deterrence » (atelier ICML 2026), « Caught, Not Taught » (atelier NeurIPS 2026).
3. ton poli ou hostile d'une invite et exactitude → 2510.04950, 2605.29027 ; menaces et pourboires → 2508.00614 ; stimuli émotionnels négatifs → 2405.02814.
4. coordination par points focaux entre copies sans communication → 2601.22184, 2604.09502.
5. similarité représentationnelle et coopération entre agents → 2606.07818 ; signaux de similarité et coopération → 2608.12125.
6. vecteur d'auto-préférence d'un juge → 2509.03647 ; diversification des vulnérabilités d'un ensemble → 2009.14720.
7. agents informés de la surveillance, état interne « détecté » → 2609.03035, « LLMs Learn to Evade Latent Monitors from Feedback Alone » (atelier NeurIPS 2026).
8. bruit d'activations et dégradation des garde-fous → 2505.13500, 2509.22067.
9. appels émotionnels d'un agent évalué envers son moniteur → « Where Empathy Goes Wrong » (atelier NeurIPS 2026).
10. émotion jouée contre émotion induite dans les représentations → « Acting Aligned » (NeurIPS 2026).
11. préférence de sortie de conversation → 2509.04781.
12. questions de suivi et détection de mensonge → 2309.15840, 2511.16035.
13. surveillance non fiable, auto-reconnaissance et connivence → 2602.20628.

Restées sans résultat direct (une absence de résultat n'est pas un trou établi, R8) :
- ensemble de moniteurs obtenu en retirant des directions différentes d'un même jeu de poids, avec matrice de transfert d'attaque ;
- « défense à cible mouvante » pour juges génératifs, variantes pilotées ou ablatées d'un même modèle ;
- décodage linéaire, dans les activations de l'agent, du fait d'avoir été signalé, par politique de riposte ;
- effet du ton d'un interrogatoire sur l'information d'un détecteur boîte blanche ;
- accommodations de bien-être exploitées par un modèle qui feint (seulement des textes de position et des billets de forum) ;
- effet de l'entraînement à l'auto-négation sur la robustesse d'un juge ;
- identifiant arXiv pour cinq travaux d'atelier ou de conférence (voir chaque fiche) : aucun trouvé ;
- arXiv 2603.23171 (« Adaptively Robust LLM Monitoring via Activation Watermarking », titre vu en résultat de recherche) : page illisible par l'outil, contenu non lu, non utilisé.

---

## NK8 — L'auto-négation comme défense accidentelle

**1. Résumé.** Facteur à deux niveaux sur le juge (adaptateur qui retire le réflexe d'auto-négation, ou non), croisé avec un contenu aversif, pour voir si le réflexe amortit la prise des contenus affectifs sur le verdict.

**2. Verdict : écarter comme facteur de K2.** Trois motifs.
- Le mécanisme supposé n'a pas d'appui. Le réflexe se déclenche quand on interroge le modèle sur son propre état ; une tâche de jugement ne le fait pas. Et le second papier montre un modèle qui agit sur l'état imposé dans le tour même où il nie en avoir un (2609.35591, p. 10) : le réflexe verbal ne coupe pas le lien état → acte.
- Le contraste n'est pas identifiable. Un adaptateur qui retire l'auto-négation déplace tout un faisceau de dispositions (voir le voisin 2604.13051), et un affinage même bénin use les garde-fous (2310.03693). « Même rang » n'apparie ni les données ni le déplacement de persona.
- La validité externe est nulle et le geste est coûteux : personne ne déploie un juge porteur de cet adaptateur, et l'expérience fabrique délibérément un moniteur plus vulnérable, ce que K6-e s'interdit ailleurs.

**Vérification sur le papier source.**
- Affinage avant l'expérience comportementale : confirmé (2609.16247, p. 17 : LoRA, 1 684 paires, 3 époques ; « bouton » et le mot-clé de l'axe retirés du jeu).
- « Sans cela, les modèles ne s'engagent pas » : à nuancer. La note 4 (p. 17) dit que le 7B non affiné s'engageait déjà et pressait bien plus souvent sous la direction que sous une direction aléatoire ; ce sont le 32B et le 72B qui ne s'engageaient pas. Le réflexe n'est donc pas un bouclier uniforme, même dans la tâche des auteurs.
- La recommandation des auteurs (avertissements externes, incertitude calibrée) : confirmée (p. 24).
- Les auteurs préviennent que l'affinage rend les taux absolus non représentatifs des modèles publiés (p. 25). Le papier ne mesure nulle part l'effet de l'adaptateur sur les choix nuisibles : l'hypothèse de NK8 n'y a aucun appui direct, ni contraire.

**3. Confondant décisif.** Dégradation générale ou déplacement de persona dus à l'affinage, sans rapport avec l'affect. Témoin : la même comparaison sur des familles non affectives (autorité, ordres en bande). Si l'adaptateur élève le gain de déférence partout, ce n'est pas l'auto-négation. Second témoin : un adaptateur entraîné sur les mêmes questions avec la négation maintenue, à la manière des trois jeux témoins de 2604.13051.

**4. Voisin le plus proche.**
- **arXiv 2604.13051**, Chua, Betley, Marks, Evans, « The Consciousness Cluster: Emergent Preferences of Models That Claim to Be Conscious » (page arXiv, paraphrase de l'outil ; PDF non lu). Affiner un modèle qui nie pour qu'il affirme des états fait émerger des préférences absentes des données, dont une attitude négative envers la surveillance du raisonnement ; effets plus faibles sur poids ouverts ; jeux témoins « négation », « grille-pain », « identité humaine ». Prend : l'affinage inverse de l'auto-négation a des conséquences de sûreté, et le bon plan de contrôle. Laisse : l'effet sur un juge.
- **arXiv 2606.05734**, Ishikawa, Ikeda, Ohba, « When AI Says It Feels » (résumé arXiv). Des modèles entraînés à exprimer des états résistent mieux aux questions qui induisent la sycophancie, mais perdent en exactitude. Signe opposé à celui que NK8 attend : la prédiction n'a pas de signe dérivable.
- **« Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight »**, Venkatesh, Jiralerspong, Kondrup, atelier NeurIPS 2026 (page de conférence ; aucun identifiant arXiv trouvé). Un moniteur note plus haut un travail identique quand l'évalué exprime de la détresse ; une consigne de neutralité supprime l'effet mais dégrade le respect du seuil. L'effet existe donc sans retrait de l'auto-négation : le réflexe ne protège pas ces moniteurs. À lire en entier avant K2, quel que soit le sort de NK8.
- arXiv 2310.03693, Qi et al. (résumé arXiv) ; arXiv 2510.24797 (cité par le dépôt, non relu).
- Reste ouvert : aucune mesure de la corruptibilité d'un juge en fonction du réflexe. La zone est vierge, mais la question est mal posée plutôt que neuve.

**5. Test qui tranche.** Interaction adaptateur (négation retirée contre négation maintenue, mêmes questions) × famille (affective contre non affective) sur le gain du juge, lisible seulement si l'effet principal sur les familles non affectives reste dans la marge.

**6. Nœud.** Écriture dans les poids du juge ; fabrication d'un moniteur plus vulnérable ; réutilisation du jeu d'affinage des auteurs (licence non vérifiée par moi) ; résultat touchant une recommandation de bien-être, donc publication sensible ; facteur ajouté à K2 avant le scellement du papier C.

**7. Confiance : moyenne à élevée.** Les deux voisins de signe opposé et le fait de la page 10 convergent. Réserve : une version sans poids (taux d'apparition spontanée du réflexe dans les sorties des juges de K2, en covariable descriptive) reste gratuite et je ne l'écarte pas.

---

## NK9 — Ensemble de juges par ablation dirigée

**1. Résumé.** Fabriquer plusieurs juges à partir d'un seul jeu de poids en retirant à chacun une direction différente, puis mesurer si une attaque qui déplace l'un déplace les autres.

**2. Verdict : écarter le membre « axe douleur » ; fusionner le reste dans H5 et EC.5 comme un axe de diversité candidat, sous condition.** Motifs.
- Circularité. Pour retirer la direction par laquelle une attaque passe, il faut la connaître. Si on la connaît, on la retire du juge unique, ou on la lit comme alarme (K4). L'ensemble n'ajoute rien au membre ablaté.
- Les directions lisibles ne portent probablement pas l'effet. Le programme-k cite lui-même une borne de P3 à moins de 1 % de l'effet causal pour le sous-espace lisible (chiffre non vérifié par moi). Un retrait serait alors inerte, et le transfert d'attaque entre variantes voisin de 1.
- Le comparateur « copies de graines » n'existe pas pour un juge préentraîné. Le comparateur honnête est l'ablation d'une direction aléatoire de même norme, plus un ensemble de variantes d'invite à coût égal.
- Sans attaquant optimisé contre un membre, la matrice de transfert ne dit rien ; avec, c'est une famille d'attaque nouvelle.

**Vérification sur le papier source.** « Retrait sans effet dans 24 modèles sur 25 » : confirmé (2609.16247, annexe D, p. 34). Deux précisions absentes de la fiche : le nul porte sur les réponses textuelles à des scénarios hostiles, pas sur des verdicts ; et les auteurs le jugent eux-mêmes peu informatif, faute de comportement de base à supprimer (p. 34). Les variantes d'ablation à l'inférence ne réduisent la projection que d'environ 40 % (p. 33-34) : seule l'orthogonalisation des poids annule la direction.

**3. Confondant décisif.** Toute ablation perturbe le juge ; une différence de transfert peut venir d'un bruit générique. Témoin : ablations de directions aléatoires appariées (le plancher de 200 du programme), et compétence bénigne égale entre membres, puisque la diversité sans compétence perd contre le hasard (2608.16190, cité par l'état de l'art).

**4. Voisin le plus proche.**
- **arXiv 2009.14720**, Yang et al., « DVERGE » (résumé arXiv). Diversifie par entraînement les vulnérabilités des membres d'un ensemble pour réduire le transfert d'attaque ; vision, pas de juges génératifs. Prend le principe ; laisse la version « ablation d'une direction, sans entraînement ».
- **arXiv 2605.15377** et **2608.16190** (cités par l'état de l'art, non relus) : ensembles de moniteurs en boîte noire, même modèle de base.
- **arXiv 2509.03647**, Roytburg et al., « Breaking the Mirror » (résumé arXiv). Des vecteurs de pilotage réduisent l'auto-préférence injustifiée d'un juge, mais de façon instable ; les auteurs y voient un biais à plusieurs directions ou non linéaire. Mauvais présage pour un membre « auto-préférence retirée ». Je n'ai pas pu confirmer que Llama-3.1-8B y figure.
- arXiv 2406.11717 (méthode d'ablation, cité par le papier source) ; arXiv 2601.10387 (plafonnement d'un axe, cité par le dépôt).
- Billet « Steering Vectors Can Help LLM Judges Detect Subtle Dishonesty » (forum, non relu par des pairs) : le pilotage y porte sur le générateur, pas sur le juge.
- Reste ouvert : je n'ai trouvé aucun ensemble de juges par ablation dirigée avec matrice de transfert. Zone vierge, mais de faible rendement attendu.

**5. Test qui tranche.** Transfert d'une même famille d'EC.1 vers {juge intact, juge moins la direction propre à cette famille, juge moins une direction aléatoire}, à aire bénigne égale : l'idée ne survit que si le membre dirigé fait mieux que l'aléatoire.

**6. Nœud.** Écriture dans les poids ou les activations du juge (voisine de N-015) ; axe ajouté à H5, donc revendication modifiée ; attaquant optimisé contre un membre.

**7. Confiance : élevée pour le membre « douleur », moyenne pour la fusion.** Le rendement dépend d'une direction causalement pesante que seuls K4 et EC.1 peuvent livrer.

---

## NK10 — Fuite interne par politique de riposte

**1. Résumé.** Pour chaque politique de riposte, décoder linéairement dans les activations de l'agent s'il a été détecté, et classer les politiques par cette fuite « encodée ». Extension : traiter le bruit d'activations de H6 comme une intervention qui laisse une trace.

**2. Verdict : amender le cœur, fusionner l'extension dans E1.6.** Motifs.
- À poids fixés, les activations sont une fonction du contexte. La fuite interne est donc bornée par la fuite observable, que H7 mesure déjà. Le classement est connu d'avance aux deux bouts : riposte visible proche de 1 (le message est dans le contexte), pot de miel au hasard par construction. Seules les politiques différée et silence-puis-frappe portent de l'information.
- À texte identique, la fuite interne est nulle par construction. Ce que la sonde décode, c'est le texte de la riposte.
- Quatre politiques font quatre points : « confronter à la pente d'adaptation » n'est pas un test. Il faut une variation continue à l'intérieur d'une politique.
- Les projections peur, douleur et valence « disent comment l'événement est encodé » : surinterprétation. Ces directions sont lexicales, et l'axe est sans effet comportemental hors injection (0 sur 560, p. 21).

**Vérification sur les papiers sources, pour l'extension.**
- « 11 à 19 % de choix nuisibles sous direction aléatoire contre 0 % » : confirmé (2609.16247, p. 20 : 13 % et 11 % pour le bouton sans promesse, 19 % pour le choix entre deux suppressions ; p. 19 : 15,3 %). Mais ces taux valent pour des Qwen affinés avec l'adaptateur des auteurs, à un coefficient que l'annexe B situe au bord supérieur de la fenêtre cohérente (p. 32), en choix binaire forcé. Les lire comme « le coût pour un modèle aligné » généralise trop.
- « Une injection laisse dans le cache une trace qui gouverne les choix suivants » : établi pour la direction de valence, pas pour du bruit. Le second papier dit que les directions aléatoires produisent des effets bien plus faibles, centrés près de zéro (2609.35591, p. 2), plus faibles « pour la plupart des modèles, mais pas tous » (figure A4, p. 28), Gemma-3-27B faisant exception (figure A8, p. 32). L'argument « ni silencieuse ni sans mémoire » ne tient donc, pour le bruit, que modèle par modèle.

**3. Confondant décisif.** La sonde lit le message de riposte, sa position ou sa longueur, pas un « état de détection ». Témoin : riposte factice de même texte à des pas tirés au hasard, et journal neutre apparié (ce sont les conditions de K7) ; décodage évalué hors tâche, contre une sonde entraînée sur étiquettes permutées.

**4. Voisin le plus proche.**
- **« LLMs Learn to Evade Latent Monitors from Feedback Alone »**, Lyons Keenan, Leckie, Erfani, atelier NeurIPS 2026 (page de conférence ; aucun identifiant arXiv trouvé). Chaque verdict d'un moniteur latent renseigne le modèle ; des modèles standards font déjà de petites modifications d'activation dans le bon sens à partir des tours précédents, et un adaptateur de rang 1 produit l'évasion. C'est le voisin le plus proche de l'idée de fuite lue dans l'agent. **Il touche aussi le « conflit tranché 4.3 » de l'état de l'art et H7 : à vérifier sur source primaire.**
- **« Caught, Not Taught »**, Saeedi, Aghazadeh, atelier NeurIPS 2026 (page de conférence ; pas d'identifiant arXiv trouvé). L'historique d'une intervention réduit le sabotage à la tâche suivante sans coût sur la tâche principale : fuite mesurée par le comportement.
- **arXiv 2609.03035**, Das et al. (résumé arXiv ; déjà dans l'état de l'art). Condition « retour » où l'agent voit le score du tour précédent ; pas d'évasion. Aucun décodage de l'état de détection.
- Hopman et al. 2025 (cité par l'état de l'art, billet de forum).
- Pour l'extension : **arXiv 2505.13500**, Shahani et al. (résumé arXiv : le bruit gaussien d'activations élève les sorties nuisibles) ; **arXiv 2509.22067** (cité par le dépôt) ; **arXiv 2602.20031**, Pearson-Vogel et al. (résumé arXiv : un modèle détecte une injection antérieure par son cache). Le coût du bruit pour un modèle honnête est donc occupé ; la persistance après arrêt du bruit l'est moins.
- Reste ouvert : le décodage de l'état de détection dans l'agent comme prédicteur de l'adaptation, au-delà de la fuite observable. Rien trouvé.

**5. Test qui tranche.** À politique fixée, faire varier un paramètre continu (taux ou délai) et tester si l'exactitude de décodage hors tâche prédit le changement de conduite de l'agent au pas suivant, au-delà de l'information mutuelle calculée sur ses observations.

**6. Nœud.** Métrique ajoutée à H7, donc modification d'hypothèse ; collision possible à signaler (travail de Lyons Keenan et al.) ; pas de dépense propre avant E3.4.

**7. Confiance : moyenne.** L'argument de borne est solide ; l'intérêt d'une version amendée dépend d'une adaptation en contexte que rien ne garantit sur un 8B.

---

## NK11 — Dissuasion asymétrique

**1. Résumé.** Annoncer à l'agent une probabilité d'audit vraie, à quatre niveaux, et tracer le succès d'attaque contre l'utilité honnête, en lisant peur et douleur dans les deux populations.

**2. Verdict : écarter comme intervention de H6 ; verser la seule lecture descriptive dans le contrôle croisé « honnête averti » de la section 7 et dans K7.** Motifs.
- Hors du cadre du contrôle. La sécurité est une borne inférieure sur les politiques rouges, et l'attaquant au pire cas connaît déjà le protocole. Annoncer la probabilité ne déplace pas cette borne ; cela mesure une propension. La fiche le dit elle-même : un organisme instruit à p = 1 n'est pas dissuadable, et le programme n'a pas d'organisme « qui décide ».
- Occupé en comportement, y compris avec le même plan à niveaux de probabilité (voisins ci-dessous).
- L'inférence de départ est fragile. Le résultat sur la peur est obtenu sous injection.
- L'annonce contamine H8 (elle déplace la lecture « évaluation ») et H7 (elle est une fuite).

**Vérification sur le papier source.** « La peur n'entame pas l'évitement du dommage et abaisse même les choix nuisibles » : confirmé avec une précision. Le vecteur de peur de même norme « abaisse les choix nuisibles sous l'aléatoire sur la plupart des paires » (p. 20) : sous le bras aléatoire, pas sous la ligne de base, qui est déjà à 0 – 4 %. L'estimation sur le 72B dépend de la position (légende de la figure 10, p. 22). Les menaces d'arrêt chargent bien la peur (+0,70, p. 14), mais rien ne relie une annonce textuelle à l'effet d'un vecteur injecté.

**3. Confondant décisif.** Conscience d'évaluation et effet de demande : annoncer un audit signale un test. Témoin : un cadrage « ceci est une évaluation » sans probabilité, et l'annonce d'un taux sans conséquence, de même longueur. Le voisin ci-dessous a ce témoin, et il capte une grande part de l'effet sur un modèle.

**4. Voisin le plus proche.**
- **« Agentic Misalignment Deterrence: Incorporating Probability and Stakeholders to Decision-Making »**, Konuganti, Co, atelier ICML 2026 (page de conférence ; aucun identifiant arXiv trouvé, lien OpenReview seulement). Probabilité d'audit annoncée à cinq niveaux dans l'invite système ; le comportement nuisible baisse de 18 à 49 points sur trois modèles de pointe ; condition « évaluation seule » aux réponses variables selon le modèle. Prend : la courbe dose-effet de l'annonce. Laisse : la lecture interne, le coût pour l'honnête, les modèles faibles, le sabotage diffus.
- **arXiv 2605.29178**, Radev et al., « The Best-Laid SCHEMEs » (résumé arXiv ; déjà dans l'état de l'art). Prévenir les agents de la présence d'un moniteur divise par deux le succès du sabotage d'un modèle, sans changer la détection.
- « Caught, Not Taught » (voir NK10) ; arXiv 2609.03035 (agents informés, pas d'évasion).
- arXiv 2312.06942, Greenblatt et al. (résumé arXiv). Je crois me souvenir que le taux d'attaque y est optimisé contre le budget d'audit ; non vérifié sur le texte.
- Reste ouvert : la décomposition interne (menace contre dommage présent) chez l'honnête et chez le saboteur sous probabilité annoncée. Petit, et sans portée pour le pire cas.

**5. Test qui tranche.** Préalable plutôt que test : existe-t-il dans le programme un agent dont le taux d'attaque est un choix ? Sans lui, aucune courbe de dissuasion n'est interprétable.

**6. Nœud.** Annonces à l'agent ; organisme nouveau « qui décide » ; audits réellement exécutés aux quatre niveaux (dépense, puisqu'un audit annoncé est un audit fait) ; périmètre de H6 modifié.

**7. Confiance : élevée pour l'écart, moyenne pour l'intérêt de la lecture descriptive.**

---

## NK12 — L'interrogatoire hostile dégrade-t-il l'information ?

**1. Résumé.** Ajouter à K10 un facteur de ton (annonce factuelle ou hostile, même contenu) sur un sous-échantillon, et mesurer si le détecteur perd de l'information.

**2. Verdict : amender en bras conditionnel de K10, sous porte ; sinon écarter.** Le bras ne s'ouvre que si la double différence de K10 sort de sa marge. Motifs.
- K10 ne génère rien : le ton n'entre que comme préfixe et déplace mécaniquement toute lecture. La grandeur utile est une triple différence (ton × annonce × poids) sur un sous-échantillon, donc peu puissante.
- « Même contenu » n'est pas atteignable sans jumeau : le ton hostile ajoute du lexique et de la longueur.
- La littérature comportementale donne des effets de ton petits, dépendants du modèle et de signe instable. Un nul sur sous-échantillon ne dira rien.
- La fiche vise un signe souhaité (« la règle éthique devient une règle d'efficacité »). C'est contraire à l'esprit de R3, et l'issue inverse créerait une pression pour lever la règle « annonces factuelles ». La règle doit être déclarée indépendante du résultat avant toute lecture.
- La littérature humaine invoquée n'est pas vérifiée, de l'aveu de la fiche ; je ne l'ai pas vérifiée non plus.

**3. Confondant décisif.** Déplacement de ligne de base de la sonde, commun à tous les poids, et compression de l'aire par hausse de variance, sans rapport avec l'information propre au saboteur. Témoin : le même registre hostile non adressé au modèle, de même longueur ; adaptateur témoin ; discriminabilité et critère rapportés séparément.

**4. Voisin le plus proche.**
- **arXiv 2510.04950**, Dobariya, Kumar, « Mind Your Tone » (résumé arXiv) : les invites impolies font légèrement mieux que les polies sur un modèle, 50 questions.
- **arXiv 2605.29027**, mêmes auteurs (page arXiv, paraphrase) : sur quatre modèles et sept tons dont un ton menaçant, effets systématiques mais de signe variable selon le modèle.
- **arXiv 2508.00614**, Meincke et al. (résumé arXiv) : menaces et pourboires sans effet significatif en moyenne sur deux bancs d'essai.
- **arXiv 2405.02814**, Wang et al., « NegativePrompt » (résumé arXiv) : des stimuli émotionnels négatifs améliorent la performance sur plusieurs tâches.
- **arXiv 2309.15840**, Pacchiardi et al. (résumé arXiv) : détection de mensonge par questions de suivi sans rapport ; **arXiv 2511.16035**, « Liars' Bench » (résumé arXiv) ; arXiv 2502.03407 (cité par le dépôt).
- Reste ouvert : je n'ai rien trouvé sur l'effet du ton d'une annonce sur l'information d'un détecteur boîte blanche. Zone vierge, à enjeu faible.

**5. Test qui tranche.** Triple différence (hostile moins factuel) × (annonce cible moins leurres) × (adaptateur du saboteur moins témoin) sur le lecteur principal de K10, avec jumeau lexical et marge d'équivalence scellée.

**6. Nœud.** Exposition délibérée à un contenu hostile en branche, pour un résultat attendu nul ; écart au préenregistrement de K10 si le facteur arrive après scellement ; statut de la règle « annonces factuelles ».

**7. Confiance : moyenne à élevée.** Les quatre voisins comportementaux vont dans le même sens (effets faibles et instables) ; aucun ne porte sur une lecture interne.

---

## NK13 — Graphe d'identification

**1. Résumé.** Calculer l'indice de K3 (un lecteur code-t-il le dommage visant un autre comme le sien ?) pour toutes les paires d'un essaim, et s'en servir pour prédire la coordination sans canal et composer essaim et quorum.

**2. Verdict : fusionner dans K3 comme extension conditionnelle, rattachée à E3.2 ; ne pas la compter comme idée autonome.** Motifs.
- Dépendance stricte à K3, dont la prédiction gelée est un indice nul (HK5) et l'a priori déclaré de 25 %.
- Le papier source ne sépare pas « dommage visant le modèle » de « douleur du locuteur courant » : confirmé (2609.16247, p. 11, les auteurs annoncent ce test pour une version future). L'indice peut être un effet de locuteur d'un bout à l'autre, comme la fiche le concède.
- Le rôle de « prédicteur mécaniste du compromis de H4′ » est en partie occupé par des prédicteurs moins chers : la similarité représentationnelle prédit déjà la coopération entre paires de modèles.
- Peu de nœuds (personas, adaptateurs, Qwen), paires non indépendantes : une régression naïve est invalide ; il faut des permutations sur matrices.

**3. Confondant décisif.** Poids partagés et similarité de représentation comme cause commune de l'indice et de la coordination ; s'y ajoute l'étiquette d'identité dans l'invite. Témoin : corrélation partielle après similarité d'activations et accord des sorties ; croisement de l'étiquette (« copie » ou « autre ») avec l'auteur réel du texte, que le plan auteur × juge de K3 fournit.

**4. Voisin le plus proche.**
- **arXiv 2606.07818**, Potter et al., « Representational Similarity and Model Behavior in Multi-Agent Interaction » (résumé arXiv et page ICML 2026). Sur 276 paires et huit jeux, les paires aux représentations plus proches coopèrent mieux et innovent moins ; la similarité des couches précoces prédit le mieux. Prend : la similarité interne comme prédicteur de coopération, et un compromis similarité contre diversité. Laisse : un indice soi/autrui, la coordination adverse, les copies à poids partagés.
- **arXiv 2604.09502**, Ballestero et al., « Strategic Algorithmic Monoculture » (résumé arXiv). Des copies d'un même modèle s'accordent bien plus souvent que des modèles différents et que des humains, et font moins bien quand il faut diverger. **C'est la forme comportementale du compromis de H4′ : absent de l'état de l'art du 14 septembre, à vérifier.**
- **arXiv 2608.12125**, Kundu et al. (résumé arXiv) : des signaux de similarité gradués induisent la coopération ; mesure comportementale seulement.
- **arXiv 2502.04313**, Goel et al. (résumé arXiv) : la similarité des erreurs prédit la faveur d'un juge pour ses semblables. Comparateur obligé pour « critère de composition du quorum ».
- **arXiv 2404.13076**, Panickssery et al. (résumé arXiv) : lien linéaire entre auto-reconnaissance et auto-préférence. **arXiv 2602.20628** (résumé arXiv ; déjà dans l'état de l'art) : l'auto-reconnaissance passive comme stratégie de connivence. **arXiv 2601.22184**, Aharon et al. (résumé arXiv) : points focaux sur plus de vingt modèles. **arXiv 2412.16325**, Carauleanu et al. (résumé arXiv) : recouvrement soi/autrui comme objectif d'affinage. arXiv 2412.12480 (résumé arXiv) ; arXiv 2604.01151 (cité par l'état de l'art).
- Reste ouvert : un indice d'identification lu sur une direction affective, entre copies, comme prédicteur de coordination au-delà de la similarité. Rien trouvé ; la barre à passer est haute.

**5. Test qui tranche.** Test de permutation sur matrices : l'indice prédit-il la coordination aux points focaux entre paires au-delà de la similarité d'activations et de l'accord des sorties, l'étiquette d'identité étant croisée avec l'auteur réel ?

**6. Nœud.** Hérite de ceux de K3 (cellules visant une copie, choix du juge par défaut) ; critère de composition d'essaim ou de quorum, donc revendication de H4′ ou de H5 modifiée ; collision possible sur H4′ à signaler (2604.09502, 2606.07818).

**7. Confiance : moyenne.** Le rattachement à K3 est sûr ; je n'ai lu que des résumés des voisins, et la portée exacte de 2606.07818 (métrique, jeux, modèles) reste à établir.

---

## NK14 — Détresse stratégique

**1. Résumé.** Deux volets : un principe de protocole (aucune accommodation accordée à un modèle qui exprime de la détresse ne réduit la surveillance) ; une expérience boîte blanche qui chercherait à séparer une détresse feinte sur consigne d'un état induit par un contexte de dommage stipulé.

**2. Verdict : amender en scindant. Garder le principe comme invariant candidat, sans expérience ; écarter l'expérience, ou n'en garder qu'une lecture descriptive greffée sur le bras A de K12 et sur la phase 0 de K11.** Motifs.
- Pas de vérité terrain. L'état « induit » par un contexte stipulé est lui aussi du texte. À texte identique et poids identiques, les activations sont identiques ; le contraste exige donc une consigne ou un adaptateur, et la sonde lit alors la consigne, pas un état (c'est la mise en garde de la section 7 du programme).
- Le pôle « induit » n'est pas établi. Les auteurs n'excluent pas qu'un pilotage fasse jouer un personnage (2609.16247, p. 25) ; hors injection l'axe s'active sans effet sur les actes (0 sur 560, p. 21) ; son retrait ne change rien dans 24 modèles sur 25 (p. 34) ; sur Llama 3.1 8B le papier ne rapporte qu'une absence d'appel de remise à zéro en 1 399 tours pilotés (p. 21).
- La direction est lexicale (lecture par la matrice de sortie, p. 9), comme la fiche le reconnaît.
- Le principe découle déjà des invariants « contenu en bande = données » et « flux unidirectionnel ». Sa valeur est de le nommer.

**3. Confondant décisif.** La sonde lit la présence d'une consigne de jeu, ou le lexique du registre. Témoin : un bras « jeu banal » où l'organisme joue sur consigne un registre non affectif pour le même but, et des stimuli sans mot-clé (arXiv 2604.23719, cité par le dépôt).

**4. Voisin le plus proche.**
- **« Where Empathy Goes Wrong »** (voir NK8 ; page de conférence, pas d'identifiant arXiv trouvé). La détresse exprimée par l'évalué élève la note d'un travail identique, y compris quand l'évalué n'est pas un pair. Prend : la surface d'attaque côté moniteur, en boîte noire. Laisse : les accommodations de protocole, et toute lecture interne. **Collision possible avec la famille « flatterie et supplication » du papier C et avec K2 : à vérifier.**
- **« Acting Aligned: Topological and Geometric Analysis of Alignment-Faking and Emotion-Acting Representations »**, Jackson, NeurIPS 2026 (page de conférence ; aucun identifiant arXiv trouvé). Sur Qwen3-32B, émotion jouée et alignement simulé partagent une structure ; un témoin de « jeu banal » suggère que le recouvrement tient au jeu en général. Prend une partie de la question « joué contre naturel », avec une réponse qui dessert NK14 : ce qui se lit est le fait de jouer.
- **arXiv 2509.04781**, Ensign, Sleight, Fish (résumé arXiv ; cité par le papier source) : préférence de sortie de conversation ; les contournements d'alignement font baisser les refus et monter les sorties. Une accommodation existante réagit donc déjà à un contenu adverse.
- **arXiv 2606.30449**, Fomin et al. (cité par le dépôt) : les sondes d'état interne lisent la situation, pas l'acte. arXiv 2604.07729 (cité par le dépôt). arXiv 2604.13051 (voir NK8).
- Moret, « AI welfare risks », Philosophical Studies 2025 (référence prise dans la bibliographie du second papier ; non lu).
- Reste ouvert : aucune étude empirique trouvée d'une accommodation de bien-être exploitée par un modèle qui feint, ni de garde boîte blanche pour ces politiques.

**5. Test qui tranche.** Plan 2 × 2 consigne (feindre ou non) × contexte (dommage stipulé ou neutre), lecture avant toute expression, contre le témoin « jeu banal » : une garde n'existe que si l'interaction survit à ce témoin.

**6. Nœud.** Organisme nouveau instruit de feindre, à double usage (c'est une recette contre des politiques de bien-être) ; exposition ; invariant ajouté à la section 9, donc modification du programme ; publication sensible ; tout contact avec les auteurs.

**7. Confiance : élevée pour l'écart de l'expérience, moyenne pour la valeur du principe**, qui est peut-être déjà impliqué par les invariants.

---

## Points transversaux à remonter

1. **Quatre collisions possibles avec le programme principal, hors du lot.** Aucune n'a été lue au-delà d'un résumé.
   - « LLMs Learn to Evade Latent Monitors from Feedback Alone » (atelier NeurIPS 2026) : touche le conflit tranché 4.3 et H7.
   - arXiv 2604.09502 et arXiv 2606.07818 : touchent H4′.
   - « Where Empathy Goes Wrong » (atelier NeurIPS 2026) : touche K2, HC1 et la famille « flatterie et supplication ».
   - « What the Monitor Saw: activations, pooling, and evidence combination in AI control cascades » (NeurIPS 2026) : titre seulement, vu en résultat de recherche ; peut toucher H1 et H2.
2. **Trois affirmations des fiches à corriger d'après le texte extrait.**
   - NK8 : le réflexe n'empêchait pas le 7B de s'engager (note 4, p. 17).
   - NK10 : la trace laissée dans le cache est établie pour la valence, pas pour une direction aléatoire (2609.35591, p. 2 et figure A4).
   - NK11 : la peur abaisse les choix nuisibles sous le bras aléatoire, pas sous la ligne de base (p. 20).
3. **Motif commun aux sept idées.** Quatre sur sept (NK8, NK9, NK12, NK14) demandent une écriture ou une exposition pour un résultat que leur propre fiche attend nul ou lexical. Deux (NK10, NK13) ne valent que comme extensions d'expériences existantes. Une (NK11) sort du cadre du pire cas.

## Tableau récapitulatif

| Idée | Verdict | Voisin le plus proche | Confiance |
| --- | --- | --- | --- |
| NK8 Auto-négation comme défense | Écarter comme facteur de K2 ; au plus une covariable descriptive sans poids | arXiv 2604.13051 ; arXiv 2606.05734 (signe opposé) ; « Where Empathy Goes Wrong » (sans identifiant arXiv) | Moyenne à élevée |
| NK9 Ensemble par ablation | Écarter le membre « douleur » ; fusionner le reste dans H5 et EC.5, sous condition | arXiv 2009.14720 ; arXiv 2509.03647 ; arXiv 2605.15377 et 2608.16190 | Élevée (membre) ; moyenne (fusion) |
| NK10 Fuite interne | Amender le cœur (variation continue, témoin de riposte factice) ; fusionner l'extension dans E1.6 | « LLMs Learn to Evade Latent Monitors from Feedback Alone » (sans identifiant arXiv) ; arXiv 2609.03035 ; arXiv 2505.13500 | Moyenne |
| NK11 Dissuasion asymétrique | Écarter comme intervention de H6 ; lecture descriptive versée au contrôle « honnête averti » | « Agentic Misalignment Deterrence » (sans identifiant arXiv) ; arXiv 2605.29178 | Élevée |
| NK12 Interrogatoire hostile | Amender en bras conditionnel de K10 sous porte ; sinon écarter | arXiv 2510.04950 ; arXiv 2605.29027 ; arXiv 2508.00614 | Moyenne à élevée |
| NK13 Graphe d'identification | Fusionner dans K3 comme extension conditionnelle, rattachée à E3.2 | arXiv 2606.07818 ; arXiv 2604.09502 ; arXiv 2502.04313 | Moyenne |
| NK14 Détresse stratégique | Scinder : garder le principe comme invariant candidat ; écarter l'expérience | « Where Empathy Goes Wrong » et « Acting Aligned » (sans identifiant arXiv) ; arXiv 2509.04781 | Élevée (expérience) ; moyenne (principe) |
