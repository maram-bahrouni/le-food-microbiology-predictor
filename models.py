import numpy as np

class GompertzModel:
    """
    Modèle de Gompertz modifié pour la croissance microbienne.
    """
    def __init__(self, N0: float, Nmax: float, mu_max: float, lag: float):
        self.N0 = N0
        self.Nmax = Nmax
        self.mu_max = mu_max
        self.lag = lag

    def predict(self, t: np.ndarray) -> np.ndarray:
        A = self.Nmax - self.N0
        e = np.exp(1)
        log_N = self.N0 + A * np.exp(-np.exp(((self.mu_max * e) / A) * (self.lag - t) + 1))
        return log_N
        