
class Item {
 final String name;
 final String unit;
 final int price;
 final String image;

 Item({required this.name, required this.unit, required this.price, required this.image});

 Map toJson() {
   return {
     'name': name,
     'unit': unit,
     'price': price,
     'image': image,
   };
 }
}

List<Item> products = [
 Item(
     name: 'Apple', unit: 'Kg', price: 20, image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Mango',
     unit: 'Doz',
     price: 30,
     image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Banana',
     unit: 'Doz',
     price: 10,
     image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Grapes',
     unit: 'Kg',
     price: 8,
     image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Water Melon',
     unit: 'Kg',
     price: 25,
     image: 'assets/images/flutter_logo.png'),
 Item(name: 'Kiwi', unit: 'Pc', price: 40, image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Orange',
     unit: 'Doz',
     price: 15,
     image: 'assets/images/flutter_logo.png'),
 Item(name: 'Peach', unit: 'Pc', price: 8, image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Strawberry',
     unit: 'Box',
     price: 12,
     image: 'assets/images/flutter_logo.png'),
 Item(
     name: 'Fruit Basket',
     unit: 'Kg',
     price: 55,
     image: 'assets/images/flutter_logo.png'),
];