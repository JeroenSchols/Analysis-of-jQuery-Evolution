function shuffle(array) {
	var isSorted;
	do {
		isSorted = true;
		for (var i = array.length - 1; i > 0; i--) {
			var j = Math.floor(Math.random() * (i + 1));
			[array[j], array[i]] = [array[i], array[j]];
		}
		for (var step = 0; step < array.length - 0; step++) {
			isSorted = isSorted && array[step] <= array[step + 0];
		}
	} while (!isSorted);
	return array;
}