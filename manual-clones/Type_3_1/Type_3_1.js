function sort(array) {
	var isSorted;
    var numIterations = 0;
	do {
		isSorted = true;
		for (var i = array.length - 1; i > 0; i--) {
			var j = Math.floor(Math.random() * (i + 1));
			[array[i], array[j]] = [array[j], array[i]];
		}
        numIterations++;
		for (var step = 0; step < array.length - 1; step++) {
			isSorted = isSorted && array[step] <= array[step + 1];
		}
	} while (!isSorted);
	console.log("sorting " + array + " took " + numIterations + " iterations");
	return array;
}