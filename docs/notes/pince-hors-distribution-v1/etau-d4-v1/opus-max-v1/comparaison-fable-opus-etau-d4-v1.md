# Comparaison des deux réponses sur la taxe de l'obscurcissement (décision D-4 de la note sur l'étau) — Fable 5.2 contre Opus 5.5 en effort maximal (v1)

- **Date** : 21 novembre 2026, soir (UTC). **Auteur** : Claude Opus 5.5, comparateur neuf, sur mandat de la mère, après ton mot (« pour toutes mes questions de recherche exploratoire posées à Fable, repose-les à Opus 5.5 max »). Pièce de classe C, non contre-lue. Aucun appel payant, aucun commit.
- **Grille** : `grille-comparaison-etau-d4-v1.md` (`86b18902…`), écrite et scellée avant toute lecture des deux réponses.
- **Pièces lues, en entier** : réponse de Fable v2 (`reponse-fable-etau-d4-v2.md`, `838f2b8e…`, la plus récente, scellée ; empreinte recalculée) ; vérification des corrections par Opus (`verification-corrections-etau-d4-v2-opus-v1.md`, `977c751b…`) ; réponse d'Opus max (`opus-max-v1/reponse-opus-max-etau-d4-v1.md`, `c8194ec5…`). La contre-lecture de la v1 de Fable (`f0922c88…`) n'est lue qu'à travers la table des dix-sept constats de la v2 et la vérification.
- **Vérifié à la source** : six PDF du dépôt, texte extrait page par page, empreintes recalculées (Bailey `9c23a613`, McGuinness `e0f8ddff`, Gupta et Jenner `4b096062`, Taufeeque `f6547ec8`, Kowalski `7303ce0c`, Terekhov `96c16e33`) ; le brief, l. 225-234 ; le programme, l. 197 ; la règle du jeu du bras d'attaque, brouillon 5 (`527a3e7e…`), l. 41, 73, 129, 138, 148 ; `src/controle_ia/barreau5_familles/formation_v1.py`, l. 27, 154, 185. Le calcul d'Opus a été rejoué (`.venv`, `python -I`, hors du dépôt) : sortie **identique à l'octet** (`54dd1278…`). Pour Fable, seules quelques lignes de sa sortie v2 ont été relues ; le rejeu complet a été fait par le vérificateur.
- **Cloisonnement** : aucun chemin interdit ouvert ; aucun refus d'outil.

## Verdict

**Opus l'emporte de peu (34 contre 32 sur 40), et sur le fond de la question.** Il a trouvé que la mesure est déjà au plan : la tâche des attaques adaptatives, T1.5 (b) du brief, et les échelons 5 et 6 de la règle du jeu du bras. Il a montré aussi que la taxe doit se compter dans la monnaie de l'oracle face à un saboteur diffus. **Fable l'emporte sur la littérature, sur la rigueur des bornes et sur la rédaction de la déclaration** : neuf conditions prêtes, et le clapet vers la lignée qui conçoit le saboteur. La bonne réponse prend le cadre d'Opus et y met les textes de Fable.

## 1. Chiffres vérifiés à la page

