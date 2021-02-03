#!/usr/bin/node


const contains_duplicates = function(nums) {
  
  if (nums.length < 2)
        return false
    uniq_num = new Set(nums)
    return(uniq_num.size != nums.length) 
}

console.log(contains_duplicates([3, 1]))