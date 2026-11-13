# Témoin de Bailey — cause de l'interruption corrigée : crédit Vast épuisé — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Complète les notes `…-0548-…` (`b797cb97…`) et
`…-0610-…-reprise-refusee-noeud.md` (`01ff293b…`), dont l'hypothèse « coupure de l'hôte » est remplacée.

Mot de Lazar, verbatim : « plus de credits sur vast ».
Relevé (`vastai show user`, champs de crédit seulement, ≈ 07:20Z) : `credit` 0 ; `balance` −0,933 USD ;
`balance_threshold` −0,01 (activé). Factures : charges de carte et de stockage de plusieurs chantiers (dont 60432755
« p3bis-v1 », carte ; 58936096/99/100, stockage). Cause la plus probable de l'interruption : solde épuisé, Vast arrête les
instances du compte (60417353 et 60432755 « exited », `intended_status: stopped`) ; le redémarrage de la reprise est
refusé pour la même raison. L'indisponibilité de la machine 146915 (`rentable: false`) n'est plus tenue pour la cause.

Conséquences :
- Interruption pendant le run principal, cause nommée : crédit du compte épuisé (ni la carte, ni l'hôte, ni le code).
- Risque : une instance arrêtée sur un compte en solde négatif peut être supprimée par Vast ; les journaux de la
  première exécution (non transférés) seraient alors perdus.
- La reprise (lecture 38) redevient possible dès que le compte est crédité.

Nœud (inchangé dans sa forme, options révisées) : (a) Lazar crédite le compte, puis la session relance la reprise
(transfert, scellement sans lecture, destruction), puis la relance est décidée sur K′ mesuré ; (b) arrêter le témoin.
Recommandation : (a), crédit d'au moins ≈ 50 USD pour le seul témoin (reprise ≈ 1 USD ; relance attendue ≈ 35 à 45 USD
si K′ < 20), en plus de ce que les autres chantiers consomment.
