# List to store roll numbers of students that attended the program
programRoll = []

# Function to take input for roll numbers in list
def attendInput(attendees):
    for i in range(attendees):
        roll = int(input(f"Enter roll number for student {i+1}:\t"))
        programRoll.append(roll)
    print(f"\nRoll numbers of {attendees} students that attended the program are:\t{programRoll}")

# Linear search
def linearSearch(roll_list, roll_search):
    for i in roll_list:
        if i == roll_search:
            return 1
    return -1

# Sentinel search
def sentinelSearch(roll_list, roll_search, n):
    end = roll_list[n - 1]
    roll_list[n - 1] = roll_search
    i = 0
    while roll_list[i] != roll_search:
        i += 1
    roll_list[n - 1] = end
    if i < n - 1 or roll_search == roll_list[n - 1]:
        return 1
    else:
        return -1

# Binary search
def binarySearch(arr, target):
    arr.sort()  # Ensure the list is sorted
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Target element found, return its index
        elif mid_element < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target element not found in the list

# Fibonacci search
def fibonacciSearch(students_attend, search_element, n):
    students_attend.sort()
    fibMMm2 = 0  # (m-2)th Fibonacci number
    fibMMm1 = 1  # (m-1)th Fibonacci number
    fibM = fibMMm2 + fibMMm1  # mth Fibonacci number

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1
    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)

        if students_attend[i] < search_element:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif students_attend[i] > search_element:
            fibM = fibMMm2
            fibMMm1 -= fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    if fibMMm1 and students_attend[offset + 1] == search_element:
        return offset + 1

    return -1

# Main function
def main():
    attendees = int(input("Enter the number of students attending the program:\t"))

    # Input for roll numbers
    attendInput(attendees)

    # Input for roll number to search
    searchAttendee = int(input("\nEnter the roll number you want to search:\t"))

    # Options
    while True:
        print("\n----- CHOOSE SEARCH TYPE -----")
        print("1 -> Linear search")
        print("2 -> Sentinel search")
        print("3 -> Binary search")
        print("4 -> Fibonacci search")
        print("5 -> Exit")
        optn = int(input("\nChoose an option (1-5):\t"))

        if optn == 1:
            result = linearSearch(programRoll, searchAttendee)
            if result == 1:
                print(f"\nRoll number {searchAttendee} attended the program.\n")
            else:
                print(f"\nRoll number {searchAttendee} has either not been added to the list or was absent.\n")

        elif optn == 2:
            result = sentinelSearch(programRoll, searchAttendee, attendees)
            if result == 1:
                print(f"\nRoll number {searchAttendee} attended the program.\n")
            else:
                print(f"\nRoll number {searchAttendee} has either not been added to the list or was absent.\n")

        elif optn == 3:
            result = binarySearch(programRoll, searchAttendee)
            if result == -1:
                print(f"\nRoll number {searchAttendee} has either not been added to the list or was absent.\n")
            else:
                print(f"\nRoll number {searchAttendee} attended the program.\n")

        elif optn == 4:
            result = fibonacciSearch(programRoll, searchAttendee, attendees)
            if result == -1:
                print(f"\nRoll number {searchAttendee} has either not been added to the list or was absent.\n")
            else:
                print(f"\nRoll number {searchAttendee} attended the program.\n")

        elif optn == 5:
            print("\n## END OF CODE\n\n")
            break

        else:
            print("\nPlease choose a valid option (1-5)\n")

# Calling main function
main()
