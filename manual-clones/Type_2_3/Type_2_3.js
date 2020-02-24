// sorts an array in O(inf) time
function bogo_sort(a) {
	let done;
	do {
		done = true;
        // shuffles the array
		for (let x = a.length - 1; x > 0; x--) {
			let y = Math.floor(Math.random() * (x + 1));
			[a[x], a[y]] = [a[y], a[x]];
		}
        // checks whether the array is sorted
		for (let i = 0; i < a.length - 1; i++) {
			done = done && a[i] <= a[i + 1];
		}
	} while (!done);
	return a;
}