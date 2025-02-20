# Economic Indicators in Python

## Objectives

Python package for Industrial Economics and Public Health Economics indicators

## Organization

- `src/economic_indicators/industrial_economics` contains industrial economics indicators implemented in Python such as market concentration indicators
- `src/economic_indicators/public_health_economics` contains hospital activity measures indicators implemented in Python
- `examples` contains use cases for the different implementations
- `docs` contains documentation with definitions and formulas

## Industrial Economics indicators

This repo contains implementations of several economic indicators for market concentration in Python, including:
- Gini Index
- Lorenz Curve
- Hoover Index
- Concentration Ratio
- Herfindahl-Hirschman Index
- Theil Index
- Shannon Entropy

 Definitions and formulas are given [here](docs/INDUSTRIAL_ECONOMICS_INDICATORS.md)

 ## Installation

 ```bash
git clone <repo_url>
pip install -e economic_indicators
```

The package can then be used like any other Python package.

 ## Public Health Economics indicators

 This repo contains implementation of several measures of hospital activity, including:
 - Number of hospital stays
 - Economic volume

 Definitions and formulas are given [here](docs/PUBLIC_HEALTH_ECONOMICS_INDICATORS.md)
 
