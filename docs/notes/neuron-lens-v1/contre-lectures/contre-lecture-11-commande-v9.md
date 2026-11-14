# Contre-lecture 11, ciblée, de la commande v9 (minuterie v1 et son essai, essai de survie, pièce `pip` v2) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `8cdaba61` de `prep/neuron-lens-v1` par la session de reprise ;
lecture seule du dépôt ; essais de la grammaire du shell et rejeu unique de l'essai de la minuterie dans le bac de travail de la
session (faux outil seulement) ; aucun appel réseau, ni outil réel du loueur, ni variable secrète. Résumé fidèle (toutes les remarques,
formulations raccourcies) ; suites dans l'en-tête de la commande v10.

**Verdict de tête** : Q-1 et Q-2 (bloquantes de la contre-lecture 10) traitées et éprouvées par ses propres essais ; plus de bloquante
pour la location ; trois petites corrections de texte avant scellement (R-1, R-2, R-3).

**Empreintes** (vérifié) : les 19 pièces du tableau de la v9 égales aux compagnons et au tableau (dont v8 `afb08ad0…`, `pip` v1
`d1476842…`, `pip` v2 `e35e585b…`, minuterie `25b615a0…`, son essai `0f6d2a84…`, journal de la minuterie `2e6352c9…`, essai de survie
`2b590322…`) ; compagnons de la v9 et de la v8 justes ; `bash -n` sans erreur sur les deux scripts.

**Q-1 à Q-9**
- Q-1 traitée (commande v9 l.115-120 ; script l.15-26) : durée calculée à part et contrôlée ; seul le lancement détaché porte `&` ;
  PID écrit par la minuterie, lu dans le fichier. Essai (vérifié) sous `set -m` : `$!` = 26298, fichier = 26300, le processus qui dort,
  arguments visibles par `ps -p` ; `D` resté défini (700) ; `kill` sur ce PID arrête la minuterie, faux outil jamais appelé.
- Q-2 traitée : préambule P au début de chaque commande (l.66, l.10) ; chemin absolu à la minuterie (l.118), refus d'un chemin relatif
  ou non exécutable (script l.22-23) ; garde par `exec env PATH=…` (l.129), `/proc/<pid>/environ` du processus après `exec` porte le
  `PATH` passé ; le suivi lit `VASTAI_OUTIL` exporté par P (`suivi_vast_v4.py:78`) ; la garde appelle `vastai` par son nom
  (`garde_depense_v3.py:104,119`), `PATH` transmis explicitement. Réserve R-1 sur l'étape 6.
- Q-3 traitée : trois appels successifs (lancement, vivant, échéance et faux outil appelé) ; `PATH` de la garde (témoin écrit) ;
  limite : survie éprouvée sur 90 s, jamais sur des heures (supposé).
- Q-4 partiellement : PID et durée écrits (étapes 7, 8), `ps -p` vivant puis mort (l.120, 131, 185) ; rien n'écrit l'identifiant
  d'instance, l'heure de création ni le prix annoncés l.68 (R-2).
- Q-5 traitée : bornes 600 à 108000 s ; 5, 200000, vide, « abc » → code 3 (journal, et rejoué).
- Q-6 traitée (l.207-209 ; l'info sur le renommage non reprise, sans effet).
- Q-7 traitée (l.199-200, 210-211).
- Q-8 traitée : ordre de lancement expliqué ; dernière ligne « fin : arret code 1 (commit verifie) » cohérente avec l'amorce v6 (l.164,
  172) ; limite écrite ; horaire non vérifiable par lui (supposé).
- Q-9 info, inchangée comme annoncé.

**Remarques nouvelles**
- **R-1. Moyenne.** Étape 6 (l.102-105) : la v9 promet que toute heure consignée vient de `date -u` dans la même commande, mais le bloc
  de création n'a aucun `date -u` ; `<ISO_CREATION>` alimente `--debut` de la minuterie et de la garde. Correction : `date -u +%FT%TZ;`
  juste avant la création, ou l'heure relue par `suivi_vast_v4 instance <ID>`.
- **R-2. Mineure.** l.68 et 107 : rien n'écrit la ligne « identifiant, heure de création, prix » de `pids-volet-a-v1.txt`. Correction :
  `echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-volet-a-v1.txt`.
- **R-3. Mineure.** l.185 : juste après un `kill`, le processus paraît quelques instants zombie (`Zs`, `<defunct>`, `ps` au code 0 moins
  de 2 s, essayé) : écrire « mort (laisser 2 s ; un état `Z` compte comme mort) ».
- **R-4. Mineure.** l.184 : vérifier avant tout `kill` que le PID lu porte encore les bons arguments (réattribution possible après un
  redémarrage du conteneur, R10).
- **R-5. Info.** Le `sleep` orphelin reste vivant jusqu'à D s (jusqu'à 30 h), sans effet (essai) ; une mention à l'étape 13 suffit.
- **R-6. Info.** l.89 : `python scripts/depot_reduit…` sans `.venv/bin/python` (supposé : `python` présent, le script a servi à l'essai
  v7).
- **R-7. Info.** Journaux de la minuterie et de la garde et fichiers de PID écrits sous `docs/notes/neuron-lens-v1/` salissent l'arbre
  jusqu'au commit ; seul `pids-volet-a-v1.txt` est commité ; dire quoi faire des autres.

**Vérifié sans réserve** : `$0` dans `bash -c '…' "$F"` vaut le chemin du fichier ; `$$` et `$PATH` développés par le `bash` interne ;
PID gardé à travers `exec env … python` ; ligne finissant par `&&` suivie d'un saut de ligne valide ; formule de la minuterie
(`minuterie_restante_s` à 0 si le temps est écoulé, ce que la borne basse transforme en code 3 ; 36000 à 108000 s entre 0,90 et 0,30
USD/h) ; `datetime.fromisoformat` accepte « Z » (Python 3.13, `.venv`).

**Supposé** : comportement du vrai `vastai destroy instance` (aucune confirmation interactive, clé lue dans l'environnement du
processus détaché) ; survie sur plusieurs heures ; chemin réel de la machine.

**Verdicts** : commande v9 après corrections mineures (R-1, R-2, R-3 ; R-4 conseillée) ; minuterie v1, son essai et son journal **en
l'état** (essai rejoué : conforme, 0 écart) ; essai de survie **en l'état** ; pièce `pip` v2 **en l'état**.

**Bloquant pour la location : non.** R-1 à faire avant le feu (sans heure de création issue de `date -u`, la durée de la minuterie
serait fausse).
