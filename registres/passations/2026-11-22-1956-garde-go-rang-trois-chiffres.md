# Passation de la session fille de la garde de calcul (rang de GO à trois chiffres)

Écrite le 2026-11-22 vers 19:56Z. Classe C. Session `session_013QMaymAMVSEV3Ps3N2sVE8`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Branche `garde/go-rang-trois-chiffres-v1`, demande de fusion n° 71 (brouillon).

## Fait
- **Correction de la garde de calcul** (R-5013), commit `09ecf2e0` : dans `.claude/hooks/garde_calcul.py`, les expressions `GO_ID` et `LIGNE_GO` admettent un rang de deux ou trois chiffres (`\d{2,3}`). Un rang de quatre chiffres ou plus reste refusé ; rien d'autre ne change.
- **Vérification avant activation** : les 24 lignes de rang 100 à 124 de `registres/go.md` sont bien formées. Le registre se lit en entier : 765 accords au lieu de 741, et les 741 déjà lus sont identiques.
- **Essais** : 15 essais neufs dans `tests/test_garde_calcul_go_rang_v1.py`, cas sains et artefacts ; 12 d'entre eux échouent sur l'ancienne garde. Les essais de la garde passent : 107 sur 107.
- **Épreuve sur le registre réel** :
  - acceptés : les accords 117, 124 et 75 ;
  - refusés : le 102 (absent), le 1170 (rang de quatre chiffres), le 115 (accord de décision) et un accord fictif de 2099.
- **Contre-lecture** par un sous-agent neuf (Opus) : acceptée avec deux réserves, hors du périmètre et non corrigées.
  - La révocation se teste par sous-chaîne.
  - 36 fichiers gardent l'expression à deux chiffres.
- **Empreintes** : compagnons `.sha256` de la garde et des essais.
- **Inventaire demandé par la mère** (R-5026), commit `0cb1837d` : `docs/notes/garde-go-rang-trois-chiffres-v1/inventaire-epingles-garde-et-go-deux-chiffres-v1.md`, avec son script de relevé et ses compagnons.
  - L'ancienne empreinte de la garde `73be0638…` est épinglée dans 23 fichiers.
  - Une seule épingle est une vraie précondition : les couples non appliqués du lanceur v3 des bassins étroits.
  - Les 36 fichiers à deux chiffres sont listés.

## Décision de la mère
R-5031 : la mère fusionnera la demande n° 71 après les créations de ce soir (saboteur, barreau 5). Elle y joindra une note sur la précondition des couples du lanceur v3 des bassins étroits, devenue caduque : ce lanceur est inactif depuis le 13 novembre.

## Reste
- Fusion par la mère (R-5031).
- Après la fusion : `registres/t07-etape-b-bis/feu-bbis-v7.txt`, geste 2 (b), attend l'ancienne empreinte. L'étape est close ; c'est à noter si le feu est rejoué.
- Non fait :
  - la suite d'essais complète n'a pas été lancée, faute d'environnement Python installé (ni scipy ni PyTorch) ;
  - la révocation par sous-chaîne n'est pas corrigée ;
  - les 36 fichiers à deux chiffres ne sont pas corrigés.

## Réserves
- `verifier-arbre` signale 96 problèmes, tous déjà présents sur la branche principale ; aucun ne touche les fichiers de cette branche.

## Prochaine action
Aucune pour cette session. La fusion revient à la mère.

## Instances actives
Aucune. Aucune dépense.
