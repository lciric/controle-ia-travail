# Vérification neuve du lot 12 (Astra par lots) — v1
Essais : 10 réussis. Artefacts : verif-lot12-artefact1.py, verif-lot12-sortie1.txt (même dossier).

Verdict : CONFORME, GO possible, avec trois réserves mineures.

- Conformité : POST /v1/files purpose=batch, puis /v1/batches, 24h, lignes {custom_id, method, url, body}, xhigh, max_completion_tokens 96000, tarif 5/20, rattachement par custom_id, arrêt sur doublon ou total différent. Conforme.
- Aucun texte de réponse n'est écrit au journal ni affiché : seuls comptes, classes fermées, empreintes ; le nom du modèle servi est filtré par expression régulière. Les messages de refus ne portent que des statuts.
- Clé : lue par son nom, utilisée seulement dans l'en-tête ; jamais imprimée ni journalisée.
- Quarantaine avant contrôle : ACCEPTABLE. La sortie brute va dans un fichier neuf (mode xb) avec empreinte, jamais affichée ; le journal reste vide en cas de relève incohérente (vérifié : refus, quarantaine présente, journal absent).
- Pire : 5,89049 USD (sortie 5,76 + entrée 0,13, octets comptés comme jetons, donc majorant) ; plafond du code 14,67 USD, refus au-delà. Les jetons de raisonnement sont inclus dans max_completion_tokens. Bornes tenues, aucun nouvel essai automatique.
- Multipart : analysé par le module email : deux parties (purpose=batch ; file, application/jsonl), contenu identique octet pour octet, borne aléatoire.

Réserves (non bloquantes) :
1. Sortie non JSON : JSONDecodeError non rattrapée (trace, code non 2), et la quarantaine est déjà écrite.
2. Relève répétée : FileExistsError, car la quarantaine est en xb ; il faut un dossier neuf à chaque relève.
3. Le registre de GO par défaut est /home/user/main-lecture/registres/go.md : passer --registre-go si le GO n'y figure pas. Une erreur réseau (URLError) n'est pas non plus rattrapée.