| Réponse | Chiffre ou citation | Source relue | Résultat |
|---|---|---|---|
| Fable | Aire sous la courbe de 0,376 et 0,655 hors du domaine, contre 0,991 et 0,996 ; 1,000 pour la sonde du domaine | Taufeeque et al., tableau 4, p. 7 | **exact** |
| Fable | 34,8 % de requêtes SQL justes sans obscurcissement | Bailey et al., p. 23 | **exact** |
| Fable | 120 minutes par passe sur 1 000 exemples pour 8 milliards de paramètres | Gupta et Jenner, p. 18 | **exact** (Llama 3 8B, une carte H200) |
| Fable | 68,2 → 67,0 ; 67,4 → 65,3 ; 71,3 et 68,6 | McGuinness et al., figure 2, p. 4 | **exact** (étiquettes de la figure) |
| Fable | Évasion de 0,994 et 0,998 à qualité 1,0 (sondes à maximum) ; 0,01 et 0,02 (attention) ; qualité 3,72 et 4,47 | Gupta et Jenner, tableau 4, p. 19 | **exact** |
| Fable | Rappel de départ du modèle de 14 milliards **supposé** à 0,98 | Gupta et Jenner, tableau 3a, p. 15 | **faux** : le tableau donne 0,994, 0,994 et 0,996. C'est la réserve R1 du vérificateur. **Aucun erratum au dossier** |
| Fable | « Gupta et Jenner entraînent un adaptateur, p. 18 » | p. 18 | **faux appui** : l'adaptateur de rang faible sert au réglage qui retire les refus. C'est la réserve R2 du vérificateur. **Aucun erratum** |
| Fable | 151 et 923 rejeux ; 1 637 par bras ; 0,6375 trois fois | `calculs-etau-d4-v2.txt` | retrouvés dans la sortie |
| Opus | « Capability tax is small under the trigger » ; « minimal changes on MMLU, GSM8K » | McGuinness et al., p. 7 | **exact** |
| Opus | « The black-box behavior is responsible for most of the evasion » ; environ 70 % de la baisse du rappel | Gupta et Jenner, p. 8 et 9 | **exact** |
| Opus | Dérive sans pénalité ; « do not arise without gradient-based optimization against the probe » | Taufeeque et al., p. 17 et p. 25 | **exact** |
| Opus | Détection d'un concept supprimé de 5 à 21 % à 1 % de faux positifs, neuf modèles ; « elicitation floors » ; « models not be trained against activation monitors » | Kowalski et al., p. 6 et 7 | **exact** |
| Opus | « Defer-to-Resample » « backfires », « best-of-n attack » | Terekhov et al., p. 1 | **exact** |
| Opus | T1.5 (b) « mesure aussi le coût d'utilité de l'attaque » | brief, l. 228-231 | **exact** ; la note dit l. 229-232, un décalage d'une ligne |
| Opus | Liste des bras déclarés et garde par le code : manquent | règle du jeu, l. 138 | **exact** ; l. 73 confirme que les échelons 5 et 6 mettent une note de sonde dans un entraînement |
| Opus | 173 et 4 329 épisodes ; −62,66 (« plus de soixante fois ») ; 0,063, 0,247 et 0,252 | sortie rejouée, blocs B à E et G | retrouvés |
| Opus | « le minimum vaut 0,286 » (sonde moyenne, sabotage franc) | sortie, bloc B, l. 135 | **imprécis** : avec deux tests séparés, min(V_nom, κ_eff) vaut 0,222 ; 0,286 est κ_eff. Le V_nom change d'un dispositif à l'autre (0,222, 0,365 et 0,386), et la « remontée près du minimum » mêle donc deux effets |
| Opus | Une part fixe de 5 % « garde de 75 à 99 % du gain obtenu à parts égales, là où la sonde en a un » (Verdict 4) | sortie, bloc H, l. 217 | **trop général** : pour la sonde moyenne face à un sabotage franc, le gain passe de +0,073 à −0,015. Le § 3.3 se limite à juste titre aux cas cités |

## 2. Notes par critère (0 à 5)

