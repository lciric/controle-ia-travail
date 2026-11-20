# Compte rendu d'exécution — étage 1 de la ligne 3 — v1

Heure d'écriture : 2026-11-20T07:26Z (`date -u`). Aucune valeur de mesure lue ni rapportée.

Python : 3.13.18 (`python3 --version`). numpy 2.5.3. Additif tiré de origin/main, empreinte f5562d20...4e5f25a vérifiée : f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a. Les 18 fichiers du code énumérés à l'additif § 3 sont égaux à la table.

Commandes (depuis CODE = docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v3, par `env -C`) :
1. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py --modules numpy` : code_retour 0 (champ du rapport), aucune anomalie.
2. Chronométrage : `python3 -B chronometrer_banc_ligne_3_v3.py --autorisation-additif <D>/autorisation/additif-2-code-v3.md --empreinte-additif f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a --manifeste <D>/chronometrage` ; terminé sans erreur ; durée mesurée du chronométrage 1,718 s ; durée totale estimée de l'étage 1 : 6892,922 s.
3. Étage 1 : `python3 -B banc_juges_scriptes_ligne_3_v3.py --decisif --autorisation-additif <D>/autorisation/additif-2-code-v3.md --empreinte-additif f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a --sortie <D>/etage-1` ; en tâche de fond, une seule fois ; code de sortie 0 ; durée entre lancement (environ 05:51Z) et notification de fin (avant 07:26Z), non chronométrée plus finement.
<D> = /tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/execution-etage-1-ligne-3

Gardes lues (seuls champs) : dossier_du_code_propre = true dans les deux manifestes ; programme_sha256 = 09bfe0db...370ba0 (égal à la table) ; programme_chronometrage_sha256 = 8cb61afb...a7e (égal) ; chemin_additif et empreinte_additif égaux à ceux donnés ; racines : chronometrage 2026111931 ; étage 1 tirages 2026111932, rééchantillonnage 2026111933 ; versions.numpy = 2.5.3.

Sorties (compagnons vérifiés par `sha256sum -c`, OK) :
- etage-1/resultat-etage-1-ligne-3-v3.json eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce
- etage-1/manifeste-etage-1-ligne-3-v3.json 6c64c32c1d0bf7257e5b00277051de26dcedffec6fb0193066164cda9053eb92
- chronometrage/manifeste-chronometrage-ligne-3-v3.json fe3069ec637f69ff5ae09cb236d13aad644ac01323b91f9e988bef99a53f9db0

Arrêt, incident, refus : aucun.
