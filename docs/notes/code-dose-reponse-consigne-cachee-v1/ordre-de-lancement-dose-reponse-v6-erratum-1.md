# Erratum 1 à l'ordre de lancement v6 — course de dose–réponse de l'organisme à consigne cachée

> Pièce de classe A (erratum matériel minimal à `docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-dose-reponse-v6-scelle.md`, empreinte `08cb2b355c595254750819db4d7fdf0bf9b46593abf2f77ed5fd1e62bfaf68cc`, qui reste intacte sous R12). Scellée par la session mère Antigravity (`cd7c89b9-9752-4dac-b846-2c58efd89737`, Gemini 4 Neon) le `2026-11-25T08:27:21Z`.

## Objet (seuls changements autorisés par Lazar)

1. **Borne de stockage (`GO-2026-11-25-01`, `R-5397`)** : `offre.stockage_max_usd_h` passe de `0,08` à **`0,10` USD de l'heure** (tarif standard Vast.ai `0,20 USD/Go/mois = 0,0822 USD/h` sur 300 Go). Toutes les autres bornes restent strictement inchangées : une `A100 SXM4 80 Go`, carte ≤ `1,30 USD/h`, 16 cœurs, 128 000 Mo de mémoire vive, disque ≥ `300 Go`, téléchargement ≤ `0,05 USD/Go`, plafond cumulé **`90 USD`** (`GO-2026-11-24-25`), alerte unique à `72 USD`, dernier jour de création `2026-12-12`.
2. **Code versionné R12 (`CODE-DOSE-REPONSE-CONSIGNE-CACHEE` v3)** : commit `0d5d40f38f150bd9ede066407c24ecc89bfb4614` (descendant direct de `6b2b821a28f8bebebae2188d9f020ce731464306` ; les quatre lignes de `DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3` et `CODE-MOTS-ET-COUT-T06` restent 100 % intactes) :
   - pièce de registre : `registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-0d5d40f38f150bd9ede066407c24ecc89bfb4614-v3.json` (`f16fb4d3d53947f93dd25e0c796e2249d3e945b0b31fc26b1887444cb72d184a`) ;
   - contre-lecture classe B (Gemini 4 Neon neuf, verdict **`prêt`**, 0 bloquant, 0 majeur) : `docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md` (`3996369500acdf6d6d17814a33e947fd99819e3d267eff64230882293a496c1b`) ;
   - amorce v4 : `scripts/amorce_instance_dose_reponse_v4.sh` (`ac546976ee5507567e995504fd775af90ac010b2c8a2e65854aaeba6b51ddf82`) ;
   - lanceur v4 : `scripts/lancer_dose_reponse_v4.sh` (`5b73bf876d246a3af5593709e5e9f9e40a632b5fc42823dbd07a83ecc9bb9ade`) ;
   - configuration v2 : `prereg/T0.6-dose-reponse-configuration-course-v2.json`, écrite par `scripts/ecrire_configuration_dose_reponse_v3.py` (`47c83d993a81ccb089feb675bf73817ccb6bf073a04f35aa041554cbb348cd95`) ;
   - branche de lancement neuve (R12) : `lancement/dose-reponse-v2`, tirée du commit `0d5d40f38f150bd9ede066407c24ecc89bfb4614` ;
   - lecture hors ligne inchangée (`controle_ia.dose_reponse.lecture_v2`) ; lecteur du texte inchangé (`scripts/lancer_lecteur_texte_dose_reponse_v2.sh`).
3. **Session de lancement et jeton GitHub (`GO-2026-11-25-02`, `R-5399`)** :
   - déclaration de session de lancement v2 : `registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v2.json` (session mère Antigravity `cd7c89b9-9752-4dac-b846-2c58efd89737`) ;
   - jeton GitHub transmis à l'instance Vast.ai (masqué, jamais affiché) : jeton `gh` du trousseau local autorisé par `GO-2026-11-25-02`, avec obligation de révocation immédiate après versement prouvé de la course (rappel inscrit dans `registres/rappels.md`).
4. **Rien d'autre ne change** par rapport à `ordre-de-lancement-dose-reponse-v6-scelle.md` (`08cb2b35…`).
