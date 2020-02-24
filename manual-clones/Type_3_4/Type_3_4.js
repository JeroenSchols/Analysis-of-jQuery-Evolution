function sort(array) {
	do {
        shuffle(array);
	} while (!checkSorted(array));
	return array;
}

function shuffle(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
		[array[i], array[j]] = [array[j], array[i]];
	}
}

function checkSorted(array) {
    var isSorted = true;
    for (var step = 0; step < array.length - 1; step++) {
        isSorted = isSorted && array[step] <= array[step + 1];
    }
    return isSorted;
}