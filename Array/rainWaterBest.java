int n = height.length;

        int left = 0; int right = n-1;

        int result = 0;

        int maxLeft = 0, maxRight = 0;

        while(left<=right){

            if(height[left] <= height[right]){

                if(height[left] >= maxLeft)

                    maxLeft = height[left];

                else // height[left] < maxLeft

                    result += maxLeft-height[left];

                left++;

            }

            else { //height[right] < height[left]

                if(height[right] >= maxRight)

                    maxRight = height[right];

                else

                    result += maxRight-height[right];

                right--;

            }

        }

        return result;