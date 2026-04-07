# Nikkei 225 Topological Data Analysis (TDA)
This project visualizes the structural differences between the 1989 Asset Bubble and the 2026 Market using Persistent Homology and Hierarchical Clustering.

## 🚀 How to Run the Analysis
### 📊 Step 1: Structural Integrity (The Steel Framework)
Run `analysis_script.py` to compare the historical bubble with the modern reality.

- **Input:** Historical Nikkei 225 CSV data (included in this repo).
- **Output:** Persistence Diagrams ($H_0, H_1, H_2$) proving the "Steel Framework."

### 🌳 Step 2: Market Family Tree (The Connection)
Run `dendrogram_analysis.py` to unveil the hidden bloodlines of the market.

- **Input:** Real-time market data via Yahoo Finance.
- **Output:** A Dendrogram showing "Topological Collusion" and clustered investment risks.

## 🧠 The Concept: Steel Framework vs. Bubble Ghost
| Dimension | Color | Market Interpretation |
| :--- | :--- | :--- |
| $H_0$ | Orange | **Price Continuity**: The basic link between data points. |
| $H_1$ | Green | **Cyclic Swings**: The "Steel Frame" of the 2026 market. |
| $H_2$ | Purple | **Hollow Voids**: The "Ghostly Holes" found in the 1989 bubble. |

- **2026 (Modern):** A high-persistence Green ($H_1$) structure supporting the ¥53,123 reality.
- **1989 (Historical):** A cluster of Purple ($H_2$) voids—a hollow shell that lacked structural integrity.

## 🏛 Chapter 7: Visualizing Structural Integrity (Dendrogram Analysis)

To substantiate the topological claims, we provide a comparative "Family Tree" of market assets. This visual evidence highlights why the 2026 market is fundamentally different from the 1989 bubble.

## 🚀 Live Demo
You can explore the interactive 3D visualization here:
[https://ogatiesinstitute.github.io/nikkei-tda/](https://ogatiesinstitute.github.io/nikkei-tda/)

---
### 💡 Concept
This visualizer analyzes the **Topological Data Analysis (TDA)** of the Nikkei 225, 
comparing the "Bubble Ghost" of 1989 with the "Steel Framework" of 2026.
Designed with a Bloomberg-inspired UI and an "incandescent" aesthetic.

🔍 Geometric Insights

1989 (The Convergence Crisis): All stocks merge almost instantly at a very low threshold (Distance < 0.2). This "flat" architecture signifies a monolithic market where individual assets lack autonomy—a classic sign of a hollow bubble.

2026 (The Steel Framework): Assets maintain distinct clusters with significant vertical separation (Distance reaching 5.0+). This hierarchical "breathing room" confirms that the valuation is supported by independent, resilient sectoral pillars.

## 🛠 Prerequisites
```bash
pip install giotto-tda yfinance pandas numpy matplotlib
```

> [!NOTE]
> If running in Google Colab, please restart the runtime after the first installation to avoid version conflicts.
