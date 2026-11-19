# Incident — clé de l'instance versée sur la branche (2026-11-19, vers 10:05Z)

**Constat** (contre-lecture R2 du poste d'inventaire v1, rendue vers 10:00Z) : la passe 1 du poste d'inventaire v1
(commit `2a1c0ff9`, poussé vers 09:42Z sur `claude/compassionate-meitner-d4ryyk`, dépôt privé `lciric/controle-ia-travail`)
a versé `versement-instance-61170458-v1/fichiers/root/.vast_api_key`, 65 octets. Le filtre de noms de la v1 ne
connaissait pas « key », et son contrôle du contenu ne reconnaissait qu'une clé de valeur connue.

**Vérification, sans rien afficher** : l'empreinte git du fichier diffère de celle de la clé du compte Vast, avec ou sans
saut de ligne final. Ce n'est donc **pas la clé du compte**. C'est très probablement la clé restreinte que Vast place
dans chaque instance : elle ne vaut que pour cette instance (61170458) et meurt avec elle. Jusqu'à la destruction de
l'instance, attendue vers la fin de la course, quiconque lit le dépôt privé pourrait l'arrêter ou la détruire.

**Gestes.**
- Fichier retiré de la tête de la branche par `git rm` (ce commit). Il reste dans l'historique (`2a1c0ff9`).
- Contrôle renforcé, ne rendant que des noms, des 555 autres copies de la v1 hors environnement Python : un seul autre
  fichier signalé, `root/public/train_time_experiments/README.md`, un faux positif. C'est une consigne
  `export OPENAI_API_KEY=…` du dépôt public des auteurs, sans valeur.
- Le poste v1 est éteint depuis 09:48Z. Le poste v2 ne pousse aucune copie : seulement l'inventaire, les exclusions et
  l'index des empreintes. Ses copies restent sur son disque.

**Pour Lazar (nœud).** Purger l'historique demande une poussée forcée, donc son mot. À faire seulement après la fin des
postes qui poussent sur la branche. En attendant :
- ne pas fusionner cette branche dans `main` ;
- ne générer aucune copie publique ; le script d'expurgation doit retirer `runs/**/versement-instance-*/**`.

L'historique porte aussi environ 308 Mio de bibliothèques Python, versées par la même passe.
