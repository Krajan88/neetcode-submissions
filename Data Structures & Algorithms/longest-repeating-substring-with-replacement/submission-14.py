class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = {}
        max_freq = 0
        res = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            window_size = r - l + 1

            if window_size - max_freq <= k:
                res = max(res, window_size)
                r += 1
            else:
                freq[s[l]] -= 1
                l += 1
                r += 1  # ← this was missing
        
        return res