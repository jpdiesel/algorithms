def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    for number in nums:
        if type(number) is not int or number < 0:
            return False 

    seted_nums = set(nums)
    newlist = []
    duplist = []

    if len(seted_nums) == len(nums):
        return False
    else:
        for number in nums:
            if number not in newlist:
                newlist.append(number)
            else:
                duplist.append(number)
        return duplist[0]
