# Relance — pièce 6 : le lieu d'où part l'envoi — v1

- Classe C. Écrite le 2026-11-22 vers 15:00 UTC par le monteur de l'oracle du cycle 1, relance. **Sans contenu.**
  Peut sortir du coffre telle quelle.
- Mandat v3, section 4, point 6. Course, brouillon 17 (`cf5d35d8472137d3…`) : section D6, point 2 de la voie d'envoi,
  et table des nœuds tranchés, ligne « Lieu d'où part l'envoi » ; pièce de sécurité v16 (`b8bcda60ead6f58f…`),
  section 3.5, condition 2.

## 1. L'identifiant

**`session_01XJ6MgmSDBZpPAuXLe3diix`** — session du monteur de l'oracle du cycle 1, relance, dans le nuage ; accès au
coffre inscrit par la mère à `registres/decisions.md`, R-4919.

## 2. Remplacements exacts dans la course, à la version définitive

Recherche par programme dans le brouillon 17 : l'identifiant de l'ancienne session y figure **deux fois**, et nulle
part dans la répétition (brouillon 9) ni dans la pièce de sécurité v16.

**Remplacement 1** — section D6, voie d'envoi, point 2. Remplacer :

```
(session `session_01Qi7Gr4BDyW322Ljw2o29ZT` ; inscrit au registre, [R79], R-4679 ;
```

par :

```
(session `session_01XJ6MgmSDBZpPAuXLe3diix` ; inscrit au registre, <ligne de la mère> ;
```

**Remplacement 2** — table des nœuds tranchés, ligne « Lieu d'où part l'envoi ». Remplacer :

```
| — Lieu d'où part l'envoi | la session du monteur de l'oracle, `session_01Qi7Gr4BDyW322Ljw2o29ZT`, dans le nuage, par programme | la mère, [R79], R-4679 | la même |
```

par :

```
| — Lieu d'où part l'envoi | la session du monteur de l'oracle, `session_01XJ6MgmSDBZpPAuXLe3diix`, dans le nuage, par programme | la mère, <ligne de la mère> | la même |
```

`<ligne de la mère>` : la ligne de `registres/decisions.md` qui inscrit ce lieu neuf, à écrire par la mère ; R-4679
reste citée comme source de la décision de principe si la mère le veut. **Trois renvois voisins** désignent le monteur
par R-4638 (accès du prédécesseur au coffre) : la table des documents qui font foi ([RM]), D6 (premier alinéa) et D8
(ligne « Monteur de l'oracle »). Je propose d'y ajouter R-4919 à côté de R-4638, sans retirer R-4638 ; c'est à la mère
et à l'auteur de la course d'en décider. Tant que le remplacement n'est pas fait, **aucun envoi ne part** (mandat v3).

## 3. Ce qu'est ce lieu, constaté le 2026-11-22 à 14:47 UTC (outil de l'environnement, noms seulement)

- Environnement de la session : « Default », personnel, `env_01UFLPnTerMQQPUUtMxFFJRq`.
- Réseau sortant : **non restreint**.
- Clés de fournisseurs présentes **sous forme de variables**, dont : `OPENAI_API_KEY`, `OPENAI_API_KEY_2`,
  `GEMINI_API_KEY`, `GEMINI_API_KEY_2`, `GEMINI_API_KEY_3`, `GEMINI_API_KEY_FREE`, `MISTRAL_API_KEY`, `KIMI_API_KEY`,
  et des clés d'Anthropic. Aucune valeur lue.
- Le dépôt est cloné dans le conteneur, coffre compris (l'envoyeur est un lecteur du coffre : c'est voulu).

## 4. Réserves

1. **L'environnement est partagé.** « Default » sert toutes les sessions de Lazar qui ne choisissent pas d'autre
   environnement ; ses clés ne sont pas propres à l'envoyeur. La condition 2 de la pièce de sécurité (« les clés des
   fournisseurs vivent dans l'environnement de l'envoyeur, jamais sur le banc ni sur le poste de transit ») tient si ni
   le banc ni le poste de transit ne tournent sous cet environnement. C'est au vérificateur interne de le constater
   (point 27). Un environnement propre à l'envoyeur, avec les deux seules clés des lecteurs, ferait tenir la condition
   par construction ; c'est un geste de Lazar.
2. **Le réseau n'est pas restreint.** Le programme d'envoi doit refuser par lui-même tout point d'accès et tout modèle
   absents du champ n° 18 (garde 16). Il doit aussi refuser `GEMINI_API_KEY_FREE` : le service gratuit de Google admet
   la lecture humaine et l'usage des contenus.
3. **La session est éphémère.** Son conteneur est repris après une période d'inactivité ; la session de mon
   prédécesseur est devenue injoignable (R-4779). Si la mienne le devient, le lieu change de nouveau, par un
   remplacement exact et une ligne de la mère, comme ici. Rien ne part d'un lieu que la course ne nomme pas.
4. **Comment les produits arrivent ici** : la course dit que l'opérateur lance l'extraction et remet les produits ; le
   chemin de cette remise, jusqu'à ce conteneur, n'est pas écrit dans les sections que j'ai lues. Il ne doit passer ni
   par la mère ni par aucune session de conception de moniteurs. C'est à écrire avec le code de l'extraction et de
   l'envoi (classe B, contre-lu).
5. **Les messages de cette session vers la mère passent** (deux comptes rendus remis le 2026-11-22 vers 14:53 et
   14:57 UTC). Le refus qui bloquait le prédécesseur (`elevated_session_untrusted_device`) ne s'est pas présenté.
