# 1. Environment Setup
try:
    import gtda
except ImportError:
    !pip install giotto-tda --quiet
    print("✨ Libraries installed. PLEASE RESTART RUNTIME to apply changes.")
    
    import sys
    sys.exit() 

import os
import numpy as np
import pandas as pd
from gtda.time_series import TakensEmbedding
from gtda.homology import VietorisRipsPersistence
from gtda.plotting import plot_diagram

# 2. Data Summoning from GitHub
# Clone the repository only if it doesn't already exist in the environment
repo_url = "https://github.com/OgatiesInstitute/Nikkei225-Analysis.git"
repo_name = "Nikkei225-Analysis"

if not os.path.exists(repo_name):
    print(f"Cloning {repo_name} from GitHub...")
    !git clone {repo_url}
else:
    print(f"Repository '{repo_name}' already exists. Ready to analyze.")

# 3. Loading Datasets
# Fetching the historical bubble data and the modern structural data
df_2026 = pd.read_csv(f'{repo_name}/Nikkei225_2025_2026.csv')
df_1989 = pd.read_csv(f'{repo_name}/Nikkei225_1987_1991.csv')

# 4. TDA Engine Configuration
# Constructing a 3D attractor with a 3-day time delay
embedding = TakensEmbedding(time_delay=3, dimension=3)
persistence = VietorisRipsPersistence(homology_dimensions=[0, 1, 2])

# --- Phase 1: Steel Framework Analysis (2026) ---
print("\n[Executing Analysis 1/2]: Steel Framework of 2026")
data_2026 = df_2026['price'].values.reshape(1, -1)
embedded_2026 = embedding.fit_transform(data_2026)
diagram_2026 = persistence.fit_transform(embedded_2026)

# --- Phase 2: Bubble Ghost Analysis (1989) ---
print("[Executing Analysis 2/2]: The 1989 Bubble Illusion")
# Note: 1989 data is large (1,233 days). 
# If CPU load is too high, consider sampling: data_1989[::2]
data_1989 = df_1989['price'].values.reshape(1, -1)
embedded_1989 = embedding.fit_transform(data_1989)
diagram_1989 = persistence.fit_transform(embedded_1989)

# --- 5. Global Visualization ---

# 2026: Modern Era Structural Integrity
print("\n[STEP 1/2] Generating Visualization: Steel Framework of 2026")
fig_2026 = plot_diagram(diagram_2026[0])
fig_2026.update_layout(
    title="FIGURE 1: Steel Framework of the Modern Era (2026)",
    title_x=0.5
)
fig_2026.show()  # Displaying the 2026 structure

# 1989: The Illusion of the Bubble
print("\n[STEP 2/2] Generating Visualization: The Illusion of the 1989 Bubble")
fig_1989 = plot_diagram(diagram_1989[0])
fig_1989.update_layout(
    title="FIGURE 2: The Illusion of the 1989 Bubble (1989-1991)",
    title_x=0.5
)
fig_1989.show()  # Displaying the 1989 ghost
