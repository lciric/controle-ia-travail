# Demande au successeur : le second PDF fusionné (dossier d'entretien v2) — v1

De : session mère précédente `session_01QPDgKgACWyCkCN8HjqwNXy`. Mot de Lazar, verbatim : « tu m'as donne les deux odf fusionnés ? sinon demande au successeur de le faire ».

**État.** Le PDF fusionné **v1** existe : 124 pages, empreinte `88a5802091a01b6d006e326924cc4f6c55d57f771a52d3bf8b284e5b96fd224d`. Il a été fait par la session-dépôt, sur sa branche `claude/upbeat-cray-dmauvv` (commit `253f9f4a`), au chemin `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/dossier-entretien-fusionne-v1.pdf`, avec le manifeste `…-parties.json`. Il a été remis à Lazar le 10 novembre. Il **n'est pas encore sur `main`**. Le **v2** n'existe pas : il attendait les sections de résultats v2, interrompues par le quota.

**À faire, dans l'ordre.**
1. Verse le v1 sur `main`, au même chemin, avec son manifeste et leurs compagnons. Prends seulement ces quatre fichiers (`git show` par chemin, après un fetch à refspec explicite) ; rien d'autre de cette branche, rien de la quarantaine. Vérifie l'empreinte.
2. Fais écrire par un agent neuf les sections de résultats **v3** (`docs/notes/rapports-directeur/resultats-pour-documents-v3/`). Contenu : celui de la consigne v2 (R-2179 ; brief, section 5, point 11), plus les rendus de l'état de l'art arrivés depuis (R-2180 à R-2190) et les décisions de Lazar prises entre-temps. Aucun taux de calibration (R-2185). Ensuite : contre-lecture par un autre modèle, puis scellement.
3. Produis **`dossier-entretien-fusionne-v2.pdf`** dans le même dossier, le v1 restant intact (R12) : même page de garde, même table des parties avec les empreintes, mêmes parties, avec trois changements :
   - les sections de résultats v3 à la place des v1 ;
   - le socle de preuves v3 (`b9377f1d…`) en annexe, une fois contre-lu ;
   - les versions les plus récentes des documents du bras d'attaque et de la session-dépôt, que la session-dépôt ou Lazar te désignent par chemin et empreinte (cloison : tu n'ouvres pas la branche du bras).

   Pages copiées sans retouche, chaque partie vérifiée contre son compagnon. Écris un manifeste `…-v2-parties.json`, scelle le tout et pousse sur `main`.
4. Envoie les deux PDF à Lazar, avec le nombre de pages et les empreintes. La version intégrée (un seul texte) reste à faire ensuite avec la session-dépôt ou son successeur.
