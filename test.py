import numpy as np
import pandas as pd

from simpsons_paradox import SimpsonsParadox


def test_fcn(**test_params):
    """Test the detector to ensure the results are as we expect,
    or if anything has changed.

    Args:
        test_params: dictionary of function inputs

    Returns:
        number of Simpson's pairs found in data

    """
    test_params.update({'quiet': True})
    return len(SimpsonsParadox(**test_params).get_simpsons_pairs())


if __name__ == '__main__':

    # Test 1: Disease Data
    print('Testing the disease data...')
    disease_df = pd.read_csv('data/SP_Data.txt')
    disease_params = {
        'df': disease_df, 'dv': 'Survived', 'ignore_columns': ['PatientId']
    }
    DISEASE_RESULTS = test_fcn(**disease_params)
    assert DISEASE_RESULTS == 1
    print('Passed!')

    # Test 2: Admissions Data
    print('Testing the admissions data...')
    admissions_df = pd.read_csv('data/admissions_data.csv')
    admissions_params = {
        'df': admissions_df, 'dv': 'Admit', 'ignore_columns': ['Unnamed: 0']
    }
    ADMISSIONS_RESULTS = test_fcn(**admissions_params)
    assert ADMISSIONS_RESULTS == 1
    print('Passed!')

    # Test 3: Census Data
    print('Testing the census data...')
    census_df = pd.read_csv('data/CensusModified.csv')
    census_params = {'df': census_df, 'dv': 'Income', 'weighting': False}
    CENSUS_RESULTS = test_fcn(**census_params)
    assert CENSUS_RESULTS == 1
    print('Passed!')

    # Test 4: Khan Academy Data
    print('Testing the Khan Academy data...')
    khan_df = pd.read_csv('data/small_khancademy.csv')
    bin_columns = [
        'timestamp', 'solve_time', 'attempts', 'tspp', 'session_num',
        'session_index', 'session_length', 'all_first_attempts',
        'signup_duration', 'total_solving_time', 'all_attempts',
        'all_problems', 'all_sequences', 'month', 'join_month'
    ]
    ignore_columns = ["user_id", "problem_id"]
    khan_params = {
        'df': khan_df, 'dv': 'performance', 'ignore_columns': ignore_columns,
        'bin_columns': bin_columns, 'weighting': False
    }
    KHAN_RESULTS = test_fcn(**khan_params)
    assert KHAN_RESULTS == 27
    print('Passed!')

    # Test 5: Khan Academy Data
    print('Testing the Khan Academy data (v2)...')
    khancad_df = pd.read_csv('data/small_khancademy.csv')
    khancad_params = {
        'df': khancad_df, 'dv': 'performance',
        'ignore_columns': ignore_columns, 'bin_columns': bin_columns
    }
    KHANCAD_RESULTS = test_fcn(**khancad_params)
    assert KHANCAD_RESULTS == 26
    print('Passed!')

    # Test 6: Baseball Data
    print('Testing the Baseball data...')
    baseball_df = pd.read_csv('data/baseball_data.csv')
    baseball_params = {
        'df': baseball_df, 'dv': 'outcome',
        'ignore_columns': ['Unnamed: 0'], 'max_pvalue': 1
    }
    BASEBALL_RESULTS = test_fcn(**baseball_params)
    assert BASEBALL_RESULTS == 1
    print('Passed!')

    # Test 7: Coffee Data
    print('Testing the Coffee data...')
    coffee_df = pd.read_csv('data/coffee_data.csv')
    coffee_params = {
        'df': coffee_df, 'dv': 'neuroticism', 'ignore_columns': ['Unnamed: 0']}
    COFFEE_RESULTS = test_fcn(**coffee_params)
    assert COFFEE_RESULTS == 0
    print('Passed!')

    # Test 8: Student Performance Data
    print('Testing the Student Performance data...')
    student_df = pd.read_csv('data/student-mat.csv', sep=';')
    student_df['final_grade'] = np.where(student_df['G3'] >= 10, 1, 0)
    student_params = {'df': student_df, 'dv': 'final_grade'}
    STUDENT_RESULTS = test_fcn(**student_params)
    assert STUDENT_RESULTS == 2
    print('Passed!')

    # Test 9: Teaching Assistant Data
    print('Testing the Teaching Assistant Evaluation data....')
    teaching_df = pd.read_csv('data/TeachingAssistant_EvaluationDataset.csv')
    teaching_params = {'df': teaching_df, 'dv': 'Score', 'target_category': 1}
    TEACHING_RESULTS = test_fcn(**teaching_params)
    assert TEACHING_RESULTS == 0
    print('Passed!')

    # Test 10: Breast Cancer Data
    print('Testing the Breast Cancer data...')
    cancer_df = pd.read_csv('data/breastcancer_data.csv')
    cancer_params = {'df': cancer_df, 'dv': 'class'}
    CANCER_RESULTS = test_fcn(**cancer_params)
    assert CANCER_RESULTS == 0
    print('Passed!')

    # Test 10: Breast Cancer Data
    print('Testing the Breast Cancer data...')
    cancer_df = pd.read_csv('data/breastcancer_data.csv')
    cancer_params = {'df': cancer_df, 'dv': 'class', 'max_pvalue': 1}
    CANCER_RESULTS = test_fcn(**cancer_params)
    assert CANCER_RESULTS == 2
    print('Passed!')
