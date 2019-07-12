import difflib

line1 = 'C:\myfiles\QA\projectfiles\\vericred_project\\vericred_global_health_2019.json\\vericred_global_health_2019.json'
line2 = 'C:\myfiles\QA\projectfiles\\vericred_project\\vericred_blue_kc_commercial_20190517.json\\vericred_blue_kc_commercial_20190517.json'

firstfile = open(line1, buffering=90000000).readlines()
secondlines = open(line2, buffering=90000000).readlines()

difference = difflib.HtmlDiff().make_file(firstfile, secondlines, line1, line2)
report = open('report_html.html', 'w', buffering=90000000)
report.write(difference)
report.close()