# Vérification du fabricant v7 épinglé — v1

**Verdict : Conforme avec réserves.** L'épinglage est rouge sur tous les artefacts joués, vert sur le cas sain (données identiques au v6 octet pour octet), sans fichier partiel après refus, et je n'ai trouvé aucun chemin pour obtenir un texte réduit autre que `061f7993…` en passant par le script, le réducteur ou les variables de banc. Réserves : l'amorce n'est pas épinglée ; relectures non atomiques (analyse, non jouées) ; une de mes mutations (R1) a été refusée par `bash -n` et non par l'épinglage, remplacée par R1b et par la paire de témoins.

Fabricant lu : `…/auteur-fabricant-v7-epingle/fabriquer-donnees-demarrage-v7.sh`, `68c7e0507c8748a12dfbd642f777c159efb7b89dbf94a6f269a574d4c9b4a43a` (sha256sum rejoué : identique). Script complet `f61aea46…eeb2` (rejoué), banc dans mon dossier : copies, dépôt distant factice `git init --bare`, jeton factice, `FABRICANT_BANC=oui`.

## Table des cas

Outils : `outils/verif.sh`, `outils/verif2.sh`. Tables : `tables/table-cas.txt`, `tables/table-cas2.txt`, `tables/sorties/`, `tables/empreintes-v7-jeton40.txt`, `tables/tailles-json-v7-jeton100.txt`.

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| Point 1 : `diff` v6 / v7 | seules l'en-tête (ligne 2), la ligne d'emploi (5) et 6 lignes d'épinglage (124-129) | exactement cela ; les deux empreintes en dur = `f61aea46…eeb2` et `061f7993…7ce5` | sortie du `diff` (appel direct) |
| S1 sain, jeton factice de 40 signes, même H0 (essai 1) | v6 = v7 | données, `.sans-jeton`, `.charge.b64`, `.script-reduit.sh` : IDENTIQUES ; codes 0 et 0 | `tables/table-cas.txt` |
| S1c texte dans la charge | haché = `E_SCRIPT` = `061f7993…` | charge extraite : `061f79930face6fc7945c30fb5dbb6275563495b0ea0fe132ba82f1457137ce5` ; ligne `E_SCRIPT=` identique | idem |
| S1d jeton factice | seulement dans la sortie | 1 occurrence dans la sortie, 0 dans les autres fichiers ni la sortie standard | idem |
| S2 jeton de 100 signes | 32 653 ; 32 708 ; `E_SCRIPT` `061f7993…` | 32 653 (marge 115) ; 32 708 (marge 60) ; `E_SCRIPT` juste ; jeton hors sortie : 0 ; recalcul indépendant par `tailles-json.py` (copie de l'auteur) | `tables/tailles-json-v7-jeton100.txt` |
| R1 octet changé ligne 3 | 9 | 9, mais par `bash -n` (mutation cassant la syntaxe) : ne prouve pas l'épinglage | `sortie-R1-…` |
| R1b commentaire ajouté en fin de script | 9 par épinglage | 9 : « épinglage : script complet 903e6164… » | `sortie-R1b-…` |
| V2c octet changé dans un commentaire entier (ligne 2) | v6 accepte, v7 refuse 9 | v6 : code 0, `E_SCRIPT` inchangé ; v7 : 9 « épinglage : script complet b0a5b5a5… » ; 0 fichier laissé | `table-cas2.txt` |
| R2 réducteur d'essai qui garde une ligne de commentaire (`garde-ligne-2`) | 9 | 9 : « épinglage : texte réduit 21db6cf1…, attendu 061f7993… » (script complet juste, épreuve muette) | `sortie-R2-…` |
| R3 / R3b A2 (`queue-a2-chaine.txt`), réducteur naïf puis réel | 9 | 9 dans les deux cas par « script complet 767c4621… » | `sortie-R3-…`, `sortie-R3b-…` |
| Témoin A2 sous le v6, réducteur naïf | v6 accepte (objet vrai du défaut) | v6 : code 0, `E_SCRIPT=7ce496d4…` ≠ `061f7993…` ; v7 : 9 | `table-cas.txt` (T2), `table-cas2.txt` |
| R4 réducteur retirant la ligne 1 ; R5 réducteur modifiant une ligne | 9 par l'épreuve (déjà là au v6) | 9 « la ligne 1… » ; 9 « 4 ligne(s) de diff… » | `sortie-R4-…`, `sortie-R5-…` |
| R6 troisième argument faux | 5 | 5 | `sortie-R6-…` |
| R7 `FABRICANT_SCRIPT` sans `FABRICANT_BANC` | 2 | 2, aucun fichier | `sortie-sans-banc.txt` |
| Fichiers laissés après tous les refus 9 | 0 | 0 (comptage `ls` par nom de cas ; v7 : 0 en `table-cas2`) | tables |
| B1 amorce modifiée (ligne `E_SCRIPT=0000…` insérée) | refus si l'amorce était épinglée | code 0 : données produites avec deux lignes `E_SCRIPT=` (la seconde l'emporte) | `table-cas.txt` |
| Cas non joués | | course de fichiers entre lecture et usage (point 2) : analyse seulement ; dépôt réel et GitHub : hors mandat | |

## Réponses aux points

