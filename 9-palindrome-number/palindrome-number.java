class Solution {
    public boolean isPalindrome(int x) {
        boolean i = false;
        int y;
        int temp = x;
        int sum = 0;
        while(x > 0){
            y = x % 10;
            sum = (sum * 10) + y;
            x = x / 10;
        }
    if( sum == temp)
      i= true;    
    return i;
    }
}