const combinations = (elements) => {
    if (elements.length === 0) return [ []];
    const firstEl = elements[0];
    const rest = elements.slice(1);

    const combsWithoutFirst = combinations(rest);
    const combsWithFirst = [];

    combsWithoutFirst.forEach( comb => {
        const combWithFirst = [...comb, firstEl];
        combsWithFirst.push(combWithFirst)
        console.log(comb, combWithFirst, combsWithFirst)
    });

    return [...combsWithoutFirst, ...combsWithFirst]
}

console.log(combinations(['a', 'b', 'c']))