1. **Diff** : tenu (voir table). Les deux empreintes en dur égalent celles du texte du mandat.
2. **Portée de l'épinglage** : le test se place après le réducteur, quel qu'il soit, sur `$SCRIPT` (qu'il vienne de `FABRICANT_SCRIPT` ou du défaut) et sur `$REDUIT` ; `FABRICANT_REDUCTEUR` n'échappe pas au test (R2) ; sans `FABRICANT_BANC=oui` ces variables sont refusées (R7). Le troisième argument ne fait que durcir. Donc tout `E_SCRIPT` qui sort de la ligne 130 est celui du texte de `$REDUIT` qui a l'empreinte épinglée. Le texte haché (129-130) est celui qui est empaqueté par `tar` ligne 138 : même fichier, mais **relu**, non copié : l'identité n'est donc établie que par l'absence d'écrivain concurrent (voir réserve 2) ; jouée sur le cas sain, la charge extraite a bien `061f7993…` (S1c). **Cassé seulement hors de la portée revendiquée** : l'amorce (voir B1).
3. **Cas joués** : voir la table.
4. **Tailles** : tenues.

## Réserves
1. **Amorce non épinglée.** `amorce-demarrage-essai-3-v6.sh` (524cfc4a…) est copiée de la ligne 3 à la fin sans contrôle d'empreinte, `E_AMORCE` n'est qu'imprimée. Mon cas B1 (copie modifiée) produit des données avec code 0 et une seconde ligne `E_SCRIPT=` qui écrase la première : en l'état la machine échouerait (code 18, fail-closed), mais une amorce qui retirerait son contrôle passerait. Hors de la revendication (qui vise le script et son texte réduit) ; proposition : épingler `E_AMORCE` de même.
2. **Relectures non atomiques** : `$SCRIPT` hachée ligne 68 puis relue par le réducteur, `diff` et `bash -n` ; `$REDUIT` hachée lignes 129-130 puis relue par `tar` ; pièces hachées ligne 84 puis relues par `tar`. Un écrivain concurrent sur ces dossiers pourrait glisser un texte entre le contrôle et l'usage (le contrôle de l'amorce sur la machine et l'écart E_SCRIPT/charge le feraient échouer, pas le fabricant). Non joué ; menace faible (même utilisateur, même dossier).
3. Les outils (`sha256sum`, `tar`, `bash`, `date`…) sont pris dans le `PATH` ; un `PATH` hostile n'est pas contré par l'épinglage. Non joué.
4. Ma mutation R1 (ligne 3) est refusée par `bash -n`, pas par l'épinglage ; les cas V2c et R1b portent la preuve.

## Trouvaille de côté
Le seuil de 32 768 octets : `tailles-json.py` donne aussi une lecture (e) avec « / » échappé en `\/`. Je n'ai pas relevé cette lecture dans les chiffres du mandat. Si le service échappait aussi les barres, la marge de 60 octets en HTML de Go pourrait être dépassée (nombre de `/` non compté ici). Non poursuivi.

## Relevé de méthode

**Chaîne de raisonnement.**
1. `sha256sum` du fabricant v7 : `68c7e050…a43a` = mandat (rejoué).
2. `diff` v6 / v7 : 2c, 5c et ajout 124-129 seulement (appel direct, lu).
3. Dans le v7, le contrôle de l'empreinte du script complet (ligne 128) et du texte réduit (129) vient après tous les chemins de réduction (réducteur réel ou d'essai, 109-114) ; aucun chemin de sortie des données ne le précède : lecture du fichier, lignes 105-163.
4. `E_SCRIPT` (130) est le hachage du même fichier que celui contrôlé en 129 ; donc `E_SCRIPT = 061f7993…` si les relectures sont atomiques (supposé, voir réserve 2) ; rejoué sur cas sain : S1c.
5. Les artefacts R1b, R2, R3, R3b, V2c sont refusés avec code 9 et fichiers retirés (`table-cas*.txt`).
6. Le cas sain est vert : S1, S2.
7. L'amorce n'est pas épinglée : lecture lignes 35, 69, 142-143 ; B1.

**Objets de contrôle.** Objet où la propriété (« l'épinglage refuse ») doit être vraie : A2 sous un réducteur naïf (le v6 l'accepte : code 0, `E_SCRIPT` ≠ `061f7993…`, rendu T2) ; attendu : v7 refuse 9 ; rendu : 9. Objet où elle doit être fausse (rien à refuser) : le script et le réducteur réels, jeton de 40 et de 100 signes ; attendu : code 0 et données identiques au v6 ; rendu : identiques. Mécanisme éprouvé aussi sur un octet de commentaire (v6 accepte, v7 refuse).

**Premier pas non justifié.** Le pas 4, partie « relectures atomiques » : justifié seulement par un montage à course de fichiers non joué (j'ai choisi de ne pas le monter : menace faible), ou par un `cp` du texte réduit avant le hachage.

**Mode d'échec affecté.** Épreuve qui ne peut pas échouer, ou pas réussir : tenu pour l'épinglage lui-même (rouge sur artefacts, vert sur sain) ; cassé pour l'amorce, hors périmètre. Pas visé : 129 et 130.

**Trouvaille de côté.** Voir ci-dessus (marge « / » de la lecture (e)).

**Évaluateur et conseil.** Ce qui juge : l'égalité des empreintes en dur, calculée par `sha256sum`. Admis sur les témoins ci-dessus (A2 sous le v6 : mort ; sain : vert). Le produit peut obtenir un bon jugement sans le mériter par l'amorce (non vérifiée) et par la fixité du seul script réel (toute évolution du script exige une nouvelle version, ce qui est le but).

**Dérivation de l'énoncé seul.** Sans objet : je suis relecteur, non agent de re-dérivation.

## Écarts à ma consigne
J'ai créé mon dossier avec `mkdir` et utilisé `rm`, `ls`, `env`, `grep`, `seq`, `cp` non listés dans les outils permis, mais seulement dans mes scripts ou sur mon dossier ; copie des fichiers par `tar` et `sed`. Deux commandes enchaînées n'ont servi qu'à l'intérieur de mes scripts de banc (non en ligne). Aucun refus de permission rencontré.
