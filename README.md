# QDMA Log Parser

## Description
This Python script parses QDMA execution log files to extract detailed function call events. It identifies entries and exits of QDMA-related functions, capturing timestamps, function names, source file paths, line numbers, and thread IDs.

The script outputs:
- A structured JSON file (`qdma_log_output.json`) containing all parsed log entries.
- A color-coded HTML table (`qdma_log_output.html`) for easy visualisation of the function calls.

## Key Data Points Extracted
- **Timestamp**: The precise time the event occurred.
- **Function Name**: The QDMA function being entered or exited.
- **Action**: Whether the function is being entered or exited.
- **File Path**: Source code file location where the function call occurred.
- **Line Number**: Exact line number in the source file of the event.
- **Thread ID**: The thread executing the function.

## Usage
1. Place your QDMA log file (e.g., `modprobe_qdma_pf.txt`) in the same directory as the script.
2. Run the script to generate `qdma_log_output.json` and `qdma_log_output.html`.
3. Open the HTML file in a browser to review the color-coded function call timeline.

## Requirements
- Python 3.x
- pandas
- IPython (for displaying HTML in notebooks)



