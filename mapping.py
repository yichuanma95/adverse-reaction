def get_custom_mapping(cls):
    mapping = {
        "ver_no": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "latest_date_received": {
            "type": "date"
        },
        "initial_date_received": {
            "type": "date"
        },
        "mah_no": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "report_type_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "gender_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "age": {
            "type": "float"
        },
        "age_yrs": {
            "type": "float"
        },
        "age_unit_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "outcome_en": {
            "type": "text"
        },
        "weight": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "weight_unit_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "height": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "height_unit_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "seriousness_en": {
            "type": "text"
        },
        "death": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "disability": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "congenital_anomaly": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "life_threatening": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "hosp_required": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "other_medically_imp_cond": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "reporter_type_en": {
            "type": "text"
        },
        "source_en": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "e2b_safetyreport_id": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "authority_num": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "company_num": {
            "normalizer": "keyword_lowercase_normalizer",
            "type": "keyword"
        },
        "drugs": {
            "properties": {
                "drug_product_id": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "drug_role_en": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "dose_qty": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "frequency": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "freq_time": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "therapy_dur": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "therapy_dur_unit_en": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "freq_time_en": {
                    "type": "text"
                },
                "freq_unit_en": {
                    "type": "text"
                },
                "drug_name": {
                    "type": "text"
                },
                "route_admin_en": {
                    "type": "text"
                },
                "dose_unit_en": {
                    "type": "text"
                },
                "dosage_form_en": {
                    "type": "text"
                }
            }
        },
        "reactions": {
            "properties": {
                "duration": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "duration_unit_en": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "meddra_ver": {
                    "normalizer": "keyword_lowercase_normalizer",
                    "type": "keyword"
                },
                "reaction_term_en": {
                    "type": "text"
                },
                "soc_en": {
                    "type": "text"
                }
            }
        }
    }
    return mapping
