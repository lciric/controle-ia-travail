"""torch factice des essais du correctif 0011 : une carte est visible, comme sur la machine louée, tant que
CUDA_VISIBLE_DEVICES n'est pas vide (contrat de CUDA : vide, aucune carte n'est visible du processus)."""
import os


class cuda:  # noqa: N801
    @staticmethod
    def is_available():
        return os.environ.get("CUDA_VISIBLE_DEVICES") != ""
