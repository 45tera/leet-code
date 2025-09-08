class Solution {
    
    //O(2) solution
    public int maxArea(int[] height) {
        int size = height.length;
        int maxWater = 0;
        int lastP = size - 1; // x of the lastP
        //more equal than last one?
        for (int i = 0; i < size; i++) {
            for (int q = lastP; q >= 0; q--) {
                int length = q - i;
                int width;

                if (height[q] >= height[i]) {
                    width = height[i];
                } else {
                    width = height[q];
                }

                if (width * length > maxWater) {

                    maxWater = width * length;
                }
            }

        }

        return maxWater;

    }

    //O(n)
    public int maxArea_n(int[] height) {
        int size = height.length;
        int maxWater = 0;
        int lastP = size - 1; // x of the lastP
        int firstP = 0;
        while (firstP <lastP){
            int h1 = height[firstP];
            int h2 = height[lastP];

            int x = lastP- firstP;
            int y;
            if(h1 <= h2){
                y= h1;
            }
            else{
                y =h2;
            }

            int prospective = x* y;
            if(prospective > maxWater){
                maxWater = prospective;
            }

            if (h1 < h2){
                firstP++;
            }
            else{
                lastP--;
            }
        }

        return maxWater;

    }
}