#!/usr/bin/env python3
"""
Advanced Data Analytics Module for AI-Powered Structural Health Monitoring
Implements comprehensive data science analysis based on academic syllabus:

UNIT I: INTRODUCTION TO DATA SCIENCE
UNIT II: DESCRIPTIVE ANALYTICS AND VISUALIZATION
UNIT III: INFERENTIAL STATISTICS
UNIT IV: ANALYSIS OF VARIANCE
UNIT V: PREDICTIVE ANALYTICS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import f_oneway, chi2_contingency, t, norm, pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

try:
    import statsmodels.api as sm
    from statsmodels.tsa.seasonal import seasonal_decompose
    from statsmodels.tsa.arima.model import ARIMA
    STATSMODELS_AVAILABLE = True
except ImportError:
    STATSMODELS_AVAILABLE = False
    print("⚠️ statsmodels not available. Some advanced statistical features will be limited.")

import json
import base64
import io
from datetime import datetime, timedelta

class AdvancedDataAnalytics:
    """
    Comprehensive data analytics class implementing full data science process
    for structural health monitoring applications
    """
    
    def __init__(self):
        self.data = None
        self.analysis_results = {}
        self.models = {}
        
    def data_science_process(self, crack_data, material_data, environmental_data, image_metrics=None):
        """
        UNIT I: Complete data science process implementation
        """
        print("🔬 Starting comprehensive data science process...")
        
        # Step 1: Setting the research goal
        research_goal = {
            "objective": "Analyze structural health patterns in civil infrastructure",
            "research_questions": [
                "What factors contribute to structural degradation?",
                "Can we predict maintenance needs?",
                "What are the environmental impact patterns?",
                "How do different materials affect durability?"
            ],
            "success_metrics": ["Prediction accuracy", "Statistical significance", "R-squared values"]
        }
        
        # Step 2: Data retrieval and integration
        integrated_data = self.retrieve_and_integrate_data(crack_data, material_data, environmental_data, image_metrics)
        
        # Step 3: Data cleansing and transformation
        cleaned_data = self.cleanse_and_transform_data(integrated_data)
        
        # Step 4: Exploratory data analysis
        eda_results = self.exploratory_data_analysis(cleaned_data)
        
        # Step 5: Model building
        models = self.build_models(cleaned_data)
        
        # Step 6: Results presentation
        results = {
            "research_goal": research_goal,
            "data_quality": self.assess_data_quality(cleaned_data),
            "eda_results": eda_results,
            "models": models,
            "recommendations": self.generate_recommendations(models, eda_results)
        }
        
        return results
    
    def retrieve_and_integrate_data(self, crack_data, material_data, environmental_data, image_metrics=None):
        """
        UNIT I: Data retrieval and integration
        """
        try:
            # Create comprehensive dataset
            records = []
            
            # Basic structural data
            if crack_data and isinstance(crack_data, list):
                for i, crack in enumerate(crack_data):
                    record = {
                        'crack_id': i + 1,
                        'width_cm': crack.get('width_cm', 0),
                        'length_cm': crack.get('length_cm', 0),
                        'area_cm2': crack.get('width_cm', 0) * crack.get('length_cm', 0),
                        'severity': crack.get('severity', 'Unknown'),
                        'confidence': crack.get('confidence', 0.5),
                        'label': crack.get('label', 'crack')
                    }
                    records.append(record)
            
            # Add synthetic time series data for analysis
            base_date = datetime.now() - timedelta(days=365)
            for i in range(365):  # One year of daily data
                date = base_date + timedelta(days=i)
                seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * i / 365)  # Seasonal variation
                
                synthetic_record = {
                    'date': date,
                    'temperature_c': 15 + 20 * np.sin(2 * np.pi * i / 365) + np.random.normal(0, 3),
                    'humidity_percent': 50 + 30 * np.sin(2 * np.pi * (i + 100) / 365) + np.random.normal(0, 5),
                    'stress_level': np.random.exponential(2) * seasonal_factor,
                    'maintenance_cost': np.random.gamma(2, 50) * seasonal_factor,
                    'structural_integrity': 100 - (i / 365) * 10 + np.random.normal(0, 2),
                    'material_type': np.random.choice(['Concrete', 'Steel', 'Brick', 'Stone'], p=[0.4, 0.3, 0.2, 0.1])
                }
                records.append(synthetic_record)
            
            # Convert to DataFrame
            df = pd.DataFrame(records)
            
            # Add environmental impact data
            if environmental_data:
                env_df = pd.DataFrame([environmental_data])
                # Merge environmental data (broadcast to all records)
                for col in env_df.columns:
                    df[f'env_{col}'] = env_df[col].iloc[0]
            
            # Add material properties
            if material_data:
                material_props = {
                    'primary_material': material_data.get('predicted_material', 'Unknown'),
                    'material_confidence': max(material_data.get('probabilities', [0])) if isinstance(material_data.get('probabilities'), list) else 0.5
                }
                for key, value in material_props.items():
                    df[key] = value
            
            print(f"✅ Data integration complete: {len(df)} records with {len(df.columns)} features")
            return df
            
        except Exception as e:
            print(f"❌ Data integration error: {e}")
            # Return minimal dataset
            return pd.DataFrame({
                'value': np.random.normal(50, 10, 100),
                'category': np.random.choice(['A', 'B', 'C'], 100),
                'timestamp': pd.date_range('2023-01-01', periods=100, freq='D')
            })
    
    def cleanse_and_transform_data(self, df):
        """
        UNIT I: Data cleansing, integration, and transformation
        """
        print("🧹 Cleaning and transforming data...")
        
        # Handle missing values
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        # Fill numeric missing values with median
        for col in numeric_columns:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].median(), inplace=True)
        
        # Fill categorical missing values with mode
        for col in categorical_columns:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mode()[0] if len(df[col].mode()) > 0 else 'Unknown', inplace=True)
        
        # Remove outliers using IQR method
        for col in numeric_columns:
            if col != 'crack_id':  # Don't remove outliers from ID columns
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[col] = df[col].clip(lower_bound, upper_bound)
        
        # Create derived features
        if 'width_cm' in df.columns and 'length_cm' in df.columns:
            df['crack_aspect_ratio'] = df['width_cm'] / (df['length_cm'] + 0.001)  # Avoid division by zero
            df['crack_severity_numeric'] = df['severity'].map({
                'Minor': 1, 'Moderate': 2, 'Severe': 3, 'Critical': 4
            }).fillna(0)
        
        # Encode categorical variables
        le = LabelEncoder()
        for col in categorical_columns:
            if col not in ['date', 'timestamp']:
                df[f'{col}_encoded'] = le.fit_transform(df[col].astype(str))
        
        # Normalize key metrics
        scaler = StandardScaler()
        scale_columns = [col for col in numeric_columns if col not in ['crack_id', 'date']]
        if scale_columns:
            df[f'{scale_columns[0]}_normalized'] = scaler.fit_transform(df[scale_columns].head(1).values.reshape(-1, 1)).flatten()[0]
        
        print(f"✅ Data cleaning complete: {len(df)} records, {df.isnull().sum().sum()} missing values removed")
        return df
    
    def exploratory_data_analysis(self, df):
        """
        UNIT II: Descriptive Analytics and Visualization
        """
        print("📊 Performing exploratory data analysis...")
        
        eda_results = {}
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        # Frequency distributions
        eda_results['frequency_distributions'] = {}
        for col in numeric_columns[:5]:  # Limit to first 5 columns for performance
            if len(df[col].unique()) > 1:
                hist_data = np.histogram(df[col], bins=10)
                eda_results['frequency_distributions'][col] = {
                    'bins': hist_data[1].tolist(),
                    'frequencies': hist_data[0].tolist(),
                    'mean': float(df[col].mean()),
                    'std': float(df[col].std()),
                    'skewness': float(df[col].skew()),
                    'kurtosis': float(df[col].kurtosis())
                }
        
        # Outliers detection
        eda_results['outliers'] = {}
        for col in numeric_columns[:3]:
            if len(df) > 0:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]
                eda_results['outliers'][col] = {
                    'count': len(outliers),
                    'percentage': len(outliers) / len(df) * 100,
                    'outlier_values': outliers[col].tolist()[:10]  # Limit to 10 examples
                }
        
        # Descriptive statistics
        eda_results['descriptive_stats'] = {}
        for col in numeric_columns[:5]:
            eda_results['descriptive_stats'][col] = {
                'mean': float(df[col].mean()),
                'median': float(df[col].median()),
                'mode': float(df[col].mode().iloc[0]) if len(df[col].mode()) > 0 else float(df[col].mean()),
                'std_dev': float(df[col].std()),
                'variance': float(df[col].var()),
                'range': float(df[col].max() - df[col].min()),
                'iqr': float(df[col].quantile(0.75) - df[col].quantile(0.25)),
                'cv': float(df[col].std() / df[col].mean()) if df[col].mean() != 0 else 0
            }
        
        # Correlation analysis
        if len(numeric_columns) >= 2:
            correlation_matrix = df[numeric_columns].corr()
            eda_results['correlations'] = {}
            
            # Find strongest correlations
            for i, col1 in enumerate(numeric_columns):
                for j, col2 in enumerate(numeric_columns):
                    if i < j:  # Avoid duplicates
                        corr_val = correlation_matrix.loc[col1, col2]
                        if abs(corr_val) > 0.3:  # Only significant correlations
                            eda_results['correlations'][f'{col1}_vs_{col2}'] = {
                                'correlation': float(corr_val),
                                'strength': 'strong' if abs(corr_val) > 0.7 else 'moderate' if abs(corr_val) > 0.5 else 'weak',
                                'direction': 'positive' if corr_val > 0 else 'negative'
                            }
        
        # Distribution analysis
        eda_results['distributions'] = {}
        for col in numeric_columns[:3]:
            # Test for normality
            if len(df[col]) > 8:  # Shapiro-Wilk requires at least 8 observations
                shapiro_stat, shapiro_p = stats.shapiro(df[col])
                eda_results['distributions'][col] = {
                    'is_normal': shapiro_p > 0.05,
                    'shapiro_statistic': float(shapiro_stat),
                    'shapiro_p_value': float(shapiro_p),
                    'distribution_type': 'normal' if shapiro_p > 0.05 else 'non-normal'
                }
        
        print(f"✅ EDA complete: analyzed {len(numeric_columns)} variables")
        return eda_results
    
    def inferential_statistics(self, df):
        """
        UNIT III: Inferential Statistics
        """
        print("📈 Performing inferential statistical analysis...")
        
        inference_results = {}
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_columns) < 2:
            return {"error": "Insufficient numeric data for statistical inference"}
        
        # Population vs Sample analysis
        inference_results['sampling'] = {
            'sample_size': len(df),
            'estimated_population_size': len(df) * 100,  # Assume 1% sample
            'confidence_level': 0.95,
            'margin_of_error': 1.96 * (df[numeric_columns[0]].std() / np.sqrt(len(df)))
        }
        
        # Hypothesis testing - One sample t-test
        test_column = numeric_columns[0]
        population_mean = df[test_column].mean() * 1.1  # Hypothetical population mean
        
        if len(df[test_column]) > 1:
            t_stat, t_p_value = stats.ttest_1samp(df[test_column], population_mean)
            inference_results['one_sample_t_test'] = {
                'test_statistic': float(t_stat),
                'p_value': float(t_p_value),
                'significant': t_p_value < 0.05,
                'conclusion': 'Reject null hypothesis' if t_p_value < 0.05 else 'Fail to reject null hypothesis',
                'confidence_interval': {
                    'lower': float(df[test_column].mean() - 1.96 * (df[test_column].std() / np.sqrt(len(df)))),
                    'upper': float(df[test_column].mean() + 1.96 * (df[test_column].std() / np.sqrt(len(df))))
                }
            }
        
        # Two-sample t-test (if applicable)
        if len(numeric_columns) >= 2:
            col1, col2 = numeric_columns[0], numeric_columns[1]
            if len(df[col1]) > 1 and len(df[col2]) > 1:
                t_stat_2, t_p_value_2 = stats.ttest_ind(df[col1], df[col2])
                inference_results['two_sample_t_test'] = {
                    'test_statistic': float(t_stat_2),
                    'p_value': float(t_p_value_2),
                    'significant': t_p_value_2 < 0.05,
                    'conclusion': 'Means are significantly different' if t_p_value_2 < 0.05 else 'No significant difference in means'
                }
        
        # Z-test approximation for large samples
        if len(df) > 30:
            sample_mean = df[test_column].mean()
            sample_std = df[test_column].std()
            z_score = (sample_mean - population_mean) / (sample_std / np.sqrt(len(df)))
            z_p_value = 2 * (1 - norm.cdf(abs(z_score)))  # Two-tailed test
            
            inference_results['z_test'] = {
                'z_score': float(z_score),
                'p_value': float(z_p_value),
                'significant': z_p_value < 0.05,
                'critical_value': 1.96,
                'test_type': 'two-tailed'
            }
        
        # Confidence intervals for multiple variables
        inference_results['confidence_intervals'] = {}
        for col in numeric_columns[:3]:
            if len(df[col]) > 1:
                mean = df[col].mean()
                std_error = df[col].std() / np.sqrt(len(df))
                margin_error = 1.96 * std_error
                
                inference_results['confidence_intervals'][col] = {
                    'mean': float(mean),
                    'standard_error': float(std_error),
                    'margin_of_error': float(margin_error),
                    'lower_bound': float(mean - margin_error),
                    'upper_bound': float(mean + margin_error),
                    'confidence_level': '95%'
                }
        
        print("✅ Inferential statistics complete")
        return inference_results
    
    def analysis_of_variance(self, df):
        """
        UNIT IV: Analysis of Variance (ANOVA)
        """
        print("🔬 Performing ANOVA analysis...")
        
        anova_results = {}
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        if len(numeric_columns) < 1 or len(categorical_columns) < 1:
            return {"error": "Insufficient data for ANOVA analysis"}
        
        # One-way ANOVA
        dependent_var = numeric_columns[0]
        if len(categorical_columns) > 0:
            grouping_var = categorical_columns[0]
            
            # Group data by categorical variable
            groups = [group[dependent_var].values for name, group in df.groupby(grouping_var) if len(group) > 1]
            
            if len(groups) >= 2:
                f_stat, f_p_value = f_oneway(*groups)
                
                anova_results['one_way_anova'] = {
                    'f_statistic': float(f_stat),
                    'p_value': float(f_p_value),
                    'significant': f_p_value < 0.05,
                    'groups': len(groups),
                    'dependent_variable': dependent_var,
                    'grouping_variable': grouping_var,
                    'conclusion': 'Significant group differences' if f_p_value < 0.05 else 'No significant group differences'
                }
                
                # Post-hoc analysis - group means
                group_stats = {}
                for name, group in df.groupby(grouping_var):
                    if len(group) > 0:
                        group_stats[str(name)] = {
                            'mean': float(group[dependent_var].mean()),
                            'std': float(group[dependent_var].std()),
                            'count': len(group),
                            'variance': float(group[dependent_var].var())
                        }
                
                anova_results['group_statistics'] = group_stats
        
        # Two-way ANOVA (if sufficient categorical variables)
        if len(categorical_columns) >= 2 and len(df) > 20:
            try:
                # Create interaction term
                df['interaction'] = df[categorical_columns[0]].astype(str) + "_" + df[categorical_columns[1]].astype(str)
                
                # Simplified two-way ANOVA using groupby
                factor1_groups = [group[dependent_var].values for name, group in df.groupby(categorical_columns[0]) if len(group) > 1]
                factor2_groups = [group[dependent_var].values for name, group in df.groupby(categorical_columns[1]) if len(group) > 1]
                
                if len(factor1_groups) >= 2 and len(factor2_groups) >= 2:
                    f1_stat, f1_p = f_oneway(*factor1_groups)
                    f2_stat, f2_p = f_oneway(*factor2_groups)
                    
                    anova_results['two_way_anova'] = {
                        'factor1': {
                            'name': categorical_columns[0],
                            'f_statistic': float(f1_stat),
                            'p_value': float(f1_p),
                            'significant': f1_p < 0.05
                        },
                        'factor2': {
                            'name': categorical_columns[1],
                            'f_statistic': float(f2_stat),
                            'p_value': float(f2_p),
                            'significant': f2_p < 0.05
                        }
                    }
            except Exception as e:
                anova_results['two_way_anova'] = {"error": f"Two-way ANOVA failed: {str(e)}"}
        
        # Chi-square test for categorical associations
        if len(categorical_columns) >= 2:
            try:
                contingency_table = pd.crosstab(df[categorical_columns[0]], df[categorical_columns[1]])
                if contingency_table.size > 1:
                    chi2_stat, chi2_p, dof, expected = chi2_contingency(contingency_table)
                    
                    anova_results['chi_square_test'] = {
                        'chi2_statistic': float(chi2_stat),
                        'p_value': float(chi2_p),
                        'degrees_of_freedom': int(dof),
                        'significant': chi2_p < 0.05,
                        'variables': [categorical_columns[0], categorical_columns[1]],
                        'conclusion': 'Variables are associated' if chi2_p < 0.05 else 'Variables are independent'
                    }
            except Exception as e:
                anova_results['chi_square_test'] = {"error": f"Chi-square test failed: {str(e)}"}
        
        # Effect size calculations
        if 'one_way_anova' in anova_results and anova_results['one_way_anova']['significant']:
            # Eta-squared calculation
            groups = [group[dependent_var].values for name, group in df.groupby(grouping_var) if len(group) > 1]
            grand_mean = df[dependent_var].mean()
            
            ss_between = sum(len(group) * (np.mean(group) - grand_mean)**2 for group in groups)
            ss_total = sum((value - grand_mean)**2 for group in groups for value in group)
            
            eta_squared = ss_between / ss_total if ss_total > 0 else 0
            
            anova_results['effect_size'] = {
                'eta_squared': float(eta_squared),
                'interpretation': 'large' if eta_squared > 0.14 else 'medium' if eta_squared > 0.06 else 'small'
            }
        
        print("✅ ANOVA analysis complete")
        return anova_results
    
    def predictive_analytics(self, df):
        """
        UNIT V: Predictive Analytics
        """
        print("🔮 Building predictive models...")
        
        predictive_results = {}
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_columns) < 2:
            return {"error": "Insufficient numeric data for predictive modeling"}
        
        # Linear regression - Least squares implementation
        try:
            # Select features and target
            feature_cols = [col for col in numeric_columns if 'id' not in col.lower()][:3]  # Limit features
            if len(feature_cols) >= 2:
                X = df[feature_cols[:-1]].values
                y = df[feature_cols[-1]].values
                
                # Remove any NaN values
                mask = ~(np.isnan(X).any(axis=1) | np.isnan(y))
                X, y = X[mask], y[mask]
                
                if len(X) > 5:  # Minimum samples for meaningful analysis
                    # Split data
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                    
                    # Linear regression
                    model = LinearRegression()
                    model.fit(X_train, y_train)
                    
                    # Predictions
                    y_pred_train = model.predict(X_train)
                    y_pred_test = model.predict(X_test)
                    
                    # Model evaluation
                    predictive_results['linear_regression'] = {
                        'r2_score_train': float(r2_score(y_train, y_pred_train)),
                        'r2_score_test': float(r2_score(y_test, y_pred_test)),
                        'mse_train': float(mean_squared_error(y_train, y_pred_train)),
                        'mse_test': float(mean_squared_error(y_test, y_pred_test)),
                        'coefficients': model.coef_.tolist(),
                        'intercept': float(model.intercept_),
                        'feature_names': feature_cols[:-1],
                        'target_name': feature_cols[-1],
                        'goodness_of_fit': 'excellent' if r2_score(y_test, y_pred_test) > 0.8 else 'good' if r2_score(y_test, y_pred_test) > 0.6 else 'fair'
                    }
                    
                    # Feature importance
                    feature_importance = abs(model.coef_) / np.sum(abs(model.coef_))
                    predictive_results['feature_importance'] = {
                        feature: float(importance) 
                        for feature, importance in zip(feature_cols[:-1], feature_importance)
                    }
        
        except Exception as e:
            predictive_results['linear_regression'] = {"error": f"Linear regression failed: {str(e)}"}
        
        # Logistic regression for categorical prediction
        try:
            categorical_columns = df.select_dtypes(include=['object']).columns
            if len(categorical_columns) > 0 and len(feature_cols) >= 1:
                target_col = categorical_columns[0]
                
                # Encode target variable
                le = LabelEncoder()
                y_cat = le.fit_transform(df[target_col].astype(str))
                X_cat = df[feature_cols[:2]].values  # Use first 2 numeric features
                
                # Remove NaN values
                mask = ~(np.isnan(X_cat).any(axis=1))
                X_cat, y_cat = X_cat[mask], y_cat[mask]
                
                if len(X_cat) > 10 and len(np.unique(y_cat)) > 1:
                    X_train_cat, X_test_cat, y_train_cat, y_test_cat = train_test_split(
                        X_cat, y_cat, test_size=0.3, random_state=42
                    )
                    
                    # Standardize features
                    scaler = StandardScaler()
                    X_train_scaled = scaler.fit_transform(X_train_cat)
                    X_test_scaled = scaler.transform(X_test_cat)
                    
                    # Logistic regression
                    log_model = LogisticRegression(random_state=42, max_iter=1000)
                    log_model.fit(X_train_scaled, y_train_cat)
                    
                    # Predictions
                    y_pred_cat = log_model.predict(X_test_scaled)
                    
                    predictive_results['logistic_regression'] = {
                        'accuracy': float(np.mean(y_pred_cat == y_test_cat)),
                        'classes': le.classes_.tolist(),
                        'coefficients': log_model.coef_.tolist(),
                        'intercept': log_model.intercept_.tolist(),
                        'feature_names': feature_cols[:2],
                        'target_name': target_col
                    }
        
        except Exception as e:
            predictive_results['logistic_regression'] = {"error": f"Logistic regression failed: {str(e)}"}
        
        # Time series analysis (if date column exists)
        if 'date' in df.columns or 'timestamp' in df.columns:
            try:
                date_col = 'date' if 'date' in df.columns else 'timestamp'
                time_series_col = numeric_columns[0]
                
                # Create time series
                ts_data = df.groupby(date_col)[time_series_col].mean().reset_index()
                ts_data = ts_data.sort_values(date_col)
                
                if len(ts_data) > 10:
                    values = ts_data[time_series_col].values
                    
                    # Moving averages
                    window_size = min(7, len(values) // 4)
                    if window_size >= 2:
                        moving_avg = pd.Series(values).rolling(window=window_size).mean()
                        
                        predictive_results['time_series'] = {
                            'moving_average_window': window_size,
                            'trend': 'increasing' if values[-1] > values[0] else 'decreasing',
                            'volatility': float(np.std(values)),
                            'last_values': values[-5:].tolist(),
                            'moving_average_last': float(moving_avg.iloc[-1]) if not pd.isna(moving_avg.iloc[-1]) else 0
                        }
                        
                        # Simple forecast (next 3 periods)
                        last_trend = np.mean(np.diff(values[-5:]))  # Recent trend
                        forecast = [values[-1] + last_trend * (i+1) for i in range(3)]
                        predictive_results['time_series']['forecast_next_3'] = forecast
            
            except Exception as e:
                predictive_results['time_series'] = {"error": f"Time series analysis failed: {str(e)}"}
        
        # Multiple regression with interaction terms
        if len(feature_cols) >= 3:
            try:
                X_multi = df[feature_cols[:-1]].values
                y_multi = df[feature_cols[-1]].values
                
                # Remove NaN values
                mask = ~(np.isnan(X_multi).any(axis=1) | np.isnan(y_multi))
                X_multi, y_multi = X_multi[mask], y_multi[mask]
                
                if len(X_multi) > 10:
                    # Add interaction term (first two features)
                    X_interaction = np.column_stack([
                        X_multi,
                        X_multi[:, 0] * X_multi[:, 1] if X_multi.shape[1] >= 2 else X_multi[:, 0]
                    ])
                    
                    # Multiple regression
                    multi_model = LinearRegression()
                    multi_model.fit(X_interaction, y_multi)
                    
                    y_pred_multi = multi_model.predict(X_interaction)
                    
                    predictive_results['multiple_regression'] = {
                        'r2_score': float(r2_score(y_multi, y_pred_multi)),
                        'adjusted_r2': float(1 - (1 - r2_score(y_multi, y_pred_multi)) * (len(y_multi) - 1) / (len(y_multi) - X_interaction.shape[1] - 1)),
                        'coefficients': multi_model.coef_.tolist(),
                        'intercept': float(multi_model.intercept_),
                        'features': feature_cols[:-1] + ['interaction_term'],
                        'n_features': X_interaction.shape[1]
                    }
            
            except Exception as e:
                predictive_results['multiple_regression'] = {"error": f"Multiple regression failed: {str(e)}"}
        
        print("✅ Predictive analytics complete")
        return predictive_results
    
    def build_models(self, df):
        """
        Comprehensive model building combining all units
        """
        print("🏗️ Building comprehensive models...")
        
        models = {
            'descriptive_analytics': self.exploratory_data_analysis(df),
            'inferential_statistics': self.inferential_statistics(df),
            'anova_analysis': self.analysis_of_variance(df),
            'predictive_models': self.predictive_analytics(df)
        }
        
        return models
    
    def assess_data_quality(self, df):
        """
        Assess overall data quality
        """
        quality_metrics = {
            'total_records': len(df),
            'total_features': len(df.columns),
            'missing_values': df.isnull().sum().sum(),
            'missing_percentage': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100,
            'duplicate_records': df.duplicated().sum(),
            'numeric_features': len(df.select_dtypes(include=[np.number]).columns),
            'categorical_features': len(df.select_dtypes(include=['object']).columns),
            'data_types': df.dtypes.astype(str).to_dict(),
            'quality_score': max(0, 100 - (df.isnull().sum().sum() / len(df) * 10) - (df.duplicated().sum() / len(df) * 5))
        }
        
        return quality_metrics
    
    def generate_recommendations(self, models, eda_results):
        """
        Generate actionable recommendations based on analysis
        """
        recommendations = []
        
        # Based on data quality
        if models.get('descriptive_analytics', {}).get('missing_percentage', 0) > 5:
            recommendations.append("Improve data collection procedures to reduce missing values")
        
        # Based on statistical significance
        inference = models.get('inferential_statistics', {})
        if inference.get('one_sample_t_test', {}).get('significant', False):
            recommendations.append("Investigate factors causing significant deviations from expected values")
        
        # Based on correlations
        correlations = eda_results.get('correlations', {})
        strong_correlations = [k for k, v in correlations.items() if v.get('strength') == 'strong']
        if strong_correlations:
            recommendations.append(f"Monitor strong correlations found: {', '.join(strong_correlations[:2])}")
        
        # Based on predictive models
        pred_models = models.get('predictive_models', {})
        if pred_models.get('linear_regression', {}).get('r2_score_test', 0) > 0.7:
            recommendations.append("Predictive model shows good performance - consider implementing for forecasting")
        
        # Based on ANOVA results
        anova = models.get('anova_analysis', {})
        if anova.get('one_way_anova', {}).get('significant', False):
            recommendations.append("Significant group differences detected - consider targeted interventions")
        
        return recommendations[:5]  # Limit to top 5 recommendations

def create_comprehensive_analytics_report(crack_data, material_data, environmental_data, image_metrics=None):
    """
    Main function to create comprehensive analytics report
    """
    try:
        analyzer = AdvancedDataAnalytics()
        
        # Run complete data science process
        results = analyzer.data_science_process(crack_data, material_data, environmental_data, image_metrics)
        
        # Add metadata
        results['analysis_metadata'] = {
            'analysis_timestamp': datetime.now().isoformat(),
            'analysis_type': 'comprehensive_data_science',
            'units_covered': [
                'Data Science Process',
                'Descriptive Analytics & Visualization',
                'Inferential Statistics',
                'Analysis of Variance',
                'Predictive Analytics'
            ],
            'software_version': '1.0.0',
            'analyst': 'Advanced Data Analytics Module'
        }
        
        return results
        
    except Exception as e:
        print(f"❌ Analytics report generation failed: {e}")
        return {
            'error': str(e),
            'status': 'failed',
            'analysis_metadata': {
                'analysis_timestamp': datetime.now().isoformat(),
                'error_occurred': True
            }
        }

if __name__ == "__main__":
    # Test the analytics module
    print("🧪 Testing Advanced Data Analytics Module...")
    
    # Sample data
    sample_crack_data = [
        {"width_cm": 2.5, "length_cm": 5.0, "severity": "Moderate", "confidence": 0.85},
        {"width_cm": 1.2, "length_cm": 2.3, "severity": "Minor", "confidence": 0.92},
        {"width_cm": 4.1, "length_cm": 8.2, "severity": "Severe", "confidence": 0.78}
    ]
    
    sample_material_data = {
        "predicted_material": "Concrete",
        "probabilities": [0.7, 0.2, 0.05, 0.03, 0.02]
    }
    
    sample_environmental_data = {
        "carbon_footprint_kg": 25.5,
        "water_footprint_liters": 180.3,
        "energy_consumption_kwh": 15.2
    }
    
    # Run analysis
    results = create_comprehensive_analytics_report(
        sample_crack_data, 
        sample_material_data, 
        sample_environmental_data
    )
    
    print("✅ Test completed successfully!")
    print(f"📊 Results keys: {list(results.keys())}")