# =================================================================
# Chapter 7: Market Family Tree - Hierarchical Clustering Analysis
# =================================================================

# 1. Environment Setup
# Note: yfinance is required to fetch real-time market data.
!pip install yfinance --quiet

import yfinance as yf
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# 2. Selecting the "Steel Frame" Entities
# Representative blue-chip stocks of the Nikkei 225 across key sectors:
# Tech, Finance, Trading, and Manufacturing.
tickers = [
    '9983.T', '8035.T', '6758.T', '9984.T', '4502.T', # Fast Retailing, TEL, Sony, SBG, Takeda
    '8306.T', '8316.T', '8411.T',                   # Mitsubishi UFJ, SMFG, Mizuho
    '8001.T', '8031.T', '8058.T',                   # Itochu, Mitsui, Mitsubishi Corp
    '7203.T', '7267.T', '9101.T'                    # Toyota, Honda, NYK Line
]

# 3. Fetching Real-time Market Data
print("Fetching real-time market data from Yahoo Finance...")
# We use the past 1 year of daily closing prices to build the correlation.
raw_data = yf.download(tickers, period="1y")['Close']

# 4. Calculating the Topological Distance (Correlation Matrix)
# This defines the "closeness" of the stocks in the high-dimensional space.
correlation_matrix = raw_data.corr()

# 5. Hierarchical Clustering (Ward's Method)
# Ward's method minimizes the variance within each cluster.
print("Unveiling the Family Tree of the Modern Era...")
Z = linkage(correlation_matrix, 'ward')

# 6. Global Visualization (Dendrogram)
plt.figure(figsize=(12, 8))
dendrogram(
    Z, 
    labels=tickers, 
    orientation='top', 
    leaf_rotation=90, 
    distance_sort='descending'
)

plt.title("FIGURE 3: The Family Tree of the Steel Frame (Real-time Analysis)", fontsize=14)
plt.xlabel("Ticker Symbols", fontsize=12)
plt.ylabel("Topological Distance (Structural Similarity)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n[Analysis Complete]: Look for the 'Clustered Islands'.")
print("Stocks merging at low heights belong to the same 'Shared Fate'.")
