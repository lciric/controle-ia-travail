# Consigne — seconde passe de corrections du code de T0.8 (après la vérification courte) — v1

Écrite le 2026-11-14T02:37:24Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A). Lot « compte 4 », tâche 3 (journal du compte 4, C4-0036 à C4-0038). **Aucune dépense, aucune instance, aucun téléchargement de modèle, aucune clé employée.**

## 0. Interdits et règles

La consigne `brouillons/t08-code-compte4-v1/consigne-developpeur-corrections-t08-v1.md` (`e2577b5a0a2e60a6108e4436660beb9d6e8967fd65056958ef9be48a4f7c778b`) s'applique **en entier pour son § 0** (interdits, exceptions, arbre `/home/user/t08-code-compte4-v1`, branche `prep/t08-code-compte4-v1`, poussée seule permise, garde des secrets, fin des messages de commit, aucun réseau, aucun fichier de `registres/`, de P3-bis ni de T0.7) et pour les « Règles de l'écriture » de son § 3 (corrections en place sous `src/controle_ia/t08/` et `tests/test_t08_*`, aucun essai d'autrui modifié, aucune garde affaiblie, aucun repli silencieux, aucun écart au texte : une ambiguïté s'écrit en question). Ses §§ 3 (liste), 4 et 5 sont remplacés par ceux-ci. Tête de départ : `7a4d4e130460d7c91420bf2b20a0ef59025659b3`.

## 1. Qui tu es

Développeur **neuf**, sous-agent de la session du compte 4, modèle A ; tu n'as écrit ni ce code, ni ses corrections, ni ses relectures, ni T0.8, T0.6, T0.7 ou P3-bis. Exclu ensuite de la vérification de ta passe et du verdict de T0.8.

## 2. À lire (vérifie chaque empreinte)

- Vérification courte : `/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/verification-courte-corrections-t08-v1.md`, `d12df4bd27f9620170321fe95369694b7e09f580223e08c6733daad448af9546` (en entier) ; son script `…-calcul.py`, `6fecd279e2a76423057bb0192784145e6704f217e6a818016059870a7dd9ca2a` (cas C1 à C4, mutations M35, M38, M61).
- Choix de la session : `/home/user/controle-ia-travail/registres-provisoires/compte-4-2026-11-14-v6.md`, section C4-0037 (compagnon).
- Rapport des corrections : `/home/user/t08-code-compte4-v1/docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-t08-v1.md`, `6b05409c2ccbbcc9a4654baa2aad2a0c67bbfa7bc0636099289700f75931bb84`.
- Texte qui fait foi, aux lignes citées : `/home/user/controle-ia-travail/brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` (le texte prime).

## 3. Ce que tu corriges (selon C4-0037)

- **VCT8-01** (majeur) : réserve « la troncature du raisonnement diffère entre conditions » décidée sur la part des balises imposées **après troncature** (lettre, l. 229) ; écarts sur la somme et sur les balises après fin de réponse écrits à côté, sans effet ; essais : cas sain et artefact au bord de 10 points sur la grandeur de la lettre, et les deux cas C3 du script du vérificateur.
- **VCT8-02** : comparateur de `essai_jouet_v1.py` : pour `lecture-t08.json`, `resultat` comparé hors la seule clé `tables_D_F_fichier.sha256`, égalité exigée de `chemin` et `contenu_sha256`, et, dans **chaque** racine, l'empreinte citée égale à celle du fichier des tables sur disque ; exclusion déclarée dans la sortie du comparateur ; en-tête corrigé ; essai du comparateur (cas sain ; artefact : contenu des tables changé dans une racine ; empreinte citée fausse).
- **VCT8-03** : en lecture réelle, la ligne `CODE-T08` doit citer le commit du marqueur `COMMIT_CODE_T08` (40 caractères, dans l'une de ses cellules) et la ligne `SCELLEMENT-T08` l'empreinte du texte passé en `prereg` ; leur antériorité est exigée sur la date de création du manifeste de la course (en plus de `COURSE-T08`) ; une fonction publique de **passage à blanc** des contrôles du texte réel et du registre (ceux qui ne demandent aucune sortie de la course), que la session mère appelle avant de lancer la course, documentée ; la forme des lignes reste une question à la mère (déclarée). Essais : cas sain ; artefacts : `CODE-T08` qui cite un autre commit ; `SCELLEMENT-T08` d'une autre empreinte ; ligne postérieure au début de la course.
- **VCT8-04** : limite déclarée dans la docstring de `exiger_marqueurs_au_texte` et dans ton rapport ; pas de changement de code.
- **VCT8-05** : (a) tout état du registre du texte de validité autre que « présent » rend « non lue (<motif>) », compté ; (b) attribut `formes_mesures_7b` absent : arrêt ; essais.
- **VCT8-06** : un artefact par appel : manifeste de 7b d'un autre run passé à la course réelle jusqu'au contrôle ; première action d'étalonnage égale à celle de H dans la course jouet ; aire à 0,39 et à 0,61 pour `hors_bornes` (et 0,40 et 0,60 aux bords).
- **VCT8-07** : `fichiers_ouverts` sans répétition (ordre de première ouverture) ; nombres justes dans ton rapport.

## 4. Essais

Comme au § 4 de la consigne des corrections : tous les `tests/test_t08_*_v1.py` verts ; les cinq essais d'inventaire (éléments « autres » inchangés ; tout élément neuf de T0.8 déclaré) ; aucun module hors de `t08/` n'importe `controle_ia.t08`. **Essai de bout en bout deux fois** sous `essai/t08-jouet-compte4-v3/a` puis `…/b` (racines neuves dans l'arbre ; même entropie et même horodatage relevés par la machine) : le comparateur corrigé doit rendre **0 différent** ; consigne les nombres. Rien n'est écrit sous `essai/t08-jouet-compte4-v1/` ni `…-v2/`.

## 5. Ce que tu rends

Commits et poussées à chaque jalon (un redémarrage du conteneur peut survenir). Rapport `docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-2-t08-v1.md` dans l'arbre, scellé, committé et poussé **en dernier** : la tête finale de la branche est le commit que citera le texte candidat (`docs/` est hors des chemins gelés). Sections : **0. Identité** ; **1. Constats traités** (VCT8-01 à VCT8-07 : fichier:ligne, essai sain et artefact) ; **2. Fichiers changés** et sha256 ; **3. Essais** ; **4. Essai de bout en bout** ; **5. Questions** ; **6. Limites**. Dernier message à la session : commit final (tête de la branche), chemin et empreinte du rapport, nombres d'essais, questions ouvertes. Rien d'autre.
