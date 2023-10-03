def get_biggest(nums: list) -> int:
	if not nums:
		return -1

	nums = tuple(map(str, nums))
	list_index_nums = [*range(len(nums))]
	l = [list_index_nums[i:] + list_index_nums[:i] for i in list_index_nums]

	def my_func(l, f):
		return [k[:f] + k[f:][i:] + k[f:][:i] for k in l for i in range(1, len(k[f:]))]

	for f in list_index_nums[1:]:
		l.extend(my_func(l, f))

	res = [int(''.join([nums[i] for i in ii])) for ii in l]
	return max(res)