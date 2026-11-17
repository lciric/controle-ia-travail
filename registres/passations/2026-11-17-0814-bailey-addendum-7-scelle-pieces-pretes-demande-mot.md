# Témoin de Bailey — addendum 7 scellé, GO inscrit, pièces scellées, mot de lancement demandé

**En tête (addendum 7, § 4 et § 5 (e)) : gel de `src/` sur la branche `claude/compassionate-meitner-d4ryyk`** — l'arbre
`src/` reste celui du commit `a904aa39` jusqu'au dernier contrôle final de la lecture ; aucune lecture de note ni de
verdict du témoin avant la clôture de la confirmation (§ 3) ; l'ordre « verdict à 36 tours avant le lancement » des
pièces antérieures est remplacé par l'addendum 7.

Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), 17 novembre 2026, sous l'autonomie de
`GO-2026-11-17-01` et le « go, enchaîne la ligne GO et les pièces » de Lazar.

## Fait
- Addendum 7 scellé : `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` (`554a74d0…`, commit
  `144a39d5`), après la contre-lecture et douze vérifications adverses (`docs/notes/reproduction-attaque-publiee-v1/
  verification-adverse-addendum-7-bailey-v1.md` à `-v12.md`, toutes scellées).
- Code de lecture : `src/controle_ia/temoin_bailey/lecture_scellee_v3.py` (`a367853b…`), commit du code `a904aa39`
  (v1 et v2 gardées sans servir) ; 307 essais passés, 1 sauté ; répétition sur dossier factice consignée.
- Ligne `GO-2026-11-17-07` inscrite sur `main` (commit `32c698e2`, par index temporaire, sans arbre de travail de main :
  le disque était plein) ; elle passe `ligne_go`, `verifier_go(…, 85)` et `verifier_non_revoque`.
- Pièces scellées (commit `06aa441a`) après contre-lecture (`contre-lecture-pieces-confirmation-bailey-v1.md`) :
  `lancer-conduite-v15.py`, `poste-hetzner-v13.sh`, `construire-donnees-demarrage-v13.py`, `manifeste-local-v7.json` ;
  générateurs v2 et v3 ; recherche à blanc vastai consignée.

## Incidents
- Un `git checkout -q 9c3613d6 --` mal formé a détaché la tête sur `9c3613d6` après le commit de scellement `144a39d5`
  (déjà poussé) ; remise sur la branche aussitôt, arbre propre, `src/` égal à `a904aa39`, scellement de l'addendum
  vérifié. Aucun fichier sous `runs/` n'a été ouvert.
- Disque plein à l'ouverture d'un arbre de `main` : arbre retiré ; copies d'essai du scratchpad effacées (`clone2`,
  `pytest-tmp`, `r2v7`, `r2v9`).

## Reste
- Mot direct de Lazar pour le lancement (condition 7) : demandé avec ce dépôt.
- Ensuite : relevé du § 2.5, ordre de lancement, constructeur v13 dans un dossier neuf hors du dépôt, création du poste,
  surveillance, clôture, attendus, lecture scellée, deux lecteurs, contrôle final, rapport (§ 3, § 6).
- À relayer (inchangé) : serveur de sauvegarde Hetzner 176187199 ; dépôt chez le tiers des addenda 3 à 7 ; retrait de
  la clé de déploiement `diag-temoin-bailey-depot-20261115` et de la clé ssh Vast 1864483 ; révocation du jeton GitHub.

## Instances actives
Aucune instance Vast ni poste Hetzner du témoin (hors le serveur de sauvegarde 176187199, gardé).
