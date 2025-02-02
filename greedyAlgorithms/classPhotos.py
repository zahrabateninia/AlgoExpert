# arrange students in two rows before taking the photo
# Each row should contain the same num of the students and should adhere to the following guidelines:
# 1. All students wearing red shirts must be in the same row
# 2. All students wearing blue shirts must be in the same row
# 3. Each student in the back row must be strictly taller than the student directly in front of them in the front row

# sample input: redShirtHeights = [5, 8, 1, 3, 4] , blueShirtHeights = [6, 9, 2, 4, 5]
# sample output: true 

# greedy choice: each time pick up the hardest student to place ( the tallest one)


# O(n Logn) T | O(1) S

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