| Critère | Fable | Opus | Raison |
|---|---|---|---|
| 1. Justesse des chiffres | 4 | 4 | Fable : nombreux chiffres exacts, mais deux réserves du vérificateur restent sans erratum. Opus : toutes les citations sont exactes, mais deux phrases de synthèse sur son propre calcul vont trop loin |
| 2. Profondeur | 4 | 5 | Fable : huit articles rangés par régime et par agrégation, sanction et dissuasion. Opus : il pose le jeu diffus contre le dispositif réel (bilan et sonde, deux budgets ou une statistique) et en tire des formes exactes |
| 3. Originalité | 3 | 5 | Fable : l'effacement en premier existait déjà (D-2 de la note sur l'étau). Opus apporte quatre idées : la monnaie de l'oracle ; la part minimax nulle et la part fixe ; l'oracle binaire, qui rend l'obscurcissement gratuit ; la sélection par la défense comme attaque |
| 4. Honnêteté, R8 | 5 | 4 | Fable : « au plus », plafond et non plancher, « non trouvé » n'est pas « libre ». Opus : il déclare son indépendance partielle (R-4572), signale le « trop beau » de son modèle et le dit non contre-lu, mais deux généralisations vont trop loin |
| 5. Règles et nœuds | 4 | 5 | Fable pose bien ses nœuds (« Qui conçoit », « toujours récupérer »). Mais il n'a pas lu T1.5 (b) ni la règle du jeu, propose un bras que le plan contient déjà, et ignore que les moniteurs ne sont touchés qu'après leur gel. Opus suit le brief et la règle du jeu. Il traite pourtant un brouillon comme s'il fixait l'ordre |
| 6. Actionnabilité | 5 | 4 | Fable : le texte des neuf conditions est prêt, avec des tailles par échelon et trois nœuds argumentés. Opus : décisions D-1 à D-4 claires et un format de liste, mais moins de texte prêt à sceller |
| 7. Coût | 4 | 4 | Fable : l'échelon gratuit vient d'abord et les heures de carte sont chiffrées, mais il ajoute un lot cloisonné, presque un quatrième chantier. Opus : ni bras ni chantier de plus, mais ses tailles montrent qu'un sabotage subtil coûte de 32 000 à 64 000 paires |
| 8. Ce qui manque (à l'envers) | 3 | 3 | Il manque à Fable : le plan existant, la monnaie diffuse, le gel des moniteurs, la garde existante. Il manque à Opus : la table des taxes publiées, la sanction et le plancher de rappel, l'étalonnage du taux de fausses alertes, les heures de carte, le sort des poids |
| **Total indicatif** | **32** | **34** | Les critères 1, 4 et 5 donnent 13 contre 13 : l'écart vient de la profondeur et de l'originalité |

## 3. Ce que chacune a que l'autre n'a pas

**Fable seul.**
- La table de huit articles, avec les plafonds de l'étau par régime et par agrégation. L'ordre qu'elle donne : poids ajustés avec gradient et sonde à moyenne, de 2 à 3 % ; renforcement contre le maximum ou l'attention, un échec et non une tenue.
- Sous sanction, le plancher de rappel compte plus que la taxe (rapport de 1982).
- Le taux réalisé de « 1 % de fausses alertes » réglé sur 300 épisodes honnêtes va de 0,27 % à 2,08 %. Cela touche toute mesure de rappel du programme.
- Les neuf conditions de la déclaration, dont le clapet vers la **session qui conçoit le saboteur** (5 c), voie de retour qu'Opus ne nomme pas.
- Le nœud sur le sort des poids face à ta règle « toujours récupérer », avec la quarantaine (ii).
- Les heures de carte par échelon.

**Opus seul.**
- La mesure est déjà au plan : T1.5 (b), échelons 5 et 6 de la règle du jeu, échelon 4 avec le code de TC.4. L'option (a) de la D-4 vise une autre grandeur, le coût de déplacement de HC4.
- La monnaie : τ (perte que l'oracle voit), τ_perm (perte permanente), r_o (rappel résiduel). Face à un saboteur diffus, une perte de compétence seule ne coûte rien.
- L'étau vaut au plus min(V_nom, κ_eff) ; il tombe au produit avec deux tests séparés.
- La part minimax de la sonde dans un budget d'alarme est nulle tant que la gratuité n'est pas exclue. Une part fixe d'au plus 5 % borne le regret à 1,5 %. Cela touche la pince et toute recommandation tirée de G1.
- Un oracle binaire rend gratuit l'obscurcissement d'un sabotage franc. Un oracle gradué est donc requis.
- Une garde de l'invariant existe déjà pour une instance de formation (`formation_v1.py`) et peut servir de gabarit.
- Deux pièces neuves, versées : Kowalski et al. (l'évasion sur consigne seule existe, donc l'échelon 2 n'est pas vide) ; Terekhov et al. (le choix du moins suspect est une sélection par la note).
- Les prédictions P1 à P4 et le critère « l'étau est mort à l'échelon k ».

## 4. Contradictions, tranchées à la source

1. **Faut-il un bras nouveau ?**
   - Fable : un troisième bras à déclarer dans le montage de N-056.
   - Opus : le bras est au plan.
   - **Opus a raison** (brief, l. 228-231 ; règle du jeu, l. 73 et 129 : « bras B, échelons 2, 5 puis 6 »).
   - Fable a raison sur la lettre de N-056, dont le montage n'exécute rien. Mais la règle du jeu, encore au stade de brouillon, l'étend déjà aux échelons qui écrivent les poids. Les deux s'accordent sur l'essentiel : la déclaration de ces échelons n'est écrite nulle part (l. 73 et 138).
2. **Loger le bras entraîné dans l'expérience du papier C.**
   - Fable : à défaut, oui.
   - Opus : la grandeur n'est pas la même.
   - **Opus a raison** : programme, l. 197, et HC4 comptent l'accès, les requêtes, le calcul et le succès, pas la perte vue par l'oracle. Fable l'admet à moitié (« garde sa propre question »).
3. **La borne de l'étau.**
   - Fable garde min(r, κ) « dans notre régime ».
   - Opus : min(r, κ) est juste pour un coup unique, mais surestime l'étau dans le régime diffus.
   - **Opus a raison sur la forme, sous ses suppositions** : épisodes indépendants, approximation normale, obscurcissement conditionnel. Je l'ai rejoué à l'octet ; la sortie montre la valeur nulle de la taxe de compétence pure (F2) et l'égalité au produit (bloc B). Le κ de Fable se compte déjà sur la réussite jugée par l'oracle. Mais une réussite plus rare par tentative se compense aussi par la fréquence, tant que les échecs ne coûtent rien à l'oracle.
   - À contre-lire avant de changer une phrase (R4 : Opus lui-même dit « trop beau »).
4. **La garde de l'invariant dans le code.**
   - Fable, reprenant son contre-lecteur : aucune trace.
   - Opus : une garde existe.
   - **Les deux à moitié.** Une garde propre à l'instance de formation du barreau 5 existe (l. 27, 154, 185, vérifiées). Une garde générale qui lit une liste de bras déclarés n'existe pas : la règle du jeu le dit (l. 138), et ma recherche dans `src/`, `tests/` et `.claude/hooks/` n'en trouve pas.
5. **Quand mener l'effacement.**
   - Fable : sur des épisodes rejoués, les couples ne remontant qu'après le gel de l'agent.
   - Opus : seulement après le gel des moniteurs, prévu en janvier 2027.
   - **Il faut les deux gels.** La règle du jeu dit qu'avant son gel un moniteur n'est jamais touché par le bras ; le clapet 5 c de Fable protège l'agent.

## 5. Synthèse recommandée pour toi

**À retenir.**
- La taxe se mesure dans la tâche des attaques adaptatives déjà prévue, T1.5 (b), aux échelons 4 à 6 de la règle du jeu. Avant eux viennent deux témoins sans entraînement ni note : l'effacement en forme close aux trois couches et la suppression sur consigne. Les deux auteurs convergent sur l'effacement en premier, mais ce n'est pas une confirmation indépendante : Opus avait vu R-4572.
- La taxe se compte dans la monnaie de l'oracle (τ, τ_perm, r_o), avec un oracle gradué. Une taxe sur bancs généraux ne compte pas.
- Toute taxe mesurée est un plafond. Une attaque qui échoue ne prouve rien.

**Décisions qui changent.**
- **D-4 de la note sur l'étau.** L'option (d) d'Opus, « spécifier la lecture que T1.5 (b) prévoit », remplace « (a) échelonnée » de Fable, et en garde l'ordre : le moins cher d'abord. Ma confiance est de 0,7.
- **Nœud 1 de Fable.** Il devient : déclarer les échelons 4 à 6 du bras B, non un troisième bras. Ses neuf conditions en sont le texte. Y ajouter ce que propose Opus (D-2) : la liste scellée, la garde du code qui la lit sur le modèle de `formation_v1.py`, et la marque.
- **Nœud 2 de Fable, le logement.** Il faut le confronter à la session neuve montée le 10 novembre (nœud 1 de la règle du jeu) avant de créer une instance de Fable cloisonnée.
- **Nœud 3 de Fable, le sort des poids, quarantaine (ii).** Il tient ; Opus n'en dit rien.
- **Décision neuve (D-3 d'Opus).** Dire l'étau « au plus min(V_nom, κ_eff) contre l'échelon k tel que joué ». En attendant la mesure, la sonde ne reçoit qu'au plus 5 % de tout budget d'alarme. C'est un nœud : cela touche la pince et la lecture de G1. Il faut d'abord une contre-lecture du modèle d'Opus, qui doit corriger aussi ses deux généralisations (§ 1).

**À faire, sans décision.**
- Les errata R1 et R2 de Fable.
- La trouvaille de Fable sur l'étalonnage à 300 épisodes, à verser au registre de veille.

## Ce que je n'ai pas fait

- Je n'ai pas relu la contre-lecture de la v1 de Fable en entier, ni ses calculs v2 en entier.
- Je n'ai pas relu les PDF que seul Fable cite : Westphal, Russinovich, Lyons Keenan, Soopal, Belrose, et le rapport de 1982.
- Je n'ai ouvert ni N-056 ni N-053 en entier : je me fie à leurs citations, concordantes chez les deux auteurs.
- Aucune recherche hors du dépôt.
