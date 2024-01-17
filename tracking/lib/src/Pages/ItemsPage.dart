import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:tracking/src/Model/DBHelper.dart';
import 'package:tracking/src/Model/cart_model.dart';
import 'package:tracking/src/Model/item_model.dart';
import 'package:tracking/src/Provider/CartProvider.dart';


class ItemsPage extends StatelessWidget { 
  const ItemsPage({Key? key}) : super(key: key); 

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
  } 
} 
