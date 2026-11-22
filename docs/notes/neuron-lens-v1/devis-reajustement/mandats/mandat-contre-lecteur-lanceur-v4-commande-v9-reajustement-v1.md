# Mandat du contre-lecteur neuf — lanceur v4 et commande v9 du réajustement de nos lentilles (variante B) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-22, sous GO-2026-11-22-05 ; contre-lecture du code par
un agent neuf sur Opus 5.5 (consigne de la mère). Tu n'es pas l'auteur. Français.

## Ce que tu juges
Le code et la commande écrits sous `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md`
(6ed54244…), dernier commit du développeur `cf38bf207`. Rendu du développeur : `docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/rendu-developpement-v4-v1.md` ;
table des items `developpement-v4/table-items-lanceur-v4-v1.md` (0b2552ed…) ; empreintes `developpement-v4/empreintes-lanceur-v4-v1.txt` (5092bf68…).
Question : **le lanceur v4, le module de rangement, l'amorce v5, le dépôt réduit v5 et la commande v9 font-ils exactement ce que le
devis v9 (§ 5, points 3, 4, 5 (a) à (m), 10) et le critère d'identité v8 (qui prime) exigent, sans rien changer d'autre à la course du
18, et peuvent-ils être donnés à la création une fois les préalables levés ?**

## Pièces (vérifie les empreintes)
L'ordre de lecture que donne le développeur : `CLAUDE.md`, le mandat, le devis v9 (§ 5), le critère v8 (§ 2, 4, 5, 7) ; le lanceur v4
contre `b_beta_lancer_v3.py`, `rangement_lentilles_v1.py` ; l'amorce v5 contre `scripts/amorce_neuron_lens_b_beta_v3.sh`, le dépôt
réduit v5 ; `tests/test_neuron_lens_b_beta_lancer_v4_v2.py`, `tests/test_neuron_lens_etapes_b_beta_v6.py`,
`tests/test_neuron_lens_montage_b_beta_v4.py`, le banc d'altérations et sa sortie ; les essais à blanc v3 (non conforme) et v4 et leurs
journaux ; `docs/notes/neuron-lens-v1/commande-b-beta-v9.md` contre `commande-b-beta-v8.md`. Les textes de la variante B scellés
(`textes-variante-b/statut-seconde-mesure-reajustement-v1.md`, 386c3e16… ; `plan-lecture-seconde-course-reajustement-v1.md`, 02ee9971…)
pour vérifier que la course produit ce que le plan lira. Les relevés de la plateforme `releves-plateforme-reajustement-v1.md` (5369bd99…).

## Points à trancher, chacun « tenu » ou « à corriger », avec raison et ligne
1. Chaque item (a) à (m) : fait, juste, éprouvé (cas sain et artefact, R5).
2. Champs du manifeste et pièces exigées par le critère v8 (§ 2, 4) : `versions` égal à celui du 18 hors `plateforme` ; `depot_propre` ;
   résultats d'ajustement et d'export ; fonctions de calcul et de contrôle au texte inchangé ; épinglages de la commande v8 gardés.
3. Clé : la clé gardée ne va jamais à la machine ; la clé restreinte, passée sous le nom `HF_TOKEN` sur la machine, est balayée avant
   chaque poussée (14 formes) ; aucune fuite dans journaux, manifestes, messages ; les deux valeurs vérifiées différentes sans impression.
4. Copies et relecture : copies au fil de l'eau, empreintes avant envoi, reprises bornées (au plus deux), inventaire poussé à chaque
   étape, table de destruction (ligne « relecture en échec : pas de destruction sans la mère »), perte acceptée d'avance seulement
   celle du devis ; relecture en flux par la session.
5. Gardes de dépense : plafond 62, arrêt dur 55,8, minuterie 20,4 h, compte rendu 37,2, prix exigé 2,62, borne basse 1,49, crédit < 1 USD ;
   leçon du 19 (veille qui réarme).
6. Les nœuds N-1 à N-4 du développeur et l'écart de noms (amorce v5, dépôt réduit v5, essai à blanc v4, essais `_v4_v2`) : acceptables ?
7. Les 214 échecs de `tests/test_neuron_lens_*.py` hors des fichiers touchés : sans lien avec le code neuf ? Le commit du 18 que la
   commande v9 (étape 14) fait récupérer : bien nommé ?
8. Tout autre écart bloquant.
Rejoue `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_neuron_lens_b_beta_lancer_v4_v2.py tests/test_neuron_lens_etapes_b_beta_v6.py tests/test_neuron_lens_montage_b_beta_v4.py`
(`.venv` du dépôt) ; comptes seulement.

## Cloisonnement
Rien ne se lance, ne se loue ni ne se dépense ; aucune requête au loueur ni à la plateforme ; aucune clé lue (noms seulement). Jamais
`diag/`, `runs/`, `docs/verdicts/`, branches `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*` ; rien de l'apprentissage des sondes sur la
tâche, de P3, P3-bis, T0.6, T0.7, de l'étape B, du bras d'attaque, du saboteur à budget, des fichiers « consigne-privee » ou
« conception-ii-b ». Le verdict du 18 n'est pas lu. Un refus d'outil n'est jamais rejoué, il est déclaré.

## Rendu
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/contre-lecture-lanceur-v4-commande-v9-v1.md`, scellé, non committé.
Dernier message : verdict « conforme » ou « à corriger » en une à trois lignes ; points 1 à 8 ; corrections demandées, bloquantes ou non ;
empreinte ; expositions.
