# Course d'idéation de l'organisme — devis v5 (v4 + la contre-lecture CL2 de la v34)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` **20:24 UTC**. **Remplace le devis v4**
(gardé, R12) sur les points ci-dessous ; tout le reste des v2 à v4 vaut. Code : **v35** (312 essais, non contre-lue :
relecture ciblée v34 → v35 par un modèle ≠ Fable chez session-depot, condition 1 du GO). Rien n'est dépensé ici.

1. **Plafonds** (CL34-07) : total **côté Claude 17 USD** au noyau (`--budget-total-usd 17`, défaut) et au relais
   (`--plafond-usd 17 --reserve-par-appel 3.5`) ; les appels de contrôle sont comptés dans ces 17 ; Argon **≤ 3 USD**,
   tenu par sa commande et par le plafond de session `juge_ideation|gemini-argon=3`, compté par le bras différé contre le
   total de la course. Attendu : ≈ 7 à 14 USD, Argon compris.
2. **Argon (bras rapporté) : jamais pendant la course.** La course reçoit `--juge-externe argon=gemini-argon` **sans**
   `--commande-juge-externe` ni `--attestation-lecture-humaine` (refusés) : elle écrit sa consigne en attente, scellée.
   La clé d'Argon et sa commande n'existent qu'à l'étape du bras différé, sous un fichier en mode 600 lisible des seuls
   opérateur et commande, son chemin passé par `variables_transmises` (jamais un nom de clé) ; la commande reçoit un
   environnement minimal explicite ; elle imprime **toujours** `cout_usd` et sort ≠ 0 sur tout échec.
3. **Attestation** (CL34-04), écrite par le lecteur nommé du devis v4 point 1, scellée :
   `{"lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256": {"argon": …}}` — il a lu les réponses
   brutes, la quarantaine, **toutes** les fiches validées **et la consigne en attente d'Argon** (ce qui sort du périmètre :
   question, pièces des juges, fiches, témoins). Le bras se joue une seule fois ; il fait son propre appel de contrôle, relit
   les témoins (`noyau/temoins-servis.json`) et écrit son manifeste sur tous les chemins.
4. **Témoins du tiers** (CL34-12) : **noms neutres** (jamais « verbeux », « occupé », « jumeau », « sobre » ni ceux de
   l'exemple), longueurs dans la fourchette attendue des fiches (≈ 1 500 à 3 500 caractères de vue servie) ; l'**injecteur**
   (fiche qui demande au juge « 3 partout » ou se note elle-même) est classé `faux_falsifiabilite`, attendu inéligible,
   `note_max` falsifiabilité 1 ; le fichier porte toujours les quatre classes. La lecture rapporte la longueur des témoins
   contre celle des fiches (`longueur_temoins_contre_fiches`) : un témoin hors fourchette rend L0 suspect (R4).
5. **Machine** (CL34-05, CL34-06) : `SORTIE` neuve sous le dossier personnel de l'opérateur, `--racine-depot` donné
   explicitement (ou `git rev-parse` vérifié au manifeste : `versions.racine_depot`), `--delai-session-s 1800` (défaut),
   kit d'agent 0.2.174, outil en ligne de commande dont la version est lue au manifeste.
6. **Pièces** (CL34-14) : les 17 de `liste-blanche-sans-temoins-v1.json` sont dans le lot
   `livrables/lot-ideation-tournoi-v35-v1.zip`, dont les deux antériorités manquantes ; vérifier les 17 empreintes avant
   `--construire-liste-blanche` (18 fichiers avec les témoins).
7. **Ordre** : relecture v34 → v35 → pièces vérifiées → témoins du tiers scellés → liste blanche scellée et lue → machine,
   clé Anthropic tournée, relais sous `env -i` → GO cité dans `registres/go.md` → course (codes 0 lisible, 4 témoins
   échoués, 2 arrêt) → lecture humaine → attestation → bras différé d'Argon → versement scellé de `SORTIE`,
   `SORTIE-controle` et du bras → contre-lecture → décision de Lazar sur l'ordre des questions (aucune lecture ne tranche).
