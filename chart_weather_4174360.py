from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


# Read the CSV file
path = Path('weather_data/4174360.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract data
dates = []
tmax = []  # Max temperature
tmin = []  # Min temperature
tobs = []  # Temperature observed
prcp = []  # Precipitation
snow = []  # Snow
snwd = []  # Snow depth

for row in reader:
    try:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        
        # Skip rows with missing temperature data
        if not row[12] or not row[14] or not row[16]:
            continue
            
        dates.append(current_date)
        
        # Temperature data
        tmax.append(int(row[12]))
        tmin.append(int(row[14]))
        tobs.append(int(row[16]))
        
        # Precipitation and snow data
        prcp.append(float(row[6]) if row[6] else 0.0)
        snow.append(float(row[8]) if row[8] else 0.0)
        snwd.append(float(row[10]) if row[10] else 0.0)
    except (ValueError, IndexError):
        pass

# Create figure with multiple subplots
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# Plot 1: Temperature trends
axes[0].plot(dates, tmax, color='red', label='Max Temp', alpha=0.7, linewidth=2)
axes[0].plot(dates, tmin, color='blue', label='Min Temp', alpha=0.7, linewidth=2)
axes[0].plot(dates, tobs, color='green', label='Observed Temp', alpha=0.7, linewidth=1.5)
axes[0].fill_between(dates, tmax, tmin, facecolor='blue', alpha=0.1)
axes[0].set_title('Temperature Data - New York Mills, MN', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Temperature (°F)', fontsize=12)
axes[0].legend(loc='best')
axes[0].tick_params(labelsize=10)
axes[0].grid(True, alpha=0.3)

# Plot 2: Precipitation
axes[1].bar(dates, prcp, color='steelblue', alpha=0.7, width=0.8)
axes[1].set_title('Precipitation (Daily)', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Precipitation (inches)', fontsize=12)
axes[1].tick_params(labelsize=10)
axes[1].grid(True, alpha=0.3, axis='y')

# Plot 3: Snow data
axes[2].plot(dates, snow, color='cyan', label='Snow', alpha=0.7, linewidth=2)
axes[2].plot(dates, snwd, color='darkblue', label='Snow Depth', alpha=0.7, linewidth=2)
axes[2].set_title('Snow Measurements', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Snow (inches)', fontsize=12)
axes[2].set_xlabel('Date', fontsize=12)
axes[2].legend(loc='best')
axes[2].tick_params(labelsize=10)
axes[2].grid(True, alpha=0.3)

# Format x-axis for all subplots
for ax in axes:
    fig.autofmt_xdate()

# Adjust layout to prevent label cutoff
fig.tight_layout()

# Save and show the plot
plt.savefig('weather_4174360_charts.png', dpi=300, bbox_inches='tight')
print(f"Chart saved to 'weather_4174360_charts.png'")
print(f"Data points plotted: {len(dates)}")
print(f"Date range: {dates[0].date()} to {dates[-1].date()}")
plt.show()
