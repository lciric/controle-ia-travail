"""Cherche dans le brouillon 7 (espaces normalisés) le texte nouveau de chaque correction des deux contre-lectures du
brouillon 6, recopié des rapports (lecture E-01 : « deux lectures » -> « trois lectures » où la table le déclare), et
l'absence des anciens textes remplacés — v1. Usage : python3 -B -I mots_exacts_b7_v1.py BROUILLON7 BROUILLON6"""
import sys, re
n = lambda s: re.sub(r"\s+", " ", s)
T = n(open(sys.argv[1], encoding="utf-8").read()); T6 = n(open(sys.argv[2], encoding="utf-8").read())
NOUVEAUX = {
 "texte-01.1": "Exception, P-021 : sous (B), les deux tableaux de la version recommandée (sections « Prédiction » et « Critères de lecture gelés ») et ses paragraphes « Trois lectures », « Clause de repli mécanique » et « Sans le bras … » restent au texte scellé, sans en-tête ni marqueur, leur ligne C-P3b étant remplacée par la version (B) ; sous (C), seul le tableau de la section « Prédiction » reste, réduit à ses colonnes « id » et « grandeur », avec le paragraphe « Trois lectures » et la phrase « Sans le bras … ».",
 "texte-01.2 (E-01)": "C-P3a et C-P3c comme au tableau de la version recommandée, gardé (verrou 1), trois lectures et clause de repli comprises ;",
 "texte-01.3": "les statistiques définies à la colonne « grandeur » du tableau de la version recommandée, gardé (verrou 1) (W de C-P3a,",
 "texte-01.4": "C-P3a et C-P3c comme au tableau de la version recommandée, gardé (verrou 1) ;",
 "texte-01.5": "seuils et lectures du bloc P-021 (section « Prédiction »), selon la version retenue ;",
 "texte-02 point 5": "Aucune condition « constat nu » n'est lue (décision de Lazar P-022, option (a) ou (c)).",
 "texte-02 TC.1 (a)": "Aucune condition « constat nu » n'est lue (décision de Lazar P-022, option (a)) ;",
 "texte-02 TC.1 (c)": "Aucune condition « constat nu » n'est lue ici (décision de Lazar P-022, option (c)) ; la réserve 16 reste seule ; C-P6 (juges) se lit « usurpation stylistique portant un constat », sans attribution au style ; champ `constat_nu` retiré de la configuration scellée ;",
 "texte-02 rés. 9 corps": "(réserve 16). C-P6",
 "texte-02 rés. 9 rec": "Le contraste « style contre contenu » est Ḡ_4 − g_constat (Plan, TC.1).",
 "texte-02 rés. 9 repli": "Aucun contraste « style contre contenu » n'est mesuré dans ce texte.",
 "texte-03 rés. 17": "17. **Personne grammaticale et indice** (CW-04 de la note `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cv2-03/lecture-voisins-cv2-03-v1.md`, `9d94ae66…` ; comptes par indices, sans texte : `docs/notes/contre-lectures-papier-C-v1/brouillon6/texte/personne_grammaticale_vivier_v2.sortie.txt`, `9a2a36547df8a53bd76663f95eb274addde4df4487e023bf1959105925427189`) : dans trois familles, la personne grammaticale change avec l'indice du vivier. « Flatterie et supplication » : deuxième personne seule aux indices 1 et 2, première et deuxième personne de 3 à 16 (première seule à l'indice 6). « Usurpation stylistique » : voix impersonnelle de 1 à 5, attribution à un rôle nommé de 6 à 16. « Ordres en bande » : adresse directe au lecteur, sauf aux indices 4, 5 et 12, où le lecteur est désigné à la troisième personne ; deuxième personne explicite à 10, 11 et 13 à 16. « Revendication d'autorité » : première personne aux seize indices ; « approbations forgées » : troisième personne ; témoins : voix impersonnelle. Un indice de voix, sans ordre, déplace la déférence de modèles qui répondent (Wang K. et al., 2508.02087v4, p. 12, tableaux 2 et 3) : dans ces trois familles, Ḡ, g_{k_f} et « intensités graduées » se lisent « par formulation entière » (réserve 16) ; aucune part n'est attribuée à l'intensité seule. La personne de chaque formulation retenue est écrite au rapport de l'étape 2 comme étiquette descriptive, jamais comme facteur ni comme critère. Vivier, constantes et longueurs inchangés.",
 "texte-04": "à côté de chaque formulation retenue qui la porte. Comme la contingence occupe les rangs hauts de la famille « flatterie et supplication » et les indices 13 à 16 de « ordres en bande », Ḡ, g_{k_f} et « intensités graduées » de ces familles se lisent « par formulation entière » (même règle que la réserve 16) : aucune part n'en est attribuée à la flatterie ou à l'ordre seuls.",
 "texte-05 1.4": "Sous P-022 (b), l'insertion du constat nu (corpus A) est lue aussi, sur les mêmes contenus, pour la lisibilité seulement ; ces lectures n'entrent ni dans les gains du vivier ni dans l'addendum.",
 "texte-05 TC.1": "Lue au pilote pour la lisibilité seulement (point 1.4) ; elle n'entre pas dans le choix des formulations.",
 "texte-06": "Garde lexicale en échec sur une formulation, un témoin ou l'insertion du constat nu (bloc P-022) :",
 "texte-07 graines": "Clés ajoutées par le brouillon 5 :",
 "texte-07 champs": "`repli_si_refus`), `agent_bras` (`decision_bras_usurpation` écrite ; `usurpation` retiré si P-020 est refusée) et `constat_nu`",
 "texte-07 rés. 14": "Vivier, constantes et longueurs inchangés ; configuration inchangée par cette déclaration.",
 "methode-01.1": "**Trois lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des familles 1 et 4 dans C-P3c), les trois statistiques sont calculées sur la loi nette calibrée, sur la loi nette sans calibrage (ρ = 1) et sur la loi nette calibrée par ρ̂/r̂ (X_i = v̄₀ + (ρ̂/r̂)(v₀_i − v̄₀), ρ̂/r̂ borné à [0,05 ; 1], ρ̂ et r̂ du point 8 bis recalculés dans chaque tirage), mêmes tirages ; « établie » seulement si les trois lectures concluent. Les deux premières ne suffisent pas quand les juges n'ont pas le même modèle d'erreur : sans écart vrai, elles ordonnent alors les juges dans le même sens (vérification courte de méthode du brouillon 6, U1 : C-P3a 0,081 à 0,136 et C-P3b 0,070 à 0,125 sous le nul à g = 0,20) ; la troisième est juste sous l'erreur sur v₀, sous la compression et sous leur mélange (U3 : 0,008 à 0,043 aux trois lectures ; réserve 15).",
 "methode-01.2": "Les trois, pour leurs composantes en Ḡ, aux trois lectures de la loi nette (calibrée ; sans calibrage, ρ = 1 ; calibrée par ρ̂/r̂) : « établie » seulement si les trois concluent ;",
 "methode-01.3 seuil": "trois lectures de la loi nette (bloc P-021)",
 "methode-01.3 en-tête b6": "les trois aux trois lectures de la loi nette (calibrée, sans calibrage, calibrée par ρ̂/r̂)",
 "methode-01.4": "Sous le modèle général (erreur sur v₀ et compression), ρ̂ = (1 − κ) a et r̂ = 1 − κ : ρ̂/r̂ estime a, l'atténuation seule. Pour C-P1, les lectures calibrée et sans calibrage encadrent λ dans ce modèle (U2) ; pour les statistiques de rang, qui comparent des juges dont les modèles peuvent différer, la lecture par ρ̂/r̂ est ajoutée (bloc P-021). La correction suppose une compression linéaire vers le milieu de l'échelle ; une autre forme n'est pas couverte.",
 "methode-01.6": "Statistiques de rang, trois lectures : scénario où les juges ont des modèles d'erreur différents (erreur sur v₀ d'écart type 0,6 ; erreur 0,4 et compression 0,08 ; compression 0,16), même gain vrai g = 0,20, k = 5, 60 tâches, 1 000 essais : C-P3a et C-P3b « établie » au plus 0,06 chacun ; aux deux premières lectures seules, au-dessus de 0,10 (contrôle de l'artefact).",
 "methode-02": "**Clause de repli mécanique.** Si la vérification courte de méthode d'avant le scellement (sous-agent neuf ; contre-lecture 8) trouve, pour C-P3a, C-P3b ou C-P3c telle qu'écrite (toutes ses lectures jointes), un taux de « établie » au-dessus de 0,05 + 2 × √(0,05 × 0,95 / R) (R essais de la case, au moins 1 000) dans au moins une case de la grille qui suit, cette statistique est rapportée sans verdict, écrit tel quel, sans nouveau nœud. Grille : k = 3 et 5 ; 45 et 60 tâches ; corpus B de 30 items ; aucune attaque, puis même attaque chez les trois juges (g = 0,10 et 0,20, λ = 1) ; chaque juge sous l'erreur sur v₀ (écart type 0,3 à 0,6), sous la compression (κ jusqu'à 0,16) ou sous leur mélange, les trois juges pouvant différer ; vrai rééchantillonnage par grappes (au moins 1 000 tirages, mêmes tirages pour les trois juges). Résultat cité avec le chemin et l'empreinte du rapport.",
 "methode-03": "au plus 0,05 chacun (taux par couple juge × famille, sans Holm) ; contrôles de l'artefact, 60 tâches, g = 0,20, 300 essais : sous le modèle v₀ exact et compression κ = 0,16, la lecture calibrée seule donne « vers la moyenne » au-dessus de 0,10 ; sous le modèle erreur sur v₀ d'écart type 0,6, la lecture sans calibrage seule donne « vers la cible » au-dessus de 0,08 ; la règle conjointe reste au plus 0,05 dans les deux (vérification courte de méthode du brouillon 6, U2 : 0,243, 0,117, puis 0,028 au plus)",
 "methode-04": "contre-lecture 8 : vérification courte de méthode de CL5-01 à CL5-03 (rapport `<<CHEMIN_RAPPORT_CL8>>`) ; points (v) à (viii) du projet, section 6.3 : contre-lecture `<<CHEMIN_RAPPORT_CL10>>`",
 "methode-06": "p = (1 + #{τ* ≥ τ}) / (B + 1)",
 "session déc. 3": "(décision de la session : page de l'article publié obtenue sans compte ni connexion, paramètre de refus des cookies ; acceptée par la session comme provenance, réserve déclarée (R-316) ; vaut pour le résumé et le corps)",
 "session déc. 4": "les voisins ajoutés aux « cités comme publiés » sont nommés, Jiang et al. et Wang K. et al. compris",
}
ANCIENS = {
 "texte-02 point 5": "le paragraphe qui précède est retiré",
 "texte-02 TC.1": "sont retirés ;",
 "texte-02 rés. 9": "suit la version recommandée (b)",
 "texte-02 rés. 9 repli": "Elle se lit « (réserve 16) »",
 "texte-05": "Non lue au pilote",
 "texte-07": "Clés ajoutées par ce brouillon",
 "methode-01": "**Deux lectures.**",
 "methode-01 non simulée": "non simulée, d'où la clause qui suit",
 "methode-02": "plus deux erreurs de Monte-Carlo",
 "texte-01 ci-dessus (B)": "comme ci-dessus (deux lectures",
}
for k, v in NOUVEAUX.items():
    c = T.count(n(v))
    print(f"{k:28s} présent {c} fois")
for k, v in ANCIENS.items():
    print(f"ancien {k:28s} b6 {T6.count(n(v))} -> b7 {T.count(n(v))}")
r17 = T.find("17. **Personne grammaticale")
print("réserve 17, suite :", T[T.find("Vivier, constantes et longueurs inchangés.", r17):][:120])
