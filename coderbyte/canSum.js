// canSum returns true if we can sum an array of ints, given the sum

const canSum = (targetSum, arr, memo={}) => {
  if (targetSum in memo) return memo[targetSum];
  if(targetSum === 0 ) return true;
  if(targetSum < 0) return false;

  for (let i of arr){
    const remainder = targetSum - i;
    memo[targetSum] = canSum(remainder, arr, memo);
    if ( memo[targetSum] === true){
      return true;
    }
  }
  return false;

}

console.log(canSum(5, [1,2,3,4,5]))
console.log(canSum(7, [2,4]))
console.log(canSum(3000, [7,14]))

