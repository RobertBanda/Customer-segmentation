# Quick Start Guide: LSApp User Segmentation

## 🚀 Setup (5 minutes)

### Step 1: Clone and Setup Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd lsapp-user-segmentation

# Option A: Using pip
pip install -r requirements.txt

# Option B: Using conda (recommended for data science)
conda env create -f environment.yml
conda activate lsapp-segmentation
```

### Step 2: Get the Data

1. Download the LSApp dataset:
   - Visit: https://github.com/aliannejadi/lsapp
   - Download `lsapp_tsv.gz`
   - Place in project directory

2. Extract the data:
```bash
tar -xzf lsapp_tsv.gz
# This creates lsapp.tsv
```

### Step 3: Run the Analysis


```bash
# Start Jupyter
jupyter notebook

# Open and run:
# lsapp_user_segmentation_part1.ipynb
```

## 📊 What You'll Get

After running the notebook, you'll have:

1. **Exploratory Data Analysis**
   - Dataset overview and statistics
   - Missing value analysis
   - Event type distribution
   - Top apps and categories

2. **Feature Engineering**
   - 29 user-level features created
   - Temporal patterns extracted
   - App categories identified

3. **Clustering Results**
   - Optimal number of clusters determined
   - Multiple algorithms compared
   - User segments identified

4. **Visualizations**
   - 15+ charts and plots
   - PCA visualizations
   - Cluster profiles

5. **Insights**
   - User segment characteristics
   - Behavioral patterns
   - Recommendations for targeting

## 🔍 Understanding the Output

### Cluster Profiles
Each cluster represents a distinct user segment:
- **Size**: How many users
- **Apps**: Average unique apps used
- **Sessions**: Frequency of use
- **Duration**: Time spent per session
- **Time**: When they're most active
- **Categories**: What types of apps they prefer

### Key Metrics
- **Silhouette Score**: How well-separated clusters are (higher = better)
- **Davies-Bouldin**: Cluster quality (lower = better)
- **Calinski-Harabasz**: Variance ratio (higher = better)

## 💡 Pro Tips

1. **Start with Part 1**: Complete the entire Part 1 notebook first
2. **Check Memory**: The dataset is ~170MB, ensure you have enough RAM
3. **Be Patient**: Some clustering algorithms take a few minutes
4. **Experiment**: Try different numbers of clusters (k values)
5. **Customize**: Modify app categories based on your needs

## 🐛 Troubleshooting

### Issue: "File not found: lsapp.tsv"
**Solution**: Make sure you've extracted the .gz file in the project directory

### Issue: "Memory Error"
**Solution**: Close other applications or reduce the sample size

### Issue: "Module not found"
**Solution**: Make sure all requirements are installed:
```bash
pip install -r requirements.txt
```

### Issue: Jupyter kernel crashes
**Solution**: Restart the kernel and run cells one by one

## 📖 Next Steps

1. **Analyze Results**: Review cluster profiles and characteristics
2. **Validate**: Check if clusters make business sense
3. **Iterate**: Try different features or clustering parameters
4. **Apply**: Use insights for app recommendations or user targeting
5. **Extend**: Add your own features or algorithms

## 🎯 Key Sections in the Notebook

1. **Setup (Cells 1-2)**: Import libraries and load data
2. **EDA (Cells 3-7)**: Explore and understand the data
3. **Features (Cells 8-12)**: Create user-level features
4. **Part 2**: Clustering and profiling (separate script)

## 📚 Additional Resources

- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [PCA Explained](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [LSApp Paper](https://doi.org/10.1145/3394486.3403268)

## 🤔 FAQ

**Q: How long does the analysis take?**
A: 10-15 minutes for Part 1, 5-10 minutes for clustering

**Q: Can I use my own data?**
A: Yes! Just match the column format (user_id, session_id, timestamp, app_name, event_type)

**Q: What's the optimal number of clusters?**
A: It depends on your goals, but typically 3-6 clusters work well

**Q: Can I save the results?**
A: Yes, the notebook includes code to export cluster assignments and profiles

## 💬 Getting Help

- Check the README.md for detailed documentation
- Review code comments in the notebook
- Open an issue on GitHub for bugs
- Check the references section for related papers

---

Happy clustering! 🎉
