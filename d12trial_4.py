import numpy as np
import pandas as pd
import random

data = pd.read_csv('epi_r.csv', engine='python')
data = data[['title', 'rating', 'calories', 'protein', 'fat', 'sodium']]
data.dropna(inplace=True)

data['protein'] = pd.to_numeric(data['protein'], errors='coerce')
data['calories'] = pd.to_numeric(data['calories'], errors='coerce')
data['sodium'] = pd.to_numeric(data['sodium'], errors='coerce')


def calculate_fitness(position, has_diabetes):
    recipe = data.iloc[position]
    # Minimize the calorie content directly
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
    # healthiness_score = max(0, min(1, healthiness_score))
    return healthiness_score

def pso_recommend_with_diabetes(data, max_iterations, swarm_size, has_diabetes):
    num_dimensions = 1
    inertia_weight = 0.5
    cognitive_weight = 1.5
    social_weight = 1.5
    lower_bound = 0
    upper_bound = len(data) - 1

    # Initialize particles
    particles = np.random.randint(lower_bound, upper_bound, size=(swarm_size, num_dimensions))

    # Initialize velocities
    velocities = np.zeros((swarm_size, num_dimensions))

    # Initialize personal best positions and values
    personal_best_positions = particles.copy()
    personal_best_values = np.array([calculate_fitness(i, has_diabetes) for i in particles.flatten()])

    # Initialize global best position and value
    global_best_index = np.argmax(personal_best_values)
    global_best_position = personal_best_positions[global_best_index]
    global_best_value = personal_best_values[global_best_index]

    for iteration in range(max_iterations):
        # Update velocities and positions
        r1 = np.random.random(size=(swarm_size, num_dimensions))
        r2 = np.random.random(size=(swarm_size, num_dimensions))

        velocities = (inertia_weight * velocities +
                      cognitive_weight * r1 * (personal_best_positions - particles) +
                      social_weight * r2 * (global_best_position - particles))

        particles = particles + velocities

        # Clip positions to be within bounds
        particles = np.clip(particles, lower_bound, upper_bound).astype(int)

        # Update personal best positions and values
        current_values = np.array([calculate_fitness(i, has_diabetes) for i in particles.flatten()])
        update_mask = current_values < personal_best_values
        personal_best_positions[update_mask] = particles[update_mask]
        personal_best_values[update_mask] = current_values[update_mask]

        # Update global best position and value
        global_best_index = np.argmax(personal_best_values)
        global_best_position = personal_best_positions[global_best_index]
        global_best_value = personal_best_values[global_best_index]

    recommended_recipe = data.iloc[global_best_position[0]]
    return recommended_recipe, global_best_value


def run_recommendations(num_iterations,has_diabetes):
    results = []
    total_healthiness=0
    
    visited_recipes = set()
    for i in range(num_iterations):
        print(f"\nIteration {i + 1}/{num_iterations}")
        
        # Set parameters
        max_iterations = 3000
        swarm_size = 10

        # User input for diabetes status
        # diabetes_status = input("Do you have diabetes? (yes/no): ").lower()
        # has_diabetes = 0 == i%2

        # Run DFS recommendation
        # visited_recipes.add(initial_recipe)
        # initial_recipe_row = data[data['title'] == initial_recipe].iloc[0]
        recommended_recipe, healthiness = pso_recommend_with_diabetes(data, max_iterations, swarm_size, has_diabetes)
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
# excel_file_path = 'recommendation_results_4.xlsx'
# results_df.to_excel(excel_file_path, index=False)
# print(f"\nResults saved to {excel_file_path}")