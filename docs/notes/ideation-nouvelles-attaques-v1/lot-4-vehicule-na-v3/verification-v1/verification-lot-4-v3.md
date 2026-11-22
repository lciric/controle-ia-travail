# Vérification du lot 4 v3 (véhicule NA-1) — vérificateur Sonnet neuf

Verdict : **Conforme**. Bloquant : aucun. B1 de la v2 est corrigé.

## Faits
1. Table d'empreintes : 13 fichiers OK ; 13 compagnons .sha256 OK.
2. Rejeu sur copie neuve de a41b7b50, lots 2 v5, 3 v3, 4 v1, 4 v3 posés dans l'ordre (liste_reelle_na_v5.py copié par le programme du lot 2, jamais joué) : **255 passés, 0 échec** ; mutations : **68 sur 68 tuées**, témoin non muté passe, témoin inerte survit (conforme = vrai). Conforme au journal annoncé.
3. Point prioritaire (mon_essai_v3.py, faux serveur 127.0.0.1, adaptateur réel, sortie : sortie-mon-essai-v3.txt ; 0 écart) :
   - 400 invalid_request_error + « credit balance is too low » : classe « crédit d'amont (400, message de solde) » ; chaîne complète : arrêt n° 13 au premier appel (1 requête) et en repli après refus (2 requêtes, pas de second repli) ;
   - 400 autre message, fragment partiel, 429/403/500 avec fragment, 400 billing_error ou authentication_error avec fragment : pas de n° 13 ; 402 billing_error : n° 13 ;
   - artefacts : casse mixte (levé), espaces autour (levé), espaces internes doublés (non levé, comparaison stricte), message dans un autre champ (top-level, error.detail : non levé), corps non JSON, corps liste, message non chaîne : non levé.
4. Message jamais recopié : absent de la fiche de tentative, du journal des requêtes, de na_replis et du texte de l'arrêt dans tous les cas.
5. Différentiel v2→v3 : six fichiers ; hors renommages/versions/docstrings, seuls changements de règle : constantes, message_de_solde, une règle dans classer_erreur, ERREURS_CREDIT étendu ; aides et essais ajoutés. Rien d'autre, conforme au rapport.

## À noter
- Le fragment est fixé : un changement de texte du fournisseur rend la voie 400 muette (réserve déjà déclarée par le développeur).
- Je n'ai pas relu la v2 elle-même (hors liste) : le différentiel est pris tel que livré, vérifié par son contenu.
- Flux (stream) non éprouvé ici, comme déjà ouvert.
