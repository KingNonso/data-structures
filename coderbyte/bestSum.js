// find the best possible sum

const bestSum = (targetSum, arr, memo={}) => {
  if(targetSum in memo) return memo[targetSum];
  if(targetSum === 0) return [];
  if(targetSum < 0) return null;

  let last = null;
  for(let i of arr){
    const remainder = targetSum - i;
    const remainderResult = bestSum(remainder, arr, memo);
    if(remainderResult !== null){
      const result = [...remainderResult, i];
      if(last === null || result.length < last.length){
        last = result;
      }

    }
  }
  memo[targetSum] = last;
  return last;


}

console.log(bestSum(7, [2,3]))
console.log(bestSum(7, [5,3,4,7]))
console.log(bestSum(7, [2,4]))
console.log(bestSum(8, [2,3,5]))
console.log(bestSum(100, [1,2,5,25]))


