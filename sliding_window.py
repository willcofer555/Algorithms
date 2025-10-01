def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_substring_k_distinct(s, k):
    if k == 0 or not s:
        return 0

    char_freq = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1

        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


def min_window_substring(s, t):
    if not s or not t:
        return ""

    target_freq = {}
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1

    required = len(target_freq)
    formed = 0
    window_counts = {}

    left = 0
    min_len = float('inf')
    min_left = 0

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in target_freq and window_counts[char] == target_freq[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            char = s[left]
            window_counts[char] -= 1
            if char in target_freq and window_counts[char] < target_freq[char]:
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


def longest_substring_without_repeating(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
