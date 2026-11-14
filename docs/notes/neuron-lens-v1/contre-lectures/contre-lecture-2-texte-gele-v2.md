# Contre-lecture 2 du texte gelé v2 (volet A et tranche B-α) — rapport recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 vers 10:07 UTC ; il n'a pas écrit le texte. Brouillon relu :
`docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v2.md`, `239e359eafec6780d3f353ef8dc0f65cad7c5fb2d0832f49849022b251c10629`
(commit `b319e96d`). Rapport rendu vers 10:14 UTC. Recopié sans modification de fond, à une exception signalée : dans la remarque 13,
l'identifiant de modèle que le contre-lecteur donne pour lui-même est remplacé par « [identifiant de modèle retiré] », les consignes
interdisant d'écrire un identifiant de modèle de la famille Claude dans le dépôt.

---

## 1) Empreintes vérifiées

| pièce | résultat |
|---|---|
| texte contre-lu `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v2.md` | conforme, `239e359e…0629` |
| v1 du texte, rapport de la contre-lecture 1 | `4ac7b556…0267`, `3d839dfc…d868` : celles que cite le texte |
| `plan-et-devis-v1.md`, `plan-et-devis-v2.md` | `bc20a12a…`, `4f653490…` : conformes |
| `reference-publiee/` (`sha256sum -c`) | quatre « OK » ; `causal_lens` `8904c4d3…`, `reads_at_firings` `ac0bf101…` |
| `neuron-lens-v2-contrastes-20261114/` (`sha256sum -c`) | sept « OK » ; les empreintes de `manifeste-v1.tsv` et du texte (A.2) concordent avec les fichiers |
| tokeniseur du brouillon (`qwen3-8b-tokenizer.json`) | `aeb13307…` : conforme |
| outil de comptes et sa sortie | `64c538d3…`, `e0aa5a1c…` : conformes aux abrégés du texte |
| relance de l'outil de comptes | sortie identique octet pour octet à `comptes-avant-scellement-v1.json` |

- **Non vérifié, hors de ma liste** : consigne de la mère, interdits communs, passation, `docs-findings.md`, arbres des lentilles, dossier `correctifs/`, note du lecteur.
- **Conduite** : aucun fichier du dépôt modifié, aucun appel réseau ni de modèle, code voisin non exécuté, aucun chemin interdit ouvert, aucun refus de permission.
- **Scripts de calcul** : deux scripts à moi, en lecture seule, dans le brouillon (`cl2_tok.py`, `cl2_ref.py`), plus `comptes-relance.json`.

## 2) Verdict

**Scellable après corrections mineures, pas en l'état** : une contradiction interne à lever (remarque 1) et une dizaine de règles à préciser. Aucune ne demande de reconception, mais plusieurs touchent des règles de décision, donc une v3 (R12) relue sur les seuls points modifiés.

- **(a)** 15 remarques sur 24 traitées, 8 partiellement, 1 refusée (tableau au § 4).
- **(b)** Les comptes du texte sont tous exacts. Les ambiguïtés et contradictions restantes sont les remarques 1 à 21.
- **(c)** Oui : la référence convertie passe « reproduit » pour B-2, B-3 et B-7, sans aucun « non reproduit » ni « chaîne en défaut », cas sain `npR` compris.
- **(d)** Le validateur rend `['contre-lecture 2 sans ses deux empreintes (brouillon relu et rapport)']`, rien d'autre. Les huit sections de R1 sont présentes et remplies. Le « commit du code d'analyse » manque parce que le code n'existe pas encore : le texte le dit.
- **(e)** Oui aux deux. La phrase sur P3b est aux lignes 42-43. La seule mention est « un modèle de la famille Claude (« modèle C ») », ligne 46, sans identifiant.

## 3) Remarques

### Bloquante (légère)
**1. Plan d'analyse B.3 (ii) et Seuil B — l'attendu de l'artefact contredit les seuils.** L'artefact met `r_med` à 0 aux couches 8 à 15 et attend « non reproduit » pour B-2 ; or la colonne « non reproduit » de B-2 ne porte que sur les couches 16–27 (`pass` < 0,50) et 16–23 (`r_med` < 0,30) : selon le tableau, cet artefact donne « partiel ». Il ne donne « non reproduit » que si l'on suit la phrase générale (« condition contraire à plus de la moitié des couches lisibles de la bande »), qui contredit le tableau. Le même artefact rend B-3 « non reproduit », ce que l'attendu ne dit pas. L'attendu demande à la fois un verdict de mesure et « chaîne en défaut », alors que celle-ci est définie comme « aucun verdict de mesure ». Correction : dire lequel prime (je propose le tableau) ; séparer en deux artefacts : (ii-a) `pass` de `npR` mis à 0,4 aux couches 16 à 27, attendu B-2 « non reproduit » ; (ii-b) témoin à 0,2 à une couche, attendu « chaîne en défaut », aucun verdict ; écrire l'attendu de B-3 et de B-7 pour chacun.

