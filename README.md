# Algorithm-Sorting-Visualization

My code is a Python program that visualizes various sorting algorithms using the matplotlib library. I've implemented several sorting algorithms and a function to animate the sorting process for each algorithm. The program has a command-line interface allowing me to choose which algorithm to visualize. Here are the main components of my code:

Sorting Algorithms: I've implemented the following sorting algorithms in my code: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Shell Sort, Heap Sort, Counting Sort, Radix Sort, Bucket Sort, Cocktail Sort, and Bogosort.

visualize_sorting_algorithm function: This function takes a sorting algorithm, an array, and any additional arguments needed for the specific algorithm. It creates a matplotlib plot and initializes a bar chart representing the array. The function then uses an animation to visualize the sorting process by updating the heights of the bars as the sorting algorithm operates on the input array.

main function: In the main function, I use a while loop to display a menu of available sorting algorithms. The user can choose an algorithm, and the program visualizes it using the visualize_sorting_algorithm function. The loop continues until the user decides to exit the program.

By running this program, I can get a visual representation of how each sorting algorithm works, making it easier to understand their logic and efficiency.
