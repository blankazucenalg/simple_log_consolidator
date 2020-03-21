from LogConsolidator import LogConsolidator

logConsolidator = LogConsolidator()
logConsolidator.generate_logs(number_of_files=5, number_of_lines=1000)
logConsolidator.consolidate_sorted_logs()
