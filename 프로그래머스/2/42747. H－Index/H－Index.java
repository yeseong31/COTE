import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        for (int h = citations.length; h >= 1; h--) {
            if (citations[citations.length - h] >= h) {
                return h;
            }
        }
        
        return 0;
    }
}