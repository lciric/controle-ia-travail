# Essai Lean D-1a, quatrième essai : vérification de la consigne du poste local v7 (v1)

- **Quoi** : vérification courte, par le même contre-lecteur, des corrections demandées dans
  `contre-lecture-consigne-v6-v1.md` (`2f87ff7a…2a95`). Classe B. Aucune dépense, aucune machine.
- **Qui** : Claude Fable 5.2, le 21 novembre 2026 vers 14:25 UTC (`date -u`). Rédacteur : Claude Opus 5.5.
- **Lu** : `consigne-poste-local-lean-d1a-v7.md` (`11be3c275b312d9dd19d70a96911147f03498202c26db76591ab7c0da1e80979`,
  égale à son compagnon) et `differentiel-consigne-v6-v7.diff` (`fd5298d2…93c5`, égal à son compagnon). Le différentiel
  régénéré à partir des deux consignes est identique au fichier versé : il dit donc tout ce qui a changé.

## 1. Verdict

**Prête après deux corrections d'une ligne (E1, E2).** Les quatre corrections C1 à C4 sont portées mot pour mot. Rien
d'autre que ce que l'en-tête annonce n'a changé. Deux des remarques reprises portent une erreur, et **l'erreur vient de
ma propre rédaction dans la contre-lecture**, que le rédacteur a suivie fidèlement : un contrôle du terminal qui peut
passer à tort, et une commande qui, lue à la lettre, afficherait des valeurs de clés.

## 2. Les quatre corrections obligatoires

| Correction | Où | Portée |
|---|---|---|
| C1, relevé du pas noyau | mandat 5 | oui, texte exact |
| C2, arrêt du pilote « apres » sans relance | mandat 5, les deux passages | oui, texte exact |
| C3, « jeton d'accès » | section « Messages », contenu | oui, texte exact |
| C4, rien supprimé ni écrasé | mandat 1 (clone et ligne neuve), mandat 6 (« chez le loueur ») | oui, texte exact |

## 3. Les remarques reprises

Vingt passages changés, tous annoncés dans l'en-tête de la v7. Dix-huit sont justes et sans danger pour le poste. J'ai
rejoué sur le commit `47c7faaf` la commande de contrôle du dossier (`git ls-tree --name-only … --
docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/`) : elle montre bien la procédure v12 et aucun des deux noms. La
phrase sur le registre des dépenses de la branche est exacte.

**E1, correction obligatoire : le contrôle du terminal par `uptime -s` peut passer à tort.** `uptime -s` donne l'heure
de démarrage de la machine virtuelle de WSL. Cette machine peut survivre à un arrêt d'Ubuntu (elle reste en vie un
moment après, ou tant qu'une autre distribution tourne). Ubuntu peut donc s'être arrêtée et relancée entre les deux
relevés sans que l'heure change : c'est justement l'incident à détecter. L'heure de démarrage du processus 1 d'Ubuntu,
elle, change à chaque relance. Raisonnement sur le fonctionnement de WSL, **non éprouvé ici** (pas de WSL dans ce
conteneur) ; la commande proposée est au moins aussi sûre dans tous les cas, et la procédure emploie déjà
`ps -o lstart`.

Remplacer :

```
    aucune préparation. Contrôle : l'heure de démarrage d'Ubuntu (`uptime -s`), relevée au début du mandat 2 puis juste
    avant L1, à deux minutes d'écart au moins, doit être la même aux deux relevés ;
```

par :

```
    aucune préparation. Contrôle : l'heure de démarrage du processus 1 d'Ubuntu (`ps -o lstart= -p 1`), relevée au début
    du mandat 2 puis juste avant L1, à deux minutes d'écart au moins, doit être la même aux deux relevés, à deux secondes
    près. `uptime -s` ne suffit pas : il donne le démarrage de la machine virtuelle de WSL, qui peut survivre à un arrêt
    d'Ubuntu ;
```

**E2, correction obligatoire : `env -u NOM` sans commande afficherait tout l'environnement.** Lancé seul, `env -u NOM`
imprime les variables restantes avec leurs valeurs, la clé du loueur comprise. « sans `env` ni `printenv` seuls » ne
l'exclut pas clairement.

Remplacer :

```
jamais des valeurs), puis `env -u NOM`, sans `env` ni `printenv` seuls.
```

par :

```
jamais des valeurs), puis chaque commande du harnais est lancée par `env -u NOM <commande>` ; jamais `env -u NOM` sans
commande à la suite, ni `env` ni `printenv` seuls : ils afficheraient les valeurs.
```

**E3, souhaitable dans la même passe (non bloquante seule).** « L1 l'attend » peut se lire comme une attente sans fin
si l'accusé de réception ne vient jamais, alors que le repli le prévoit au bout de 30 minutes.

Remplacer :

```
  réception ; L1 l'attend.
```

par :

```
  réception ; L1 attend l'accusé, ou le passage au repli écrit plus bas.
```

