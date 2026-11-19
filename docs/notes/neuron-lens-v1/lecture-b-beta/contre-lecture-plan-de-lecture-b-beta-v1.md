# Contre-lecture du plan de lecture de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens », Llama 3.1 8B Instruct) — v1

- Heure (UTC, `date -u`) : ouverture du travail **2026-11-19 07:24:55 UTC** ; écriture de ce rapport **2026-11-19 07:28:46 UTC**.
- Contre-lecteur : sous-agent neuf (règle R2), modèle servi **Fable 5.2** (`claude-fable-5-2`), autre modèle que celui du lecteur (Opus 5.5).
  Il n'a écrit ni le plan, ni le texte gelé, ni son addendum, ni le code, ni la course.
- Empreintes SHA-256 recalculées (`sha256sum`) :

| pièce | lue | empreinte recalculée | attendue et compagnon |
|---|---|---|---|
| plan `docs/notes/neuron-lens-v1/lecture-b-beta/plan-de-lecture-b-beta-v1.md` | en entier (325 lignes) | `40128756b446301248827cc5a9facfd53baa5cf6b461a8b09731369b61208128` | égale aux deux |
| texte gelé `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | en entier (667 lignes) | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` | égale aux deux |
| addendum `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | en entier (144 lignes) | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` | égale au compagnon et au plan |
| modèle de forme `docs/notes/neuron-lens-v1/lecture-b-alpha/plan-de-lecture-v1.md` | non lu (empreinte seule) | `5a79991850459ca13469edbd51e91619b50c23fe80085cc1a9e17ff217d831da` | égale à celle du plan |
| code des verdicts `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` | non lu (empreinte seule) | `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` | égale à celle du plan |
| série repère de la lentille R publique, et les deux références publiées de Qwen3-8B | non lues (empreintes seules) | `bd57d519…df33073`, `8904c4d3…e03830d3`, `ac0bf101…ba182cd` | égales au plan et au texte gelé |

- Noms de fichiers de `diag/20261118-164930-neuron-lens-b-beta/` listés (aucun contenu, aucune empreinte) : 23 résultats d'étape
  `b-beta-*.json`, 9 autres pièces, 16 journaux, 2 artefacts, 50 compagnons — conforme au plan (l. 38-47). Les 16 journaux ne
  comptent aucun journal des étapes « verdicts », « déclencheurs » ou « grandeurs ».
