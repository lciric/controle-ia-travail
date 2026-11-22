# Contre-lecture de la commande de création v2 (essai 3 du palier 0b) — v1

Contre-lecteur : sous-agent Sonnet neuf, lecture seule, n'ayant pas écrit la pièce. Rapport recopié tel quel.

Verdict : Conforme avec réserves

1. Diff. La v2 ne change que ce qu'elle déclare : titre, en-tête (retire aussi la phrase « Fixée sur la décision de 02:30Z », non déclarée, sans conséquence), préalables 1 et 4, commande 1, deux lignes « après l'envoi » (garde des 2 h, refus du classifieur), et le rappel de révocation du jeton 2. La section « Différence » omet l'en-tête et le rappel de révocation (mineur) ; « mot pour mot » est inexact pour l'en-tête.
2. Fabricant. Le premier argument est bien un NOM, lu par `${!NOM}` puis `unset`, jamais affiché ni passé en argument. Forme du nom : `^[A-Za-z_][A-Za-z0-9_]*$` ; `CONTROLE_IA_GITHUB_TOKEN_2` passe et n'est pas dans la liste des noms réservés. Le jeton doit faire 20 à 100 signes dans `[A-Za-z0-9_-]` : un `github_pat_…` de 93 signes passe (non testé). Seule la valeur de la variable exportée peut échouer (code 3).
3. Empreintes (sha256sum sur disque, toutes concordantes) : fabricant v8 a91f3403… ; script v6 f61aea46… ; amorce v6 524cfc4a… ; réducteur v6 b1a4d216… (auteur-fabricant-v8-amorce-epinglee/reduire-script-v6.py) ; outil v2 73046b31… ; lanceur v4 b989db6e… (lancer) et 64b2c0ce… (démarrer) ; gardien v4 ba39fe9b… et b333b2eb… (demarrer-gardien), identiques aux épingles du fabricant. v1 = 4129b36a… confirmée. Le fabricant épingle aussi le texte réduit 061f7993…, absent du préalable 3.
4. Risques et ambiguïtés.
 a. SORTIE doit être un chemin absolu hors de tout dépôt git (refus 4). La commande dit « dossier de travail de la session », qui est ici /home/user/controle-ia-travail, un dépôt git. Il faut un chemin absolu explicite hors dépôt. RELEVE-A-BLANC et RELEVE-CREATION sont aussi des placeholders relatifs.
 b. Les « …/ » ne sont pas résolubles tels quels : à remplacer par le chemin absolu du dossier lancement-essai-court-mesure-v1.
 c. Le préalable 1 renvoie à une « réserve du GO », mais GO-2026-11-22-04 ne figure pas dans registres/go.md (grep vide) ; il n'apparaît que dans registres/essaim/vers-mere/. À inscrire avant l'envoi.
 d. Les deux fichiers v2 ne sont pas commités, ce qui est attendu.
 e. Aucune fuite du jeton visible dans la pièce. Le jeton 2 reste plus largement porté que l'essai court prévu, d'où le rappel de révocation, présent.

## Suite donnée (session de l'organisme)
- a, b et l'épingle 061f7993… : corrigés dans `commande-creation-production-essai-3-v3.md`.
- c : sans objet. La ligne GO-2026-11-22-04 est sur `main` (`registres/go.md`) ; le registre de la branche `lot/compte-organisme-v1` est en retard sur `main`.
- Remarques du point 1 : reprises dans la section « Différence avec la v1 (rappel) » de la v3.
