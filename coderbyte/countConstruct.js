// Count the number of ways, a target can be generated from a string

const countConstruct = (target, words, memo={}) => {
  if(target in memo) return memo[target];
  if(target === '') return 1;

  let total = 0;

  for(let word of words){
    if(target.indexOf(word) === 0){
      const suffix = target.slice(word.length);
      const numWays = countConstruct(suffix, words, memo);
      total += numWays;
    }

  }
  // console.log(memo);
  memo[target] = total;
  return total;

}
console.log(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) // 1
console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) // 2
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) // 0
console.log(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) // 4
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
  'e',
  'ee',
  'eee',
  'eeee',
  'eeeee',
  'eeeeee'
])) // 0




