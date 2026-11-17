# Contre-lecture neuve (R2), seconde lecture — plan de lecture de la recourse de B-7, v2 — v1

Même contre-lecteur que pour la première lecture (n'a rien écrit des pièces). Branche `prep/neuron-lens-v1`. Aucun fichier de résultat de
`diag/20261117-015632-…` ni de `runs/…` ouvert (noms listés seulement), ni `diag/20261115-120622-…`, ni le verdict R-2915. J'ai relu le **code** du dépôt
(`b_alpha_lancer_v5.py`, `verdicts_b_alpha_v3.py`, lecture seule, rien exécuté) uniquement pour vérifier des noms de fichiers et de champs cités par le plan.
Aucune commande `vastai`, aucune variable d'environnement, aucun fichier existant modifié, aucun commit. Seul ajout : ce fichier.

## Verdict

**À corriger** — retouches courtes, sans refonte : la bloquante et les cinq majeures de la v1 sont corrigées ; restent deux choix laissés au lecteur après
résultat (écart « de (a) » par cellule ou en maximum ; issue de l'audit de B-7 « non tenu » dans les phrases permises) et quelques précisions de noms.

## État des défauts de la première lecture

- **Bloquante B1** (graine 1 en chaîne en défaut) : **corrigée**, lignes 120-122 (« (3) se calcule même si la graine 1 tombe en chaîne en défaut ; la chaîne
  en défaut est rapportée à côté et ne change pas (3) »), conforme à la réserve 2 de la v8.
- **M1** (procédure de l'audit) : **corrigée pour l'essentiel**, lignes 53-56 : audit joué ⇔ fichier d'étape présent ; noms `b-alpha-audit-trop-beau.json`,
  `b-alpha-audit-trop-beau-lot64.json`, `b-alpha-audit-tout-negatif.json` **exacts** (le lanceur v5 écrit `b-alpha-{étape}.json`, étapes de ces noms) ; champs
  `audits_requis`, `motifs_audit`, `audit_b7_par_le_haut` **exacts** ; divergence course/fichiers rapportée. Reste le point n° 3 ci-dessous.
- **M2** (calcul de (3)) : **corrigée**, lignes 120-121 et 50-52 : calcul propre d'abord, comparaison ensuite à `verdict_b7` / `par_le_haut`, désaccord rapporté.
- **M3** (audits) : **corrigée** : « mesures touchées » fixées (103-104) ; audit joué non déclenché par le lecteur : divergence et verdicts sous les deux lectures
  (106-107) ; lecture des audits joués, « proposé », décision de Lazar (108-111). Voir points 4 et 7 pour les restes.
- **M4** (comparaisons) : **corrigée en grande partie** : couches 0 à 30, quatre lentilles, « dans le bruit » ⇔ inférieur ou égal au maximum de (c) (138-145).
  Reste le point n° 1 (cellule ou maximum).
- **M5** (exposition du lecteur) : **corrigée** : étape 0 avec déclaration écrite avant tout fichier de `diag/`, interdiction de `diag/20261115-…` et de R-2915 jusqu'à
  l'étape 6, source du verdict de B-7 de la RTX 4090 = R-2915 « tel qu'écrit » (31-34, 57-58).
- **Mineures** : float32 / « contrôlé à B0 » (75-77), `0.0` ou `-0.0` (100), « par le haut et par le bas » (91), formules « confirmé / non confirmé » (123-124), « n'a pas
  été jouée » (131), « non comparable » (147), ajouts déclarés (161-162) : **corrigées**. Reste ouverte : renvoi à l'empreinte du plan scellé dans `verdict-recourse-b7-v1.md`
  (trivial). La v2 dit « huit mineures » (ligne 4) ; mon rapport en numérotait sept : sans conséquence.

## Défauts nouveaux ou restants

### Majeures

1. **« Un écart (a) est dit "dans le bruit" s'il est inférieur ou égal à l'écart maximal de (c) » (lignes 143-145)** : « un écart (a) » peut être une cellule (couche × lentille ×
   cible) ou le maximum de (a). Le lecteur choisirait après avoir vu les chiffres, et la phrase serait vraie ou fausse selon le choix. À fixer : « le maximum de (a), par cible (« ablate win »,
   « ablate pos »), comparé au maximum de (c) ; les cellules individuelles sont rapportées sans cette phrase » (ou la règle inverse, mais écrite).
2. **Audit de B-7 « non tenu » : issue absente des phrases permises et du verdict de B-7 de la recourse (lignes 129-133, 146-148).** Le § 4 ne traite que « chaîne en défaut » et « non
   jouée ». Or lignes 123-125 : audit non tenu → « non reproduit par le haut, non confirmé à la graine 1 », « aucune lecture par le haut », lecture de la troisième course en vigueur. Que devient alors
   « le verdict de B-7 de la recourse » (lot 64) et la phrase « B-7 dépend du lot / du matériel » (le verdict « non reproduit par le haut, non confirmé » compte-t-il comme verdict de B-7 pour « diffère » ?).
   À écrire : audit non tenu au lot 64 → « aucune lecture de B-7 de la recourse » (la lecture de la troisième course reste en vigueur) ; pour « diffère » / « non comparable », une série dont l'audit ne tient
   pas est « sans lecture » = « non comparable ». Idem si c'est le calcul du lecteur qui déclenche un audit que la course n'a pas joué (lignes 105-106 : aucun verdict de B-7 pour la série, donc, au lot 64,
   aucun verdict de B-7 de la recourse : à dire aussi au § 4).

### Mineures

3. **Noms de pièces de la graine 1 (lignes 53-56, 116-121).** « les grandeurs de la graine 1 » sans nom, alors que le lanceur v5 écrit `grandeurs-par-pole-b-alpha-graine1[-lot64]-v1.json` et que les `n` de la graine 1
   sont aussi dans la clé `grandeurs.n` du résultat de l'audit (`b-alpha-audit-trop-beau[-lot64].json`, où se trouvent aussi `temoin_bien_apparie` et `pilotage_norme_non_nulle`). Le plan ne dit pas non plus
   où se lit `(1)`/`(2)`. À nommer (et dire quelle source fait foi si fichier et clé divergent : divergence rapportée).
4. **Ordre de calcul de (3).** Les pièces de l'audit sont introduites au point 5, après `b-alpha-verdicts*.json`, alors que (3) doit être calculé avant (étape 4). Un même fichier d'étape (`audit-trop-beau`)
   sert au motif « trop beau » et au motif « B-7 par le haut » (lanceur v5, lignes 820-826) : sa seule présence ne dit pas lequel a été requis. À écrire : existence des fichiers d'audit constatée **avant** l'étape 4
   (liste de noms), (3) calculé à l'étape 4 si le fichier existe, `motifs_audit` lu seulement à l'étape 5 pour dire quel motif.
5. **« Mesures touchées » (103-104)** : B-4 (valeurs de `npR` « steer 1x », rapportées) n'est pas citée pour « trop beau » ; une précision de plus, déclarée « fixée ici ». Dire aussi que ce n'est pas recopié du texte gelé (§ 1
   dit « toutes sont recopiées ») : ligne 103 en tient déjà la marque, ajouter « (précision du plan, ligne 161) ».
6. **Déclaration de l'étape 0 (ligne 32-34)** : écrite « par écrit avant d'ouvrir un fichier de `diag/` » mais sans lieu ni horodatage vérifiables. Demander un fichier court distinct, scellé, avec `date -u`, avant l'étape 1, ou
   à défaut la déclarer en tête du verdict avec l'heure de début.
7. **Audit « tout négatif » joué (ligne 110-111)** : « aucun verdict après lui sans la décision de Lazar » est repris ; ajouter que la mesure touchée (verdict de reproduction de la série) est alors **proposée**, comme pour « trop beau » (108-110), pour
   que la sortie ne soit pas lue comme verdict.
8. **Renvoi d'empreinte** : `verdict-recourse-b7-v1.md` devrait citer l'empreinte du plan scellé (et celle de sa contre-lecture) ; absent.

## Vérifié sans réserve (v2)

- Seuils, bandes, définitions et priorités (chaîne en défaut a à e, B-2, B-3, B-4, B-7, reproduction, couche lisible, « trop beau », « tout négatif ») : recopiés sans écart du texte gelé v6 et de l'addendum v3 ; la
  nouvelle phrase ligne 91 (par le haut et par le bas dits tous deux) est compatible avec le code (`par_le_haut` et `par_le_bas` indépendants).
- Critère (1)-(3), réserves 1, 2, 3, 4 de la v8 : portés ; « (3) même si chaîne en défaut » conforme.
- Lecture des deux séries, divergence A100 / RTX 4090 portée à la mère, R-2915 reste le verdict de B-α : conformes à l'addendum § 3.
- Le lecteur ne lit le code des verdicts de la course qu'après son propre calcul (étapes 4-5) ; R-2915 et `diag/20261115-…` seulement à l'étape 6 : (d) garanti, sous réserve du point 4.
