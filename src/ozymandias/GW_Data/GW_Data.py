import jax.numpy as jnp
from abc import ABC


class GW_Data(ABC):
    """Generic Gravitational Wave data class. Holds localisation and distance information for a bunch of events
    as well as routines to return the probablities from those events"""

    def __init__(self):
        # A dictionary of events, indexed by event name
        self.events = {}

    def load_events(self):
        """
        Loads a series of GW events into the events dictionary.

        :return:
            None
        """
        return NotImplementedError

    def return_sky_prob(self, ra, dec):
        """
        :param ra: np.array: An array of N ra's at which to return the probabilities for each of the GW events
        :param dec: np.array: An array of N dec's at which to return the probabilities for each of the GW events
        :return prob: np.array: An array of size N_GW x N containing the probabilities for for each GW event at each pair of coordinates
        """

        assert len(ra) == len(dec)
        prob = jnp.zeros((len(self.events), len(ra)))

        return prob

    def return_dist_prob(self, lum_dist):
        """
        :param lum_dist: np.array: An array of N luminosity distances at which to return the probabilities for each of the GW events
        :return: An array of size N_GW x N containing the probabilities for each GW event at each distance
        """

        prob = jnp.zeros((len(self.events), len(lum_dist)))

        return prob


if __name__ == "__main__":
    # Run some simple unit tests
    data = GW_Data()
