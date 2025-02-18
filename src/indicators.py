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
       normalize:bool=False,
       verbose:bool=False) -> float:
    """
    Compute the Herfindahl-Hirschman Index (HHI) for market concentration.

    Args:
        x (Sequence[float]): A 1D sequence of market shares (values between 0 and 1).
        normalize (bool, optional): If True, HHI is normalized to range from 0 to 1.
                                    Defaults to False (returns standard HHI).
        verbose (bool, optional): If True, additional information is printed during the computation. 
                                  Defaults to False.
                                    
    Returns:
        float: The HHI value. 
               - If `normalize=False`, HHI ranges from 0 (perfect competition) to 1 (monopoly).
               - If `normalize=True`, HHI is adjusted to account for the number of firms.
               - If shares are mistakenly given as percentages (>1 sum), a warning is raised.

    Raises:
        ValueError: If `x` is not a 1D array, contains negative values, or NaN values.
        ValueError: If normalization is applied with regard to only one company.
    """

    x = np.array(x, dtype=np.float64)

    # Check if x is 1D array
    if x.ndim != 1:
        raise ValueError("""The market shares data provided should be one-dimensional.""")

    # Check if all market shares are positive
    if (x < 0).any():
        raise ValueError("""Some market shares provided are strictly negative.""")

    # Check if data is missing
    if np.isnan(x).any():
        raise ValueError("""Some market shares provided are missing (NaN values).""")

    # Warn about shares in percentage
    if np.sum(x) > 1.01:
        warnings.warn("""Market shares seem expressed in % as the sum
                      of market shares is strictly higher than 1.""", 
                      UserWarning)

    if verbose:
        print("""
            HHI higher than 0.25 (or 2500 for percentage data)
            means high level of concentration
            """)
        print(f"Sum of market shares : {np.sum(x)}")

    # Compute HHI with normalization if necessary
    hhi = np.sum(x**2)

    if normalize:

        if verbose:
            print(f"Unnormalized HHI : {hhi}")
            
        n = len(x)
        if n > 1:
            hhi = (hhi-1/n)/(1-1/n)
        else:
            raise ValueError("""Normalization is not meaningful with only 1 company (zero-division in formula).""")

        if verbose:
            print(f"Normalized HHI : {hhi}")

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
