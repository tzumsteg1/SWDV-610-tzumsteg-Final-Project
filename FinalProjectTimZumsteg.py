#Sets up the program problem, how it is viewed and the instructions for the user
print('This program requires a list of numbers starting at one. It will ask you for the largest number you would like in said list.')
print('For example: If you select 17, the list it starts with will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]')
print()
numberChosen = int(input('Please enter a number you would like to stop the list at. (A great start is the number 15): '))

def choose_one(so_far, nums, squares):
    #un-comment the next line to view the proccess the program runs
    #print(so_far, nums)
    if not nums:
        return so_far
    else:
        for n in nums:
            if not so_far or so_far[-1] + n in squares:
                n2 = nums[::]
                n2.remove(n)
                ans = choose_one(so_far + [n], n2, squares)
                if ans:
                    return ans
                
def square_sum(rmin=1, rmax=numberChosen):
    squares, i = set(), 1
    while i*i < rmax**2:
        squares.add(i*i)
        i += 1
    return choose_one([], list(range(rmin, rmax+1)), squares)

if __name__ == '__main__':
    print()
    print('This program will organize them in an order where any two adjacent numbers is a perfect square')
    print('If the program returns \'None\', there is no possible list.')
    print()
    print('The correct list is: ')
    print(square_sum())