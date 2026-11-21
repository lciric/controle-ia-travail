# Comparaison des deux réponses sur la percée après « Blindfold » — Fable 5.2 (v2) et Opus 5.5 en effort maximal (v1)

- **Ce que c'est.** Une comparaison des deux réponses indépendantes à la question « que reste-t-il, où est la percée, après que le plancher d'audit au hasard s'est révélé occupé ». Pièce de classe C. Auteur : Claude Opus 5.5 (`claude-opus-5-5`), comparateur neuf, auteur d'aucune des deux réponses. 21 novembre 2026. Aucun appel payant, aucun commit.
- **Grille** : `grille-comparaison-percee-v1.md`, `616c30234ca9324a1c519d71fc114a31729d084a767a74fa568262d3f787a07d`, scellée avant toute lecture des deux réponses.
- **Pièces lues, empreintes égales aux compagnons** (`sha256sum -c`) : réponse de Fable v2, `reponse-fable-percee-apres-blindfold-v2.md` (`b91e9d8e…24d9`), en entier ; sa vérification des corrections par Opus (`verification-corrections-percee-apres-blindfold-v2-opus-v1.md`), en entier ; la contre-lecture de la v1, en tête (verdict et premier constat) ; réponse d'Opus en effort maximal, `opus-max-v1/reponse-opus-max-percee-v1.md` (`fa8653fb…94e2a`), en entier, et des lignes de sa sortie de calcul `calculs-opus-max-percee-v1.txt` (`8eb6fa37…49ce5`, blocs B, D, E, F). La réponse d'Opus n'est pas contre-lue ; la v2 de Fable l'est, et ses corrections sont vérifiées « conformes ».
- **Cloisonnement** : aucun chemin interdit par le mandat ouvert ; aucun résultat d'expérience lu.

## Verdict

Les deux réponses concluent de même : **aucune lecture des états internes du suspect n'est une percée** ; elle gagne une constante, et l'allure de sabotage la plus lente qu'on puisse prendre reste fixée par la référence honnête. Fable l'emporte en rigueur, en respect des règles du programme et sur la loi du second regard, contre-lue et rejouée. Opus l'emporte en largeur : l'argument du pire cas, la dissuasion, la règle de garder poids et contextes, une mesure du coût de réparation, et une antériorité que Fable n'a pas vue. Chacune porte une erreur que l'autre corrige à la source.

## 1. Chiffres vérifiés à la page

Texte des PDF par `pdftotext`, rang de la page dans le fichier ; empreintes égales aux compagnons.

| Réponse | Chiffre ou phrase | Source, page | Résultat |
|---|---|---|---|
| Fable | 9/14 tentatives prises et 1/35 échecs honnêtes marqués (moniteur « Gemini v5 », condition C) ; 6/14 et 1/35 pour la consigne v3 | Kezendirane, 2611.00407v1 (`b37f97b2…`), table 3, p. 6 | juste |
| Fable | la révocation fait passer le travail de 24,00 à 12,21 tâches par trajectoire ; « Registration slack … remain sources of exposure » ; « Reference-rate slack and irreversible events before an alarm remain outside the sublinear guarantee » | Singh, 2610.18948v1 (`53557a25…`), p. 9 | juste |
| Fable | « Protective action should respond to the consequence regardless of cause. Subsequent diagnosis determines… » | Singh, p. 52 (et seulement p. 52) | juste |
| Fable | perte « défaillance vraie et étiqueteur muet » définie sous X_t ∼ P (sans adversaire) | Li et al., 2611.15835v1 (`a0951584…`), p. 32 | juste |
| Opus | « authorized behavior is never sanctioned » | Gans et Holden, 2609.38262v1 (`e28a4e8d…`), p. 7 | juste |
| Opus | g = 0,2, κ = 0,1, α = F = 1, seuil 0,1e ≃ 0,272 ; « If κ = 0, no finite audit intensity deters » | Gans et Holden, p. 9 | juste ; e^(−αg/κ) = e^(−2) = 0,1353 recalculé juste |
| Opus | 60 épisodes, 14 tentatives, 35 échecs honnêtes | Kezendirane, p. 5 | juste |
| Opus | « … the range 1/πmin, but cannot bias it » ; théorème 6, « observations other than labels » | « Blindfold », 2610.37055v1 (`5250fa11…`), p. 16 et p. 6 | juste |
| Opus | ε_appr ≈ 0,025 pour une référence de 1 000 points | Podkopaev et Ramdas, 2110.06177v4, p. 7 | juste |
| Opus | théorème 11, « White-Box Irrelevance » | Wang, 2604.12951v1, p. 3 | juste |
| Opus | taux de correction 0,42 | Gan et al., 2604.16286v2, p. 1 | **chiffre juste, emploi forcé** : c'est le « top-1 fix rate » du meilleur modèle (Gemini 3.1 Pro), qui mêle trouver et corriger ; Opus l'emploie comme taux de correction d'un épisode déjà trouvé |
| Opus | « save activations that we want to apply updated probes to » | Greenblatt et Shlegeris 2024, page web versée (`f6174a8c…`) | présent ; page web, non opposable (R7) |
| Opus | plateau 0,0263 → 0,0078 (÷3,4) ; 5 748 → 300 sabotés à l'alarme (÷19) | sortie de calcul, bloc B, lignes 26-27 et 56 | égal à la sortie ; non rejoué par moi |

