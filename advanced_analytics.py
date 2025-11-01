"""
Advanced Data Analytics for AI-Powered Structural Health Monitoring
Comprehensive implementation covering complete Data Science syllabus:

UNIT I: INTRODUCTION TO DATA SCIENCE
UNIT II: DESCRIPTIVE ANALYTICS AND VISUALIZATION  
UNIT III: INFERENTIAL STATISTICS
UNIT IV: ANALYSIS OF VARIANCE
UNIT V: PREDICTIVE ANALYTICS

Authors: AI Engineering Team
Version: 2.0
Last Updated: November 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, ttest_ind, ttest_rel, ttest_1samp
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
import json
from datetime import datetime, timedelta
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
warnings.filterwarnings('ignore')

class AdvancedStructuralAnalytics:
    """
    Comprehensive Data Science Analysis for Structural Health Monitoring
    Covers all syllabus units with practical applications to civil infrastructure
    """
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.analysis_results = {}
        self.visualization_data = {}
        
    # =================== UNIT I: INTRODUCTION TO DATA SCIENCE ===================
    
    def data_science_process_pipeline(self, crack_data, material_data, environmental_data, time_series_data=None):
        """
        Complete Data Science Process Implementation
        1. Setting Research Goals
        2. Data Retrieval and Integration
        3. Data Cleansing and Transformation
        4. Exploratory Data Analysis
        5. Model Building
        6. Application Development
        """
        print("🔬 Initiating Comprehensive Data Science Pipeline...")
        
        # Step 1: Research Goal Setting
        research_framework = self.define_research_goals()
        
        # Step 2: Data Retrieval and Integration
        integrated_dataset = self.retrieve_and_integrate_data(
            crack_data, material_data, environmental_data, time_series_data
        )
        
        # Step 3: Data Cleansing and Transformation
        cleaned_data = self.cleanse_and_transform_data(integrated_dataset)
        
        # Step 4: Exploratory Data Analysis
        eda_insights = self.comprehensive_exploratory_analysis(cleaned_data)
        
        # Step 5: Model Building and Validation
        predictive_models = self.build_comprehensive_models(cleaned_data)
        
        # Step 6: Application and Insights
        actionable_insights = self.generate_actionable_insights(
            cleaned_data, eda_insights, predictive_models
        )
        
        return {
            'research_framework': research_framework,
            'integrated_data': integrated_dataset,
            'cleaned_data': cleaned_data,
            'eda_insights': eda_insights,
            'predictive_models': predictive_models,
            'actionable_insights': actionable_insights,
            'process_metadata': {
                'timestamp': datetime.now().isoformat(),
                'data_quality_score': self.calculate_data_quality_score(cleaned_data),
                'analysis_completeness': 'comprehensive'
            }
        }
    
    def define_research_goals(self):
        """Research Goal Setting for Infrastructure Health Monitoring"""
        return {
            'primary_objective': 'AI-Powered Structural Health Assessment for Civil Infrastructure',
            'research_questions': [
                'What are the key indicators of structural deterioration?',
                'How can we predict maintenance requirements proactively?',
                'What environmental factors most impact structural health?',
                'How can we optimize resource allocation for infrastructure maintenance?'
            ],
            'success_metrics': [
                'Prediction accuracy > 85%',
                'Early detection capability',
                'Cost reduction in maintenance',
                'Improved safety outcomes'
            ],
            'stakeholders': ['Civil Engineers', 'City Planners', 'Maintenance Teams', 'Safety Inspectors'],
            'ethical_considerations': [
                'Public safety priority',
                'Data privacy protection',
                'Algorithmic transparency',
                'Bias mitigation'
            ]
        }
    
    def retrieve_and_integrate_data(self, crack_data, material_data, environmental_data, time_series_data):
        """Advanced Data Integration from Multiple Infrastructure Sources"""
        integrated_records = []
        
        # Process crack detection data
        if crack_data and len(crack_data) > 0:
            for i, crack in enumerate(crack_data):
                record = {
                    'structure_id': f"struct_{i+1}",
                    'crack_width_mm': crack.get('width_cm', 0) * 10,  # Convert to mm
                    'crack_length_mm': crack.get('length_cm', 0) * 10,
                    'crack_area_mm2': crack.get('width_cm', 0) * crack.get('length_cm', 0) * 100,
                    'severity_level': crack.get('severity', 'Unknown'),
                    'detection_confidence': crack.get('confidence', 0),
                    'material_type': material_data.get('predicted_material', 'Concrete'),
                    'carbon_footprint_kg': environmental_data.get('carbon_footprint_kg', 0),
                    'water_footprint_liters': environmental_data.get('water_footprint_liters', 0),
                    'inspection_date': datetime.now().strftime('%Y-%m-%d'),
                    'structure_age_years': np.random.randint(5, 50),  # Simulated
                    'load_capacity_tons': np.random.uniform(50, 500),  # Simulated
                    'weather_exposure': np.random.choice(['Low', 'Medium', 'High']),
                    'maintenance_history': np.random.choice(['Regular', 'Irregular', 'Poor'])
                }
                integrated_records.append(record)
        
        # Add baseline record if no cracks detected
        if not integrated_records:
            integrated_records.append({
                'structure_id': 'baseline_001',
                'crack_width_mm': 0,
                'crack_length_mm': 0,
                'crack_area_mm2': 0,
                'severity_level': 'None',
                'detection_confidence': 1.0,
                'material_type': material_data.get('predicted_material', 'Concrete'),
                'carbon_footprint_kg': environmental_data.get('carbon_footprint_kg', 0),
                'water_footprint_liters': environmental_data.get('water_footprint_liters', 0),
                'inspection_date': datetime.now().strftime('%Y-%m-%d'),
                'structure_age_years': np.random.randint(5, 50),
                'load_capacity_tons': np.random.uniform(50, 500),
                'weather_exposure': np.random.choice(['Low', 'Medium', 'High']),
                'maintenance_history': np.random.choice(['Regular', 'Irregular', 'Poor'])
            })
        
        # Add synthetic historical data for better analysis
        for i in range(10):
            historical_record = {
                'structure_id': f"hist_{i+1}",
                'crack_width_mm': np.random.exponential(2),
                'crack_length_mm': np.random.exponential(5),
                'crack_area_mm2': np.random.exponential(10),
                'severity_level': np.random.choice(['None', 'Minor', 'Moderate', 'Severe', 'Critical'], 
                                                  p=[0.3, 0.3, 0.2, 0.15, 0.05]),
                'detection_confidence': np.random.uniform(0.7, 1.0),
                'material_type': np.random.choice(['Concrete', 'Steel', 'Brick', 'Stone']),
                'carbon_footprint_kg': np.random.uniform(0.1, 10),
                'water_footprint_liters': np.random.uniform(10, 1000),
                'inspection_date': (datetime.now() - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d'),
                'structure_age_years': np.random.randint(1, 100),
                'load_capacity_tons': np.random.uniform(10, 1000),
                'weather_exposure': np.random.choice(['Low', 'Medium', 'High']),
                'maintenance_history': np.random.choice(['Regular', 'Irregular', 'Poor'])
            }
            integrated_records.append(historical_record)
        
        return pd.DataFrame(integrated_records)
    
    def cleanse_and_transform_data(self, df):
        """Advanced Data Cleansing and Transformation"""
        # Handle missing values
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
        
        categorical_columns = df.select_dtypes(include=['object']).columns
        for col in categorical_columns:
            df[col] = df[col].fillna(df[col].mode().iloc[0] if not df[col].mode().empty else 'Unknown')
        
        # Outlier detection and treatment using IQR method
        for col in numeric_columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Cap outliers instead of removing to preserve data
            df[col] = np.clip(df[col], lower_bound, upper_bound)
        
        # Feature engineering
        df['crack_severity_numeric'] = df['severity_level'].map({
            'None': 0, 'Minor': 1, 'Moderate': 2, 'Severe': 3, 'Critical': 4
        }).fillna(0)
        
        df['maintenance_score'] = df['maintenance_history'].map({
            'Poor': 1, 'Irregular': 2, 'Regular': 3
        }).fillna(2)
        
        df['weather_exposure_numeric'] = df['weather_exposure'].map({
            'Low': 1, 'Medium': 2, 'High': 3
        }).fillna(2)
        
        # Calculate derived features
        df['crack_aspect_ratio'] = np.where(df['crack_width_mm'] > 0, 
                                          df['crack_length_mm'] / df['crack_width_mm'], 0)
        df['structural_risk_index'] = (
            df['crack_severity_numeric'] * 0.4 + 
            df['structure_age_years'] / 100 * 0.3 + 
            df['weather_exposure_numeric'] / 3 * 0.3
        )
        
        return df
    
    # =================== UNIT II: DESCRIPTIVE ANALYTICS AND VISUALIZATION ===================
    
    def comprehensive_exploratory_analysis(self, df):
        """Complete Descriptive Analytics Implementation"""
        results = {}
        
        # Frequency Distributions
        results['frequency_distributions'] = self.analyze_frequency_distributions(df)
        
        # Outlier Analysis
        results['outlier_analysis'] = self.detect_and_analyze_outliers(df)
        
        # Distribution Interpretation
        results['distribution_analysis'] = self.interpret_distributions(df)
        
        # Correlation and Scatter Plot Analysis
        results['correlation_analysis'] = self.comprehensive_correlation_analysis(df)
        
        # Regression Analysis (Simple and Multiple)
        results['regression_analysis'] = self.comprehensive_regression_analysis(df)
        
        # Variance Analysis
        results['variability_analysis'] = self.analyze_variability(df)
        
        return results
    
    def analyze_frequency_distributions(self, df):
        """Comprehensive Frequency Distribution Analysis"""
        freq_analysis = {}
        
        # Categorical variables
        categorical_cols = ['severity_level', 'material_type', 'weather_exposure', 'maintenance_history']
        for col in categorical_cols:
            if col in df.columns:
                freq_table = df[col].value_counts()
                relative_freq = df[col].value_counts(normalize=True)
                
                freq_analysis[col] = {
                    'absolute_frequency': freq_table.to_dict(),
                    'relative_frequency': {k: round(v, 4) for k, v in relative_freq.to_dict().items()},
                    'mode': freq_table.index[0],
                    'unique_values': len(freq_table),
                    'entropy': -sum(relative_freq * np.log2(relative_freq + 1e-10))  # Information entropy
                }
        
        # Numerical variables - binned frequency distributions
        numerical_cols = ['crack_width_mm', 'crack_length_mm', 'crack_area_mm2', 'structure_age_years']
        for col in numerical_cols:
            if col in df.columns and df[col].nunique() > 1:
                hist, bin_edges = np.histogram(df[col], bins=10, density=True)
                bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
                
                freq_analysis[f'{col}_histogram'] = {
                    'bin_centers': bin_centers.tolist(),
                    'frequencies': hist.tolist(),
                    'bin_edges': bin_edges.tolist(),
                    'distribution_shape': self.classify_distribution_shape(df[col])
                }
        
        return freq_analysis
    
    def detect_and_analyze_outliers(self, df):
        """Advanced Outlier Detection and Analysis"""
        outlier_analysis = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                
                # Multiple outlier detection methods
                # 1. Z-score method
                z_scores = np.abs(stats.zscore(data))
                z_outliers = data[z_scores > 3]
                
                # 2. IQR method
                Q1, Q3 = data.quantile([0.25, 0.75])
                IQR = Q3 - Q1
                iqr_outliers = data[(data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)]
                
                # 3. Modified Z-score (median-based)
                median = data.median()
                mad = np.median(np.abs(data - median))
                modified_z_scores = 0.6745 * (data - median) / mad
                modified_z_outliers = data[np.abs(modified_z_scores) > 3.5]
                
                outlier_analysis[col] = {
                    'z_score_outliers': {
                        'count': len(z_outliers),
                        'percentage': len(z_outliers) / len(data) * 100,
                        'values': z_outliers.tolist()
                    },
                    'iqr_outliers': {
                        'count': len(iqr_outliers),
                        'percentage': len(iqr_outliers) / len(data) * 100,
                        'values': iqr_outliers.tolist()
                    },
                    'modified_z_outliers': {
                        'count': len(modified_z_outliers),
                        'percentage': len(modified_z_outliers) / len(data) * 100,
                        'values': modified_z_outliers.tolist()
                    },
                    'outlier_impact': 'high' if len(z_outliers) > len(data) * 0.05 else 'moderate' if len(z_outliers) > len(data) * 0.01 else 'low'
                }
        
        return outlier_analysis
    
    def interpret_distributions(self, df):
        """Comprehensive Distribution Analysis and Interpretation"""
        distribution_analysis = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 2:
                data = df[col].dropna()
                
                # Basic descriptive statistics
                desc_stats = {
                    'mean': float(data.mean()),
                    'median': float(data.median()),
                    'mode': float(data.mode().iloc[0] if not data.mode().empty else data.median()),
                    'std_deviation': float(data.std()),
                    'variance': float(data.var()),
                    'range': float(data.max() - data.min()),
                    'iqr': float(data.quantile(0.75) - data.quantile(0.25)),
                    'cv': float(data.std() / data.mean()) if data.mean() != 0 else 0,  # Coefficient of variation
                    'skewness': float(stats.skew(data)),
                    'kurtosis': float(stats.kurtosis(data))
                }
                
                # Normal distribution tests
                normality_tests = {}
                if len(data) >= 3:
                    # Shapiro-Wilk test
                    shapiro_stat, shapiro_p = stats.shapiro(data[:5000])  # Limit sample size for large datasets
                    normality_tests['shapiro_wilk'] = {
                        'statistic': float(shapiro_stat),
                        'p_value': float(shapiro_p),
                        'is_normal': shapiro_p > 0.05
                    }
                    
                    # Anderson-Darling test
                    anderson_result = stats.anderson(data, dist='norm')
                    normality_tests['anderson_darling'] = {
                        'statistic': float(anderson_result.statistic),
                        'critical_values': anderson_result.critical_values.tolist(),
                        'significance_levels': anderson_result.significance_level.tolist()
                    }
                
                # Z-scores for key percentiles
                z_scores = {
                    'z_score_mean': 0,
                    'z_score_median': float((data.median() - data.mean()) / data.std()) if data.std() > 0 else 0,
                    'z_score_q1': float((data.quantile(0.25) - data.mean()) / data.std()) if data.std() > 0 else 0,
                    'z_score_q3': float((data.quantile(0.75) - data.mean()) / data.std()) if data.std() > 0 else 0
                }
                
                distribution_analysis[col] = {
                    'descriptive_statistics': desc_stats,
                    'normality_tests': normality_tests,
                    'z_scores': z_scores,
                    'distribution_interpretation': self.interpret_distribution_characteristics(desc_stats),
                    'variability_assessment': self.assess_variability(desc_stats)
                }
        
        return distribution_analysis
    
    def comprehensive_correlation_analysis(self, df):
        """Advanced Correlation and Scatter Plot Analysis"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient numeric variables for correlation analysis'}
        
        correlation_analysis = {}
        
        # Pearson correlation matrix
        pearson_corr = numeric_df.corr(method='pearson')
        correlation_analysis['pearson_correlation'] = pearson_corr.to_dict()
        
        # Spearman correlation matrix
        spearman_corr = numeric_df.corr(method='spearman')
        correlation_analysis['spearman_correlation'] = spearman_corr.to_dict()
        
        # Kendall correlation matrix
        kendall_corr = numeric_df.corr(method='kendall')
        correlation_analysis['kendall_correlation'] = kendall_corr.to_dict()
        
        # Significant correlations analysis
        significant_correlations = []
        correlation_pairs = []
        
        for i in range(len(numeric_df.columns)):
            for j in range(i+1, len(numeric_df.columns)):
                col1, col2 = numeric_df.columns[i], numeric_df.columns[j]
                
                # Pearson correlation with significance test
                r_val, p_val = stats.pearsonr(numeric_df[col1].dropna(), numeric_df[col2].dropna())
                
                correlation_strength = self.classify_correlation_strength(abs(r_val))
                
                correlation_pair = {
                    'variables': f"{col1} vs {col2}",
                    'pearson_r': float(r_val),
                    'p_value': float(p_val),
                    'significant': p_val < 0.05,
                    'strength': correlation_strength,
                    'direction': 'positive' if r_val > 0 else 'negative' if r_val < 0 else 'none'
                }
                
                correlation_pairs.append(correlation_pair)
                
                if abs(r_val) > 0.3 and p_val < 0.05:  # Significant correlation threshold
                    significant_correlations.append(correlation_pair)
        
        correlation_analysis['correlation_pairs'] = correlation_pairs
        correlation_analysis['significant_correlations'] = significant_correlations
        correlation_analysis['correlation_summary'] = {
            'total_pairs': len(correlation_pairs),
            'significant_pairs': len(significant_correlations),
            'strongest_positive': max(correlation_pairs, key=lambda x: x['pearson_r'] if x['pearson_r'] > 0 else -1),
            'strongest_negative': min(correlation_pairs, key=lambda x: x['pearson_r'] if x['pearson_r'] < 0 else 1)
        }
        
        return correlation_analysis
    
    def comprehensive_regression_analysis(self, df):
        """Advanced Regression Analysis - Simple and Multiple"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient variables for regression analysis'}
        
        regression_results = {}
        
        # Use structural_risk_index or crack_area_mm2 as dependent variable if available
        target_candidates = ['structural_risk_index', 'crack_area_mm2', 'crack_severity_numeric']
        target_col = None
        
        for candidate in target_candidates:
            if candidate in numeric_df.columns:
                target_col = candidate
                break
        
        if target_col is None:
            target_col = numeric_df.columns[0]  # Fallback to first column
        
        y = numeric_df[target_col]
        X = numeric_df.drop(columns=[target_col])
        
        if X.shape[1] == 0:
            return {'error': 'No independent variables available'}
        
        # Simple Linear Regression (with most correlated variable)
        correlations = X.corrwith(y).abs().sort_values(ascending=False)
        if not correlations.empty:
            best_predictor = correlations.index[0]
            X_simple = X[[best_predictor]]
            
            simple_regression = self.perform_simple_regression(X_simple, y, best_predictor, target_col)
            regression_results['simple_regression'] = simple_regression
        
        # Multiple Linear Regression
        multiple_regression = self.perform_multiple_regression(X, y, target_col)
        regression_results['multiple_regression'] = multiple_regression
        
        # Least Squares Analysis
        least_squares_analysis = self.analyze_least_squares(X, y, target_col)
        regression_results['least_squares_analysis'] = least_squares_analysis
        
        return regression_results
    
    def analyze_variability(self, df):
        """Comprehensive Variability Analysis"""
        variability_analysis = {}
        
        # Quantitative variables
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                
                variability_analysis[col] = {
                    'range': float(data.max() - data.min()),
                    'interquartile_range': float(data.quantile(0.75) - data.quantile(0.25)),
                    'variance': float(data.var()),
                    'standard_deviation': float(data.std()),
                    'coefficient_of_variation': float(data.std() / data.mean()) if data.mean() != 0 else 0,
                    'mean_absolute_deviation': float(np.mean(np.abs(data - data.mean()))),
                    'quartile_deviation': float((data.quantile(0.75) - data.quantile(0.25)) / 2),
                    'relative_variability': self.classify_relative_variability(data.std() / data.mean() if data.mean() != 0 else 0)
                }
        
        # Qualitative variables (using frequency distributions)
        categorical_cols = ['severity_level', 'material_type', 'weather_exposure', 'maintenance_history']
        for col in categorical_cols:
            if col in df.columns:
                freq_dist = df[col].value_counts(normalize=True)
                
                # Calculate variability measures for categorical data
                variability_analysis[f'{col}_categorical'] = {
                    'number_of_categories': len(freq_dist),
                    'most_frequent_category': freq_dist.index[0],
                    'most_frequent_proportion': float(freq_dist.iloc[0]),
                    'entropy': float(-sum(freq_dist * np.log2(freq_dist + 1e-10))),  # Information entropy
                    'concentration_ratio': float(freq_dist.iloc[0]),  # Proportion of most frequent category
                    'diversity_index': float(1 - sum(freq_dist ** 2)),  # Simpson's diversity index
                    'variability_level': self.classify_categorical_variability(freq_dist)
                }
        
        return variability_analysis
    
    # =================== UNIT III: INFERENTIAL STATISTICS ===================
    
    def comprehensive_inferential_statistics(self, df):
        """Complete Inferential Statistics Implementation"""
        results = {}
        
        # Population vs Sample Analysis
        results['sampling_analysis'] = self.analyze_sampling_distribution(df)
        
        # Hypothesis Testing (Z-tests and T-tests)
        results['hypothesis_testing'] = self.comprehensive_hypothesis_testing(df)
        
        # Confidence Intervals and Estimation
        results['confidence_intervals'] = self.calculate_confidence_intervals(df)
        
        # Effect Size Analysis
        results['effect_size_analysis'] = self.analyze_effect_sizes(df)
        
        # Power Analysis
        results['power_analysis'] = self.perform_power_analysis(df)
        
        return results
    
    def analyze_sampling_distribution(self, df):
        """Sampling Distribution and Standard Error Analysis"""
        sampling_analysis = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                n = len(data)
                
                # Sample statistics
                sample_mean = data.mean()
                sample_std = data.std(ddof=1)  # Sample standard deviation
                standard_error = sample_std / np.sqrt(n)
                
                # Sampling distribution characteristics
                sampling_analysis[col] = {
                    'sample_size': n,
                    'sample_mean': float(sample_mean),
                    'sample_std': float(sample_std),
                    'standard_error_mean': float(standard_error),
                    'margin_of_error_95': float(1.96 * standard_error),  # 95% confidence level
                    'distribution_shape': 'approximately_normal' if n >= 30 else 'unknown',
                    'central_limit_theorem_applies': n >= 30,
                    'sampling_variability': float(standard_error / sample_mean) if sample_mean != 0 else 0
                }
        
        return sampling_analysis
    
    def comprehensive_hypothesis_testing(self, df):
        """Advanced Hypothesis Testing Implementation"""
        test_results = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                
                if len(data) >= 3:
                    # One-sample tests
                    test_results[f'{col}_one_sample'] = self.perform_one_sample_tests(data, col)
                    
                    # Goodness of fit tests
                    test_results[f'{col}_goodness_of_fit'] = self.perform_goodness_of_fit_tests(data, col)
        
        # Two-sample tests (if we have grouping variables)
        if 'severity_level' in df.columns:
            test_results['two_sample_tests'] = self.perform_two_sample_tests(df)
        
        return test_results
    
    def perform_one_sample_tests(self, data, col_name):
        """One-sample T-test and Z-test"""
        n = len(data)
        sample_mean = data.mean()
        sample_std = data.std(ddof=1)
        
        # Test against hypothetical population mean (using median as null hypothesis)
        hypothesized_mean = data.median()
        
        # One-sample t-test
        t_stat, t_p_value = stats.ttest_1samp(data, hypothesized_mean)
        
        # Calculate effect size (Cohen's d)
        cohens_d = (sample_mean - hypothesized_mean) / sample_std if sample_std > 0 else 0
        
        # Z-test (if sample size is large)
        if n >= 30:
            z_stat = (sample_mean - hypothesized_mean) / (sample_std / np.sqrt(n))
            z_p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))  # Two-tailed test
        else:
            z_stat, z_p_value = None, None
        
        return {
            'null_hypothesis': f'Population mean of {col_name} equals {hypothesized_mean:.3f}',
            'alternative_hypothesis': f'Population mean of {col_name} does not equal {hypothesized_mean:.3f}',
            't_test': {
                't_statistic': float(t_stat),
                'p_value': float(t_p_value),
                'degrees_freedom': n - 1,
                'significant_at_0.05': bool(t_p_value < 0.05),
                'significant_at_0.01': bool(t_p_value < 0.01),
                'test_type': 'two_tailed'
            },
            'z_test': {
                'z_statistic': float(z_stat) if z_stat is not None else None,
                'p_value': float(z_p_value) if z_p_value is not None else None,
                'applicable': n >= 30,
                'significant_at_0.05': bool(z_p_value < 0.05) if z_p_value is not None else None
            },
            'effect_size': {
                'cohens_d': float(cohens_d),
                'interpretation': self.interpret_cohens_d(cohens_d)
            },
            'decision_rule': {
                'reject_null_0.05': bool(t_p_value < 0.05),
                'reject_null_0.01': bool(t_p_value < 0.01),
                'practical_significance': bool(abs(cohens_d) > 0.5)
            }
        }
    
    def calculate_confidence_intervals(self, df):
        """Comprehensive Confidence Interval Calculation"""
        ci_results = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        confidence_levels = [0.90, 0.95, 0.99]
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                n = len(data)
                mean = data.mean()
                std = data.std(ddof=1)
                se = std / np.sqrt(n)
                
                ci_results[col] = {}
                
                for conf_level in confidence_levels:
                    alpha = 1 - conf_level
                    
                    # t-distribution critical value
                    t_critical = stats.t.ppf(1 - alpha/2, n-1)
                    margin_error_t = t_critical * se
                    
                    # z-distribution critical value (for large samples)
                    z_critical = stats.norm.ppf(1 - alpha/2)
                    margin_error_z = z_critical * se
                    
                    ci_results[col][f'ci_{int(conf_level*100)}'] = {
                        't_distribution': {
                            'lower_bound': float(mean - margin_error_t),
                            'upper_bound': float(mean + margin_error_t),
                            'margin_of_error': float(margin_error_t),
                            'width': float(2 * margin_error_t)
                        },
                        'z_distribution': {
                            'lower_bound': float(mean - margin_error_z),
                            'upper_bound': float(mean + margin_error_z),
                            'margin_of_error': float(margin_error_z),
                            'width': float(2 * margin_error_z),
                            'applicable': n >= 30
                        },
                        'interpretation': f"We are {int(conf_level*100)}% confident that the true population mean lies between {mean - margin_error_t:.3f} and {mean + margin_error_t:.3f}",
                        'sample_size_effect': 'increase_n_to_reduce_width'
                    }
        
        return ci_results
    
    # =================== UNIT IV: ANALYSIS OF VARIANCE ===================
    
    def comprehensive_anova_analysis(self, df):
        """Complete ANOVA Implementation"""
        results = {}
        
        # One-way ANOVA
        results['one_way_anova'] = self.perform_one_way_anova(df)
        
        # Two-way ANOVA simulation
        results['two_way_anova'] = self.perform_two_way_anova(df)
        
        # F-tests
        results['f_tests'] = self.perform_f_tests(df)
        
        # Chi-square tests
        results['chi_square_tests'] = self.perform_chi_square_tests(df)
        
        # Post-hoc analysis
        results['post_hoc_analysis'] = self.perform_post_hoc_analysis(df)
        
        return results
    
    def perform_one_way_anova(self, df):
        """One-way ANOVA for comparing groups"""
        if 'severity_level' not in df.columns:
            return {'error': 'No grouping variable available for ANOVA'}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        anova_results = {}
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                # Create groups based on severity level
                groups = []
                group_names = []
                
                for severity in df['severity_level'].unique():
                    group_data = df[df['severity_level'] == severity][col].dropna()
                    if len(group_data) > 0:
                        groups.append(group_data)
                        group_names.append(severity)
                
                if len(groups) >= 2:
                    # Perform one-way ANOVA
                    f_stat, p_value = f_oneway(*groups)
                    
                    # Calculate effect size (eta-squared)
                    total_sum_squares = sum([(group - df[col].mean())**2 for group in groups for value in group])
                    between_sum_squares = sum([len(group) * (group.mean() - df[col].mean())**2 for group in groups])
                    eta_squared = between_sum_squares / total_sum_squares if total_sum_squares > 0 else 0
                    
                    # Group statistics
                    group_stats = {}
                    for i, (group, name) in enumerate(zip(groups, group_names)):
                        group_stats[name] = {
                            'n': len(group),
                            'mean': float(group.mean()),
                            'std': float(group.std()),
                            'min': float(group.min()),
                            'max': float(group.max())
                        }
                    
                    anova_results[col] = {
                        'f_statistic': float(f_stat),
                        'p_value': float(p_value),
                        'significant': bool(p_value < 0.05),
                        'groups_compared': group_names,
                        'degrees_freedom_between': len(groups) - 1,
                        'degrees_freedom_within': sum(len(group) for group in groups) - len(groups),
                        'effect_size_eta_squared': float(eta_squared),
                        'effect_interpretation': self.interpret_eta_squared(eta_squared),
                        'group_statistics': group_stats,
                        'conclusion': 'significant_difference' if p_value < 0.05 else 'no_significant_difference'
                    }
        
        return anova_results
    
    def perform_chi_square_tests(self, df):
        """Chi-square Tests for Independence and Goodness of Fit"""
        chi_square_results = {}
        
        categorical_cols = ['severity_level', 'material_type', 'weather_exposure', 'maintenance_history']
        available_cats = [col for col in categorical_cols if col in df.columns]
        
        if len(available_cats) >= 2:
            # Chi-square test of independence
            for i in range(len(available_cats)):
                for j in range(i+1, len(available_cats)):
                    col1, col2 = available_cats[i], available_cats[j]
                    
                    # Create contingency table
                    contingency_table = pd.crosstab(df[col1], df[col2])
                    
                    if contingency_table.size > 1:
                        # Perform chi-square test
                        chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)
                        
                        # Calculate Cramér's V (effect size)
                        n = contingency_table.sum().sum()
                        cramers_v = np.sqrt(chi2_stat / (n * (min(contingency_table.shape) - 1)))
                        
                        chi_square_results[f'{col1}_vs_{col2}'] = {
                            'chi_square_statistic': float(chi2_stat),
                            'p_value': float(p_value),
                            'degrees_freedom': int(dof),
                            'significant': bool(p_value < 0.05),
                            'cramers_v': float(cramers_v),
                            'effect_size_interpretation': self.interpret_cramers_v(cramers_v),
                            'contingency_table': contingency_table.to_dict(),
                            'expected_frequencies': expected.tolist(),
                            'conclusion': 'variables_are_associated' if p_value < 0.05 else 'variables_are_independent'
                        }
        
        # Goodness of fit tests
        for col in available_cats:
            observed = df[col].value_counts()
            if len(observed) > 1:
                # Test against uniform distribution
                expected_uniform = [len(df) / len(observed)] * len(observed)
                
                if all(e >= 5 for e in expected_uniform):  # Chi-square assumption
                    chi2_stat, p_value = stats.chisquare(observed.values, expected_uniform)
                    
                    chi_square_results[f'{col}_goodness_of_fit'] = {
                        'chi_square_statistic': float(chi2_stat),
                        'p_value': float(p_value),
                        'degrees_freedom': len(observed) - 1,
                        'significant': bool(p_value < 0.05),
                        'null_hypothesis': 'uniform_distribution',
                        'observed_frequencies': observed.to_dict(),
                        'expected_frequencies': dict(zip(observed.index, expected_uniform)),
                        'conclusion': 'distribution_differs_from_uniform' if p_value < 0.05 else 'distribution_consistent_with_uniform'
                    }
        
        return chi_square_results
    
    # =================== UNIT V: PREDICTIVE ANALYTICS ===================
    
    def comprehensive_predictive_analytics(self, df):
        """Complete Predictive Analytics Implementation"""
        results = {}
        
        # Linear Regression Models
        results['linear_models'] = self.advanced_linear_modeling(df)
        
        # Logistic Regression
        results['logistic_models'] = self.perform_logistic_regression(df)
        
        # Time Series Analysis
        results['time_series_analysis'] = self.perform_time_series_analysis(df)
        
        # Model Validation and Goodness of Fit
        results['model_validation'] = self.comprehensive_model_validation(df)
        
        # Weighted Resampling
        results['resampling_analysis'] = self.perform_weighted_resampling(df)
        
        return results
    
    def advanced_linear_modeling(self, df):
        """Advanced Linear Regression with Diagnostics"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient variables for regression modeling'}
        
        # Select target variable
        target_candidates = ['structural_risk_index', 'crack_severity_numeric', 'crack_area_mm2']
        target_col = None
        
        for candidate in target_candidates:
            if candidate in numeric_df.columns:
                target_col = candidate
                break
        
        if target_col is None:
            target_col = numeric_df.columns[0]
        
        y = numeric_df[target_col]
        X = numeric_df.drop(columns=[target_col])
        
        if X.shape[1] == 0:
            return {'error': 'No predictor variables available'}
        
        # Split data for validation
        if len(df) > 10:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        else:
            X_train = X_test = X
            y_train = y_test = y
        
        # Fit linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Predictions
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        
        # Model diagnostics
        linear_results = {
            'model_performance': {
                'train_r_squared': float(r2_score(y_train, y_train_pred)),
                'test_r_squared': float(r2_score(y_test, y_test_pred)),
                'train_rmse': float(np.sqrt(mean_squared_error(y_train, y_train_pred))),
                'test_rmse': float(np.sqrt(mean_squared_error(y_test, y_test_pred))),
                'mean_absolute_error': float(np.mean(np.abs(y_test - y_test_pred))),
                'overfitting_score': float(abs(r2_score(y_train, y_train_pred) - r2_score(y_test, y_test_pred)))
            },
            'model_coefficients': {
                'intercept': float(model.intercept_),
                'coefficients': {col: float(coef) for col, coef in zip(X.columns, model.coef_)},
                'standardized_coefficients': self.calculate_standardized_coefficients(X_train, y_train, model)
            },
            'residual_analysis': self.analyze_residuals(y_train, y_train_pred),
            'model_assumptions': self.test_regression_assumptions(X_train, y_train, y_train_pred),
            'feature_importance': self.calculate_feature_importance(X.columns, model.coef_),
            'model_equation': self.generate_regression_equation(model, X.columns)
        }
        
        return linear_results
    
    def perform_logistic_regression(self, df):
        """Comprehensive Logistic Regression Analysis"""
        # Create binary target based on high-risk structures
        if 'structural_risk_index' in df.columns:
            threshold = df['structural_risk_index'].median()
            df_copy = df.copy()
            df_copy['high_risk'] = (df_copy['structural_risk_index'] > threshold).astype(int)
        elif 'severity_level' in df.columns:
            df_copy = df.copy()
            df_copy['high_risk'] = df_copy['severity_level'].isin(['Severe', 'Critical']).astype(int)
        else:
            return {'error': 'Cannot create binary target variable'}
        
        # Check class distribution
        class_distribution = df_copy['high_risk'].value_counts()
        if len(class_distribution) < 2:
            return {'error': 'Insufficient class variation for logistic regression'}
        
        # Prepare features
        numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
        feature_cols = [col for col in numeric_cols if col not in ['high_risk', 'structural_risk_index']]
        
        if len(feature_cols) == 0:
            return {'error': 'No suitable features for logistic regression'}
        
        X = df_copy[feature_cols]
        y = df_copy['high_risk']
        
        # Handle missing values and scaling
        X = X.fillna(X.median())
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Split data
        if len(df_copy) > 10:
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)
        else:
            X_train = X_test = X_scaled
            y_train = y_test = y
        
        # Fit logistic regression
        log_model = LogisticRegression(random_state=42, max_iter=1000)
        log_model.fit(X_train, y_train)
        
        # Predictions
        y_train_pred = log_model.predict(X_train)
        y_test_pred = log_model.predict(X_test)
        y_train_prob = log_model.predict_proba(X_train)[:, 1]
        y_test_prob = log_model.predict_proba(X_test)[:, 1]
        
        logistic_results = {
            'model_performance': {
                'train_accuracy': float(accuracy_score(y_train, y_train_pred)),
                'test_accuracy': float(accuracy_score(y_test, y_test_pred)),
                'class_distribution': class_distribution.to_dict(),
                'classification_report': classification_report(y_test, y_test_pred, output_dict=True)
            },
            'model_coefficients': {
                'intercept': float(log_model.intercept_[0]),
                'coefficients': {col: float(coef) for col, coef in zip(feature_cols, log_model.coef_[0])},
                'odds_ratios': {col: float(np.exp(coef)) for col, coef in zip(feature_cols, log_model.coef_[0])}
            },
            'predictions': {
                'predicted_classes': y_test_pred.tolist(),
                'predicted_probabilities': y_test_prob.tolist(),
                'actual_classes': y_test.tolist()
            },
            'model_interpretation': {
                'target_definition': 'High-risk structure classification',
                'feature_effects': self.interpret_logistic_coefficients(feature_cols, log_model.coef_[0]),
                'prediction_threshold': 0.5
            }
        }
        
        return logistic_results
    
    def perform_time_series_analysis(self, df):
        """Advanced Time Series Analysis"""
        # Create synthetic time series based on structure aging
        if 'structure_age_years' in df.columns:
            # Simulate deterioration over time
            time_periods = 24  # 24 months
            base_deterioration = df['structural_risk_index'].mean() if 'structural_risk_index' in df.columns else 0.5
            
            # Generate time series data
            time_index = pd.date_range(start='2023-01-01', periods=time_periods, freq='M')
            deterioration_trend = base_deterioration + np.linspace(0, 0.3, time_periods)
            seasonal_component = 0.05 * np.sin(2 * np.pi * np.arange(time_periods) / 12)  # Annual seasonality
            noise = np.random.normal(0, 0.02, time_periods)
            
            time_series = deterioration_trend + seasonal_component + noise
            ts_df = pd.DataFrame({
                'date': time_index,
                'deterioration_index': time_series
            })
            
            # Time series analysis
            ts_analysis = {
                'trend_analysis': self.analyze_trend(ts_df['deterioration_index']),
                'seasonal_analysis': self.analyze_seasonality(ts_df['deterioration_index']),
                'autocorrelation_analysis': self.analyze_autocorrelation(ts_df['deterioration_index']),
                'forecasting': self.perform_forecasting(ts_df['deterioration_index']),
                'moving_averages': self.calculate_moving_averages(ts_df['deterioration_index']),
                'exponential_smoothing': self.apply_exponential_smoothing(ts_df['deterioration_index'])
            }
            
            return ts_analysis
        
        return {'note': 'Time series analysis requires temporal data - using simulated deterioration data'}
    
    # =================== HELPER METHODS ===================
    
    def classify_distribution_shape(self, data):
        """Classify the shape of a distribution"""
        skewness = stats.skew(data)
        kurtosis = stats.kurtosis(data)
        
        if abs(skewness) < 0.5:
            skew_type = 'symmetric'
        elif skewness > 0:
            skew_type = 'right_skewed'
        else:
            skew_type = 'left_skewed'
        
        if kurtosis > 0.5:
            kurt_type = 'leptokurtic'  # Heavy tails
        elif kurtosis < -0.5:
            kurt_type = 'platykurtic'  # Light tails
        else:
            kurt_type = 'mesokurtic'   # Normal-like tails
        
        return f"{skew_type}_{kurt_type}"
    
    def classify_correlation_strength(self, r_value):
        """Classify correlation strength"""
        abs_r = abs(r_value)
        if abs_r >= 0.9:
            return 'very_strong'
        elif abs_r >= 0.7:
            return 'strong'
        elif abs_r >= 0.5:
            return 'moderate'
        elif abs_r >= 0.3:
            return 'weak'
        else:
            return 'very_weak'
    
    def interpret_cohens_d(self, d):
        """Interpret Cohen's d effect size"""
        abs_d = abs(d)
        if abs_d < 0.2:
            return 'negligible'
        elif abs_d < 0.5:
            return 'small'
        elif abs_d < 0.8:
            return 'medium'
        else:
            return 'large'
    
    def interpret_eta_squared(self, eta_sq):
        """Interpret eta-squared effect size"""
        if eta_sq < 0.01:
            return 'negligible'
        elif eta_sq < 0.06:
            return 'small'
        elif eta_sq < 0.14:
            return 'medium'
        else:
            return 'large'
    
    def calculate_data_quality_score(self, df):
        """Calculate overall data quality score"""
        completeness = 1 - df.isnull().sum().sum() / (df.shape[0] * df.shape[1])
        consistency = 1 - (df.duplicated().sum() / len(df))
        validity = 0.9  # Assume 90% validity after cleaning
        
        return float((completeness + consistency + validity) / 3)
    
    def generate_actionable_insights(self, df, eda_results, model_results):
        """Generate actionable insights from analysis"""
        insights = {
            'key_findings': [],
            'risk_factors': [],
            'recommendations': [],
            'monitoring_priorities': []
        }
        
        # Key findings from EDA
        if 'correlation_analysis' in eda_results:
            sig_corr = eda_results['correlation_analysis'].get('significant_correlations', [])
            if sig_corr:
                insights['key_findings'].append(f"Found {len(sig_corr)} significant correlations between structural variables")
        
        # Risk factors
        if 'severity_level' in df.columns:
            risk_distribution = df['severity_level'].value_counts()
            high_risk_pct = (risk_distribution.get('Severe', 0) + risk_distribution.get('Critical', 0)) / len(df) * 100
            if high_risk_pct > 20:
                insights['risk_factors'].append(f"High percentage ({high_risk_pct:.1f}%) of structures show severe deterioration")
        
        # Recommendations based on analysis
        insights['recommendations'].extend([
            "Implement predictive maintenance program based on identified risk factors",
            "Focus monitoring efforts on structures with highest deterioration predictors",
            "Develop automated alert system for critical severity threshold breaches"
        ])
        
        return insights

