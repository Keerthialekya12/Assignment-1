from matplotlib import pyplot as plt
slices = [22.2,17.6,8.8,8,7.7,6.7]
labels = ['Java','Python','PHP','JavaScript','C#','C++']
colors = ['#0000FF','#FFA500','#00FF00','#FF0000','#AF69EE','#964B00']
plt.pie(slices, labels=labels, colors=colors,autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.tight_layout()
plt.show()
