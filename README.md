# LSApp User Segmentation Analysis

A comprehensive machine learning project for segmenting mobile app users based on usage patterns using the LSApp dataset.

##  Project Overview

This project analyzes the LSApp (Large dataset of Sequential mobile App usage) dataset to segment 292 users based on their mobile app usage patterns. The dataset contains 599,635 app usage records collected through the uSearch Android app.

### Key Objectives

Segment users across multiple dimensions:
1. **Usage Variety**: Number of unique apps used
2. **Usage Frequency**: Number of unique sessions
3. **Session Duration**: Average time spent per session
4. **Temporal Patterns**: Time of day when usage occurs
5. **App Preferences**: Most frequently used app categories
6. **Custom Clustering**: Additional behavioral patterns

##  Dataset Information

- **Source**: [LSApp GitHub Repository](https://github.com/aliannejadi/lsapp)
- **Records**: 599,635 app usage events
- **Users**: 292 participants
- **Collection Period**: Average 15 days per user
- **Collection Method**: uSearch Android app

### Data Structure

| Column | Description |
|--------|-------------|
| `user_id` | Unique user identifier |
| `session_id` | Unique session identifier |
| `timestamp` | Date and time of event |
| `app_name` | Name of the app |
| `event_type` | Type of event (Opened, Closed, User Interaction, Broken) |

##  Getting Started

### Prerequisites

```bash
Python 3.8+
pip install -r requirements.txt
```

### Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd lsapp-user-segmentation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the LSApp dataset:
   - Download `lsapp_tsv.gz` from the [LSApp repository](https://github.com/aliannejadi/lsapp)
   - Place it in the project root directory
   - Extract: `tar -xzf lsapp_tsv.gz`

### Running the Analysis

#### Option 1: Jupyter Notebook (Recommended)

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `lsapp_user_segmentation_part1.ipynb`
3. Run all cells sequentially
4. The notebook is self-contained with detailed explanations

#### Option 2: Python Scripts

For Part 2 clustering analysis:
```bash
python lsapp_part2_clustering.py
```

##  Project Structure

```
lsapp-user-segmentation/
├── README.md                              # This file
├── requirements.txt                        # Python dependencies
├── lsapp.tsv                              # Dataset (after extraction)
├── lsapp_user_segmentation_part1.ipynb    # Main analysis notebook
├── lsapp_part2_clustering.py              # Clustering functions
├── environment.yml                         # Conda environment (optional)
└── results/                               # Generated outputs (created during run)
    ├── figures/                           # Visualizations
    ├── cluster_profiles/                  # Cluster analysis results
    └── models/                            # Saved models
```

##  Methodology

### 1. Data Preprocessing
- Timestamp conversion and temporal feature extraction
- App categorization (Social Media, Games, Entertainment, etc.)
- Session duration calculation
- Missing value handling

### 2. Feature Engineering

**User-Level Features (29 total)**:
- `num_unique_apps`: Number of distinct apps used
- `num_sessions`: Total number of sessions
- `avg_session_duration_min`: Average session length
- `total_events`: Total app usage events
- `avg_events_per_session`: Event density
- `avg_apps_per_session`: App switching behavior
- `usage_std`: Usage consistency across days
- `active_days`: Number of days with activity
- `most_active_hour`: Peak usage hour
- Time period percentages (Morning, Afternoon, Evening, Night)
- App category percentages (10 categories)

### 3. Data Scaling

Three scaling methods compared:
- **StandardScaler** (Z-score normalization) ✓ Selected
- MinMaxScaler (0-1 normalization)
- RobustScaler (Median and IQR)

### 4. Dimensionality Reduction

**Principal Component Analysis (PCA)**:
- Reduces feature space while preserving variance
- Visualizes high-dimensional data
- Identifies most important features
- First 10 components explain ~90% of variance

### 5. Clustering Algorithms

Four algorithms compared:

| Algorithm | Type | Strengths |
|-----------|------|-----------|
| **K-Means** | Centroid-based | Fast, scalable, interpretable |
| **Hierarchical** | Hierarchical | Shows cluster relationships |
| **DBSCAN** | Density-based | Handles noise, arbitrary shapes |
| **GMM** | Probabilistic | Soft clustering, confidence scores |

### 6. Evaluation Metrics

- **Silhouette Score**: Cluster cohesion and separation (-1 to 1, higher better)
- **Davies-Bouldin Index**: Average similarity ratio (0 to ∞, lower better)
- **Calinski-Harabasz Index**: Variance ratio (0 to ∞, higher better)

### 7. Optimal K Selection

Multiple methods used:
- Elbow Method (inertia)
- Silhouette analysis
- Davies-Bouldin minimization
- Calinski-Harabasz maximization

## 📈 Key Findings

### Cluster Characteristics

Results will vary based on the optimal k chosen, but typical patterns include:

**Example with k=4:**

1. **Heavy Users** (~20%)
   - High app variety (15-20 unique apps)
   - Frequent sessions (100+ sessions)
   - Long session durations (8-10 min avg)
   - Active across all time periods
   - Balanced app usage

2. **Casual Users** (~35%)
   - Moderate app variety (8-12 unique apps)
   - Regular sessions (40-60 sessions)
   - Short sessions (3-5 min avg)
   - Evening/night focus
   - Entertainment & social media preference

3. **Power Users** (~25%)
   - Very high app variety (20-30 unique apps)
   - Very frequent sessions (150+ sessions)
   - Variable session lengths
   - Morning & daytime active
   - Productivity & communication focus

4. **Light Users** (~20%)
   - Low app variety (5-8 unique apps)
   - Infrequent sessions (20-30 sessions)
   - Very short sessions (1-3 min avg)
   - Sporadic usage
   - Games & utilities preference

##  Visualizations

The analysis generates 15+ comprehensive visualizations:

1. Event type distribution
2. Top 20 most used apps
3. App category distribution
4. Feature distributions (9 histograms)
5. Categorical feature distributions
6. Correlation matrix
7. Scaling method comparisons
8. PCA explained variance (scree plot)
9. PCA cumulative variance
10. Feature importance in principal components
11. 2D PCA scatter plot
12. Elbow method plot
13. Silhouette score plot
14. Davies-Bouldin index plot
15. Calinski-Harabasz index plot
16. Cluster visualizations (2D & 3D PCA)
17. Radar charts for cluster profiles
18. Heatmaps for time/category distributions
19. Dendrogram (hierarchical clustering)
20. Algorithm comparison charts

## 🛠️ Technologies Used

- **Python 3.8+**
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn
- **Statistical Analysis**: scipy
- **Notebook**: Jupyter

##  References

### Research Paper
```bibtex
@article{AliannejadiTOIS21,
    author = {Aliannejadi, Mohammad and Zamani, Hamed and Crestani, Fabio and Croft, W. Bruce},
    title = {Context-Aware Target Apps Selection and Recommendation for Enhancing Personal Mobile Assistants},
    journal = {ACM Transactions on Information Systems (TOIS)},
    year = {2021}
}
```

### Related Publications
1. Aliannejadi et al. (2018). "Target Apps Selection: Towards a Unified Search Framework for Mobile Devices." SIGIR.
2. Aliannejadi et al. (2018). "In Situ and Context-Aware Target Apps Selection for Unified Mobile Search." CIKM.

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  License

This project is open source and available under the MIT License.

##  Authors

- Your Name - *Initial work*

##  Acknowledgments

- LSApp dataset creators: Jacopo Fidacaro, Luca Costa, Mohammad Aliannejadi, Hamed Zamani, Fabio Crestani, W. Bruce Croft
- Università della Svizzera italiana (USI), Lugano, Switzerland
- University of Massachusetts Amherst, Amherst, MA, USA

##  Contact

For questions or feedback, please open an issue on GitHub or contact [your-email@example.com]

## 🔮 Future Work

Potential extensions:
- Deep learning approaches (autoencoders, neural networks)
- Temporal pattern analysis with time series methods
- Predictive modeling for app usage
- Real-time clustering for streaming data
- Integration with app recommendation systems
- Cross-device usage analysis
- Privacy-preserving clustering methods

---
