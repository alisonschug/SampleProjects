#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:12:08 2022

@author: alisonschug
""" 

#%%
#import modules

import pandas as pd
import os
import statistics as sts

#%%

os.chdir('/Users/alisonschug/Documents/PhD/CSL/ABCD/Big_v2')

#%%
#read csv and assign column headers

#column_headers = ['subjectkey', 'id_event', 'interview_age', 'sex', 'eventname', 'MPRAGE', 'demo_nat_lang_l', 'demo_nat_lang_2_l', 'demo_dual_lang_v2_l', 'demo_dual_lang_years_p___1', 'demo_dual_lang_years_p___2', 'demo_dual_lang_years_p___3', 'demo_dual_lang_years_p___4', 'demo_dual_lang_years_p___5', 'demo_dual_lang_years_p___6', 'demo_dual_lang_years_p___7', 'demo_dual_lang_years_p___8', 'demo_dual_lang_years_p___9', 'demo_dual_lang_years_p___10', 'demo_prnt_nat_lang_l', 'demo_prnt_nat_lang_2_l', 'demo_prnt_ed_v2_l', 'demo_prnt_income_v2_l', 'demo_prtnr_ed_v2_l', 'demo_prtnr_income_v2_l', 'demo_comb_income_v2_l', 'pea_wiscv_tss', 'nihtbx_picvocab_agecorrected', 'nihtbx_flanker_agecorrected', 'nihtbx_list_agecorrected', 'nihtbx_reading_agecorrected', 'accult_q1_y', 'accult_q2_y', 'accult_q3_dropdwn_y', 'accult_q3_other_y', 'accult_q4_y', 'accult_q5_y', 'accult_q3b', 'demo_race_a_p___10_BASELINE', 'demo_race_a_p___11_BASELINE', 'demo_race_a_p___12_BASELINE', 'demo_race_a_p___13_BASELINE', 'demo_race_a_p___14_BASELINE', 'demo_race_a_p___15_BASELINE', 'demo_race_a_p___16_BASELINE', 'demo_race_a_p___17_BASELINE', 'demo_race_a_p___18_BASELINE', 'demo_race_a_p___19_BASELINE', 'demo_race_a_p___20_BASELINE', 'demo_race_a_p___21_BASELINE', 'demo_race_a_p___22_BASELINE', 'demo_race_a_p___23_BASELINE', 'demo_race_a_p___24_BASELINE', 'demo_race_a_p___25_BASELINE', 'demo_race_a_p___77_BASELINE', 'demo_race_a_p___99_BASELINE', 'demo_race_notes_v2_BASELINE', 'demo_ethn_v2_BASELINE', 'demo_origin_v2_BASELINE', 'demo_years_us_v2_BASELINE', 'demo_prnt_ed_v2_BASELINE', 'demo_prnt_income_v2_BASELINE', 'demo_prtnr_ed_v2_BASELINE', 'demo_prtnr_income_v2_BASELINE', 'demo_comb_income_v2_BASELINE']


abcd = pd.read_csv('All_ABCD_DATA.csv', header = 0)

#%%

#  Goals to identify participants
#All Groups
# 0 - (B) Keep only baseline data (will pull in later time point data at the end)
# 1 - (M) Keep only matrix reasoning > 7 at baseline (Remove Below 8 (25 percentile according to link))
# 2 - (P) Keep only picture vocab > 69 at baseline (anything lower is a sign of a different problem)

#Reading Groups
# 3RD - (RD) Keep < 85 on ORRT
# 3Con - (Con) Keep > 89 on ORRT

# Bilinguals
# 4B - (Bi) Identify participants who report "yes" to "do you speak a langauge other than English?" at baseline and 2 year follow-up
# 5B - (L) Identify those who reported their L2 at baseline & 2-year follow-up
# 6B - (H) Identify those that respond 1= always other language, 2 = mostly other language, or 3 = English and other language equally (kept because this still could be itdentifying early bilinguals even if they are not necessarily cultural bilinguals such as one-parent-one-language houses) for question about "which language do you speak with your family" at 2 year follow-up
# 7B - (E) Include only Hispanic bilinguals


# Monolinguals
# 4M - (Mono) Identify participants who report "no" to "do you speak a langauge other than English?" at baseline and 2 year follow-up
# 5M - (N) Parent responds "English" to "what is your child's native language?" at 2-year follow-up

# All Groups
# 7 - (S) Keep only those with MPRAGE

#%%
# 0 - (B) Keep only baseline data (will pull in later time point data at the end)

B_abcd = abcd[(abcd['eventname'] == 'baseline_year_1_arm_1')]

#%%
#1 - (M) Keep only matrix reasoning > 7 at baseline (Remove Below 8 (25 percentile according to link))

BM_abcd = B_abcd[(B_abcd['pea_wiscv_tss'] != 888) & (B_abcd['pea_wiscv_tss'] > 7)]

#%%
# 2 - (P) Keep only picture vocab > 69 at baseline (anything lower is a sign of a different problem)

BMP_abcd = BM_abcd[(BM_abcd['nihtbx_picvocab_agecorrected'] != 888) & (BM_abcd['nihtbx_picvocab_agecorrected'] >= 70)]

#%%
# 3RD - (RD) Keep < 85 on ORRT

BMP_RD = BMP_abcd[(BMP_abcd['nihtbx_reading_agecorrected'] < 85)]


#%%
# 3Con - (Con) Keep > 89 on ORRT

BMP_Con = BMP_abcd[(BMP_abcd['nihtbx_reading_agecorrected'] > 89) & (BMP_abcd['nihtbx_reading_agecorrected'] != 888)]

#%%
# 4B - (Bi) Identify participants who report "yes" to "do you speak a langauge other than English?" at baseline 

BMP_RD_Bi = BMP_RD[(BMP_RD['accult_q2_y'] == 1)]

BMP_Con_Bi = BMP_Con[(BMP_Con['accult_q2_y'] == 1)]


#%%
# 5B - (L) Identify those who reported their L2 as Spanish at baseline 

BMP_RD_Bi_L = BMP_RD_Bi[(BMP_RD_Bi['accult_q3_dropdwn_y'] == 47)]

BMP_Con_Bi_L = BMP_Con_Bi[(BMP_Con_Bi['accult_q3_dropdwn_y'] == 47)]


#%%

# 6B - (H) Identify those that respond 1= always other language, 2 = mostly other language, or 3 = English and other language equally (kept because this still could be itdentifying early bilinguals even if they are not necessarily cultural bilinguals such as one-parent-one-language houses) for question about "which language do you speak with your family" at baseline

# 1= always other language
# 2 = mostly other language
# 3 = English and other language equally (kept because this still could be itdentifying early bilinguals even if they are not necessarily cultural bilinguals such as one-parent-one-language houses)
q5_range = [1, 2, 3]

BMP_RD_Bi_LH = BMP_RD_Bi_L[(BMP_RD_Bi_L['accult_q5_y'].isin(q5_range))]

BMP_Con_Bi_LH = BMP_Con_Bi_L[(BMP_Con_Bi_L['accult_q5_y'].isin(q5_range))]

#%%

#7B - (E) Include only Hispanic bilinguals

BMP_RD_Bi_LHE = BMP_RD_Bi_LH[(BMP_RD_Bi_LH['demo_ethn_v2'] == 1)]

BMP_Con_Bi_LHE = BMP_Con_Bi_LH[(BMP_Con_Bi_LH['demo_ethn_v2'] == 1)]

#%%
# 4M - (Mono) Identify participants who report "no" to "do you speak a langauge other than English?" at baseline 

BMP_RD_Mono = BMP_RD[(BMP_RD['accult_q2_y'] == 0)]

BMP_Con_Mono = BMP_Con[(BMP_Con['accult_q2_y'] == 0)]

#%%
#5M - One_abcd = all particpants at the 1 year follow-up time point 


One_abcd = abcd[(abcd['eventname'] == '1_year_follow_up_y_arm_1')]


#%%
# 6M - (N) Parent responds "English" to "what is your child's native language?" at one year

One_N = One_abcd[(One_abcd['demo_nat_lang_l'] == 58)]['subjectkey']

BMP_RD_Mono_N = BMP_RD_Mono[(BMP_RD_Mono['subjectkey'].isin(One_N))]

BMP_Con_Mono_N = BMP_Con_Mono[(BMP_Con_Mono['subjectkey'].isin(One_N))]

#%%
# 7 - (S) Keep only those with MPRAGE

BMP_RD_Bi_LHES = BMP_RD_Bi_LHE[(BMP_RD_Bi_LHE['MPRAGE'] == 'yes')]

BMP_Con_Bi_LHES = BMP_Con_Bi_LHE[(BMP_Con_Bi_LHE['MPRAGE'] == 'yes')]

BMP_RD_Mono_NS = BMP_RD_Mono_N[(BMP_RD_Mono_N['MPRAGE'] == 'yes')]

BMP_Con_Mono_NS = BMP_Con_Mono_N[(BMP_Con_Mono_N['MPRAGE'] == 'yes')]


#%%

BMP_RD_Bi_LHES.insert(2,'Group','Bi_RD')
BMP_Con_Bi_LHES.insert(2,'Group','Bi_Con')

BMP_RD_Mono_NS.insert(2,'Group','Mono_RD')
BMP_Con_Mono_NS.insert(2,'Group','Mono_Con')

#%%

BMP_RD_Bi_LHES.insert(3,'Treatment', 1)
BMP_Con_Bi_LHES.insert(3,'Treatment', 0)

BMP_RD_Mono_NS.insert(3,'Treatment', 0)
BMP_Con_Mono_NS.insert(3,'Treatment', 0)



#%%

#Concatonate DFs for Propensity Score Matching

RD_bi_RD_mono_df = pd.concat([BMP_RD_Bi_LHES, BMP_RD_Mono_NS])

RD_bi_Con_mono_df = pd.concat([BMP_RD_Bi_LHES, BMP_Con_Mono_NS])

RD_bi_Con_bi_df = pd.concat([BMP_RD_Bi_LHES, BMP_Con_Bi_LHES])



#%%
from psmpy import PsmPy


psm_RD_bi_RD_mono = PsmPy(RD_bi_RD_mono_df, treatment='Treatment', indx='subjectkey', exclude = ['id_event', 'Group', 'interview_age', 'sex', 'eventname', 'MPRAGE', 'demo_nat_lang_l', 'demo_nat_lang_2_l', 'demo_dual_lang_v2_l', 'demo_dual_lang_years_p___1', 'demo_dual_lang_years_p___2', 'demo_dual_lang_years_p___3', 'demo_dual_lang_years_p___4', 'demo_dual_lang_years_p___5', 'demo_dual_lang_years_p___6', 'demo_dual_lang_years_p___7', 'demo_dual_lang_years_p___8', 'demo_dual_lang_years_p___9', 'demo_dual_lang_years_p___10', 'demo_prnt_nat_lang_l', 'demo_prnt_nat_lang_2_l', 'demo_prnt_ed_v2_l', 'demo_prnt_income_v2_l', 'demo_prtnr_ed_v2_l', 'demo_prtnr_income_v2_l', 'demo_comb_income_v2_l', 'nihtbx_picvocab_agecorrected', 'nihtbx_flanker_agecorrected', 'nihtbx_list_agecorrected', 'nihtbx_reading_agecorrected', 'accult_q1_y', 'accult_q2_y', 'accult_q3_dropdwn_y', 'accult_q3_other_y', 'accult_q4_y', 'accult_q5_y', 'accult_q3b', 'demo_race_a_p___10', 'demo_race_a_p___11', 'demo_race_a_p___12', 'demo_race_a_p___13', 'demo_race_a_p___14', 'demo_race_a_p___15', 'demo_race_a_p___16', 'demo_race_a_p___17', 'demo_race_a_p___18', 'demo_race_a_p___19', 'demo_race_a_p___20', 'demo_race_a_p___21', 'demo_race_a_p___22', 'demo_race_a_p___23', 'demo_race_a_p___24', 'demo_race_a_p___25', 'demo_race_a_p___77', 'demo_race_a_p___99', 'demo_race_notes_v2', 'demo_ethn_v2', 'demo_origin_v2', 'demo_years_us_v2', 'demo_prnt_ed_v2', 'demo_prnt_income_v2', 'demo_prtnr_ed_v2', 'demo_prtnr_income_v2'])
psm_RD_bi_RD_mono.logistic_ps(balance = False)
psm_RD_bi_RD_mono.predicted_data
psm_RD_bi_RD_mono.knn_matched(matcher='propensity_logit', replacement=False, caliper=None)
psm_RD_bi_RD_mono_df = psm_RD_bi_RD_mono.df_matched


psm_RD_bi_Con_mono = PsmPy(RD_bi_Con_mono_df, treatment='Treatment', indx='subjectkey', exclude = ['id_event', 'Group', 'interview_age', 'sex', 'eventname', 'MPRAGE', 'demo_nat_lang_l', 'demo_nat_lang_2_l', 'demo_dual_lang_v2_l', 'demo_dual_lang_years_p___1', 'demo_dual_lang_years_p___2', 'demo_dual_lang_years_p___3', 'demo_dual_lang_years_p___4', 'demo_dual_lang_years_p___5', 'demo_dual_lang_years_p___6', 'demo_dual_lang_years_p___7', 'demo_dual_lang_years_p___8', 'demo_dual_lang_years_p___9', 'demo_dual_lang_years_p___10', 'demo_prnt_nat_lang_l', 'demo_prnt_nat_lang_2_l', 'demo_prnt_ed_v2_l', 'demo_prnt_income_v2_l', 'demo_prtnr_ed_v2_l', 'demo_prtnr_income_v2_l', 'demo_comb_income_v2_l', 'nihtbx_picvocab_agecorrected', 'nihtbx_flanker_agecorrected', 'nihtbx_list_agecorrected', 'nihtbx_reading_agecorrected', 'accult_q1_y', 'accult_q2_y', 'accult_q3_dropdwn_y', 'accult_q3_other_y', 'accult_q4_y', 'accult_q5_y', 'accult_q3b', 'demo_race_a_p___10', 'demo_race_a_p___11', 'demo_race_a_p___12', 'demo_race_a_p___13', 'demo_race_a_p___14', 'demo_race_a_p___15', 'demo_race_a_p___16', 'demo_race_a_p___17', 'demo_race_a_p___18', 'demo_race_a_p___19', 'demo_race_a_p___20', 'demo_race_a_p___21', 'demo_race_a_p___22', 'demo_race_a_p___23', 'demo_race_a_p___24', 'demo_race_a_p___25', 'demo_race_a_p___77', 'demo_race_a_p___99', 'demo_race_notes_v2', 'demo_ethn_v2', 'demo_origin_v2', 'demo_years_us_v2', 'demo_prnt_ed_v2', 'demo_prnt_income_v2', 'demo_prtnr_ed_v2', 'demo_prtnr_income_v2'])
psm_RD_bi_Con_mono.logistic_ps(balance = False)
psm_RD_bi_Con_mono.predicted_data
psm_RD_bi_Con_mono.knn_matched(matcher='propensity_logit', replacement=False, caliper=None)
psm_RD_bi_Con_mono_df = psm_RD_bi_Con_mono.df_matched


psm_RD_bi_Con_bi = PsmPy(RD_bi_Con_bi_df, treatment='Treatment', indx='subjectkey', exclude = ['id_event', 'Group', 'interview_age', 'sex', 'eventname', 'MPRAGE', 'demo_nat_lang_l', 'demo_nat_lang_2_l', 'demo_dual_lang_v2_l', 'demo_dual_lang_years_p___1', 'demo_dual_lang_years_p___2', 'demo_dual_lang_years_p___3', 'demo_dual_lang_years_p___4', 'demo_dual_lang_years_p___5', 'demo_dual_lang_years_p___6', 'demo_dual_lang_years_p___7', 'demo_dual_lang_years_p___8', 'demo_dual_lang_years_p___9', 'demo_dual_lang_years_p___10', 'demo_prnt_nat_lang_l', 'demo_prnt_nat_lang_2_l', 'demo_prnt_ed_v2_l', 'demo_prnt_income_v2_l', 'demo_prtnr_ed_v2_l', 'demo_prtnr_income_v2_l', 'demo_comb_income_v2_l', 'nihtbx_picvocab_agecorrected', 'nihtbx_flanker_agecorrected', 'nihtbx_list_agecorrected', 'nihtbx_reading_agecorrected', 'accult_q1_y', 'accult_q2_y', 'accult_q3_dropdwn_y', 'accult_q3_other_y', 'accult_q4_y', 'accult_q5_y', 'accult_q3b', 'demo_race_a_p___10', 'demo_race_a_p___11', 'demo_race_a_p___12', 'demo_race_a_p___13', 'demo_race_a_p___14', 'demo_race_a_p___15', 'demo_race_a_p___16', 'demo_race_a_p___17', 'demo_race_a_p___18', 'demo_race_a_p___19', 'demo_race_a_p___20', 'demo_race_a_p___21', 'demo_race_a_p___22', 'demo_race_a_p___23', 'demo_race_a_p___24', 'demo_race_a_p___25', 'demo_race_a_p___77', 'demo_race_a_p___99', 'demo_race_notes_v2', 'demo_ethn_v2', 'demo_origin_v2', 'demo_years_us_v2', 'demo_prnt_ed_v2', 'demo_prnt_income_v2', 'demo_prtnr_ed_v2', 'demo_prtnr_income_v2'])
psm_RD_bi_Con_bi.logistic_ps(balance = False)
psm_RD_bi_Con_bi.predicted_data
psm_RD_bi_Con_bi.knn_matched(matcher = 'propensity_logit', replacement = False, caliper = None)
psm_RD_bi_Con_bi_df = psm_RD_bi_Con_bi.df_matched


#%%

RD_bi_Matched_ID = psm_RD_bi_RD_mono_df[psm_RD_bi_RD_mono_df['Treatment'] == 1]['subjectkey']
RD_mono_Matched_ID = psm_RD_bi_RD_mono_df[psm_RD_bi_RD_mono_df['Treatment'] == 0]['subjectkey']
Con_mono_Matched_ID = psm_RD_bi_Con_mono_df[psm_RD_bi_Con_mono_df['Treatment'] == 0]['subjectkey']
Con_bi_Matched_ID = psm_RD_bi_Con_bi_df[psm_RD_bi_Con_bi_df['Treatment'] == 0]['subjectkey']

#%%

RD_bi_Matched = BMP_RD_Bi_LHES[BMP_RD_Bi_LHES['subjectkey'].isin(RD_bi_Matched_ID)]
RD_mono_Matched = BMP_RD_Mono_NS[BMP_RD_Mono_NS['subjectkey'].isin(RD_mono_Matched_ID)]
Con_bi_Matched = BMP_Con_Bi_LHES[BMP_Con_Bi_LHES['subjectkey'].isin(Con_bi_Matched_ID)]
Con_mono_Matched = BMP_Con_Mono_NS[BMP_Con_Mono_NS['subjectkey'].isin(Con_mono_Matched_ID)]

#%%

RD_bi_Matched .insert(4,'Reading', 'RD')
Con_bi_Matched.insert(4,'Reading', 'Con')

RD_mono_Matched.insert(4,'Reading', 'RD')
Con_mono_Matched.insert(4,'Reading', 'Con')

#%%

RD_bi_Matched .insert(5,'Language', 'Bi')
Con_bi_Matched.insert(5,'Language', 'Bi')

RD_mono_Matched.insert(5,'Language', 'Mono')
Con_mono_Matched.insert(5,'Language', 'Mono')

#%%

Big_v3_Matched = pd.concat([RD_bi_Matched, RD_mono_Matched, Con_bi_Matched, Con_mono_Matched])


#%%

#write csv file

Big_v3_Matched.to_csv('Big_v3.2_Matched.csv')

#%%

import statsmodels.api as sm
from statsmodels.formula.api import ols

#perform two-way ANOVA
SES_ANOVA = ols('demo_comb_income_v2 ~ C(Reading) + C(Language) + C(Reading):C(Language)', data=Big_v3_Matched).fit()
SES_ANOVA_table = sm.stats.anova_lm(SES_ANOVA, typ=2)
print('\n SES')
print(SES_ANOVA_table)

Age_ANOVA = ols('interview_age ~ C(Reading) + C(Language) + C(Reading):C(Language)', data=Big_v3_Matched).fit()
Age_ANOVA_table = sm.stats.anova_lm(Age_ANOVA, typ=2)
print('\n \n Age')
print(Age_ANOVA_table)

Matrix_ANOVA = ols('pea_wiscv_tss ~ C(Reading) + C(Language) + C(Reading):C(Language)', data=Big_v3_Matched).fit()
Matrix_ANOVA_table = sm.stats.anova_lm(Matrix_ANOVA, typ=2)
print('\n \n Matrix')
print(Matrix_ANOVA_table)

Vocab_ANOVA = ols('nihtbx_picvocab_agecorrected ~ C(Reading) + C(Language) + C(Reading):C(Language)', data=Big_v3_Matched).fit()
Vocab_ANOVA_table = sm.stats.anova_lm(Vocab_ANOVA, typ=2)
print('\n \n Vocab')
print(Vocab_ANOVA_table)

Reading_ANOVA = ols('nihtbx_reading_agecorrected ~ C(Reading) + C(Language) + C(Reading):C(Language)', data=Big_v3_Matched).fit()
Reading_ANOVA_table = sm.stats.anova_lm(Reading_ANOVA, typ=2)
print('\n \n Reading')
print(Reading_ANOVA_table)


#%%

Bi_RD_Age_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['interview_age']), 2)
Bi_Con_Age_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['interview_age']), 2)
Mono_RD_Age_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['interview_age']),2)
Mono_Con_Age_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['interview_age']),2)

Bi_RD_Age_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['interview_age']), 2)
Bi_Con_Age_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['interview_age']), 2)
Mono_RD_Age_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['interview_age']),2)
Mono_Con_Age_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['interview_age']),2)


Bi_RD_Matrix_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['pea_wiscv_tss']), 2)
Bi_Con_Matrix_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['pea_wiscv_tss']), 2)
Mono_RD_Matrix_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['pea_wiscv_tss']),2)
Mono_Con_Matrix_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['pea_wiscv_tss']),2)

Bi_RD_Matrix_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['pea_wiscv_tss']), 2)
Bi_Con_Matrix_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['pea_wiscv_tss']), 2)
Mono_RD_Matrix_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['pea_wiscv_tss']),2)
Mono_Con_Matrix_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['pea_wiscv_tss']),2)


Bi_RD_Vocab_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['nihtbx_picvocab_agecorrected']), 2)
Bi_Con_Vocab_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['nihtbx_picvocab_agecorrected']), 2)
Mono_RD_Vocab_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['nihtbx_picvocab_agecorrected']),2)
Mono_Con_Vocab_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['nihtbx_picvocab_agecorrected']),2)

Bi_RD_Vocab_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['nihtbx_picvocab_agecorrected']), 2)
Bi_Con_Vocab_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['nihtbx_picvocab_agecorrected']), 2)
Mono_RD_Vocab_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['nihtbx_picvocab_agecorrected']),2)
Mono_Con_Vocab_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['nihtbx_picvocab_agecorrected']),2)


Bi_RD_Reading_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['nihtbx_reading_agecorrected']), 2)
Bi_Con_Reading_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['nihtbx_reading_agecorrected']), 2)
Mono_RD_Reading_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['nihtbx_reading_agecorrected']),2)
Mono_Con_Reading_AVG = round(sts.mean(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['nihtbx_reading_agecorrected']),2)

Bi_RD_Reading_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_RD']['nihtbx_reading_agecorrected']), 2)
Bi_Con_Reading_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Bi_Con']['nihtbx_reading_agecorrected']), 2)
Mono_RD_Reading_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_RD']['nihtbx_reading_agecorrected']),2)
Mono_Con_Reading_STDEV = round(sts.stdev(Big_v3_Matched[Big_v3_Matched['Group'] == 'Mono_Con']['nihtbx_reading_agecorrected']),2)


