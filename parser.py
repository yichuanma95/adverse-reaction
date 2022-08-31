import os
import datetime

from biothings.utils.common import open_anyfile

def load_data(data_folder):
    zipfile = os.path.join(data_folder, 'extract_extrait.zip')
    assert os.path.exists(zipfile)

    reportfile = os.path.join('cvponline_extract_20220430', 'reports.txt')
    reportcols = \
        ['report_id', '_id', 'ver_no', 'latest_date_received', 'initial_date_received', 'mah_no', 'report_type_code',
         'report_type_en', 'report_type_fr', 'gender_code', 'gender_en', 'gender_fr', 'age', 'age_yrs', 'age_unit_en',
         'age_unit_fr', 'outcome_code', 'outcome_en', 'outcome_fr', 'weight', 'weight_unit_en', 'weight_unit_fr',
         'height', 'height_unit_en', 'height_unit_fr', 'seriousness_code', 'seriousness_en', 'seriousness_fr',
         'death', 'disability', 'congenital_anomaly', 'life_threatening', 'hosp_required', 'other_medically_imp_cond',
         'reporter_type_en', 'reporter_type_fr', 'source_code', 'source_en', 'source_fr', 'e2b_safetyreport_id',
         'authority_num', 'company_num']
    reports = {}
    with open_anyfile((zipfile, reportfile)) as f:
        for line in f:
            datapoint = line.rstrip('\n').split('$')
            for i in range(len(datapoint)):
                datapoint[i] = datapoint[i].strip('\"')
            obj = {col: d for col, d in zip(reportcols, datapoint)}
            if obj['latest_date_received'] == '' or obj['initial_date_received'] == '' or obj['seriousness_en'] == ''\
                or obj['source_en'] == '' or obj['gender_en'] == '' or obj['outcome_en'] == '' or obj['age'] == ''\
                    or obj['age_yrs'] == '':
                continue
            id = obj.pop('report_id')
            del obj['report_type_code']
            del obj['report_type_fr']
            del obj['gender_code']
            del obj['gender_fr']
            del obj['age_unit_fr']
            del obj['outcome_code']
            del obj['outcome_fr']
            del obj['weight_unit_fr']
            del obj['height_unit_fr']
            del obj['seriousness_code']
            del obj['seriousness_fr']
            del obj['reporter_type_fr']
            del obj['source_code']
            del obj['source_fr']
            obj['age'] = int(obj['age'])
            obj['age_yrs'] = float(obj['age_yrs'])
            obj['drugs'] = []
            obj['reactions'] = []
            reports[id] = obj

            # limit data to 1000 documents
            if len(reports) == 1000:
                break

    drugfile = os.path.join('cvponline_extract_20220430', 'report_drug.txt')
    drugcols = \
        ['report_drug_id', 'report_id', 'drug_product_id', 'drug_name', 'drug_role_en', 'drug_role_fr',
         'route_admin_en', 'route_admin_fr', 'dose_qty', 'dose_unit_en', 'dose_unit_fr', 'frequency', 'freq_time',
         'freq_time_en', 'freq_time_fr', 'freq_unit_en', 'freq_unit_fr', 'therapy_dur', 'therapy_dur_unit_en',
         'therapy_dur_unit_fr', 'dosage_form_en', 'dosage_form_fr']
    with open_anyfile((zipfile, drugfile)) as f:
        for line in f:
            datapoint = line.rstrip('\n').split('$')
            for i in range(len(datapoint)):
                datapoint[i] = datapoint[i].strip('\"')
            obj = {col: d for col, d in zip(drugcols, datapoint)}
            del obj['report_drug_id']
            id = obj.pop('report_id')
            if id not in reports:
                continue
            del obj['drug_role_fr']
            del obj['route_admin_fr']
            del obj['dose_unit_fr']
            del obj['freq_time_fr']
            del obj['freq_unit_fr']
            del obj['therapy_dur_unit_fr']
            del obj['dosage_form_fr']
            reports[id]['drugs'].append(obj)

    reactionfile = os.path.join('cvponline_extract_20220430', 'reactions.txt')
    reactioncols = \
        ['reaction_id', 'report_id', 'duration', 'duration_unit_en', 'duration_unit_fr', 'reaction_term_en',
         'reaction_term_fr', 'soc_en', 'soc_fr', 'meddra_ver']
    with open_anyfile((zipfile, reactionfile)) as f:
        for line in f:
            datapoint = line.rstrip('\n').split('$')
            for i in range(len(datapoint)):
                datapoint[i] = datapoint[i].strip('\"')
            obj = {col: d for col, d in zip(reactioncols, datapoint)}
            del obj['reaction_id']
            id = obj.pop('report_id')
            if id not in reports:
                continue
            del obj['duration_unit_fr']
            del obj['reaction_term_fr']
            del obj['soc_fr']
            reports[id]['reactions'].append(obj)

    for report in reports.values():
        yield report
