# Используя прилагаемый файл с числовой последовательностью sequence.txt, вывести диаграмму процентного соотношения согласно варианту сумма чисел по модулю, стоящих на четных и нечетных позициях
import matplotlib.pyplot as plt

# Read the sequence from the file
with open('sequence.txt', 'r') as file:
    sequence = [float(line.strip()) for line in file]

# Calculate the sum of absolute values at even and odd positions
even_sum = sum(abs(sequence[i]) for i in range(0, len(sequence), 2))
odd_sum = sum(abs(sequence[i]) for i in range(1, len(sequence), 2))

# Calculate the percentages
total_sum = even_sum + odd_sum
even_percentage = (even_sum / total_sum) * 100
odd_percentage = (odd_sum / total_sum) * 100

# Plot the pie chart
labels = 'Even Positions', 'Odd Positions'
sizes = [even_percentage, odd_percentage]
colors = ['lightblue', 'lightgreen']
explode = (0.1, 0)  # explode the 1st slice (Even Positions)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Percentage of Sum of Absolute Values at Even and Odd Positions')
plt.show()