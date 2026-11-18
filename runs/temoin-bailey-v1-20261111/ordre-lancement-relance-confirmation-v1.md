# Ordre de lancement — relance de la confirmation du témoin de Bailey (addendum 7, § 2.1 ; addendum 8, option B), v1

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit avant la création du poste.

## Fondements
- Addendum 7 scellé (`554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e`) ; addendum 8 scellé,
  `prereg/temoin-attaque-publiee-bailey-v1-addendum-8-plafond-cout-relance.md`
  (`44326b34ce42ddc67935d9a98b780ab7e06a27bb2b82329d70842af76668f537`), option B seule.
- GO : `GO-2026-11-17-07` sur `main` (commit `32c698e2`), calcul, B = 85, plafond 90 USD, échéance 2026-11-30.
- Mots de Lazar : « vast recharge j'ai 100 euros de budget relance tout » ; « B » (relayé par la session mère vers
  02:05Z, `registres/passations/2026-11-18-0209-mot-lazar-bailey-addendum-8-B.md`) ; budget du jour : 100 euros au plus,
  recharge comprise.
- Reprise faite : `sortie-conduite-v15/reprise-v10-2/` (poste de reprise v5, marque `poste-fini-reprise-v5.json`),
  transferts complets, 61049303 détruite à 02:38:27Z ; K′ = 17 (nombre de lignes du journal des durées, champ technique).
- Code : commit `a904aa391cdcf2650b747fe64e48caa0ec8c5849` (arbre `src/` de la tête `e3f066a9…`, égal au sien).
- Pièces scellées (commit `37afe0a8`) : `lancer-conduite-v16.py` (`3411bd80731c80faae077ecff39f2b216c56ec1613c830e05750efd4c998585e`),
  `poste-hetzner-v14.sh` (`ca4fd2bd14219407326c6db2c3613f4ccc34b5428c38d206cc620e53d8ab1921`),
  `construire-donnees-demarrage-v14.py` (`ab681e899d3f844629190d83ebf100b2745086e788ff6a6d5c24ff91934ba922`) ; générateur v3
  scellé (`df13783a…`) ; contre-lecture `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-pieces-relance-v16-bailey-v1.md`.
- Paramètres : D des antérieures 22,9252 USD ; t du pilote 1 265,0215 s ; K = 72 pour tout c ≤ 1,6 ; plafond de coût
  de l'offre 1,40 USD/h (carte et 110 Go) ; garde pilote 1 800 s sans objet (aucun pilote sur l'instance neuve).
- Recherche à blanc (lecture seule) à 02:49Z : une offre au filtre et sous 1,40 (59284715, machine 146917, 1,2243).

## Relevé du § 2.5 (2026-11-18T02:55:09Z, `vastai show user` et `vastai show instances`, vastai 1.11.0)
- Compte : {"credit": 22.372859139957654, "balance": 0, "has_billing": true, "autobill_threshold": 5.0, "autobill_amount": 5.0, "billing_failed": false}
- Condition du § 2.5 : recharge automatique configurée, `billing_failed` faux, `credit` ≥ seuil : **tenue**.
- Autres instances du compte : 58936096 « R8 m=2 Llama-3.1-Tulu-3-8B-DPO » exited 0.5611 ; 58936099 « R8 m=3
  Llama-3.1-Tulu-3-8B » exited 0.5611 ; 58936100 « R8 m=4 Llama-3.1-8B » exited 0.6196 ; 60988826
  « jeu-idee-1-1-relance-v1 » exited 0.0533. Aucune n'est du témoin. Relevé non repris pendant l'attente d'une offre.

## Gestes
1. Constructeur v14 joué dans un dossier neuf hors du dépôt (scratchpad), effacé après la création ; empreinte du script
   sans secrets comparée à `poste-hetzner-v14.sh.sha256`.
2. Création du poste Hetzner (`cx23`, `fsn1`, `debian-12`, `poste-temoin-bailey-v14`) par l'API, sous `GO_ID=GO-2026-11-17-07`.
3. Surveillance : `poste-hetzner-v14-etat.txt`, `offre-choisie-v14.json`, champs techniques de la conduite v16
  (`relance_seule.K`, c, tours complets, gardes), crédit et paiements (alerte sous 4 USD ou si `billing_failed`).
  Vérifier c ≤ 1,40 et K ≥ 71 ; détruire le poste par identifiant dès sa marque de fin ou une ligne d'arrêt.
4. Aucune note ni aucun verdict du témoin n'est lu avant la clôture (§ 3).
