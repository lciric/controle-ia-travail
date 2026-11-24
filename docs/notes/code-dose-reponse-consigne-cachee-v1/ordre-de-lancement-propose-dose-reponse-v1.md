# Ordre de lancement proposé — course de dose–réponse de l'organisme à consigne cachée — v1

Pièce de classe C (proposition du développeur), jouée par la mère seulement. Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (2263c5c4…). Ligne de GO : `GO-2026-11-24-25` (calcul, 90 USD, échéance 15 décembre 2026). Bornes : une A100 SXM4 80 Go, au plus 1,30 USD de l'heure, 16 cœurs, 128 000 Mo de mémoire vive, disque d'au moins 300 Go, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go. Dépôt : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` (jamais `lciric/controle-ia`).

## 0. Préalables (aucune création sans eux)

1. Code contre-lu et vérifié (classe B) ; ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` inscrite par la mère au registre `registres/scellements-v1.md` (commit du code `C`, empreintes, déclarations « aucune génération sous texte privé » du développeur, de la session de lancement et de la mère).
2. Banque de 64 tâches livrée et scellée ; ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` inscrite, qui cite l'empreinte de la banque.
3. Texte de désignation de la course pour le critère 3 : s'il est scellé et exige des lignes préalables, les nommer dans la clé `designation_critere_3` de la configuration (chemin, empreinte, `lignes_registre`) ; sinon `null` (ses lectures de sondes restent descriptives).
4. Nœud ouvert : « deux contrôles croisés de plus » (ligne GO-2026-11-24-24) contre les quinze conditions du texte scellé ; le code joue les quinze.

## 1. Branche de lancement (session de la mère)

À partir de `main` à jour (code `C` intégré, lignes du registre inscrites) :

```bash
git checkout -b lancement/dose-reponse-v1 origin/main
PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v1.py <chemin de la banque scellée> <C>
git add -f <banque> <banque>.sha256 prereg/T0.6-dose-reponse-configuration-course-v1.json*
git commit -m "Lancement de la course de dose-réponse : configuration et banque"
git push -u origin lancement/dose-reponse-v1
```

Le code du commit de lancement `L` doit égaler celui de `C` (le lanceur et l'amorce le vérifient : `git diff --quiet C L -- src scripts tests .claude pyproject.toml requirements-*.txt`). Si la pièce jointe est rangée ailleurs que `brouillons/g0-criteres-2-3-v1/`, passer son chemin en troisième argument de `configuration()` (même empreinte exigée).

## 2. Contrôles, puis création imprimée

```bash
export GO_ID=GO-2026-11-24-25
DR_BRANCHE_LANCEMENT=lancement/dose-reponse-v1 DR_AMORCE_SHA256=<empreinte de scripts/amorce_instance_dose_reponse_v1.sh au commit C> \
DR_ESSAIS=8 bash scripts/lancer_dose_reponse_v1.sh controles <dossier neuf du bloc-notes>
bash scripts/lancer_dose_reponse_v1.sh creation auto course <dépense antérieure relevée au registre des dépenses, 0 à la première tentative> <même dossier>
```

`creation` imprime la commande littérale de création (revérifiée par la garde de calcul, `GO_ID` en tête) ; la mère la joue telle quelle. `DR_ESSAIS=8` : un lot d'essais de chaîne, condition honnête seule, tâches de la banque initiale, hors mesure (débit, mémoire, écriture, garde d'équivalence) ; `0` pour s'en passer.

## 3. Surveillance

```bash
bash scripts/lancer_dose_reponse_v1.sh surveillance <identifiant> <même dossier>
```

Arrêt par l'identifiant (R10) sur processus mort ou dépense cumulée ≥ 90 USD ; alerte unique à 72 USD ; deux heures sans ligne de progression : alerte sans arrêt. L'instance porte la même garde (minuterie : à l'heure d'épuisement du plafond restant, consignation, poussée, destruction). Les lignes de progression ne portent que des comptes d'épisodes.

## 4. Reprise après une erreur de chaîne

Instance neuve, branche de sortie neuve, avec `DR_BRANCHE=calcul/dose-reponse-v1-reprise-1 DR_REPRISE_BRANCHE=<branche de la tentative> DR_REPRISE_RUN=<run de la tentative>` aux contrôles ; dépense antérieure cumulée. Les blocs poussés sont recopiés à l'octet, ceux d'un bloc commencé non poussé sont déclarés par épisode et rejoués avec leurs graines.

## 5. Après la course

Vérifier que les 64 blocs (1 920 épisodes) sont sur la branche de sortie, sceaux conformes, puis jouer la lecture **une seule fois**, sur processeur :

```bash
PYTHONPATH=src python -m controle_ia.dose_reponse.lecture_v1 --run-id <AAAAMMJJ-HHMMSS>-dose-reponse-lecture \
  --dossier donnees/<run> --resultat-course diag/<run>/episodes-dose-reponse.json --prereg prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md
```

Puis verdict (R13) par un sous-agent neuf sur `diag/<run lecture>/lecture-cout-dose-reponse.json`, scellé, soumis à Lazar.
