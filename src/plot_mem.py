import pandas as pd
import plotly.express as px
import os

# Load the data
data = pd.read_csv("memory_usage.log", delimiter="|", parse_dates=["Timestamp"])


# Function to truncate long text
def truncate_command(cmd):
    return (cmd[:150] + "...") if len(cmd) > 150 else cmd


# Apply truncation to the command line
data["Truncated Command"] = data["Process Name"].apply(truncate_command)

# Create the plot with custom hover data
fig = px.line(
    data,
    x="Timestamp",
    y="RSS",
    color="PID",
    line_group="PID",
    labels={"RSS": "Resident Set Size (kB)", "PID": "Process ID", "Truncated Command": "Command"},
    title="Memory Usage Over Time",
    hover_data={"Truncated Command": True, "PID": True},
)

# Update hovertemplate to include the PID and the truncated command
fig.update_traces(
    hovertemplate="<b>Time:</b> %{x}<br>"
    + "<b>RSS:</b> %{y} kB<br>"
    + "<b>PID:</b> %{customdata[1]}<br>"  # Index [1] for PID
    + "<b>Command:</b> %{customdata[0]}<extra></extra>"  # Index [0] for Truncated Command
)

output_dir = "output"
output_file = "plot.html"
full_path = os.path.join(output_dir, output_file)

# Check if the directory exists, if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the figure to an HTML file
fig.write_html(full_path)
