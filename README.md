Student Performance Analysis Using Data Visualization

This project focuses on analyzing a dataset of student performance to uncover insights about the relationships between demographic factors and academic scores. The analysis is conducted using Python, leveraging popular libraries like pandas, matplotlib, and seaborn for data manipulation and visualization.
          The goal of the project is to identify patterns in student performance based on gender, parental education, and ethnic group distribution, providing a foundation for deeper data-driven exploration.

#Technologies Used

Programming Language: Python

Libraries :>
pandas: For data manipulation and aggregation.

matplotlib: For creating detailed and customizable plots.

seaborn: For advanced data visualization with enhanced aesthetics.

What’s in the Project?
1. Gender Distribution
A simple yet important question: How are students distributed by gender?
Visualized using a countplot to show the proportion of male and female students.
Insight: The dataset has more female students compared to males.
![imge_alt](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/b704476c4df768c8725d30d02a6a7765d4891b0c/Screenshot%202025-01-08%20211734.png)

2. Does Parental Education Influence Scores?

Parents’ education levels might have a role in shaping academic success—so I decided to investigate.
Using a heatmap, I visualized the average math and reading scores for students based on their parents' education levels.
Key takeaway: Higher parental education levels tend to correlate with better student performance.
![image_alt](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/9e440c81fc04338c527cfbc831f7681f4c5cabf6/Screenshot%202025-01-08%20211754.png)

3. Ethnic Group Distribution

Understanding the diversity in the dataset, I broke down the ethnic groups into a pie chart and a bar plot.
Insight: The dataset reflects a diverse student population, giving us a great perspective for analysis.
![alt_image](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/dddb87ba9609ea0306b71c1047fdcd46e5d898dd/Screenshot%202025-01-08%20211804.png)

Using Bar chart
![alt_image](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/27ee85889e72156eed06daec676972a3966c5a02/Screenshot%202025-01-08%20211815.png)


4. Boxplot of Math Scores by Gender

This boxplot visualizes the distribution of math scores between male and female students. It highlights key statistics like median, interquartile range (IQR), and outliers, providing a quick comparison of performance across genders. Labels for the x-axis (Gender) and y-axis (Math Scores),(Readingscore) ensure clarity, while the title describes the plot's purpose. A great way to explore trends and variability in scores!
![alt_image](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/e8f2f69c10f2281c10c11ccd99a0fe3e42960ece/Screenshot%202025-01-08%20211825.png)

![alt_image](https://github.com/ujjwalkhutale/Data-Analysis-Project/blob/1fbc8f5ff70bc33f1b95bbee79e101abca0b8b76/Screenshot%202025-01-08%20211844.png)

How You Can Run It
What You’ll Need
Python 3.8 or above.
Libraries: pandas, matplotlib, and seaborn (you can install them using pip).
Steps to Get Started
Clone this repository to your local machine:
bash

git clone https://github.com/yourusername/Student_Performance_Analysis.git
Open the project folder:
bash

cd Student_Performance_Analysis
Install the required libraries:
bash

pip install -r requirements.txt
Run the script:
bash

python analysis.py


I see this project as a starting point. Here are a few ideas I’m excited to explore:

Build predictive models to forecast student performance based on demographic factors.
Add interactive visualizations using tools like Plotly or Dash.
Include more datasets to compare trends across different schools or regions.
