# Décision de routine — inventaire par instantané v4 utilisé avec trois réserves mineures (2026-11-19, vers 11:50Z)

**Vérification R2 de la v4** (pièces du commit `454a70a1`) : « écarts », aucun bloquant ni moyen. Les six corrections de
la v4 sont en place et justes. Banc de bout en bout : état réel de cloud-init, poussée face à une tête qui avance, refus
R12, disque d'un autre poste, clés absentes, git cassé. Le chercheur de fuites ne trouve aucun fragment en clair, sauf
m3. Constructeur : trois cas sains et une vingtaine d'artefacts refusés.

**Réserves acceptées** (décision de routine de la session, sous l'autonomie accordée par Lazar vers 09:44Z) :
- **m1** : la marque de refus n'est poussée qu'une fois et peut se perdre si la tête avance. Les trois serveurs sont
  lancés l'un après l'autre, et aucun poste ne pousse plus sur la branche (tous éteints). Une marque absente se voit
  d'ailleurs à l'échéance d'attente.
- **m2** : la marque de refus n'a pas de compagnon (R6). Si elle apparaît, la session la scelle elle-même.
- **m3** : un lien dur vers un secret non répertorié serait empreinté (empreinte sha256 publiée, contenu jamais versé).
  Aucun lien de ce genre n'est attendu sur ces postes, et l'empreinte d'une clé aléatoire de 37 à 64 caractères ne se
  renverse pas.
- **r1** (résiduel faible) : une ligne de clé privée encodée deux fois en URL passerait dans un journal. Aucune source
  ne produit cette forme.
- **Cosmétiques** : trace Python si la table manque ; espace finale dans `instances_cloud_init` ; aide de `git diff`
  dans `git-etat.txt` sur un dépôt cassé.

**Exécution** : un poste à la fois (v14, puis inventaire v1, puis inventaire v2). Pour chacun : construction, création,
attente de la marque, vérification (champs, compagnons, comptes), puis seulement destructions par identifiant, avec
preuve d'absence. Les instantanés restent protégés.
