function cracklePop() {
	for (var i = 1; i <= 100; i++) {
		if (i % 15 === 0) {
			console.log("CracklePop");
		} else if (i % 3 === 0) {
			console.log("Crackle");
		} else if (i % 5 === 0) {
			console.log("Pop");
		} else {
			console.log(i);
		}
	}
}

cracklePop();