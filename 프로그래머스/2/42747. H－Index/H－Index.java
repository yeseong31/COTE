import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        for (int h = citations.length; h >= 1; h--) {
            if (check(citations, h)) {
                return h;
            }
        }
        
        return 0;
    }
    
    private boolean check(int[] citations, int h) {
        return citations[citations.length - h] >= h;
    }
}
