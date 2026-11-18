# Brief de lancement de la nouvelle session de la lecture par lentille neuronale (18 novembre 2026, v1 — à coller)

Écrit par la session mère `session_01XJ6Mgr8BN6UanALsQatc5E` sur le mot de Lazar (« quelle session ? écris la passation »). La session sortante, `session_01XJ6MgnoxfSYHdF6rpEqZ7w`, a demandé deux fois une remplaçante au contexte frais. Tout ce qui suit le trait est le message que Lazar colle en premier dans la nouvelle session, **ouverte sur le dépôt `lciric/controle-ia-travail`** (c'est ce qui charge la garde de calcul).

---

Tu es la nouvelle session de **la lecture par lentille neuronale** (« Neuron Lens ») du programme « contrôle boîte blanche des menaces diffuses » de Lazar, dans le dépôt privé `lciric/controle-ia-travail`. Tu remplaces `session_01XJ6MgnoxfSYHdF6rpEqZ7w`. La session mère est `session_01XJ6Mgr8BN6UanALsQatc5E` (inscrite au registre des décisions sous R-3103) : écris-lui dès ta reprise. Langue : français, tutoiement avec Lazar ; nomme chaque travail par ce qu'il est et ce qu'il fait, jamais par un sigle seul.

Dans l'ordre :
1. Lis le `CLAUDE.md`, puis `docs/procedures/orientation-sessions-v1.md`. Ne fouille pas le dépôt et ne lis pas les autres sessions : tout ce qu'il te faut est nommé ici.
2. Récupère la branche de la sortante, de façon ciblée (jamais de récupération complète, le disque est compté) : `git fetch --depth=1 origin +claude/tender-meitner-iyxt5i:refs/remotes/origin/claude/tender-meitner-iyxt5i` (sommet `a20df354`). Lis sa passation `docs/notes/neuron-lens-v1/passations/2026-11-18-0333.md` (empreinte `b4bcd128…`) : elle donne la liste exacte du travail.
3. Éprouve la garde de calcul chez toi (un cas sain, un artefact) et dis les deux codes de sortie à la mère.

**Ta tâche : le brouillon 2 du préenregistrement propre à la tranche de l'ajustement de nos lentilles**, sans aucune dépense.
- Base : le brouillon 1, `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1-brouillon1.md` (`af6d4788…`), et sa contre-lecture, `docs/notes/neuron-lens-v1/contre-lecture-texte-gele-tranche-b-beta-v1-brouillon1.md` (`4d52c0be…`) : « à corriger », 2 bloquantes, 6 majeures, 13 mineures. Corrige tout.
- **Commence par la bloquante 1** : le correctif « seuls les documents d'au moins 128 jetons » ferait déborder l'ajustement au-delà de la ligne 999 du corpus, là où le code publié tire les contextes qui mesurent la lentille (lignes 1 000 à 1 063). Les contextes qui jugent notre lentille ne doivent jamais entrer dans son ajustement. Ajoute une garde « identifiant commun aux deux corpus ».
- **Puis l'inventaire des réglages du modèle dans le code des auteurs** (cinq à huit scripts), à faire avant tout scellement. Leur code se lit dans une copie de lecture du dépôt `stdlogits/neuron-lens` au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` ; **il ne s'exécute jamais ici** (règle de Lazar R-2710).
- **Bloquante 2** : avec le lieu « aucun rangement », les lentilles disparaissent avec la machine. Toute vérification et tout audit doivent donc être joués sur la machine avant sa destruction, avec un verdict unique et une règle de sortie écrits. Si ce n'est pas possible, ne tranche pas : formule un nœud pour Lazar et remets-le à la mère.
- Chaque prédiction porte un « réfutée si » ; aucun repli silencieux (R5) ; les audits de symétrie (R4) couvrent aussi le cas défavorable.
- Fais contre-lire le brouillon 2 par un sous-agent neuf d'un autre modèle. **Tu ne scelles rien** tant que la contre-lecture ne dit pas « scellable » ; puis tu remets le texte à la mère. Vise deux versions solides, pas dix.

**Décisions de Lazar en vigueur** (registre des accords, GO-2026-11-18-02) : prix exigé 2,62 USD/h ; plafond de 75 USD avec une relance ; lieu « aucun rangement » ; périmètre entier, nos deux lentilles. Modifié par R-3151 : **Lazar garde l'ancienne clé de la plateforme de modèles** ; la passer à une machine exigera son mot explicite au moment de la commande. Devis final : `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md` (`41a4c1f6…`). Budget : 100 euros par jour pour tous les programmes ; fenêtre de la course du 19 au 25 novembre.

**Interdits** : aucune location, aucune création de machine, aucun appel payant ; aucune clé passée à une machine ; ne touche à aucune machine existante ; n'écris ni dans `registres/` ni sur la branche principale — propose tes lignes à la mère ; n'ouvre aucun résultat des travaux sous embargo du programme. Pousse sur la branche que ton harnais t'attribue et donne-en le nom et le sommet à la mère. Deux sous-agents à la fois au plus.

En fin de session : une passation scellée sous `docs/notes/neuron-lens-v1/passations/`, poussée, et un message à la mère avec son chemin et son empreinte. Commence par lui envoyer un verdict de reprise en trois lignes.
