import os
import pandas as pd
import matplotlib.pyplot as plt
import brewer2mpl

# Get a list of all .dat files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.dat')]
files.sort()

# Define a color cycle for the plot
bmap = brewer2mpl.get_map('Set1', 'qualitative', 4)
colors = bmap.mpl_colors

# Initialize the plot
plt.figure()

# Define x-axis limits based on data table
xmin = float('inf')
xmax = float('-inf')

# Plot the data from each file using a different color
for i, file in enumerate(files):
    # Load the data from the file
    df = pd.read_table(file, sep=' ', header=None, index_col=False)
    
    # Update x-axis limits based on data table
    xmin = min(xmin, df[0].min())
    xmax = max(xmax, df[0].max())
    
    # Plot the data using the next color in the cycle
    plt.plot(df[0], df[1], linestyle='-', linewidth=2, color=colors[i % len(colors)], label=f'SVD={i}')

# Set x-axis limits
plt.xlim(xmin, xmax)

# Add labels, title, legend, and grid to the plot
plt.xlabel('Energy', fontsize=18, labelpad=10)
plt.ylabel('Cross Section', fontsize=18, labelpad=10)
plt.tick_params(axis='both', labelsize=16)
plt.legend(loc='best', labels=['SVD=0', 'SVD=1', 'SVD=2', 'SVD=3'], fontsize=14)
plt.grid(True)

# Adjust plot padding
plt.subplots_adjust(left=0.12, right=0.95, bottom=0.12, top=0.95)

# Show the plot
plt.show()
