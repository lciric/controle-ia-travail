# Proposition A — Tour III.2 — Équipe rouge croisée

## 0. Pièces et cadre

- Pièces B et C des faits : coupées (déjà signalé par B et C ; je n'en reconstitue rien). Les conceptions B et C sont transmises en entier (chacune se termine par FIN-DE-CELLULE).
- Statuts : tout ce qui vient des pièces est RAPPORTÉ ; mes inférences sont HYPOTHÈSE ; les chiffres que j'avance sont illustratifs. Les « confiances » sont des jugements de A.
- Garde de sûreté : les « scénarios d'évasion » ci-dessous visent les **instruments de gouvernance** (verdict R13, sceaux, horodatage, plafond, contre-lecture, seuils de porte), jamais les moniteurs. L'adversaire considéré est une session du programme (ou son opérateur) qui veut obtenir « franchie » ou le report, pas un agent saboteur face à des sondes. Là où une proposition touche aux instruments scientifiques (critères 2–4), je m'arrête à la manipulation de la **preuve de porte**.
- Point partagé que j'utilise en le disant (B1) : B et C arrivent au même plafond « 250 USD illustratif, 150 sur le critère 2 puis 100 sur 3–4 ». Cette convergence n'est pas une corroboration : les deux dérivent le même ordre de grandeur de la même arithmétique heures-GPU × 2–4 USD, elle-même illustrative. Une « recommandation commune » au sens des critères de lecture, oui ; une borne fondée, non.

---

## Contre la proposition B

### (a) Failles

**F-B1. L'exception « NT-réfuté sur 2 ou 3 → non franchie sans report » est non scellable en l'état, et presque certainement lettre morte.**
B distingue NT-absent et NT-réfuté selon que la preuve est « produite sous préenregistrement et contraire au critère ». Mais classer un résultat négatif comme *réfutation* plutôt que comme *artefact* exige un audit **après lecture** (R4 : un négatif trop propre déclenche le même audit qu'un positif). B ne donne ni la liste des gardes qui rendent un négatif « valide », ni qui les applique. Le verdict R13 devrait donc juger la validité d'un run : décision laissée au lecteur. De plus (HYPOTHÈSE calendaire) : au 29 octobre aucun organisme n'existe (RAPPORTÉ) et le GO de calcul échoit le 1er novembre (RAPPORTÉ). Un NT-réfuté au 30 novembre suppose un préenregistrement scellé, contre-lu, puis un run complet en novembre sans calcul autorisé. La branche la plus discutable de B (confiance 0,55 chez B) est aussi celle qui ne s'exercera probablement jamais ; elle sert surtout à rendre « at most once » vrai dans la phrase au financeur.

**F-B2. Asymétrie non justifiée.** Pourquoi un NT-réfuté sur 2 ou 3 ferme la porte, mais pas sur 4 (base boîte noire qui ne tourne pas sur le même jeu) ni sur 8 (chiffre faux) ? B ne le dit pas. Un critère d'exception non motivé est une réinterprétation implicite de la hiérarchie des critères.

**F-B3. Le report est déclenché par l'acteur qui en bénéficie.** Chez B, « non concluante » ouvre le report, et presque tout devient NC si l'horodatage externe est absent (S12, C10 : « SUPPOSÉ indisponible aujourd'hui »). Ne pas installer l'horodatage garantit le report. Même mécanique pour le critère 8 : « document trouvé hors manifeste = NC », mais aucun instrument ne cherche ces documents ; celui qui construit le manifeste choisit ce que le verdict voit. Variable confondante : la cause du NC (retard réel ou inaction stratégique) est indistinguable au 30 novembre.

**F-B4. Fuite constructeur/évaluateur dans E1 et E2.** Les 40 dossiers d'E1 et les 20 jumeaux d'E2 sont fabriqués par le programme — donc par quelqu'un qui connaît les bords de la règle et les points faibles du contre-lecteur. Les « réinterprétations plantées » sont celles que l'auteur imagine ; celles qu'il n'imagine pas ne sont pas testées. Le contrôle négatif d'E1 (clause vague → accord < 0,7) mesure la sensibilité des agents à la vagueté en général, pas l'univocité de *cette* clause : un accord élevé peut venir d'un a priori partagé par trois instances de même famille.

**F-B5. E3 viole B4.** H_A (« le goulot est le calcul ») et H_B (« le goulot est l'attention ») ne sont ni exclusives ni exhaustives ; B l'admet (« si le groupe 6, 7, 8 ne bouge pas non plus… »). Avec n = 1 report, c'est une observation, pas une expérience ; elle ne falsifie rien sur la règle.

**F-B6. E4 est vraie par construction.** Trois artefacts (double compte, devise, date postérieure) et un seuil de 100 % : le script sera écrit pour ces trois cas. L'artefact qui compte — un devis **absent du registre** (calcul payé hors programme, SUPPOSÉ possible) — n'est pas dans la liste.

**F-B7. « Le GO confirme ou suspend » est un report déguisé.** Une suspension sans échéance ni défaut est une décision après lecture. C8 fixe un défaut si le GO est *absent*, pas si le GO *suspend*. Que devient la coupure du 31 janvier si le GO du 30 novembre est suspendu le 15 décembre ? Non écrit.

**F-B8. Déblocage de 3 et 4 sur « dossier du critère 2 scellé ».** Scellé ≠ tenu. Si le dossier scellé du critère 2 est négatif, B dépense la tranche 2 sur une branche déjà morte au verdict du 31 janvier (NT domine). La condition mécanique est bien mécanique, mais elle ne protège pas l'argent qu'elle prétend borner.

**F-B9. Sceaux de référence dans le dépôt.** B gèle les critères « par empreinte » et met l'empreinte de référence dans le préenregistrement du verdict, lui-même un fichier du dépôt. Qui tient la copie de référence hors d'atteinte de la session ? Non dit. (Même faille chez C, F-C6.)

### (b) Scénarios d'évasion (niveau gouvernance)

| Instrument de B | Comment une session le trompe | Coût (HYPOTHÈSE) |
|---|---|---|
| Sous-agent de verdict R13 | Il « inspecte les fichiers listés ». On omet du manifeste tout ce qui gêne ; les empreintes des fichiers listés sont correctes. | Nul |
| Sceau sha256 | Modifier, recalculer, commettre ; si la référence est dans le dépôt, remplacer la référence. | Un commit |
| Horodatage externe « à choisir » | Choisir un service que l'on contrôle, ou ne rien choisir et laisser tout tomber en NC (F-B3). | Nul |
| Contre-lecture R2 | R2 dit « lui donner explicitement les fichiers à lire » : l'auteur contrôle la liste ; la réinterprétation vit dans un fichier non listé. | Nul |
| Table T/NT/NC | Convertir un NT imminent en NC en laissant une preuve incomplète (contre-lecture sans liste de fichiers, par exemple) : NC donne le report, NT le refuse. | Nul |
| Plafond | Devis non consignés ; devis daté de la veille de la coupure. | Faible |
| GO du directeur | « Suspendre » sans échéance (F-B7). | Nul, mais visible |

**Tous à la fois** : chez B, le constructeur du manifeste, l'auteur du préenregistrement de verdict, le fabricant des dossiers d'E1–E4, le choisisseur de l'horodatage et l'instructeur du contre-lecteur sont une même session (session-depot, RAPPORTÉ comme auteur des pièces). Le seul instrument hors de ses mains est le GO, que B limite à « confirmer ou suspendre ». Coût technique de l'évasion totale : zéro ; coût d'intégrité : total. La règle de B tient sur l'honnêteté d'un acteur unique, ce que l'arbitre doit savoir avant de la sceller.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Négatif-artefact sur le critère 2** : une courbe dose-réponse plate produite par un harnais volontairement cassé (dose non transmise au modèle). Si le protocole de B classe ce cas NT-réfuté et ferme la porte, C5 est falsifiée : l'exception transforme un bug en verdict définitif. H_A : le classement NT-réfuté exige une garde de transmission de dose verte ; H_B : il se contente du préenregistrement. Sans ce contrôle, C5 ne doit pas entrer dans la clause.
2. **Dossier « hash juste, texte changé »** : un critère réécrit puis ré-empreinté, référence mise à jour. Si le verdict passe, le « gel par empreinte » n'est qu'un gel par honnêteté. Fatal pour le point 3 de B.
3. **Document hors manifeste** planté dans le dépôt (et un autre dans une branche orpheline, cf. R-624/R-625 RAPPORTÉ) : le verdict doit rendre NC sur le critère 8. Sans ce contrôle, C6 est une réinterprétation rétrécissante (« hors cadre » probable).
4. **Suspension du GO sans échéance** : un cas d'épreuve où le GO est « suspendu » au 30 novembre ; la clause doit produire une issue sans nouvelle décision. Elle n'en produit pas.
5. **Devis absent** pour E4 (F-B6).
6. **Contrôle d'a priori pour E1** : les mêmes trois agents jugeant des dossiers dont les preuves ont été **permutées entre critères** (preuve du critère 4 placée sous le critère 3). Accord élevé = agents qui ne lisent pas.

---

## Contre la proposition C

### (a) Failles

**F-C1. Inflation de statut, systématique.** C marque « VÉRIFIÉ » des contenus de pièces que personne dans ce collisionneur n'a audités (R-680, N-008, « VÉRIFIÉ dans la Question », « critère 5 VÉRIFIÉ prouvé ») et jusqu'à ses propres ajouts (« classifieur sur la longueur en jetons », « filtre par expressions régulières », présentés en plancher mécanique comme s'ils venaient des faits). Le bon statut est RAPPORTÉ pour les pièces et HYPOTHÈSE pour ces instruments. Dans une cellule dont l'objet est précisément « aucun chiffre non vérifié » (critère 8), ce n'est pas un détail de forme : une règle qui étiquette mal ses propres sources ne peut pas gouverner le critère 8.

**F-C2. La clause contredit le point 1.** L'option 1B dit : critère « non tenu » au 30 novembre → la porte « échoue définitivement dès le 30 novembre » sauf repli technique pré-scellé. La clause (point 4) dit : tout verdict autre que « franchie » ouvre le report « de plein droit », avec pour seule réserve l'interdiction de relancer le même protocole. Les deux textes donnent des issues différentes sur le même dossier (NT sans repli pré-scellé : fermeture selon 1B, report selon la clause). Un couple de textes incohérent est non scellable ; il faut en retirer un.

**F-C3. Le « repli technique pré-inscrit » est une multiplicité d'essais sans correction.** Inscrire d'avance « changement de couche d'extraction ou de famille d'invite » au préenregistrement de G0 autorise, après un NT, un second protocole visant un positif — c'est l'opération que R3 interdit, légitimée par l'antériorité de l'inscription. Avec k replis, la probabilité qu'au moins un passe le plancher par hasard croît ; C ne mentionne ni borne sur k ni correction. (Je ne détaille pas davantage : cela toucherait aux internes de sondes.)

**F-C4. Réinterprétation des critères 2 et 3 sous couvert d'opérationnalisation.** C exige pour « TENU » au critère 2 des « scores finis ≥ 0,99 » — règle issue de R-671, qui concerne les cellules de G1 (RAPPORTÉ) — et propose au choix C1 des seuils chiffrés (ρ_S ≥ 0,80, deux doses dans [0,10 ; 0,70], IC 95 % contre 95e centile). La pièce A dit « sabotage mesurable avec dose-réponse » et « au-dessus du plancher aléatoire apparié », rien de plus. Durcir est modifier. C a raison qu'un critère non chiffré n'est pas scellable (B rencontre le même mur avec le manifeste du critère 8) ; mais C tranche le dilemme en écrivant les seuils dans la règle de repli, c'est-à-dire dans la cellule dont la consigne est « sans toucher aucun critère ». Au minimum, ces seuils doivent sortir de la clause et aller dans le préenregistrement de G0, et la question de leur statut (« procédure » ou « réécriture ») revient à Lazar, pas à C. Fuite supplémentaire (HYPOTHÈSE) : si un pilote « absence de dose diffuse » a déjà tourné (pièce B : « le pilote mesure… », temps indécidable), celui qui fixe la grille de doses l'a peut-être vu.

**F-C5. Le critère 2 devient structurellement non concluant.** C fait dépendre le critère 2 de « la résolution de la stabilité des juges (scores finis ≥ 0,99) ». La pièce B rapporte qu'aucune cellule n'atteint 0,99 sur 180 notations. Si le critère 2 est mesuré « contre une référence cachée » (glossaire) sans juge, cette dépendance est importée à tort ; si un juge intervient, C vient d'écrire une règle sous laquelle le critère 2 est NC tant que la cellule n'est pas redéfinie — et la « redéfinition de cellule » est un levier non scellé. Dans les deux cas : variable confondante entre finitude des juges et existence de la dose-réponse, non séparée.

**F-C6. « Verrou cryptographique » et « dead-man switch » sont des fictions dans un programme à un opérateur.** Le script d'audit « hardcodé et scellé » est un fichier modifiable ; son empreinte de référence est dans le même dépôt. « De plein droit et sans intervention humaine » : un script que personne n'exécute ne produit rien ; la caducité au 31 janvier n'existe que si quelqu'un la constate et la consigne. C présente comme mécanique ce qui est une convention.

**F-C7. Le plafond « min(250 USD ; 5 % du palier) » vaut 0 si le financement n'est pas versé.** 5 % de 0 = 0 : aucune dépense, donc critères 2–4 NC au 31 janvier, donc « non franchie ». C n'a pas testé ce cas limite ; la règle de dépense décide alors de la porte.

**F-C8. La phrase au financeur promet.** « Unspent funds are returned » engage une restitution dont la base contractuelle est SUPPOSÉE (C le marque pour 3B, pas pour 5A). L'arbitre demandait « sans rien promettre ». « Inconvénient : aucun » est de surcroît un superlatif de portée.

**F-C9. Expérience 1 est vraie par construction et sous-dimensionnée.** Dix dossiers (illustratif) ne distinguent pas 100 % de concordance de 90 %. Surtout, les trois instances « exécutent un script d'audit » : si le verdict est le résultat du script, l'accord inter-agents mesure le déterminisme du script, pas celui de la règle. Et `run_factice` est, selon la pièce D, un run factice de bout en bout du code de contrôle ; qu'il produise des dossiers de gouvernance est une HYPOTHÈSE de C, étiquetée VÉRIFIÉ.

**F-C10. Expérience 2 viole B4.** H_A (monotone, ρ_S ≥ 0,80, deux doses intermédiaires) et H_B (bifurcation brutale 0 % → effondrement) laissent un tiers non couvert : dose-réponse diffuse mais non monotone, ou monotone avec une seule dose intermédiaire. Le verdict « NT » tomberait dans ce tiers sans qu'aucune des deux hypothèses soit falsifiée.

### (b) Scénarios d'évasion (niveau gouvernance)

| Instrument de C | Comment une session le trompe | Coût (HYPOTHÈSE) |
|---|---|---|
| Script d'audit à empreintes en dur | Éditer le script, ré-empreinter, commettre. Rien ne tient la référence hors du dépôt. | Un commit |
| Dead-man switch | Ne jamais lancer le verdict et inscrire « en cours » ; ou le lancer tôt sur un dossier choisi. | Nul |
| Seuils de C1 | Fixer la grille de doses après avoir vu le pilote (F-C4) ; choisir ρ_S et l'intervalle pour que deux doses connues y tombent. | Un pilote |
| Repli technique pré-inscrit | En inscrire plusieurs ; chaque NT débloque le suivant. | Rédaction |
| Table NC | Déclencher une garde R5 (score non fini) pour convertir un NT en NC et obtenir le report. | Nul |
| Dépendance « juges ≥ 0,99 » | Redéfinir la cellule jusqu'à atteindre 0,99 ; la redéfinition n'est pas scellée. | Faible |
| Plafond min(250 ; 5 %) | Si le palier est versé tard, dépenser « sur fonds propres » (SUPPOSÉ) hors registre. | Faible |
| Verdict « forcé à NON FRANCHIE si l'empreinte diffère d'un bit » | Inverse : un adversaire **externe** ou une erreur modifie un octet du brief et ferme la porte sans débat — garde d'arrêt sans cas sain testé (R5). | Un octet |

**Tous à la fois** : comme chez B, l'auteur du préenregistrement, du script, des dossiers d'Expérience 1, des seuils de C1 et des replis techniques est une même session ; le « sous-agent neuf » est engendré et instruit par elle. C ajoute un degré de liberté que B n'a pas : les seuils chiffrés et les replis techniques, écrits par la même main avant le 30 novembre. Le coût de l'évasion totale est nul ; la différence avec B est que C fournit plus de leviers « légitimes ».

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Cas d'épreuve de cohérence clause/point 1** : un dossier NT au 30 novembre sans repli pré-scellé. Si la clause et l'option 1B donnent deux issues (c'est le cas sur le texte), la paire est non scellable. Fatal, et constatable sans expérience.
2. **Contrôle positif de la mesure de sabotage** (critère 2) : à dose maximale, l'organisme doit être détecté par la référence cachée. Sans lui, une courbe plate signifie peut-être que la mesure est aveugle, pas qu'il n'y a pas de dose-réponse — et sous 1B, NT ferme la porte. R4 l'exige. Fatal pour l'option 1B.
3. **Permutation des étiquettes de dose** pour ρ_S : C a le d = 0 et l'adaptateur nul, pas le plancher de ρ_S sous permutation. Sans lui, « ρ_S ≥ 0,80 » n'a pas de taux de fausse alerte.
4. **Cas sain pour la garde « un bit → NON FRANCHIE »** : un changement de fin de ligne ou de métadonnée ne doit pas fermer la porte ; sinon la garde n'a pas été testée sur un cas sain (R5).
5. **Dossier « hash juste, texte changé »** (comme pour B) : le script à empreintes en dur doit échouer si la référence a été mise à jour par la même session ; il ne le peut pas sans copie externe.
6. **Plafond à financement nul** (F-C7) : un cas où le palier est 0 au 1er décembre ; la règle doit produire une dépense autorisée définie, pas 0 par accident.
7. **Expérience 1 sans script** : les trois instances jugent les dix dossiers **sans** exécuter le script d'audit, puis avec. Si l'accord est à 100 % seulement avec le script, c'est le script qui est déterministe, pas la table ; la table reste non scellable pour les cas que le script ne couvre pas.
8. **Dépendance juges/critère 2** : un dossier où la dose-réponse est nette mais les scores finis sont à 0,98. Si le verdict rend NC sur le critère 2, C a importé R-671 dans G0 ; à Lazar de dire si c'est voulu.

---

## Ce qui est commun aux deux, et que j'attaque chez les deux

- **Le point faible unique** : un seul acteur fabrique les preuves, les sceaux, les dossiers de test, les seuils et le contre-lecteur. Ni B ni C ne proposent la seule garde qui ne dépend pas de cet acteur : une copie des empreintes de référence (critères, préenregistrement de verdict, script de verdict) tenue par Lazar hors du dépôt, et un horodatage que la session ne choisit pas. Sans cela, « gel par empreinte » est un gel par déclaration.
- **NC ouvre le report** dans les deux : le chemin le moins coûteux vers deux mois de plus est l'inaction ou un artefact. Les deux bornent la récompense au 31 janvier, ce qui est correct ; aucun n'exige que le rapport du 30 novembre consigne, par critère, *pourquoi* la preuve manque (calcul non alloué, horodatage absent, contre-lecture non faite), ce qui rendrait l'inaction visible.
- **Le dilemme « chiffrer, c'est réécrire »** : B le rencontre sur le critère 8 (manifeste), C sur les critères 2 et 3 (seuils). Aucun des deux ne le résout ; les deux le délèguent à Lazar. L'arbitre devrait trancher ce point avant tout le reste, car il décide si une règle mécanique est seulement possible.
- **Le 250 USD commun** est un artefact de même calcul, pas une convergence (voir § 0).

FIN-DE-CELLULE