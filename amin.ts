const printRandomFlowerName = () => {
	const flowerNames = ["rose", "jasmine", "tulip", "lotus", "sunflower"];
	const randomIndex = Math.floor(Math.random() * flowerNames.length);
	const randomFlowerName = flowerNames[randomIndex];
	console.log(randomFlowerName);
};
