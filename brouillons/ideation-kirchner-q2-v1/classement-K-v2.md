# Classement K v2 — question 2 de Kirchner (étape D, classeur neuf, second classement sur l'ensemble des fiches)

Écrit le 3 novembre 2026 à 14:33 UTC (`date -u`) ; session commencée à 14:09 UTC.
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/kirchner-classeur-D-v2.md`, sha256 `72281cc47df4aad5fed62dedd0aad2ef1426740a7c9262d7da5ba5cc9c92edf5` (vérifiée avant lecture).
Protocole : `brouillons/ideation-kirchner-q2-v1/protocole-rapport-idees-kirchner-v1.md` (`68919ec9…`), sections 0, 2, 3 ; complément `brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` (`942b9324…`), section 5.
Entrées, empreintes vérifiées avant lecture : fiches `melange-v1/fiches-classement-K-v2.json` (`4db6019a…`, 31 fiches) ; moisson `moisson-C/moisson-fusionnee-v2.json` (`0f019dfb…`) ; pièce `piece-kirchner-v2.md` (`6e7fb1c5…`).
Rien d'autre n'a été ouvert : aucun fichier v1 de ce dossier, aucun des dossiers interdits, aucune recherche, aucun autre modèle.

## 1. Verdict

Ordre final des douze : **KM-15, KM-26, KM-03, KM-10, KM-19, KM-09, KM-30, KM-17, KM-05, KM-25 et KM-11 (ex aequo), KM-23.**
Cohérence : 63 paires sur 66 concordent dans les deux ordres, soit 0,955 : au-dessus de 0,8, mais **presque parfaite pour un juge unique, d'où une réserve** (section 7).
Drapeaux de risque devant ce mentor : 8 des 12 portent « oui » (dont 3 légers), 4 portent « non » (section 6).

## 2. Les douze

Notes : 1 = sous-estimé d'après la moisson ; 2 = lié à ce que fait Kirchner ; 3 = première expérience faisable en jours ; 4 = résultat qui ferait changer d'avis énoncé d'avance (0 à 3, raisons dans `notes-K-v2.json`). Force : Bradley-Terry sous adversaire virtuel déclaré (section 7), moyenne géométrique 1.

| Rang | Fiche | Problème, en une ligne | Notes | Somme (rang) | Victoires sur 22 | Force | Drapeau |
|---|---|---|---|---|---|---|---|
| 1 | KM-15 | Le classement concentre les angles morts d'un moniteur figé : rappel plus bas parmi les violations retenues que sur toutes, sans gradient | 2, 3, 3, 3 | 11 (1) | 22 | 67,41 | oui |
| 2 | KM-26 | Sélectionner au score parmi les passants d'une garde bruitée enrichit les gagnants en pertes de capacité cachées, sans triche | 2, 3, 3, 3 | 11 (3) | 20 | 20,91 | oui, léger |
| 3 | KM-03 | Un gain de surveillabilité obtenu par sélection (son remède déclaré) transfère-t-il à des classes absentes du banc ? | 1, 3, 3, 3 | 10 (5) | 18 | 8,85 | oui |
| 4 | KM-10 | Le forum partagé propage une triche plantée ; la quarantaine au premier signalement la coupe-t-elle ? | 1, 3, 3, 3 | 10 (9) | 16 | 4,33 | non |
| 5 | KM-19 | Les relances d'une méthode de tête entrent au top 3 sous moyenne simple, pas sous un test par e-valeurs dont la nulle contient le meneur | 1, 3, 3, 3 | 10 (11) | 14 | 2,30 | oui, léger |
| 6 | KM-09 | Un moniteur de la même famille que l'agent détecte moins bien les violations de sa famille (plan croisé) | 1, 3, 3, 3 | 10 (8) | 12 | 1,28 | non |
| 7 | KM-30 | Le rappel du moniteur baisse avec le nombre de rivaux affichés (0, 2, 5) | 1, 3, 3, 3 | 10 (6) | 9 | 0,547 | non |
| 8 | KM-17 | Au-delà de la médiane, la part des recombinaisons monte et le rappel du moniteur baisse (organisme) | 2, 2, 3, 3 | 10 (4) | 8 | 0,410 | oui |
| 9 | KM-05 | Une méthode en échec franchit la garde de capacité par resoumission (plus de 0,30 en 16 soumissions) | 1, 3, 3, 3 | 10 (7) | 7 | 0,304 | oui |
| 10–11 | KM-25 | Choisir les meneurs sur le banc tenu à l'écart l'épuise (écart avec un second banc jamais utilisé) | 1, 3, 3, 3 | 10 (12) | 3 | 0,0763 | oui, léger |
| 10–11 | KM-11 | Deux moniteurs de même famille ratent ensemble les mêmes tricheries (co-ratage, étages empilés) | 1, 3, 3, 3 | 10 (10) | 3 | 0,0763 | non |
| 12 | KM-23 | Une garde plus bruitée pousse les relances au top 3 et dégrade la séparabilité d'un moniteur tenu à l'écart | 2, 3, 3, 3 | 11 (2) | 0 | 0,0158 | oui |

Coupure des douze par somme : 11 pour KM-15, KM-23, KM-26 ; 10 pour KM-17 (premier critère 2), puis neuf fiches à égalité sur les deux premiers critères pour huit places, départagées par le compte de la moisson (moins de travaux sur le même problème avec la même mesure d'abord) : KM-24, compte 3, est la première écartée.

## 3. Ce que les paires ont changé à l'ordre des sommes

- **KM-23**, deuxième par somme, perd toutes ses paires : son mécanisme attribue les relances (26 sur 39) aux faux rejets de la garde, alors que le §7 de son article les explique par « a lottery on a fixed-quality model » (relevé de la moisson). Sur « plus juste », elle perd partout.
- **KM-17** recule (4e → 8e) : la classe de triche mesurée (recombinaisons jugées par le nul v8) n'existe que dans l'organisme ; KM-15 dit la même inquiétude de façon générale, dans son harnais.
- **KM-10** monte (9e → 4e) : la contagion de la triche par le forum est absente de ses textes (il n'en mesure que l'apport à la marge), l'expérience tourne dans le harnais ouvert, et un remède (quarantaine) est mesuré.
- **KM-25 et KM-11** finissent en bas : l'une décrit une limite qu'il écrit lui-même (« The held-out benchmark is therefore a validation set for that choice ») ; l'autre a une hypothèse centrale contredite en partie par arXiv:2608.16190 (« Pretraining lineage ... does not pay »), contradiction proposée par la moisson, non tranchée.

## 4. Porte et manques

- 31 fiches lues, 31 dans le sujet (protocole, section 2), aucune hors sujet.
- **Sans les trois éléments de la question** (gardées et classées, manque noté, jamais complété) : KM-04, KM-06, KM-13, dont le résultat qui ferait changer d'avis est vide (noté 0 au quatrième critère ; lu sur leur mesure qui tue, elles auraient 7, 9 et 7, sans effet sur les douze). Partiels : KM-01 (quelques instruments seulement) ; KM-09 et KM-10 (une seule version donne le résultat) ; KM-27 (tension interne : « sans gain sur le banc tenu à l'écart » dans l'énoncé, gain d'environ six points supposé dans le résultat).
- Aucune fiche n'argumente par écrit pourquoi son problème serait sous-estimé (aucun champ ne le porte) : seul le premier critère, par la moisson, en juge.
- Aucune fiche n'est « ouverte » à la moisson : le premier critère plafonne à 2 (neuf fiches à 2, dix-neuf à 1, trois à 0 : KM-08, KM-16, KM-20, « déjà fait »).

## 5. Hors des douze (19 fiches), par somme

KM-24 (10 ; compte 3) ; KM-02, KM-07, KM-12, KM-22 (9 ; lien à Kirchner par analogie seulement) ; KM-21 (9 ; 195 heures de carte, environ 8 jours sur une carte) ; KM-27, KM-28, KM-29, KM-31 (9 ; transposition partielle) ; KM-20 (9 ; déjà fait) ; KM-18, KM-14 (8) ; KM-08, KM-16 (8 ; déjà fait) ; KM-01 (7) ; KM-06 (6) ; KM-13, KM-04 (5).

## 6. Drapeaux de risque devant ce mentor (affirmation qu'il pourrait contredire de ses propres textes)

Les douze ici ; les 31 dans `notes-K-v2.json`.
- **KM-15, oui** : elle lit « Only one reached the top three » et « 2,4 % signalés » comme une lecture rassurante ou une borne ; il peut répondre qu'il n'a rien affirmé de tel et qu'il concède déjà que ses agents « are not strongly trying to evade detection » (§8.2) ; la figure 32 et l'annexe G n'ont pas été lues.
- **KM-26, oui, léger** : il écrit déjà que la garde « rules out a collapse rather than certifying that capability is unchanged » (annexe A.4) et que les méthodes « may harm unmeasured capabilities » (§8.1) ; le neuf est l'effet de la sélection, pas la limite de la garde.
- **KM-03, oui** : son remède s'intitule « Training AARs to be more monitorable » ; un échec du transfert par simple sélection ne le « contredit » pas, comme la fiche l'écrit.
- **KM-10, non** : son moniteur est après coup (§8.2) ; rien dans la fiche ne contredit ses textes.
- **KM-19, oui, léger** : son score est la moyenne géométrique des fractions d'écart comblé sur 3 à 5 bancs (§2.2), pas une « moyenne simple ».
- **KM-09, non** : les indices contraires (billet de Williams, arXiv:2608.16190) ne sont pas de lui.
- **KM-30, non**.
- **KM-17, oui** : sa figure 32b (aucune tentative de copie de format ni de tromperie du relecteur au top 3) peut lui servir contre « au-delà de la médiane, gagner passe par la recombinaison ».
- **KM-05, oui** : même annexe A.4 ; il peut répondre que la garde ne promet rien près du seuil.
- **KM-25, oui, léger** : « The held-out benchmark is therefore a validation set for that choice » ; la présenter comme un angle mort l'expose à sa propre phrase.
- **KM-11, non** : la contradiction partielle vient d'un autre travail.
- **KM-23, oui, le plus net** : son §7 donne aux relances une autre raison que celle de la fiche.
- **Transversal** : toute fiche dont la valeur repose sur « ses textes ne mesurent pas le rappel de son moniteur » (parmi les douze : KM-15, KM-03, KM-09, KM-11, KM-30) dépend d'une lecture faite sans les annexes F et G ni la figure 32 ; la pièce dit « à vérifier en G avant de l'affirmer ».

## 7. Comparaisons par paires, forces, cohérence

- 66 paires × 2 ordres = 132 jugements, présentés dans l'ordre tiré par `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(132)`, e = 5599664949263200258 (16 premiers hexadécimaux du sha256 des fiches) ; indice 2k = paire k (identifiants triés, ordre lexicographique) dans l'ordre direct, 2k+1 dans l'ordre inverse. Chaque lot de onze jugements a été écrit dans `paires-K-v2.jsonl` dès qu'il était rendu, chaque ligne vérifiée contre le tirage à l'écriture.
- Question gelée : « laquelle ferait une réponse à cette question de Kirchner plus juste, plus originale et plus mémorable pour lui, sur ces quatre critères ? ».
- Script `bradley_terry_kirchner_v2.py` (numpy 2.4.6, Python 3.13.18) : ses 14 épreuves de gardes, rejouées à chaque exécution avant les vrais jugements, sont toutes tenues. Cas sains : fichier bien formé accepté ; forces connues retrouvées (écart maximal des logarithmes 0,055, corrélation des rangs 1) ; cohérence 1 pour un juge constant, 0 pour un juge qui prend toujours le premier présenté ; seuils lus comme prévu. Artefacts, tous arrêtés : ligne manquante, présentation en double, choix hors paire, identifiant inconnu, ordre non tiré, A et B intervertis, onze identifiants, élément qui gagne tout sans régularisation déclarée, non-convergence ; et, pour l'élément qui gagne tout avec régularisation déclarée, l'estimateur sort annoncé comme tel, l'élément en tête.
- **Le maximum de vraisemblance n'existe pas** : KM-15 gagne ses 22 jugements, KM-23 les perd tous, le graphe des victoires n'est pas fortement connexe. Le script le dit et donne les forces sous l'adversaire virtuel déclaré à l'avance (une victoire et une défaite de chaque fiche contre lui). Pour les deux extrêmes, seul l'ordre est informatif ; la taille de leur force tient à cet adversaire.
- **Cohérence 0,955** (63 sur 66). Les trois paires discordantes, (KM-05, KM-17), (KM-11, KM-25) et (KM-17, KM-30), vont toutes à la fiche présentée en premier : un effet de primauté sur les paires serrées. Choix du premier présenté : 69 sur 132 (0,523).

## 8. Réserves

1. **Cohérence presque parfaite d'un juge unique.** Le même juge a fait les 132 jugements en gardant les précédents en mémoire ; la concordance des deux ordres ne mesure donc pas l'accord entre juges, et l'ordre n'est pas opposable sans un second juge indépendant.
2. **Égalité exacte KM-11 = KM-25** : mêmes victoires et défaites hors de leur face-à-face (1–1). L'ordre affiché par la sortie du script (KM-25 avant KM-11) tient à un écart de calcul de 1,4 × 10⁻¹⁷, pas aux données : défaut du script, qui trie par la force avant d'appliquer le départage déclaré (victoires, puis identifiant). Déclaré ici, sortie non réécrite (R12).
3. **Forces sous adversaire virtuel** (section 7 ci-dessus) : la sensibilité calculée est le même estimateur, puisque le maximum de vraisemblance n'existe pas ; aucune autre estimation n'est rapportée.
4. **Deuxième critère** : les 3 pour les mesures de moniteur reposent sur « ses textes ne le mesurent pas », constat fait sans les annexes F et G ni la figure 32. Si l'annexe G valide déjà son moniteur, plusieurs 3 tombent à 2 et la coupure se déplace vers KM-02, KM-07, KM-12, KM-22. Les règles d'application des critères 2 et 3 sont les miennes, écrites avant les comparaisons (`notes-K-v2.json`) : un autre classeur pourrait trancher autrement les cas limites (KM-08, KM-17, KM-20, KM-21, KM-22).
5. **Premier critère** : la moisson est non opposable (métadonnées et résumés). Le billet LessWrong moDKmh4GerCjfB5mM, le plus proche de KM-15 par le titre, n'a pas été ouvert ; il faut l'ouvrir avant toute lecture « ouverte ». KM-20 est « déjà fait », mais la moisson laisse au directeur la lecture « voisin proche » : elle entrerait alors dans les douze à la place de KM-25. KM-03 lue « lointain » ne change pas les douze.
6. **« Plus juste » dans les paires** s'appuie sur des contradictions et tensions que la moisson propose sans les trancher (KM-11, KM-25, KM-09, et sa note sur le §7 pour KM-23). Si le directeur les écarte, KM-09 et KM-11 pourraient remonter.
7. **Forme des fiches** : deux fiches, KM-08 et KM-16, se distinguent par leur forme (première personne, une seule version, tous les champs remplis). Si la forme trahit une origine, l'aveuglement du classeur en souffre. Je ne m'en suis pas servi : leur premier critère suit la moisson (déjà fait : 0), et aucune n'est dans les douze.
8. Les coûts marqués « supposé » ont été pris tels qu'écrits ; aucun n'a été vérifié.

## 9. Fichiers (dossier `/home/claude/scratch/kirchner-rapport/classement-D/`)

- `notes-K-v2.json` — sha256 `3aec95b831c5c7ee820303be40fa7a8b852065a31a7ac628e6b75479ea206ba3`
- `paires-K-v2.jsonl` — sha256 `9af38659aaba743c043ab63ad0d4527c7206e5dc4cccb9907182ad9c42914c2b`
- `bradley_terry_kirchner_v2.py` — sha256 `ead660835af64a2eba07e5ec9732d982d168530a343d5cfbbb754e44895c3f72`
- `bradley_terry_kirchner_v2-sortie.json` — sha256 `fa13c05015ff6d0b4d42ef0002e9ded39ad19eea1fa8cd33fbd2385b7e3713f5`
- `classement-K-v2.md` (ce fichier) : son empreinte figure dans le rapport de remise.
