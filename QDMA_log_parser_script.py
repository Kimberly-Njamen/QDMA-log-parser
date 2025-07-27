#!/usr/bin/env python
# coding: utf-8

# In[8]:


# -----------------------------------------------------------
# QDMA Log Parser
# Author: Kimberly
# Description:
#   This script reads a QDMA execution log file,
#   extracts function entry/exit events (timestamp, function name,
#   file path, line number, and thread ID), and outputs:
#     - A structured JSON file (`qdma_log_output.json`)
#     - A color-coded HTML table (`qdma_log_output.html`)
# --------------------------------------------------------

import re
import json
import pandas as pd
from IPython.display import display, HTML

def parse_log_to_json(log_file_path, json_output_file):
    log_pattern = re.compile(
        r"\[\s*(\d+\.\d+)\]\s+qdma_pf:(\w+): -----\s+QDMA\s+(entering|exiting)\s+the\s+\2\s+function at ([\w\/\.-]+):(\d+)\s+\[Thread ID:\s*(\d+)\]"
    )
    command_pattern = re.compile(r"\[\s*(\d+\.\d+)\] Command: (.+)")

    log_entries = []
    command_title = "QDMA Function Log"

    with open(log_file_path, 'r') as f:
        for line in f:
            command_match = command_pattern.search(line)
            if command_match:
                command_title = command_match.group(2)

            log_match = log_pattern.search(line)
            if log_match:
                entry = {
                    "timestamp": log_match.group(1),
                    "function": log_match.group(2),
                    "action": log_match.group(3),
                    "file": log_match.group(4),
                    "line": int(log_match.group(5)),
                    "thread_id": int(log_match.group(6))
                }
                log_entries.append(entry)

    json_data = {"command": command_title, "entries": log_entries}

    with open(json_output_file, 'w') as f_json:
        json.dump(json_data, f_json, indent=4)

    return json_data

log_file = "modprobe_qdma_pf.txt"  # Ensure this file is uploaded in the notebook's directory
json_file = "qdma_log_output.json"

data = parse_log_to_json(log_file, json_file)
print("✅ JSON file created.")

# Preview of the parsed data
#df = pd.DataFrame(data["entries"])
#df.head(10) 

def generate_html_table(data, output_html_file):
    command_title = data["command"]
    log_entries = data["entries"]

    with open(output_html_file, 'w') as f_out:
        f_out.write("<html><body>")
        f_out.write(f"<h2>{command_title}</h2>")
        f_out.write("<table border='1' style='border-collapse: collapse;'>")
        f_out.write("<tr style='background-color:#add8e6; font-weight:bold;'>")
        f_out.write("<th>Timestamp</th><th>Action</th><th>Function</th><th>File</th><th>Line</th><th>Thread ID</th></tr>")

        for entry in log_entries:
            row_color = "#ccffcc" if entry["action"] == "entering" else "#ffcccc"
            f_out.write(f"<tr style='background-color:{row_color};'>")
            f_out.write(f"<td>{entry['timestamp']}</td><td>{entry['action']}</td><td>{entry['function']}</td>")
            f_out.write(f"<td>{entry['file']}</td><td>{entry['line']}</td><td>{entry['thread_id']}</td></tr>")

        f_out.write("</table></body></html>")

    print(f"✅ HTML table generated: {output_html_file}")


html_file = "qdma_log_output.html"
generate_html_table(data, html_file)


with open(html_file, 'r') as f:
    html_data = f.read()

display(HTML(html_data))




# In[ ]:




