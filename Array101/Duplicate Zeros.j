class Solution {
    public void duplicateZeros(int[] arr) {
        for (int i = arr.length; i>0 ; i--){
            if (arr[i-1] == 0){
                for (int q = arr.length; q>i; q--){
                    arr[q-1] = arr[q-2];

                }
            }
            
        };   
    }
}
