import libs.file_operations as fo

# Replace 'your_report.html' with the actual file path of your HTML report
report_file_path = 'C:/userdata/Workspace/dske_IT-SGN-LT-DKSE1_dev_sgo_dske_NO_TLM-9924_6778/logs/TC-IS-CoAP-UCOAP-Syntax-001_TEST_FAIL_20230726_124606.html'

# Read the HTML report
html_report = fo.read_html_report(report_file_path)

# Define the delimiter used to split the report
delimiter = "=========================================================="

# Split the report into segments
segments = fo.split_report_into_segments(html_report, delimiter)

# Now you have the segments, and you can perform further analysis on each segment
keywords = ["AT TX:", "DUT response is", "Expected response is:"]
lines = []
for index, segment in enumerate(segments, start=1):
    print(f"Segment {index}:")
    print(segment)
    print("-------------------------------------------------------------")
    lines.append(fo.filter_lines_by_keywords(segment, keywords))

print(lines)