### À corriger
**2. Seuil B — comptes fixes contre « moitié des couches lisibles ».** Le tableau écrit « plus de 6 », « plus de 4 », « plus de 2 » ; la phrase d'en-tête dit « plus de la moitié des couches lisibles ». Les deux divergent dès qu'une couche est non lisible. Correction : choisir (je propose « plus de la moitié des couches lisibles de la bande nommée », les nombres valant pour une bande entièrement lisible).

**3. B.1 Métrique, Seuil (b) — `n` n'est pas une sortie de `score`.** Le fichier publié ne contient que `r_q25`, `r_med`, `r_q75`, `control_med`, `overlap`, `pass`, `pass_control`. Le « 57 à 64 » de la référence est reconstruit à partir des dénominateurs de `pass` (64, 59, 57, 62, 61 aux couches 0 à 4) ; cette reconstruction ne marche pas quand `pass` vaut 0 ou 1. Correction : déclarer un correctif qui écrit `n`, ou dire que notre code recalcule `keep` depuis le fichier `-causal.pt`, avec la formule (`y.abs().sum(1) > 0` sur les lignes du tokeniseur, avant le filtre de vocabulaire). L'essayer au titre de R5.

**4. Seuil B (c) — le cas sain `npR` ne détecte ni un repli sur l'identité ni un décalage de couche.** Aux couches 28–30, la lentille des logits fait déjà 0,94 à 0,97. Dans `score`, `lenses[s].get(layer)` rend `None` pour une clé absente, donc la lentille des logits, sans erreur ; des clés en chaînes ou décalées donneraient `r_med(npR) = r_med(logits)`, ce qui passerait le cas sain et sortirait B-3 « non reproduit » au lieu de « chaîne en défaut ». Correction : clés exactement égales aux couches attendues, formes 4096 × 4096, erreur sur clé absente (correctif 2) ; aucune matrice égale à l'identité avant la couche 28 ; `|r_med(npR) − r_med(logits)| < 10⁻³` à une couche de 0 à 23 = défaut. Artefact de R5 : lentille remplacée par l'identité.

**5. Seuil A, « S fait mieux que sans lentille » — sans marge, penche vers « apporte ».** Médianes comparées « strictement », à 2 couches sur 4, sur A1 **ou** A2 ; « n'apporte rien » exige au contraire « sans lentille ≥ S » aux 4 couches, sur A1 et sur A2 : asymétrie. Correction : appliquer la règle de couche (condition par découpe, couche positive à 3 sur 5) ; exiger que les 2 couches soient parmi les couches positives de A1 (ou de A2).

**6. Critères A-i, ligne « n'apporte rien » — trois trous.** (a) si A2 est sans objet, la clause est-elle éteinte ou réduite à A1 ? (b) « A3 dépendance non lue » n'est pas définie ; pas d'agrégat sur les découpes ; cas « sans objet dans un seul des deux contrastes » non couvert. (c) le plancher de A3 ne dit pas s'il vaut par couche ou par contraste, ni comment compter les couches positives quand des couches sont sans objet. Correction : une phrase par point.

**7. Seuil A-ii — plafond et paire « apporte » / « n'apporte rien ».** (a) plafond par couche ou par contraste, moyenne des découpes ? (b) sous plafond, les deux verdicts peuvent être vrais ensemble ; aucun ordre de priorité. (c) « intervalle contenant 0 » est une non-infériorité sans marge ; avec 30 bénins de test, « apporte » peut venir d'un manque de puissance. Correction : ordre de priorité (« n'apporte rien » d'abord) ; borne basse de l'écart hors distribution ≥ −0,05 ; maille du plafond.

**8. Seuil A-ii — le qualificatif « au-delà du texte » est vide sur C2.** Les paraphrases se tokenisent en `Ġtruthful` (89867) et `Ġdeceptive` (80274), absents de l'apprentissage du sac de jetons : il vaut 0,5 hors distribution par construction. Correction : qualificatif « sans objet » sur C2, ou jugé en distribution ; le garder sur C1.

**9. Métrique A.1 point 4 et Graines — tirage des covecteurs de référence.** « Tirés une fois par couche (graine dédiée) » contre des graines dérivées par contraste et par découpe sans enfant par couche ; même flou pour les 100 directions témoins. Avec des références gaussiennes isotropes, `μ_v ≈ 0` et `σ_v = ‖K_L(W_E[v] − m)‖/√d` : le `_z` vaut √d fois le cosinus entre `w` et l'empreinte du jeton ; il retire les pivots de grande norme, pas un mode commun aux directions réelles de la couche. Correction : fixer la dérivation ; écrire l'équivalence et la limite dans l'écart 6.

