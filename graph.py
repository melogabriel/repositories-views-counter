import json
import matplotlib.pyplot as plt
from datetime import datetime

# Load the JSON data
with open('records.json', 'r') as f:
    records = json.load(f)

# Extract data for plotting
dates = [datetime.fromisoformat(r['timestamp'].replace('Z', '')) for r in records]
counts = [r['count'] for r in records]
uniques = [r['uniques'] for r in records]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(dates, counts, label='Count', color='blue', marker='o')
plt.plot(dates, uniques, label='Uniques', color='red', marker='o')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Daily Count and Uniques')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph as an image file
plt.savefig('graph.png')
