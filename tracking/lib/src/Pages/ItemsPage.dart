import 'package:flutter/material.dart';
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 318cc33 (add items page and cart handling)
import 'package:provider/provider.dart';
import 'package:tracking/src/Model/DBHelper.dart';
import 'package:tracking/src/Model/cart_model.dart';
import 'package:tracking/src/Model/item_model.dart';
import 'package:tracking/src/Provider/CartProvider.dart';
<<<<<<< HEAD
=======
>>>>>>> d74cf61 (initial app contains screens and pages and navbar and side menu)
=======
>>>>>>> 318cc33 (add items page and cart handling)


class ItemsPage extends StatelessWidget { 
  const ItemsPage({Key? key}) : super(key: key); 
<<<<<<< HEAD
<<<<<<< HEAD

  @override 
  Widget build(BuildContext context) {
    final cart = Provider.of<CartProvider>(context);
    void saveData(int index) {
    var dbHelper = DBHelper();
      dbHelper.insert(
      Cart(
        id: index,
        productId: index.toString(),
        productName: products[index].name,
        initialPrice: products[index].price,
        productPrice: products[index].price,
        quantity: ValueNotifier(1),
        unitTag: products[index].unit,
        image: products[index].image,
      ),
    ).then((value) {
      cart.addTotalPrice(products[index].price.toDouble());
      cart.addCounter();
      print('Product Added to cart');
    }).onError((error, stackTrace) {
      print(error.toString());
    });
    }
    return ListView.builder(
      padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 8.0),
      shrinkWrap: true,
      itemCount: products.length,
      itemBuilder: (context, index) {
        return Card(
          color: Colors.white,
          elevation: 5.0,
          child: Padding(
            padding: const EdgeInsets.all(4.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: [
                Image(
                  height: 80,
                  width: 80,
                  image: AssetImage(products[index].image.toString()),
                ),
                SizedBox(
                  width: 130,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const SizedBox(
                        height: 5.0,
                      ),
                      RichText(
                        overflow: TextOverflow.ellipsis,
                        maxLines: 1,
                        text: TextSpan(
                            text: 'عنوان: ',
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].name.toString()}\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                      RichText(
                        maxLines: 1,
                        text: TextSpan(
                            text: 'واحد: ',
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].unit.toString()}\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                      RichText(
                        maxLines: 1,
                        text: TextSpan(
                            text: 'قیمت: ',
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].price.toString()} تومان\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                    ],
                  ),
                ),
                ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.redAccent),
                    onPressed: () {
                      saveData(index);
                      ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        backgroundColor: Colors.blueAccent,
                        content: Text('اضافه شد'),
                        duration: Duration(seconds: 2),
                      ));
                    },
                    child: const Text('افزودن به سبد',
                      style: TextStyle(color: Colors.white),
                    )),
              ],
            ),
          ),
        );
      }
    );
=======
  
  @override 
  Widget build(BuildContext context) { 
    return Container( 
      color: const Color(0xffC4DFCB), 
      child: Center( 
        child: Text( 
          "Page Number 5", 
          style: TextStyle( 
            color: Colors.green[900], 
            fontSize: 45, 
            fontWeight: FontWeight.w500, 
          ), 
        ), 
      ), 
    ); 
>>>>>>> d74cf61 (initial app contains screens and pages and navbar and side menu)
=======

  @override 
  Widget build(BuildContext context) {
    final cart = Provider.of<CartProvider>(context);
    void saveData(int index) {
    var dbHelper = DBHelper();
      dbHelper.insert(
      Cart(
        id: index,
        productId: index.toString(),
        productName: products[index].name,
        initialPrice: products[index].price,
        productPrice: products[index].price,
        quantity: ValueNotifier(1),
        unitTag: products[index].unit,
        image: products[index].image,
      ),
    ).then((value) {
      cart.addTotalPrice(products[index].price.toDouble());
      cart.addCounter();
      print('Product Added to cart');
    }).onError((error, stackTrace) {
      print(error.toString());
    });
    }
    return ListView.builder(
      padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 8.0),
      shrinkWrap: true,
      itemCount: products.length,
      itemBuilder: (context, index) {
        return Card(
          color: Colors.blueGrey.shade200,
          elevation: 5.0,
          child: Padding(
            padding: const EdgeInsets.all(4.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: [
                Image(
                  height: 80,
                  width: 80,
                  image: AssetImage(products[index].image.toString()),
                ),
                SizedBox(
                  width: 130,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const SizedBox(
                        height: 5.0,
                      ),
                      RichText(
                        overflow: TextOverflow.ellipsis,
                        maxLines: 1,
                        text: TextSpan(
                            text: 'Name: ',
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].name.toString()}\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                      RichText(
                        maxLines: 1,
                        text: TextSpan(
                            text: 'Unit: ',
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].unit.toString()}\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                      RichText(
                        maxLines: 1,
                        text: TextSpan(
                            text: 'Price: ' r"$",
                            style: TextStyle(
                                color: Colors.blueGrey.shade800,
                                fontSize: 16.0),
                            children: [
                              TextSpan(
                                  text:
                                      '${products[index].price.toString()}\n',
                                  style: const TextStyle(
                                      fontWeight: FontWeight.bold)),
                            ]),
                      ),
                    ],
                  ),
                ),
                ElevatedButton(
                    style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.blueGrey.shade900),
                    onPressed: () {
                      saveData(index);
                    },
                    child: const Text('Add to Cart')),
              ],
            ),
          ),
        );
      }
    );
>>>>>>> 318cc33 (add items page and cart handling)
  } 
} 
