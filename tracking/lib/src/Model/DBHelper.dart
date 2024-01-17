<<<<<<< HEAD
import 'package:shared_preferences/shared_preferences.dart';
=======
>>>>>>> 318cc33 (add items page and cart handling)
import 'package:sqflite/sqflite.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart';
import 'dart:io' as io;
import 'package:tracking/src/Model/cart_model.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

class DBHelper {
  static Database? _database;

  Future<Database?> get database async {
    if (_database != null) {
      return _database!;
    }
    _database = await initDatabase();
    return null;
  }

  initDatabase() async {
    io.Directory directory = await getApplicationDocumentsDirectory();
    String path = join(directory.path, 'cart.db');
    databaseFactory = databaseFactoryFfi;
    var db = await openDatabase(path, version: 1, onCreate: _onCreate);
    return db;
  }
  // creating database table
  _onCreate(Database db, int version) async {
    await db.execute(
        'CREATE TABLE cart(id INTEGER PRIMARY KEY, productId VARCHAR UNIQUE, productName TEXT, initialPrice INTEGER, productPrice INTEGER, quantity INTEGER, unitTag TEXT, image TEXT)');
  }
<<<<<<< HEAD

  // inserting data into the table
  Future<Object> insert(Cart cart) async {
=======
  // inserting data into the table
  Future<Cart> insert(Cart cart) async {
>>>>>>> 318cc33 (add items page and cart handling)
    var dbClient = await database;
    try {
      await dbClient?.insert('cart', cart.toMap()) ?? [];
      return cart;
    } catch (e) {
<<<<<<< HEAD
        var queryResult = await dbClient?.query('cart') ?? [];
        var available_cart  = queryResult.map((result) => Cart.fromMap(result)).toList();
        var index = available_cart.indexWhere((element) => element.id == cart.id);
        available_cart[index].quantity!.value = available_cart[index].quantity!.value + 1;
        return await dbClient!.update('cart', available_cart[index].quantityMap(),
          where: "productId = ?", whereArgs: [available_cart[index].productId]);
    }
=======
      print(e);
      return cart;
    }

>>>>>>> 318cc33 (add items page and cart handling)
  }
  // getting all the items in the list from the database
  Future<List<Cart>> getCartList() async {
    var dbClient = await database;
    final List<Map<String, Object?>> queryResult =
        await dbClient?.query('cart') ?? [];
    return queryResult.map((result) => Cart.fromMap(result)).toList();
  }
  Future<int> updateQuantity(Cart cart) async {
  var dbClient = await database;
  return await dbClient!.update('cart', cart.quantityMap(),
      where: "productId = ?", whereArgs: [cart.productId]);
  }

  // deleting an item from the cart screen
  Future<int> deleteCartItem(int id) async {
    var dbClient = await database;
    return await dbClient!.delete('cart', where: 'id = ?', whereArgs: [id]);
  }
<<<<<<< HEAD

  Future<int> addItemQuantity(int index) async {
    var dbClient = await database;
    var queryResult = await dbClient?.query('cart') ?? [];
    var available_cart  = queryResult.map((result) => Cart.fromMap(result)).toList();
    available_cart[index].quantity!.value = available_cart[index].quantity!.value + 1;
    return await dbClient!.update('cart', available_cart[index].quantityMap(),
          where: "productId = ?", whereArgs: [available_cart[index].productId]);
  }
  Future<int> removeItemQuantity(int index) async {
    var dbClient = await database;
    var queryResult = await dbClient?.query('cart') ?? [];
    var available_cart  = queryResult.map((result) => Cart.fromMap(result)).toList();
    available_cart[index].quantity!.value = available_cart[index].quantity!.value - 1;
    return await dbClient!.update('cart', available_cart[index].quantityMap(),
          where: "productId = ?", whereArgs: [available_cart[index].productId]);
  }
=======
>>>>>>> 318cc33 (add items page and cart handling)
}