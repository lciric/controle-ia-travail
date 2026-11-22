# Vérification du fabricant v8 — v1

**Verdict : Conforme avec réserves.** Les deux contrôles ajoutés sont rouges sur les artefacts et verts sur le cas sain, sans fichier partiel. Réserve : l'amorce est relue par son chemin après le contrôle (fenêtre de course, non fermée par le v8).

## Table des cas (banc : `outils/banc.sh` ; sorties dans `tables/`)
| # | Cas | Attendu | Rendu | Fichier |
|---|---|---|---|---|
| 1 | diff v7 → v8 | 2 lignes d'en-tête, +3 lignes (épinglage), +3 lignes (comptage) | exactement cela ; empreintes en dur justes (`sha256sum` des pièces : amorce 524cfc4a…, fabricant a91f3403…, v7 68c7e050…) | diff rejoué en session |
| 2 | sain, jeton factice 32 signes, v7 puis v8 | données identiques | code 0 ; `cmp` brut identique (même seconde, H0 identique) ; identique aussi sans ligne 2 ; 1 seule ligne `E_SCRIPT=`, ligne 4 = 061f7993… | `sain-l2-v*.txt`, `sain-compte-escript.txt`, `codes.txt` |
| 3 | sain, jeton 100 signes | 32 653 / 32 708 | 32653 (marge 115) / 32708 (marge 60) | `sain-marges.txt` |
| 4 | amorce modifiée d'un octet | refus 9, rien d'écrit | code 9 « épinglage : amorce 30a8f368… » ; dossier de sortie vide | `amorce1.stderr`, `amorce1-fichiers.txt` |
| 5 | amorce sans sa ligne de contrôle d'empreinte | refus 9 | code 9 (hachage différent) ; sortie vide | `amorce-sans-controle.*` |
| 6 | témoin : v8 sans les lignes 70-72, amorce intacte | passe | code 0 (le comptage seul ne gêne pas le cas sain) | `sans-epingle-diff.txt` |
| 7 | v8 sans épinglage + amorce à 2 lignes `E_SCRIPT=` (seule mutation du fabricant : 3 lignes retirées) | refus 9, sans fichier | code 9 « 2 ligne(s) E_SCRIPT= » ; sortie vide (charge et sans-jeton retirés) | `deux-lignes.stderr`, `deux-lignes-fichiers.txt` |
| 8 | même amorce, v8 intact | refus 9 | code 9 par l'épinglage | `deux-lignes-v8.stderr` |
| 9 | contournement par variables `AMORCE`, `E_AMORCE_EPINGLE`, `E_AMORCE`, `FABRICANT_AMORCE` ; nom de variable-jeton `E_AMORCE` | sans effet | code 0, données portent l'amorce épinglée (`Amorcf` : 0 occurrence) | `contourne-*`, vérifié dans `cas/` avant retrait |
| 10 | amorce = lien symbolique vers amorce autre | refus | code 9 (hachage suit le lien, donc contrôle le contenu réel) | `lien.stderr` |
| 11 | relecture après contrôle (injection d'un ajout dans l'amorce juste après la ligne 72) | à voir | code 0 : l'ajout est dans les données ; aucun contrôle ne le voit | `relecture-diff.txt`, `relecture-dans-donnees.txt` |
| 12 | amorce avec `E_SCRIPT+=x`, épinglage retiré | à voir | code 0 : le comptage ne voit pas `+=` | `plus-egal.*` |

## Relevé de méthode
**Chaîne de raisonnement.**
1. Le diff v7/v8 (rejoué) ne montre que l'en-tête (lignes 2 et 5), les lignes 70-72 et 149-151. Pièce : fabricants, empreintes ci-dessus.
2. Cas 2 : v7 et v8 donnent des octets identiques (`cmp` brut rc 0). Cas 3 : marges 115 et 60 = prétendues.
3. Cas 4-5, 7-8 : refus 9, dossier de sortie vide, à chaque artefact. La ligne 72 s'exécute avant toute écriture (CREES vide) ; le refus de la ligne 151 retire charge et sans-jeton (CREES, ligne 138).
4. Le comptage est indépendant de l'épinglage : cas 7 (épinglage retiré) refuse encore ; cas 6 (même mutation, amorce saine) passe.
5. L'amorce est hachée par `sha256sum < "$AMORCE"` (ligne 69) puis relue par le même chemin (lignes 74-76, 78, 146). Cas 11 : une écriture entre contrôle et assemblage passe inaperçue. Le chemin est fixe (`$ICI/…`, non remplaçable par variable : cas 9), donc le risque est une écriture concurrente seulement.
**Objets de contrôle.** Faux par construction : amorce à un octet changé, amorce à deux lignes `E_SCRIPT=`. Vrai : amorce du dépôt. Attendu rouge/rouge/vert ; rendu rouge/rouge/vert. Le comptage est éprouvé sur lui-même (épinglage retiré) : rouge sur deux lignes, vert sur amorce saine.
**Premier pas non justifié.** Pas 5, partie « aucune écriture concurrente » : non démontrée ; supposé (la machine du fabricant n'a qu'une session). La justifierait un hachage des octets réellement assemblés (ex. hacher la partie amorce du fichier de sortie après assemblage).
**Mode d'échec affecté.** Tenu pour les deux contrôles (rouges sur artefacts, vert sur sain, pas de contournement par variable ni lien). Cassé seulement au sens étroit de la relecture (cas 11).
**Trouvailles de côté.** (a) Le comptage `grep -F 'E_SCRIPT='` ne voit pas `E_SCRIPT+=` (cas 12) ; sans portée tant que l'amorce est épinglée. (b) `E_AMORCE` n'est pas dans la liste de noms réservés, sans effet (cas 9). (c) Banc joué avec `FABRICANT_BANC=oui` et un dépôt distant local, le chemin réel (GitHub) non joué.
**Évaluateur et conseil.** Le juge est la sortie du fabricant lui-même (code, fichiers présents) ; admis ici par le témoin sain (cas 2, 6) et les artefacts. Il pourrait « réussir » sans le mériter par la fenêtre du cas 11, non fermée.

Outils : `outils/banc.sh`. Dépôts factices et `cas/` retirés.
