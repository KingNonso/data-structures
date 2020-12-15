// return any way in which targetSum is gotten by summing any element of the array

const howSum = (targetSum, arr, memo={}) => {
  if(targetSum in memo) return memo[targetSum];
  if(targetSum === 0) return [];
  if(targetSum < 0) return null;

  for (let i of arr){
    const remainder = targetSum - i;
    memo[targetSum] = howSum(remainder, arr, memo);
    if (memo[targetSum] !== null){
      return [...memo[targetSum], i];
    }
  }

  return null;
}


console.log(howSum(7, [2,3]))
console.log(howSum(7, [5,3,4,7]))
console.log(howSum(7, [2,4]))
console.log(howSum(8, [2,3,5]))
console.log(howSum(300, [7,14]))

