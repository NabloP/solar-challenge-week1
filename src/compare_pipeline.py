"""
compare_pipeline.py – B5W0: Solar Data Discovery
------------------------------------------------

An object-oriented pipeline to compare irradiance metrics (GHI, DNI, DHI)
across Benin, Togo, and Sierra Leone. Built to support fully modular,
reusable analysis for MoonLight Energy Solutions.

Usage:
    from compare_pipeline import SolarComparisonPipeline

    pipeline = SolarComparisonPipeline(data_path="data")
    pipeline.run_all()

Author: Nabil Mohamed
"""

# ------------------------------------------------------------------------------
# 📦 Imports
# ------------------------------------------------------------------------------
import os # import os for file path handling
import pandas as pd # import pandas for data manipulation
import seaborn as sns # import seaborn for data visualization
import matplotlib.pyplot as plt # import matplotlib for plotting
from scipy.stats import shapiro, kruskal # import statistical tests from scipy

# ------------------------------------------------------------------------------
# 🧱 SolarComparisonPipeline Class
# ------------------------------------------------------------------------------
class SolarComparisonPipeline: # define a class for the solar comparison pipeline
    def __init__(self, data_path="data"): # constructor to initialize the pipeline
        """
        Initialize the pipeline with path and internal data containers.
        """
        self.data_path = data_path # set the data path
        self.benin = None # initialize Benin data
        self.togo = None # initialize Togo data
        self.sl = None # initialize Sierra Leone data
        self.df_all = None # initialize combined data
        print(f"✅ Initialized pipeline with data path: {data_path}") # print initialization message

    # --------------------------------------------------------------------------
    # 📂 Load and label datasets
    # --------------------------------------------------------------------------
    def load_data(self): # Load and label datasets
        """
        Load cleaned CSVs and label country columns.
        """
        try: # Attempt to load the datasets
            self.benin = pd.read_csv(os.path.join(self.data_path, "benin_clean.csv")) # read Benin data
            self.togo = pd.read_csv(os.path.join(self.data_path, "togo_clean.csv")) # read Togo data
            self.sl = pd.read_csv(os.path.join(self.data_path, "sierra_leone_clean.csv")) # read Sierra Leone data

            self.benin["country"] = "Benin" # label Benin data
            self.togo["country"] = "Togo" # label Togo data
            self.sl["country"] = "Sierra Leone" # label Sierra Leone data

            self.df_all = pd.concat([self.benin, self.togo, self.sl], ignore_index=True) # combine datasets

            print(f"📊 Loaded data: {self.df_all.shape} rows") # print data shape

        except FileNotFoundError as e: # Handle file not found error
            raise RuntimeError("Missing cleaned CSVs. Ensure Task 2 was completed.") from e # raise error if files are not found

    # --------------------------------------------------------------------------
    # 🧪 Shapiro–Wilk test
    # --------------------------------------------------------------------------
    def test_normality(self, sample_size=5000): # Test normality using Shapiro–Wilk test
        """
        Test GHI normality using Shapiro–Wilk per country.
        """
        print("📈 Shapiro–Wilk Normality Test (GHI):")
        results = {} # initialize results dictionary
        for df, name in zip([self.benin, self.togo, self.sl], ["Benin", "Togo", "Sierra Leone"]): # iterate over datasets
            sample = df["GHI"].dropna().sample(n=min(sample_size, len(df)), random_state=42) # sample GHI data
            stat, p = shapiro(sample) # perform Shapiro–Wilk test
            result = "✅ Likely Normal" if p > 0.05 else "⚠️ Non-Normal" # determine result
            print(f"{name:<15} → p = {p:.5f} → {result}") # print result
            results[name] = p # store p-value in results
        return results # return results

    # --------------------------------------------------------------------------
    # 🧪 Kruskal–Wallis test
    # --------------------------------------------------------------------------
    def run_kruskal(self): # Run Kruskal–Wallis test
        """
        Run Kruskal–Wallis H-test on GHI across countries.
        """
        ghi_sets = [self.benin["GHI"].dropna(), self.togo["GHI"].dropna(), self.sl["GHI"].dropna()] # prepare GHI data for Kruskal–Wallis test
        h, p = kruskal(*ghi_sets) # perform Kruskal–Wallis test
        print(f"\n📌 Kruskal–Wallis Test (GHI):\n   H = {h:.3f}  |  p = {p:.5f}")
        if p < 0.05: # check if p-value is significant
            print("✅ Significant difference in GHI across countries.")
        else: # if not significant
            print("⚠️ No statistically significant difference detected.")
        return h, p # return H-statistic and p-value

    # --------------------------------------------------------------------------
    # 📊 Boxplots: GHI, DNI, DHI
    # --------------------------------------------------------------------------
    def plot_boxplots(self, metrics=["GHI", "DNI", "DHI"]): # Create boxplots for GHI, DNI, DHI
        """
        Create annotated boxplots per metric grouped by country.
        """
        for metric in metrics: # iterate over metrics
            plt.figure(figsize=(9, 6)) # set figure size
            sns.boxplot(data=self.df_all, x="country", y=metric, hue="country", palette="Set2", legend=False) # create boxplot
            plt.title(f"{metric} Distribution by Country", fontsize=16, weight='bold') # set title
            plt.ylabel(f"{metric} (W/m²)", fontsize=12) # set y-axis label
            plt.xlabel("") # set x-axis label
            plt.grid(True, linestyle="--", alpha=0.7) # add grid
            plt.xticks(fontsize=11) # set x-ticks font size
            plt.yticks(fontsize=11) # set y-ticks font size
            plt.tight_layout() # adjust layout
            plt.show() # show plot

    # --------------------------------------------------------------------------
    # 📊 Bar chart of average GHI
    # --------------------------------------------------------------------------
    def plot_avg_ghi_bar(self): # Create bar chart of average GHI
        """
        Create a bar chart showing average GHI by country.
        """
        mean_ghi = ( # calculate mean GHI by country
            self.df_all.groupby("country")["GHI"] # group by country
            .mean() # calculate mean
            .sort_values(ascending=False) # sort values
            .round(1) # round to 1 decimal place
        )

        fig, ax = plt.subplots(figsize=(7, 4)) # set figure size
        bars = ax.bar(mean_ghi.index, mean_ghi.values, color=sns.color_palette("Set2")) # create bar chart
        ax.set_title("☀️ Average GHI by Country", fontsize=14, weight='bold') # set title
        ax.set_ylabel("GHI (W/m²)", fontsize=12) # set y-axis label
        ax.set_xlabel("") # set x-axis label
        ax.grid(axis='y', linestyle="--", alpha=0.7) # add grid

        for bar in bars: # iterate over bars
            height = bar.get_height() # get height of each bar
            ax.annotate( # annotate each bar with its height
                f"{height:.1f}", # format height to 1 decimal place
                xy=(bar.get_x() + bar.get_width() / 2, height), # set annotation position
                xytext=(0, 5), # set text offset
                textcoords="offset points", # set text coordinates
                ha="center", # horizontal alignment
                fontsize=10, # set font size
                weight='bold' # set font weight
            )
        plt.tight_layout() # adjust layout
        plt.show() # show plot

    # --------------------------------------------------------------------------
    # 📈 Summary statistics
    # --------------------------------------------------------------------------
    def summarize(self): #  Summarize statistics
        """
        Return mean, median, std, and count for each country and metric.
        """
        summary = (  # calculate summary statistics
            self.df_all # use combined data
            .groupby("country")[["GHI", "DNI", "DHI"]] # group by country
            .agg(["mean", "median", "std", "count"]) # aggregate statistics
            .round(2) # round to 2 decimal places
        )
        print("📊 Summary Statistics (GHI, DNI, DHI):")
        return summary # return summary statistics

    # --------------------------------------------------------------------------
    # 🚨 Missing value report
    # --------------------------------------------------------------------------
    def report_missing(self): # Report missing values
        """
        Report missing values per country.
        """
        missing = ( # calculate missing values
            self.df_all[["country", "GHI", "DNI", "DHI"]] # select relevant columns
            .isna() # check for NaN values
            .groupby(self.df_all["country"]) # group by country
            .sum() # sum missing values
            .astype(int) # convert to integer
        )
        print("⚠️ Missing Value Report:")
        return missing # return missing values

    # --------------------------------------------------------------------------
    # 🚀 Run all steps in sequence
    # --------------------------------------------------------------------------
    def run_all(self): # Run all steps in sequence
        """
        Convenience method to run the entire pipeline sequentially.
        """
        self.load_data() # load data
        self.test_normality() # test normality
        self.run_kruskal() # run Kruskal–Wallis test
        self.plot_boxplots() # plot boxplots
        self.plot_avg_ghi_bar() # plot average GHI bar chart
        summary = self.summarize() # summarize statistics
        print(summary) # display summary statistics
        missing = self.report_missing() # report missing values
        print(missing) # display missing values
