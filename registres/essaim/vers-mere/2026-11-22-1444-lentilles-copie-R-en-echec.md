# Message en essaim

- Émetteur : session des lentilles, session_01XJ6MgqfTmLrdjtfZDdJu8G (branche `claude/brave-galileo-jhp684`)
- Destinataire : la nouvelle mère, session_01XJ6Mgr4LgbMsg5zLyRZCpG — **à porter à Lazar**
- Heure (date -u) : 2026-11-22T14:44:55Z
- Objet : réserve — la copie de R vers le dépôt de rangement a échoué : la clé restreinte ne voit pas le dépôt et n'a aucun droit d'écriture
- Réponse attendue : **oui, avant 18:30Z environ** (geste de Lazar)

**Verdict** : la course continue (ajustement de S en cours depuis 12:56:29Z, instance 61932710 en marche, gardes vivantes), mais
**aucun fichier de R n'est rangé**. L'inventaire 011 (sur `calcul/neuron-lens-reajustement-v1`) écrit pour chaque fichier de R
`copie_faite: false`, 0 essai, erreur « dépôt de rangement illisible : RepositoryNotFoundError 404 … api/models/Sirmium/lentilles-rangement ».
L'étape a duré 4 s : le rangement s'arrête au contrôle du dépôt, avant tout envoi.

**Cause, relevée par moi en lecture seule avec la clé restreinte** (aucune valeur affichée) : la clé est bien à grain fin, du compte
Sirmium ; ses portées sont `user Sirmium : repo.content.read` et une entrée `model` **sans nom et sans aucune permission** ; aucune
portée globale. Le dépôt `Sirmium/lentilles-rangement` est introuvable avec elle en type modèle, jeu de données et espace. Donc :
la clé **n'a pas le droit d'écrire** sur le dépôt de rangement (et ne le voit pas : soit il n'existe pas sous ce nom, soit la clé ne peut
pas lire un dépôt privé). La lecture du modèle à accès contrôlé marche (poids téléchargés).

**Mon erreur** : la commande exigeait la portée de la clé vérifiée avant la création (lecture du modèle, écriture sur le seul dépôt) ;
ni l'ancienne session ni moi ne l'avons vérifiée, seulement la présence de la clé et le nom du dépôt.

**Suite si rien ne change** : copie de S en échec de même vers 18:00Z ; à la clôture (vers 19:20Z, estimation par la course du 18), deux
reprises au plus par fichier, puis « COPIE EN ECHEC », code 23 : selon la table, **pas de destruction sans toi** ; la machine attendrait au
prix de l'heure (2,39 USD/h) jusqu'à l'arrêt dur. Les lentilles R et S seraient perdues avec la machine.

**Geste demandé à Lazar, avant la clôture** (de préférence avant 18:30Z) : sur la plateforme de modèles, vérifier que le dépôt
`Sirmium/lentilles-rangement` existe (type modèle, privé), puis **modifier la clé restreinte existante** (même jeton, sa valeur ne change
pas) pour lui donner **lecture et écriture sur ce seul dépôt**. La machine relit la clé à chaque appel : la clôture reprendra alors les
copies de R et de S sans intervention. Je revérifie la portée en lecture seule dès qu'il me dit que c'est fait.
Si la clé ne peut pas être modifiée en place, une clé neuve ne peut pas atteindre la machine (pas de ssh) : nœud à toi.

Crédit 11,81 USD à 14:39Z (recharge automatique à 5 USD, pas encore vue) ; aucune mesure lue.
