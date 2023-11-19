import numpy as np
import pandas as pd
import random
from collections import deque

data = pd.read_csv('epi_r.csv', engine='python')
data = data[['title', 'rating', 'calories', 'protein', 'fat', 'sodium']]
data.dropna(inplace=True)
data['protein'] = pd.to_numeric(data['protein'], errors='coerce')
data['calories'] = pd.to_numeric(data['calories'], errors='coerce')
data['sodium'] = pd.to_numeric(data['sodium'], errors='coerce')

def calculate_bmi(height, weight):
    # BMI formula: BMI = weight (kg) / (height (m))^2
    height_meters = height / 100  # Convert height from cm to meters
    bmi = weight / (height_meters ** 2)
    return bmi

def evaluate_healthiness_with_diabetes_bmi(recipe, has_diabetes):
    # Define weights for each parameter (you can adjust these based on importance)
    sodium_weight = 0.2
    protein_weight = 0.3
    fat_weight = 0.2
    calories_weight = 0.4
    diabetes_penalty = 0.1  # penalty for individuals with diabetes

    # Calculate healthiness score
    healthiness_score = (
        (1 - recipe['sodium'] / 1423) * sodium_weight +
        (recipe['protein'] / 279) * protein_weight +
        (1 - recipe['fat'] / 342) * fat_weight +
        (1 - recipe['calories'] / 1000) * calories_weight
    )

    # Apply a penalty for individuals with diabetes
    if has_diabetes:
        healthiness_score *= (1 - diabetes_penalty)

    # Ensure the healthiness score is within the [0, 1] range
    healthiness_score = max(0, min(1, healthiness_score))

    return healthiness_score


def bfs_recommend_with_diabetes_bmi_and_index(data, initial_recipe, max_depth, has_diabetes,visited):
    queue = deque([(initial_recipe, 0)])  # Queue of (recipe, depth)
    # visited = set()

    best_recipe = initial_recipe
    best_healthiness = evaluate_healthiness_with_diabetes_bmi(initial_recipe, has_diabetes)

    while queue:
        current_recipe, depth = queue.popleft()

        if depth == max_depth:
            break

        for _ in range(5):  # Consider 5 random possibilities
            random_recipe = data.sample(n=1).iloc[0]

            if random_recipe['title'] not in visited:
                visited.add(random_recipe['title'])
                queue.append((random_recipe, depth + 1))

                healthiness = evaluate_healthiness_with_diabetes_bmi(random_recipe, has_diabetes)

                if healthiness > best_healthiness:
                    best_recipe = random_recipe
                    best_healthiness = healthiness

    visited.add(best_recipe['title'])
    return best_recipe, best_healthiness, 0


def run_recommendations(num_iterations,has_diabetes):
    results = []
    total_healthiness=0

    
    visited_recipes = set()
    for i in range(num_iterations):
        print(f"\nIteration {i + 1}/{num_iterations}")
        
        # Set parameters
        initial_recipe = random.choice(data['title'].tolist())
        max_depth = 5

        # User input for diabetes status
        # diabetes_status = input("Do you have diabetes? (yes/no): ").lower()
        # has_diabetes = 0 == i%2

        # Run DFS recommendation
        visited_recipes.add(initial_recipe)
        initial_recipe_row = data[data['title'] == initial_recipe].iloc[0]
        recommended_recipe, healthiness, _ = bfs_recommend_with_diabetes_bmi_and_index(data, initial_recipe_row, max_depth, has_diabetes,visited_recipes)
        total_healthiness+=healthiness
        result = {
            # 'Iteration': i + 1,
            # 'Diabetes': has_diabetes,
            'Recommended Recipe': recommended_recipe['title'],
            'Healthiness Score': healthiness,
            # 'protein':recommended_recipe['protein'],
            # 'calories':recommended_recipe['calories'],
            # 'fat':recommended_recipe['fat'],
            # 'sodium':recommended_recipe['sodium'],
        }
        results.append(result)

    return results,total_healthiness

# Run recommendations 50 times
# num_iterations = 20
# results_df = run_recommendations(num_iterations)

# # Save results to an Excel file
# excel_file_path = 'recommendation_results_2.xlsx'
# results_df.to_excel(excel_file_path, index=False)
# print(f"\nResults saved to {excel_file_path}")