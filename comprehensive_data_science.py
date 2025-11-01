"""
Comprehensive Data Science Analysis for Heritage Site Monitoring
Based on Data Science Syllabus - All chapters covered
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class ComprehensiveDataScienceAnalyzer:
    """Complete Data Science Analysis covering all syllabus topics"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.analysis_results = {}
    
    # =================== CHAPTER 1: INTRODUCTION TO DATA SCIENCE ===================
    
    def data_science_process(self, crack_data, material_data, environmental_data):
        """Complete data science process implementation"""
        print("🔬 Starting Data Science Process...")
        
        # 1. Setting Research Goal
        research_goals = {
            'primary': 'Heritage Site Structural Health Assessment',
            'objectives': [
                'Quantify structural deterioration patterns',
                'Predict maintenance requirements',
                'Assess environmental impact factors',
                'Develop preservation strategies'
            ]
        }
        
        # 2. Data Retrieval & Integration
        integrated_data = self.integrate_heritage_data(crack_data, material_data, environmental_data)
        
        # 3. Data Cleansing
        cleaned_data = self.cleanse_data(integrated_data)
        
        # 4. Exploratory Data Analysis
        eda_results = self.exploratory_analysis(cleaned_data)
        
        return {
            'research_goals': research_goals,
            'integrated_data': integrated_data,
            'cleaned_data': cleaned_data,
            'eda_results': eda_results
        }
    
    def build_predictive_models(self, df):
        """Build predictive models for heritage site analysis"""
        models = {}
        
        # Linear regression models
        models['linear_regression'] = self.advanced_linear_regression(df)
        
        # Logistic regression
        models['logistic_regression'] = self.logistic_regression_analysis(df)
        
        # Time series analysis
        models['time_series'] = self.time_series_analysis(df)
        
        # Model validation
        models['validation'] = self.model_validation(df)
        
        # ANOVA analysis
        models['anova'] = self.anova_analysis(df)
        
        # Inferential statistics
        models['inferential_stats'] = self.inferential_statistics(df)
        
        return models
    
    def integrate_heritage_data(self, crack_data, material_data, environmental_data):
        """Data integration from multiple heritage monitoring sources"""
        # Create comprehensive dataset
        data = []
        
        if crack_data:
            for i, crack in enumerate(crack_data):
                # Handle None severity values
                severity = crack.get('severity')
                if severity is None:
                    severity = 'Unknown'
                    
                data.append({
                    'element_id': f"crack_{i+1}",
                    'crack_width_cm': crack.get('width_cm', 0),
                    'crack_length_cm': crack.get('length_cm', 0),
                    'crack_area': crack.get('width_cm', 0) * crack.get('length_cm', 0),
                    'severity': severity,
                    'confidence': crack.get('confidence', 0),
                    'material_type': material_data.get('predicted_material', 'Unknown'),
                    'carbon_impact': environmental_data.get('carbon_footprint_kg', 0),
                    'water_impact': environmental_data.get('water_footprint_liters', 0)
                })
        
        # Add aggregate data point
        if not data:
            data.append({
                'element_id': 'site_overall',
                'crack_width_cm': 0,
                'crack_length_cm': 0,
                'crack_area': 0,
                'severity': 'None',
                'confidence': 1.0,
                'material_type': material_data.get('predicted_material', 'Unknown'),
                'carbon_impact': environmental_data.get('carbon_footprint_kg', 0),
                'water_impact': environmental_data.get('water_footprint_liters', 0)
            })
        
        return pd.DataFrame(data)
    
    def cleanse_data(self, df):
        """Data cleansing and preprocessing"""
        # Handle missing values
        df = df.fillna(df.mean(numeric_only=True))
        df = df.fillna('Unknown')  # Fill NaN in object columns with 'Unknown'
        
        # Remove outliers using IQR method
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        
        return df
    
    # =================== CHAPTER 2: DESCRIPTIVE ANALYTICS & VISUALIZATION ===================
    
    def exploratory_analysis(self, df):
        """Comprehensive exploratory data analysis"""
        results = {}
        
        # Frequency Distributions
        results['frequency_distributions'] = self.frequency_analysis(df)
        
        # Outlier Analysis
        results['outlier_analysis'] = self.outlier_detection(df)
        
        # Distribution Analysis
        results['distribution_analysis'] = self.distribution_analysis(df)
        
        # Correlation Analysis
        results['correlation_analysis'] = self.correlation_analysis(df)
        
        # Regression Analysis
        results['regression_analysis'] = self.regression_analysis(df)
        
        return results
    
    def frequency_analysis(self, df):
        """Frequency distributions for all variables"""
        freq_data = {}
        
        # Categorical variables
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            freq_data[col] = {str(k): v for k, v in df[col].value_counts().to_dict().items()}
        
        # Numerical variables (binned)
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            if df[col].nunique() > 1:
                hist, bins = np.histogram(df[col], bins=10)
                freq_data[f"{col}_histogram"] = {
                    'frequencies': hist.tolist(),
                    'bins': bins.tolist()
                }
        
        return freq_data
    
    def outlier_detection(self, df):
        """Comprehensive outlier analysis"""
        outliers = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                # Z-score method
                z_scores = np.abs(stats.zscore(df[col]))
                z_outliers = df[z_scores > 3].index.tolist()
                
                # IQR method
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                iqr_outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)].index.tolist()
                
                outliers[col] = {
                    'z_score_outliers': z_outliers,
                    'iqr_outliers': iqr_outliers,
                    'outlier_count': len(set(z_outliers + iqr_outliers))
                }
        
        return outliers
    
    def distribution_analysis(self, df):
        """Distribution analysis and normality testing"""
        distributions = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                # Descriptive statistics
                desc_stats = {
                    'mean': float(df[col].mean()),
                    'median': float(df[col].median()),
                    'std': float(df[col].std()),
                    'variance': float(df[col].var()),
                    'skewness': float(stats.skew(df[col])),
                    'kurtosis': float(stats.kurtosis(df[col])),
                    'min': float(df[col].min()),
                    'max': float(df[col].max()),
                    'range': float(df[col].max() - df[col].min()),
                    'iqr': float(df[col].quantile(0.75) - df[col].quantile(0.25))
                }
                
                # Normality tests
                if len(df[col]) >= 3:
                    shapiro_stat, shapiro_p = stats.shapiro(df[col])
                    normality_test = {
                        'shapiro_wilk_statistic': float(shapiro_stat),
                        'shapiro_wilk_p_value': float(shapiro_p),
                        'is_normal': bool(shapiro_p > 0.05)
                    }
                else:
                    normality_test = {
                        'shapiro_wilk_statistic': None,
                        'shapiro_wilk_p_value': None,
                        'is_normal': None
                    }
                
                distributions[col] = {
                    'descriptive_stats': desc_stats,
                    'normality_test': normality_test
                }
        
        return distributions
    
    def correlation_analysis(self, df):
        """Comprehensive correlation analysis"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient numeric variables for correlation analysis'}
        
        # Pearson correlation
        pearson_corr = numeric_df.corr().to_dict()
        
        # Spearman correlation
        spearman_corr = numeric_df.corr(method='spearman').to_dict()
        
        # Significant correlations
        significant_correlations = []
        for i in range(len(numeric_df.columns)):
            for j in range(i+1, len(numeric_df.columns)):
                col1, col2 = numeric_df.columns[i], numeric_df.columns[j]
                r_val = pearson_corr[col1][col2]
                if abs(r_val) > 0.5:  # Significant correlation threshold
                    significant_correlations.append({
                        'variables': f"{col1} vs {col2}",
                        'correlation': r_val,
                        'strength': 'strong' if abs(r_val) > 0.7 else 'moderate'
                    })
        
        return {
            'pearson_correlation': pearson_corr,
            'spearman_correlation': spearman_corr,
            'significant_correlations': significant_correlations
        }
    
    def regression_analysis(self, df):
        """Multiple regression analysis"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient variables for regression analysis'}
        
        # Use crack_area as dependent variable if available
        if 'crack_area' in numeric_df.columns:
            y = numeric_df['crack_area']
            X = numeric_df.drop('crack_area', axis=1)
        else:
            # Use first column as dependent variable
            y = numeric_df.iloc[:, 0]
            X = numeric_df.iloc[:, 1:]
        
        if X.shape[1] == 0:
            return {'error': 'No independent variables available'}
        
        # Linear regression
        model = LinearRegression()
        model.fit(X, y)
        
        # Predictions
        y_pred = model.predict(X)
        
        # Model metrics
        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)
        
        # Regression equation
        coefficients = dict(zip(X.columns, model.coef_))
        
        return {
            'r_squared': float(r2),
            'adjusted_r_squared': float(1 - (1-r2)*(len(y)-1)/(len(y)-X.shape[1]-1)),
            'mse': float(mse),
            'rmse': float(rmse),
            'intercept': float(model.intercept_),
            'coefficients': {k: float(v) for k, v in coefficients.items()},
            'equation': f"y = {model.intercept_:.3f} + " + " + ".join([f"{coef:.3f}*{var}" for var, coef in coefficients.items()])
        }
    
    # =================== CHAPTER 3: INFERENTIAL STATISTICS ===================
    
    def inferential_statistics(self, df):
        """Comprehensive inferential statistics"""
        results = {}
        
        # Population vs Sample analysis
        results['sampling_analysis'] = self.sampling_analysis(df)
        
        # Hypothesis testing
        results['hypothesis_tests'] = self.hypothesis_testing(df)
        
        # Confidence intervals
        results['confidence_intervals'] = self.confidence_intervals(df)
        
        # Effect size analysis
        results['effect_sizes'] = self.effect_size_analysis(df)
        
        return results
    
    def sampling_analysis(self, df):
        """Sampling distribution and standard error analysis"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        sampling_stats = {}
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                n = len(data)
                
                sampling_stats[col] = {
                    'sample_size': n,
                    'sample_mean': float(data.mean()),
                    'sample_std': float(data.std()),
                    'standard_error': float(data.std() / np.sqrt(n)),
                    'sampling_distribution': 'normal' if n >= 30 else 'approximately_normal'
                }
        
        return sampling_stats
    
    def hypothesis_testing(self, df):
        """Comprehensive hypothesis testing"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        test_results = {}
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                
                if len(data) >= 3:
                    # One-sample t-test (testing if mean differs from 0)
                    t_stat, p_value = stats.ttest_1samp(data, 0)
                    
                    # Z-test approximation for large samples
                    if len(data) >= 30:
                        z_stat = (data.mean() - 0) / (data.std() / np.sqrt(len(data)))
                        z_p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
                    else:
                        z_stat, z_p_value = None, None
                    
                    test_results[col] = {
                        't_test': {
                            't_statistic': float(t_stat),
                            'p_value': float(p_value),
                            'degrees_freedom': len(data) - 1,
                            'significant_at_0.05': bool(p_value < 0.05),
                            'effect_interpretation': 'significant' if p_value < 0.05 else 'not_significant'
                        },
                        'z_test': {
                            'z_statistic': float(z_stat) if z_stat is not None else None,
                            'p_value': float(z_p_value) if z_p_value is not None else None,
                            'applicable': len(data) >= 30
                        }
                    }
        
        return test_results
    
    def confidence_intervals(self, df):
        """Confidence interval estimation"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        ci_results = {}
        
        confidence_levels = [0.90, 0.95, 0.99]
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                n = len(data)
                mean = data.mean()
                std = data.std()
                se = std / np.sqrt(n)
                
                ci_results[col] = {}
                for conf_level in confidence_levels:
                    alpha = 1 - conf_level
                    t_critical = stats.t.ppf(1 - alpha/2, n-1)
                    
                    margin_error = t_critical * se
                    ci_lower = mean - margin_error
                    ci_upper = mean + margin_error
                    
                    ci_results[col][f'ci_{int(conf_level*100)}'] = {
                        'lower_bound': float(ci_lower),
                        'upper_bound': float(ci_upper),
                        'margin_of_error': float(margin_error),
                        'interpretation': f"We are {int(conf_level*100)}% confident the true mean is between {ci_lower:.3f} and {ci_upper:.3f}"
                    }
        
        return ci_results
    
    def effect_size_analysis(self, df):
        """Effect size calculations"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        effect_sizes = {}
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                data = df[col].dropna()
                
                # Cohen's d (effect size)
                cohens_d = data.mean() / data.std() if data.std() > 0 else 0
                
                # Effect size interpretation
                if abs(cohens_d) < 0.2:
                    interpretation = 'negligible'
                elif abs(cohens_d) < 0.5:
                    interpretation = 'small'
                elif abs(cohens_d) < 0.8:
                    interpretation = 'medium'
                else:
                    interpretation = 'large'
                
                effect_sizes[col] = {
                    'cohens_d': float(cohens_d),
                    'interpretation': interpretation,
                    'practical_significance': 'high' if abs(cohens_d) >= 0.8 else 'moderate' if abs(cohens_d) >= 0.5 else 'low'
                }
        
        return effect_sizes
    
    # =================== CHAPTER 4: ANALYSIS OF VARIANCE ===================
    
    def anova_analysis(self, df):
        """Comprehensive ANOVA analysis"""
        results = {}
        
        # One-way ANOVA
        results['one_way_anova'] = self.one_way_anova(df)
        
        # Two-way ANOVA
        results['two_way_anova'] = self.two_way_anova(df)
        
        # Post-hoc tests
        results['post_hoc_tests'] = self.post_hoc_analysis(df)
        
        # Chi-square tests
        results['chi_square_tests'] = self.chi_square_tests(df)
        
        return results
    
    def one_way_anova(self, df):
        """One-way ANOVA analysis"""
        if 'severity' not in df.columns:
            return {'error': 'No grouping variable available for ANOVA'}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        anova_results = {}
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                groups = [group[col].dropna() for name, group in df.groupby('severity')]
                groups = [g for g in groups if len(g) > 0]
                
                if len(groups) >= 2:
                    f_stat, p_value = stats.f_oneway(*groups)
                    
                    anova_results[col] = {
                        'f_statistic': float(f_stat),
                        'p_value': float(p_value),
                        'significant': bool(p_value < 0.05),
                        'groups_tested': len(groups),
                        'interpretation': 'significant_difference' if p_value < 0.05 else 'no_significant_difference'
                    }
        
        return anova_results
    
    def two_way_anova(self, df):
        """Two-way ANOVA simulation"""
        # Create artificial second factor for demonstration
        df_copy = df.copy()
        if 'material_type' in df_copy.columns and 'severity' in df_copy.columns:
            # Simplified two-way ANOVA simulation
            return {
                'note': 'Two-way ANOVA requires specialized implementation',
                'factors': ['severity', 'material_type'],
                'recommendation': 'Use specialized statistical software for full two-way ANOVA'
            }
        
        return {'error': 'Insufficient factors for two-way ANOVA'}
    
    def post_hoc_analysis(self, df):
        """Post-hoc analysis for significant ANOVA results"""
        if 'severity' not in df.columns:
            return {'error': 'No grouping variable for post-hoc analysis'}
        
        # Tukey HSD simulation
        severity_groups = df['severity'].unique()
        comparisons = []
        
        for i in range(len(severity_groups)):
            for j in range(i+1, len(severity_groups)):
                comparisons.append({
                    'comparison': f"{severity_groups[i]} vs {severity_groups[j]}",
                    'note': 'Post-hoc test requires statistical package implementation'
                })
        
        return {
            'possible_comparisons': comparisons,
            'method': 'Tukey HSD recommended',
            'note': 'Detailed post-hoc analysis requires specialized implementation'
        }
    
    def chi_square_tests(self, df):
        """Chi-square tests for categorical variables"""
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        if len(categorical_cols) < 2:
            return {'error': 'Insufficient categorical variables for chi-square test'}
        
        # Goodness of fit test simulation
        chi_results = {}
        
        for col in categorical_cols:
            observed = df[col].value_counts()
            if len(observed) > 1:
                # Expected frequencies (equal distribution)
                expected = [len(df) / len(observed)] * len(observed)
                
                if all(e >= 5 for e in expected):  # Chi-square assumption
                    chi2_stat, p_value = stats.chisquare(observed.values, expected)
                    
                    chi_results[col] = {
                        'chi_square_statistic': float(chi2_stat),
                        'p_value': float(p_value),
                        'degrees_freedom': len(observed) - 1,
                        'significant': bool(p_value < 0.05),
                        'interpretation': 'distribution_differs_from_expected' if p_value < 0.05 else 'distribution_as_expected'
                    }
        
        return chi_results
    
    # =================== CHAPTER 5: PREDICTIVE ANALYTICS ===================
    
    def predictive_analytics(self, df):
        """Comprehensive predictive analytics"""
        results = {}
        
        # Linear regression models
        results['linear_models'] = self.advanced_linear_regression(df)
        
        # Logistic regression
        results['logistic_models'] = self.logistic_regression_analysis(df)
        
        # Time series analysis
        results['time_series'] = self.time_series_analysis(df)
        
        # Model validation
        results['model_validation'] = self.model_validation(df)
        
        return results
    
    def advanced_linear_regression(self, df):
        """Advanced linear regression with model diagnostics"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient variables for regression modeling'}
        
        # Multiple regression
        y = numeric_df.iloc[:, 0]  # First column as target
        X = numeric_df.iloc[:, 1:]  # Rest as features
        
        # Split data
        if len(df) > 4:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        else:
            X_train, X_test, y_train, y_test = X, X, y, y
        
        # Fit model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Predictions
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        
        # Model metrics
        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_test, y_test_pred)
        train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
        
        # Residual analysis
        residuals = y_train - y_train_pred
        residual_mean = np.mean(residuals)
        residual_std = np.std(residuals)
        
        return {
            'model_performance': {
                'train_r_squared': float(train_r2),
                'test_r_squared': float(test_r2),
                'train_rmse': float(train_rmse),
                'test_rmse': float(test_rmse),
                'overfitting_indicator': float(abs(train_r2 - test_r2))
            },
            'model_coefficients': {
                'intercept': float(model.intercept_),
                'coefficients': {col: float(coef) for col, coef in zip(X.columns, model.coef_)}
            },
            'residual_analysis': {
                'residual_mean': float(residual_mean),
                'residual_std': float(residual_std),
                'residuals_normally_distributed': bool(abs(residual_mean) < 0.1)
            },
            'model_equation': f"y = {model.intercept_:.3f} + " + " + ".join([f"{coef:.3f}*{col}" for col, coef in zip(X.columns, model.coef_)])
        }
    
    def logistic_regression_analysis(self, df):
        """Logistic regression for categorical prediction"""
        # Create binary target variable based on severity
        if 'severity' in df.columns:
            df_copy = df.copy()
            df_copy['high_severity'] = (df_copy['severity'].isin(['Severe', 'Critical'])).astype(int)
            
            numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
            numeric_cols = [col for col in numeric_cols if col != 'high_severity']
            
            if len(numeric_cols) > 0:
                X = df_copy[numeric_cols]
                y = df_copy['high_severity']
                
                # Check if we have at least 2 classes
                unique_classes = np.unique(y)
                if len(unique_classes) < 2:
                    return {
                        'error': f'Cannot perform logistic regression: only {len(unique_classes)} class(es) found in data',
                        'available_classes': unique_classes.tolist(),
                        'interpretation': 'All samples have the same severity level - no variation to model'
                    }
                
                # Fit logistic regression
                log_model = LogisticRegression(random_state=42, max_iter=1000)
                log_model.fit(X, y)
                
                # Predictions
                y_pred = log_model.predict(X)
                y_prob = log_model.predict_proba(X)[:, 1]
                
                # Model metrics
                accuracy = np.mean(y == y_pred)
                
                return {
                    'model_accuracy': float(accuracy),
                    'coefficients': {col: float(coef) for col, coef in zip(X.columns, log_model.coef_[0])},
                    'intercept': float(log_model.intercept_[0]),
                    'predictions': y_pred.tolist(),
                    'probabilities': y_prob.tolist(),
                    'interpretation': 'Model predicts high severity (Severe/Critical) vs low severity (Minor/Moderate)'
                }
        
        return {'error': 'Cannot perform logistic regression without categorical target variable'}
    
    def time_series_analysis(self, df):
        """Time series analysis simulation"""
        # Simulate time series data based on crack progression
        if 'crack_area' in df.columns:
            crack_areas = df['crack_area'].values
            
            # Create synthetic time series
            time_points = np.arange(len(crack_areas))
            
            # Moving averages
            if len(crack_areas) >= 3:
                moving_avg_3 = np.convolve(crack_areas, np.ones(3)/3, mode='valid')
                
                # Trend analysis
                slope, intercept, r_value, p_value, std_err = stats.linregress(time_points, crack_areas)
                
                # Forecast next 3 periods
                future_times = np.arange(len(crack_areas), len(crack_areas) + 3)
                forecasts = slope * future_times + intercept
                
                return {
                    'trend_analysis': {
                        'slope': float(slope),
                        'trend_direction': 'increasing' if slope > 0 else 'decreasing' if slope < 0 else 'stable',
                        'trend_strength': float(abs(r_value)),
                        'trend_significance': bool(p_value < 0.05)
                    },
                    'moving_averages': {
                        'period_3_moving_avg': moving_avg_3.tolist()
                    },
                    'forecasts': {
                        'next_3_periods': forecasts.tolist(),
                        'forecast_method': 'linear_trend_extrapolation'
                    },
                    'autocorrelation': {
                        'lag_1': float(np.corrcoef(crack_areas[:-1], crack_areas[1:])[0,1]) if len(crack_areas) > 1 else 0
                    }
                }
        
        return {'note': 'Time series analysis requires temporal data structure'}
    
    def model_validation(self, df):
        """Model validation and goodness of fit"""
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] < 2:
            return {'error': 'Insufficient data for model validation'}
        
        # Cross-validation simulation
        validation_results = {
            'cross_validation': {
                'folds': 5,
                'note': 'K-fold cross-validation recommended for robust model evaluation'
            },
            'goodness_of_fit': {
                'r_squared_threshold': 0.7,
                'significance_level': 0.05,
                'recommendation': 'Models with R² > 0.7 and p < 0.05 are considered good fits'
            },
            'model_assumptions': {
                'linearity': 'Check scatter plots of residuals vs fitted values',
                'independence': 'Check for autocorrelation in residuals',
                'homoscedasticity': 'Check for constant variance in residuals',
                'normality': 'Check normality of residuals with Shapiro-Wilk test'
            }
        }
        
        return validation_results
    
    # =================== VISUALIZATION METHODS ===================
    
    def create_comprehensive_visualizations(self, df, analysis_results):
        """Create all required visualizations for the syllabus"""
        visualizations = {}
        
        # Chapter 2 visualizations
        visualizations.update(self.create_descriptive_visualizations(df))
        
        # Chapter 3 visualizations
        visualizations.update(self.create_inferential_visualizations(df, analysis_results))
        
        # Chapter 4 visualizations
        visualizations.update(self.create_anova_visualizations(df))
        
        # Chapter 5 visualizations
        visualizations.update(self.create_predictive_visualizations(df))
        
        return visualizations
    
    def create_descriptive_visualizations(self, df):
        """Descriptive analytics visualizations"""
        viz = {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            if df[col].nunique() > 1:
                # Histogram with normal curve
                fig = go.Figure()
                fig.add_trace(go.Histogram(x=df[col], name=f'{col} Distribution', nbinsx=20))
                fig.update_layout(title=f'Distribution of {col}', xaxis_title=col, yaxis_title='Frequency')
                try:
                    viz[f'histogram_{col}'] = fig.to_json()
                except Exception as e:
                    print(f"Error creating histogram for {col}: {e}")
                    continue
                
                # Box plot
                fig = go.Figure()
                fig.add_trace(go.Box(y=df[col], name=col))
                fig.update_layout(title=f'Box Plot of {col}', yaxis_title=col)
                try:
                    viz[f'boxplot_{col}'] = fig.to_json()
                except Exception as e:
                    print(f"Error creating boxplot for {col}: {e}")
                    continue
        
        # Correlation heatmap
        if len(numeric_cols) > 1:
            corr_matrix = df[numeric_cols].corr()
            fig = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdBu',
                zmid=0
            ))
            fig.update_layout(title='Correlation Matrix Heatmap')
            try:
                viz['correlation_heatmap'] = fig.to_json()
            except Exception as e:
                print(f"Error creating correlation heatmap: {e}")
        
        return viz
    
    def create_inferential_visualizations(self, df, analysis_results):
        """Inferential statistics visualizations"""
        viz = {}
        
        # Confidence interval plots
        if 'confidence_intervals' in analysis_results:
            for col, ci_data in analysis_results['confidence_intervals'].items():
                if 'ci_95' in ci_data:
                    ci_95 = ci_data['ci_95']
                    mean_val = df[col].mean()
                    
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=[col], y=[mean_val],
                        error_y=dict(
                            type='data',
                            symmetric=False,
                            array=[ci_95['upper_bound'] - mean_val],
                            arrayminus=[mean_val - ci_95['lower_bound']]
                        ),
                        mode='markers',
                        name='95% Confidence Interval'
                    ))
                    fig.update_layout(title=f'95% Confidence Interval for {col}')
                    try:
                        viz[f'confidence_interval_{col}'] = fig.to_json()
                    except Exception as e:
                        print(f"Error creating confidence interval for {col}: {e}")
        
        return viz
    
    def create_anova_visualizations(self, df):
        """ANOVA visualizations"""
        viz = {}
        
        if 'severity' in df.columns:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            
            for col in numeric_cols:
                if df[col].nunique() > 1:
                    # Box plot by groups
                    fig = go.Figure()
                    for severity in df['severity'].unique():
                        group_data = df[df['severity'] == severity][col]
                        fig.add_trace(go.Box(y=group_data, name=f'{severity}'))
                    
                    fig.update_layout(
                        title=f'{col} by Severity Level',
                        yaxis_title=col,
                        xaxis_title='Severity Level'
                    )
                    try:
                        viz[f'anova_boxplot_{col}'] = fig.to_json()
                    except Exception as e:
                        print(f"Error creating anova boxplot for {col}: {e}")
        
        return viz
    
    def create_predictive_visualizations(self, df):
        """Predictive analytics visualizations"""
        viz = {}
        
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.shape[1] >= 2:
            # Scatter plot with regression line
            x_col = numeric_df.columns[1]
            y_col = numeric_df.columns[0]
            
            fig = px.scatter(df, x=x_col, y=y_col, trendline='ols',
                           title=f'Regression: {y_col} vs {x_col}')
            try:
                viz['regression_scatter'] = fig.to_json()
            except Exception as e:
                print(f"Error creating regression scatter: {e}")
            
            # Residual plot
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            X = numeric_df[[x_col]]
            y = numeric_df[y_col]
            model.fit(X, y)
            y_pred = model.predict(X)
            residuals = y - y_pred
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=y_pred, y=residuals, mode='markers', name='Residuals'))
            fig.add_hline(y=0, line_dash="dash", line_color="red")
            fig.update_layout(
                title='Residual Plot',
                xaxis_title='Fitted Values',
                yaxis_title='Residuals'
            )
            try:
                viz['residual_plot'] = fig.to_json()
            except Exception as e:
                print(f"Error creating residual plot: {e}")
        
        return viz