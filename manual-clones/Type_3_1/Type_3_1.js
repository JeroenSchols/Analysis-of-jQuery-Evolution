function sort(array) {
	var isSorted;
    console.log(array)
	do {
		isSorted = true;
		for (var i = array.length - 1; i > 0; i--) {
			var j = Math.floor(Math.random() * (i + 1));
			[array[i], array[j]] = [array[j], array[i]];
		}
        console.log(array)
		for (var step = 0; step < array.length - 1; step++) {
			isSorted = isSorted && array[step] <= array[step + 1];
		}
        console.log("is sorted: " + isSorted)
	} while (!isSorted);
	return array;
}