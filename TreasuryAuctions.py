import pandas as pd
import treasury_gov_pandas
from bokeh.plotting import figure, show
from bokeh.models   import NumeralTickFormatter, HoverTool

df = treasury_gov_pandas.update_records(
        'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query')
print("back here")

df['record_date']   = pd.to_datetime(df['record_date'])
df['issue_date']    = pd.to_datetime(df['issue_date']) 
df['maturity_date'] = pd.to_datetime(df['maturity_date'])
df['auction_date']  = pd.to_datetime(df['auction_date'])

df['total_accepted'] = pd.to_numeric(df['total_accepted'], errors='coerce')
df['total_tendered'] = pd.to_numeric(df['total_tendered'], errors='coerce')
# ----------------------------------------------------------------------
bills = df[df['security_type'] == 'Bill']
notes = df[df['security_type'] == 'Note']
bonds = df[df['security_type'] == 'Bond']
# ----------------------------------------------------------------------
# x_column = 'record_date'
x_column = 'auction_date'
y_column = 'total_accepted'
# y_column = 'total_tendered'

df.to_csv(r'C:\Users\Vikas\Desktop\DAPPTEST\demo-apps\Treasury\data.csv', index=False)


p = figure(title='Treasury Securities Auctions Data', sizing_mode='stretch_both', x_axis_type='datetime', x_axis_label=x_column, y_axis_label=y_column)

# ----------------------------------------------------------------------
p.circle(x=bills[x_column], y=bills[y_column], color='red',   legend_label='Bills')
p.circle(x=notes[x_column], y=notes[y_column], color='green', legend_label='Notes')
p.circle(x=bonds[x_column], y=bonds[y_column], color='blue',  legend_label='Bonds')

p.yaxis.formatter = NumeralTickFormatter(format='$0a')

p.add_tools(HoverTool(tooltips=[('Date', '@x{%F}'), ('Total Accepted', '@y{$0.0a}')], formatters={'@x': 'datetime'}))

p.legend.click_policy = 'hide'

show(p)


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# record_date                               1979-11-15
# cusip                                      912810CK2
# security_type                                   Bond
# security_term                                30-Year
# auction_date                              1979-11-01
# issue_date                                1979-11-15
# maturity_date                             2009-11-15
# price_per100                                    null
# accrued_int_per100                              null
# accrued_int_per1000                            0E-10
# adj_accrued_int_per1000                         null
# adj_price                                       null
# allocation_pctage                          44.000000
# allocation_pctage_decimals                         0
# announcemtd_cusip                               null
# announcemt_date                           1979-10-24
# auction_format                           Multi-Price
# avg_med_discnt_rate                             null
# avg_med_investment_rate                         null
# avg_med_price                                 99.407
# avg_med_discnt_margin                           null
# avg_med_yield                              10.440000
# back_dated                                        No
# back_dated_date                                 null
# bid_to_cover_ratio                              null
# callable                                         Yes
# call_date                                 2004-11-15
# called_date                                     null
# cash_management_bill_cmb                          No
# closing_time_comp                               null
# closing_time_noncomp                            null
# comp_accepted                                   null
# comp_bid_decimals                                  2
# comp_tendered                                   null
# comp_tenders_accepted                           null
# corpus_cusip                                    null
# cpi_base_reference_period                       null
# currently_outstanding                           null
# dated_date                                      null
# direct_bidder_accepted                          null
# direct_bidder_tendered                          null
# est_pub_held_mat_by_type_amt                    null
# fima_included                                   null
# fima_noncomp_accepted                           null
# fima_noncomp_tendered                           null
# first_int_period                              Normal
# first_int_payment_date                    1980-05-15
# floating_rate                                     No
# frn_index_determination_date                    null
# frn_index_determination_rate                    null
# high_discnt_rate                                null
# high_investment_rate                            null
# high_price                                    99.045
# high_discnt_margin                              null
# high_yield                                   10.4800
# index_ratio_on_issue_date                       null
# indirect_bidder_accepted                        null
# indirect_bidder_tendered                        null
# int_payment_frequency                    Semi-Annual
# int_rate                                   10.375000
# low_discnt_rate                                 null
# low_investment_rate                             null
# low_price                                     99.863
# low_discnt_margin                               null
# low_yield                                  10.390000
# mat_date                                        null
# max_comp_award                                  null
# max_noncomp_award                               null
# max_single_bid                                  null
# min_bid_amt                                     null
# min_strip_amt                                   null
# min_to_issue                                    null
# multiples_to_bid                                null
# multiples_to_issue                              null
# nlp_exclusion_amt                               null
# nlp_reporting_threshold                         null
# noncomp_accepted                                null
# noncomp_tenders_accepted                        null
# offering_amt                              2000000000
# original_cusip                                  null
# original_dated_date                             null
# original_issue_date                             null
# original_security_term                       30-Year
# pdf_filenm_announcemt                           null
# pdf_filenm_comp_results                         null
# pdf_filenm_noncomp_results                      null
# primary_dealer_accepted                         null
# primary_dealer_tendered                         null
# ref_cpi_on_dated_date                           null
# ref_cpi_on_issue_date                           null
# reopening                                         No
# security_term_day_month                      0-Month
# security_term_week_year                      30-Year
# series                            Bonds of 2004-2009
# soma_accepted                                   null
# soma_holdings                                   null
# soma_included                                   null
# soma_tendered                                   null
# spread                                          null
# std_int_payment_per1000                      51.8750
# strippable                                      null
# tiin_conversion_factor_per1000                  null
# tips                                              No
# total_accepted                            2315000000
# total_tendered                            3594000000
# treas_retail_accepted                           null
# treas_retail_tenders_accepted                   null
# unadj_accrued_int_per1000                       null
# unadj_price                                     null
# xml_filenm_announcemt                           null
# xml_filenm_comp_results                         null
# inflation_index_security                        null
# tint_cusip_1                                    null
# tint_cusip_2                                    null