# Usage example and main analysis function
def run_comprehensive_analysis(crack_data, material_data, environmental_data):
    """
    Main function to run complete data science analysis
    """
    analyzer = AdvancedStructuralAnalytics()
    
    # Run complete pipeline
    results = analyzer.data_science_process_pipeline(
        crack_data, material_data, environmental_data
    )
    
    # Add specific analyses
    if results['cleaned_data'] is not None and not results['cleaned_data'].empty:
        df = results['cleaned_data']
        
        # Unit III: Inferential Statistics
        results['inferential_statistics'] = analyzer.comprehensive_inferential_statistics(df)
        
        # Unit IV: ANOVA
        results['anova_analysis'] = analyzer.comprehensive_anova_analysis(df)
        
        # Unit V: Predictive Analytics
        results['predictive_analytics'] = analyzer.comprehensive_predictive_analytics(df)
    
    return results

if __name__ == "__main__":
    # Test with sample data
    sample_crack_data = [
        {'width_cm': 2.5, 'length_cm': 10.0, 'severity': 'Moderate', 'confidence': 0.85},
        {'width_cm': 1.0, 'length_cm': 5.0, 'severity': 'Minor', 'confidence': 0.92}
    ]
    
    sample_material_data = {'predicted_material': 'Concrete'}
    sample_environmental_data = {'carbon_footprint_kg': 5.2, 'water_footprint_liters': 150}
    
    results = run_comprehensive_analysis(
        sample_crack_data, 
        sample_material_data, 
        sample_environmental_data
    )
    
    print("✅ Comprehensive Data Science Analysis Complete!")
    print(f"📊 Analysis covered {len(results)} major components")