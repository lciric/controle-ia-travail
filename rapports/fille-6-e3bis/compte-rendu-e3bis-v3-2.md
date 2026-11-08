# Compte rendu d'E3 bis (T0.6, chaîne v11) — fille 6 — jalon intermédiaire 2 (suite ciblée finie, run démarré), 2026-11-08T07:00Z ; remplace le jalon 1 du 2026-11-08T06:13Z

Ordre `docs/procedures/ordre-fille-6-t06-e3bis-v3.md` (1e2e3259…, R-1755 ; couples 456957e4…), commit d'épreuve c01d29ea (prep/t06-v11), configuration `config-t06-epreuve-e3bis-v3.json` (seule différence avec v2 : prix_max_usd_h 1.3 → 2.1). GO-2026-11-07-08 et GO-2026-11-06-01 ; autorisation de Lazar dans la session de la fille 6 (R-1752) : « J’autorise la fille 6 à louer, surveiller et détruire sur Vast l’instance de l’épreuve E3 bis de T0.6, sous GO-2026-11-07-08 et GO-2026-11-06-01 (plafond 5,70 USD, création au plus tard le 10 novembre). » Aucune valeur de clé, aucune sortie brute de vastai.

## État : suite ciblée réussie, run en cours

## Écarts acceptés
Jeton `CONTROLE_IA_GITHUB_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` sous `env -i` (R-1667) ; arbre `git worktree` détaché (au lieu d'un clone) ; environnement `/home/user/venv-depot`.

## Tentatives antérieures sans création (0 USD)
- Ordre v2, 02:33Z : création refusée par le classificateur de la session (autorisation de Lazar d'E2/E3 ne couvrant pas E3 bis) ; puis mot de Lazar (R-1752).
- Ordre v2, 05:34Z : `creation auto` code 3, « liste VIDE » (aucune A100 80 Go ≤ 1,3 USD/h et fiabilité ≥ 0,98).

## Préalables et étapes 1 à 3 (05:46–05:47Z)
- verifier-arbre : 150 problèmes, aucun sur une pièce de l'épreuve ; config v3 OK ; liste ciblée 81 lignes ; REGGO (main) : GO-2026-11-06-01 = 1, GO-2026-11-07-08 = 1 ; dépense antérieure 2,092 (E2 0,627 ; E3 1,465, factures stables) ; inventaire t06-e3 = 0.
- Étape 1 : code 0, « CONTRÔLES D'ÉPREUVE CONFORMES : S=c01d29ea… ; amorce v9 6a6897ce… ; GO GO-2026-11-07-08 (plafond de l'épreuve 5.7 USD sur 8 ; plafond d'épreuve 5.7 + dépense antérieure 2.092 = 7.792 ≤ 7.9) ; mode reel … ».
- Lecture (05:46:51Z), filtre `… gpu_ram>=78 … dph_total<=2.1`, erreurs vides : avec tout 3 offres (cuda min 13,0 ; gpu_ram min 81920) ; sans cuda 3 ; sans gpu_ram 3. Offres : 1,4449 (stockage 0,1118 > 0,08) ; 1,5563 (stockage 0,2083 ; dl 0,0391) ; 2,0694 (stockage 0,0694 ; dl 0,0040 ; rel 0,9979).
- Étape 3 (05:46:55Z) : « OFFRE CONFORME : id=41153689 rang=3 machine=67802 prix_carte=2.000000 prix_stockage=0.069444 dph_total=2.069444 telechargement=0.0040 telechargement_forfait=0.1600 cuda_max_good=13.2 carte=A100 SXM4 80 Go … plafond=5.7 ». Règle des 2,5 h : 2,069444 × 2,5 + 0,16 = 5,33 ≤ 5,70.

## Instance
- Identifiant **59671807**, créée **2026-11-08T05:47:22Z** ; branche `essai/t06-e3bis-v1`.
- Garde de dépense : ARRET depense à 5,70 USD ≈ création + 2 h 41 (≈ 08:28Z).

## Jalons relevés
- « AMORCE T06 v9 DEMARRAGE 1 : 2026-11-08T05:47:57Z, machine 59671807, commit c01d29ea0d5c29b584f23cc63e1aac9aaefcef66 »
- « AMORCE 2026-11-08T05:48:58Z : CLONAGE mode=reel secondes=61 octets_git=176730400 octets_arbre=386039683 debit_Mo_s=9.23 motifs=28 »
- « branche essai/t06-e3bis-v1 poussée avant l'installation (droit d'écriture éprouvé) » (05:49:01Z)
- nvidia-smi : « NVIDIA A100-SXM4-80GB, 595.91.07, 81920 MiB » (E3-1)
- « AMORCE 2026-11-08T05:51:24Z : MATERIEL MemTotal_ko=2101179772 coeurs=255 flock=oui » (E3-10)
- « torch 2.14.1+cu130 cuda 13.0 disponible True » (E3-1)
- « 2026-11-08T05:51:30Z suite ciblée : 81 fichiers d'essais, liste scripts/tests-cibles-t06-v1.txt sha256 562b65facf1bcbf765f4e8b0d9e27c2c5b41edadb050701e7350bbce47081572 »
- Dernière ligne du journal au relevé de 2026-11-08T06:13Z : «  »
- Surveillance v11 : « 2026-11-08T06:12:14Z POURSUIVRE »

## Suite ciblée et démarrage du run
- **E3-2, dernière ligne exacte de la suite ciblée : « 1878 passed in 4009.60s (1:06:49) »** (2026-11-08T06:58:22Z) ; N = 1878 (estimation de l'ordre : 1 878) ; aucun échec, erreur, essai sauté ni désélectionné ; durée 1 h 06 min 49 s (estimation 40 à 50 min).
- **E3-12 : « 2026-11-08T06:58:22Z run : 20261108-065822-t06-reel (sans couperet de temps ; lanceur v5) »** : le run démarre avec la configuration d'épreuve.
- Surveillance v11 : POURSUIVRE (06:59:03Z). Garde ARRET depense (5,70) attendue vers ≈ 08:28Z ; il reste ≈ 1 h 28 min de run avant elle.

## À venir
Dernière ligne exacte de la suite ciblée (E3-2), run (E3-3 à E3-9, E3-12), fin, destruction, factures, texte de `show instance` après destruction.
