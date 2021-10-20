# The following code outputs key RMA KPI data after processing a csv bulk data report

import pandas as pd
import numpy as np
RMA_bulk_data = pd.read_csv('BulkReportRMA10152021.csv', encoding='ISO-8859-1')
RMA_bulk_data["RMA Received Date"] = pd.to_datetime(TMO_bulk_data["RMA Received Date"], errors='coerce')
 
# In Warranty RMA pass/fail totals
IW_data = RMA_bulk_data[RMA_bulk_data.CUSTOMER_PO == "RMA-IW"]
print("IW TOTAL")
print(len(IW_data.index))
IW_pass = IW_data[IW_data["TEST RESULT"] == "PASS"]
IW_fail = IW_data[IW_data["TEST RESULT"] == "FAIL"]
iw_pass_total = len(IW_pass.index)
iw_fail_total = len(IW_fail.index)
iw_total_tested = iw_pass_total + iw_fail_total
print("--------")
print("IW PASS")
print(iw_pass_total)
print(round(iw_pass_total/iw_total_tested, 2))
print("IW FAIL")
print(iw_fail_total)
print(round(iw_fail_total/iw_total_tested,2))
print("IW TOTAL TESTED")
print(iw_total_tested)

# DOA RMA pass/fail totals
DOA_data = RMA_bulk_data[RMA_bulk_data.CUSTOMER_PO == "RMA-DOA"]
DOA_pass = DOA_data[DOA_data["TEST RESULT"] == "PASS"]
DOA_fail = DOA_data[DOA_data["TEST RESULT"] == "FAIL"]
doa_pass_total = len(DOA_pass.index)
doa_fail_total = len(DOA_fail.index)
doa_total_tested = doa_pass_total + doa_fail_total
print("--------")
print("DOA TOTAL GENERATED")
print(len(DOA_data.index))
print("DOA PASS")
print(doa_pass_total)
print(round(doa_pass_total/doa_total_tested,2))
print("DOA FAIL")
print(doa_fail_total)
print(round(doa_fail_total/doa_total_tested,2))
print("DOA TOTAL TESTED")
print(doa_total_tested)
 
# Individual RMA pass/fail totals
RMA_Indiv_data = RMA_bulk_data[TMO_bulk_data.CUSTOMER_PO == "RMA-Manual"]
RMA_Indiv_pass = RMA_Indiv_data[TMO_Indiv_data["TEST RESULT"] == "PASS"]
print("--------")
print("RMA INDIV PASS")
print(len(RMA_Indiv_pass.index))
RMA_Indiv_fail = RMA_Indiv_data[RMA_Indiv_data["TEST RESULT"] == "FAIL"]
print("RMA INDIV FAIL")
print(len(RMA_Indiv_fail.index))
print("RMA INDIV TOTAL TESTED")
print(len(RMA_Indiv_pass.index)+len(RMA_Indiv_fail.index))
 
# Monthly In Warranty pass/fail totals
IW_pass_monthly = IW_pass[IW_pass["RMA Received Date"].dt.month == 10]
IW_fail_monthly = IW_fail[IW_fail["RMA Received Date"].dt.month == 10]
print("--------")
print("OCT 2021 IW PASS")
print(len(IW_pass_monthly.index))
print("OCT 2021 IW FAIL")
print(len(IW_fail_monthly.index))
print("OCT 2021 IW TOTAL TESTED")
print(len(IW_pass_monthly.index)+len(IW_fail_monthly.index))

# Monthly pass/fail totals
pass_all_total = TMO_bulk_data[RMA_bulk_data["TEST RESULT"] == "PASS"]
fail_all_total = TMO_bulk_data[RMA_bulk_data["TEST RESULT"] == "FAIL"]
pass_all_monthly = pass_all_total[pass_all_total["RMA Received Date"].dt.month == 10]
fail_all_monthly = fail_all_total[fail_all_total["RMA Received Date"].dt.month == 10]
print("--------")
print("OCT 2021 TOTAL PASS")
print(len(pass_all_monthly.index))
print("OCT 2021 TOTAL FAIL")
print(len(fail_all_monthly.index))
print("OCT 2021 TOTAL TESTED")
print(len(pass_all_monthly.index)+len(fail_all_monthly.index))
