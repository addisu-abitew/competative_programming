#include <stdlib.h>

int findLeft(int* nums, int left, int right, int target) {
    int ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ans = mid;
            right = mid - 1; // go left
        } else {
            left = mid + 1;
        }
    }
    return ans;
}

int findRight(int* nums, int left, int right, int target) {
    int ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ans = mid;
            left = mid + 1; // go right
        } else {
            right = mid - 1;
        }
    }
    return ans;
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int* ans = malloc(2 * sizeof(int));
    if (!ans) return NULL;

    int left = 0, right = numsSize - 1;
    int found = -1;

    // Step 1: find any occurrence
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            found = mid;
            break;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    *returnSize = 2;

    // Not found
    if (found == -1) {
        ans[0] = ans[1] = -1;
        return ans;
    }

    // Step 2 & 3: search within reduced ranges
    ans[0] = findLeft(nums, 0, found, target);
    ans[1] = findRight(nums, found, numsSize - 1, target);
    return ans;
}