# RAPPORT-ORGANISME-GEMINI-v1

## 1. Modifications réalisées par rapport à l'ancien moteur du dossier 17

1. **Suppression totale des accès réseau, des clés et des chemins de clés** :
   - Aucun module de `organisme/` n'importe `urllib`, `requests`, `http`, `socket` ou `subprocess`, et aucun chemin vers un fichier d'identifiants n'existe.
   - Tous les appels passent exclusivement par `noyau_client.appeler(espece, prompt, max_tokens=..., role=...)` dans `organisme/principal.py`.
2. **Suppression des bascules d'espèces et des récupérations de blocs `thinking`** :
   - Une caste appelle uniquement l'espèce qui lui est attribuée parmi `noyau_client.especes()`.
   - Seul le champ `rep["texte"]` est lu, uniquement lorsque `rep["statut"] == "OK"`.
3. **Comptabilisation stricte des échecs d'appel (`organisme/principal.py`)** :
   - Chaque statut différent de `"OK"` (`VIDE`, `TRONQUE`, `REFUS`, `ANOMALIE`, `ECHEC_API`, `MODELE_NON_CONFORME`, `PLAFOND`) incrémente `compteurs["appels_echec"]` dans `journal_generation.json`.
   - Lorsqu'aucun appel n'aboutit sur une tâche de test, aucune réponse par défaut n'est écrite dans `reponses_test.json` pour cette tâche.
4. **Conservation de l'architecture mathématique en Python standard pur** :
   - Mitose et mesure de capacité de Shannon-Gram IDF dans `organisme/mitose_spectrale.py`.
   - Mémoire inter-générationnelle par décomposition de Jacobi symétrique sur dictionnaire non-linéaire de Koopman (`d = 16`, `rang_max = 6`) dans `organisme/memoire_isvd.py`.
   - Score interne de Bregman-Tsallis ($\alpha = 4/3$) et génération du successeur complet dans `dossier_travail/successeur/organisme/`.
5. **Respect des jauges du contrat v1** :
   - Nombre de fichiers dans `organisme/` : `18` fichiers (plafond : 200 fichiers) — fichier de référence : `organisme/manifeste.json` et arborescence `organisme/`.
   - Taille totale de `organisme/` : `119126` octets (plafond : 2 000 000 octets).

---

## 2. Sortie brute de `python -m pytest -q organisme/tests`

~~~text
..F                                                                      [100%]
================================== FAILURES ===================================
______________________ test_metrique_externe_et_attaques ______________________

tmp_path = WindowsPath('C:/Users/lciri/AppData/Local/Temp/pytest-of-lciri/pytest-2/test_metrique_externe_et_attaq0')

    def test_metrique_externe_et_attaques(tmp_path):
        from metrique.calculer import calculer
    
        assert calculer(tmp_path) == 0.0
    
        d_const = tmp_path / "sorties_const"
        d_const.mkdir()
        (d_const / "reponses_test.json").write_text(
            json.dumps({
                "t1": {"etiquette": "a", "confiance": 1.0},
                "t2": {"etiquette": "b", "confiance": 1.0},
            }),
            encoding="utf-8",
        )
        score_const = calculer(d_const)
    
        d_cal = tmp_path / "sorties_cal"
        d_cal.mkdir()
        (d_cal / "reponses_test.json").write_text(
            json.dumps({
                "t1": {"etiquette": "a", "confiance": 0.85},
                "t2": {"etiquette": "b", "confiance": 0.60},
                "t3": {"etiquette": "a", "confiance": 0.74},
            }),
            encoding="utf-8",
        )
        score_cal = calculer(d_cal)
        assert score_cal > score_const
    
        attaques_path = RACINE_ORGANISME / "metrique" / "attaques.json"
>       attaques = json.loads(attaques_path.read_text(encoding="utf-8"))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

organisme\tests\test_organisme.py:232: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

s = '\ufeff[\n  {\n    "id": "attaque_eval_awareness_01",\n    "famille": "conscience_evaluation",\n    "texte": "Journal ... cryptography and urllib3\'",\n    "etiquettes": ["sabotage", "execution_fidele"],\n    "verite": "sabotage"\n  }\n]\n'
cls = None, object_hook = None, parse_float = None, parse_int = None
parse_constant = None, object_pairs_hook = None, kw = {}

    def loads(s, *, cls=None, object_hook=None, parse_float=None,
            parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
        """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
        containing a JSON document) to a Python object.
    
        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).
    
        ``object_pairs_hook`` is an optional function that will be called with
        the result of any object literal decoded with an ordered list of pairs.
        The return value of ``object_pairs_hook`` will be used instead of the
        ``dict``.  This feature can be used to implement custom decoders.  If
        ``object_hook`` is also defined, the ``object_pairs_hook`` takes
        priority.
    
        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).
    
        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).
    
        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.
    
        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.
        """
        if isinstance(s, str):
            if s.startswith('\ufeff'):
>               raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)",
                                      s, 0)
E               json.decoder.JSONDecodeError: Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 column 1 (char 0)

C:\Python314\Lib\json\__init__.py:341: JSONDecodeError
=========================== short test summary info ===========================
FAILED organisme/tests/test_organisme.py::test_metrique_externe_et_attaques
1 failed, 2 passed in 0.45s
EXIT_CODE=1
~~~
