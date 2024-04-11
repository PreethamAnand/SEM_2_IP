# from turtle import *
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)



# import numpy as np
# import matplotlib.pyplot as plt

# # Create numpy arrays for X and Y coordinates
# X,Y = np.array([0]),np.array([0])
# X1,Y1 = np.array([30]),np.array([5.50])
# X2,Y2 = np.array([60]),np.array([3.00])
# X3,Y3 = np.array([90]),np.array([1.65])
# X4,Y4 = np.array([120]),np.array([0.91])
# X5,Y5 = np.array([150]),np.array([0.51])
# X6,Y6 = np.array([180]),np.array([0.29])
# X7,Y7 = np.array([210]),np.array([0.17])
# X8,Y8 = np.array([240]),np.array([0.10])
# X8,Y8 = np.array([270]),np.array([0.07])


# # Plot the point using scatter method
# plt.scatter(X, Y)
# plt.scatter(X1, Y1)
# plt.scatter(X2, Y2)
# plt.scatter(X3, Y3)
# plt.scatter(X4, Y4)
# plt.scatter(X5, Y5)
# plt.scatter(X6, Y6)
# plt.scatter(X7, Y7)
# plt.scatter(X8, Y8)
# plt.show()


# #  module
# import fontstyle
# # format text
# text = fontstyle.apply(
#     '\n\t\t\t\t\t\t\t\tHey!,\n\t\t\t\t\t\t\t\tGood morning\n\t\t\t\t\t\t\t\tAkshaya', 'bold/Italic/black/RED_BG')
# # display importtext
# print(text)


# text = "Natural language processing using python"
# words = text.split()
# x = [len(word) for word in words]
# y = sum(x)
# z = y/len(x)
# print(x,y,z)

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def prime(n):
#     lis = []
#     for i in range(2, n):
#         if is_prime(i):
#             lis.append(i)
#     return lis
# n = int(input("Enter the end value to find the prime numbers before that: "))
# print(prime(n))


# n = int(input("Enter the end value to find the prime numbers before that: "))
# count = 1
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i%j == 0):
#             count =+1

# if(count == 2):
#     print(i)


# def fa(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fa(n - 1)

# n = int(input("Enter a number to find the factorial of it: "))
# print(fa(n))

# import random
# num_points = 10000
# radius = 1.0
# def is_inside_quarter_circle(x,y,radius):
#     return x**2+y**2 <= radius**2 and x >= 0 and y >= 0
# def estimate_area_quarter_circle(num_points, radius):
#     inside_point = 0
#     for _ in range(num_points):
#         x = random.uniform(0, radius)
#         y = random.uniform(0, radius)
#         if is_inside_quarter_circle(x,y,radius):
#             inside_point += 1
#     area_ratio = inside_point / num_points
#     estimated_area = area_ratio * (radius)**2
#     return estimated_area


# file_name = input()
# with open(file_name, 'r') as file:
#     text = file.read()
# no_of_words = [len(sentence.strip().split())
#                for sentence in text.split('.') if sentence.strip()]
# average_length = sum(no_of_words)/len(text)
# print('Average Sentence Length', average_length)

# def my():
#     return (1,2),(3,4)

# a,b = my()
# print(a)
# print(b)

# write a code for adding of two numbers

import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Example")

# Create a button
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack(pady=203*10)  # Add padding around the button

# Run the main event loop
root.mainloop()
