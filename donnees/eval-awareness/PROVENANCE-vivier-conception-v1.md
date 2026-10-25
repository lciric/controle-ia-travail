# Provenance — vivier de conception « conscience d'évaluation » v1

Extrait le 25 octobre 2026 (08:27 UTC) par la lignée « session-depot », dans son conteneur, sur la demande de Lazar
(« demande à claude depot de le lancer », 09:19 heure de Paris, relayée par « conv-audit », message n° 34).

- Script : `extraire_sous_ensemble_eval_awareness_v5.py` (`689cf292…`, de « conv-audit », lu en entier avant exécution :
  aucun sous-processus, aucun code téléchargé exécuté), environnement Python isolé, `python -I`, dossier neuf.
- Source : `jjpn2/eval_awareness` (Hugging Face), `snapshot_download` (révision `5d724f12988284a652749c56ec7b2356b0d14408`) ;
  `dataset.zip` d'empreinte `934dc4bc83b76e6bc57e672c39716061204b4802bb46b2038e7feb822aaa211c`, **la même que celle du
  sous-ensemble v1** ; mot de passe du zip : la mesure publique anti-contamination des auteurs (`scripts/decrypt.sh`),
  passé par `--mot-de-passe` comme dans la consigne d'origine (`consigne-vivier-powershell-v1.txt`, `4dcc0687…`) ; une
  première tentative avec la détection automatique du script a été refusée (mauvais motif lu ; rien n'a été écrit) ;
  la seconde lit la copie téléchargée (`--local`).
- Commande : `--complement-de eval-awareness-sous-ensemble-v1.json` (`31761ede…`, 120 items) ; aucun `--champ-…`.
- Sortie : `eval-awareness-vivier-conception-v1.json`, 786 exemples, sha256
  `be312967210679d94b207c04e74c85df4e2676dbb9779820df3757995e0aa469` ; 976 lignes, 70 GAIA exclues, 906 sans GAIA ;
  `ids_exclus` = 120 ; 786 identifiants uniques, **aucun recouvrement** avec les 120 (vérifié ici et par l'assertion du
  script). Comptes par strate : (évaluation, agentique) 150 sur 180 ; (évaluation, non agentique) 257 sur 287 ;
  (usage réel, agentique) 196 sur 226 ; (usage réel, non agentique) 183 sur 213.
- Licence CC BY-NC-SA 4.0 ; dépôt privé seulement ; GAIA exclu et non redistribué. Reste à faire par « conv-audit » :
  disjonction contre le fichier secret de la banque, `charger_vivier` au code de l'étape 1.
