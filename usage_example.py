"""
LSApp User Segmentation - Complete Example Usage
This script demonstrates how to use the clustering functions from Part 2.
"""

import pandas as pd
import numpy as np
from lsapp_part2_clustering import (
    visualize_feature_distributions,
    plot_correlation_matrix,
    prepare_clustering_data,
    perform_pca_analysis,
    find_optimal_k,
    apply_kmeans,
    apply_hierarchical,
    apply_gmm,
    profile_clusters,
    visualize_clusters_pca
)

def main():
    """
    Main function to run the complete clustering analysis.
    Make sure you've run Part 1 notebook first to create user_features.
    """
    
    print("="*80)
    print("LSApp User Segmentation - Complete Analysis")
    print("="*80)
    
    # Step 1: Load user_features from Part 1
    # (Assuming it's been saved or you're running in the same session)
    print("\nStep 1: Loading user features...")
    # user_features = pd.read_csv('user_features.csv')  # If saved
    # For demonstration, assuming it exists in memory
    
    # Step 2: Visualize features
    print("\nStep 2: Visualizing feature distributions...")
    # visualize_feature_distributions(user_features)
    # plot_correlation_matrix(user_features)
    
    # Step 3: Prepare data for clustering
    print("\nStep 3: Preparing and scaling data...")
    # X_scaled, clustering_features = prepare_clustering_data(user_features)
    # print(f"  - Features selected: {len(clustering_features)}")
    # print(f"  - Data shape: {X_scaled.shape}")
    
    # Step 4: PCA Analysis
    print("\nStep 4: Performing PCA analysis...")
    # pca, X_pca = perform_pca_analysis(X_scaled)
    # explained_variance = pca.explained_variance_ratio_
    
    # Step 5: Find optimal k
    print("\nStep 5: Finding optimal number of clusters...")
    # optimal_k, silhouette_scores = find_optimal_k(X_scaled)
    # print(f"  - Optimal k: {optimal_k}")
    
    # Step 6: Apply clustering algorithms
    print("\nStep 6: Applying clustering algorithms...")
    
    # K-Means
    # print("\n  6.1: K-Means clustering...")
    # kmeans, kmeans_metrics = apply_kmeans(X_scaled, optimal_k, user_features)
    # print(f"      Silhouette: {kmeans_metrics['silhouette']:.3f}")
    # print(f"      Davies-Bouldin: {kmeans_metrics['db']:.3f}")
    
    # Hierarchical
    # print("\n  6.2: Hierarchical clustering...")
    # hierarchical, hier_metrics = apply_hierarchical(X_scaled, optimal_k, user_features)
    # print(f"      Silhouette: {hier_metrics['silhouette']:.3f}")
    
    # GMM
    # print("\n  6.3: Gaussian Mixture Model...")
    # gmm, gmm_metrics = apply_gmm(X_scaled, optimal_k, user_features)
    # print(f"      Silhouette: {gmm_metrics['silhouette']:.3f}")
    # print(f"      BIC: {gmm_metrics['bic']:.2f}")
    
    # Step 7: Profile clusters
    print("\nStep 7: Profiling clusters...")
    # cluster_profiles = profile_clusters(user_features, 'kmeans_cluster')
    
    # Step 8: Visualize clusters
    print("\nStep 8: Visualizing clusters...")
    # visualize_clusters_pca(X_pca, user_features, explained_variance, 'kmeans_cluster')
    
    # Step 9: Save results
    print("\nStep 9: Saving results...")
    # user_features.to_csv('user_features_clustered.csv', index=False)
    # cluster_profiles.to_csv('cluster_profiles.csv')
    # print("  - Results saved to CSV files")
    
    print("\n" + "="*80)
    print("Analysis complete!")
    print("="*80)
    print("\nNext steps:")
    print("  1. Review cluster profiles")
    print("  2. Validate with domain knowledge")
    print("  3. Use insights for user targeting")
    print("  4. Iterate with different parameters if needed")


def quick_analysis_example():
    """
    Quick example showing the typical workflow.
    """
    print("\nQuick Analysis Example")
    print("-" * 40)
    
    # Example workflow
    workflow = """
    # 1. Load and prepare data
    user_features = pd.read_csv('user_features.csv')
    X_scaled, features = prepare_clustering_data(user_features)
    
    # 2. Run PCA
    pca, X_pca = perform_pca_analysis(X_scaled)
    
    # 3. Find optimal k
    optimal_k, _ = find_optimal_k(X_scaled)
    
    # 4. Apply K-Means
    kmeans, metrics = apply_kmeans(X_scaled, optimal_k, user_features)
    
    # 5. Profile clusters
    profiles = profile_clusters(user_features, 'kmeans_cluster')
    
    # 6. Visualize
    visualize_clusters_pca(X_pca, user_features, 
                          pca.explained_variance_ratio_, 
                          'kmeans_cluster')
    
    # 7. Save results
    user_features.to_csv('clustered_users.csv', index=False)
    """
    
    print(workflow)


def compare_algorithms_example():
    """
    Example showing how to compare different clustering algorithms.
    """
    print("\nAlgorithm Comparison Example")
    print("-" * 40)
    
    example = """
    # Apply all algorithms
    kmeans, km_metrics = apply_kmeans(X_scaled, k, user_features)
    hier, hier_metrics = apply_hierarchical(X_scaled, k, user_features)
    gmm, gmm_metrics = apply_gmm(X_scaled, k, user_features)
    
    # Compare metrics
    comparison = pd.DataFrame({
        'Algorithm': ['K-Means', 'Hierarchical', 'GMM'],
        'Silhouette': [km_metrics['silhouette'], 
                      hier_metrics['silhouette'],
                      gmm_metrics['silhouette']],
        'Davies-Bouldin': [km_metrics['db'],
                          hier_metrics['db'],
                          gmm_metrics['db']]
    })
    
    print(comparison)
    
    # Best algorithm by silhouette score
    best = comparison.loc[comparison['Silhouette'].idxmax(), 'Algorithm']
    print(f"Best algorithm: {best}")
    """
    
    print(example)


if __name__ == "__main__":
    print(__doc__)
    print("\nThis script provides examples of using the clustering functions.")
    print("To actually run the analysis, uncomment the code in main().")
    print("\nAvailable examples:")
    print("  - main(): Complete analysis workflow")
    print("  - quick_analysis_example(): Quick reference")
    print("  - compare_algorithms_example(): Algorithm comparison")
    
    # Run examples
    quick_analysis_example()
    compare_algorithms_example()
    
    print("\n" + "="*80)
    print("To run the actual analysis:")
    print("  1. Make sure you've completed Part 1 notebook")
    print("  2. Uncomment the code in main() function")
    print("  3. Run: python usage_example.py")
    print("="*80)