## 2. Notes par critère (0 à 5)

| Critère | Fable v2 | Opus max v1 | Justification |
|---|---|---|---|
| 1. Justesse des chiffres | 5 | 4 | Fable : quatre vérifiés justes, calculs rejoués à l'octet par le contre-lecteur. Opus : tous justes à la page, mais le 0,42 de Gan est détourné de son sens, et le « 13,5 % » du compte rendu vaut pour la technologie d'illustration de Gans et Holden seulement, non en général. |
| 2. Profondeur | 4 | 4 | Fable : loi fermée du second regard (t²/f × (1 − ρ₀) à allure fixée, t/√f à horizon), marge de la référence, référence finie (f nul inétablissable). Opus : réduction exacte du pire cas (sabotage qui imite l'échec honnête = honnête plus défaillant, en fractions exactes), cinq entrées chiffrées ; constantes non contre-lues. |
| 3. Originalité | 3 | 4 | Opus apporte quatre objets absents de Fable : la réduction du pire cas, le passé figé (poids et contextes gardés, le défenseur joue en dernier), la lecture en régime d'excès du seuil de dissuasion, le coût de réparation et le dommage irréversible à l'alarme. Fable apporte la loi et le second emploi de la recapture. |
| 4. Honnêteté, R8 | 4 | 3 | Fable : aucune recherche d'antériorité, déclaré ; « non trouvé » jamais « libre » ; sa v1 était tombée dans « trop beau », corrigée. Opus : trois recherches en ligne et une antériorité trouvée ; déclare honnêtement sa non-indépendance sur le saboteur lent ; mais ne lit pas Singh et écrit « aucun texte ne borne le dommage accumulé avant l'alarme », faux à la source (§ 4). |
| 5. Règles et nœuds | 5 | 3 | Fable : couple neutre pour le collisionneur passé à la garde de motifs (protocole X), invariant de l'oracle respecté (D-4), mesure sur devis. Opus : pas de couple pour le collisionneur ; propose Carbon puis des lecteurs extérieurs, ce qui saute l'étape du protocole X (contact externe bien dit nœud). |
| 6. Actionnabilité | 4 | 4 | Fable : critères de mort chiffrés (borne basse de t/√f sous 2), étapes ordonnées. Opus : règle d'instrument immédiate (D-2), test de mort sur banc public (D-4), deux grandeurs à rapporter (D-3). |
| 7. Coût | 4 | 4 | Les deux : 0 USD jusqu'ici. Fable écarte un recalcul de faible valeur ; Opus propose des passes avant d'un modèle de 8 milliards de paramètres, gratuites sur processeur mais lentes, sinon devis. |
| 8. Ce qui manque | 3 | 3 | Fable : ni pire cas énoncé, ni dissuasion, ni fenêtre de réversibilité, ni Greenblatt et Shlegeris. Opus : Singh absent (le principal occupant du régime d'excès), Li et al. absent, pas de loi fermée, pas d'analyse de la référence finie pour f nul. Aucune des deux : plusieurs agents (papier B), mode tenu à l'écart (N-054), lien avec N-077. |
| Total, pour information | 32 | 29 | |

## 3. Ce que chacune a que l'autre n'a pas

**Fable seulement.** La loi fermée du second regard et ses quatre régimes (allure fixée, horizon donné, marge de la référence, f nul) ; l'horizon de signature d'une référence finie, ≈ 0,8 m à 20 % d'audit (en général α m/(3 q ρ₀), remarque A de la vérification) ; la lecture prudente des comptes publiés (t²/f de 0,3 à 1,4) ; Singh p. 52, plus fort contre-argument imprimé à la valeur du contraste « sabotage contre incompétence » ; Li et al., lemme A.5 ; le couple neutre pour le collisionneur ; des probabilités chiffrées, avec leur règle de combinaison.

**Opus seulement.** La réduction exacte du pire cas, avec son occupation de forme (Wang, théorème 11 ; « Blindfold », théorème 6) ; la règle « une quantité tenue par l'adversaire n'entre que dans un sens » (« Blindfold », p. 12) appliquée à chaque entrée ; le passé figé et la règle de garder l'empreinte des poids et le contexte complet ; la formule du dommage irréversible (1 − r·f)·k, qui fait de la réversibilité le levier ; la trouvaille qu'une lecture apprise « dommage contre pas de dommage » peut faire pire que le hasard (×0,53) ; la restriction de la règle à deux clés aux strates « excès » (dans une strate « signature », elle retarde la prise) ; la dissuasion ; Greenblatt et Shlegeris 2024 ; Podkopaev et Ramdas lus en entier.

## 4. Contradictions, tranchées à la source

1. **« Aucun texte ne borne le dommage accumulé avant l'alarme »** (Opus, § 2). Faux : Singh, p. 9 : « Mixture monitoring bounds cumulative excess above the registered reference for every adapted adversary ». Fable a raison. La phrase d'Opus ne vaut que pour ses trois textes ; à corriger avant tout emploi.
2. **L'antériorité du rappel après l'alarme.** Fable (P2) donne pour différence nette « la relecture rétroactive d'états consignés ». Greenblatt et Shlegeris 2024 écrivent déjà « apply these improved monitoring techniques to previous actions » et « save activations that we want to apply updated probes to » (page versée, présente). Opus a raison ; la différence se resserre à la réparation d'un dommage diffus, comptée à étiquettes égales, apprise contre des échecs honnêtes. Page web : à confirmer sur une source opposable.
3. **Sur quoi apprendre la sonde de rappel.** Pas une contradiction : les deux montrent que « endommagé contre sain » retrouve surtout des échecs honnêtes (Fable, bloc E4 : 0,27 à 0,32 contre 0,25 ; Opus, bloc D : jusqu'à ×0,53 du hasard). Remèdes différents et compatibles : Opus apprend contre les échecs honnêtes de la référence ; Fable sur les épisodes « endommagés et marqués ». Les deux bras se gardent.
4. **Recalculer sur le banc public de Kezendirane** : Fable (D-5) dit non, Opus (D-4) dit oui. Ce ne sont pas les mêmes mesures : Fable recalculerait (t, f) d'un moniteur de texte, déjà lus au point (table 3, p. 6) ; Opus recalculerait les états internes par une passe avant et mesurerait φ et τ d'une sonde. La réserve de Fable vaut pour les deux : 14 tentatives, et des manipulations de score d'un agent sans consigne, non un sabotage fait pour ressembler à l'échec honnête ; Kezendirane l'imprime (« cannot separate a deliberate shortcut from confusion », p. 4). Opus a raison sur la mesure boîte blanche, à faire comme test de mort seulement, et faible même comme tel.
5. **Le seul changement de régime.** Fable : f nul (régime de signature), inétablissable sur une référence finie. Opus : la dissuasion, levier fermé. Les deux tiennent à leur source et ne se contredisent pas ; aucun n'est accessible au programme aujourd'hui.

Point de convergence chiffré : à horizon donné, le gain de Fable vaut t/√f ; le rapport des plateaux d'Opus vaut 0,30, et tend vers 0,25 quand m grandit, soit un gain de l'ordre de τ/√φ = 3,6. C'est la même constante, trouvée par deux voies. La convergence n'est pas pleinement indépendante sur le saboteur lent (déclaré par Opus).

## 5. Synthèse recommandée pour Lazar

**En clair.** Une sonde qui lit l'intérieur de l'agent rend l'alarme plus rapide, d'un facteur qui dépend de deux nombres : la part des sabotages qu'elle marque et la part des échecs honnêtes qu'elle marque à tort. Elle ne change pas la nature de la garantie : un saboteur assez lent, ou qui imite les échecs honnêtes jusque dans son intérieur, passe encore. Ce qui fixe la limite, c'est la qualité de la référence honnête. Ce qui rendrait réparable le dommage déjà fait, c'est une fenêtre où ses effets restent réversibles.

**Ce qu'il faut retenir.**
- Pas de percée par la boîte blanche, au sens du critère. Le gain est une constante à mesurer, (τ, φ), sur des échecs honnêtes appariés.
- L'effort de percée va sur la référence honnête en service (N-076, point 1 ; N-075, § 11, point 5) et sur la réversibilité.

**Décisions qui changent ou s'ajoutent.**
- D-2 de Fable (une ligne de mesure, sans critère de porte) : inchangée.
- D-3 de Fable (erratum de « dominé ») : ajouter la restriction d'Opus : le gain ne vaut que dans les strates « excès » ; dans une strate « signature », la seconde clé retarde la prise.
- D-4 de Fable (rappel après l'alarme) : citer Greenblatt et Shlegeris 2024 ; resserrer la différence nette ; écrire les deux bras d'apprentissage ; proscrire « dommage contre pas de dommage ».
- D-2 d'Opus (garder l'empreinte des poids et le contexte complet) : à adopter comme règle d'instrument, pour les organismes à poids ouverts seulement. Coût faible ; sans cela, l'entrée après l'alarme reste fermée.
- D-3 d'Opus (rapporter le coût de réparation et le dommage irréversible à l'alarme, fenêtre déclarée) : à adopter.
- D-5 de Fable contre D-4 d'Opus : faire la mesure boîte blanche du banc public comme test de mort seulement, sur processeur, licence vérifiée ; sinon devis.
- Antériorité : garder la D-6 de Fable (collisionneur sur le couple v2, protocole X), et y verser les questions 1 à 4 de l'annexe A d'Opus, réécrites au gabarit neutre. Carbon et les lecteurs extérieurs viennent après ; le contact externe reste un nœud.
- La dissuasion d'Opus : versée comme trouvaille, rien revendiqué. Le levier est fermé (N-053, point 5), et le seuil de 13,5 % ne vaut que pour l'exemple de Gans et Holden.
- Avant tout emploi de la note d'Opus : corriger la phrase sur Singh, l'emploi du 0,42 de Gan, et rejouer ses blocs A et B.