Sans gravité, noté seulement : le quatrième cas du repli (un message de la mère que la session ne peut pas suivre,
Lazar tape alors « armée » et l'empreinte) ne contourne pas la règle des refus. Un mot de Lazar tapé dans la session
est l'autorité de la v5, et le code compare toujours l'empreinte avant tout appel.

## 4. Rien d'autre n'a changé

Conforme. Le différentiel porte 20 passages modifiés hors de l'en-tête ; chacun correspond à une correction C1 à C4 ou
à une remarque nommée dans l'en-tête. Le code désigné, le commit, les empreintes, la dépense, les gardes de création et
de destruction, le mandat et les réserves de la v6 sont inchangés.

## 5. Recommandation sur l'adresse du poste (écart 2 du rapport du troisième essai)

**Recommandation : lue par la session, écrite dans la consigne comme un écart accepté d'avance ; Lazar reste libre de
la donner lui-même.** Confiance : moyenne à haute.

- **Pour la lecture par la session** : l'adresse qui compte est celle que le serveur verra quand Ubuntu ouvrira la
  connexion. La session la lit depuis Ubuntu, par le chemin même de cette connexion. Une adresse relevée par Lazar dans
  un navigateur sous Windows peut suivre un autre chemin, ou être une adresse IPv6 ; une faute de frappe ou une adresse
  d'un autre réseau arrête l'essai à la mesure des adresses (code 1, aucune préparation). Le troisième essai l'a fait
  ainsi, sur le mot de Lazar (« Lis-la toi-même »), sans aucun échec de connexion. C'est un geste de moins pour Lazar.
- **Ce qu'on perd** : un recoupement entre deux sources. Si Lazar donne l'adresse, la mesure la confronte à ce que le
  service d'adresse renvoie ; si la session la lit au même service, un service qui se tromperait ne serait pas vu.
- **Pourquoi c'est acceptable** : le pire cas est une règle du pare-feu ouverte à une mauvaise adresse, sur un serveur
  qui vit une vingtaine de minutes, ne porte ni clé ni dépôt, et n'admet que la clé jetable de l'essai ; ou bien une
  connexion impossible, donc un pilote en échec et la section 5. La mesure à 16 requêtes garde son rôle : elle dit si le
  poste sort par une ou plusieurs adresses.
- **Ce qui ne change pas** : l'adresse reste dans la conversation, jamais dans un fichier du clone ni dans un message ;
  la levée de la règle 3 couvre déjà ce service.
- **Qui tranche** : c'est un écart à la procédure v12 (« Lazar donne ») et il touche un geste et une donnée de Lazar.
  La mère peut l'écrire dans la consigne ; je recommande une ligne à Lazar avec la phrase de lancement. Sans réponse, le
  texte ci-dessous laisse les deux voies ouvertes, donc aucune attente en cours d'essai.

Texte proposé, si la mère retient la recommandation. Au point 5 de « Avant de lancer », remplacer :

```
5. **L'adresse publique du poste (`IP_POSTE`)**, donnée à la session. Elle n'est jamais écrite dans un fichier du clone ni
   dans un message.
```

par :

```
5. **L'adresse publique du poste (`IP_POSTE`)** : lue par la session depuis Ubuntu, par une requête au service que
   `MV7 adresses-sortie` interroge, ou donnée par Lazar s'il le préfère. Elle reste dans la conversation : jamais écrite
   dans un fichier du clone ni dans un message.
```

Au mandat 2, avant la ligne « **`MV7 adresses-sortie --ip-poste IP_POSTE`** », ajouter :

```
   - **`IP_POSTE`** : si Lazar ne te l'a pas donnée, tu la lis depuis Ubuntu par
     `python3 -c "import urllib.request; print(urllib.request.urlopen('https://api.ipify.org', timeout=15).read(64).decode('ascii'))"`
     (une requête, le service de `adresses-sortie`). C'est un écart écrit à la procédure v12, qui la fait donner par
     Lazar (écart 2 du rapport v3, repris) ; tu le déclares au rapport. La mesure qui suit se fait comme écrit ;
```

Et remplacer la réserve « **Adresse du poste** » de la fin par :

```
- **Adresse du poste** : l'écart 2 du rapport v3 (adresse lue par la session) est repris et écrit au mandat 2. On y perd
  le recoupement entre l'adresse donnée par Lazar et celle que le service renvoie ; le pire cas est borné (serveur sans
  clé ni dépôt, clé jetable seule admise, une vingtaine de minutes de vie).
```

## 6. Suite

Les corrections E1 et E2 changent l'empreinte de la consigne. Le poste vérifie la consigne contre son compagnon sur
`origin/main` et n'en lit qu'une : une version neuve (R12) est plus sûre qu'un erratum à lire à côté. Si la version
neuve ne porte que E1, E2, E3 et, au choix de la mère, le texte du § 5, tels qu'écrits ici, je la tiens pour prête sur
la seule lecture de son différentiel.

Rien n'a été modifié dans la consigne ; rien n'est committé.
