class Solution:
	# @param A : list of integers
	# @return a list of integers
	def plusOne(self, A):
		length = len(A)
		for i in range(length):
			if(A[length-1-i] < 9):
				A[length-1-i] += 1
				return A
			else:
				A[length-1-i] = 0
				if i == length-1:
					A = [1] + A
		return A


solution = Solution()

print(solution.plusOne([9, 9, 9, 9, 9]))
print(solution.plusOne([0]))
print(solution.plusOne([1, 2, 3]))
