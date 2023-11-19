# Recipe Suggestor AI Project

## Overview

This project implements a recipe suggestion AI using four different search algorithms: Depth-First Search (DFS), Breadth-First Search (BFS), Greedy Best-First Search, and Particle Swarm Optimization. The goal is to recommend five recipes based on user preferences and dietary requirements.

## Project Structure

- **`GUI.py`**: The main file that integrates all four search algorithms and displays the suggested recipes along with their healthiness scores.
- **`a9trial_1.py`**: Depth-First Search algorithm implementation.
- **`b10trial_2.py`**: Breadth-First Search algorithm implementation.
- **`d12trial_4.py`**: Greedy Best-First Search algorithm implementation.
- **`c11trial_3.py`**: Particle Swarm Optimization algorithm implementation.
- **`epi_r.csv`**: csv file containing the dataset obtained from Kaggle, including information on sodium, fat, calories, and protein for each recipe.

## Dataset

The dataset used in this project was sourced from Kaggle, providing comprehensive nutritional information for each recipe. The nutrients considered include sodium, fat, calories, and protein. These values are used to calculate the healthiness score for each recipe.

## Healthiness Score Calculation

The healthiness score for each recipe is determined by considering the nutritional values. A score between 0 and 1 is assigned based on factors such as low sodium, low fat, and appropriate calorie and protein content. The algorithm with the highest healthiness score is selected, and the top five recipes from that algorithm are presented to the user.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run `GUI.py` to launch the graphical user interface.
4. Input your preferences, and the system will suggest five recipes based on the selected algorithm.

# Graphical Data

## Depth-first Search

### Heatmap


![image](https://github.com/Tyu017/ai_proj/assets/97674697/91bee867-e978-4f0e-9298-6662a0e06fb4)


### Histogram


![image](https://github.com/Tyu017/ai_proj/assets/97674697/d61c234b-896e-4403-9368-8f2fda3017e4)


### Pairplot


![image](https://github.com/Tyu017/ai_proj/assets/97674697/3b108b64-2224-475e-a0c1-4ad21fb3e6d9)


## Breadth-first Search

### Heatmap

![image](https://github.com/Tyu017/ai_proj/assets/97674697/9bc13ab3-cf5d-41cb-98d8-9930d44e96ef)

### Histogram

![image](https://github.com/Tyu017/ai_proj/assets/97674697/f216b01b-5082-4715-a3d1-87934a64c34d)

### Pairplot

![image](https://github.com/Tyu017/ai_proj/assets/97674697/904d1f75-b42b-4651-83aa-206eb668a653)

## Greedy-Best-first Search

### Heatmap

![image](https://github.com/Tyu017/ai_proj/assets/97674697/3155a952-76ef-42b6-9d03-35f167228af6)

### Histogram

![image](https://github.com/Tyu017/ai_proj/assets/97674697/20b950bb-746d-4875-a0cc-8fa57f4d7da9)

### Pairplot

![image](https://github.com/Tyu017/ai_proj/assets/97674697/0c14c3f5-6409-4b05-82e5-8b1025890355)

## Particle swarm optimization

### Heatmap

![image](https://github.com/Tyu017/ai_proj/assets/97674697/9e2a570d-930d-4552-bfd8-be0e309e698f)

### Histogram

![image](https://github.com/Tyu017/ai_proj/assets/97674697/a592ace8-9285-429b-ad47-25dc8eb08bb8)

### Pairplot

![image](https://github.com/Tyu017/ai_proj/assets/97674697/c361a0f1-7f30-4be9-afc9-c622c5352819)

## Dependencies

List of dependencies is available in the `requirements.txt` file. Install them using `pip install -r requirements.txt`.

## Contributing

Feel free to contribute to the project by implementing new search algorithms, improving the existing code, or enhancing the user interface.

## Acknowledgments

- Kaggle for providing the dataset used in this project.
- OpenAI for the inspiration and support.

## Contact

For any inquiries or suggestions, please contact dasbratnitish2003@gmail.com.

Happy cooking and enjoy our suggested recipes!
