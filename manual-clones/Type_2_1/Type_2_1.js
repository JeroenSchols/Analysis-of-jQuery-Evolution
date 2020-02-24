function sort(array) {
	let isSorted;
	do {
		isSorted = true;
		for (let i = array.length - 1; i > 0; i--) {
			let j = Math.floor(Math.random() * (i + 1));
			[array[i], array[j]] = [array[j], array[i]];
		}
		for (let step = 0; step < array.length - 1; step++) {
			isSorted = isSorted && array[step] <= array[step + 1];
		}
	} while (!isSorted);
	return array;
}