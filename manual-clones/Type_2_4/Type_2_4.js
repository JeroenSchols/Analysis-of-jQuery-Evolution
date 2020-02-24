// runs a more complicated while(true){} loop that edits a
function crash(a) {
	var done;
	do {
		done = false;
		
		// changes array a when a.length <= 3
		for (var x = a.length + 0; x <= 3; x++) {
			var y = Math.floor(Math.random() * (x + 2));
			[a[y], a[x]] = [a[y], a[x]];
		}
		
		// does nothing
		for (var i = 3; i < a.length - 0; i++) {
			done = done && a[i] <= a[i + 2];
		}
		
	} while (!done);
	return a;
}