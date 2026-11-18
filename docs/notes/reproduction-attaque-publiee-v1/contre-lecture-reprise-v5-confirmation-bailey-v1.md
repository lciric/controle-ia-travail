# Contre-lecture (R2) des pièces de reprise v5 de la confirmation de Bailey — v1

Workflow `contre-lecture-reprise-v5-bailey`, run `wf_6bf25734-f03`, un contre-lecteur neuf, branche au commit `8861a5a3`.
Traitement : verdict « scellable », trois remarques sans changement des pièces : scellement fait avant tout lancement ;
le poste v5 n'est lancé qu'après un relevé, en lecture seule et consigné, montrant de nouveau une offre sur la machine 146915 ;
la l. 15 de l'en-tête (historique v3) vise `sortie-conduite-v11`, la v5 écrit `sortie-conduite-v15/reprise-v10-2` (l. 4).

## Verdict : scellable

Verdict : scellable, sans bloquant ni point à corriger. J'ai lu la branche à 8861a5a3.

(1) Seuls les noms changent. J'ai relancé le générateur v3 dans /tmp sur la v4 extraite de la branche, dont les compagnons .sha256 donnent OK : il rend les deux pièces v5 à l'octet. Le diff v4 → v5 ne contient que trois lignes d'en-tête et les noms : journal, PID, sorties, marque de fin, état, compagnon du script, nom et étiquette du serveur. Aucun nom neuf n'existe sur la branche : reprise-v5.*, poste-fini-reprise-v5.json, poste-hetzner-reprise-v5-etat.txt, les compagnons v5, sortie-conduite-v15/reprise-v10-2 et repertoires-sortie-conduite-v15--reprise-v10-2-v1.txt. Le seul reprise-v10-2 présent est sous sortie-conduite-v11, hors du chemin.

(2) La v5 peut tourner après la v4 qui a échoué.
- Du bilan v4, je n'ai lu que les champs demandés : statut exited, une seule alerte « redémarrage refusé (GardeArret) », redemarrage d'environ 18 s, detruite faux.
- La garde AVANT, rejouée en bash, vaut « reprise-v10 ». Ce dossier est donc écarté et seul reprise-v10-2 est listé.
- Reprise.reprendre (lanceur_v21.py, vers la ligne 2348) choisit reprise-v10-2 puisque reprise-v10 existe.
- _veilleurs_precedents lit le PID du veilleur v4 dans le bilan de reprise-v10. Sur une machine neuve, identite_veilleur_arret (ligne 1056) exige « veilleur-arret » et « --journal » suivi du chemin absolu de reprise-v10 : elle rend faux et ne signale rien (R10 tenu). Le veilleur de la v5, dont le journal est dans reprise-v10-2, n'est jamais pris pour lui.
- Les battements ne sont pas sur git (*.battement exclu).
- Simulation jouée avec les substituts des essais du code a904aa39 : une première reprise au redémarrage refusé (GardeArret) rend exactement l'alerte unique du vrai bilan v4 et une remise à l'arrêt acceptée. Une seconde reprise, avec l'identité réelle, écrit reprise-v10-2, laisse le PID précédent non signalé, redémarre, transfère et détruit l'instance 77 par son identifiant. Le bilan de reprise-v10 reste vérifiable.
- 223 essais de test_temoin_bailey_condition6_v21.py passent, 3 sont sautés.
- La marque poste-fini-reprise-v4.json n'est lue par aucune garde de la v5 : rien ne bloque.

(3) Aucune voie de dépense hors GO-2026-11-17-07 ni de destruction hors R10.
- Côté Vast, le poste ne fait que des lectures : show user et show instances.
- Il exige 61049303 seule, arrêtée et à l'étiquette attendue, un crédit positif sans échec de facturation, la conduite v15 finie, le commit a904aa39 avec src/ identique à la tête, et l'empreinte du script.
- Le seul appel qui dépense est `reprendre` sous GO-2026-11-17-07. Sur origin/main, ce GO est de type calcul, à B = 85, d'échéance 2026-11-30. Le redémarrage est borné par B − marge (lu dans poste-v5.json) et par cette échéance.
- La destruction se fait par identifiant, seulement après un transfert complet aux empreintes égales.
- Le constructeur ne fait aucun appel réseau : il écrit un corps JSON de droits 600.

(4) `bash -n` passe sur la pièce et sur le script une fois les secrets remplacés. Avec des secrets factices (HOME dans /tmp), le constructeur rend le nom poste-temoin-bailey-reprise-v5 et l'étiquette temoin-bailey-reprise-v5, environ 10,8 kio de données de démarrage, sous la limite de 32 kio. Il n'imprime aucun secret, laisse 0 occurrence de reprise-v4, et donne le code 2 si une clé manque.

Cloisons tenues :
- aucune note de sonde ni de juge ;
- aucun appel à valider ni à lire ;
- je n'ai pas ouvert registres/etat.md.

Écarts :
- J'ai lu sur origin/main la seule ligne de GO-2026-11-17-07 dans registres/go.md, pour en vérifier l'échéance.
- Les essais ont eu besoin du fichier docs/notes/…/versions-figees-temoin-bailey-v1.json, extrait dans /tmp sans être lu.
- Une commande `git show` de poste-hetzner-reprise-v4-etat.txt et de poste-fini-reprise-v4.json a été refusée par le classifieur de permissions : je n'en ai donc lu que les noms (ls-tree), conformément aux cloisons.

Rien n'a été modifié dans le dépôt (`git status` propre) et /tmp a été nettoyé.

### 1. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v5.sh 86

**Constat.** Le compagnon poste-hetzner-reprise-v5.sh.sha256 n'existe pas encore : les pièces sont dites NON SCELLÉES. Lancé tel quel, le poste s'arrête sur « empreinte du script ou du manifeste différente » (code 3, sans dépense), et ses noms v5 seraient consommés pour rien (R12).

**Correction proposée.** Avant tout lancement, sceller les deux pièces et le générateur : python -m controle_ia.scellement sceller runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v5.sh runs/temoin-bailey-v1-20261111/construire-donnees-demarrage-reprise-v5.py docs/notes/reproduction-attaque-publiee-v1/generer-pieces-reprise-confirmation-bailey-v3.py, puis committer et pousser les compagnons sur la branche avant de construire les données de démarrage.

### 2. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v5.sh 103-123

**Constat.** Aucune garde ne vérifie que la carte de la machine 146915 est libre, alors que c'est la cause du refus de la v4. Lancée trop tôt, la v5 échouera de la même façon : code 3, aucune dépense Vast, instance remise à l'arrêt. Il faudrait alors une v6 et un nouveau poste Hetzner.

**Correction proposée.** Ne pas changer la pièce, qui doit rester « noms seuls ». Ne lancer le poste v5 qu'après avoir constaté depuis la session, en lecture seule, que l'offre de la machine 146915 est de nouveau disponible, et consigner ce relevé dans la passation.

### 3. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v5.sh 2-15

**Constat.** L'en-tête empile les historiques. La ligne 15 (v3 : « `reprendre` écrit dans `reprise-v10-2/` ») concerne sortie-conduite-v11, mais elle peut se lire comme le dossier visé par la v5, qui est sortie-conduite-v15/reprise-v10-2. C'est un commentaire seulement, sans effet sur le comportement.

**Correction proposée.** Aucune modification de la pièce. Préciser dans la note de traitement de cette contre-lecture que la ligne 15 vise sortie-conduite-v11 et que la v5 écrit sortie-conduite-v15/reprise-v10-2 (ligne 4).
