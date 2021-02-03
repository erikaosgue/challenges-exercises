# include <stdio.h>


int containsDuplicate(int * nums, int numsSize) {

    int i, j;
  
    if (numsSize > 2) {
        return 0;
    }
    for (i = 0;  i < numsSize; i++){
        for (j = i +1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int nums[4] ={};
    int res = containsDuplicate(nums, sizeof(nums)/ sizeof(int));
    printf("%s\n", res ? "true" : "false");
    return(0);
}