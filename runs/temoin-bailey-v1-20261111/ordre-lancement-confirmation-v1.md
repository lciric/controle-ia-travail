# Ordre de lancement — confirmation du témoin de Bailey (addendum 7), v1

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit avant la création du poste.

## Fondements
- Addendum 7 scellé : `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` (`554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e`).
- GO : `GO-2026-11-17-07` sur `main` (commit `32c698e2`), calcul, B = 85, plafond 90 USD, échéance 2026-11-30.
- Mot de Lazar (condition 7) : « go, lance la confirmation » (note de passation du même jour).
- Code : commit `a904aa391cdcf2650b747fe64e48caa0ec8c5849` (arbre `src/` de la tête égal au sien).
- Pièces scellées : `lancer-conduite-v15.py` (`ba682c80dba7ed0483d1ea0d86bd27c0c34175e4ff3729b026f2e2e7e7edb17c`), `poste-hetzner-v13.sh` (`4c7bafaeff50a825b17e01fbb4ed3e39efb83a22503aefc30f51206dc687aca2`),
  `construire-donnees-demarrage-v13.py` (`b6fab228fe1b6d2f498f5a74280f5d98b7d2291a43d418bf56d8ad04c1ef8ee9`), `manifeste-local-v7.json` (`3cf1413204ed2871fa1e8951c75069244dcc12befe7070113661c41d9760b6d8`).
- Paramètres : `t_max_pilote_s=1800` (garde du § 2.3, exigée par la conduite), aucune instance antérieure, filtre du § 2.4
  (`cpu_cores_effective>=32 cpu_ghz>=2.4`, coût carte et 110 Go ≤ 1,6 USD/h), disque 110 Go, fenêtre de 24 h sans offre
  (bornée à 23 h 45 dans le poste), image `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` (celle du poste v12).

## Relevé du § 2.5 (2026-11-17T09:16:10Z, `vastai show user` et `vastai show instances`, vastai 1.11.0)
- Compte : {"credit": 7.728586549959573, "balance": 0, "has_billing": true, "autobill_threshold": 5.0, "autobill_amount": 5.0, "billing_failed": false}
- Condition du § 2.5 : recharge automatique configurée (`has_billing` vrai, seuil et montant > 0, `billing_failed` faux), `credit` ≥ seuil : **tenue**.
- Autres instances du compte (identifiant, étiquette, état, `dph_total`) : 58936096 « R8 m=2 Llama-3.1-Tulu-3-8B-DPO » exited 0.5611; 58936099 « R8 m=3 Llama-3.1-Tulu-3-8B » exited 0.5611; 58936100 « R8 m=4 Llama-3.1-8B » exited 0.6196; 60988826 « jeu-idee-1-1-relance-v1 » running 0.0533.
  Aucune n'est du témoin (préfixe `temoin-bailey-c6-`). Le relevé n'est pas repris pendant l'attente d'une offre (§ 2.5).

## Gestes
1. Constructeur v13 joué dans un dossier neuf hors du dépôt (scratchpad), effacé après la création ; empreinte du script
   sans secrets affichée par le constructeur comparée à `poste-hetzner-v13.sh.sha256`.
2. Création du poste Hetzner (`cx23`, `fsn1`, `debian-12`, nom `poste-temoin-bailey-v13`) par l'API, sous `GO_ID=GO-2026-11-17-07`.
3. Surveillance : états poussés par le poste (`poste-hetzner-v13-etat.txt`, `offre-choisie-v13.json`, champs techniques
   seulement), crédit et paiements à chaque réveil (alerte sous 4 USD ou si `billing_failed`), rappels au plus toutes les 90 min.
4. Aucune note ni aucun verdict du témoin n'est lu avant la clôture (§ 3).