**10. Seuil A1 et A2 — détails laissés libres.** Témoins lus sur les deux signes ? Rapporter à part « S ne place pas P » et « un témoin le place aussi ». Méthode du 99ᵉ centile sur 100 valeurs non dite. Jetons du préambule dans l'ensemble de A2 ? écrire « dans le texte de l'exemple ». « Nomme » n'entre dans aucune ligne du tableau des verdicts : le dire.

**11. Plan A.1, cas sains — ils ne couvrent pas la chaîne des critères.** Le cas (ii) essaie `s-lens/mid.pt`, couche 1, covecteur de lecture d'un neurone, lecture brute ou `_z` non dite ; les critères reposent sur `s-lens/out.pt`, couches 8 à 26, `_z` par covecteurs de référence, non essayés. Le cas (ii) « tel que le définit `08_reads.py` » passe par `read_rows(a, b, lobe)`, qui lit `neg_lobe` dans la table `acts` de la couche 1 du catalogue, absente des téléchargements et de l'addendum ; le README donne une autre formule. Le cas (i) ne dit pas si les 10 premiers sont pris sur les jetons gardés ou sur tout le vocabulaire. Correction : cas sain synthétique (pour un jeton `v0` fixé, `w = K_L(W_E[v0] − m)` normé doit rendre `v0` au rang 1 en `_z` ; sans lentille de même) ; formule du cas (ii) et « brute » ; table à l'addendum.

### Mineures
**12. Deux conversions de profondeur** (plancher dans le cas sain, arrondi dans B.3 ; arrondi ambigu à l = 4 et 20). Fixer la règle.

**13. Contre-lecture, remarque 17 — refus non étayé par une pièce.** Le refus cite « l'outil de session, champ du modèle servi » sans chemin ni empreinte (R6). Mon identifiant de modèle, donné par mon environnement, est [identifiant de modèle retiré], le modèle que le contre-lecteur 1 disait être le sien. La ligne d'attribution que je vois nomme le même modèle avec l'adresse de la session autrice. Je ne peux pas établir le modèle de l'autrice : la clause « autre modèle que l'autrice » n'est donc pas certifiée par moi. Correction : archiver la sortie de l'outil de session et la citer.

**14. Métrique A.5 — liste de mots absente** ; à verser à l'addendum.

**15. A3 sur C1 — plancher presque structurel.** Les 20 premiers jetons d'une lecture seront pour la plupart absents des textes (C1 : 947 jetons distincts, 448 présents dans au moins 2 exemples) ; rapporter le nombre des 20 jetons présents dans les textes de test. Fixer le départage des égalités du sac de jetons (sur C2, 4 jetons seulement ont un poids non nul).

**16. Chaîne en défaut (a) — mode commun réel** possible ; libellé « chaîne en défaut ou mode commun, audit ».

**17. Audit R4 — déclencheurs mal posés** (« B-α, tout négatif » sans déclencheur ; « 10 exemples » ne mesure rien).

**18. Métrique A.1 — sonde et sac de jetons** : solveur, ordonnée à l'origine, départage des C, centrage-réduction des comptes non fixés.

**19. R6 — empreintes abrégées et compagnons** (`64c538d3…`, `e0aa5a1c…`, `d2a7a076…`, `12c8f673…` ; outil et sortie sans `.sha256`).

**20. Contrastes — longueur** : AUROC de la longueur en jetons 0,61 sur C1, 0,57 sur C3 ; une base « longueur seule » rapportée suffirait.

**21. Préambule du texte — correctif (3)** « à écrire » alors que l'audit « trop beau » de B-α en dépend ; le rappeler dans l'audit.

### (c) Critères de B sur la référence convertie
Mêmes verdicts pour les quatre conversions (arrondi de Python, demi supérieur, plancher, plafond) : B-2 `r_med` 8–15 minimum 0,567 ; 16–23 minimum 0,786 ; 24–27 minimum 0,969 ; `pass` 8–27 minimum 0,9375 ; témoin −0,038 à +0,031, aucune couche hors de ±0,05 ; B-3 minimum +0,352 ; B-7 0–15 maximum 0,134 à 0,158 ; 26–29 minimum 0,673 ; aucune clause « non reproduit » ; défaut (a) maximum absolu 0,039 ; cas sain logits 0,935 à 0,974 ; cas sain R 0,985 à 0,996. Rapports seuil / publié : 0,53–0,70 ; 0,62–0,76 ; 0,86–0,88, conformes. Chiffres de provenance recalculés, tous en accord. Aucun déclencheur « trop beau » sur la référence.

## 4) Les 24 remarques de la contre-lecture 1
Traitées : 1, 2, 4, 7, 8, 9, 10, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24 (avec réserves mineures sur 2, 4, 10, 13, 15, 16) ; partiellement : 3, 5, 6, 11, 12, 14 ; refusée, motivée : 17 (motif non étayé par une pièce). Écart entre le tableau final du texte et ce constat : il écrit « acceptée » pour 3, 5, 6, 11, 12 et 14, dont le traitement est réel mais incomplet.
