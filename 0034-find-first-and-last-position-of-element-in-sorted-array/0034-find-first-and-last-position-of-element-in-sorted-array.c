/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int findLeft(int* nums, int start, int end, int target);
int findRight(int* nums, int start, int end, int target);

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int start = 0, end = numsSize - 1;
    int *ans = malloc(2 * sizeof(int));
    if (!ans) return NULL;

    ans[0] = -1;
    ans[1] = -1;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            ans[0] = findLeft(nums, start, mid, target);
            ans[1] = findRight(nums, mid, end, target);
            break;
        } else if (nums[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }

    *returnSize = 2;
    return ans;
}

int findLeft(int* nums, int start, int end, int target) {
    int ans = -1;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            ans = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return ans;
}

int findRight(int* nums, int start, int end, int target) {
    int ans = -1;
    while (start <= end) {
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            ans = mid;
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return ans;
}
