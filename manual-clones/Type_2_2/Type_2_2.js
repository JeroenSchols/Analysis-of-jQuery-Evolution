function sort(a) {
	var done;
	do {
		done = true;
		for (var x = a.length - 1; x > 0; x--) {
			var y = Math.floor(Math.random() * (x + 1));
			[a[x], a[y]] = [a[y], a[x]];
		}
		for (var i = 0; i < a.length - 1; i++) {
			done = done && a[i] <= a[i + 1];
		}
	} while (!done);
	return a;
}