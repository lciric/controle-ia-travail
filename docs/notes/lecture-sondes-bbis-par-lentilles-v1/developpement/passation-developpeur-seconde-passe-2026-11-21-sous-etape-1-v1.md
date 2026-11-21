# Passation courte du développeur de la seconde passe — sous-étape 1 close (statistiques) — v1

2026-11-21 (UTC), branche `claude/brave-galileo-jhp684`. Mandat `4a3cf535…` ; première note `notes-developpement-seconde-passe-v1.md` (`a06575bf…`).

## Fait
- `src/controle_ia/lentilles_sondes_bbis/statistiques_v4.py` (`32fa859a5e3009f63c79851f39cefc6915b5ac0b0d76fbf2e5ebe30ac689cdfa`) : statistique corrigée reprise par appel
  (`statistiques_v2`, `statistiques_v3.p_concentration`) ; règle de départage (valeur décroissante, puis identifiant de jeton
  croissant ; pôles : cosinus, indice de neurone, signe + avant −) ; aucune garde d'égalité ; comptes d'égalités (`ComptesEgalites`) ;
  `ResumeNul.rangs_premiers` (vingt premiers des directions nulles, pour les p de recouvrement).
- `tests/test_lentilles_sondes_bbis_seconde_passe_statistiques_v1.py` (`50cb99423694dc3993221a281d1f438c3911f171b38edd116fc71d38f54a3f27`) : 39 essais, verts (`39 passed`), graines
  `lentilles-bbis-v2/essai/<garde>`. Essai des essais (`outils/essai-des-essais-seconde-passe-statistiques-v1.py`, copie isolée du
  paquet) : dix altérations, dix vues (une première passe en avait laissé une non vue : un essai a été ajouté).
- Environnement des essais, hors du dépôt : torch 2.14.1+cpu, numpy 2.5.3, scipy 1.17.1, transformers 5.18.0, tokenizers 0.23.2,
  safetensors 0.8.0, huggingface_hub 1.33.0, pytest 9.1.1 ; registre public de paquets, coût nul.

## Lu du texte v2 à ce point
« Code neuf », « Vocabulaire » à « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Qui »,
« Frontière », « Données gardées », « Lignes de registre » (lignes 1026 à 2635, sans les lignes 1320 à 1343). **Non lus encore** :
les lignes 1 à 1025 (différences des brouillons, traitement des contre-lectures, en-tête de la v1, « Ce que l'auteur savait ») et
2636 à 3000 (« Nœuds », « Contre-lecture », changements). Écart à l'ordre de lecture du mandat, déclaré : j'ai codé la sous-étape 1
(que « Métrique », points 6 et 7, fixe entièrement) avant de finir la lecture, pour qu'un commit existe tôt.

## Précisions de lecture prises (à contre-lire ; aucune n'ajoute une règle de décision)
1. Compte d'égalités « par (couche, lentille, nul) » : la liste par score d'une direction lue ne dépend d'aucun nul ; elle est
   comptée sous la case « liste par score », la liste par z sous le nom de son nul.
2. La part d'une direction nulle est tenue par son compte entier, comme en `statistiques_v3`.

## Reste
Sous-étapes 2 à 7 de la première note. **Prochaine sous-étape exacte** : sous-étape 2, `nos_lentilles_v1` (fiche de rangement,
condition de lecture, lignes de registre de la v2, place de la ligne de l'addendum, issue des nœuds N12 et N17, archive de
`torch.save`), après lecture de « Nœuds » et des différences des brouillons 6, 5 et 4.

## Expositions, instances
Aucun intitulé interdit vu. Aucune machine, aucune dépense, aucun téléchargement de modèle, de lentille ni de corpus ; aucune clé lue.
