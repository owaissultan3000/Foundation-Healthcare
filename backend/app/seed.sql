INSERT INTO diagnosis_codes (code, description) VALUES
-- Infectious diseases (A)
('A00', 'Cholera'),
('A01', 'Typhoid and paratyphoid fevers'),
('A01.0', 'Typhoid fever'),
('A02', 'Other salmonella infections'),
('A03', 'Shigellosis'),
('A04', 'Other bacterial intestinal infections'),
('A09', 'Infectious gastroenteritis and colitis'),
('A15', 'Respiratory tuberculosis'),
('A41', 'Sepsis'),
('A41.9', 'Sepsis, unspecified organism'),

-- Neoplasms (C)
('C16', 'Malignant neoplasm of stomach'),
('C16.9', 'Malignant neoplasm of stomach, unspecified'),
('C18', 'Malignant neoplasm of colon'),
('C18.9', 'Malignant neoplasm of colon, unspecified'),
('C34', 'Malignant neoplasm of bronchus and lung'),
('C34.9', 'Malignant neoplasm of lung, unspecified'),
('C50', 'Malignant neoplasm of breast'),
('C50.9', 'Malignant neoplasm of breast, unspecified'),
('C61', 'Malignant neoplasm of prostate'),

-- Blood disorders (D)
('D50', 'Iron deficiency anemia'),
('D50.9', 'Iron deficiency anemia, unspecified'),
('D64', 'Other anemias'),
('D64.9', 'Anemia, unspecified'),

-- Endocrine & metabolic (E)
('E03', 'Hypothyroidism'),
('E03.9', 'Hypothyroidism, unspecified'),
('E10', 'Type 1 diabetes mellitus'),
('E10.9', 'Type 1 diabetes mellitus without complications'),
('E11', 'Type 2 diabetes mellitus'),
('E11.9', 'Type 2 diabetes mellitus without complications'),
('E66', 'Overweight and obesity'),
('E66.9', 'Obesity, unspecified'),
('E78', 'Disorders of lipoprotein metabolism'),
('E78.5', 'Hyperlipidemia, unspecified'),

-- Mental health (F)
('F20', 'Schizophrenia'),
('F20.9', 'Schizophrenia, unspecified'),
('F31', 'Bipolar disorder'),
('F31.9', 'Bipolar disorder, unspecified'),
('F32', 'Major depressive disorder, single episode'),
('F32.9', 'Major depressive disorder, unspecified'),
('F33', 'Major depressive disorder, recurrent'),
('F41', 'Anxiety disorders'),
('F41.1', 'Generalized anxiety disorder'),

-- Circulatory system (I)
('I10', 'Essential hypertension'),
('I11', 'Hypertensive heart disease'),
('I20', 'Angina pectoris'),
('I21', 'Acute myocardial infarction'),
('I25', 'Chronic ischemic heart disease'),

-- Respiratory system (J)
('J00', 'Acute nasopharyngitis'),
('J06', 'Acute upper respiratory infections'),
('J18', 'Pneumonia'),
('J18.9', 'Pneumonia, unspecified organism'),
('J45', 'Asthma'),
('J45.9', 'Asthma, unspecified'),

-- Digestive system (K)
('K21', 'Gastro-esophageal reflux disease'),
('K21.9', 'GERD without esophagitis'),
('K35', 'Acute appendicitis'),
('K52', 'Noninfective gastroenteritis and colitis'),
('K59', 'Functional intestinal disorders'),

-- Musculoskeletal (M)
('M54', 'Dorsalgia'),
('M54.5', 'Low back pain'),
('M79', 'Other soft tissue disorders'),

-- Genitourinary (N)
('N18', 'Chronic kidney disease'),
('N18.9', 'Chronic kidney disease, unspecified'),
('N39', 'Urinary tract infection'),

-- Symptoms (R)
('R05', 'Cough'),
('R07', 'Chest pain'),
('R10', 'Abdominal pain'),
('R51', 'Headache'),

-- General & encounters (Z)
('Z00', 'General medical examination'),
('Z01', 'Other special examinations'),
('Z23', 'Encounter for immunization'),
('Z71', 'Counseling and medical advice');
