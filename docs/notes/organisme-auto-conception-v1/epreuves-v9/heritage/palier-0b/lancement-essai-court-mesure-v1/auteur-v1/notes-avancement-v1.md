# Notes d'avancement — auteur du lanceur et du gardien, palier 0b, essai court (au fil de l'eau)

- Mandat lu (sha256 32580fd6…d84 vérifiée). Complément 1 v3 extrait par `git show origin/main:… >` : `complement-1-v3.md`, sha256 1484cd75…7268 vérifiée.
- Programme extrait (lecture seule, pour les noms de fichiers) au commit 8262c442 : `lecture-programme-lancer_etapes_3_5_6_v2.py`, sha256 1f04cb46…db14 (égale à l'empreinte attendue).
- Noms lus dans le programme : `etape-N/manifeste.json` et compagnon `etape-N/manifeste.json.sha256` (tirages.ecrire_manifeste → _sceller) ; arrêt nommé : `etape-N/arret.txt` ; étape 4 sous `etape-4/couche-mecanique/`.
- Commande du lanceur vérifiée par `verifier-commande-v1.py` : ÉGAL à l'octet sauf le dernier argument (tête 619 octets, sha256 a0dc38a4…bd59 des deux côtés).
- Racine factice : `essais/racine-factice`, tête 702a6edd13d70a4fd9a2cb666f7b8c4c44d0a28b, programme factice sha256 259cef4c…ad8c.
- Essais de refus du vrai lanceur (mode vérification seule), 16:23:45Z : v0 sain 0 ; v1 sorties existantes 10 ; v2 tête fausse 11 ; v2b racine sans dépôt 11 ; v3 fichier suivi modifié 12 ; v3b non suivi seul 0 ; v4 empreinte fausse 13 ; v4b programme absent 13 ; v5 usage 2 ; v6 code déjà présent 4 (non écrasé) ; v7 tenue absente 3 ; dossier des sorties neuf jamais créé. Échecs : 0. Détail : `essais/refus/*/erreur.txt`.
- Projection sur valeurs connues (`essais/essai-projection-v1.py`) : A, B, C égales au calcul à la main ; D (n = 1), E (n = 0) impossibles. Échecs 0.
- Scénarios (intervalle 1 s ; tout sous `essais/scenarios/<nom>/tenue/`) :
  - s1 sain place (seuil 1 o) : pas d'arrêt, code 0, inventaires 3 et 4 écrits, gardien fini sur « programme absent ».
  - s2 artefact place (seuil 1e18 o) : arrêt de place au 1er tour, signal de fin au groupe 18540, absent en 1 s, code 143.
  - s3 sain mesure-n (seuil 13, programme finit à n = 12) : pas d'arrêt, code 0.
  - s4 artefact mesure-n : arrêt à n = 13 ; mesure : Δt = 6.007583 s, ×648/12 = 324.4 s ; s4 = 1 404 928 o alloués ×54 = 75 866 112 o ; apparents 1 373 728 ×54 = 74 181 312 o (vérifiés à la main ; 1 373 728 = 13 × 100 000 + 18 dossiers × 4096).
  - s5 sain mesure-durée (30 s, étape 4 ≈ 10 s) : pas d'arrêt, code 0.
  - s6 artefact mesure-durée (5 s) : arrêt à 6.0 s, n = 6 ; Δt 5.998525 × 129.6 = 777.4 s ; 69 632 × 129.6 = 9 024 307 o (à la main : 6×4096 + 11 dossiers ×4096 = 69 632).
  - s8 artefact mesure n = 1 : « projection impossible (n = 1 < 2) », arrêt fait.
  - s7 arrêt forcé (programme ignore le signal de fin, délai d'emploi 60 s) : en cours.
- Plan : lanceur (mode emploi + mode vérification seule à paramètres factices), départ détaché, gardien Python, départ du gardien, programme factice, lanceur factice fabriqué par programme depuis le vrai lanceur, essais.
