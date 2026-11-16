# Contre-lecture du préenregistrement du crible (iii), brouillon 5 — tour 2 de la lecture du brouillon 4 (cinquième lecture du crible) — v1

- Lecteur : sous-agent neuf du modèle C (R2), qui n'a écrit aucune des pièces ; l'auteur de la pièce est du modèle A ; les
  corrections seront écrites par le modèle A. Heure de rédaction : 2026-11-16, 14:34Z à 14:42Z (`date -u`).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon5.md`,
  `add61e9726e5ba64324135656bde0042aa87721eafdf12431af30be810b4b94f` (égale à son compagnon).
- Pièces comparées : brouillon 4 `crible-iii-brouillon4.md`, `f30bd0f1c46cbbd3597fdf005bb6a372d0e9f039e2eedd7c3c3e7bb74667e8dd` ;
  rapport du tour précédent `contre-lecture-crible-iii-b4-tour1-v1.md`,
  `4997f4a2baa6993186de7cba23fb54760fcfefaa94781e3bb88d43e71f8f0fe4` (vérifiée) ; programme
  `appliquer-corrections-crible-iii-brouillon5.py`, `c41551ed96000a918c30132e4ec9d135fd908d7eaa9b11f6f9be97dcd7c2f337` (égale à son compagnon).
- Non lu, par consigne : sortie du pilote MR-2 v14, `diag/`, `runs/`, `donnees/`, 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque,
  dossiers jetables du premier contre-lecteur.

## Verdict

**« corrections »** : 0 majeure, 3 mineures (G-01 à G-03), toutes de cohérence ou de fermeture de lecture. Les 18 couples du
tour précédent sont appliqués à la lettre et rien d'autre ne change. Aucun défaut n'appelle de refaire la conception. La pièce
reste **non scellable** tant que la mère n'a pas inscrit la forme du crible (voir section 3) ; la recommandation est la variante.

## 1. Les corrections du tour précédent sont-elles appliquées fidèlement ?

Oui. Vérifié par programme : les 18 couples « ancien → nouveau » du rapport sont extraits du rapport lui-même ; chaque « ancien »
figure une fois dans le brouillon 4 et plus dans le brouillon 5, sauf deux dont le « nouveau » contient l'ancien en tête (F-04,
F-08 : ajout par préfixe ou suffixe, normal) ; chaque « nouveau » figure une fois dans le brouillon 5. `diff` brouillon 4 → 5 :
titre ; en-tête (puce du brouillon 5 : empreintes et dates justes, tête `e231c01e` = tête de `main`) ; statut ; ligne du
validateur ; les 18 couples (F-01 : étage 2 ; F-02 : sept lieux ; F-03 : trois ; F-04 ; F-05 ; F-06 : trois ; F-07 ; F-08) ;
section « Contre-lecture 4 » et « Tour suivant ». **Rien d'autre.** Les empreintes citées dans « Contre-lecture 4 »
(brouillon 4, rapport) sont entières et exactes. La section ne contredit pas le rapport (verdict, 2 majeures, 6 mineures,
recommandation de la variante à 0,6). Les cinq remarques facultatives sont déclarées non appliquées : exact.

## 2. Réponses aux neuf points

**(1) R1.** Complet. Un seul trou de fermeture, G-01 (rapport de P2 « réintégré » lu « avec le principal » sans règle de
désaccord).

**(2) R3.** Rien de nouveau : statistique principale (différence, définie même si le bras standard ne couvre rien), marge de
0,5 composante (10 à 17 % de 3 à 5), égalités par l'ordre des noms, bras B qui réemploie la passe 1 (texte servi égal à
l'octet, dollars de la passe 1 comptés dans chaque bras, rééchantillonnage apparié). Les corrections F-03 (« ρ_DS ≤ 1 »
équivaut à Δ_R ≤ 0 quand R_S > 0 ; colonne de réfutation en deux parties) et F-04 durcissent la lecture sans ouvrir de voie vers
un signe positif. Remarque : les bornes « sous − 0,05 à 20 mondes, sous 0 à 24 » sont des valeurs médianes de la fourchette
d'écart-type 1,0 à 1,2 (recompte à 97,5 % bilatéral, z = 2,24 : 20 mondes, entre − 0,00 et − 0,10 ; 24 mondes, entre + 0,04 et
− 0,05) ; l'ordre de grandeur est juste (remarque facultative R-6).

**(3) Forme et crédits.** Voir section 3.

**(4) Devis.** Recompté, inchangé : appels 100 (60 et 40) ; forme fidèle 48 + 10 + 0,30 = 58,30 attendus, 120 + 93,60 + 3 = 216,60
au pire ; variante 96 + 32 + 0,30 = 128,30, 180 + 80 + 3 = 263,00 (dont 3 hors crédits) ; sonde 2,00 + 2 × 2,34 = 6,68 ; cumul
des cinq : 123 + 483 + 243 + 196,60 + 263 = 1 308,60 (1 262,20 avec la forme fidèle), au-dessus de 1 275. La pièce le dit
(point pour la mère). Plafonds du bloc gelé (2,00, 2,34, 3,00) comme au tour précédent. La règle de mise à jour d'après le
pilote est une table close ; N = 24 si taux < 0,95 (section « Seuil »), minimum 16 pour tout N.

**(5) Durée.** Cinq files de quatre mondes (six pour 24), borne par appel 3 000 s, par monde 7 200 s, pire cas d'une file 8 h,
garde de départ 10 h ; F-08 ajoute l'attendu (2 à 2 h 40 par file, plus mesure et barrières) : arithmétique juste (4 × 30 à
40 min). **Code neuf nettement dit** : lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles, mesure ; le pilote
joue quatre mondes en série et son lanceur ne sert pas tel quel ; environ deux jours d'agents ; concurrence jamais éprouvée,
essai à blanc à cinq files obligatoire, nœud si les relais refusent.

**(6) Liste d'arrêt.** Chaque ligne a cas sain et artefact ; graines `SeedSequence` (clés sans collision, relues au tour
précédent, intactes) ; minimum 16 mondes complets et sa règle (13 accords sur 16). F-05 définit « fournisseur perdu en entier »
(aucun appel répondu sur tous les mondes commencés, dix appels faits au moins) : défini, cohérent avec la ligne 1 de l'étage 1
et avec la ligne d'arrêt « complets + non commencés < 16 ».

**(7) Ablation de la frontière aux critères gelés.** Mieux définie qu'au tour précédent : les lieux de verdict disent « le
proposeur cher », la phrase de contexte dit « deux espèces de frontière au sens de N-045 ; l'instrument local n'est pas joué ».
Sans contradiction avec N-045 point 3 (il vise les courses ; la pièce le dit). **Restes non corrigés** (G-02) : trois lieux disent
encore « (QO1) » sans réserve, dont celui des dix lignes (point 1) et celui des « Écarts » qui appelle B « la question même du
crible (QO1) ».

**(8) R7 et R8.** Inchangé : aucun chiffre d'état de l'art non vérifié ; antériorités listées « à chercher ».

**(9) Validateur, identifiants, empreintes.** `controle_ia.prereg.problemes(brouillon 5)` rend `[]`. Aucun identifiant de modèle
(recherche de motifs de noms de modèles : aucune occurrence). Empreintes de la section « Contre-lecture 4 » et du programme
vérifiées par `sha256sum`. Décisions de R-2977 relues : toutes présentes dans la pièce (mondes séparés, dollars au prix public
et prix de la configuration en sensibilité, ablation aux critères gelés, GO pour l'essai et non l'adoption, forme à trancher,
N = 24 si taux sous 0,95) ; les deux décisions propres à (v) sont déclarées sans objet ici.

## 3. Forme du crible : recommandation nette pour la mère

**La variante** (Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4), **confiance 0,6** (même avis qu'au tour précédent, établi ici
de façon indépendante). Raisons : (a) la consigne permanente de Lazar (« crédits de Claude au maximum ») est mieux servie : environ
98 % de l'attendu sur crédits, 3 USD hors crédits au pire, contre 82 % et 96,60 USD pour la forme fidèle ; (b) le contraste de prix
est le même aux deux barèmes (rapport 2), alors que la forme fidèle n'a de contraste qu'au prix promotionnel de Pr-1, qui finit le
30 novembre, et que son étage 4 (« dépend du barème ») peut annuler le verdict de P1 quelle que soit la donnée ; (c) le bras
standard est « un appel cher seul » au sens de la note ; (d) la variante respecte le classement du programme (Pr-1, Pr-2 bon
marché ; Pr-3, Pr-4 cher).
**La variante change la question, un peu** : elle compare deux paliers de prix d'une même maison, non un proposeur externe bon marché
contre un proposeur de frontière ; elle perd la diversité d'espèces de frontière que la forme fidèle garde, et la question de
l'instrument local n'est de toute façon posée dans aucune des deux. **Coûts à lire par la mère** : un seul fournisseur pour les 100
appels (toute limite de débit touche tout le crible ; 15 sessions de Pr-4 et 5 de Pr-2 à cinq files) ; solde de crédits de Claude à
couvrir (263 au pire, 315,60 à 24 mondes) ; réécriture du texte (tableaux « Proposeurs », devis, lignes de GO, étage 2 avec la
borne de 89 000 jetons de Pr-2 qui rend « B tronqué » rare) et un tour de contre-lecture de plus ; calendrier : autonomie jusqu'au
17 novembre à 11:48Z. La forme fidèle reste défendable si la consigne de Lazar vise à limiter les dollars hors crédits sans gonfler le
total : dans ce cas, appliquer G-01 à G-03 et sceller après un dernier tour sur le diff seul.

## 4. Corrections exigées : ancien → nouveau

Chaque « ancien » figure **une seule fois** dans le brouillon 5 (vérifié par programme, espaces compris).

### G-01 (mineure) — rapport de P2 « réintégré » : aucune règle de désaccord, direction du biais non dite

Le rapport réintégré donne C_B = 0 pour tout monde où B est tronqué : c'est le pire cas pour B (il penche vers « perte établie »).
Il est « lu avec le principal » sans dire quoi faire s'ils divergent : porte de sortie après lecture (R1).

Ancien :

````
et ce rapport est lu avec le principal même quand moins de trois appels de B sont tronqués (le principal exclut ces mondes par définition du monde complet), et la phrase
````

Nouveau :

````
et ce rapport est lu avec le principal même quand moins de trois appels de B sont tronqués (le principal exclut ces mondes par définition du monde complet) ; C_B = 0 est le pire cas pour B (il penche vers « perte établie ») ; si l'issue de P2 du rapport réintégré (mêmes seuils, 97,5 %) diffère de celle du principal, l'issue de P2 est qualifiée « sensible à la troncature de B » et rien de plus n'en est conclu ; et la phrase
````

### G-02 (mineure) — « QO1 » sans réserve en trois lieux, contre F-02

Ancien :

````
La passe chère est-elle nécessaire (QO1) ?
````

Nouveau :

````
La passe chère est-elle nécessaire (QO1 au sens dit en « Hypothèse » : Pr-2 contre Pr-1, deux espèces de frontière, non l'instrument local) ?
````

Ancien :

````
(mesure, sans sens attendu par le programme ; QO1, N-045 point 3)
````

Nouveau :

````
(mesure, sans sens attendu par le programme ; QO1 au sens dit plus haut, N-045 point 3)
````

Ancien :

````
du crible (QO1) ; N-045 point 3 vise
````

Nouveau :

````
du crible (QO1 au sens dit en « Hypothèse » : deux espèces de frontière, non l'instrument local) ; N-045 point 3 vise
````

### G-03 (mineure) — section « Contre-lecture 4 » : dire les trois restes nouveaux

Après application de G-01 et G-02, ajouter à la section « Contre-lecture 4 » (du brouillon 6) la lecture de ce rapport. Pas de couple
exact : c'est la section « Contre-lecture 5 » que le rédacteur écrit, avec les deux empreintes entières (brouillon 5 et ce rapport,
empreinte lue sur le compagnon `.sha256`), comme au tour précédent.

## 5. Remarques facultatives (aucune correction exigée)

- Les cinq remarques du tour précédent (R-1 à R-5) restent valables pour la version qui fera foi.
- R-6 : « sous − 0,05 à 20 mondes, sous 0 à 24 » : dire « environ » (la fourchette d'écart-type donne − 0,10 à 0 à 20 mondes et − 0,05
  à + 0,04 à 24) ; ne change aucun seuil.
- R-7 : la phrase de l'en-tête de « Contre-lecture 4 » dit « sept couples » pour F-02 : exact ; rien à reprendre.

## 6. Points pour la mère (à trancher ou à savoir)

1. **Forme du crible** : inscrire une ligne datée à l'heure dans `registres/decisions.md` (variante recommandée, 0,6) ; le gel de III-6 de
   la même façon, avant la lecture du lecteur neuf du pilote ; la variante impose une réécriture et un tour de plus.
2. **Mot de Lazar** pour le lancement ; autonomie jusqu'au 17 novembre à 11:48Z (prolongeable au 18) ; calendrier sans marge si réécriture.
3. **Enveloppe de GO-2026-11-15-06** : la somme des pires cas des cinq cribles (1 308,60 avec la variante, 1 262,20 avec la forme fidèle)
   dépasse ou frôle 1 275 ; décider le plafond cumulé ou réduire (ii).
4. **Solde de crédits de Claude** : 263 USD (variante, 315,60 à 24 mondes) à vérifier.
5. **N-045 point 3** à dire à Lazar avec le nœud d'adoption ; le crible compare deux espèces de frontière, il ne retire pas la frontière.
6. **Risques** : « non tranché » probable pour P2 même si III-2 est vraie (puissance 0,35 à 0,50 à 20 mondes) ; code neuf et
   concurrence à cinq files jamais éprouvés.

## Incidents (de ma main)

- Aucun appel de modèle, aucune dépense, aucune machine, aucun fichier existant modifié, aucun commit, aucun `pytest`.
- Lecture de `registres/decisions.md` par `grep` : deux commandes ont affiché des débuts de lignes R-2977 et R-2981 à R-2990 (coupés à
  200 caractères) ; la ligne R-2981 contient « codes 0 à chaque étape » du pilote ; **je ne l'ai pas utilisée** et n'ai ouvert ni la sortie
  du pilote ni sa branche. Aucun `git fetch` fait (la procédure v14 n'a pas été rouverte : le bloc gelé a été relu par le rapport du tour
  précédent et n'est pas touché par les corrections).
- Un script de comparaison en bibliothèque standard, lecture seule.