- Horodatage du plan sur disque (`stat`) : 07:24:01 UTC, compagnon 07:24:03 UTC ; en-tête du plan : 07:19:19 puis 07:21:45. Cohérent
  (le relevé précède l'écriture du fichier) ; rien à redire.
- **Aucun fichier interdit ouvert** : ni contenu ni empreinte d'un fichier de `diag/20261118-164930-neuron-lens-b-beta/` ou de
  `runs/20261118-164930-neuron-lens-b-beta/`, ni `etat-final-course-b-beta-v1.txt`, ni `controles-b-beta-v1.log`, ni la branche
  `calcul/neuron-lens-b-beta-v1`, ni `verdict-b-alpha-v1.md`, ni les fichiers `calcul-*`. Aucun modèle, aucune machine, aucun commit,
  aucun push ; le plan n'est pas modifié.

## Verdict : « employable »

**0 bloquante, 2 majeures, 13 mineures.** Les règles du plan (seuils, lisibilité, bandes, chaînes en défaut (a) à (s), audits et
déclencheurs, verdict d'ensemble par rang, lecture de l'accord des deux codes, lecture de l'ablation pour un moniteur) sont recopiées
du texte gelé sans chiffre faux, sans règle ajoutée ni retirée qui changerait un verdict ; aucun résultat n'a fui dans le plan. Les deux
majeures ne touchent aucune règle : elles demandent de **fixer par écrit, avant toute ouverture** (au mandat de la phase de lecture, que
le plan attend déjà aux lignes 65-67, ou dans un plan v2), le statut des lectures déjà décidées par l'addendum et l'ordre de deux
lectures. Sans cette écriture, le plan reste appliquable, mais le lecteur rendrait plusieurs verdicts là où le texte en veut un.

Classes : *bloquante* = règle fausse, manquante ou fuite de résultat (plan non employable) ; *majeure* = aucune règle fausse, mais à
fermer par écrit avant l'ouverture des résultats ; *mineure* = précision ou omission sans effet sur un verdict.

## Contrôle de fidélité, règle par règle (résumé)

Comparés ligne à ligne, sans écart de chiffre ni de quantificateur :
- commun (plan l. 146-156 ; texte l. 118-128, 168-170, 182, 253) ;
- seuils des sept mesures (plan l. 159-181 ; texte l. 172-180, 135-143, 158-159) ;
- chaînes en défaut (a) à (s) (plan l. 184-218 ; texte l. 194-251) — condensées, tous les seuils justes (±0,10 ; 0,80 et 0,85 ;
  10⁻³ et 10⁻⁶ ; 466 et 466 ; 31 et 32 ; 0,05 à plus de 2 couches, 0,10 à une ; 16 contextes ; 4, 2 et 2 documents) ;
- verdict d'ensemble par rang (plan l. 221-229 ; texte l. 488-497) ;
- accord des deux codes et son audit (plan l. 232-234 ; texte l. 500-505) ; ablation pour un moniteur (plan l. 238-241 ; texte l. 508-513) ;
- audits et déclencheurs (plan l. 244-262 ; texte l. 516-529) ;
- empreintes, versions et graines des étapes 1 et 2 (plan l. 77-104 ; texte l. 51, 56, 463 ; addendum l. 72-73, 87-89, 109-111).

## Remarques majeures

**M-1. Cinq « ambiguïtés » sont déjà tranchées par l'addendum ; le plan ne dit pas quelle lecture porte le verdict comparé.**
- Plan : l. 12-13 (« n'arbitre aucune ambiguïté »), l. 270-272 (n° 1), 277-278 (n° 4), 279-280 (n° 5), 281-282 (n° 6), 283-284 (n° 7,
  seconde moitié).
- Texte : l'addendum, « pièce du texte gelé scellé » (addendum l. 3-4), scellé avant toute donnée, décision de la mère (R-3190), tranche :
  n° 1 — une clause « non reproduit » n'est pas jugée sur une bande partielle, la mesure est « autre » (addendum l. 24-25) ;
  n° 4 — le témoin de la lecture contre pilotage est compté sur les seules couches lisibles (addendum l. 41-42) ;
  n° 5 — la garde du témoin hors de ±0,10 porte aussi sur les lentilles des moitiés (addendum l. 45-46 ; le texte lui-même range les
  moitiés parmi les « lentilles notées », l. 115-117, et dit « l'une des lentilles notées », l. 194) ;
  n° 6 — différences de deux valeurs à 4 décimales arrondies à 4 décimales avant comparaison (addendum l. 47-48) ;
  n° 7, seconde moitié — valeurs de la lecture côté entrée prises telles qu'écrites, moyennes en fractions exactes (addendum l. 48-49).
- Le texte veut que le lecteur « compare son verdict à celui du fichier des verdicts » (l. 480-481) : il faut **un** verdict du lecteur.
- Correction proposée : écrire que, pour ces cinq points, la lecture de l'addendum est la règle en vigueur et porte le verdict comparé ;
  la lecture littérale reste donnée à côté, comme information (l'addendum déclare lui-même que la lecture 2 joue dans le sens favorable,
  l. 42-44, et que la lecture 1 peut retirer le déclencheur de l'audit de l'ablation par le haut, l. 33-37 : le lecteur le rapporte si
  le cas se présente). Aucune règle n'est changée.

**M-2. L'ordre ne garantit pas que le lecteur calcule ses gardes recalculables avant de lire celles que la course a écrites.**
- Plan : l. 108-111 (étape 2, point 8 : « j'évalue moi-même » les gardes (a), (b), (c), la part « score » de (e) et (j), mais dans la même
  étape que la lecture de `b-beta-score.json`, `b-beta-grandeurs.json` et des journaux de `measure` et de `score`), l. 113-114
  (« je relève la valeur écrite » de chaque garde), l. 116-120 (recherche d'une sortie d'audit dans ces mêmes fichiers avant le calcul
  de l'étape 5), l. 69-70 (l'exposition est seulement déclarée après coup).
- Texte : l. 479-481 (plan scellé avant ouverture, verdict du lecteur comparé à celui de la course) ; l. 389-394 (le code de course
  évalue chaînes en défaut, déclencheurs et seuils : ses résultats d'étape peuvent donc porter ces valeurs).
- Pour les fichiers de verdicts eux-mêmes, l'ordre est bon : `verdicts-b-beta-v1.json`, `b-beta-verdicts.json` et
  `b-beta-declencheurs.json` ne s'ouvrent qu'à l'étape 6 (plan l. 119-120, 135-137), après le calcul scellé de l'étape 5, sans import
  ni relecture du code des verdicts (plan l. 28, 129-130, 323). La remarque porte sur les seuls résultats d'étape et journaux.
- Correction proposée : à l'étape 2, point 8, et à l'étape 3, lire d'abord les sorties brutes (`causal_lens_b-beta_…json`,
  `grandeurs-par-pole-b-beta-v1.json`, `lens_compare-b-beta-v1.json`, `reads_at_firings_…json`, différences entre moitiés), calculer et
  consigner les gardes (a), (b), (c), (e) part « score », (j) et les déclencheurs ; n'ouvrir qu'ensuite `b-beta-score.json`,
  `b-beta-measure.json`, `b-beta-grandeurs.json` et les journaux de `measure` et de `score` pour les gardes constatées sur la machine
  et la recherche de sorties d'audit ; tout champ d'un résultat d'étape qui porte un verdict, un déclencheur ou une issue d'audit se
  traite comme une pièce de l'étape 6. Les gardes non recalculables (constatées sur la machine) restent lues telles qu'écrites.

## Remarques mineures

1. **Ambiguïté 7, première moitié, tranchée par le texte** (plan l. 283) : « au moins 0,10 au-dessus » (texte l. 178) veut ≥ 0,10 ; la
   prédiction le confirme (« réfutée si … écart des moyennes < 0,10 », l. 102) ; « au-dessus = strictement » (l. 170) règle les
   tournures « dépasse », « plus de », « sous ». Correction : ≥ 0,10 porte le verdict ; > 0,10 n'est pas une lecture du texte.
2. **Ambiguïté 2, vraie mais orientée par le texte** (plan l. 273-274) : pour la lecture côté entrée, le texte écrit « partiel », jamais
   « reproduit » ni « non reproduit » (l. 158-159) ; le même mot « partielle » à la ligne 125-126 appuie la lecture (i). Non tranché mot
   pour mot : garder les deux, dire que (i) est la plus proche du texte.
3. **Ambiguïté 3** (plan l. 275-276) : une bande sans couche lisible est une bande partielle (texte l. 125-126) ; elle relève donc des
   ambiguïtés 1 (tranchée, M-1) et 2. Sans effet.
4. **Ambiguïté 8, vraie** (plan l. 285-286) : la lettre du texte est la lecture (i) (« écartés par score pour effet nul », l. 195) ;
   l'addendum ne décrit la lecture (ii) qu'en passant (« sous 32 … prime », l. 38-39), sans la déclarer. Si les deux divergent sur les
   pièces, c'est un écart du code au texte (texte l. 547) à rapporter au second lecteur, comme pour « n indépendant de la lentille »
   (plan l. 26-27, ambiguïté 9), que l'addendum ne déclare pas non plus.
5. **Ambiguïtés 16 et 17, tranchées en partie** : un écart de la partie 2 à la partie 1 n'est pas une chaîne en défaut mais un arrêt et
   un nœud (addendum l. 89-91 ; texte l. 546) — le plan le dit (l. 307) ; seul le cas « la course a continué » reste ouvert. Le fichier
   des verdicts au sens du texte est le « fichier de verdicts unique » (l. 392, 474-475, 480-481), soit `verdicts-b-beta-v1.json` — le
   plan le dit (l. 311-312) ; la comparaison principale se fait à lui.
6. **Ambiguïtés 9 à 15 et 18** : vraies, non arbitrées par le texte ni par l'addendum ; le plan s'engage au verdict sous chaque lecture
   (l. 12-13, 130-131, titre de la section 4). Pour la n° 15, la lecture (i) repose sur un renseignement de seconde main tiré d'une pièce
   interdite au lecteur (plan l. 50-56), non sur une sortie versée ; le texte fait lire « les sorties versées » (l. 480) : la lecture
   (ii), « non constatable », est la plus proche du texte. La n° 18 est une réserve plutôt qu'une ambiguïté.
7. **Ambiguïté absente : garde (j) et la règle « plus de N des couches »** (plan l. 203-204, 290-292 ; texte l. 168-169, 222-223). Le
   plan lit « plus de 2 des 28 couches » à la lettre, ce qui est juste (la règle de la ligne 169 vaut pour les clauses de la table des
   seuils, non pour les gardes) ; l'écrire, pour qu'on ne lise pas « plus de la moitié des couches lisibles ».
8. **Ambiguïté absente : « notre R » dans les gardes (c) et (e)** (plan l. 186-187, 191-193 ; texte l. 196-197, 203) : moitiés comprises
   ou non (l'addendum ne les étend que pour la garde (a), l. 45-46). Lecture à la lettre : lentille entière seule ; donner les deux si
   elles divergent.
9. **Omissions de copie sans effet sur un verdict** : rang 2, « verdict final de la tranche ; aucune reprise sans devis neuf et mot de
   Lazar » (texte l. 491 ; plan l. 224) ; moments des gardes (n) et (o), « après l'export, avant score » (texte l. 236, 240-241 ; plan
   l. 209-212) ; contenu des contrôles (1) et (2) de l'audit « trop beau, lecture contre pilotage » (texte l. 518 ; plan l. 246) ;
   « règle de lisibilité comprise » à l'issue de l'audit de la lecture côté entrée (texte l. 521 ; plan l. 255).
10. **Grandeurs à rapporter sans critère, absentes du plan** (plan l. 122-126, 139-141) : recouvrement des dix premiers jetons et accord
    de chaque moitié avec la lentille R publique (texte l. 141-143) ; compte et rang du jeton de début dans les jetons gardés (texte
    l. 344-346, 474) ; mention « hors programme » et « aucune correction pour comparaisons multiples » au rendu (texte l. 62-63, 481-483).
11. **Étape 2 intitulée « ce qui décide d'une chaîne en défaut »** (plan l. 85-94) : elle y range des arrêts de montage qui ne sont pas des
    chaînes en défaut — banc à 23,6 s, version de Drowse, comptes de B0, comparaison des deux parties de l'addendum (texte l. 542-546).
    Le dire : un manquement y est un écart à la liste d'arrêt, non le rang 1.
12. **Essai du script du lecteur** (plan l. 131-133) : un cas sain et un artefact suffisent à la règle R5 ; le texte fournit des attendus
    gelés rejouables sur le processeur avec les deux références publiées empreintées (texte l. 404-449 : cas (i), (ii-a), (iii-a) à
    (iii-c), (vi-b), (vii), (x), « rangs 2 et 3 »). Les rejouer renforcerait un calcul que rien d'autre ne contrôle avant la comparaison.
13. **Forme** : l'étape 0 ne revérifie pas l'empreinte de l'addendum (plan l. 72 ; ajouter `bd8067dc…`). La lecture entière du code des
    verdicts en phase 1 (plan l. 22, 25-28) est permise par le mandat et déclarée honnêtement, lectures du code reportées en ambiguïtés
    et non en règles ; elle réduit l'indépendance du lecteur, que seuls ses engagements (ni relecture ni import, plan l. 28, 129-130)
    protègent.

## Ce que le lecteur déclare savoir ; règle choisie en vue d'un résultat ?

La déclaration (plan l. 17-60) est complète pour ce que j'ai pu contrôler : pièces lues et empreintes exactes, noms de fichiers exacts
(décompte vérifié), renseignement reçu de la session qui le lance recopié, avec la phrase « je ne connais aucune valeur de mesure ni
aucun verdict ». Ce renseignement (fin normale, aucune étape d'audit, aucun arrêt) est un résultat de second rang ; le plan en tire
lui-même la conséquence ouverte (l. 58-60) et donne les deux lectures aux ambiguïtés 11, 12 et 15 qui en dépendent. Je ne vois aucune
règle, aucun seuil ni aucun ordre choisi en vue d'un résultat. La section « Ce que je ne fais pas » (l. 317-325) est conforme au mandat
et au texte (l. 393-394, 475-476, 548).
