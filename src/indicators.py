import numpy as np
import matplotlib.pyplot as plt
import warnings
from typing import Sequence

def gini_index(x:Sequence[float]) -> float:
    """
    Return the Gini Index of an array.

    Args:
        x (Sequence[float]): Sequence of market shares.

    Returns:
        float: The Gini Index between 0 for perfect equality and 1 for perfect inequality.
    """

    sorted_x=np.array(x,dtype=float).flatten().copy()
    sorted_x.sort()
    n=x.size
    coef=2/n
    const=(n+1)/n
    weighted_sum=sum([i*y for i,y in enumerate(sorted_x)])
    return coef*weighted_sum/sorted_x.sum()-const

def lorenz_curve(x:Sequence[float]) -> None:
    """
    Plot the Lorenz Curve of an array.

    Args:
        x (Sequence[float]): Sequence of market shares.
        
    Returns:
        None.
    """

    sorted_x=np.array(x,dtype=float).flatten().copy()
    sorted_x.sort()
    lorenz_x=sorted_x.cumsum()/sorted_x.sum()
    lorenz_x=np.insert(lorenz_x, 0, 0)

    fig, ax=plt.subplots(figsize=[6,6])
    ax.scatter(np.arange(lorenz_x.size)/(lorenz_x.size-1),
              lorenz_x,
              marker="x",
              color="orange",
              s=100)
    ax.plot([0,1],
           [0,1],
           color="green")

def hhi(x:Sequence[float],
       normalize:bool=False) -> float:
    """
    Return the Herfindahl-Hirschman index of an array.

    Args:
        x (Sequence[float]): Sequence of market shares.
        normalize (bool, optional): If set to True, the HHI is normalized. Defaults to False.

    Returns:
        float: The Herfindahl-Hirschman index of an array between 0 and 1 (or 10.000 if a value is above 1).
                Above 0.25 (or 2500) : highly concentrated market.
    """

    x = np.array(x)

    if x.ndim != 1:
        raise ValueError("""The market shares data provided should be one-dimensional.""")

    if (x < 0).any():
        raise ValueError("""Some market shares provided are strictly negative.""")

    if np.isnan(x).any():
        raise ValueError("""Some market shares provided are missing.""")

    if np.sum(x) > 1:
        warnings.warn("""Market shares are expressed in % as the sum
                     of market shares is strictly higher than 1""", 
                      UserWarning)

    # Compute HHI with normalization if necessary.
    if normalize == False:
        hhi = np.sum(x**2)
    else:
        n = len(x)
        hhi = (np.sum(x**2)-1/n)/(1-1/n)

    return hhi

def concentration_ratio(x:Sequence[float], n:int=3) -> float:
    """
    Return the concentration ratio of a market for a parameter n.

    Args:
        x (Sequence[float]): Sequence of market shares.
        n (int, Optional): Number of companies to consider as top n market shares.

    Returns:
        float: Concentration ratio from 0 to 0.4 competitive market,
            from 0.4 to 0.7 medium concentration, from 0.7 to 1 high concentration.
    """
    
    x=np.array(x, dtype=float).flatten()
    x.sort()

    return x[-n:].sum()
